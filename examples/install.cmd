python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\celitech_sdk-1.3.4-py3-none-any.whl --force-reinstall
