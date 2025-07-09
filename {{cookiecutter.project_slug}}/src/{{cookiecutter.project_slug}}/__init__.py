"""Top-level package for {{ cookiecutter.project_name }}."""

__all__ = [
    '__version__',
    '__author__',
    '__email__',
    'cli',
    'health',
]

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

from .__pre_init__ import cli
from health import *