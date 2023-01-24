pip install build
rmdir dist
pip install twine
python -m build
twine upload dist/*
