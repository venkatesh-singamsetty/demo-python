"""Setup script for demo-python package."""
from setuptools import setup, find_packages

setup(
    name="demo-python",
    version="1.0.0",
    description="A demo Python project",
    author="Venkatesh Singamsetty",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.0",
    ],
    entry_points={
        "console_scripts": [
            "demo-python=myapp.main:main",
        ],
    },
)
