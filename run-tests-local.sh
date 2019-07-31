echo "Running all integration tests"
python3 -m pytest -s -r chars --base_url ${base_url-"something.com"} integration-tests
sleep 2