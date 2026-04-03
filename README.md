# QA API Testing Project

This project demonstrates basic API testing using Python and pytest.

## Project Description

The goal of this project is to test a public REST API and validate its behavior under different scenarios.

## What is tested

- Successful API response (status 200)
- Handling of non-existing resources (status 404)
- Validation of response data (JSON fields like id, username, email)

## Technologies

- Python
- pytest
- requests

## How to run tests

```bash
python -m pytest
```

## Example test cases

- Retrieve existing user
- Handle non-existing user
- Validate response data structure

Tests can be executed automatically using pytest.
