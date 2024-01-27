from setuptools import setup, find_packages
from typing import List

def get_requires(file_path : str) -> List[str]:

    HYPHEN_E_DOT = '-e .'

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [item.replace('\n', '') for item in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.0',
    author='manoj',
    author_email='manojdatascientist0101.@gmail.com',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt')

)
