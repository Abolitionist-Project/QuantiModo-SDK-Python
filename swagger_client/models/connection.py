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


class Connection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Connection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'user_id': 'int',
            'connector_id': 'int',
            'connect_status': 'str',
            'connect_error': 'str',
            'update_requested_at': 'datetime',
            'update_status': 'str',
            'update_error': 'str',
            'last_successful_updated_at': 'datetime',
            'created_at': 'datetime',
            'updated_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'connector_id': 'connector_id',
            'connect_status': 'connect_status',
            'connect_error': 'connect_error',
            'update_requested_at': 'update_requested_at',
            'update_status': 'update_status',
            'update_error': 'update_error',
            'last_successful_updated_at': 'last_successful_updated_at',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = None
        self._user_id = None
        self._connector_id = None
        self._connect_status = None
        self._connect_error = None
        self._update_requested_at = None
        self._update_status = None
        self._update_error = None
        self._last_successful_updated_at = None
        self._created_at = None
        self._updated_at = None

    @property
    def id(self):
        """
        Gets the id of this Connection.
        id

        :return: The id of this Connection.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Connection.
        id

        :param id: The id of this Connection.
        :type: int
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this Connection.
        user_id

        :return: The user_id of this Connection.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Connection.
        user_id

        :param user_id: The user_id of this Connection.
        :type: int
        """
        self._user_id = user_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this Connection.
        connector_id

        :return: The connector_id of this Connection.
        :rtype: int
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this Connection.
        connector_id

        :param connector_id: The connector_id of this Connection.
        :type: int
        """
        self._connector_id = connector_id

    @property
    def connect_status(self):
        """
        Gets the connect_status of this Connection.
        connect_status

        :return: The connect_status of this Connection.
        :rtype: str
        """
        return self._connect_status

    @connect_status.setter
    def connect_status(self, connect_status):
        """
        Sets the connect_status of this Connection.
        connect_status

        :param connect_status: The connect_status of this Connection.
        :type: str
        """
        self._connect_status = connect_status

    @property
    def connect_error(self):
        """
        Gets the connect_error of this Connection.
        connect_error

        :return: The connect_error of this Connection.
        :rtype: str
        """
        return self._connect_error

    @connect_error.setter
    def connect_error(self, connect_error):
        """
        Sets the connect_error of this Connection.
        connect_error

        :param connect_error: The connect_error of this Connection.
        :type: str
        """
        self._connect_error = connect_error

    @property
    def update_requested_at(self):
        """
        Gets the update_requested_at of this Connection.
        update_requested_at

        :return: The update_requested_at of this Connection.
        :rtype: datetime
        """
        return self._update_requested_at

    @update_requested_at.setter
    def update_requested_at(self, update_requested_at):
        """
        Sets the update_requested_at of this Connection.
        update_requested_at

        :param update_requested_at: The update_requested_at of this Connection.
        :type: datetime
        """
        self._update_requested_at = update_requested_at

    @property
    def update_status(self):
        """
        Gets the update_status of this Connection.
        update_status

        :return: The update_status of this Connection.
        :rtype: str
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        """
        Sets the update_status of this Connection.
        update_status

        :param update_status: The update_status of this Connection.
        :type: str
        """
        self._update_status = update_status

    @property
    def update_error(self):
        """
        Gets the update_error of this Connection.
        update_error

        :return: The update_error of this Connection.
        :rtype: str
        """
        return self._update_error

    @update_error.setter
    def update_error(self, update_error):
        """
        Sets the update_error of this Connection.
        update_error

        :param update_error: The update_error of this Connection.
        :type: str
        """
        self._update_error = update_error

    @property
    def last_successful_updated_at(self):
        """
        Gets the last_successful_updated_at of this Connection.
        last_successful_updated_at

        :return: The last_successful_updated_at of this Connection.
        :rtype: datetime
        """
        return self._last_successful_updated_at

    @last_successful_updated_at.setter
    def last_successful_updated_at(self, last_successful_updated_at):
        """
        Sets the last_successful_updated_at of this Connection.
        last_successful_updated_at

        :param last_successful_updated_at: The last_successful_updated_at of this Connection.
        :type: datetime
        """
        self._last_successful_updated_at = last_successful_updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this Connection.
        created_at

        :return: The created_at of this Connection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Connection.
        created_at

        :param created_at: The created_at of this Connection.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Connection.
        updated_at

        :return: The updated_at of this Connection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Connection.
        updated_at

        :param updated_at: The updated_at of this Connection.
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