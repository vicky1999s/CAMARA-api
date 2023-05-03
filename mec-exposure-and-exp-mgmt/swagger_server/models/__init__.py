# coding: utf-8

# flake8: noqa
from __future__ import absolute_import
# import models into model package
from swagger_server.models.get_mec_platforms_response import GetMECPlatformsResponse
from swagger_server.models.get_regions_response import GetRegionsResponse
from swagger_server.models.get_resources_response import GetResourcesResponse
from swagger_server.models.get_service_endpoints_response import GetServiceEndpointsResponse
from swagger_server.models.get_service_profiles_response import GetServiceProfilesResponse
from swagger_server.models.get_zones_response import GetZonesResponse
from swagger_server.models.links_all_mec_platforms import LinksAllMecPlatforms
from swagger_server.models.links_all_mec_platforms_link import LinksAllMecPlatformsLink
from swagger_server.models.links_all_regions import LinksAllRegions
from swagger_server.models.links_all_regions_link import LinksAllRegionsLink
from swagger_server.models.links_all_service_endpoints import LinksAllServiceEndpoints
from swagger_server.models.links_all_service_endpoints_link import LinksAllServiceEndpointsLink
from swagger_server.models.links_all_service_profiles import LinksAllServiceProfiles
from swagger_server.models.links_all_service_profiles_link import LinksAllServiceProfilesLink
from swagger_server.models.links_all_zones import LinksAllZones
from swagger_server.models.links_all_zones_link import LinksAllZonesLink
from swagger_server.models.links_bookmark import LinksBookmark
from swagger_server.models.links_bookmark_link import LinksBookmarkLink
from swagger_server.models.links_common import LinksCommon
from swagger_server.models.links_create_service_profile import LinksCreateServiceProfile
from swagger_server.models.links_create_service_profile_link import LinksCreateServiceProfileLink
from swagger_server.models.links_delete_service_endpoint import LinksDeleteServiceEndpoint
from swagger_server.models.links_delete_service_endpoint_link import LinksDeleteServiceEndpointLink
from swagger_server.models.links_delete_service_profile import LinksDeleteServiceProfile
from swagger_server.models.links_delete_service_profile_link import LinksDeleteServiceProfileLink
from swagger_server.models.links_optimal_mec_platforms_by_density import LinksOptimalMECPlatformsByDensity
from swagger_server.models.links_optimal_mec_platforms_by_density_link import LinksOptimalMECPlatformsByDensityLink
from swagger_server.models.links_optimal_mec_platforms_by_region import LinksOptimalMECPlatformsByRegion
from swagger_server.models.links_optimal_mec_platforms_by_region_link import LinksOptimalMECPlatformsByRegionLink
from swagger_server.models.links_optimal_mec_platforms_by_service_profile import LinksOptimalMECPlatformsByServiceProfile
from swagger_server.models.links_optimal_mec_platforms_by_service_profile_link import LinksOptimalMECPlatformsByServiceProfileLink
from swagger_server.models.links_optimal_mec_platforms_by_ue import LinksOptimalMECPlatformsByUE
from swagger_server.models.links_optimal_mec_platforms_by_ue_link import LinksOptimalMECPlatformsByUELink
from swagger_server.models.links_optimal_mec_platforms_by_zone import LinksOptimalMECPlatformsByZone
from swagger_server.models.links_optimal_mec_platforms_by_zone_link import LinksOptimalMECPlatformsByZoneLink
from swagger_server.models.links_optimal_service_endpoints_by_region import LinksOptimalServiceEndpointsByRegion
from swagger_server.models.links_optimal_service_endpoints_by_region_link import LinksOptimalServiceEndpointsByRegionLink
from swagger_server.models.links_optimal_service_endpoints_by_service_profile import LinksOptimalServiceEndpointsByServiceProfile
from swagger_server.models.links_optimal_service_endpoints_by_service_profile_link import LinksOptimalServiceEndpointsByServiceProfileLink
from swagger_server.models.links_optimal_service_endpoints_by_zone import LinksOptimalServiceEndpointsByZone
from swagger_server.models.links_optimal_service_endpoints_by_zone_link import LinksOptimalServiceEndpointsByZoneLink
from swagger_server.models.links_register_service_endpoint import LinksRegisterServiceEndpoint
from swagger_server.models.links_register_service_endpoint_link import LinksRegisterServiceEndpointLink
from swagger_server.models.links_self import LinksSelf
from swagger_server.models.links_self_link import LinksSelfLink
from swagger_server.models.links_terms_of_service import LinksTermsOfService
from swagger_server.models.links_terms_of_service_link import LinksTermsOfServiceLink
from swagger_server.models.links_update_service_endpoint import LinksUpdateServiceEndpoint
from swagger_server.models.links_update_service_endpoint_link import LinksUpdateServiceEndpointLink
from swagger_server.models.links_update_service_profile import LinksUpdateServiceProfile
from swagger_server.models.links_update_service_profile_link import LinksUpdateServiceProfileLink
from swagger_server.models.links_version_history import LinksVersionHistory
from swagger_server.models.links_version_history_link import LinksVersionHistoryLink
from swagger_server.models.one_of_get_mec_platforms_response_links_items import OneOfGetMECPlatformsResponseLinksItems
from swagger_server.models.one_of_get_regions_response_links_items import OneOfGetRegionsResponseLinksItems
from swagger_server.models.one_of_get_service_endpoints_response_links_items import OneOfGetServiceEndpointsResponseLinksItems
from swagger_server.models.one_of_get_service_profiles_response_links_items import OneOfGetServiceProfilesResponseLinksItems
from swagger_server.models.one_of_get_zones_response_links_items import OneOfGetZonesResponseLinksItems
from swagger_server.models.one_of_links_common_items import OneOfLinksCommonItems
from swagger_server.models.one_of_post_service_endpoint_response_links_items import OneOfPostServiceEndpointResponseLinksItems
from swagger_server.models.one_of_post_service_profile_response_links_items import OneOfPostServiceProfileResponseLinksItems
from swagger_server.models.one_of_resources_items import OneOfResourcesItems
from swagger_server.models.post_service_endpoint_response import PostServiceEndpointResponse
from swagger_server.models.post_service_profile_response import PostServiceProfileResponse
from swagger_server.models.resources import Resources
from swagger_server.models.resources_edge_hosted_service import ResourcesEdgeHostedService
from swagger_server.models.resources_edge_service_description import ResourcesEdgeServiceDescription
from swagger_server.models.resources_mec_platform import ResourcesMecPlatform
from swagger_server.models.resources_region import ResourcesRegion
from swagger_server.models.resources_region_metadata import ResourcesRegionMetadata
from swagger_server.models.resources_service_endpoint import ResourcesServiceEndpoint
from swagger_server.models.resources_service_profile import ResourcesServiceProfile
from swagger_server.models.resources_service_profile_properties import ResourcesServiceProfileProperties
from swagger_server.models.resources_zone import ResourcesZone
from swagger_server.models.resources_zone_metadata import ResourcesZoneMetadata
from swagger_server.models.types_compute_resources import TypesComputeResources
from swagger_server.models.types_compute_resources_gpu import TypesComputeResourcesGPU
from swagger_server.models.types_edge_resource import TypesEdgeResource
from swagger_server.models.types_error import TypesError
from swagger_server.models.types_network_resources import TypesNetworkResources
from swagger_server.models.types_region_id import TypesRegionId
from swagger_server.models.types_service_endpoints_id import TypesServiceEndpointsId
from swagger_server.models.types_service_profile_id import TypesServiceProfileId
from swagger_server.models.types_success import TypesSuccess
from swagger_server.models.types_ue_identity import TypesUEIdentity
from swagger_server.models.types_ue_identity_type import TypesUEIdentityType
from swagger_server.models.types_zone_id import TypesZoneId