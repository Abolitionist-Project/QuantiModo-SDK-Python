# coding: utf-8

"""
    QuantiModo

    Welcome to QuantiModo API! QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications. [Learn about QuantiModo](https://quantimo.do) or contact us at <api@quantimo.do>.         Before you get started, you will need to: * Sign in/Sign up, and add some data at [https://app.quantimo.do/api/v2/account/connectors](https://app.quantimo.do/api/v2/account/connectors) to try out the API for yourself * Create an app to get your client id and secret at [https://app.quantimo.do/api/v2/apps](https://app.quantimo.do/api/v2/apps) * As long as you're signed in, it will use your browser's cookie for authentication.  However, client applications must use OAuth2 tokens to access the API.     ## Application Endpoints These endpoints give you access to all authorized users' data for that application. ### Getting Application Token Make a `POST` request to `/api/v2/oauth/access_token`         * `grant_type` Must be `client_credentials`.         * `clientId` Your application's clientId.         * `client_secret` Your application's client_secret.         * `redirect_uri` Your application's redirect url.                ## Example Queries ### Query Options The standard query options for QuantiModo API are as described in the table below. These are the available query options in QuantiModo API: <table>            <thead>                <tr>                    <th>Parameter</th>                    <th>Description</th>                </tr>            </thead>            <tbody>                <tr>                    <td>limit</td>                    <td>The LIMIT is used to limit the number of results returned.  So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.</td>                </tr>                <tr>                    <td>offset</td>                    <td>Suppose you wanted to show results 11-20. You'd set the    offset to 10 and the limit to 10.</td>                </tr>                <tr>                    <td>sort</td>                    <td>Sort by given field. If the field is prefixed with '-', it    will sort in descending order.</td>                </tr>            </tbody>        </table>         ### Pagination Conventions Since the maximum limit is 200 records, to get more than that you'll have to make multiple API calls and page through the results. To retrieve all the data, you can iterate through data by using the `limit` and `offset` query parameters.For example, if you want to retrieve data from 61-80 then you can use a query with the following parameters,         `/v2/variables?limit=20&offset=60`         Generally, you'll be retrieving new or updated user data. To avoid unnecessary API calls, you'll want to store your last refresh time locally.  Initially, it should be set to 0. Then whenever you make a request to get new data, you should limit the returned results to those updated since your last refresh by appending append         `?lastUpdated=(ge)&quot2013-01-D01T01:01:01&quot`         to your request.         Also for better pagination, you can get link to the records of first, last, next and previous page from response headers: * `Total-Count` - Total number of results for given query * `Link-First` - Link to get first page records * `Link-Last` - Link to get last page records * `Link-Prev` - Link to get previous records set * `Link-Next` - Link to get next records set         Remember, response header will be only sent when the record set is available. e.g. You will not get a ```Link-Last``` & ```Link-Next``` when you query for the last page.         ### Filter operators support API supports the following operators with filter parameters: <br> **Comparison operators**         Comparison operators allow you to limit results to those greater than, less than, or equal to a specified value for a specified attribute. These operators can be used with strings, numbers, and dates. The following comparison operators are available: * `gt` for `greater than` comparison * `ge` for `greater than or equal` comparison * `lt` for `less than` comparison * `le` for `less than or equal` comparison         They are included in queries using the following format:         `(<operator>)<value>`         For example, in order to filter value which is greater than 21, the following query parameter should be used:         `?value=(gt)21` <br><br> **Equals/In Operators**         It also allows filtering by the exact value of an attribute or by a set of values, depending on the type of value passed as a query parameter. If the value contains commas, the parameter is split on commas and used as array input for `IN` filtering, otherwise the exact match is applied. In order to only show records which have the value 42, the following query should be used:         `?value=42`         In order to filter records which have value 42 or 43, the following query should be used:         `?value=42,43` <br><br> **Like operators**         Like operators allow filtering using `LIKE` query. This operator is triggered if exact match operator is used, but value contains `%` sign as the first or last character. In order to filter records which category that start with `Food`, the following query should be used:         `?category=Food%` <br><br> **Negation operator**         It is possible to get negated results of a query by prefixed the operator with `!`. Some examples:         `//filter records except those with value are not 42 or 43`<br> `?value=!42,43`         `//filter records with value not greater than 21`<br> `?value=!(ge)21` <br><br> **Multiple constraints for single attribute**         It is possible to apply multiple constraints by providing an array of query filters:         Filter all records which value is greater than 20.2 and less than 20.3<br> `?value[]=(gt)20.2&value[]=(lt)20.3`         Filter all records which value is greater than 20.2 and less than 20.3 but not 20.2778<br> `?value[]=(gt)20.2&value[]=(lt)20.3&value[]=!20.2778`<br><br> 

    OpenAPI spec version: 2.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ApplicationEndpointsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v2_application_connections_get(self, **kwargs):
        """
        Get all Connections
        Get all Connections

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_connections_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: The id for the connector data source for which the connection is connected
        :param str connect_status: Indicates whether a connector is currently connected to a service for a user.
        :param str connect_error: Error message if there is a problem with authorizing this connection.
        :param str update_requested_at: Time at which an update was requested by a user.
        :param str update_status: Indicates whether a connector is currently updated.
        :param str update_error: Indicates if there was an error during the update.
        :param str last_successful_updated_at: The time at which the connector was last successfully updated.
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_connections_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_connections_get_with_http_info(**kwargs)
            return data

    def v2_application_connections_get_with_http_info(self, **kwargs):
        """
        Get all Connections
        Get all Connections

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_connections_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: The id for the connector data source for which the connection is connected
        :param str connect_status: Indicates whether a connector is currently connected to a service for a user.
        :param str connect_error: Error message if there is a problem with authorizing this connection.
        :param str update_requested_at: Time at which an update was requested by a user.
        :param str update_status: Indicates whether a connector is currently updated.
        :param str update_error: Indicates if there was an error during the update.
        :param str last_successful_updated_at: The time at which the connector was last successfully updated.
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'connector_id', 'connect_status', 'connect_error', 'update_requested_at', 'update_status', 'update_error', 'last_successful_updated_at', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_connections_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/connections'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'connector_id' in params:
            query_params['connector_id'] = params['connector_id']
        if 'connect_status' in params:
            query_params['connect_status'] = params['connect_status']
        if 'connect_error' in params:
            query_params['connect_error'] = params['connect_error']
        if 'update_requested_at' in params:
            query_params['update_requested_at'] = params['update_requested_at']
        if 'update_status' in params:
            query_params['update_status'] = params['update_status']
        if 'update_error' in params:
            query_params['update_error'] = params['update_error']
        if 'last_successful_updated_at' in params:
            query_params['last_successful_updated_at'] = params['last_successful_updated_at']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2003',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_credentials_get(self, **kwargs):
        """
        Get all Credentials
        Get all Credentials

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_credentials_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: The id for the connector data source from which the credential was obtained
        :param str attr_key: Attribute name such as token, userid, username, or password
        :param str attr_value: Encrypted value for the attribute specified
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_credentials_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_credentials_get_with_http_info(**kwargs)
            return data

    def v2_application_credentials_get_with_http_info(self, **kwargs):
        """
        Get all Credentials
        Get all Credentials

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_credentials_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: The id for the connector data source from which the credential was obtained
        :param str attr_key: Attribute name such as token, userid, username, or password
        :param str attr_value: Encrypted value for the attribute specified
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'connector_id', 'attr_key', 'attr_value', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_credentials_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/credentials'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'connector_id' in params:
            query_params['connector_id'] = params['connector_id']
        if 'attr_key' in params:
            query_params['attr_key'] = params['attr_key']
        if 'attr_value' in params:
            query_params['attr_value'] = params['attr_value']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2004',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_measurements_get(self, **kwargs):
        """
        Get measurements for all users using your application
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_measurements_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param str client_id: The ID of the client application which originally stored the measurement
        :param int connector_id: The id for the connector data source from which the measurement was obtained
        :param int variable_id: ID of the variable for which we are creating the measurement records
        :param int source_id: Application or device used to record the measurement values
        :param str start_time: start time for the measurement event. Use ISO 8601 datetime format 
        :param float value: The value of the measurement after conversion to the default unit for that variable
        :param int unit_id: The default unit id for the variable
        :param float original_value: Unconverted value of measurement as originally posted (before conversion to default unit)
        :param int original_unit_id: Unit id of the measurement as originally submitted
        :param int duration: Duration of the event being measurement in seconds
        :param str note: An optional note the user may include with their measurement
        :param float latitude: Latitude at which the measurement was taken
        :param float longitude: Longitude at which the measurement was taken
        :param str location: Optional human readable name for the location where the measurement was recorded
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param str error: An error message if there is a problem with the measurement
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_measurements_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_measurements_get_with_http_info(**kwargs)
            return data

    def v2_application_measurements_get_with_http_info(self, **kwargs):
        """
        Get measurements for all users using your application
        Measurements are any value that can be recorded like daily steps, a mood rating, or apples eaten.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_measurements_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param str client_id: The ID of the client application which originally stored the measurement
        :param int connector_id: The id for the connector data source from which the measurement was obtained
        :param int variable_id: ID of the variable for which we are creating the measurement records
        :param int source_id: Application or device used to record the measurement values
        :param str start_time: start time for the measurement event. Use ISO 8601 datetime format 
        :param float value: The value of the measurement after conversion to the default unit for that variable
        :param int unit_id: The default unit id for the variable
        :param float original_value: Unconverted value of measurement as originally posted (before conversion to default unit)
        :param int original_unit_id: Unit id of the measurement as originally submitted
        :param int duration: Duration of the event being measurement in seconds
        :param str note: An optional note the user may include with their measurement
        :param float latitude: Latitude at which the measurement was taken
        :param float longitude: Longitude at which the measurement was taken
        :param str location: Optional human readable name for the location where the measurement was recorded
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param str error: An error message if there is a problem with the measurement
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'client_id', 'connector_id', 'variable_id', 'source_id', 'start_time', 'value', 'unit_id', 'original_value', 'original_unit_id', 'duration', 'note', 'latitude', 'longitude', 'location', 'created_at', 'updated_at', 'error', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_measurements_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/measurements'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'connector_id' in params:
            query_params['connector_id'] = params['connector_id']
        if 'variable_id' in params:
            query_params['variable_id'] = params['variable_id']
        if 'source_id' in params:
            query_params['source_id'] = params['source_id']
        if 'start_time' in params:
            query_params['start_time'] = params['start_time']
        if 'value' in params:
            query_params['value'] = params['value']
        if 'unit_id' in params:
            query_params['unit_id'] = params['unit_id']
        if 'original_value' in params:
            query_params['original_value'] = params['original_value']
        if 'original_unit_id' in params:
            query_params['original_unit_id'] = params['original_unit_id']
        if 'duration' in params:
            query_params['duration'] = params['duration']
        if 'note' in params:
            query_params['note'] = params['note']
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        if 'location' in params:
            query_params['location'] = params['location']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'error' in params:
            query_params['error'] = params['error']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2005',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_tracking_reminders_get(self, **kwargs):
        """
        Get tracking reminders
        Get the variable id, frequency, and default value for the user tracking reminders 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_tracking_reminders_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this trackingReminder
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_tracking_reminders_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_tracking_reminders_get_with_http_info(**kwargs)
            return data

    def v2_application_tracking_reminders_get_with_http_info(self, **kwargs):
        """
        Get tracking reminders
        Get the variable id, frequency, and default value for the user tracking reminders 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_tracking_reminders_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this trackingReminder
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'client_id', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_tracking_reminders_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/trackingReminders'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_updates_get(self, **kwargs):
        """
        Get all Updates
        Get all Updates

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_updates_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: connector_id
        :param int number_of_measurements: number_of_measurements
        :param bool success: success
        :param str message: message
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_updates_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_updates_get_with_http_info(**kwargs)
            return data

    def v2_application_updates_get_with_http_info(self, **kwargs):
        """
        Get all Updates
        Get all Updates

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_updates_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: Application's OAuth2 access token
        :param int connector_id: connector_id
        :param int number_of_measurements: number_of_measurements
        :param bool success: success
        :param str message: message
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'connector_id', 'number_of_measurements', 'success', 'message', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_updates_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/updates'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'connector_id' in params:
            query_params['connector_id'] = params['connector_id']
        if 'number_of_measurements' in params:
            query_params['number_of_measurements'] = params['number_of_measurements']
        if 'success' in params:
            query_params['success'] = params['success']
        if 'message' in params:
            query_params['message'] = params['message']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2006',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_user_variable_relationships_get(self, **kwargs):
        """
        Get all UserVariableRelationships
        Get all UserVariableRelationships

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_user_variable_relationships_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int id: id
        :param str confidence_level: Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param float confidence_score: A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param str direction: Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values.
        :param int duration_of_action: Estimated number of seconds following the onset delay in which a stimulus produces a perceivable effect
        :param str error_message: error_message
        :param int onset_delay: Estimated number of seconds that pass before a stimulus produces a perceivable effect
        :param int outcome_variable_id: Variable ID for the outcome variable
        :param int predictor_variable_id: Variable ID for the predictor variable
        :param int predictor_unit_id: ID for default unit of the predictor variable
        :param float sinn_rank: A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting.
        :param str strength_level: Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores.
        :param float strength_score: A value represented to the size of the effect which the predictor appears to have on the outcome.
        :param str vote: vote
        :param float value_predicting_high_outcome: Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value
        :param float value_predicting_low_outcome: Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_user_variable_relationships_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_user_variable_relationships_get_with_http_info(**kwargs)
            return data

    def v2_application_user_variable_relationships_get_with_http_info(self, **kwargs):
        """
        Get all UserVariableRelationships
        Get all UserVariableRelationships

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_user_variable_relationships_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int id: id
        :param str confidence_level: Our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param float confidence_score: A quantitative representation of our confidence that a consistent predictive relationship exists based on the amount of evidence, reproducibility, and other factors
        :param str direction: Direction is positive if higher predictor values generally precede higher outcome values. Direction is negative if higher predictor values generally precede lower outcome values.
        :param int duration_of_action: Estimated number of seconds following the onset delay in which a stimulus produces a perceivable effect
        :param str error_message: error_message
        :param int onset_delay: Estimated number of seconds that pass before a stimulus produces a perceivable effect
        :param int outcome_variable_id: Variable ID for the outcome variable
        :param int predictor_variable_id: Variable ID for the predictor variable
        :param int predictor_unit_id: ID for default unit of the predictor variable
        :param float sinn_rank: A value representative of the relevance of this predictor relative to other predictors of this outcome.  Usually used for relevancy sorting.
        :param str strength_level: Can be weak, medium, or strong based on the size of the effect which the predictor appears to have on the outcome relative to other variable relationship strength scores.
        :param float strength_score: A value represented to the size of the effect which the predictor appears to have on the outcome.
        :param str vote: vote
        :param float value_predicting_high_outcome: Value for the predictor variable (in it's default unit) which typically precedes an above average outcome value
        :param float value_predicting_low_outcome: Value for the predictor variable (in it's default unit) which typically precedes a below average outcome value
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'id', 'confidence_level', 'confidence_score', 'direction', 'duration_of_action', 'error_message', 'onset_delay', 'outcome_variable_id', 'predictor_variable_id', 'predictor_unit_id', 'sinn_rank', 'strength_level', 'strength_score', 'vote', 'value_predicting_high_outcome', 'value_predicting_low_outcome', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_user_variable_relationships_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/userVariableRelationships'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'confidence_level' in params:
            query_params['confidence_level'] = params['confidence_level']
        if 'confidence_score' in params:
            query_params['confidence_score'] = params['confidence_score']
        if 'direction' in params:
            query_params['direction'] = params['direction']
        if 'duration_of_action' in params:
            query_params['duration_of_action'] = params['duration_of_action']
        if 'error_message' in params:
            query_params['error_message'] = params['error_message']
        if 'onset_delay' in params:
            query_params['onset_delay'] = params['onset_delay']
        if 'outcome_variable_id' in params:
            query_params['outcome_variable_id'] = params['outcome_variable_id']
        if 'predictor_variable_id' in params:
            query_params['predictor_variable_id'] = params['predictor_variable_id']
        if 'predictor_unit_id' in params:
            query_params['predictor_unit_id'] = params['predictor_unit_id']
        if 'sinn_rank' in params:
            query_params['sinn_rank'] = params['sinn_rank']
        if 'strength_level' in params:
            query_params['strength_level'] = params['strength_level']
        if 'strength_score' in params:
            query_params['strength_score'] = params['strength_score']
        if 'vote' in params:
            query_params['vote'] = params['vote']
        if 'value_predicting_high_outcome' in params:
            query_params['value_predicting_high_outcome'] = params['value_predicting_high_outcome']
        if 'value_predicting_low_outcome' in params:
            query_params['value_predicting_low_outcome'] = params['value_predicting_low_outcome']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2007',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_user_variables_get(self, **kwargs):
        """
        Get all UserVariables
        Get all UserVariables

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_user_variables_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this user variable
        :param int parent_id: ID of the parent variable if this variable has any parent
        :param int variable_id: ID of variable
        :param int default_unit_id: D of unit to use for this variable
        :param float minimum_allowed_value: Minimum reasonable value for this variable (uses default unit)
        :param float maximum_allowed_value: Maximum reasonable value for this variable (uses default unit)
        :param float filling_value: Value for replacing null measurements
        :param int join_with: The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables
        :param int onset_delay: Estimated number of seconds that pass before a stimulus produces a perceivable effect
        :param int duration_of_action: Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect
        :param int variable_category_id: ID of variable category
        :param int updated: updated
        :param int public: Is variable public
        :param bool cause_only: A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user
        :param str filling_type: 0 -> No filling, 1 -> Use filling-value
        :param int number_of_measurements: Number of measurements
        :param int number_of_processed_measurements: Number of processed measurements
        :param int measurements_at_last_analysis: Number of measurements at last analysis
        :param int last_unit_id: ID of last Unit
        :param int last_original_unit_id: ID of last original Unit
        :param int last_original_value: Last original value which is stored
        :param float last_value: Last Value
        :param int last_source_id: ID of last source
        :param int number_of_correlations: Number of correlations for this variable
        :param str status: status
        :param str error_message: error_message
        :param str last_successful_update_time: When this variable or its settings were last updated
        :param float standard_deviation: Standard deviation
        :param float variance: Variance
        :param float minimum_recorded_value: Minimum recorded value of this variable
        :param float maximum_recorded_value: Maximum recorded value of this variable
        :param float mean: Mean
        :param float median: Median
        :param int most_common_unit_id: Most common Unit ID
        :param float most_common_value: Most common value
        :param float number_of_unique_daily_values: Number of unique daily values
        :param int number_of_changes: Number of changes
        :param float skewness: Skewness
        :param float kurtosis: Kurtosis
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param str location: Location
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param bool outcome: Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables
        :param str sources: Comma-separated list of source names to limit variables to those sources
        :param int earliest_source_time: Earliest source time
        :param int latest_source_time: Latest source time
        :param int earliest_measurement_time: Earliest measurement time
        :param int latest_measurement_time: Latest measurement time
        :param int earliest_filling_time: Earliest filling time
        :param int latest_filling_time: Latest filling time
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_user_variables_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_user_variables_get_with_http_info(**kwargs)
            return data

    def v2_application_user_variables_get_with_http_info(self, **kwargs):
        """
        Get all UserVariables
        Get all UserVariables

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_user_variables_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this user variable
        :param int parent_id: ID of the parent variable if this variable has any parent
        :param int variable_id: ID of variable
        :param int default_unit_id: D of unit to use for this variable
        :param float minimum_allowed_value: Minimum reasonable value for this variable (uses default unit)
        :param float maximum_allowed_value: Maximum reasonable value for this variable (uses default unit)
        :param float filling_value: Value for replacing null measurements
        :param int join_with: The Variable this Variable should be joined with. If the variable is joined with some other variable then it is not shown to user in the list of variables
        :param int onset_delay: Estimated number of seconds that pass before a stimulus produces a perceivable effect
        :param int duration_of_action: Estimated duration of time following the onset delay in which a stimulus produces a perceivable effect
        :param int variable_category_id: ID of variable category
        :param int updated: updated
        :param int public: Is variable public
        :param bool cause_only: A value of 1 indicates that this variable is generally a cause in a causal relationship.  An example of a causeOnly variable would be a variable such as Cloud Cover which would generally not be influenced by the behaviour of the user
        :param str filling_type: 0 -> No filling, 1 -> Use filling-value
        :param int number_of_measurements: Number of measurements
        :param int number_of_processed_measurements: Number of processed measurements
        :param int measurements_at_last_analysis: Number of measurements at last analysis
        :param int last_unit_id: ID of last Unit
        :param int last_original_unit_id: ID of last original Unit
        :param int last_original_value: Last original value which is stored
        :param float last_value: Last Value
        :param int last_source_id: ID of last source
        :param int number_of_correlations: Number of correlations for this variable
        :param str status: status
        :param str error_message: error_message
        :param str last_successful_update_time: When this variable or its settings were last updated
        :param float standard_deviation: Standard deviation
        :param float variance: Variance
        :param float minimum_recorded_value: Minimum recorded value of this variable
        :param float maximum_recorded_value: Maximum recorded value of this variable
        :param float mean: Mean
        :param float median: Median
        :param int most_common_unit_id: Most common Unit ID
        :param float most_common_value: Most common value
        :param float number_of_unique_daily_values: Number of unique daily values
        :param int number_of_changes: Number of changes
        :param float skewness: Skewness
        :param float kurtosis: Kurtosis
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param str location: Location
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param bool outcome: Outcome variables (those with `outcome` == 1) are variables for which a human would generally want to identify the influencing factors.  These include symptoms of illness, physique, mood, cognitive performance, etc.  Generally correlation calculations are only performed on outcome variables
        :param str sources: Comma-separated list of source names to limit variables to those sources
        :param int earliest_source_time: Earliest source time
        :param int latest_source_time: Latest source time
        :param int earliest_measurement_time: Earliest measurement time
        :param int latest_measurement_time: Latest measurement time
        :param int earliest_filling_time: Earliest filling time
        :param int latest_filling_time: Latest filling time
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'client_id', 'parent_id', 'variable_id', 'default_unit_id', 'minimum_allowed_value', 'maximum_allowed_value', 'filling_value', 'join_with', 'onset_delay', 'duration_of_action', 'variable_category_id', 'updated', 'public', 'cause_only', 'filling_type', 'number_of_measurements', 'number_of_processed_measurements', 'measurements_at_last_analysis', 'last_unit_id', 'last_original_unit_id', 'last_original_value', 'last_value', 'last_source_id', 'number_of_correlations', 'status', 'error_message', 'last_successful_update_time', 'standard_deviation', 'variance', 'minimum_recorded_value', 'maximum_recorded_value', 'mean', 'median', 'most_common_unit_id', 'most_common_value', 'number_of_unique_daily_values', 'number_of_changes', 'skewness', 'kurtosis', 'latitude', 'longitude', 'location', 'created_at', 'updated_at', 'outcome', 'sources', 'earliest_source_time', 'latest_source_time', 'earliest_measurement_time', 'latest_measurement_time', 'earliest_filling_time', 'latest_filling_time', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_user_variables_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/userVariables'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'parent_id' in params:
            query_params['parent_id'] = params['parent_id']
        if 'variable_id' in params:
            query_params['variable_id'] = params['variable_id']
        if 'default_unit_id' in params:
            query_params['default_unit_id'] = params['default_unit_id']
        if 'minimum_allowed_value' in params:
            query_params['minimum_allowed_value'] = params['minimum_allowed_value']
        if 'maximum_allowed_value' in params:
            query_params['maximum_allowed_value'] = params['maximum_allowed_value']
        if 'filling_value' in params:
            query_params['filling_value'] = params['filling_value']
        if 'join_with' in params:
            query_params['join_with'] = params['join_with']
        if 'onset_delay' in params:
            query_params['onset_delay'] = params['onset_delay']
        if 'duration_of_action' in params:
            query_params['duration_of_action'] = params['duration_of_action']
        if 'variable_category_id' in params:
            query_params['variable_category_id'] = params['variable_category_id']
        if 'updated' in params:
            query_params['updated'] = params['updated']
        if 'public' in params:
            query_params['public'] = params['public']
        if 'cause_only' in params:
            query_params['cause_only'] = params['cause_only']
        if 'filling_type' in params:
            query_params['filling_type'] = params['filling_type']
        if 'number_of_measurements' in params:
            query_params['number_of_measurements'] = params['number_of_measurements']
        if 'number_of_processed_measurements' in params:
            query_params['number_of_processed_measurements'] = params['number_of_processed_measurements']
        if 'measurements_at_last_analysis' in params:
            query_params['measurements_at_last_analysis'] = params['measurements_at_last_analysis']
        if 'last_unit_id' in params:
            query_params['last_unit_id'] = params['last_unit_id']
        if 'last_original_unit_id' in params:
            query_params['last_original_unit_id'] = params['last_original_unit_id']
        if 'last_original_value' in params:
            query_params['last_original_value'] = params['last_original_value']
        if 'last_value' in params:
            query_params['last_value'] = params['last_value']
        if 'last_source_id' in params:
            query_params['last_source_id'] = params['last_source_id']
        if 'number_of_correlations' in params:
            query_params['number_of_correlations'] = params['number_of_correlations']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'error_message' in params:
            query_params['error_message'] = params['error_message']
        if 'last_successful_update_time' in params:
            query_params['last_successful_update_time'] = params['last_successful_update_time']
        if 'standard_deviation' in params:
            query_params['standard_deviation'] = params['standard_deviation']
        if 'variance' in params:
            query_params['variance'] = params['variance']
        if 'minimum_recorded_value' in params:
            query_params['minimum_recorded_value'] = params['minimum_recorded_value']
        if 'maximum_recorded_value' in params:
            query_params['maximum_recorded_value'] = params['maximum_recorded_value']
        if 'mean' in params:
            query_params['mean'] = params['mean']
        if 'median' in params:
            query_params['median'] = params['median']
        if 'most_common_unit_id' in params:
            query_params['most_common_unit_id'] = params['most_common_unit_id']
        if 'most_common_value' in params:
            query_params['most_common_value'] = params['most_common_value']
        if 'number_of_unique_daily_values' in params:
            query_params['number_of_unique_daily_values'] = params['number_of_unique_daily_values']
        if 'number_of_changes' in params:
            query_params['number_of_changes'] = params['number_of_changes']
        if 'skewness' in params:
            query_params['skewness'] = params['skewness']
        if 'kurtosis' in params:
            query_params['kurtosis'] = params['kurtosis']
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        if 'location' in params:
            query_params['location'] = params['location']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'outcome' in params:
            query_params['outcome'] = params['outcome']
        if 'sources' in params:
            query_params['sources'] = params['sources']
        if 'earliest_source_time' in params:
            query_params['earliest_source_time'] = params['earliest_source_time']
        if 'latest_source_time' in params:
            query_params['latest_source_time'] = params['latest_source_time']
        if 'earliest_measurement_time' in params:
            query_params['earliest_measurement_time'] = params['earliest_measurement_time']
        if 'latest_measurement_time' in params:
            query_params['latest_measurement_time'] = params['latest_measurement_time']
        if 'earliest_filling_time' in params:
            query_params['earliest_filling_time'] = params['earliest_filling_time']
        if 'latest_filling_time' in params:
            query_params['latest_filling_time'] = params['latest_filling_time']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2008',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_variable_user_sources_get(self, **kwargs):
        """
        Get all VariableUserSources
        Get all VariableUserSources

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_variable_user_sources_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int variable_id: ID of variable
        :param int timestamp: Time that this measurement occurred Uses epoch minute (epoch time divided by 60)
        :param int earliest_measurement_time: Earliest measurement time
        :param int latest_measurement_time: Latest measurement time
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_variable_user_sources_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_variable_user_sources_get_with_http_info(**kwargs)
            return data

    def v2_application_variable_user_sources_get_with_http_info(self, **kwargs):
        """
        Get all VariableUserSources
        Get all VariableUserSources

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_variable_user_sources_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param int variable_id: ID of variable
        :param int timestamp: Time that this measurement occurred Uses epoch minute (epoch time divided by 60)
        :param int earliest_measurement_time: Earliest measurement time
        :param int latest_measurement_time: Latest measurement time
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'variable_id', 'timestamp', 'earliest_measurement_time', 'latest_measurement_time', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_variable_user_sources_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/variableUserSources'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'variable_id' in params:
            query_params['variable_id'] = params['variable_id']
        if 'timestamp' in params:
            query_params['timestamp'] = params['timestamp']
        if 'earliest_measurement_time' in params:
            query_params['earliest_measurement_time'] = params['earliest_measurement_time']
        if 'latest_measurement_time' in params:
            query_params['latest_measurement_time'] = params['latest_measurement_time']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2009',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v2_application_votes_get(self, **kwargs):
        """
        Get all Votes
        Get all Votes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_votes_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this vote
        :param int cause_id: ID of predictor variable
        :param int effect_id: ID of outcome variable
        :param int value: Value of Vote. 1 is for upvote. 0 is for downvote.  Otherwise, there is no vote.
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v2_application_votes_get_with_http_info(**kwargs)
        else:
            (data) = self.v2_application_votes_get_with_http_info(**kwargs)
            return data

    def v2_application_votes_get_with_http_info(self, **kwargs):
        """
        Get all Votes
        Get all Votes

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v2_application_votes_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token: User's OAuth2 access token
        :param str client_id: The ID of the client application which last created or updated this vote
        :param int cause_id: ID of predictor variable
        :param int effect_id: ID of outcome variable
        :param int value: Value of Vote. 1 is for upvote. 0 is for downvote.  Otherwise, there is no vote.
        :param str created_at: When the record was first created. Use ISO 8601 datetime format 
        :param str updated_at: When the record was last updated. Use ISO 8601 datetime format 
        :param int limit: The LIMIT is used to limit the number of results returned. So if you have 1000 results, but only want to the first 10, you would set this to 10 and offset to 0. The maximum limit is 200 records.
        :param int offset: OFFSET says to skip that many rows before beginning to return rows to the client. OFFSET 0 is the same as omitting the OFFSET clause. If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
        :param str sort: Sort by given field. If the field is prefixed with '-', it will sort in descending order.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'client_id', 'cause_id', 'effect_id', 'value', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_application_votes_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v2/application/votes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'cause_id' in params:
            query_params['cause_id'] = params['cause_id']
        if 'effect_id' in params:
            query_params['effect_id'] = params['effect_id']
        if 'value' in params:
            query_params['value'] = params['value']
        if 'created_at' in params:
            query_params['created_at'] = params['created_at']
        if 'updated_at' in params:
            query_params['updated_at'] = params['updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2', 'internalApiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20010',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))