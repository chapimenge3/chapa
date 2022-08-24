import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Chapa",
    version="0.0.1",
    author="Temkin Mengistu, Chapi",
    author_email="chapimenge3@gmail.com",
    description="Python SDK for Chapa API https://developer.chapa.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chapimenge3/chapa",
    project_urls={
        "Bug Tracker": "https://github.com/chapimenge3/chapa/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"chapa": "chapa"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
)
