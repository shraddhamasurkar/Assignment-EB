# JSONPlaceholder API Automation

A small Python script for the QA Lead assignment. It fetches all posts from the public JSONPlaceholder API, checks for HTTP 200, verifies that every post includes `userId`, `id`, `title`, and `body`, and writes the first five posts to `first_five_posts.json`.

It also includes parameterized pytest coverage for `/posts`, `/comments`, and `/users`, with Pydantic schema validation and a response time requirement of less than two seconds per endpoint.

## Run

Python 3.9 or newer is recommended.

```bash
python -m pip install -r requirements.txt
python api_automation.py
pytest -v
```

The output file is created beside the script. The command exits with status 1 and prints an error if the request, response status, JSON format, or post schema is invalid.

The pytest suite calls the live public API, so it requires an internet connection. Each request uses a two-second timeout and the test asserts elapsed request time is under two seconds.
