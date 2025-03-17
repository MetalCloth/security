from setuptools import find_packages, setup
from typing import List


e='-e .'

def get_requirements(file_path:str)->List[str]:
    '''Function to get requirements from requirements file'''
    requirements=[]
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[i.replace('\n',"") for i in requirements]
        if e in requirements:
            requirements.remove(e)
    return requirements   
setup(
    name="Network-Security",
    version="0.1",
    author="Puneet Rawat",
    author_email="rawatpuneet927@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
 
 