## setup.py is responsible to create ML applications as a package files and we can use this package to install in our application 
## even we can deploy this package in pypi so any one can use this as package 
from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements =[]
    HYPEN_E_DOT="-e ."
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="MLProjects",
    version="0.0.1",
    author = "Bhavani",
    author_email="durgabhavani777@hotmail.com",
    peckages=find_packages(),
    install_req=get_requirements('requirements.txt')
)