import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read() 
    # we have to do this as, if we wan to publish this project as a package in the PyPi
    # so this is the thing it will be published at that site(readme)

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "jaisehgal007"
SRC_REPO = "textSummarizer" # this is installed as my local package
AUTHOR_EMAIL = "jaisehgal511@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for NLP Text Summarizer application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/jaisehgal007/Text-Summarizer",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }
)
