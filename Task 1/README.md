# JSONPlaceholder API Automation

A small Python script for the QA Lead assignment. It fetches all posts from the public JSONPlaceholder API, checks for HTTP 200, verifies that every post includes `userId`, `id`, `title`, and `body`, and writes the first five posts to `first_five_posts.json`.

## Run

Python 3.9 or newer is recommended.

```bash
python -m pip install -r requirements.txt
python api_automation.py
```

The output file is created beside the script. The command exits with status 1 and prints an error if the request, response status, JSON format, or post schema is invalid.
