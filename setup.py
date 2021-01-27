import setuptools

setuptools.setup(
    name='django-spaceless-middleware',
    version='2021.1.27',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
