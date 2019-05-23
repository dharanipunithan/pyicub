.PHONY: all setup clean_dist distro clean install testsetup test

NAME='pyicub'
VERSION=`python setup.py -V`

all:
	echo "noop for debbuild"

setup:
	echo "building version ${VERSION}"

clean_dist:
	-rm -f MANIFEST
	-rm -rf dist
	-rm -rf deb_dist

distro: setup clean_dist
	python setup.py sdist

clean: clean_dist
	echo "clean"

install: distro
	sudo checkinstall python setup.py install

testsetup:
	echo "running pyicub tests"

test: testsetup
	nosetests --with-coverage --cover-package=pyicub --with-xunit test