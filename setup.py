from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
        name="rentropy",
        version="0.1.2",
        rust_extensions=[RustExtension("rentropy.rentropy", binding=Binding.PyO3)],
        packages=["rentropy"],
        zip_safe=False,
)
