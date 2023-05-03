# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.resources_mec_platform import ResourcesMecPlatform  # noqa: F401,E501
from swagger_server.models.resources_zone_metadata import ResourcesZoneMetadata  # noqa: F401,E501
from swagger_server.models.types_region_id import TypesRegionId  # noqa: F401,E501
from swagger_server.models.types_zone_id import TypesZoneId  # noqa: F401,E501
from swagger_server import util


class ResourcesZone(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zone_id: TypesZoneId=None, region_id: TypesRegionId=None, mec_platforms: List[ResourcesMecPlatform]=None):  # noqa: E501
        """ResourcesZone - a model defined in Swagger

        :param zone_id: The zone_id of this ResourcesZone.  # noqa: E501
        :type zone_id: TypesZoneId
        :param region_id: The region_id of this ResourcesZone.  # noqa: E501
        :type region_id: TypesRegionId
        :param mec_platforms: The mec_platforms of this ResourcesZone.  # noqa: E501
        :type mec_platforms: List[ResourcesMecPlatform]
        """
        self.swagger_types = {
            'zone_id': TypesZoneId,
            'region_id': TypesRegionId,
            'mec_platforms': List[ResourcesMecPlatform]
        }

        self.attribute_map = {
            'zone_id': 'zoneId',
            'region_id': 'regionId',
            'mec_platforms': 'mecPlatforms'
        }
        self._zone_id = zone_id
        self._region_id = region_id
        self._mec_platforms = mec_platforms

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesZone':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourcesZone of this ResourcesZone.  # noqa: E501
        :rtype: ResourcesZone
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_id(self) -> TypesZoneId:
        """Gets the zone_id of this ResourcesZone.


        :return: The zone_id of this ResourcesZone.
        :rtype: TypesZoneId
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id: TypesZoneId):
        """Sets the zone_id of this ResourcesZone.


        :param zone_id: The zone_id of this ResourcesZone.
        :type zone_id: TypesZoneId
        """

        self._zone_id = zone_id

    @property
    def region_id(self) -> TypesRegionId:
        """Gets the region_id of this ResourcesZone.


        :return: The region_id of this ResourcesZone.
        :rtype: TypesRegionId
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id: TypesRegionId):
        """Sets the region_id of this ResourcesZone.


        :param region_id: The region_id of this ResourcesZone.
        :type region_id: TypesRegionId
        """

        self._region_id = region_id

    @property
    def mec_platforms(self) -> List[ResourcesMecPlatform]:
        """Gets the mec_platforms of this ResourcesZone.


        :return: The mec_platforms of this ResourcesZone.
        :rtype: List[ResourcesMecPlatform]
        """
        return self._mec_platforms

    @mec_platforms.setter
    def mec_platforms(self, mec_platforms: List[ResourcesMecPlatform]):
        """Sets the mec_platforms of this ResourcesZone.


        :param mec_platforms: The mec_platforms of this ResourcesZone.
        :type mec_platforms: List[ResourcesMecPlatform]
        """

        self._mec_platforms = mec_platforms
