#in order to make src directory global we create this file 

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

##making src directory as a package
setup(
    name="src",
    version="0.0.1",
    author="Koushik V",
    description="A small package for dvc ml pipeline    ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoushikVK/Automate-MLPipelines-using-DVC",
    author_email="koushikofficial@yahoo.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)