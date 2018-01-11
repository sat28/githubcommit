from githubcommit.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'githubcommit',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "githubcommit",
        "src": "static",
        "require": "githubcommit/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
