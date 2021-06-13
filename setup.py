from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    "georss_client>=0.14",
    "dateparser>=0.7.0",
]

setup(
    name="georss_ign_sismologia_client",
    version="0.3",
    author="Malte Franken",
    author_email="coding@subspace.de",
    description="A GeoRSS client library for the IGN Sismologia feed.",
    license="Apache-2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exxamalte/python-georss-ign-sismologia-client",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES,
)
