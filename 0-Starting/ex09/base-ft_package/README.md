# Build and install

```bash
pip install build
python -m build # create the dist folder

# Install: one of these
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# Check install
pip show -v ft_package
``