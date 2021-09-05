from setuptools import setup

setup(
    name='IsDigit',
    url='https://github.com/editid0/IsDigit',
    author='editid',
    packages=['isdigit'],
    version='0.0.5',
    license='MIT',
    description='Simple, mainly useless, python package that checks if a string, int, or float is a digit.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    keywords='python isdigit float int string'
)