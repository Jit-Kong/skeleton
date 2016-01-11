try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'mygame',
    'author': 'kxl',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'kxl8368@126.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'mygame'
}

setup(**config)
