from distutils.core import setup, Extension
import numpy

setup(
    ext_modules = [
        Extension("resample",sources=["resample.c"], include_dirs = [numpy.get_include()])
        ],
    include_package_data = True
    )
    
import shutil
# shutil.rmtree('build')
