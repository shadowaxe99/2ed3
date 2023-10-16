```python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from google.cloud import firestore

# Initialize Firestore
db = firestore.Client()

# Get SendGrid API Key from environment variables
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

def send_email(brand_email, influencer_name, brand_name, email_content):
    """
    Function to send personalized emails to brands using SendGrid API.
    """
    message = Mail(
        from_email='no-reply@influencer.com',
        to_emails=brand_email,
        subject=f'New Collaboration Request from {influencer_name}',
        html_content=email_content.format(influencer_name=influencer_name, brand_name=brand_name))

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

def track_response(brand_email):
    """
    Function to track and record brand responses using SendGrid's Event Webhook.
    """
    # Get the collection of responses from Firestore
    responses = db.collection('responses')

    # Query for the brand's response
    query = responses.where('email', '==', brand_email).stream()

    # Print the response data
    for doc in query:
        print(f'{doc.id} => {doc.to_dict()}')

    # Store the response data in Firestore for further analysis
    responses.document().set({
        'email': brand_email,
        'response': doc.to_dict()
    })
```