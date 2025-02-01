from setuptools import setup, find_namespace_packages

setup(
    name='stable-diffusion',
    version='0.0.1',
    description='',
    packages=find_namespace_packages(include=['ldm*']),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)