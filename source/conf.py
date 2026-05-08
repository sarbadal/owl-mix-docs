import os
import sys
sys.path.insert(0, os.path.abspath('..'))


project = 'owlmix-dev'
copyright = '2026, Sarbadal Pal'
author = 'Sarbadal Pal'

extensions = [
    'sphinx.ext.autodoc',
    # ... other extensions
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'display_version': False,  # For older theme versions
    'version_selector': False, # For newer theme versions
}
 
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_show_sphinx = False
html_copy_source = False

