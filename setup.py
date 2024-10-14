from setuptools import setup, find_packages

setup(
    name="IgaProTest",
    version="0.2.0",
    author="IGA-PRO (admin-iga)",
    description="FOR TEST!!!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/admin-iga/IgaProTest",  # Ссылка на проект
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
