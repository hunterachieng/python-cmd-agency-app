from setuptools import find_packages, setup

setup(
    name="scripts",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">3.6",
    install_requires =["Click"],
    entry_points={
        'console_scripts':["command_line = scripts.command_line:main"]
    }
)