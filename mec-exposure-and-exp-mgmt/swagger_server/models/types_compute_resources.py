# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.types_compute_resources_gpu import TypesComputeResourcesGPU  # noqa: F401,E501
from swagger_server import util


class TypesComputeResources(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, gpu: TypesComputeResourcesGPU=None, min_ramgb: int=None, min_storage_gb: int=None):  # noqa: E501
        """TypesComputeResources - a model defined in Swagger

        :param gpu: The gpu of this TypesComputeResources.  # noqa: E501
        :type gpu: TypesComputeResourcesGPU
        :param min_ramgb: The min_ramgb of this TypesComputeResources.  # noqa: E501
        :type min_ramgb: int
        :param min_storage_gb: The min_storage_gb of this TypesComputeResources.  # noqa: E501
        :type min_storage_gb: int
        """
        self.swagger_types = {
            'gpu': TypesComputeResourcesGPU,
            'min_ramgb': int,
            'min_storage_gb': int
        }

        self.attribute_map = {
            'gpu': 'GPU',
            'min_ramgb': 'minRAMGB',
            'min_storage_gb': 'minStorageGB'
        }
        self._gpu = gpu
        self._min_ramgb = min_ramgb
        self._min_storage_gb = min_storage_gb

    @classmethod
    def from_dict(cls, dikt) -> 'TypesComputeResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TypesComputeResources of this TypesComputeResources.  # noqa: E501
        :rtype: TypesComputeResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gpu(self) -> TypesComputeResourcesGPU:
        """Gets the gpu of this TypesComputeResources.


        :return: The gpu of this TypesComputeResources.
        :rtype: TypesComputeResourcesGPU
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu: TypesComputeResourcesGPU):
        """Sets the gpu of this TypesComputeResources.


        :param gpu: The gpu of this TypesComputeResources.
        :type gpu: TypesComputeResourcesGPU
        """

        self._gpu = gpu

    @property
    def min_ramgb(self) -> int:
        """Gets the min_ramgb of this TypesComputeResources.

        minimum RAM required in Gigabytes.  # noqa: E501

        :return: The min_ramgb of this TypesComputeResources.
        :rtype: int
        """
        return self._min_ramgb

    @min_ramgb.setter
    def min_ramgb(self, min_ramgb: int):
        """Sets the min_ramgb of this TypesComputeResources.

        minimum RAM required in Gigabytes.  # noqa: E501

        :param min_ramgb: The min_ramgb of this TypesComputeResources.
        :type min_ramgb: int
        """

        self._min_ramgb = min_ramgb

    @property
    def min_storage_gb(self) -> int:
        """Gets the min_storage_gb of this TypesComputeResources.

        Minimum storgae requirement in Gigabytes  # noqa: E501

        :return: The min_storage_gb of this TypesComputeResources.
        :rtype: int
        """
        return self._min_storage_gb

    @min_storage_gb.setter
    def min_storage_gb(self, min_storage_gb: int):
        """Sets the min_storage_gb of this TypesComputeResources.

        Minimum storgae requirement in Gigabytes  # noqa: E501

        :param min_storage_gb: The min_storage_gb of this TypesComputeResources.
        :type min_storage_gb: int
        """

        self._min_storage_gb = min_storage_gb
