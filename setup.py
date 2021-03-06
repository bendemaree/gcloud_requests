from setuptools import setup

from gcloud_requests import __version__

setup(
    name="gcloud_requests",
    description="Thread-safe client functionality for gcloud-python via requests.",
    version=__version__,
    url="https://github.com/LeadPages/gcloud_requests",
    author="LeadPages",
    author_email="opensource@leadpages.net",
    license="MIT",
    packages=["gcloud_requests"],
    install_requires=[
        "gcloud==0.7.0",
        "requests==2.7.0",
        "certifi==2015.09.06.2"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7"
    ]
)
