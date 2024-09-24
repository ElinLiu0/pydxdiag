wheel:
	powershell Remove-Item -Recurse -Force dist
	powershell Remove-Item -Recurse -Force build
	powershell Remove-Item -Recurse -Force pydxdiag.egg-info
	python setup.py bdist_wheel sdist
install:
	powershell Remove-Item -Recurse -Force dist
	powershell Remove-Item -Recurse -Force build
	powershell Remove-Item -Recurse -Force pydxdiag.egg-info
	python setup.py install
uninstall:
	pip uninstall -y pydxdiag
token:
	powershell start https://pypi.org/manage/account/
publish:
	twine upload dist/*
testing:
	cd test && python test.py
gendoc:
	cd doc && make html
viewdoc:
	powershell start doc/_build/html/index.html