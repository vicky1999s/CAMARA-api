# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_register_service_endpoint_link import LinksRegisterServiceEndpointLink  # noqa: F401,E501
from swagger_server import util


class LinksRegisterServiceEndpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksRegisterServiceEndpointLink=None):  # noqa: E501
        """LinksRegisterServiceEndpoint - a model defined in Swagger

        :param link: The link of this LinksRegisterServiceEndpoint.  # noqa: E501
        :type link: LinksRegisterServiceEndpointLink
        """
        self.swagger_types = {
            'link': LinksRegisterServiceEndpointLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksRegisterServiceEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksRegisterServiceEndpoint of this LinksRegisterServiceEndpoint.  # noqa: E501
        :rtype: LinksRegisterServiceEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksRegisterServiceEndpointLink:
        """Gets the link of this LinksRegisterServiceEndpoint.


        :return: The link of this LinksRegisterServiceEndpoint.
        :rtype: LinksRegisterServiceEndpointLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksRegisterServiceEndpointLink):
        """Sets the link of this LinksRegisterServiceEndpoint.


        :param link: The link of this LinksRegisterServiceEndpoint.
        :type link: LinksRegisterServiceEndpointLink
        """

        self._link = link
