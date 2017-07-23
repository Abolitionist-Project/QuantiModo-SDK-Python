# coding: utf-8

"""
    QuantiModo

    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications. [Learn about QuantiModo](https://quantimo.do), check out our [docs](https://github.com/QuantiModo/docs) or contact us at [help.quantimo.do](https://help.quantimo.do). 

    OpenAPI spec version: 2.0
    
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


class TagsApi(object):
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

    def v1_user_tags_delete_post(self, tagged_variable_id, tag_variable_id, **kwargs):
        """
        Delete user tag or ingredient
        Delete previously created user tags or ingredients.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_tags_delete_post(tagged_variable_id, tag_variable_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int tagged_variable_id: This is the id of the variable being tagged with an ingredient or something. (required)
        :param int tag_variable_id: This is the id of the ingredient variable whose value is determined based on the value of the tagged variable. (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_user_tags_delete_post_with_http_info(tagged_variable_id, tag_variable_id, **kwargs)
        else:
            (data) = self.v1_user_tags_delete_post_with_http_info(tagged_variable_id, tag_variable_id, **kwargs)
            return data

    def v1_user_tags_delete_post_with_http_info(self, tagged_variable_id, tag_variable_id, **kwargs):
        """
        Delete user tag or ingredient
        Delete previously created user tags or ingredients.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_tags_delete_post_with_http_info(tagged_variable_id, tag_variable_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int tagged_variable_id: This is the id of the variable being tagged with an ingredient or something. (required)
        :param int tag_variable_id: This is the id of the ingredient variable whose value is determined based on the value of the tagged variable. (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tagged_variable_id', 'tag_variable_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_tags_delete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tagged_variable_id' is set
        if ('tagged_variable_id' not in params) or (params['tagged_variable_id'] is None):
            raise ValueError("Missing the required parameter `tagged_variable_id` when calling `v1_user_tags_delete_post`")
        # verify the required parameter 'tag_variable_id' is set
        if ('tag_variable_id' not in params) or (params['tag_variable_id'] is None):
            raise ValueError("Missing the required parameter `tag_variable_id` when calling `v1_user_tags_delete_post`")


        collection_formats = {}

        resource_path = '/v1/userTags/delete'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tagged_variable_id' in params:
            query_params['taggedVariableId'] = params['tagged_variable_id']
        if 'tag_variable_id' in params:
            query_params['tagVariableId'] = params['tag_variable_id']

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
        auth_settings = ['access_token', 'quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def v1_user_tags_post(self, body, **kwargs):
        """
        Post or update user tags or ingredients
        This endpoint allows users to tag foods with their ingredients.  This information will then be used to infer the user intake of the different ingredients by just entering the foods. The inferred intake levels will then be used to determine the effects of different nutrients on the user during analysis.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_tags_post(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserTag body: Contains the new user tag data (required)
        :param str access_token: User's OAuth2 access token
        :param int user_id: User's id
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_user_tags_post_with_http_info(body, **kwargs)
        else:
            (data) = self.v1_user_tags_post_with_http_info(body, **kwargs)
            return data

    def v1_user_tags_post_with_http_info(self, body, **kwargs):
        """
        Post or update user tags or ingredients
        This endpoint allows users to tag foods with their ingredients.  This information will then be used to infer the user intake of the different ingredients by just entering the foods. The inferred intake levels will then be used to determine the effects of different nutrients on the user during analysis.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_tags_post_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserTag body: Contains the new user tag data (required)
        :param str access_token: User's OAuth2 access token
        :param int user_id: User's id
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'access_token', 'user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_tags_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_user_tags_post`")


        collection_formats = {}

        resource_path = '/v1/userTags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']
        if 'user_id' in params:
            query_params['userId'] = params['user_id']

        header_params = {}

        form_params = []
        local_var_files = {}

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
        auth_settings = ['access_token', 'quantimodo_oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CommonResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
