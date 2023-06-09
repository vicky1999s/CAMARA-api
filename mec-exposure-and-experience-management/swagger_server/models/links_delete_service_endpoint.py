# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_deleteserviceendpoint_link import LinksDeleteserviceendpointLink  # noqa: F401,E501
from swagger_server import util


class LinksDeleteServiceEndpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksDeleteserviceendpointLink=None):  # noqa: E501
        """LinksDeleteServiceEndpoint - a model defined in Swagger

        :param link: The link of this LinksDeleteServiceEndpoint.  # noqa: E501
        :type link: LinksDeleteserviceendpointLink
        """
        self.swagger_types = {
            'link': LinksDeleteserviceendpointLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksDeleteServiceEndpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Delete-service-endpoint of this LinksDeleteServiceEndpoint.  # noqa: E501
        :rtype: LinksDeleteServiceEndpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksDeleteserviceendpointLink:
        """Gets the link of this LinksDeleteServiceEndpoint.


        :return: The link of this LinksDeleteServiceEndpoint.
        :rtype: LinksDeleteserviceendpointLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksDeleteserviceendpointLink):
        """Sets the link of this LinksDeleteServiceEndpoint.


        :param link: The link of this LinksDeleteServiceEndpoint.
        :type link: LinksDeleteserviceendpointLink
        """

        self._link = link
