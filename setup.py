# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='django-recaptcha2',
    packages=find_packages(exclude=['samples']),
    namespace_packages = ['snowpenguin', 'snowpenguin.django'],
    # package_data={'': ['']},
    include_package_data=True,
    version='0.1.7',
    install_requires=[
        'Django>=1.5',
        'requests'
    ],
    description='Django reCaptcha v2 field/widget',
    author='Andrea Briganti',
    author_email='kbytesys@gmail.com',
    url='https://github.com/kbytesys/django-recaptcha2',
    download_url='https://github.com/kbytesys/django-recaptcha2/tarball/v0.1.7',
    keywords=['django', 'recaptcha', 'recaptcha2'],
    license='GNU LGPL v2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: Italian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
