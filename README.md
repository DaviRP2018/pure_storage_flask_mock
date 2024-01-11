# Pure Storage API Mock

## Overview

This project provides a mock implementation of Pure Storage API, primarily focusing on authentication simulation. It allows developers to test their applications against a simulated Pure Storage environment without making actual API calls.

## Features

- Simulates Pure Storage authentication process.
- Provides mock responses for various API endpoints.


## Manage certificates
* https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

Creating new cert and key
```bash
cd server
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

Export to SL1 or CentOS client and trust
```bash
scp cert.pem key.pem <user>@<address>:

# <address>
sudo trust anchor --store cert.pem
```


### Easy and background usage

## Docker

Just run the docker container
```bash
./start.sh
```


### Manual usage (better for debugging)

## Installation

1. Clone the repository:

```bash
git clone <remote>
```

2. Navigate to the project directory:

```bash
cd pure_storage_flask_mock
```

3. Create env

```bash
python -m venv venv
source venv/bin/activate
```

4. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python server/wsgi.py
```

2. The mock API will be accessible at [https://localhost:8000](https://localhost:8000).

## API Endpoints

- **Authentication:**
  - `/api/1.4/auth/token`: Simulates token generation.

- **Sample Endpoints:**
  - `/api/1.4/array`: Mock data for arrays.
  - `/api/1.4/version`: Mock data for version.

## Settings

If you want to change any settings like host, port, token, go to `settings.py`.
Avoid using ports bellow 1024 because they need privileged access.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
