# fastapi_gh.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_item**](DefaultApi.md#read_item) | **GET** /items/{item_id} | Read Item
[**read_root**](DefaultApi.md#read_root) | **GET** / | Read Root


# **read_item**
> bool, date, datetime, dict, float, int, list, str, none_type read_item(item_id)

Read Item

### Example

```python
import time
import fastapi_gh
from fastapi_gh.api import default_api
from fastapi_gh.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastapi_gh.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fastapi_gh.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    item_id = 1 # int | 
    q = "q_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Read Item
        api_response = api_instance.read_item(item_id)
        pprint(api_response)
    except fastapi_gh.ApiException as e:
        print("Exception when calling DefaultApi->read_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read Item
        api_response = api_instance.read_item(item_id, q=q)
        pprint(api_response)
    except fastapi_gh.ApiException as e:
        print("Exception when calling DefaultApi->read_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  |
 **q** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_root**
> bool, date, datetime, dict, float, int, list, str, none_type read_root()

Read Root

### Example

```python
import time
import fastapi_gh
from fastapi_gh.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastapi_gh.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fastapi_gh.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Read Root
        api_response = api_instance.read_root()
        pprint(api_response)
    except fastapi_gh.ApiException as e:
        print("Exception when calling DefaultApi->read_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

