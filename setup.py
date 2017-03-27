from setuptools import setup

setup(
    version='0.0.1',
    name="datapop",
    description="A data population and encryption tool for game makers and other content creators.",
    author="Tim Raveling",
    author_email="tsraveling@gmail.com"
    py_modules=['datapop'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        datapop=datapop:cli
    ''',
)