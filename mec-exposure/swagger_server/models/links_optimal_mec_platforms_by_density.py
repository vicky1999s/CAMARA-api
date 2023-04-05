# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_optimal_me_cplatformsbydensity_link import LinksOptimalMECplatformsbydensityLink  # noqa: F401,E501
from swagger_server import util


class LinksOptimalMECPlatformsByDensity(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksOptimalMECplatformsbydensityLink=None):  # noqa: E501
        """LinksOptimalMECPlatformsByDensity - a model defined in Swagger

        :param link: The link of this LinksOptimalMECPlatformsByDensity.  # noqa: E501
        :type link: LinksOptimalMECplatformsbydensityLink
        """
        self.swagger_types = {
            'link': LinksOptimalMECplatformsbydensityLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksOptimalMECPlatformsByDensity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Optimal-MEC-platforms-by-density of this LinksOptimalMECPlatformsByDensity.  # noqa: E501
        :rtype: LinksOptimalMECPlatformsByDensity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksOptimalMECplatformsbydensityLink:
        """Gets the link of this LinksOptimalMECPlatformsByDensity.


        :return: The link of this LinksOptimalMECPlatformsByDensity.
        :rtype: LinksOptimalMECplatformsbydensityLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksOptimalMECplatformsbydensityLink):
        """Sets the link of this LinksOptimalMECPlatformsByDensity.


        :param link: The link of this LinksOptimalMECPlatformsByDensity.
        :type link: LinksOptimalMECplatformsbydensityLink
        """

        self._link = link
