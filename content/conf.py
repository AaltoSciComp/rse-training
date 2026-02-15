# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Aalto RSE training'
copyright = '2026, The contributors'
author = 'The contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_lesson',
              'sphinx_rtd_theme_ext_color_contrast',
              'sphinx_aaltoscicomp_branding',
              'sphinx.ext.intersphinx',
              ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


intersphinx_mapping = {
    'scicomp': ('https://scicomp.aalto.fi/', None),
    'manuals': ('https://coderefinery.github.io/manuals/', None),
    }
intersphinx_disabled_reftypes = [ ]
