pip install build
rmdir dist
pip install twine
pip install wheel
python -m build --sdist
twine upload dist/* --testpypi
