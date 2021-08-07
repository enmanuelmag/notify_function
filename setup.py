import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notify_function",
    version="1.2.2",
    author="Enmanuel Magallanes Pinargote",
    author_email="enmanuelmag@cardor.dev",
    description="Notify you when a function finished with option to send a email or message to discord channel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enmanuel-mag/notify_function",
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
