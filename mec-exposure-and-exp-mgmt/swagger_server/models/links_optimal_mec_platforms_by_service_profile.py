# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_optimal_mec_platforms_by_service_profile_link import LinksOptimalMECPlatformsByServiceProfileLink  # noqa: F401,E501
from swagger_server import util


class LinksOptimalMECPlatformsByServiceProfile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksOptimalMECPlatformsByServiceProfileLink=None):  # noqa: E501
        """LinksOptimalMECPlatformsByServiceProfile - a model defined in Swagger

        :param link: The link of this LinksOptimalMECPlatformsByServiceProfile.  # noqa: E501
        :type link: LinksOptimalMECPlatformsByServiceProfileLink
        """
        self.swagger_types = {
            'link': LinksOptimalMECPlatformsByServiceProfileLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksOptimalMECPlatformsByServiceProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksOptimalMECPlatformsByServiceProfile of this LinksOptimalMECPlatformsByServiceProfile.  # noqa: E501
        :rtype: LinksOptimalMECPlatformsByServiceProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksOptimalMECPlatformsByServiceProfileLink:
        """Gets the link of this LinksOptimalMECPlatformsByServiceProfile.


        :return: The link of this LinksOptimalMECPlatformsByServiceProfile.
        :rtype: LinksOptimalMECPlatformsByServiceProfileLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksOptimalMECPlatformsByServiceProfileLink):
        """Sets the link of this LinksOptimalMECPlatformsByServiceProfile.


        :param link: The link of this LinksOptimalMECPlatformsByServiceProfile.
        :type link: LinksOptimalMECPlatformsByServiceProfileLink
        """

        self._link = link
