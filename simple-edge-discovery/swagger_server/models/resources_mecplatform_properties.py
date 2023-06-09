# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResourcesMecplatformProperties(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, data: object=None):  # noqa: E501
        """ResourcesMecplatformProperties - a model defined in Swagger

        :param type: The type of this ResourcesMecplatformProperties.  # noqa: E501
        :type type: str
        :param data: The data of this ResourcesMecplatformProperties.  # noqa: E501
        :type data: object
        """
        self.swagger_types = {
            'type': str,
            'data': object
        }

        self.attribute_map = {
            'type': 'type',
            'data': 'data'
        }
        self._type = type
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesMecplatformProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resources_mecplatform_properties of this ResourcesMecplatformProperties.  # noqa: E501
        :rtype: ResourcesMecplatformProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ResourcesMecplatformProperties.


        :return: The type of this ResourcesMecplatformProperties.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ResourcesMecplatformProperties.


        :param type: The type of this ResourcesMecplatformProperties.
        :type type: str
        """

        self._type = type

    @property
    def data(self) -> object:
        """Gets the data of this ResourcesMecplatformProperties.


        :return: The data of this ResourcesMecplatformProperties.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data: object):
        """Sets the data of this ResourcesMecplatformProperties.


        :param data: The data of this ResourcesMecplatformProperties.
        :type data: object
        """

        self._data = data
