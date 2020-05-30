# sslexp
#### check a state of your ssl certificates simply and cleverly

[![PyPI version](https://badge.fury.io/py/sslexp.png)](https://badge.fury.io/py/sslexp)
[![Build Status](https://travis-ci.org/patrikskrivanek/ssl_expiration.svg?branch=master)](https://travis-ci.org/patrikskrivanek/ssl_expiration)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/patrikskrivanek/ssl_expiration.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/patrikskrivanek/ssl_expiration/context:python)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

This program checks the expiration date of an ssl certificate.
First set the url param that should contain the url address of a domain.
The program returns a message and a status code based on a measurement result.

### Installation
```bash
# using pip
pip install sslexp

# or if you are running multiple versions of python such as 2.7.x and 3.x 
pip3 install sslexp

# from source using git clone
git clone https://github.com/patrikskrivanek/ssl_expiration.git

# from source using wget
wget https://github.com/patrikskrivanek/ssl_expiration/blob/master/sslexp
```

### Documentation
Argument | Description | Data type | Required
------------ | ------------- | ------------- | -------------
--url | URL of an ssl certificate for check | string | yes
--warning | Number of days for warning output | integer | no *[default 30]*
--critical | Number of days for critical output | integer | no *[default 20]*
--port | SSL port | integer | no *[default 443]*
--timeout | Timeout in seconds for check | integer | no *[default 3]*
--version | Show program version | | optional
-h --help | Show program help and usage | | optional

Status | Exit code | 
------------ | -------------
STATE_OK | 0
STATE_WARNING | 1
STATE_CRITICAL | 2
STATE_UNKNOWN | 3

### Examples
```bash
# check an ssl cert of github
sslexp --url github.com

# check the cert with your own warning and critical params
sslexp --url github.com --warning 5 --critical 3

# check the ssl certificate on specific port
sslexp --url website.com --port 8085

# check the ssl cert with timeout
sslexp --url website.com --timeout 5

# show program help
sslexp --help

# show program version
sslexp --version
```
