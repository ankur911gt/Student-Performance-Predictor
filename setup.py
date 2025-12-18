from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function takes the file path as input and returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: #opens the file and reads the lines
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","").strip() for req in requirements] #removes the new line character and whitespace
        #removes the -e . from the requirements
        requirements=[req for req in requirements if req != HYPEN_E_DOT and req != '']
        #returns the list of requirements
    return requirements

setup(
name='Student Performance Predictor',
version='0.0.1',
author='Ankur',
author_email='ankur123info@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)