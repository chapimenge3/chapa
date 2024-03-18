import setuptools
import os

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

version_number = os.environ.get('CHAPA_VERSION', '0.1.0')

setuptools.setup(
    name='chapa',
    version=version_number,
    author='Temkin Mengistu (Chapi)',
    author_email='chapimenge3@gmail.com',
    description='Python SDK for Chapa API https://developer.chapa.co',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chapimenge3/chapa',
    packages=['chapa'],
    package_dir={'chapa': 'chapa'},
    project_urls={
        'Source': 'https://github.com/chapimenge3/chapa',
        'Bug Tracker': 'https://github.com/chapimenge3/chapa/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=[
        'httpx>=0.27.0',
    ],
)
