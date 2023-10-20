from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_tko',
    version='1.0.0',
    author='Kateryna Tkachuk',
    author_email='chelovek_k@ukr.net',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
)