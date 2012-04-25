from distutils.core import setup, Extension
import distutils.util
import subprocess
import numpy as np

cdist_fit = Extension('dist_fit.cdist_fit',
                    sources = ['dist_fit/cdist_fit.c'],
                    include_dirs= [np.get_include()],
                    extra_link_args = [])

cdist_func = Extension('dist_fit.cdist_func',
        sources = ['dist_fit/cdist_func.c'],
        include_dirs= [np.get_include()],
        extra_link_args = [])

common = Extension('dist_fit.common',
        sources = ['dist_fit/common.c'],
        include_dirs= [np.get_include()],
        extra_link_args = [])

setup (name = 'dist_fit',
       version = '1.00',
       description = 'Distribution Fitting/Regression Library',
       author='Piti Ongmongkolkul',
       author_email='piti118@gmail.com',
       url='https://github.com/piti118/dist_fit',
       package_dir = {'dist_fit': 'dist_fit'},
       packages = ['dist_fit'],
       ext_modules = [cdist_fit,cdist_func,common]
       )