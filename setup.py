import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="pastepdb",

	# version of the module
	version="0.0.0",

	# Name of Author
	author="Pooria Ahmadi",

	# your Email address
	author_email="pooriababak444@gmail.com",

	# #Small Description about module
	# description="adding number",
    description='Embedded database and easy for use',
	# long_description=long_description,

	# Specifying that we are using markdown file for description
	long_description=long_description,
	long_description_content_type="text/markdown",

	# Any link to reach this module, ***if*** you have any webpage or github profile
	# url="https://github.com/username/",
    url='https://pastep.com',
	packages=setuptools.find_packages(),


	# if module has dependecies i.e. if your package rely on other package at pypi.org
	# then you must add there, in order to download every requirement of package


    install_requires=[
        'betterlog'
    ],
	#	 install_requires=[
	#	 "package1",
	# "package2",
	# ],


	license="MIT",

	# classifiers like program is suitable for python3, just leave as it is.
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
