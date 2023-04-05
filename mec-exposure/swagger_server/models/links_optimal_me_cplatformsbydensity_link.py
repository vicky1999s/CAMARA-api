# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class LinksOptimalMECplatformsbydensityLink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rel: str=None, method: str=None, href: str=None):  # noqa: E501
        """LinksOptimalMECplatformsbydensityLink - a model defined in Swagger

        :param rel: The rel of this LinksOptimalMECplatformsbydensityLink.  # noqa: E501
        :type rel: str
        :param method: The method of this LinksOptimalMECplatformsbydensityLink.  # noqa: E501
        :type method: str
        :param href: The href of this LinksOptimalMECplatformsbydensityLink.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'LinksOptimalMECplatformsbydensityLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_OptimalMECplatformsbydensity_link of this LinksOptimalMECplatformsbydensityLink.  # noqa: E501
        :rtype: LinksOptimalMECplatformsbydensityLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rel(self) -> str:
        """Gets the rel of this LinksOptimalMECplatformsbydensityLink.


        :return: The rel of this LinksOptimalMECplatformsbydensityLink.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this LinksOptimalMECplatformsbydensityLink.


        :param rel: The rel of this LinksOptimalMECplatformsbydensityLink.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def method(self) -> str:
        """Gets the method of this LinksOptimalMECplatformsbydensityLink.


        :return: The method of this LinksOptimalMECplatformsbydensityLink.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this LinksOptimalMECplatformsbydensityLink.


        :param method: The method of this LinksOptimalMECplatformsbydensityLink.
        :type method: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def href(self) -> str:
        """Gets the href of this LinksOptimalMECplatformsbydensityLink.


        :return: The href of this LinksOptimalMECplatformsbydensityLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this LinksOptimalMECplatformsbydensityLink.


        :param href: The href of this LinksOptimalMECplatformsbydensityLink.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
