# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Source(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Source - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'client_id': 'str',
            'name': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'client_id': 'client_id',
            'name': 'name',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = None
        self._client_id = None
        self._name = None
        self._created_at = None
        self._updated_at = None

    @property
    def id(self):
        """
        Gets the id of this Source.
        id

        :return: The id of this Source.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Source.
        id

        :param id: The id of this Source.
        :type: int
        """
        self._id = id

    @property
    def client_id(self):
        """
        Gets the client_id of this Source.
        client_id

        :return: The client_id of this Source.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this Source.
        client_id

        :param client_id: The client_id of this Source.
        :type: str
        """
        self._client_id = client_id

    @property
    def name(self):
        """
        Gets the name of this Source.
        Name of the application or device

        :return: The name of this Source.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Source.
        Name of the application or device

        :param name: The name of this Source.
        :type: str
        """
        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this Source.
        created_at

        :return: The created_at of this Source.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Source.
        created_at

        :param created_at: The created_at of this Source.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Source.
        updated_at

        :return: The updated_at of this Source.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Source.
        updated_at

        :param updated_at: The updated_at of this Source.
        :type: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
