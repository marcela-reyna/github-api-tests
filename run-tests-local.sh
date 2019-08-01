base_url="https://api.github.com"

echo "Running all integration tests"
python3 -m pytest -s -r chars --base_url ${base_url} tests