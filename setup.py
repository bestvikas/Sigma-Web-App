from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sigmaarocos/__init__.py
from sigmaarocos import __version__ as version

setup(
	name="sigmaarocos",
	version=version,
	description="Sigma Arocos",
	author="Vikas Deshmukh",
	author_email="vikas.deshmukh@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
