# coding: utf-8

"""
UserApi.py
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


class UserApi(object):
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
                config.api_client = ApiClient('https://localhost/api')
            self.api_client = config.api_client

    def user_me_get(self, **kwargs):
        """
        Get all available units for variableGet authenticated user
        Returns user info for the currently authenticated user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_me_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_me_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user/me'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

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
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['oauth2']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='User',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def v1_organizations_organization_id_users_post(self, organization_id, body, **kwargs):
        """
        Get user tokens for existing users, create new users
        Get user tokens for existing users, create new users

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_organizations_organization_id_users_post(organization_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int organization_id: Organization ID (required)
        :param UserTokenRequest body: Provides organization token and user ID (required)
        :return: UserTokenSuccessfulResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        # verify the required parameter 'organization_id' is set
        if organization_id is None:
            raise ValueError("Missing the required parameter `organization_id` when calling `v1_organizations_organization_id_users_post`")
        # verify the required parameter 'body' is set
        if body is None:
            raise ValueError("Missing the required parameter `body` when calling `v1_organizations_organization_id_users_post`")

        all_params = ['organization_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_organizations_organization_id_users_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/organizations/{organizationId}/users'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        if 'organization_id' in params:
            path_params['organizationId'] = params['organization_id']

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
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserTokenSuccessfulResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
