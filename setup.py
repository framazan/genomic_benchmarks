from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='genomic-datasets',
    version='0.0.1',
    description='Genomic Datasets',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='RBP Bioinformatics',
    author_email='ML.Bioinfo.CEITEC@gmail.com',
    license='Apache License 2.0',
    keywords=['bioinformatics', 'genomics', 'data'],
    url='https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks',
    # download_url='https://gitlab.com/RBP_Bioinformatics/rbp/-/archive/master/rbp-master.tar.gz',
    packages=find_packages('tools'),
    package_dir={'': 'tools'},
    scripts=[],
    # setup_requires=['pytest-runner'],
    install_requires=[
        'torch',
        'pathlib',
        'biopython>=1.79',
        'requests',
        'pip>=20.0.1',
        'numpy>=1.17.0',
        'pandas>=1.1.4',
        'tqdm>=4.41.1',
    ],
    # tests_require=['pytest'],
    # cmdclass={'test': PyTest},
    include_package_data=True,
    package_data={},
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)