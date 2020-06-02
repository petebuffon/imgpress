from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='imgpress',
    version='0.1.0',
    author='Pete Buffon',
    author_email='pabuffon@gmail.com',
    description='A utility for encoding and compressing images for optimal web use.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/petebuffon/imgpress',
    packages=find_packages('src'),
    package_dir={'': 'src'}, 
    install_requires=['pillow'],
    entry_points={
        'console_scripts': [
            'imgpress=imgpress.cli:main'
        ],
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires=''
)
