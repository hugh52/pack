** To simply and quickly establish this, for both reading packages from the web and reading packages from an existing file, there are only comments within the python files that use traditional looping techniques, opposed to the much more efficient, list comprehension methods show as well (though both implementations should product the same output). **


** Environement Specifics:**

- Anaconda3-2019.10-Linux-x86_64
- Python 3.7.6

** Provided Data - as .txt file or from website **

- 'packages.txt': file of Python packages that include the version; meant to simulate a standard 'requirements.txt' from or for a virtual environment.
- website that includes a table with one column having a list of packages for Anaconda built for Python 3.7 and Linux 64 bit (other Python versions and architectures available from website).

** Data Created From Script(s) **

- 'packages_new.txt' : output of Python packages file 'packages.txt', but without the version constraint present in the original file.
- 'requirements.txt': output of Anaconda packages without the version restriction.

