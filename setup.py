#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

VERSION = '0.1'
URL='https://git.paradigmadigital.com/ansible/programansible/'

setup(name='programansible',
      version=VERSION,
      description='Class to make it easier to execute playbooks from Python.',
      author='Àlex Pérez-Pujol',
      author_email='alexperez@paradigmadigital.com',
      url=URL,
      download_url=URL + 'repository/archive.tar.gz?ref=' + VERSION,
      license="GPLv3",
      packages=['programansible'],
      package_dir={'programansible': 'programansible'},
      install_requires=[
          "ansible>=2.3.1.0",
          "pyyaml>=3.12",
          ],
      )
