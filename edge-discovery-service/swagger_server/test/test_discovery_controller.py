# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_mec_platforms_response import GetMECPlatformsResponse  # noqa: E501
from swagger_server.models.get_regions_response import GetRegionsResponse  # noqa: E501
from swagger_server.models.get_resources_response import GetResourcesResponse  # noqa: E501
from swagger_server.models.get_service_endpoints_response import GetServiceEndpointsResponse  # noqa: E501
from swagger_server.models.get_zones_response import GetZonesResponse  # noqa: E501
from swagger_server.models.resources_region import ResourcesRegion  # noqa: E501
from swagger_server.models.resources_zone import ResourcesZone  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_region_id import TypesRegionId  # noqa: E501
from swagger_server.models.types_service_endpoints_id import TypesServiceEndpointsId  # noqa: E501
from swagger_server.models.types_ue_identity import TypesUEIdentity  # noqa: E501
from swagger_server.models.types_ue_identity_type import TypesUEIdentityType  # noqa: E501
from swagger_server.models.types_zone_id import TypesZoneId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDiscoveryController(BaseTestCase):
    """DiscoveryController integration test stubs"""

    def test_bookmark(self):
        """Test case for bookmark

        List the links to the top-level resources of this API
        """
        response = self.client.open(
            '/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mecplatforms(self):
        """Test case for get_mecplatforms

        Discover optimal MEC Platforms for deployed applications
        """
        query_string = [('region', 'region_example'),
                        ('zone', 'zone_example'),
                        ('service_profile_id', 'service_profile_id_example'),
                        ('subscriber_density', 56),
                        ('ue_identity_type', TypesUEIdentityType()),
                        ('ue_identity', TypesUEIdentity())]
        response = self.client.open(
            '/mecplatforms',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_region(self):
        """Test case for get_region

        Fetch details for a region
        """
        response = self.client.open(
            '/regions/{regionId}'.format(region_id=TypesRegionId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_regions(self):
        """Test case for get_regions

        List the geographical regions supported, and the associated zones
        """
        response = self.client.open(
            '/regions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_endpoints(self):
        """Test case for get_service_endpoints

        Find optimal Service Endpoints for clients to connect to
        """
        query_string = [('region', 'region_example'),
                        ('zone', 'zone_example'),
                        ('service_endpoints_ids', TypesServiceEndpointsId()),
                        ('subscriber_density', 56),
                        ('ue_identity_type', TypesUEIdentityType()),
                        ('ue_identity', TypesUEIdentity())]
        response = self.client.open(
            '/serviceendpoints',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone_by_id(self):
        """Test case for get_zone_by_id

        Read the properties of a zone
        """
        response = self.client.open(
            '/zones/{zoneId}'.format(zone_id=TypesZoneId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zones(self):
        """Test case for get_zones

        List all zones, or zones within a region
        """
        query_string = [('region', 'region_example')]
        response = self.client.open(
            '/zones',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
