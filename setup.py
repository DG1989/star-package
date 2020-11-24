from setuptools import setup
import os

def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
    name='starrecommender',
    version='0.0.1',
    author='Dennis Gehri',
    author_email='dennis.gehri@gmail.com',
    packages=['starrecommender'],
    url='https://github.com/DG1989/star-package',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    description='3 star lion recommender',
    long_description=open_file('README.md').read()
)
