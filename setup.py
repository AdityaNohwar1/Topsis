import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="TOPSIS-Aditya-102103738",
    version="1.0.0",
    description="Apply topsis to a dataset in a csv file",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AdityaNohwar1/topsis",
    author="Aditya Nohwar",
    author_email="adityanohwar100@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "Topsis_func=topsis.__main__:main",
        ]
    },
)