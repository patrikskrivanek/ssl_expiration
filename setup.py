import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sslexp",
    version="v1.0.0",
    scripts=['sslexp'],
    author="Patrik Skřivánek",
    author_email="kriegsmarine1995@gmail.com",
    description="A Python utility for checking states of ssl certificates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/patrikskrivanek/ssl_expiration",
    download_url="https://github.com/patrikskrivanek/ssl_expiration/releases",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ssl certificate check"
)
