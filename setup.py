from setuptools import setup, find_packages

setup(
    name='tap_colors',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas'])
