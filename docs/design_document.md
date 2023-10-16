# Design Document

## Email Automation and Response Tracking

This document outlines the design and implementation of the email automation and response tracking functionality in our system. The goal is to enable the system to send personalized emails to brands and track their responses. This functionality enhances the communication between influencers and brands and provides valuable insights for analytics.

### Third-party Email Service Provider

We have chosen SendGrid as our third-party email service provider. SendGrid supports both email automation and response tracking features, making it an ideal choice for our requirements.

### Integration Process

The SendGrid SDK has been integrated into our project. The `send_email` and `track_response` functions in the `cloud_functions/functions.py` file use the SendGrid API to send emails and track responses.

### Send Email Function

The `send_email` function sends personalized emails to brands. It takes the brand and influencer data as parameters and uses the SendGrid API to send the email. The email content is dynamic and customizable based on the brand and influencer data.

### Track Response Function

The `track_response` function tracks and records brand responses. It uses the SendGrid tracking mechanisms to track the responses and stores the response data in the Firestore database for further analysis and reporting.

### Configuration Steps

To set up SendGrid and obtain the necessary API keys, follow these steps:

1. Sign up for a SendGrid account.
2. Navigate to the API Keys section in the SendGrid dashboard.
3. Create a new API key with full access permissions.
4. Store the API key in a secure location.

### Limitations and Restrictions

SendGrid imposes certain limitations and restrictions, such as email sending limits and tracking capabilities. Please refer to the SendGrid documentation for more information.

### Unit Tests

Comprehensive unit tests have been written to validate the functionality of the `send_email` and `track_response` functions. These tests are located in the `tests/test_functions.py` file. To run the tests, use the following command: `python -m unittest tests/test_functions.py`.

### Future Improvements

While the current implementation meets our requirements, there are potential limitations and edge cases that could be addressed in future improvements. For example, the system could be enhanced to handle larger volumes of emails and to provide more detailed tracking data.