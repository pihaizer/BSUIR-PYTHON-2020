from setuptools import setup, find_packages


setup(
    name="Lab_2",
    version="1.0",
    packages=find_packages(),
    package_data={
        "MergeSort": ["*.txt"]
    },
    author="Nikita Andrasovich",
    description="Lab 2 Package",
)