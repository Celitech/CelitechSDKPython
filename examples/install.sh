python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/celitech_sdk-1.3.42-py3-none-any.whl --force-reinstall
