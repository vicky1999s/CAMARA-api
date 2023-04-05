# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class LinksUpdateserviceprofileLink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rel: str=None, method: str=None, href: str=None):  # noqa: E501
        """LinksUpdateserviceprofileLink - a model defined in Swagger

        :param rel: The rel of this LinksUpdateserviceprofileLink.  # noqa: E501
        :type rel: str
        :param method: The method of this LinksUpdateserviceprofileLink.  # noqa: E501
        :type method: str
        :param href: The href of this LinksUpdateserviceprofileLink.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'LinksUpdateserviceprofileLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Updateserviceprofile_link of this LinksUpdateserviceprofileLink.  # noqa: E501
        :rtype: LinksUpdateserviceprofileLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rel(self) -> str:
        """Gets the rel of this LinksUpdateserviceprofileLink.


        :return: The rel of this LinksUpdateserviceprofileLink.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this LinksUpdateserviceprofileLink.


        :param rel: The rel of this LinksUpdateserviceprofileLink.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

    @property
    def method(self) -> str:
        """Gets the method of this LinksUpdateserviceprofileLink.


        :return: The method of this LinksUpdateserviceprofileLink.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this LinksUpdateserviceprofileLink.


        :param method: The method of this LinksUpdateserviceprofileLink.
        :type method: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def href(self) -> str:
        """Gets the href of this LinksUpdateserviceprofileLink.


        :return: The href of this LinksUpdateserviceprofileLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this LinksUpdateserviceprofileLink.


        :param href: The href of this LinksUpdateserviceprofileLink.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
