# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_mec_platforms_response import GetMECPlatformsResponse  # noqa: E501
from swagger_server.models.get_resources_response import GetResourcesResponse  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_ue_identity import TypesUEIdentity  # noqa: E501
from swagger_server.models.types_ue_identity_type import TypesUEIdentityType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDiscoveryController(BaseTestCase):
    """DiscoveryController integration test stubs"""

    def test_bookmark(self):
        """Test case for bookmark

        API bookmark
        """
        response = self.client.open(
            '/alphatest/SimpleAPI/1.1.2/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mecplatforms(self):
        """Test case for get_mecplatforms

        Returns the name of the closest MEC platform(s) to the UE that sent the request.
        """
        query_string = [('region', 'region_example'),
                        ('zone', 'zone_example'),
                        ('service_profile_id', 'service_profile_id_example'),
                        ('subscriber_density', 56),
                        ('ue_identity_type', TypesUEIdentityType()),
                        ('ue_identity', TypesUEIdentity())]
        response = self.client.open(
            '/alphatest/SimpleAPI/1.1.2/mecplatforms',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
