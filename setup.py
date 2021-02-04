import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pickledict",
    version="1.0.1",
    author="driazati",
    author_email="email@example.com",
    description="Auto-saving dicts and lists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/driazati/pickledict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
