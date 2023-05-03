# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResourcesServiceEndpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, uri: str=None, fqdn: str=None, ipv4_address: str=None, ipv6_address: str=None, port: int=None):  # noqa: E501
        """ResourcesServiceEndpoint - a model defined in Swagger

        :param uri: The uri of this ResourcesServiceEndpoint.  # noqa: E501
        :type uri: str
        :param fqdn: The fqdn of this ResourcesServiceEndpoint.  # noqa: E501
        :type fqdn: str
        :param ipv4_address: The ipv4_address of this ResourcesServiceEndpoint.  # noqa: E501
        :type ipv4_address: str
        :param ipv6_address: The ipv6_address of this ResourcesServiceEndpoint.  # noqa: E501
        :type ipv6_address: str
        :param port: The port of this ResourcesServiceEndpoint.  # noqa: E501
        :type port: int
        """
        self.swagger_types = {
            'uri': str,
            'fqdn': str,
            'ipv4_address': str,
            'ipv6_address': str,
            'port': int
        }

        self.attribute_map = {
            'uri': 'uri',
            'fqdn': 'fqdn',
            'ipv4_address': 'ipv4Address',
            'ipv6_address': 'ipv6Address',
            'port': 'port'
        }
        self._uri = uri
        self._fqdn = fqdn
        self._ipv4_address = ipv4_address
        self._ipv6_address = ipv6_address
        self._port = port

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesServiceEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourcesServiceEndpoint of this ResourcesServiceEndpoint.  # noqa: E501
        :rtype: ResourcesServiceEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self) -> str:
        """Gets the uri of this ResourcesServiceEndpoint.

        URI of Service Endpoint if available  # noqa: E501

        :return: The uri of this ResourcesServiceEndpoint.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this ResourcesServiceEndpoint.

        URI of Service Endpoint if available  # noqa: E501

        :param uri: The uri of this ResourcesServiceEndpoint.
        :type uri: str
        """

        self._uri = uri

    @property
    def fqdn(self) -> str:
        """Gets the fqdn of this ResourcesServiceEndpoint.

        FQDN of Service Endpoint if available  # noqa: E501

        :return: The fqdn of this ResourcesServiceEndpoint.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn: str):
        """Sets the fqdn of this ResourcesServiceEndpoint.

        FQDN of Service Endpoint if available  # noqa: E501

        :param fqdn: The fqdn of this ResourcesServiceEndpoint.
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def ipv4_address(self) -> str:
        """Gets the ipv4_address of this ResourcesServiceEndpoint.

        IPv4 Address of Service Endpoint if available  # noqa: E501

        :return: The ipv4_address of this ResourcesServiceEndpoint.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address: str):
        """Sets the ipv4_address of this ResourcesServiceEndpoint.

        IPv4 Address of Service Endpoint if available  # noqa: E501

        :param ipv4_address: The ipv4_address of this ResourcesServiceEndpoint.
        :type ipv4_address: str
        """

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self) -> str:
        """Gets the ipv6_address of this ResourcesServiceEndpoint.

        IPv6 Address of Service Endpoint if available  # noqa: E501

        :return: The ipv6_address of this ResourcesServiceEndpoint.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address: str):
        """Sets the ipv6_address of this ResourcesServiceEndpoint.

        IPv6 Address of Service Endpoint if available  # noqa: E501

        :param ipv6_address: The ipv6_address of this ResourcesServiceEndpoint.
        :type ipv6_address: str
        """

        self._ipv6_address = ipv6_address

    @property
    def port(self) -> int:
        """Gets the port of this ResourcesServiceEndpoint.

        Port information of Service Endpoint if IPv4 or IPv6 is mentioned   # noqa: E501

        :return: The port of this ResourcesServiceEndpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this ResourcesServiceEndpoint.

        Port information of Service Endpoint if IPv4 or IPv6 is mentioned   # noqa: E501

        :param port: The port of this ResourcesServiceEndpoint.
        :type port: int
        """

        self._port = port
