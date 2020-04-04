import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="lab2_kureychik",
    version="0.0.1",
    packages=setuptools.find_packages(),
    author="Pavel Kureychik",
    author_email="kureychik.pasha@mail.ru",
    license='MIT',
    description="BSUIR Python lab2 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)