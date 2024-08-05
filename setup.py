from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="generateMFT",
    version="1.0.0",
    author="Benjamin Cance",
    author_email="bjc@tdx.li",
    description="A project to generate MFT tables with varied errors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rowingdude/generateMFT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # None yet.
    ],
)
