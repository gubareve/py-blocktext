from setuptools import setup, find_packages

setup(
    name='pyblocktext',
    version='0.1',
    packages=find_packages(exclude=['.github*']),
    license='MIT',
    description='a python package to generate blocktext',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/gubareve/py-blocktext/',
    author='Evan Gubarev',
    author_email='evan@evangubarev.com'
)
