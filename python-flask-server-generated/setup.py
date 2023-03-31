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
    description="Simple MEC Discovery API",
    author_email="",
    url="",
    keywords=["Swagger", "Simple MEC Discovery API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    # Find your nearest MEC platform --- Network operators will typically have multiple MEC sites in a given territory. Connecting your application to a server on the closest MEC platform means the lowest latency - however, the physical location of a user is not an accurate match to the closest MEC site, due to the way operator networks are configured. This API returns the MEC platforms with the _shortest network path_ to the client making the request, and hence the lowest propagation delay. * If you have a server instance deployed there, connect to it to gain the lowest latency * Or if not, you may wish to deploy an instance there using the APIs of the cloud provider supporting that zone.    This API is intended to be called by a client application hosted on a UE attached to the operator network. _Note that the API parameters have been listed in this &#x27;simple API&#x27; to align with the full API, but are optional and may not be supported by the API server_ --- 
    """
)
