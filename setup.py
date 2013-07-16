from setuptools import setup

setup(
    name = "pantograph",
    version = "0.1.0",
    author = "Howard Mao",
    author_email = "zhehao.mao@gmail.com",
    description = "Python library for drawing on HTML5 canvas",
    url = "https://github.com/adicu/pantograph",
    license = "MIT",

    packages = ["pantograph"],
    install_requires = ["tornado>=2.2"]
)