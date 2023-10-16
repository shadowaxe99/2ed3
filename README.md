# Email Automation and Response Tracking System

This project is designed to enhance the communication between influencers and brands by automating the process of sending personalized emails and tracking their responses. The system uses a third-party email service provider's SDK or API for email automation and response tracking, and stores the response data in a Firestore database for further analysis and reporting.

## Features

- **Email Automation**: The `send_email` function in the `cloud_functions/functions.py` file sends personalized emails to brands using the email service provider's API. The email content is dynamic and customizable based on the brand and influencer data.

- **Response Tracking**: The `track_response` function in the `cloud_functions/functions.py` file tracks and records brand responses using the email service provider's tracking mechanisms.

## Documentation

- **Design Document**: The `docs/design_document.md` file provides a detailed outline of the email automation and response tracking functionality, including the chosen email service provider and the integration process.

- **API Documentation**: The `docs/api_documentation.md` file provides clear and concise explanations of the `send_email` and `track_response` functions, including the parameters, expected behavior, and any error handling mechanisms. It also includes examples and illustrations to demonstrate the usage of the email automation and response tracking functionality.

- **Guidelines and Best Practices**: The `docs/guidelines_and_best_practices.md` file provides guidelines and best practices for using the email automation and response tracking functionality, including recommendations for email content personalization and tracking data analysis.

## Unit Tests

The `tests/test_functions.py` file contains comprehensive unit tests for the `send_email` and `track_response` functions. Information on how to run these tests and interpret the results is provided in the `docs/guidelines_and_best_practices.md` file.

## Getting Started

To get started with this project, you will need to set up the email service provider and obtain the necessary API keys or credentials. The configuration steps are documented in the `docs/design_document.md` file.

## Limitations and Future Improvements

The system may have some limitations or restrictions imposed by the chosen email service provider, such as email sending limits or tracking capabilities. These are documented in the `docs/design_document.md` file. Recommendations for future improvements are also provided in this document.

## Contribution

We welcome contributions from the community. Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.