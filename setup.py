from setuptools import setup

setup(
    name="snapshotalyzer",
    version="0.1",
    author="Mario Scalas",
    author_email="mario.scalas@gmail.com",
    description="Snapshotalyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    url="https://github.com/scalasm/snapshotalyzer",
    packages=["shotty"],
    install_requires=[
        "click",
        "boto3"
    ],
    entry_points="""
        [console_scripts]
        shotty=shotty.shotty:cli
    """
)