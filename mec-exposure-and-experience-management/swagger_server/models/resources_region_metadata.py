# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.types_region_id import TypesRegionId  # noqa: F401,E501
from swagger_server import util


class ResourcesRegionMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, region_id: TypesRegionId=None, name: str=None, country_code: str=None, metro: str=None, area: str=None):  # noqa: E501
        """ResourcesRegionMetadata - a model defined in Swagger

        :param region_id: The region_id of this ResourcesRegionMetadata.  # noqa: E501
        :type region_id: TypesRegionId
        :param name: The name of this ResourcesRegionMetadata.  # noqa: E501
        :type name: str
        :param country_code: The country_code of this ResourcesRegionMetadata.  # noqa: E501
        :type country_code: str
        :param metro: The metro of this ResourcesRegionMetadata.  # noqa: E501
        :type metro: str
        :param area: The area of this ResourcesRegionMetadata.  # noqa: E501
        :type area: str
        """
        self.swagger_types = {
            'region_id': TypesRegionId,
            'name': str,
            'country_code': str,
            'metro': str,
            'area': str
        }

        self.attribute_map = {
            'region_id': 'regionId',
            'name': 'name',
            'country_code': 'countryCode',
            'metro': 'metro',
            'area': 'area'
        }
        self._region_id = region_id
        self._name = name
        self._country_code = country_code
        self._metro = metro
        self._area = area

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesRegionMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resources_region_metadata of this ResourcesRegionMetadata.  # noqa: E501
        :rtype: ResourcesRegionMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def region_id(self) -> TypesRegionId:
        """Gets the region_id of this ResourcesRegionMetadata.


        :return: The region_id of this ResourcesRegionMetadata.
        :rtype: TypesRegionId
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id: TypesRegionId):
        """Sets the region_id of this ResourcesRegionMetadata.


        :param region_id: The region_id of this ResourcesRegionMetadata.
        :type region_id: TypesRegionId
        """

        self._region_id = region_id

    @property
    def name(self) -> str:
        """Gets the name of this ResourcesRegionMetadata.


        :return: The name of this ResourcesRegionMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ResourcesRegionMetadata.


        :param name: The name of this ResourcesRegionMetadata.
        :type name: str
        """

        self._name = name

    @property
    def country_code(self) -> str:
        """Gets the country_code of this ResourcesRegionMetadata.


        :return: The country_code of this ResourcesRegionMetadata.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """Sets the country_code of this ResourcesRegionMetadata.


        :param country_code: The country_code of this ResourcesRegionMetadata.
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def metro(self) -> str:
        """Gets the metro of this ResourcesRegionMetadata.


        :return: The metro of this ResourcesRegionMetadata.
        :rtype: str
        """
        return self._metro

    @metro.setter
    def metro(self, metro: str):
        """Sets the metro of this ResourcesRegionMetadata.


        :param metro: The metro of this ResourcesRegionMetadata.
        :type metro: str
        """

        self._metro = metro

    @property
    def area(self) -> str:
        """Gets the area of this ResourcesRegionMetadata.


        :return: The area of this ResourcesRegionMetadata.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area: str):
        """Sets the area of this ResourcesRegionMetadata.


        :param area: The area of this ResourcesRegionMetadata.
        :type area: str
        """

        self._area = area