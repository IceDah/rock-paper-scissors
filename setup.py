from setuptools import setup

setup(
    name='rock-paper-scissors',
    version='0.1',
    description='A  simple rock-paper-scissors game',
    url='https://github.com/IceDah/rock-paper-scissors',
    author='IceDah',
    author_email='',
    license='',
    py_modules=['rock_paper_scissors'],
    install_requires=[
        
    ],
   entry_points={
        'console_scripts': [
            'rock-paper-scissors = rock_paper_scissors:main',
        ],
    },
)
