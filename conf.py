# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import shutil
import os

project = 'codeinfo'
copyright = '2024, sanjay'
author = 'sanjay'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

new_dir_path_recursive = 'readthedocs'
os.makedirs(new_dir_path_recursive, exist_ok=True)

# Specify the source and destination directories
source_directory = '_build/html'
destination_directory = 'readthedocs/html'

# Copy the directory and its contents
shutil.copytree(source_directory, destination_directory)



# Create a directory named "my_new_dir" in the current working directory

