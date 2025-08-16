from dotenv import load_dotenv
import os
import json
import smtplib

# Load environment variables from .env file
load_dotenv()

def send_email(event, context):
    try:
        # Parse JSON body from HTTP event
        body = json.loads(event.get('body', '{}'))
        receiver = body['receiver_email']
        subject = body['subject']
        text = body['body_text']
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input', 'details': str(e)})
        }

    # Retrieve SMTP credentials from environment variables
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')

    # Debug: Print SMTP configuration (remove or comment out in production)
    print("Pre-flight ENV check:")
    print("SMTP_HOST:", smtp_host)
    print("SMTP_PORT:", smtp_port)
    print("SMTP_USER:", smtp_user)

    msg = f"Subject: {subject}\n\n{text}"

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            print("Starting TLS...")
            server.starttls()
            print("Logging in...")
            server.login(smtp_user, smtp_pass)
            print(f"Sending email to {receiver}...")
            server.sendmail(smtp_user, receiver, msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error during SMTP operation: {e}")
        return {
            'statusCode': 502,
            'body': json.dumps({'error': str(e)})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Email sent successfully'})
    }
