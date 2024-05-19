from setuptools import setup,find_packages

setup(
    name='PyKozo',
    version='0.0.2',
    license='MIT',
    description='PyKozo is a Python library that allows for complete web development using Python scripts.',
    author='Miguel Nevado',
    author_email='miangeldev@proton.me',
    url='https://github.com/miangeldev/pykozo',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['pykozo','html','tags','web','development']
)