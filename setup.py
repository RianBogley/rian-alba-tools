from setuptools import setup, find_packages

setup(
    name='ALBA_Pipeline',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'nilearn',
        'numpy',
        'openpyxl',
        'pandas',
        'pingouin',
        'plotly',
        'progressbar',
        'ptitprince',
        'scipy',
        'seaborn',
        'sklearn',
        'statsmodels',
        'zentables',
        'joblib',
    ],
    url='https://github.com/RianBogley/ALBA_Pipeline/',
    author='Rian Bogley',
    author_email='rianbogley@gmail.com',
    description='',
)