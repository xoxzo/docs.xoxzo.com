====================================
OTP API
====================================

The OTP API allows you to send and verify one-time passwords (OTP) via SMS using HTTP endpoints.

Register Website API
====================================
To register a new website domain, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/otp/register-website/

with the following parameters:

    ===========  ============================  ========  ============  ============
    Name         Description                   Required  Data Type     Example
    ===========  ============================  ========  ============  ============
    website      Your domain name              Yes       UTF-8         xoxzo.com
    template_id  Optional OTP template ID      No        Integer       3
    ===========  ============================  ========  ============  ============

Template id is list of templates that currently we have, these are the lists:

    ============ ============================
    template_id  Value
    ============ ============================
    3             あなたの確認コードは123456です。
    ============ ============================

*123456 is example of the numbers OTP


The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "message": "Website registered successfully."
    }


If the website is already registered, the following response will be returned with HTTP ``400 BAD REQUEST`` status code::

    HTTP/1.1 400 BAD REQUEST
    Content-Type: application/json

    {
        "website": [
            "website info with this website already exists."
        ]
    }

.. note::
   * ``template_id`` defaults to 3 if omitted.
   * Your API credentials must be linked to the domain.


Request OTP API
====================================
To send an OTP code to a phone number, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/otp/request/

with the following parameters:

    ===============  ======================================  =========  ================  ====================
    Name             Description                             Required   Data Type         Example              
    ===============  ======================================  =========  ================  ====================
    website          Registered domain                       Yes        UTF-8             xoxzo.com            
    phone_number     Recipient number in E.164 format        Yes        E.164             +818012345678        
    ===============  ======================================  =========  ================  ====================

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "msgid": "1234567890"
    }

.. note::
   * ``400 Bad Request`` is returned if parameters are missing or invalid.
   * ``401 Unauthorized`` is returned for invalid API credentials.
   * One active OTP per phone number per domain is enforced.


Verify OTP API
====================================
To verify an OTP submitted by the user, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/otp/verify/

with the following parameters:

    ==============  ===========================  ========  ============  =================
    Name            Description                  Required  Data Type     Example
    ==============  ===========================  ========  ============  =================
    website         Registered domain            Yes       UTF-8         xoxzo.com
    phone_number    Recipient number             Yes       E.164         +818012345678
    otp             OTP code submitted by user   Yes       Numeric       654321
    ==============  ===========================  ========  ============  =================

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "is_otp_valid": true,
        "user_identifier": "user@xoxzo.com",
        "phone_number": "818012345678",
        "msgid": "1234567890"
        "website": "https://xoxzo.com",
    }

Below is an example of a failed verification::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "is_otp_valid": false
    }

.. note::
   * OTP verification requires exact match of phone number and domain.
   * OTPs are valid for a limited time and only one active OTP is allowed per number/domain.
