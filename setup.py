from setuptools import setup

setup(name='yts',
      version='0.3',
      description='a python powered movie torrent downloader',
      url='http://github.com/storborg/funniest',
      author='NarenArya',
      author_email='narenarya@live.com',
      license='MIT',
      packages=['yts'],
      install_requires=['requests'],
       classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX :: Linux :: Windows :: Mac'],
      zip_safe=False)