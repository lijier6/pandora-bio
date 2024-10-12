# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from pandora import version

setup(
	name='pandora-microbiome',
	version=version.__version__,
	description='pandora, a collection of handy functions.',
	url='https://github.com/lijierr/pandora',
	author=version.__author__,
	author_email=version.__email__,

	classifiers=[
				'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
				'Programming Language :: Python :: 3 :: Only',
				'Operating System :: Unix',
	],
	keywords='biology bioinformatics',
	scripts=['bin/pandora'],
	# packages = find_packages(),
	packages=['pandora'],
	include_package_data=True,
	python_requires='>=3.6',
	install_requires=['hellokit>=0.1.0', ],
)
