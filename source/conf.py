# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ascendia Docs'
copyright = '''2025 Ascendia Group. All rights reserved. Developed by the Ascendia Dev Team. 
Operated and maintained by the Ascendia Minecraft Server Division.'''
author = 'Ascendia Dev Team & Ascendia Minecraft Server Group '
release = 'V1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'
html_show_sphinx = False
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_show_sphinx = False

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
