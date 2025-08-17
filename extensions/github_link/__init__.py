"""
* přidává proměnnou kontextu github_link(režim): poskytuje URL (v příslušném režimu)
současný dokument na GitHubu
* pokud je aktivní sphinx.ext.linkcode, automaticky vytváří odkaz na GitHub
odkazy (pomocí nastavení config.linkcode_resolve)

Nastavení
========

* „github_user“, uživatelské jméno nebo organizace, pod kterou projekt žije
* „github_project“, název projektu na GitHub
* (volitelné) „verze“, odkaz na větvení Githubu (výchozí hodnota: master)

Poznámky
=====

* funkce „linkcode_resolve“ podporuje pouze doménu Python
* generuje https odkazy na GitHub
* výslovně dováží „odoo“, takže je k ničemu pro nikoho jiného
"""

import importlib
import inspect
import os.path

import contextlib
from urllib.parse import urlunsplit


def setup(app):
    app.add_config_value('github_user', None, 'env')
    app.add_config_value('github_project', None, 'env')
    app.connect('html-page-context', add_doc_link)

    def linkcode_resolve(domain, info):
        """Vyřešené objekty jsou přiřazeny k odpovídajícímu URL na GitHubu."""
        # Dokončeno:
        if domain != 'py':
            return None

        if not (app.config.github_user and app.config.github_project):
            return None

        module, fullname = info['module'], info['fullname']
        # TODO: atributy a vlastnosti nemají moduly, možná by se mělo zkusit hledat
        #       jejich cacheované hostitelské objektu?
        if not module:
            return None

        obj = importlib.import_module(module)
        for item in fullname.split('.'):
            obj = getattr(obj, item, None)

        if obj is None:
            return None

        # získat originál z ozdobených metod
        with contextlib.suppress(AttributeError):
            obj = obj._orig

        try:
            obj_source_path = inspect.getsourcefile(obj)
            _, line = inspect.getsourcelines(obj)
        except (TypeError, OSError):
            # obj nemá modul nebo něco podobného
            return None

        # FIXME: udělat hledání kořenového projektu nezávislým na projektu
        if module.startswith('odoo.upgrade.util'):
            from odoo.upgrade import util
            project = 'upgrade-util'
            project_root = os.path.join(os.path.dirname(util.__file__), '../..')
        else:
            import odoo
            project = 'odoo'
            project_root = os.path.join(os.path.dirname(odoo.__file__), '..')
        return make_github_link(
            app,
            project=project,
            path=os.path.relpath(obj_source_path, project_root),
            line=line,
        )
    app.config.linkcode_resolve = linkcode_resolve

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }

def make_github_link(app, project, path, line=None, mode="blob"):
    branch = app.config.version or 'master'
    if project == 'upgrade-util':
        branch = 'master'

    urlpath = f"/{app.config.github_user}/{project}/{mode}/{branch}/{path}"
    return urlunsplit((
        'https',
        'github.com',
        urlpath,
        '',
        '' if line is None else 'L%d' % line
    ))


def add_doc_link(app, pagename, templatename, context, doctree):
    """Přidat funkci github_link, která odkazuje na aktuální stránku (.rst) na GitHub"""
    if not app.config.github_user and app.config.github_project:
        return

    # FIXME: najít jiný způsob, jak se vrátit ke zdrojovému souboru
    # Ve verzi Sphinx 1.3 je možné mít více zdrojových přípon, a
    # Mohou být v budoucnu užitečné
    source_suffix = app.config.source_suffix
    source_suffix = next(iter(source_suffix))
    context['github_link'] = lambda mode='edit': make_github_link(
        app, project=app.config.github_project, path=f'content/{pagename}{source_suffix}', mode=mode)
