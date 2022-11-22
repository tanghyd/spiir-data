from setuptools import find_namespace_packages, setup

setup(
    name="spiir-data",
    version="0.0.2",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", include=["spiir*"]),
    namespace_packages=["spiir"],
    python_requires=">=3.8",
    install_requires=[
        "lalsuite",
        "astropy",
        "python-ligo-lw>=1.8.1",
        "numpy>=1.23",
        "scipy",
        "pandas",
        "matplotlib",
    ],
    description="A Python data library for gravitational wave science by SPIIR.",
    author="Daniel Tang",
    author_email="daniel.tang@uwa.edu.au",
)
