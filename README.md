# Serverless Python Email API

This is a Serverless Framework project that creates a REST API to send emails via SMTP using Python. The API accepts JSON input with the recipient email, subject, and message body, then sends the email accordingly.

---

## Features

- Serverless REST API using AWS Lambda (locally via serverless-offline)
- Sends emails using SMTP with TLS encryption
- Environment variables managed securely with `.env` and python-dotenv
- Detailed error handling and appropriate HTTP response codes
- Easy local development and testing with Serverless Framework offline plugin

---

## Prerequisites

- Node.js (v12+ recommended) with npm
- Python 3.8 or higher
- Serverless Framework CLI installed globally:  

npm install -g serverless

- A Gmail account with 2-Step Verification enabled and an **App Password** generated for
- Python dependencies installed (`python-dotenv`)
---
## Setup
1. Clone or download this repository.
2. Install Node.js dependencies and Serverless plugins:

npm install

3. Create a `.env` file in the project root with your SMTP credentials:

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

> **Note:** For Gmail, generate an **App Password** at https://myaccount.google.com/apppa
4. Ensure your `.env` file is not committed to version control by verifying `.gitignore`.
---
## Running Locally
Start the serverless offline server for local testing:

serverless offline

The API will be available at:

http://localhost:3000/dev/send-email

---
## API Usage
### Endpoint
`POST /dev/send-email`
### Request Body (JSON)

{
"receiver_email": "recipient@example.com",
"subject": "Hello",
"body_text": "This is a test email"
}


### Successful Response

{
"message": "Email sent successfully"
}

### Error Responses
- 400 Bad Request: When the input JSON is invalid or missing fields
- 502 Bad Gateway: When SMTP authentication fails or connection to the SMTP server cannot
---

---
## Troubleshooting
- Verify SMTP credentials (`SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`).
- Ensure 2-Step Verification is enabled on Gmail and use an App Password.
- Check your network or firewall does not block SMTP port 587.
- Add debugging prints (already included in `handler.py`) to isolate issues.
---
## Author
Atla Lakshmi Sindhura
