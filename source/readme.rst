====================================
README
====================================

About this document
====================================
This document aims to be the starting point for you to start exploring the 
rest of the documentation for the Xoxzo Cloud Telephony Platform.

General Usage
====================================

All APIs uses standard HTTP error codes to signify if a request was successful
or otherwise. Successful requests returns ``2xx`` error codes such as ``200`` or ``201``, 
while failed requests returns something else.

As an example, if your request to an endpoint like::

    https://api.xoxzo.com/voice/simple/playbacks/

was successful and accepted for processing, you will get a response such as::

    HTTP/1.0 201 CREATED

On the other hand, if your request was invalid and not accepted for processing,
you will get a non-200 error code, such as ``400`` and will contain
more information on the error in the body of the response such as::

    HTTP/1.0 400 BAD REQUEST
    Content-Type: application/json

    {
        "recording_url": [
            "This field is required."
            ]
    }



Rate limiting
------------------------------------

When the server load goes too high, rate limiting will apply. You will get response such as::

    HTTP/1.0 429 Too Many Requests
    Content-Type: application/json

    {
        "detail":"Request was throttled. Expected available in 1 second."
    }
