python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/celitech_sdk-1.1.87-py3-none-any.whl --force-reinstall
