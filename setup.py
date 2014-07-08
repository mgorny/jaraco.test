#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

setup_params = dict(
	name='jaraco.test',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	url="https://bitbucket.org/jaraco/jaraco.test",
	packages=setuptools.find_packages(),
	namespace_packages=['jaraco'],
	zip_safe=False,
	install_requires=[
		'jaraco.util',
		'six',
		'path.py',
	],
	setup_requires=[
		'hgtools',
		'pytest-runner',
	],
	tests_require=[
		'pytest',
		'mock',
	],
	entry_points={
		'pytest11': [
			'MongoDB = jaraco.test.mongodb',
		],
	}
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
