from setuptools import setup

setup(name='norris',
      version='0.1',
      description='Wrapper for the ICNDB API',
      url='http://github.com/chriscardillo/norris_py',
      author='Chris Cardillo',
      author_email='CFCardillo23@gmail.com',
      license='MIT',
      packages=['norris'],
      install_requires=['requests', 'pandas'],
      zip_safe=False)
