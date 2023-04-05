# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_service_profiles_response import GetServiceProfilesResponse  # noqa: E501
from swagger_server.models.post_service_profile_response import PostServiceProfileResponse  # noqa: E501
from swagger_server.models.resources_service_profile import ResourcesServiceProfile  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServiceProfilesController(BaseTestCase):
    """ServiceProfilesController integration test stubs"""

    def test_create_service_profile(self):
        """Test case for create_service_profile

        Create a service profile
        """
        body = ResourcesServiceProfile()
        response = self.client.open(
            '/serviceprofiles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_service_profile(self):
        """Test case for delete_service_profile

        Delete a Service Profile
        """
        response = self.client.open(
            '/serviceprofiles/{serviceProfileId}'.format(service_profile_id='service_profile_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_profile_by_profile_id(self):
        """Test case for get_service_profile_by_profile_id

        Fetch a service profile
        """
        response = self.client.open(
            '/serviceprofiles/{serviceProfileId}'.format(service_profile_id='service_profile_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_profiles(self):
        """Test case for get_service_profiles

        List all service profiles registered under your API key
        """
        response = self.client.open(
            '/serviceprofiles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_service_profile(self):
        """Test case for update_service_profile

        Update Service Profile
        """
        body = ResourcesServiceProfile()
        response = self.client.open(
            '/serviceprofiles/{serviceProfileId}'.format(service_profile_id='service_profile_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
