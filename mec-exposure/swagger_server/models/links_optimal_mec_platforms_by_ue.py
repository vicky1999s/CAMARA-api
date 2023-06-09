# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_optimal_me_cplatformsby_ue_link import LinksOptimalMECplatformsbyUELink  # noqa: F401,E501
from swagger_server import util


class LinksOptimalMECPlatformsByUE(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksOptimalMECplatformsbyUELink=None):  # noqa: E501
        """LinksOptimalMECPlatformsByUE - a model defined in Swagger

        :param link: The link of this LinksOptimalMECPlatformsByUE.  # noqa: E501
        :type link: LinksOptimalMECplatformsbyUELink
        """
        self.swagger_types = {
            'link': LinksOptimalMECplatformsbyUELink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksOptimalMECPlatformsByUE':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Optimal-MEC-platforms-by-UE of this LinksOptimalMECPlatformsByUE.  # noqa: E501
        :rtype: LinksOptimalMECPlatformsByUE
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksOptimalMECplatformsbyUELink:
        """Gets the link of this LinksOptimalMECPlatformsByUE.


        :return: The link of this LinksOptimalMECPlatformsByUE.
        :rtype: LinksOptimalMECplatformsbyUELink
        """
        return self._link

    @link.setter
    def link(self, link: LinksOptimalMECplatformsbyUELink):
        """Sets the link of this LinksOptimalMECPlatformsByUE.


        :param link: The link of this LinksOptimalMECPlatformsByUE.
        :type link: LinksOptimalMECplatformsbyUELink
        """

        self._link = link
