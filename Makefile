all:
	rm -rf build/ dist/ pickledict.egg-info/
	python setup.py sdist bdist_wheel
	twine upload dist/*
