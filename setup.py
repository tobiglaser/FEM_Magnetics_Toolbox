#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

# with open('requirements.txt', 'r') as f:
#     requirements = f.read().splitlines()

setup_requirements = ['setuptools_scm']

test_requirements = []

setup(
    author="LEA - Uni Paderborn",
    author_email='upblea@mail.upb.de',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X'
    ],
    description="FEM Magnetics Toolbox",
    install_requires=['pandas~=2.2.1',
                      'numpy~=1.26.0',
                      'matplotlib~=3.8.0',
                      'gmsh>=4.13.1',
                      'onelab>=1.0',
                      'scipy~=1.12.0',
                      'pytest',
                      'pycodestyle',
                      'PyQt5>=5.15.6',
                      'mplcursors>=0.5.1',  # TODO Is this necessary?
                      'deepdiff>=6.2.1',  # comparing result dicts for pytests
                      'materialdatabase==0.3.0',
                      'optuna',
                      'plotly',
                      'mag-net-hub',
                      'tqdm'],
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='femmt',
    name='femmt',
    packages=find_packages(include=['femmt', 'femmt.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={},
    url='https://github.com/upb-lea/FEM_Magnetics_Toolbox',
    project_urls={
        "Documentation": "https://upb-lea.github.io/FEM_Magnetics_Toolbox/main/intro.html",
        "Source Code": "https://github.com/upb-lea/FEM_Magnetics_Toolbox",
    },
    version='0.5.4',
    zip_safe=False,
    data_files=[('', ['CHANGELOG.md'])]
)
