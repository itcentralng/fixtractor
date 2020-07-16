import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='itunes_extractor',  
     version='0.1.0',
     scripts=['itunes_extractor'] ,
     author="Nasir Mustapha",
     author_email="nasir@mrteey.com",
     description="A simple tool to help you extract files from your iTunes backup.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mrteey/flask-setup",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )