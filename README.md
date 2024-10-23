# SnipIt (URL Shortener)

This is a simple URL shortener built using Django, allowing users to shorten long URLs and retrieve the original URLs via a shortened link. It stores the shortened URL, tracks the number of hits, and the URL expires after a configured time. The architecture consists of a single Django app (`snipit`) with two key API endpoints: one for generating shortened URLs and another for retrieving the original URL.

## How it works

### 1. Create a virtual env and activate it

```bash
python3 -m venv .venv
source .venv/bin/activate 
```

### 2. Install all required libraries

```bash
make install 
```

### 3. Apply the migrations

```bash
make migrate 
```

### 4. Start the server

Now the application will be available in http://127.0.0.1:8000, utilise below 2 API's to shorten any url and then retrieving it

```bash
make start 
```

### 5. Shorten URL (POST)

This API accepts an original URL, generates a shortened version using MD5 hashing, stores it in the database with an expiry of 30 days, and returns the shortened URL.

```bash
curl -X POST http://127.0.0.1:8000/api/v1/shorten/ \
    -d "original_url=https://example.com"
```

### 6. Retrieve Original URL (GET)

```bash
curl -X GET http://127.0.0.1:8000/<shortened_url>/
```
