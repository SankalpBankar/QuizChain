from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Sankalp Bankar',
    author_email='sankalpbankar7@gmail.com',
    install_requires=["groq","langchain","streamlit","python-dotenv","pypdf"],
    packages=find_packages()
)