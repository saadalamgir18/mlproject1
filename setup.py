from setuptools import find_packages, setup
from typing import List


Hyphen_E_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if Hyphen_E_dot in requirements:
            requirements.remove(Hyphen_E_dots)
    return requirements



setup(
    name = "mlproject1",
    version = "0.0.1",
    authot = "saad",
    auther_email = "saadalamgir18@gmail.com",
    packages = find_packages(),
    intall_requires = get_requirements("requirements.txt")

)