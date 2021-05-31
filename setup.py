from setuptools import find_packages, setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AnyHR',
    version='0.0.1',
    description='Library implementing hit-and-run methods for sampling open bounded sets.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/figlerg/anyHR',
    author='Felix Gigler, Dejan Nickovic, Cristinel Mateis, Nicolas Basset, Thao Dang',
    author_email='felix.gigler.fl@ait.ac.at, dejan.nickovic@ait.ac.at',
    license='BSD',
    python_requires='>=3.5',
    install_requires=[
        'z3-solver', 'antlr4-python3-runtime', 'numpy'
    ],
    packages=find_packages(),

    classifiers=[
        'License :: OSI Approved :: BSD License',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6',
	    'Programming Language :: Python :: 3.7',
    ],
)