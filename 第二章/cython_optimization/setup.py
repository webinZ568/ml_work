from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import numpy

compile_flags = ['-std=c++11', '-fopenmp']
linker_flags = ['-fopenmp']

module = Extension('tm',
                   ['tm.pyx'],
                   language='c++',
                   include_dirs=[numpy.get_include()],  # This helps to create numpy
                   extra_compile_args=compile_flags,
                   extra_link_args=linker_flags)

setup(
    name='tm', cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(module),
)
