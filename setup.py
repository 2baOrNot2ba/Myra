#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'dreamBeam',
      version = '0.2',
      description = 'Measurement equation framework for interferometry in Radio Astronomy.',
      author = 'Tobia D. Carozzi',
      author_email = 'tobia.carozzi@chalmers.se',
      packages = find_packages(),
      package_data = {'dreambeam.telescopes.LOFAR':
                ['share/*.cc','share/simmos/*.cfg','share/alignment/*.txt','data/*teldat.p']},
      license = 'ISC',
      classifiers = [
          'Development Status :: 1 - Planning',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: ISC License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Astronomy',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Visualization'
      ],
      install_requires=[
          'numpy>=1.10',
          'python-casacore',
          'matplotlib',
          'antpat'
      ],
      scripts = ['scripts/pointing_jones.py']
     )
