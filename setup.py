from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open("README.md") as readme:
    long_description = readme.read()

setup(
        name="rentropy",
        version="0.1.3",
        author="Timm Behner",
        author_email="timm.behner@fkie.fraunhofer.de",
        description="A small wrapper around a rust entropy crate",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/tbehner/rentropy",
        rust_extensions=[RustExtension("rentropy.rentropy", binding=Binding.PyO3)],
        packages=["rentropy"],
        zip_safe=False,
        classifiers=[
            "Programming Language :: Rust",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Topic :: Utilities",
            ]
)
