from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cyplanet.pyx"))

setup(ext_modules = exts)
