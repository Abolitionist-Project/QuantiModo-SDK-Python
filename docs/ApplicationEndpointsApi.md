# swagger_client.ApplicationEndpointsApi

All URIs are relative to *https://app.quantimo.do/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_application_connections_get**](ApplicationEndpointsApi.md#v2_application_connections_get) | **GET** /v2/application/connections | Get all Connections
[**v2_application_credentials_get**](ApplicationEndpointsApi.md#v2_application_credentials_get) | **GET** /v2/application/credentials | Get all Credentials
[**v2_application_measurements_get**](ApplicationEndpointsApi.md#v2_application_measurements_get) | **GET** /v2/application/measurements | Get measurements for all users using your application
[**v2_application_tracking_reminders_get**](ApplicationEndpointsApi.md#v2_application_tracking_reminders_get) | **GET** /v2/application/trackingReminders | Get tracking reminders
[**v2_application_updates_get**](ApplicationEndpointsApi.md#v2_application_updates_get) | **GET** /v2/application/updates | Get all Updates
[**v2_application_user_variable_relationships_get**](ApplicationEndpointsApi.md#v2_application_user_variable_relationships_get) | **GET** /v2/application/userVariableRelationships | Get all UserVariableRelationships
[**v2_application_user_variables_get**](ApplicationEndpointsApi.md#v2_application_user_variables_get) | **GET** /v2/application/userVariables | Get all UserVariables
[**v2_application_variable_user_sources_get**](ApplicationEndpointsApi.md#v2_application_variable_user_sources_get) | **GET** /v2/application/variableUserSources | Get all VariableUserSources
[**v2_application_votes_get**](ApplicationEndpointsApi.md#v2_application_votes_get) | **GET** /v2/application/votes | Get all Votes


# **v2_application_connections_get**
> InlineResponse2003 v2_application_connections_get(access_token=access_token, connector_id=connector_id, connect_status=connect_status, connect_error=connect_error, update_requested_at=update_requested_at, update_status=update_status, update_error=update_error, last_successful_updated_at=last_successful_updated_at, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get all Connections

Get all Connections

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | Application's OAuth2 access token (optional)
connector_id = 56 # int | The id for the connector data source for which the connection is connected (optional)
connect_status = 'connect_status_example' # str | Indicates whether a connector is currently connected to a service for a user. (optional)
connect_error = 'connect_error_example' # str | Error message if there is a problem with authorizing this connection. (optional)
update_requested_at = 'update_requested_at_example' # str | Time at which an update was requested by a user. (optional)
update_status = 'update_status_example' # str | Indicates whether a connector is currently updated. (optional)
update_error = 'update_error_example' # str | Indicates if there was an error during the update. (optional)
last_successful_updated_at = 'last_successful_updated_at_example' # str | The time at which the connector was last successfully updated. (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all Connections
    api_response = api_instance.v2_application_connections_get(access_token=access_token, connector_id=connector_id, connect_status=connect_status, connect_error=connect_error, update_requested_at=update_requested_at, update_status=update_status, update_error=update_error, last_successful_updated_at=last_successful_updated_at, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_connections_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Application&#39;s OAuth2 access token | [optional] 
 **connector_id** | **int**| The id for the connector data source for which the connection is connected | [optional] 
 **connect_status** | **str**| Indicates whether a connector is currently connected to a service for a user. | [optional] 
 **connect_error** | **str**| Error message if there is a problem with authorizing this connection. | [optional] 
 **update_requested_at** | **str**| Time at which an update was requested by a user. | [optional] 
 **update_status** | **str**| Indicates whether a connector is currently updated. | [optional] 
 **update_error** | **str**| Indicates if there was an error during the update. | [optional] 
 **last_successful_updated_at** | **str**| The time at which the connector was last successfully updated. | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_credentials_get**
> InlineResponse2004 v2_application_credentials_get(access_token=access_token, connector_id=connector_id, attr_key=attr_key, attr_value=attr_value, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get all Credentials

Get all Credentials

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | Application's OAuth2 access token (optional)
connector_id = 56 # int | The id for the connector data source from which the credential was obtained (optional)
attr_key = 'attr_key_example' # str | Attribute name such as token, userid, username, or password (optional)
attr_value = 'attr_value_example' # str | Encrypted value for the attribute specified (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all Credentials
    api_response = api_instance.v2_application_credentials_get(access_token=access_token, connector_id=connector_id, attr_key=attr_key, attr_value=attr_value, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_credentials_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Application&#39;s OAuth2 access token | [optional] 
 **connector_id** | **int**| The id for the connector data source from which the credential was obtained | [optional] 
 **attr_key** | **str**| Attribute name such as token, userid, username, or password | [optional] 
 **attr_value** | **str**| Encrypted value for the attribute specified | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_measurements_get**
> InlineResponse2005 v2_application_measurements_get(access_token=access_token, client_id=client_id, connector_id=connector_id, variable_id=variable_id, source_id=source_id, start_time=start_time, value=value, unit_id=unit_id, original_value=original_value, original_unit_id=original_unit_id, duration=duration, note=note, latitude=latitude, longitude=longitude, location=location, created_at=created_at, updated_at=updated_at, error=error, limit=limit, offset=offset, sort=sort)

Get measurements for all users using your application

Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten.

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | Application's OAuth2 access token (optional)
client_id = 'client_id_example' # str | The ID of the client application which originally stored the measurement (optional)
connector_id = 56 # int | The id for the connector data source from which the measurement was obtained (optional)
variable_id = 56 # int | ID of the variable for which we are creating the measurement records (optional)
source_id = 56 # int | Application or device used to record the measurement values (optional)
start_time = 'start_time_example' # str | start time for the measurement event. Use ISO 8601 datetime format  (optional)
value = 3.4 # float | The value of the measurement after conversion to the default unit for that variable (optional)
unit_id = 56 # int | The default unit id for the variable (optional)
original_value = 3.4 # float | Unconverted value of measurement as originally posted (before conversion to default unit) (optional)
original_unit_id = 56 # int | Unit id of the measurement as originally submitted (optional)
duration = 56 # int | Duration of the event being measurement in seconds (optional)
note = 'note_example' # str | An optional note the user may include with their measurement (optional)
latitude = 3.4 # float | Latitude at which the measurement was taken (optional)
longitude = 3.4 # float | Longitude at which the measurement was taken (optional)
location = 'location_example' # str | Optional human readable name for the location where the measurement was recorded (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
error = 'error_example' # str | An error message if there is a problem with the measurement (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get measurements for all users using your application
    api_response = api_instance.v2_application_measurements_get(access_token=access_token, client_id=client_id, connector_id=connector_id, variable_id=variable_id, source_id=source_id, start_time=start_time, value=value, unit_id=unit_id, original_value=original_value, original_unit_id=original_unit_id, duration=duration, note=note, latitude=latitude, longitude=longitude, location=location, created_at=created_at, updated_at=updated_at, error=error, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_measurements_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Application&#39;s OAuth2 access token | [optional] 
 **client_id** | **str**| The ID of the client application which originally stored the measurement | [optional] 
 **connector_id** | **int**| The id for the connector data source from which the measurement was obtained | [optional] 
 **variable_id** | **int**| ID of the variable for which we are creating the measurement records | [optional] 
 **source_id** | **int**| Application or device used to record the measurement values | [optional] 
 **start_time** | **str**| start time for the measurement event. Use ISO 8601 datetime format  | [optional] 
 **value** | **float**| The value of the measurement after conversion to the default unit for that variable | [optional] 
 **unit_id** | **int**| The default unit id for the variable | [optional] 
 **original_value** | **float**| Unconverted value of measurement as originally posted (before conversion to default unit) | [optional] 
 **original_unit_id** | **int**| Unit id of the measurement as originally submitted | [optional] 
 **duration** | **int**| Duration of the event being measurement in seconds | [optional] 
 **note** | **str**| An optional note the user may include with their measurement | [optional] 
 **latitude** | **float**| Latitude at which the measurement was taken | [optional] 
 **longitude** | **float**| Longitude at which the measurement was taken | [optional] 
 **location** | **str**| Optional human readable name for the location where the measurement was recorded | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **error** | **str**| An error message if there is a problem with the measurement | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_tracking_reminders_get**
> InlineResponse2001 v2_application_tracking_reminders_get(access_token=access_token, client_id=client_id, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get tracking reminders

Get the variable id, frequency, and default value for the user tracking reminders 

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
client_id = 'client_id_example' # str | The ID of the client application which last created or updated this trackingReminder (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get tracking reminders
    api_response = api_instance.v2_application_tracking_reminders_get(access_token=access_token, client_id=client_id, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_tracking_reminders_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **client_id** | **str**| The ID of the client application which last created or updated this trackingReminder | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_updates_get**
> InlineResponse2006 v2_application_updates_get(access_token=access_token, connector_id=connector_id, number_of_measurements=number_of_measurements, success=success, message=message, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get all Updates

Get all Updates

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | Application's OAuth2 access token (optional)
connector_id = 56 # int | connector_id (optional)
number_of_measurements = 56 # int | number_of_measurements (optional)
success = true # bool | success (optional)
message = 'message_example' # str | message (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all Updates
    api_response = api_instance.v2_application_updates_get(access_token=access_token, connector_id=connector_id, number_of_measurements=number_of_measurements, success=success, message=message, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_updates_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Application&#39;s OAuth2 access token | [optional] 
 **connector_id** | **int**| connector_id | [optional] 
 **number_of_measurements** | **int**| number_of_measurements | [optional] 
 **success** | **bool**| success | [optional] 
 **message** | **str**| message | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_user_variable_relationships_get**
> InlineResponse2007 v2_application_user_variable_relationships_get(access_token=access_token, id=id, confidence_level=confidence_level, confidence_score=confidence_score, direction=direction, duration_of_action=duration_of_action, error_message=error_message, onset_delay=onset_delay, outcome_variable_id=outcome_variable_id, predictor_variable_id=predictor_variable_id, predictor_unit_id=predictor_unit_id, sinn_rank=sinn_rank, strength_level=strength_level, strength_score=strength_score, vote=vote, value_predicting_high_outcome=value_predicting_high_outcome, value_predicting_low_outcome=value_predicting_low_outcome, limit=limit, offset=offset, sort=sort)

Get all UserVariableRelationships

Get all UserVariableRelationships

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
id = 56 # int | id (optional)
confidence_level = 'confidence_level_example' # str | Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors (optional)
confidence_score = 3.4 # float | A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors (optional)
direction = 'direction_example' # str | Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values. (optional)
duration_of_action = 56 # int | Estimated number of seconds following the onset delay in which a stimulus produces a perceivable effect (optional)
error_message = 'error_message_example' # str | error_message (optional)
onset_delay = 56 # int | Estimated number of seconds that pass before a stimulus produces a perceivable effect (optional)
outcome_variable_id = 56 # int | Variable ID for the outcome variable (optional)
predictor_variable_id = 56 # int | Variable ID for the predictor variable (optional)
predictor_unit_id = 56 # int | ID for default unit of the predictor variable (optional)
sinn_rank = 3.4 # float | A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting. (optional)
strength_level = 'strength_level_example' # str | Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores. (optional)
strength_score = 3.4 # float | A value represented to the size of the effect which the predictor appears to have on the outcome. (optional)
vote = 'vote_example' # str | vote (optional)
value_predicting_high_outcome = 3.4 # float | Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value (optional)
value_predicting_low_outcome = 3.4 # float | Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all UserVariableRelationships
    api_response = api_instance.v2_application_user_variable_relationships_get(access_token=access_token, id=id, confidence_level=confidence_level, confidence_score=confidence_score, direction=direction, duration_of_action=duration_of_action, error_message=error_message, onset_delay=onset_delay, outcome_variable_id=outcome_variable_id, predictor_variable_id=predictor_variable_id, predictor_unit_id=predictor_unit_id, sinn_rank=sinn_rank, strength_level=strength_level, strength_score=strength_score, vote=vote, value_predicting_high_outcome=value_predicting_high_outcome, value_predicting_low_outcome=value_predicting_low_outcome, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_user_variable_relationships_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **id** | **int**| id | [optional] 
 **confidence_level** | **str**| Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors | [optional] 
 **confidence_score** | **float**| A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors | [optional] 
 **direction** | **str**| Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values. | [optional] 
 **duration_of_action** | **int**| Estimated number of seconds following the onset delay in which a stimulus produces a perceivable effect | [optional] 
 **error_message** | **str**| error_message | [optional] 
 **onset_delay** | **int**| Estimated number of seconds that pass before a stimulus produces a perceivable effect | [optional] 
 **outcome_variable_id** | **int**| Variable ID for the outcome variable | [optional] 
 **predictor_variable_id** | **int**| Variable ID for the predictor variable | [optional] 
 **predictor_unit_id** | **int**| ID for default unit of the predictor variable | [optional] 
 **sinn_rank** | **float**| A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting. | [optional] 
 **strength_level** | **str**| Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores. | [optional] 
 **strength_score** | **float**| A value represented to the size of the effect which the predictor appears to have on the outcome. | [optional] 
 **vote** | **str**| vote | [optional] 
 **value_predicting_high_outcome** | **float**| Value for the predictor variable (in it&#39;s default unit) which typically precedes an above average outcome value | [optional] 
 **value_predicting_low_outcome** | **float**| Value for the predictor variable (in it&#39;s default unit) which typically precedes a below average outcome value | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_user_variables_get**
> InlineResponse2008 v2_application_user_variables_get(access_token=access_token, client_id=client_id, parent_id=parent_id, variable_id=variable_id, default_unit_id=default_unit_id, minimum_allowed_value=minimum_allowed_value, maximum_allowed_value=maximum_allowed_value, filling_value=filling_value, join_with=join_with, onset_delay=onset_delay, duration_of_action=duration_of_action, variable_category_id=variable_category_id, updated=updated, public=public, cause_only=cause_only, filling_type=filling_type, number_of_measurements=number_of_measurements, number_of_processed_measurements=number_of_processed_measurements, measurements_at_last_analysis=measurements_at_last_analysis, last_unit_id=last_unit_id, last_original_unit_id=last_original_unit_id, last_original_value=last_original_value, last_value=last_value, last_source_id=last_source_id, number_of_correlations=number_of_correlations, status=status, error_message=error_message, last_successful_update_time=last_successful_update_time, standard_deviation=standard_deviation, variance=variance, minimum_recorded_value=minimum_recorded_value, maximum_recorded_value=maximum_recorded_value, mean=mean, median=median, most_common_unit_id=most_common_unit_id, most_common_value=most_common_value, number_of_unique_daily_values=number_of_unique_daily_values, number_of_changes=number_of_changes, skewness=skewness, kurtosis=kurtosis, latitude=latitude, longitude=longitude, location=location, created_at=created_at, updated_at=updated_at, outcome=outcome, sources=sources, earliest_source_time=earliest_source_time, latest_source_time=latest_source_time, earliest_measurement_time=earliest_measurement_time, latest_measurement_time=latest_measurement_time, earliest_filling_time=earliest_filling_time, latest_filling_time=latest_filling_time, limit=limit, offset=offset, sort=sort)

Get all UserVariables

Get all UserVariables

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
client_id = 'client_id_example' # str | The ID of the client application which last created or updated this user variable (optional)
parent_id = 56 # int | ID of the parent variable if this variable has any parent (optional)
variable_id = 56 # int | ID of variable (optional)
default_unit_id = 56 # int | D of unit to use for this variable (optional)
minimum_allowed_value = 3.4 # float | Minimum reasonable value for this variable (uses default unit) (optional)
maximum_allowed_value = 3.4 # float | Maximum reasonable value for this variable (uses default unit) (optional)
filling_value = 3.4 # float | Value for replacing null measurements (optional)
join_with = 56 # int | The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables (optional)
onset_delay = 56 # int | Estimated number of seconds that pass before a stimulus produces a perceivable effect (optional)
duration_of_action = 56 # int | Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect (optional)
variable_category_id = 56 # int | ID of variable category (optional)
updated = 56 # int | updated (optional)
public = 56 # int | Is variable public (optional)
cause_only = true # bool | A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user (optional)
filling_type = 'filling_type_example' # str | 0 -> No filling, 1 -> Use filling-value (optional)
number_of_measurements = 56 # int | Number of measurements (optional)
number_of_processed_measurements = 56 # int | Number of processed measurements (optional)
measurements_at_last_analysis = 56 # int | Number of measurements at last analysis (optional)
last_unit_id = 56 # int | ID of last Unit (optional)
last_original_unit_id = 56 # int | ID of last original Unit (optional)
last_original_value = 56 # int | Last original value which is stored (optional)
last_value = 3.4 # float | Last Value (optional)
last_source_id = 56 # int | ID of last source (optional)
number_of_correlations = 56 # int | Number of correlations for this variable (optional)
status = 'status_example' # str | status (optional)
error_message = 'error_message_example' # str | error_message (optional)
last_successful_update_time = 'last_successful_update_time_example' # str | When this variable or its settings were last updated (optional)
standard_deviation = 3.4 # float | Standard deviation (optional)
variance = 3.4 # float | Variance (optional)
minimum_recorded_value = 3.4 # float | Minimum recorded value of this variable (optional)
maximum_recorded_value = 3.4 # float | Maximum recorded value of this variable (optional)
mean = 3.4 # float | Mean (optional)
median = 3.4 # float | Median (optional)
most_common_unit_id = 56 # int | Most common Unit ID (optional)
most_common_value = 3.4 # float | Most common value (optional)
number_of_unique_daily_values = 3.4 # float | Number of unique daily values (optional)
number_of_changes = 56 # int | Number of changes (optional)
skewness = 3.4 # float | Skewness (optional)
kurtosis = 3.4 # float | Kurtosis (optional)
latitude = 3.4 # float | Latitude (optional)
longitude = 3.4 # float | Longitude (optional)
location = 'location_example' # str | Location (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
outcome = true # bool | Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables (optional)
sources = 'sources_example' # str | Comma-separated list of source names to limit variables to those sources (optional)
earliest_source_time = 56 # int | Earliest source time (optional)
latest_source_time = 56 # int | Latest source time (optional)
earliest_measurement_time = 56 # int | Earliest measurement time (optional)
latest_measurement_time = 56 # int | Latest measurement time (optional)
earliest_filling_time = 56 # int | Earliest filling time (optional)
latest_filling_time = 56 # int | Latest filling time (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all UserVariables
    api_response = api_instance.v2_application_user_variables_get(access_token=access_token, client_id=client_id, parent_id=parent_id, variable_id=variable_id, default_unit_id=default_unit_id, minimum_allowed_value=minimum_allowed_value, maximum_allowed_value=maximum_allowed_value, filling_value=filling_value, join_with=join_with, onset_delay=onset_delay, duration_of_action=duration_of_action, variable_category_id=variable_category_id, updated=updated, public=public, cause_only=cause_only, filling_type=filling_type, number_of_measurements=number_of_measurements, number_of_processed_measurements=number_of_processed_measurements, measurements_at_last_analysis=measurements_at_last_analysis, last_unit_id=last_unit_id, last_original_unit_id=last_original_unit_id, last_original_value=last_original_value, last_value=last_value, last_source_id=last_source_id, number_of_correlations=number_of_correlations, status=status, error_message=error_message, last_successful_update_time=last_successful_update_time, standard_deviation=standard_deviation, variance=variance, minimum_recorded_value=minimum_recorded_value, maximum_recorded_value=maximum_recorded_value, mean=mean, median=median, most_common_unit_id=most_common_unit_id, most_common_value=most_common_value, number_of_unique_daily_values=number_of_unique_daily_values, number_of_changes=number_of_changes, skewness=skewness, kurtosis=kurtosis, latitude=latitude, longitude=longitude, location=location, created_at=created_at, updated_at=updated_at, outcome=outcome, sources=sources, earliest_source_time=earliest_source_time, latest_source_time=latest_source_time, earliest_measurement_time=earliest_measurement_time, latest_measurement_time=latest_measurement_time, earliest_filling_time=earliest_filling_time, latest_filling_time=latest_filling_time, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_user_variables_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **client_id** | **str**| The ID of the client application which last created or updated this user variable | [optional] 
 **parent_id** | **int**| ID of the parent variable if this variable has any parent | [optional] 
 **variable_id** | **int**| ID of variable | [optional] 
 **default_unit_id** | **int**| D of unit to use for this variable | [optional] 
 **minimum_allowed_value** | **float**| Minimum reasonable value for this variable (uses default unit) | [optional] 
 **maximum_allowed_value** | **float**| Maximum reasonable value for this variable (uses default unit) | [optional] 
 **filling_value** | **float**| Value for replacing null measurements | [optional] 
 **join_with** | **int**| The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables | [optional] 
 **onset_delay** | **int**| Estimated number of seconds that pass before a stimulus produces a perceivable effect | [optional] 
 **duration_of_action** | **int**| Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect | [optional] 
 **variable_category_id** | **int**| ID of variable category | [optional] 
 **updated** | **int**| updated | [optional] 
 **public** | **int**| Is variable public | [optional] 
 **cause_only** | **bool**| A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user | [optional] 
 **filling_type** | **str**| 0 -&gt; No filling, 1 -&gt; Use filling-value | [optional] 
 **number_of_measurements** | **int**| Number of measurements | [optional] 
 **number_of_processed_measurements** | **int**| Number of processed measurements | [optional] 
 **measurements_at_last_analysis** | **int**| Number of measurements at last analysis | [optional] 
 **last_unit_id** | **int**| ID of last Unit | [optional] 
 **last_original_unit_id** | **int**| ID of last original Unit | [optional] 
 **last_original_value** | **int**| Last original value which is stored | [optional] 
 **last_value** | **float**| Last Value | [optional] 
 **last_source_id** | **int**| ID of last source | [optional] 
 **number_of_correlations** | **int**| Number of correlations for this variable | [optional] 
 **status** | **str**| status | [optional] 
 **error_message** | **str**| error_message | [optional] 
 **last_successful_update_time** | **str**| When this variable or its settings were last updated | [optional] 
 **standard_deviation** | **float**| Standard deviation | [optional] 
 **variance** | **float**| Variance | [optional] 
 **minimum_recorded_value** | **float**| Minimum recorded value of this variable | [optional] 
 **maximum_recorded_value** | **float**| Maximum recorded value of this variable | [optional] 
 **mean** | **float**| Mean | [optional] 
 **median** | **float**| Median | [optional] 
 **most_common_unit_id** | **int**| Most common Unit ID | [optional] 
 **most_common_value** | **float**| Most common value | [optional] 
 **number_of_unique_daily_values** | **float**| Number of unique daily values | [optional] 
 **number_of_changes** | **int**| Number of changes | [optional] 
 **skewness** | **float**| Skewness | [optional] 
 **kurtosis** | **float**| Kurtosis | [optional] 
 **latitude** | **float**| Latitude | [optional] 
 **longitude** | **float**| Longitude | [optional] 
 **location** | **str**| Location | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **outcome** | **bool**| Outcome variables (those with &#x60;outcome&#x60; &#x3D;&#x3D; 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables | [optional] 
 **sources** | **str**| Comma-separated list of source names to limit variables to those sources | [optional] 
 **earliest_source_time** | **int**| Earliest source time | [optional] 
 **latest_source_time** | **int**| Latest source time | [optional] 
 **earliest_measurement_time** | **int**| Earliest measurement time | [optional] 
 **latest_measurement_time** | **int**| Latest measurement time | [optional] 
 **earliest_filling_time** | **int**| Earliest filling time | [optional] 
 **latest_filling_time** | **int**| Latest filling time | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_variable_user_sources_get**
> InlineResponse2009 v2_application_variable_user_sources_get(access_token=access_token, variable_id=variable_id, timestamp=timestamp, earliest_measurement_time=earliest_measurement_time, latest_measurement_time=latest_measurement_time, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get all VariableUserSources

Get all VariableUserSources

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
variable_id = 56 # int | ID of variable (optional)
timestamp = 56 # int | Time that this measurement occurred Uses epoch minute (epoch time divided by 60) (optional)
earliest_measurement_time = 56 # int | Earliest measurement time (optional)
latest_measurement_time = 56 # int | Latest measurement time (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all VariableUserSources
    api_response = api_instance.v2_application_variable_user_sources_get(access_token=access_token, variable_id=variable_id, timestamp=timestamp, earliest_measurement_time=earliest_measurement_time, latest_measurement_time=latest_measurement_time, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_variable_user_sources_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **variable_id** | **int**| ID of variable | [optional] 
 **timestamp** | **int**| Time that this measurement occurred Uses epoch minute (epoch time divided by 60) | [optional] 
 **earliest_measurement_time** | **int**| Earliest measurement time | [optional] 
 **latest_measurement_time** | **int**| Latest measurement time | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_application_votes_get**
> InlineResponse20010 v2_application_votes_get(access_token=access_token, client_id=client_id, cause_id=cause_id, effect_id=effect_id, value=value, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)

Get all Votes

Get all Votes

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
api_instance = swagger_client.ApplicationEndpointsApi()
access_token = 'access_token_example' # str | User's OAuth2 access token (optional)
client_id = 'client_id_example' # str | The ID of the client application which last created or updated this vote (optional)
cause_id = 56 # int | ID of predictor variable (optional)
effect_id = 56 # int | ID of outcome variable (optional)
value = 56 # int | Value of Vote. 1 is for upvote. 0 is for downvote.  Otherwise, there is no vote. (optional)
created_at = 'created_at_example' # str | When the record was first created. Use ISO 8601 datetime format  (optional)
updated_at = 'updated_at_example' # str | When the record was last updated. Use ISO 8601 datetime format  (optional)
limit = 56 # int | The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. (optional)
offset = 56 # int | OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. (optional)
sort = 'sort_example' # str | Sort by given field. If the field is prefixed with '-', it will sort in descending order. (optional)

try: 
    # Get all Votes
    api_response = api_instance.v2_application_votes_get(access_token=access_token, client_id=client_id, cause_id=cause_id, effect_id=effect_id, value=value, created_at=created_at, updated_at=updated_at, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationEndpointsApi->v2_application_votes_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| User&#39;s OAuth2 access token | [optional] 
 **client_id** | **str**| The ID of the client application which last created or updated this vote | [optional] 
 **cause_id** | **int**| ID of predictor variable | [optional] 
 **effect_id** | **int**| ID of outcome variable | [optional] 
 **value** | **int**| Value of Vote. 1 is for upvote. 0 is for downvote.  Otherwise, there is no vote. | [optional] 
 **created_at** | **str**| When the record was first created. Use ISO 8601 datetime format  | [optional] 
 **updated_at** | **str**| When the record was last updated. Use ISO 8601 datetime format  | [optional] 
 **limit** | **int**| The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records. | [optional] 
 **offset** | **int**| OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned. | [optional] 
 **sort** | **str**| Sort by given field. If the field is prefixed with &#39;-&#39;, it will sort in descending order. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oauth2](../README.md#oauth2), [internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
