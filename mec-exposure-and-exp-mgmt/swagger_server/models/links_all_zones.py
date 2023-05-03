# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_all_zones_link import LinksAllZonesLink  # noqa: F401,E501
from swagger_server import util


class LinksAllZones(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksAllZonesLink=None):  # noqa: E501
        """LinksAllZones - a model defined in Swagger

        :param link: The link of this LinksAllZones.  # noqa: E501
        :type link: LinksAllZonesLink
        """
        self.swagger_types = {
            'link': LinksAllZonesLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksAllZones':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksAllZones of this LinksAllZones.  # noqa: E501
        :rtype: LinksAllZones
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksAllZonesLink:
        """Gets the link of this LinksAllZones.


        :return: The link of this LinksAllZones.
        :rtype: LinksAllZonesLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksAllZonesLink):
        """Sets the link of this LinksAllZones.


        :param link: The link of this LinksAllZones.
        :type link: LinksAllZonesLink
        """

        self._link = link