# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_optimal_service_endpoints_by_region_link import LinksOptimalServiceEndpointsByRegionLink  # noqa: F401,E501
from swagger_server import util


class LinksOptimalServiceEndpointsByRegion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksOptimalServiceEndpointsByRegionLink=None):  # noqa: E501
        """LinksOptimalServiceEndpointsByRegion - a model defined in Swagger

        :param link: The link of this LinksOptimalServiceEndpointsByRegion.  # noqa: E501
        :type link: LinksOptimalServiceEndpointsByRegionLink
        """
        self.swagger_types = {
            'link': LinksOptimalServiceEndpointsByRegionLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksOptimalServiceEndpointsByRegion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksOptimalServiceEndpointsByRegion of this LinksOptimalServiceEndpointsByRegion.  # noqa: E501
        :rtype: LinksOptimalServiceEndpointsByRegion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksOptimalServiceEndpointsByRegionLink:
        """Gets the link of this LinksOptimalServiceEndpointsByRegion.


        :return: The link of this LinksOptimalServiceEndpointsByRegion.
        :rtype: LinksOptimalServiceEndpointsByRegionLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksOptimalServiceEndpointsByRegionLink):
        """Sets the link of this LinksOptimalServiceEndpointsByRegion.


        :param link: The link of this LinksOptimalServiceEndpointsByRegion.
        :type link: LinksOptimalServiceEndpointsByRegionLink
        """

        self._link = link
