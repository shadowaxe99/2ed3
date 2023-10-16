# API Documentation

This document provides detailed information about the API of the email automation and response tracking functionality implemented in the `cloud_functions/functions.py` file.

## `send_email` Function

The `send_email` function is used to send personalized emails to brands.

### Parameters

- `brand_data`: A dictionary containing the brand's information. It should include the brand's email address and any other data needed for personalizing the email content.
- `influencer_data`: A dictionary containing the influencer's information. It should include any data needed for personalizing the email content.

### Return Value

The function returns a dictionary with the following keys:

- `status`: A string indicating the status of the email sending operation. It can be 'success' or 'failure'.
- `message`: A string providing more information about the operation's status.

### Error Handling

If an error occurs during the email sending operation, the function will catch the exception and return a dictionary with `status` set to 'failure' and `message` containing the error message.

## `track_response` Function

The `track_response` function is used to track and record brand responses.

### Parameters

- `brand_email`: A string containing the brand's email address. It is used to identify the brand in the response tracking system.

### Return Value

The function returns a dictionary with the following keys:

- `status`: A string indicating the status of the response tracking operation. It can be 'success' or 'failure'.
- `response_data`: A dictionary containing the response data if the operation was successful. It includes the brand's email address, the response time, and the response content.

### Error Handling

If an error occurs during the response tracking operation, the function will catch the exception and return a dictionary with `status` set to 'failure' and `message` containing the error message.

## Running Unit Tests

To run the unit tests for the `send_email` and `track_response` functions, navigate to the `tests` directory and run the `test_functions.py` file. The test results will be displayed in the console.

## Limitations and Restrictions

The email automation and response tracking functionality is subject to the limitations and restrictions imposed by the chosen email service provider. These may include email sending limits, tracking capabilities, and data retention policies. Please refer to the email service provider's documentation for more information.