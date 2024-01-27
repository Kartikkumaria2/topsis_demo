from setuptools import setup, find_packages

setup(
    name='topsis_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'topsis_demo = topsis_demo.topsis_demo:main',
        ],
    },
)