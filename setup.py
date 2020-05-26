# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


base_dir = os.path.dirname(__file__)
setup(
    name='elastalert',
    version='0.2.4',
    description='Runs custom filters on Elasticsearch and alerts on matches',
    author='Quentin Long',
    author_email='qlo@yelp.com',
    setup_requires='setuptools',
    license='Copyright 2014 Yelp',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['elastalert-create-index=elastalert.create_index:main',
                            'elastalert-test-rule=elastalert.test_rule:main',
                            'elastalert-rule-from-kibana=elastalert.rule_from_kibana:main',
                            'elastalert=elastalert.elastalert:main']},
    packages=find_packages(),
    package_data={'elastalert': ['schema.yaml', 'es_mappings/**/*.json']},
    install_requires=[
        'apscheduler',
        'aws-requests-auth',
        'blist',
        'boto3',
        'configparser',
        'croniter',
        'elasticsearch',
        'envparse',
        'exotel',
        'jira',
        'jsonschema',
        'mock',
        'prison',
        'PyStaticConfiguration',
        'python-dateutil',
        'PyYAML',
        'requests',
        'stomp.py',
        'texttable',
        'twilio',
        'python-magic',
        'cffi'
    ]
)
