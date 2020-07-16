import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='fixtractor',  
     version='0.1.1',
     scripts=['fixtractor'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you extract files from backup folders or any kind of folders with files that can not be identified.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=setuptools.find_packages(),
     install_requires=["python-magic"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )