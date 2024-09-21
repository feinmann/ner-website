from distutils.core import setup
from setuptools import find_packages

setup(
    name="ner-website",
    version="0.0.1",
    description="Simple Website for NER",
    packages=['static', 'templates', 'test']
)