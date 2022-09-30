# configuration files
based on the module: https://docs.python.org/3/library/configparser.html

The file "configuration.py" provides the class "Configuration". It is basically a wrapper class around the
configparser, to handle the file operations.


## VCS
When using git or other Online-VCS it is not a good idea to place credentials within the source code. config files are
a good alternative to handle credentials outside the source code. It is also more user-friendly. In order to keep config
files outside the VCS, these files should be using the extension *.conf and this extension can then be added to the 
.gitignore-file.
