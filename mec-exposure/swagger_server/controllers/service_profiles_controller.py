import connexion
import six

from swagger_server.models.get_service_profiles_response import GetServiceProfilesResponse  # noqa: E501
from swagger_server.models.post_service_profile_response import PostServiceProfileResponse  # noqa: E501
from swagger_server.models.resources_service_profile import ResourcesServiceProfile  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server import util


def create_service_profile(body=None):  # noqa: E501
    """Create a service profile

    Creates a service profile that describes the resource requirements of a service. # noqa: E501

    :param body: service profile
    :type body: dict | bytes

    :rtype: PostServiceProfileResponse
    """
    if connexion.request.is_json:
        body = ResourcesServiceProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_service_profile(service_profile_id):  # noqa: E501
    """Delete a Service Profile

    Delete Service Profile based on unique service profile ID # noqa: E501

    :param service_profile_id: 
    :type service_profile_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_service_profile_by_profile_id(service_profile_id):  # noqa: E501
    """Fetch a service profile

    Returns a specified service profile. # noqa: E501

    :param service_profile_id: 
    :type service_profile_id: str

    :rtype: ResourcesServiceProfile
    """
    return 'do some magic!'


def get_service_profiles():  # noqa: E501
    """List all service profiles registered under your API key

    List all service profiles registered under your API key # noqa: E501


    :rtype: GetServiceProfilesResponse
    """
    return 'do some magic!'


def update_service_profile(service_profile_id, body=None):  # noqa: E501
    """Update Service Profile

    Update the definition of a Service Profile. # noqa: E501

    :param service_profile_id: 
    :type service_profile_id: str
    :param body: Service Profile definition
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResourcesServiceProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
