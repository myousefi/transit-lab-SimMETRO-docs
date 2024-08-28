# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pygments


project = "TransitLab SimMETRO"
subtitle = "A Modern Rail Transit Simulation Platform"
copyright = "2024, Transit Mobility Lab"
author = "Mojtaba Yousefi"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
highlight_language = "python"

html_static_path = ["_static"]

extensions = [
    "sphinxcontrib.bibtex",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
]
bibtex_bibfiles = ["refs.bib"]

html_css_files = [
    "custom.css",
]
highlight_options = {"linenos": True}

html_theme_options = {
    "code_font_size": "0.8em",
    "code_font_family": "Consolas, 'Courier New', monospace",
}

pygments_style = "friendly"

viewcode_follow_imported_members = True
viewcode_enable_epub = True

latex_elements = {
    "preamble": r"""
\usepackage{listings}
\lstset{
    basicstyle=\small\ttfamily,
    breaklines=true,
    breakatwhitespace=true,
    frame=single,
    showstringspaces=false,
    columns=flexible
}
""",
}

autodoc_class_signature = "separated"


def setup(app):
    app.add_css_file("custom.css")
