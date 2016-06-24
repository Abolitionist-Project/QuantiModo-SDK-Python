# swagger_client.ConnectorsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_connect_js_get**](ConnectorsApi.md#v1_connect_js_get) | **GET** /v1/connect.js | Get embeddable connect javascript
[**v1_connect_mobile_get**](ConnectorsApi.md#v1_connect_mobile_get) | **GET** /v1/connect/mobile | Mobile connect page
[**v1_connectors_connector_connect_get**](ConnectorsApi.md#v1_connectors_connector_connect_get) | **GET** /v1/connectors/{connector}/connect | Obtain a token from 3rd party data source
[**v1_connectors_connector_connect_instructions_get**](ConnectorsApi.md#v1_connectors_connector_connect_instructions_get) | **GET** /v1/connectors/{connector}/connectInstructions | Connection Instructions
[**v1_connectors_connector_connect_parameter_get**](ConnectorsApi.md#v1_connectors_connector_connect_parameter_get) | **GET** /v1/connectors/{connector}/connectParameter | Connect Parameter
[**v1_connectors_connector_disconnect_get**](ConnectorsApi.md#v1_connectors_connector_disconnect_get) | **GET** /v1/connectors/{connector}/disconnect | Delete stored connection info
[**v1_connectors_connector_info_get**](ConnectorsApi.md#v1_connectors_connector_info_get) | **GET** /v1/connectors/{connector}/info | Get connector info for user
[**v1_connectors_connector_update_get**](ConnectorsApi.md#v1_connectors_connector_update_get) | **GET** /v1/connectors/{connector}/update | Sync with data source
[**v1_connectors_list_get**](ConnectorsApi.md#v1_connectors_list_get) | **GET** /v1/connectors/list | List of Connectors


# **v1_connect_js_get**
> v1_connect_js_get(access_token=access_token)

Get embeddable connect javascript

Get embeddable connect javascript. Usage:    - Embedding in applications with popups for 3rd-party authentication windows.      Use `qmSetupInPopup` function after connecting `connect.js`.    - Embedding in applications with popups for 3rd-party authentication windows.      Requires a selector to block. It will be embedded in this block.      Use `qmSetupOnPage` function after connecting `connect.js`.    - Embedding in mobile applications without popups for 3rd-party authentication.      Use `qmSetupOnMobile` function after connecting `connect.js`.      if using the MoodiModo Clones, Use `qmSetupOnIonic` function after connecting `connect.js`. 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: internalApiKey
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get embeddable connect javascript
    api_instance.v1_connect_js_get(access_token=access_token)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connect_js_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connect_mobile_get**
> v1_connect_mobile_get(access_token)

Mobile connect page

This page is designed to be opened in a webview.  Instead of using popup authentication boxes, it uses redirection. You can include the user's access_token as a URL parameter like https://app.quantimo.do/api/v1/connect/mobile?access_token=123

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: internalApiKey
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
access_token = 'access_token_example' # str | User OAuth access token

try: 
    # Mobile connect page
    api_instance.v1_connect_mobile_get(access_token)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connect_mobile_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User OAuth access token | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_connect_get**
> v1_connectors_connector_connect_get(connector, access_token=access_token)

Obtain a token from 3rd party data source

Attempt to obtain a token from the data provider, store it in the database. With this, the connector to continue to obtain new user data until the token is revoked.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Obtain a token from 3rd party data source
    api_instance.v1_connectors_connector_connect_get(connector, access_token=access_token)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_connect_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_connect_instructions_get**
> v1_connectors_connector_connect_instructions_get(connector, parameters, url, use_popup, access_token=access_token)

Connection Instructions

Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint.
parameters = 'parameters_example' # str | JSON Array of Parameters for the request to enable connector.
url = 'url_example' # str | URL which should be used to enable the connector.
use_popup = true # bool | Should use popup when enabling connector
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Connection Instructions
    api_instance.v1_connectors_connector_connect_instructions_get(connector, parameters, url, use_popup, access_token=access_token)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_connect_instructions_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. | 
 **parameters** | **str**| JSON Array of Parameters for the request to enable connector. | 
 **url** | **str**| URL which should be used to enable the connector. | 
 **use_popup** | **bool**| Should use popup when enabling connector | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_connect_parameter_get**
> ConnectorInstruction v1_connectors_connector_connect_parameter_get(connector, display_name, key, placeholder, type, use_popup, access_token=access_token, default_value=default_value)

Connect Parameter

Returns instructions that describe what parameters and endpoint to use to connect to the given data provider.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint.
display_name = 'display_name_example' # str | Name of the parameter that is user visible in the form
key = 'key_example' # str | Name of the property that the user has to enter such as username or password Connector (used in HTTP request)
placeholder = 'placeholder_example' # str | Placeholder hint value for the parameter input tag.
type = 'type_example' # str | Type of input field such as those found here http://www.w3schools.com/tags/tag_input.asp
use_popup = true # bool | Should use popup when enabling connector
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
default_value = 'default_value_example' # str | Default parameter value (optional)

try: 
    # Connect Parameter
    api_response = api_instance.v1_connectors_connector_connect_parameter_get(connector, display_name, key, placeholder, type, use_popup, access_token=access_token, default_value=default_value)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_connect_parameter_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. | 
 **display_name** | **str**| Name of the parameter that is user visible in the form | 
 **key** | **str**| Name of the property that the user has to enter such as username or password Connector (used in HTTP request) | 
 **placeholder** | **str**| Placeholder hint value for the parameter input tag. | 
 **type** | **str**| Type of input field such as those found here http://www.w3schools.com/tags/tag_input.asp | 
 **use_popup** | **bool**| Should use popup when enabling connector | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **default_value** | **str**| Default parameter value | [optional] 

### Return type

[**ConnectorInstruction**](ConnectorInstruction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_disconnect_get**
> v1_connectors_connector_disconnect_get(connector)

Delete stored connection info

The disconnect method deletes any stored tokens or connection information from the connectors database.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint.

try: 
    # Delete stored connection info
    api_instance.v1_connectors_connector_disconnect_get(connector)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_disconnect_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_info_get**
> ConnectorInfo v1_connectors_connector_info_get(connector, access_token=access_token)

Get connector info for user

Returns information about the connector such as the connector id, whether or not is connected for this user (i.e. we have a token or credentials), and its update history for the user.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint.
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Get connector info for user
    api_response = api_instance.v1_connectors_connector_info_get(connector, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_info_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device. Get a list of available connectors from the /connectors/list endpoint. | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

[**ConnectorInfo**](ConnectorInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_connector_update_get**
> v1_connectors_connector_update_get(connector, access_token=access_token)

Sync with data source

The update method tells the QM Connector Framework to check with the data provider (such as Fitbit or MyFitnessPal) and retrieve any new measurements available.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()
connector = 'connector_example' # str | Lowercase system name of the source application or device
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)

try: 
    # Sync with data source
    api_instance.v1_connectors_connector_update_get(connector, access_token=access_token)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_connector_update_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector** | **str**| Lowercase system name of the source application or device | 
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_connectors_list_get**
> list[Connector] v1_connectors_list_get()

List of Connectors

A connector pulls data from other data providers using their API or a screenscraper. Returns a list of all available connectors and information about them such as their id, name, whether the user has provided access, logo url, connection instructions, and the update history.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ConnectorsApi()

try: 
    # List of Connectors
    api_response = api_instance.v1_connectors_list_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConnectorsApi->v1_connectors_list_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Connector]**](Connector.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
