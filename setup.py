from setuptools import setup, find_packages
from os import path

location = path.abspath(path.dirname(__file__))

#Get full desription of project from README.md 
with open(path.join(location, 'README.md'), encoding='UTF-8') as f:
    service_description = f.read()

setup(
    name = 'bookstore',
    version = '0.0.1',
    packages = find_packages(),
    include_package_data = True,

    install_requires = [
        'django',
    ],

    #package metadata
    author = 'Jane Mishchishina',
    author_email = 'janekaraim@gmail.com',
    description = 'Test task for djangostars.com',
    long_description=service_description,
    long_description_content_type = 'text/markdown',
    keywords = 'test task',
    license = 'MIT',

)