# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Aalto RSE training'
html_title = project
copyright = '2026, The contributors'
author = 'The contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_lesson',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx_aaltoscicomp_branding',
    'sphinx.ext.intersphinx',
    'sphinx_misc_rkdarst.site_map',
]

templates_path = ['_templates']
exclude_patterns = []

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "colon_fence",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    "prev_next_buttons_location": False,
    "style_external_links": True,
#    "collapse_navigation": True,
#    "navigation_depth": 2
}
html_css_files = [
    "theme_overrides.css",
]
html_context = {
    #"github_url": "https://github.com/AaltoSciComp/rse-training/"
    "display_github": True,
    "github_user": "AaltoSciComp",
    "github_repo": "rse-training",
    "github_version": "main",
    "conf_py_path": "/content/",
}


latex_engine = 'xelatex'
latex_toplevel_sectioning = 'chapter'  # 'part' | 'chapter' | 'section'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_theme = 'manual'


intersphinx_mapping = {
    'scicomp': ('https://scicomp.aalto.fi/', None),
    'manuals': ('https://coderefinery.github.io/manuals/', None),
    }
intersphinx_disabled_reftypes = [ ]
