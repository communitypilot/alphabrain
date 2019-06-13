from setuptools import setup
from setuptools import find_packages

long_description = 'Library for Deep Learning and Computational Neuroscience'

setup(name='alphabrain',
      version='0.0.1',
      description='Computational Neuroscience',
      long_description=long_description,
      author='Leon Hillmann',
      author_email='leon.hillmannt@gmail.com',
      url='https://github.com/LeonHillmann/alphabrain',
      download_url='',
      license='MIT',
      install_requires=['numpy>=1.9.1',
                        'scipy>=0.14',
                        'six>=1.9.0',
                        'pyyaml',
                        'h5py',
                        'keras_applications>=1.0.6',
                        'keras_preprocessing>=1.0.5'
                        ],
      extras_require={
          'visualize': ['pydot>=1.2.4'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'flaky',
                    'pytest-cov',
                    'pandas',
                    'requests',
                    'markdown'],
      },
      classifiers=[
          'Development Status :: 5 - Beta Experimental',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
