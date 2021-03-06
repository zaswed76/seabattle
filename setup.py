from os.path import join, dirname

import program
from setuptools import setup, find_packages

setup(
        name="program",
        # в __init__ пакета
        version=program.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['program = program.script:main']
        }

)
