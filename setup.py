# Author: Elin
# Date: 2024-09-03 14:56:04
# Last Modified by:   Elin
# Last Modified time: 2024-09-03 14:56:04


from setuptools import setup, find_packages

setup(
    name = "pydxdiag",
    version = "0.1.8.1",
    packages = [
        "pydxdiag",
        "pydxdiag.functions",
        "pydxdiag.functions.device",
        "pydxdiag.functions.sz",
        "pydxdiag.schema",
        "pydxdiag.schema.device",
        "pydxdiag.schema.sz",
    ],
    install_requires = [
        "pydantic",
        "beautifulsoup4",
        "lxml"
    ],
    author = "Elin",
    author_email = "982467922@qq.com",
    description = "A python library for parsing dxdiag output",
    long_description_content_type="text/markdown",
    python_requires = ">=3.10",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    long_description=open('README.md',encoding="utf-8").read(),
    url = "https://github.com/ElinLiu0/pydxdiag",
)