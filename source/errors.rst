====================================
Error List
====================================

This page lists sample error responses and describes in more details the errors that you might encounter
when using the API.

Sample error responses
------------------------------------

Invalid parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: 

    HTTP/1.0 400 BAD REQUEST
    Content-Type: application/json

    {
        "recording_url": [
            "This field is required."
            ]
    }

Invalid SID/Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: 

    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json

    {
        "detail": "Invalid sid/token"
    }

Not Enough Credits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    HTTP/1.0 403 FORBIDDEN
    Content-Type: application/json

    {
        "non_field_errors": [
            "Not enough credits, required: 20"
            ]
    }


Error list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are some of the common errors which you might encounter when using the
API:

   ===========================         ==================================================================
   Error message                       Description         
   ===========================         ==================================================================
   Country not allowed                 Your account is not allowed to send or make calls to this country.
                                       Please contact help@xoxzo.com for more details.
   Invalid sid/token                   The sid or token you're using is invalid.
   Invalid sent_date                   The sent_date should be within 90 days.
   Invalid sent_date format            The sent_date should use following format: YYYY-mm-dd.
   Not enough credits                  Your account doesn't have sufficient credits to use the
                                       API.
   This field is required              A parameter which is required for the API
                                       is missing. Please check your request
                                       again.
   ===========================         ==================================================================


