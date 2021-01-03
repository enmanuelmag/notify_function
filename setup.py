import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notifier_function",  # Replace with your own username
    version="1.5.1",
    author="Enmanuel Magallanes Pinargote",
    author_email="fmagalla@fiec.espol.edu.ec",
    description="Notify you when a function finished with option to send a email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enmanuel-mag/notifier_function",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'py-notifier',
    ],
    python_requires='>=3.6',
)
