from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="orderbook",
    version="0.1.0",
    author="Sydney Medina",
    description="A real-time order book matching engine in Python.",
    packages=find_packages(),
    install_requires=[
        requirements,
    ],
    python_requires=">=3.9",
)
