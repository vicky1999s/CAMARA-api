# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.resources import Resources  # noqa: F401,E501
from swagger_server.models.one_ofget_resources_response_links_items import OneOfgetResourcesResponseLinksItems  # noqa: F401,E501
from swagger_server import util


class GetResourcesResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, resources: List[Resources]=None, links: List[OneOfgetResourcesResponseLinksItems]=None):  # noqa: E501
        """GetResourcesResponse - a model defined in Swagger

        :param resources: The resources of this GetResourcesResponse.  # noqa: E501
        :type resources: List[Resources]
        :param links: The links of this GetResourcesResponse.  # noqa: E501
        :type links: List[OneOfgetResourcesResponseLinksItems]
        """
        self.swagger_types = {
            'resources': List[Resources],
            'links': List[OneOfgetResourcesResponseLinksItems]
        }

        self.attribute_map = {
            'resources': 'resources',
            'links': 'links'
        }
        self._resources = resources
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'GetResourcesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The getResourcesResponse of this GetResourcesResponse.  # noqa: E501
        :rtype: GetResourcesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resources(self) -> List[Resources]:
        """Gets the resources of this GetResourcesResponse.


        :return: The resources of this GetResourcesResponse.
        :rtype: List[Resources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources: List[Resources]):
        """Sets the resources of this GetResourcesResponse.


        :param resources: The resources of this GetResourcesResponse.
        :type resources: List[Resources]
        """

        self._resources = resources

    @property
    def links(self) -> List[OneOfgetResourcesResponseLinksItems]:
        """Gets the links of this GetResourcesResponse.


        :return: The links of this GetResourcesResponse.
        :rtype: List[OneOfgetResourcesResponseLinksItems]
        """
        return self._links

    @links.setter
    def links(self, links: List[OneOfgetResourcesResponseLinksItems]):
        """Sets the links of this GetResourcesResponse.


        :param links: The links of this GetResourcesResponse.
        :type links: List[OneOfgetResourcesResponseLinksItems]
        """

        self._links = links
