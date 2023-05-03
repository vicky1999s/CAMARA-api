import connexion
import six

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
from swagger_server import util


def bookmark():  # noqa: E501
    """List the links to the top-level resources of this API

    List the top level resources available from the API bookmark and the links to reach them # noqa: E501


    :rtype: GetResourcesResponse
    """
    return 'do some magic!'


def get_mecplatforms(region=None, zone=None, service_profile_id=None, subscriber_density=None, ue_identity_type=None, ue_identity=None):  # noqa: E501
    """Discover optimal MEC Platforms for deployed applications

    Returns a list of optimal MEC Platforms where you can register your deployed application. You can choose to search without passing any of the inputs paramaters or a combination of Service Profile, Region, subscriber density or UEIdentity. # noqa: E501

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


def get_region(region_id):  # noqa: E501
    """Fetch details for a region

    Fetch details for a region # noqa: E501

    :param region_id: 
    :type region_id: dict | bytes

    :rtype: ResourcesRegion
    """
    if connexion.request.is_json:
        region_id = TypesRegionId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_regions():  # noqa: E501
    """List the geographical regions supported, and the associated zones

    List the geographical regions supported and the zones within each # noqa: E501


    :rtype: GetRegionsResponse
    """
    return 'do some magic!'


def get_service_endpoints(service_endpoints_ids, region=None, zone=None, subscriber_density=None, ue_identity_type=None, ue_identity=None):  # noqa: E501
    """Find optimal Service Endpoints for clients to connect to

    Returns a list of optimal Service Endpoints that client devices can connect to. You can search based on Service Profile, Region, subscriber density or UEIdentity. # noqa: E501

    :param service_endpoints_ids: serviceEndpointsIds, delimited by pipe. Each serviceEndpointsId is a pointer to the service endpoints (IP address, FQDN etc.) previously registered for a given service.
    :type service_endpoints_ids: list | bytes
    :param region: MEC region ID
    :type region: str
    :param zone: MEC zone ID
    :type zone: str
    :param subscriber_density: Minimum number of 4G/5G subscribers per square kilometer.
    :type subscriber_density: int
    :param ue_identity_type: Type of User Equipment identifier used in &#x60;UEIdentity&#x60;.
    :type ue_identity_type: dict | bytes
    :param ue_identity: Identifier value for User Equipment. The type of identifier is defined by the UEIdentityType parameter.
    :type ue_identity: dict | bytes

    :rtype: GetServiceEndpointsResponse
    """
    if connexion.request.is_json:
        service_endpoints_ids = [TypesServiceEndpointsId.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if connexion.request.is_json:
        ue_identity_type = TypesUEIdentityType.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        ue_identity = TypesUEIdentity.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_zone_by_id(zone_id):  # noqa: E501
    """Read the properties of a zone

    Read the properties of a zone # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: ResourcesZone
    """
    if connexion.request.is_json:
        zone_id = TypesZoneId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_zones(region=None):  # noqa: E501
    """List all zones, or zones within a region

    Returns a list of all zones or zones within a specified region. # noqa: E501

    :param region: MEC region ID
    :type region: str

    :rtype: GetZonesResponse
    """
    return 'do some magic!'
