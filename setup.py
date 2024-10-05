from setuptools import setup, find_packages

setup(
    name='folder-explorer',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'folder-explorer=src.folder_explorer:main',
        ],
    },
)