from setuptools import setup, find_packages

setup(
    name='edsaprojrecsort',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Victor094>/<edsaprojrecsort.git>',
    author='<Victor Nkadimeng>',
    author_email='<magabevic@gmail.com>'
)
