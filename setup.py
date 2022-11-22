from setuptools import find_namespace_packages, setup

setup(
    name="spiir-data",
    version="0.0.2",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", include=["spiir*"]),
    namespace_packages=["spiir"],
    python_requires=">=3.8",
    install_requires=[
        "astropy",
        "lalsuite",
        "pandas",
        "python-ligo-lw>=1.8.1",
        "matplotlib",
        "numpy>=1.23",
        "scipy",
        "tqdm",
    ],
    extras_reqire={"pycbc": "pycbc"},
    description="A data processing library for the SPIIR gravitational wave pipeline.",
    author="Daniel Tang",
    author_email="daniel.tang@uwa.edu.au",
)
