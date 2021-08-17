import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'src/flask_githubapp/version.py'), 'r') as f:
    exec(f.read())

setup(
    name='Flask-GitHubApplication',
    version=__version__,
    url='https://github.com/ffalor/flask-githubapp',
    license='GNU3',
    author='Frank Falor',
    author_email='ffalorjr@outlook.com',
    description='Flask extension for creating Github Apps',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    install_requires=[
        'flask==2.0.1',
        'ghapi==0.1.19',
        'requests==2.22.0',
        'pyjwt[crypto]==2.1.0'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
