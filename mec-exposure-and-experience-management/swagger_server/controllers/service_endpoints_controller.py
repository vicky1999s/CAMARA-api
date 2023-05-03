import connexion
import six

from swagger_server.models.post_service_endpoint_response import PostServiceEndpointResponse  # noqa: E501
from swagger_server.models.resources_edge_hosted_service import ResourcesEdgeHostedService  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_service_endpoints_id import TypesServiceEndpointsId  # noqa: E501
from swagger_server import util


def deregister_service_endpoint(service_endpoints_id):  # noqa: E501
    """Deregister an application&#x27;s Service Endpoint

    Deregister an application&#x27;s Service Endpoint from the MEC Platform(s). # noqa: E501

    :param service_endpoints_id: 
    :type service_endpoints_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service_endpoints_id = TypesServiceEndpointsId.from_dict(connexion.request.get_json())  # noqa: E501\
    return 'do some magic!'


def get_service_endpoints_by_service_endpoints_id(service_endpoints_id):  # noqa: E501
    """Get registered edge service endpoint information

    Returns endpoint information for all Service Endpoints registered to a specified serviceEndpointId. # noqa: E501

    :param service_endpoints_id: 
    :type service_endpoints_id: dict | bytes

    :rtype: List[ResourcesEdgeHostedService]
    """
    if connexion.request.is_json:
        service_endpoints_id = TypesServiceEndpointsId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_service_endpoints(body=None):  # noqa: E501
    """Register Service Endpoints

    Register Service Endpoints of a deployed application to specified MEC Platforms. # noqa: E501

    :param body: Array of Service Endpoints for a deployed application
    :type body: list | bytes

    :rtype: PostServiceEndpointResponse
    """
    if connexion.request.is_json:
        body = [ResourcesEdgeHostedService.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    body = connexion.request.get_json()
    print(body)
    return 'do some magic!'


def update_service_endpoint(service_endpoints_id, body=None):  # noqa: E501
    """Update a Service Endpoint

    Update registered Service Endpoint information. # noqa: E501

    :param service_endpoints_id: 
    :type service_endpoints_id: dict | bytes
    :param body: Service Endpoint information
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service_endpoints_id = TypesServiceEndpointsId.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = [ResourcesEdgeHostedService.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
