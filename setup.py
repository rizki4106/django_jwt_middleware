from setuptools import setup

with open("README.md", "r") as files:
    readme = files.read()
    files.close()

setup(
    name="vidstream",
    version="1.0.0",
    author="Rizki Maulana",
    author_email="rizkimaulana348@gmail.com",
    description="Authorize request with jsonwebtoken",
    long_description_content_type="text/markdown",
    long_description=readme,
    install_requires=['django', 'jwt'],
    keywords=["django", "jwt", "jsonwebtoken", "middleware"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)