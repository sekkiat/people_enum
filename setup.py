from setuptools import setup

setup(
    name='People_Enum',
    version='0.1',
    packages=['People_Enum'],
    entry_points={
        'console_scripts':[
            'People_Enum=People_Enum.__main__:main'
        ]
    }
)
