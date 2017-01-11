from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

long_description = '''Function to combine p-values with Hartung's method, the Truncated
Product Method, or Fisher's method '''

setup(
    ext_modules = cythonize("combine_pvalues/tpm/tpm.pyx"),
    name="combine_pvalues",
    version="0.1.0",
    packages=["combine_pvalues"],
    author="Kyle S. Smith",
    license="MIT Licenses",
    description='Combined array of pvalues',
    install_requires=['numpy', 'scipy', 'cython'],
    long_description=long_description,
    url="https://github.com/kylessmith/combine_pvalues",
    author_email="kyle.s.smith@ucdenver.edu"
)
