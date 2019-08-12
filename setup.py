import sys

try:
    from setuptools import setup
    using_setuptools = True
except ImportError:
    from distutils.core import setup
    using_setuptools = False

from os.path import join, dirname

with open(join(dirname(__file__), 'scrapydartx/VERSION')) as f:
    version = f.read().strip()

setup_args = {
    'name': 'scrapydartx',
    'version': version,
    'url': 'https://github.com/GuardianGH/scrapydartx',
    'description': 'a extension from ScrapydArt with added automatic scheduling and automatically stop the abnormal crawlers functions',
    'long_description': open('README.rst', encoding="utf-8").read(),
    'author': 'Scrapy developers',
    'author_email': 'zhling2012@live.com',
    'maintainer': 'Scrapy developers',
    'maintainer_email': 'info@scrapy.org',
    'license': 'BSD',
    'packages': ['scrapydartx'],
    'include_package_data': True,
    'zip_safe': False,
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Internet :: WWW/HTTP',
    ],
}


if using_setuptools:
    setup_args['install_requires'] = [
        'Twisted>=8.0',
        'Scrapy>=1.0',
        'six',
        'enum-compat',
    ]
    setup_args['entry_points'] = {'console_scripts': [
        'scrapydartx = scrapydartx.scripts.scrapyd_run:main'
    ]}
else:
    setup_args['scripts'] = ['scrapydartx/scripts/scrapyd_run.py']

setup(**setup_args)
