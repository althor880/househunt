from setuptools import setup
setup(
    name = 'househunt',
    packages = ['househunt'],
    install_requires=[
        'requests',
        'xmltodict',
        'tinydb',
        'lxml',
    ],
    version = '0.5',
    description = 'Python module to search Redfin and combine with results from the Zillow API',
    author = 'AlThor880',
    author_email = 'althor880@gmail.com',
    url = 'https://github.com/althor880/househunt',
    download_url = 'https://github.com/althor880/househunt/tarball/0.5',
    keywords = ['house', 'realty', 'zillow', 'redfin', 'api'],
    classifiers = [],
)
