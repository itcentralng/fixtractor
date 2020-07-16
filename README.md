# FIXTRACTOR
A simple tool to help you extract files from backup folders or any kind of folders with files that can not be identified for example a corrupt iTunes backup folder.

# REQUIREMENT
You need to install libmagic on your computer [check here](https://github.com/ahupp/python-magic) for how to.

# INSTALLATION
`pip install fixtractor`

# USAGE
`fixtractor -e some/directory/destination`<br />
`fixtractor --extract some/directory/destination`<br />
`fixtractor -e some/directory/destination -m 20mb`<br />
`fixtractor --extract some/directory/destination --minimum 20mb`


# FLAGS
`-e --extract` directory destination, the folder you want to extract from that is.
`-m --minimum` minimum file size you want to extract, default is 0kb, all file sizes that is.


