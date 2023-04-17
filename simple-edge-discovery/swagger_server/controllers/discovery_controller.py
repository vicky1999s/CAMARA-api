import connexion
import six
import json
import boto3

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from scipy.spatial import KDTree

from swagger_server.models.get_mec_platforms_response import GetMECPlatformsResponse  # noqa: E501
from swagger_server.models.get_resources_response import GetResourcesResponse  # noqa: E501
from swagger_server.models.types_error import TypesError  # noqa: E501
from swagger_server.models.types_ue_identity import TypesUEIdentity  # noqa: E501
from swagger_server.models.types_ue_identity_type import TypesUEIdentityType  # noqa: E501
from swagger_server import util


dynamodb = boto3.resource('dynamodb',region_name = 'ap-southeast-1')
TABLE = dynamodb.Table('dsm-osm-camara')
#regions_list = ["chennai" ,"singapore","mumbai","london","netherlands","New york","bangalore"]
aws_region_map = {"ap-southeast-1":"singapore","us-west-1":"North California","ap-south-1":"mumbai"}
regions_list = []
coordinates = []
coordinates_key_map = {}

def bookmark():  # noqa: E501
    dynamodb = boto3.resource('dynamodb',region_name = 'ap-southeast-1')
    table = dynamodb.Table(tableName)
    return table

#get all items from DB
def getAvailbleMecs():
    response = TABLE.scan()
    items = response['Items']
    for i in range(len(items)):
        regions_list.append(items[i]["location"])

#get a itemm from db
def get_mec_by_id(columnName , value):
    response = TABLE.get_item(Key={columnName: edgeid})
    return item

#it will return the list of CO ordinates from a list of regions
def CoordinatesOfRegions():
    coordinates_list = []
    for region in regions_list:
      region_co = getRegionCoordinates(aws_region_map[region])
      coordinates_list.append(region_co)
      coordinates_key_map[tuple(region_co)] = aws_region_map[region]
    return coordinates_list

#it will compare two co ordinates points and return nearest one
def getNearestCoordinate(region):
    #coordinates = CoordinatesOfRegions()
    tree = KDTree(coordinates)
    ue_co = getRegionCoordinates(region)
    if not ue_co:
        return None

    nearest_idx = tree.query([ue_co])[1][0]
    nearest_coord = coordinates[nearest_idx]

    return nearest_coord

#gives coordinates of a region
def getRegionCoordinates(region):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(region)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        "print(latitude,longitude)"
        return [latitude,longitude]
    return None

#return region of a coordinates
"""def getRegion(coordinates):
    geolocator = Nominatim(user_agent="my_app")
    latitude = coordinates[0]
    longitude = coordinates[1]
    print("##",latitude,longitude)
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address"""

#nearest mec for loop
"""def getNearestMec(ue_region):
    ue_coordinates = getRegionCoordinates(ue_region)
    min_distance = float('inf')
    nearest_mec = None
    for region in regions_list:
        region_co = getRegionCoordinates(region)
        distance = geodesic(ue_coordinates,region_co).km
        if distance < min_distance:
             min_distance = distance
             nearest_mec = region_co

    print("the nearest region is ",nearest_mec,"with the distance of km",min_distance)
    return nearest_mec"""

getAvailbleMecs()
coordinates = CoordinatesOfRegions()
def get_mecplatforms(region, zone=None, service_profile_id=None, subscriber_density=None, ue_identity_type=None, ue_identity=None):  # noqa: E501
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
    "coordinates =  getRegionCoordinates(region)"
    "nearest_mec = getNearestMec(region)"
    "print(coordinates)"
    print(getRegionCoordinates(region))

    nearest_mec = getNearestCoordinate(region)
    if not nearest_mec:
        return "invalid region"

    jsonResponse =  {
        "MECPlatforms": [
            {
            "ern": {},
            "properties": [
                {
                "data": {
                    "latitude": nearest_mec[0],
                    "longitude": nearest_mec[1] 
                },
                "type": "type"
                },
                {
                "data": {
                    "edge_name": "",
                    "region":   coordinates_key_map[tuple(nearest_mec)]
                },
                "type": "type"
                }
            ],
            "region": {},
            "status": "STATUS_ENABLED",
            "zone": {}
            }
        ],
        "links": [
            "",
            ""
        ]
        }

    #return json.dumps(nearest_mec)

    return jsonResponse 