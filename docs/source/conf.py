# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example_pkg'
copyright = '2023, Rick Staa'
author = 'Rick Staa'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
extensions = [
    "autoapi.extension",  # Generate API documentation from code.
    "sphinx.ext.autodoc",  # Include documentation from docstrings.
]
autoapi_dirs = [
    "../../pkg_a",
    "../../pkg_b",
]

# Extensions settings

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
