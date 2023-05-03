# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="MEC Exposure &amp; Experience Management API",
    author_email="",
    url="",
    keywords=["Swagger", "MEC Exposure &amp; Experience Management API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    # Introduction ---  Use the MEC Exposure &amp; Experience Management API for discovery and utilisation of Multi-Access Edge Compute (MEC)  resources and services.    --- # API Scope  ---  APIs defined in this version of the specification can be categorized into the following areas:  * __MEC Edge Discovery__ - discovery of optimal MEC platforms * __MEC Service Discovery__ - discovery of optimal Service Endpoints for client connections * __MEC Service Profile management__ - register, retrieve, update, and delete MEC Service Profiles * __MEC Service Endpoint management__ - register one or more Service Endpoints, and retrieve, update, and delete those registrations * __MEC Edge Event notification__ - subscription management for MEC and Service discovery Event notifications  --- # Definitions --- This section provides definitions of terminologies commonly referred to throughout the API descriptions.  * __API Consumer__ - A user or an application consuming the MEC Exposure and Experience Management APIs.  * __Application Service Provider__ - the developer/publisher who deploys applications on MEC platforms. * __Density__ - Minimum 4G/5G subscriber density in a geographical area, represented as the number of subscribers per square kilometer. * __Edge Application__ - A cloud application that has some services deployed to MEC Platforms to take advantage of low latency and high bandwidth when interacting with devices. * __Edge Discovery Service (EDS)__ - MEC Exposure and Experience Management APIs exposed as a service by a TSP. * __Edge Resource__ - An object defined by the sevice provider representing an edge resource within its network domain, such as a MEC Platform. * __Event__ - A MEC event is triggered if the previously-discovered MEC platform is no longer the optimal choice of all available MEC platforms, due to a change in the underlying network or MEC infrastructure. The TSP will send out change notifications to API Consumers who have active subscription to the event notification.  * __MEC  Platform__ - A collection of cloud computing resources housed in a TSP&#x27;s network facility that provide Multi-access Edge Computing (MEC) capabilities.     * __Optimal MEC  Platforms__ - A list of one or more optimal MEC Platforms to register a Service Endpoint, based on the latency and availability of each MEC platform, and optionally also based on various query criteria (Service Profile, Region, subscriber density or UE identity) defined by the API Consumer.       * __Optimal MEC Service Endpoints__ – A list of one or more MEC Service Endpoints that provide optimal user experience to the client device, based on internal network conditions known to the MEC Platform, and also optionally based on various query criteria (Service Profile, Region, subscriber density or UE identity) defined by the API Consumer.  * __Region__ - A TSP-defined string identifier representing a certain geographical or logical area where MEC resources and services are provided. * __Registered MEC Hosted Services__ - Applications running on MEC platforms which are registered with Edge Discovery Service using the service registry APIs. * __Service Endpoint__ - The routable endpoint of the service(s) within a deployed application that clients connect to, where a service is a subcomponent of application     * __Service Profile__ - Information about the MEC application and the associated service characteristics. * __TSP__ - Telecommunications Service Provider.       * __UEIdentity__ - User Equipment identity, which can be a device&#x27;s IP address, MSISDN, IMEI, MDN, or GPSI. * __Zone__ - A logical collection of MEC Platforms in a telecommunication provider&#x27;s network. A Zone is part of a Region.    --- # Link relationships ---  __REGIONS__ * __All-regions__  list all regions  __ZONES__ * __All-zones__  list all available zones  __MEC PLATFORMS__ * __All-mec-platforms__ list all MEC platforms * __Optimal-MECPlatforms-by-density__ return the optimal MEC platform for a given subscriber density * __Optimal-MECPlatforms-by-service-profile__ return the optimal MEC platform for a given service profile * __Optimal-MECPlatforms-by-UE__ return the optimal MEC platform for a given UE identifier * __Optimal-MECPlatforms-by-region__ return the optimal MEC platform for a given region * __Optimal-MECPlatforms-by-zone__ return the optimal MEC platform for a given zone  __Service Endpoints__ * __All-service-endpoints__ list all Service Endpoints * __Register-service-endpoint__ Register a Service Endpoint      * __Update-service-endpoint__ Update a Service Endpoint * __Delete-service-endpoint__ Delete a Service Endpoint * __Optimal-service-endpoints-by-zone__ return the optimal Service Endpoints associated with the specified Zone * __Optimal-service-endpoints-by-region__ return the optimal Service Endpoints associated with the specified Region * __Optimal-service-endpoints-by-service-profile__ return the optimal Service Endpoints associated with the specified Service Profile  __SERVICE PROFILES__ * __All-service-profiles__ list all Service Profiles * __Create-service-profile__ create a new Service Profile * __Update-service-profiles__ Update a Service Profiles * __Delete-service-profile__ Delete a Service Profile based on ID    __EVENTS AND SUBSCRIPTIONS__ * __All-events__ list all events * __All-subscriptions__ list all subscriptions * __Create-subscription__ create a subscription for Edge Discovery and workload discovery events * __Update-subscription__ Update a subscription for Edge Discovery and workload discovery events * __Delete-subscription__ Delete a subscription for Edge Discovery and workload discovery events  __COMMON__ * __Self__ the self-referring URI for the response * __Version-History__ link to version history for this API * __Terms-of-Service__ link The Terms of Service for this API * __Bookmark__ link to the API bookmark  --- # Security and resilience --- * __Authentication:__ API requests are made with the API Consumer&#x27;s unique key * __Integrity:__ APIs requests, responses and callbacks are made using HTTP over TLS 1.3 (HTTPS) * __Consent to access resources__ is brokered via OAuth2.0 with implicit, password and client credentials grant flows * __Replay errors__ are mitigated through use of request correlator IDs. 
    """
)
