from setuptools import setup, find_packages

setup(
    name='django-likes',
    version='dev',
    description='Django app providing view interface to django-secretballot.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-likes',
    packages = find_packages(),
    include_package_data=True,
)
