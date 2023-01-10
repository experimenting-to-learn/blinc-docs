# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BLINC'
copyright = 'BLINC Team'
author = 'BLINC Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.redoc',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'kr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

redoc = [
    {
        'name': 'Batcomputer API',
        'page': 'api',
        'spec': 'specs/github.yml',
        'embed': True,
    },
    {
        'name': 'Example API',
        'page': 'example/index',
        'spec': 'http://example.com/openapi.yml',
        'opts': {
            'required-props-first': True,
            'expand-responses': ["200", "201"],
        }
    },
]