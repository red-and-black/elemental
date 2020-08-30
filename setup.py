import setuptools

import elemental


with open("README.rst", "r") as f:
    LONG_DESCRIPTION = f.read()


setuptools.setup(
    name=elemental.__title__.lower(),
    version=elemental.__version__,
    description=elemental.__description__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author=elemental.__author__,
    author_email=elemental.__author_email__,
    license=elemental.__licence__,
    url=elemental.__url__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Testing",
    ],
    keywords="selenium, testing",
    install_requires=[
        "selenium>=3.141",
    ],
    python_requires=">=3.5",
)
