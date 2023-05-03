# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_update_service_endpoint_link import LinksUpdateServiceEndpointLink  # noqa: F401,E501
from swagger_server import util


class LinksUpdateServiceEndpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksUpdateServiceEndpointLink=None):  # noqa: E501
        """LinksUpdateServiceEndpoint - a model defined in Swagger

        :param link: The link of this LinksUpdateServiceEndpoint.  # noqa: E501
        :type link: LinksUpdateServiceEndpointLink
        """
        self.swagger_types = {
            'link': LinksUpdateServiceEndpointLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksUpdateServiceEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksUpdateServiceEndpoint of this LinksUpdateServiceEndpoint.  # noqa: E501
        :rtype: LinksUpdateServiceEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksUpdateServiceEndpointLink:
        """Gets the link of this LinksUpdateServiceEndpoint.


        :return: The link of this LinksUpdateServiceEndpoint.
        :rtype: LinksUpdateServiceEndpointLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksUpdateServiceEndpointLink):
        """Sets the link of this LinksUpdateServiceEndpoint.


        :param link: The link of this LinksUpdateServiceEndpoint.
        :type link: LinksUpdateServiceEndpointLink
        """

        self._link = link
