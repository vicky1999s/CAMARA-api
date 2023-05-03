# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_terms_of_service_link import LinksTermsOfServiceLink  # noqa: F401,E501
from swagger_server import util


class LinksTermsOfService(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksTermsOfServiceLink=None):  # noqa: E501
        """LinksTermsOfService - a model defined in Swagger

        :param link: The link of this LinksTermsOfService.  # noqa: E501
        :type link: LinksTermsOfServiceLink
        """
        self.swagger_types = {
            'link': LinksTermsOfServiceLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksTermsOfService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinksTermsOfService of this LinksTermsOfService.  # noqa: E501
        :rtype: LinksTermsOfService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksTermsOfServiceLink:
        """Gets the link of this LinksTermsOfService.


        :return: The link of this LinksTermsOfService.
        :rtype: LinksTermsOfServiceLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksTermsOfServiceLink):
        """Sets the link of this LinksTermsOfService.


        :param link: The link of this LinksTermsOfService.
        :type link: LinksTermsOfServiceLink
        """

        self._link = link