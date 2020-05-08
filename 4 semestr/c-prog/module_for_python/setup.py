from distutils.core import setup, Extension

modPM = Extension('modPM', sources = ['modPM.c'])

setup(name='modPM',
      version='0.1.0',
      description='Module for count complex numbers and vectors',
      ext_modules=[modPM])