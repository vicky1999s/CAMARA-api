# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class LinksAllserviceprofilesLink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rel: str=None, method: str=None, href: str=None):  # noqa: E501
        """LinksAllserviceprofilesLink - a model defined in Swagger

        :param rel: The rel of this LinksAllserviceprofilesLink.  # noqa: E501
        :type rel: str
        :param method: The method of this LinksAllserviceprofilesLink.  # noqa: E501
        :type method: str
        :param href: The href of this LinksAllserviceprofilesLink.  # noqa: E501
        :type href: str
        """
        self.swagger_types = {
            'rel': str,
            'method': str,
            'href': str
        }

        self.attribute_map = {
            'rel': 'rel',
            'method': 'method',
            'href': 'href'
        }
        self._rel = rel
        self._method = method
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'LinksAllserviceprofilesLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Allserviceprofiles_link of this LinksAllserviceprofilesLink.  # noqa: E501
        :rtype: LinksAllserviceprofilesLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rel(self) -> str:
        """Gets the rel of this LinksAllserviceprofilesLink.


        :return: The rel of this LinksAllserviceprofilesLink.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this LinksAllserviceprofilesLink.


        :param rel: The rel of this LinksAllserviceprofilesLink.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def method(self) -> str:
        """Gets the method of this LinksAllserviceprofilesLink.


        :return: The method of this LinksAllserviceprofilesLink.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this LinksAllserviceprofilesLink.


        :param method: The method of this LinksAllserviceprofilesLink.
        :type method: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def href(self) -> str:
        """Gets the href of this LinksAllserviceprofilesLink.


        :return: The href of this LinksAllserviceprofilesLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this LinksAllserviceprofilesLink.


        :param href: The href of this LinksAllserviceprofilesLink.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
