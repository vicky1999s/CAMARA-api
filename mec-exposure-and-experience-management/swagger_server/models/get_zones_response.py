# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.resources_zone_metadata import ResourcesZoneMetadata  # noqa: F401,E501
from swagger_server.models.one_of_get_zones_response_links_items import OneOfGetZonesResponseLinksItems  # noqa: F401,E501
from swagger_server import util


class GetZonesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zones: List[ResourcesZoneMetadata]=None, links: List[OneOfGetZonesResponseLinksItems]=None):  # noqa: E501
        """GetZonesResponse - a model defined in Swagger

        :param zones: The zones of this GetZonesResponse.  # noqa: E501
        :type zones: List[ResourcesZoneMetadata]
        :param links: The links of this GetZonesResponse.  # noqa: E501
        :type links: List[OneOfGetZonesResponseLinksItems]
        """
        self.swagger_types = {
            'zones': List[ResourcesZoneMetadata],
            'links': List[OneOfGetZonesResponseLinksItems]
        }

        self.attribute_map = {
            'zones': 'zones',
            'links': 'links'
        }
        self._zones = zones
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'GetZonesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetZonesResponse of this GetZonesResponse.  # noqa: E501
        :rtype: GetZonesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zones(self) -> List[ResourcesZoneMetadata]:
        """Gets the zones of this GetZonesResponse.


        :return: The zones of this GetZonesResponse.
        :rtype: List[ResourcesZoneMetadata]
        """
        return self._zones

    @zones.setter
    def zones(self, zones: List[ResourcesZoneMetadata]):
        """Sets the zones of this GetZonesResponse.


        :param zones: The zones of this GetZonesResponse.
        :type zones: List[ResourcesZoneMetadata]
        """

        self._zones = zones

    @property
    def links(self) -> List[OneOfGetZonesResponseLinksItems]:
        """Gets the links of this GetZonesResponse.


        :return: The links of this GetZonesResponse.
        :rtype: List[OneOfGetZonesResponseLinksItems]
        """
        return self._links

    @links.setter
    def links(self, links: List[OneOfGetZonesResponseLinksItems]):
        """Sets the links of this GetZonesResponse.


        :param links: The links of this GetZonesResponse.
        :type links: List[OneOfGetZonesResponseLinksItems]
        """

        self._links = links
