import setuptools

# Read the README file for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Stores Price Prediction'
AUTHOR_USER_NAME = 'MikeOdons'
SRC_REPO = 'mlProject'
AUTHOR_EMAIL = 'michaelodonghanro287@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small Python package for machine learning app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},  # Specify the root package directory
    packages=setuptools.find_packages(where="src")
)