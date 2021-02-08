# FastAPI Client Generation with Github Action Example
FastAPI example with GitHub Action to generate client code.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import fastapi_gh
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fastapi_gh
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import fastapi_gh
from pprint import pprint
from fastapi_gh.api import default_api
from fastapi_gh.model.http_validation_error import HTTPValidationError
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastapi_gh.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with fastapi_gh.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    item_id = 1 # int | 
q = "q_example" # str |  (optional)

    try:
        # Read Item
        api_response = api_instance.read_item(item_id, q=q)
        pprint(api_response)
    except fastapi_gh.ApiException as e:
        print("Exception when calling DefaultApi->read_item: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**read_item**](docs/DefaultApi.md#read_item) | **GET** /items/{item_id} | Read Item
*DefaultApi* | [**read_root**](docs/DefaultApi.md#read_root) | **GET** / | Read Root


## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in fastapi_gh.apis and fastapi_gh.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from fastapi_gh.api.default_api import DefaultApi`
- `from fastapi_gh.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import fastapi_gh
from fastapi_gh.apis import *
from fastapi_gh.models import *
```

