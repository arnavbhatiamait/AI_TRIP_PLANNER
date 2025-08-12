from setuptools import find_packages, setup
from typing import List
def get_requirements(path ="./requirements.txt") -> List[str]:
    requirement_list:List[str] = []
    try:
        with open(path) as f:
            lines=f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except Exception as e:
        print(f"Error reading {path}: {e}")
    return requirement_list

print(get_requirements())
setup(
    name="AI_TRIP_PLANNER",
    version="0.0.1",
    author="Arnav Bhatia",
    author_email="arnavbhatiamait@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)