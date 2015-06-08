#!/usr/bin/env python
# coding: utf-8

"""
ConnectApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..util import remove_none

from ..swagger import ApiClient

class ConnectApi(object):

    def __init__(self, api_client):
        self.api_client = api_client
    
    def v1_connect/js_get(self, t, **kwargs):
        """
        Get embeddable connect javascript
        Get embeddable connect javascript

        :param str t: User token (required)
        
        :return: None
        """
        
        # verify the required parameter 't' is set
        if t is None:
            raise ValueError("Missing the required parameter `t` when calling `v1_connect/js_get`")
        
        all_params = ['t']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_connect/js_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/connect.js'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict(t=params.get('t')))
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['application/x-javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        
    def v1_connect_mobile_get(self, t, **kwargs):
        """
        Mobile connect page
        Mobile connect page

        :param str t: User token (required)
        
        :return: None
        """
        
        # verify the required parameter 't' is set
        if t is None:
            raise ValueError("Missing the required parameter `t` when calling `v1_connect_mobile_get`")
        
        all_params = ['t']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method v1_connect_mobile_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/connect/mobile'.replace('{format}', 'json')
        method = 'GET'

        path_params = remove_none(dict())
        query_params = remove_none(dict(t=params.get('t')))
        header_params = remove_none(dict())
        form_params = remove_none(dict())
        files = remove_none(dict())
        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = ApiClient.select_header_accept(['text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = ApiClient.select_header_content_type([])

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None)
        









