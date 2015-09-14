from setuptools import find_packages
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
requires=[i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='videoscene',
    version="0.1.0",
    description='Parse scene release tags',
    long_description=read_md('README.md'),
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='http://github.com/walidsa3d/videoscene',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    test_suite="tests",
    license="MIT",
    zip_safe=False,

)
