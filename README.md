A PostgreSQL version of the bucketier backend which instead stores data indefinatley rather then temporaly. Would need modifications to frontend to work, since this will be using classic jwt authentication.

# Install Dependencies
- Run `pip3 install -r requirements-dev.txt`

# Running Locally
- Run `uvicorn src.main:app --reload`