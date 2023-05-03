# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.post_service_endpoint_response import PostServiceEndpointResponse  # noqa: E501
from swagger_server.models.resources_edge_hosted_service import ResourcesEdgeHostedService  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_service_endpoints_id import TypesServiceEndpointsId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServiceEndpointsController(BaseTestCase):
    """ServiceEndpointsController integration test stubs"""

    def test_deregister_service_endpoint(self):
        """Test case for deregister_service_endpoint

        Deregister an application's Service Endpoint
        """
        response = self.client.open(
            '/serviceendpoints/{serviceEndpointsId}'.format(service_endpoints_id=TypesServiceEndpointsId()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_endpoints_by_service_endpoints_id(self):
        """Test case for get_service_endpoints_by_service_endpoints_id

        Get registered edge service endpoint information
        """
        response = self.client.open(
            '/serviceendpoints/{serviceEndpointsId}'.format(service_endpoints_id=TypesServiceEndpointsId()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_service_endpoints(self):
        """Test case for register_service_endpoints

        Register Service Endpoints
        """
        body = [ResourcesEdgeHostedService()]
        response = self.client.open(
            '/serviceendpoints',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_service_endpoint(self):
        """Test case for update_service_endpoint

        Update a Service Endpoint
        """
        body = [ResourcesEdgeHostedService()]
        response = self.client.open(
            '/serviceendpoints/{serviceEndpointsId}'.format(service_endpoints_id=TypesServiceEndpointsId()),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
