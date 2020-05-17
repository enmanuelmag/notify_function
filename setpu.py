import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notify_end",  # Replace with your own username
    version="0.4.0",
    author="Enmanuel Magallanes Pinargote",
    author_email="fmagalla@fiec.espol.edu.ec",
    description="Notify you when a function end",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
