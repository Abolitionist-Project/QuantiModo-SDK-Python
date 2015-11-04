# coding: utf-8

"""
ConnectionApi.py
Copyright 2015 SmartBear Software

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

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ConnectionApi(object):
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

    def connections_get(self, **kwargs):
        """
        Get all Connections
        Get all Connections

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connections_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: user_id
        :param int connector_id: connector_id
        :param str connect_status: connect_status
        :param str connect_error: connect_error
        :param str update_requested_at: update_requested_at
        :param str update_status: update_status
        :param str update_error: update_error
        :param str last_successful_updated_at: last_successful_updated_at
        :param str created_at: created_at
        :param str updated_at: updated_at
        :param int limit: limit
        :param int offset: offset
        :param str sort: sort
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'connector_id', 'connect_status', 'connect_error', 'update_requested_at', 'update_status', 'update_error', 'last_successful_updated_at', 'created_at', 'updated_at', 'limit', 'offset', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connections_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connections'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']
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

        form_params = {}
        files = {}

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
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2003',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connections_post(self, **kwargs):
        """
        Store Connection
        Store Connection

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connections_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Connection body: Connection that should be stored
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connections_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connections'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2004',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connections_id_get(self, id, **kwargs):
        """
        Get Connection
        Get Connection

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connections_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Connection (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `connections_id_get`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connections_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connections/{id}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

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
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2004',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connections_id_put(self, id, **kwargs):
        """
        Update Connection
        Update Connection

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connections_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Connection (required)
        :param Connection body: Connection that should be updated
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `connections_id_put`")

        all_params = ['id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connections_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connections/{id}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def connections_id_delete(self, id, **kwargs):
        """
        Delete Connection
        Delete Connection

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.connections_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: id of Connection (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `connections_id_delete`")

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connections_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/connections/{id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

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
        auth_settings = ['quantimodo_oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response