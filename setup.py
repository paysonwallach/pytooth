import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pytooth",
    version="0.1.0",
    author="Payson Wallach",
    author_email="paysonwallach@icloud.com",
    description="A better PyBluez",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paysonwallach/pytooth",
    packages=setuptools.find_packages(),
    classifiers=["Topic :: System :: Networking", "Operating System :: POSIX :: Linux"]
)
