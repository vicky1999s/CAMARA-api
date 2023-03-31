import connexion
import six

from swagger_server.models.get_mec_platforms_response import GetMECPlatformsResponse  # noqa: E501
from swagger_server.models.get_resources_response import GetResourcesResponse  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_ue_identity import TypesUEIdentity  # noqa: E501
from swagger_server.models.types_ue_identity_type import TypesUEIdentityType  # noqa: E501
from swagger_server import util


def bookmark():  # noqa: E501
    """API bookmark

    API bookmark # noqa: E501


    :rtype: GetResourcesResponse
    """
    return 'do some magic!'


def get_mecplatforms(region=None, zone=None, service_profile_id=None, subscriber_density=None, ue_identity_type=None, ue_identity=None):  # noqa: E501
    """Returns the name of the closest MEC platform(s) to the UE that sent the request.

    ON receiving this request, the network will calculate which of its MEC platforms have the shortest network path to the UE (terminal) from which the request was made. # noqa: E501

    :param region: MEC region ID
    :type region: str
    :param zone: MEC zone ID
    :type zone: str
    :param service_profile_id: service profile identifier
    :type service_profile_id: str
    :param subscriber_density: Minimum number of 4G/5G subscribers per square kilometer.
    :type subscriber_density: int
    :param ue_identity_type: Type of User Equipment identifier used in &#x60;UEIdentity&#x60;.
    :type ue_identity_type: dict | bytes
    :param ue_identity: Identifier value for User Equipment. The type of identifier is defined by the UEIdentityType parameter.
    :type ue_identity: dict | bytes

    :rtype: GetMECPlatformsResponse
    """
    if connexion.request.is_json:
        ue_identity_type = TypesUEIdentityType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        ue_identity = TypesUEIdentity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
