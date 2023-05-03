import connexion
import six
import boto3
import json
import uuid

from swagger_server.models.get_service_profiles_response import GetServiceProfilesResponse  # noqa: E501
from swagger_server.models.post_service_profile_response import PostServiceProfileResponse  # noqa: E501
from swagger_server.models.resources_service_profile import ResourcesServiceProfile  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server import util

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('camara_serviceprofiles')

def create_service_profile(body=None):  # noqa: E501
    """Create a service profile

    Creates a service profile that describes the resource requirements of a service. # noqa: E501

    :param body: service profile
    :type body: dict | bytes

    :rtype: PostServiceProfileResponse
    """
    if connexion.request.is_json:
        #body = ResourcesServiceProfile.from_dict(connexion.request.get_json())  # noqa: E501
        item = connexion.request.get_json()
        # item = {
        #     "service_profile_id": "abcd-efgh",
        #     "body": value
        # }
        item["service_profile_id"] = str(uuid.uuid4())
        response = table.put_item(Item=item)
        print(item)
        print(response)

        res_json = {
            'service_profile_id': item["service_profile_id"]
            }
    return res_json


def delete_service_profile(service_profile_id):  # noqa: E501
    """Delete a Service Profile
    Delete Service Profile based on unique service profile ID # noqa: E501
    :param service_profile_id: 
    :type service_profile_id: str
    :rtype: None
    """
    response = table.delete_item(Key = {"service_profile_id": service_profile_id})
    print(response)
    
    return 'deleted'


def get_service_profile_by_profile_id(service_profile_id):  # noqa: E501
    """Fetch a service profile
    Returns a specified service profile. # noqa: E501
    :param service_profile_id: 
    :type service_profile_id: str
    :rtype: ResourcesServiceProfile
    """
    response = table.get_item(Key = {"service_profile_id": service_profile_id})
    print(response)
    return response["Item"]


def get_service_profiles():  # noqa: E501
    """List all service profiles registered under your API key
    List all service profiles registered under your API key # noqa: E501
    :rtype: GetServiceProfilesResponse
    """
    response = table.scan()
    for item in response["Items"]:
        print(item)
    return response["Items"]


def update_service_profile(service_profile_id, body=None):  # noqa: E501
    """Update Service Profile
    Update the definition of a Service Profile. # noqa: E501
    :param service_profile_id: 
    :type service_profile_id: str
    :param body: Service Profile definition
    :type body: dict | bytes
    :rtype: None
    """
    # if connexion.request.is_json:
    #     body = ResourcesServiceProfile.from_dict(connexion.request.get_json())  
    item = connexion.request.get_json()
    item["service_profile_id"] = service_profile_id
    response = table.put_item(Item=item)
    print(response)
    return item
