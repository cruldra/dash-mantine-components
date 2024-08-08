.$PROFILE
Set-ConsoleTitle -Title "构建和发布"

& "D:/Workspace/dongjak/dongjak-dash-components/.venv/Scripts/activate.ps1"

npm run build

python setup.py sdist

twine upload -u cruldra -p pypi-AgEIcHlwaS5vcmcCJDMxNjEwMzgxLTBhZTItNDgzYy04YzU2LWI4YWQ3MDk0YWUwNwACH1sxLFsiZG9uZ2phay1kYXNoLWNvbXBvbmVudHMiXV0AAixbMixbImU3OWM5ZTk3LTIzOTktNDMzOS05MzM3LTA0YTYxOTVmMGU0MCJdXQAABiAXPD-7Fne2VaRWmkFCxENukxn3q924UP9DI26WQv5IQA dist/*
