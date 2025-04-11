from setuptools import find_packages, setup

setup(
    name="insuraflow_dag",
    packages=find_packages(exclude=["insuraflow_dag_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
