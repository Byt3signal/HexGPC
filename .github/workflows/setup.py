from setuptools import setup, find_packages

setup(
    name="hexgpc",  
    version="1.0.0", 
    description="An tool that Converts Images into Binary, Reads the Binary pixels converts the Pixels into hexadecimal Values.",
    author="Byt3signal",
    author_email="hexgpcauthor@gmail.com",
    packages=find_packages(),
    install_requires=["Pillow"],  
    python_requires=">=3.6",
)
