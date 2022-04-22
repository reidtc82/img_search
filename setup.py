from setuptools import setup, find_packages

requires = ["flask", "flask-sqlalchemy", "psycopg2", "flask_wtf"]

setup(
    name="img_search",
    version="0.0",
    description="An image search clone built with Flask",
    author="Reid Case",
    keywords="image search flask",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
