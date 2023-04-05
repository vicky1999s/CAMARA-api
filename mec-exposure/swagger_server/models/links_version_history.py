# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links_version_history_link import LinksVersionHistoryLink  # noqa: F401,E501
from swagger_server import util


class LinksVersionHistory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, link: LinksVersionHistoryLink=None):  # noqa: E501
        """LinksVersionHistory - a model defined in Swagger

        :param link: The link of this LinksVersionHistory.  # noqa: E501
        :type link: LinksVersionHistoryLink
        """
        self.swagger_types = {
            'link': LinksVersionHistoryLink
        }

        self.attribute_map = {
            'link': 'link'
        }
        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'LinksVersionHistory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The links_Version-History of this LinksVersionHistory.  # noqa: E501
        :rtype: LinksVersionHistory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> LinksVersionHistoryLink:
        """Gets the link of this LinksVersionHistory.


        :return: The link of this LinksVersionHistory.
        :rtype: LinksVersionHistoryLink
        """
        return self._link

    @link.setter
    def link(self, link: LinksVersionHistoryLink):
        """Sets the link of this LinksVersionHistory.


        :param link: The link of this LinksVersionHistory.
        :type link: LinksVersionHistoryLink
        """

        self._link = link
