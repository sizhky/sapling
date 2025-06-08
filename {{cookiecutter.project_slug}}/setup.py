#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    'Click>=7.0',
    {%- endif %}
    {%- if cookiecutter.command_line_interface|lower == 'typer' %}
    'typer>=0.6.0',
    {%- endif %}
]

test_requirements = [
    {%- if cookiecutter.use_pytest == 'y' %}
    'pytest>=6.0',
    {%- endif %}
]

setup(
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        {%- if cookiecutter.open_source_license == 'MIT license' %}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.open_source_license == 'BSD license' %}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.open_source_license == 'ISC license' %}
        'License :: OSI Approved :: ISC License (ISCL)',
        {%- elif cookiecutter.open_source_license == 'Apache Software License 2.0' %}
        'License :: OSI Approved :: Apache Software License',
        {%- elif cookiecutter.open_source_license == 'GNU General Public License v3' %}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    {%- if cookiecutter.command_line_interface|lower == 'typer' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:app',
        ],
    },
    {%- endif %}
    install_requires=requirements,
    {%- if cookiecutter.open_source_license == 'MIT license' %}
    license="MIT license",
    {%- elif cookiecutter.open_source_license == 'BSD license' %}
    license="BSD license",
    {%- elif cookiecutter.open_source_license == 'ISC license' %}
    license="ISC license",
    {%- elif cookiecutter.open_source_license == 'Apache Software License 2.0' %}
    license="Apache Software License 2.0",
    {%- elif cookiecutter.open_source_license == 'GNU General Public License v3' %}
    license="GNU General Public License v3",
    {%- endif %}
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
