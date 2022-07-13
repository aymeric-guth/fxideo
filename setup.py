from setuptools import setup, find_packages


setup(
    name="fxideo",
    version="0.0.1",
    license="GPLv2+",
    url="https://git.ars-virtualis.org/yul/fxideo",
    description="string wrapper for ideographic characters handling in terminal based display",
    author_email="aymeric.guth@protonmail.com",
    author="Aymeric Guth",
    packages=find_packages(),
    package_data={"fxideo": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v2 or later(GPLv2+)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
