A FastAPI/PostgreSQL version of the bucketier backend which instead stores data indefinatley rather then temporaly. Would need modifications to the frontend for it to work, since this will be using authentication (jwt).

- FastAPI
- PostgreSQL

# Install Dependencies
- Run `pip3 install -r requirements-dev.txt`

# Running Locally
- Run `uvicorn src.main:app --reload`