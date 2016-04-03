==================================== 
SMS API
====================================

The SMS API allows you to send SMS to supported carriers via beautiful HTTP endpoints.

Send SMS messages API
====================================
To send a SMS message, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/sms/messages/

with the following parameters:

    =========  ==================  ========  ===================  ===========================  ===================
    Name       Description         Required  Data Type            Max Length                   Example
    =========  ==================  ========  ===================  ===========================  ===================
    message    Message body        Yes       UTF-8                ASCII: 160, Non-ASCII: 70    こんにちは
    recipient  Message recipient   Yes       E.164                Min:10, Max:15               +8190123456789
                                                                  (exclude + sign prefix)
    sender     Sender ID           Yes       Alphanumeric         15 digit or 10 alphanumeric  Xoxzo1
    =========  ==================  ========  ===================  ===========================  ===================

JP specific optional parameters
------------------------------------

The additonal parameters below are for JP specific usage and recipients:

    ==============  ==================  ========    =================== =========================== ===================
    Name            Description         Required    Data Type           Max Length                  Example
    ==============  ==================  ========    =================== =========================== ===================
    jp-kp           K-Premium flag      No          The string **true** N/A                         true 
    jp-kddi-sender  Sender ID for au    No          Numeric             Min:10, Max:12              0312341234
    ==============  ==================  ========    =================== =========================== ===================

Please refer to our `K-Premium Service FAQ <http://help.xoxzo.com/customer/en/portal/articles/2264921--sms-api-the-k-premium-service>`_ for more information on the K-Premium Service.

.. note::
   Notes on the **recipient** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country 
      code then followed directly by the mobile number leaving the local **0** prefix .
   *  Example of a valid recipient is: *+818011234567* with *81* as the Japan country code and *8011234567* 
      as the mobile number.

.. note::
   Notes on the **sender** parameter:

   *  The **sender** parameter does not require a + sign prefix.
   *  You can also specify alphanumeric **sender** such as *XOXZO1* or *XOXZO* for the sender. In this case, 
      the maximum length for the **sender** parameter is 10.
   * If the **sender** parameter contains only digits, the maximum length is 15.

.. warning::
   The **sender** is sent as through a best effort method and is not guaranteed to be shown on
   the recipient's mobile as it is and maybe replaced with an arbitary **sender**. This is dependent on the 
   policies of the carriers, intermerdiary networks and governments, and they may not honour your request.

.. note::
   Notes on the **message** parameter:

   *  This is the main message that you'll be sending to the recipient.
   *  All messages must be encoded in UTF-8
   *  Messages which only contains ASCII based characters will have a maximum 
      length of 160 characters, while other types of messages will have a 
      maximum length of 70 characters

Examples
------------------------------------

Below is an example request using cURL::
    
    curl -u <SID>:<AUTH_TOKEN> --data-urlencode 'recipient=<recipient>' --data-urlencode 'sender=<sender>' --data-urlencode 'message=<message>' https://api.xoxzo.com/sms/messages/

The ``<message>`` in the above example **must** be encoded in UTF-8 before sending.

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    [
        {
            "msgid": "<msgid>"
        }
    ]

Response data
------------------------------------

    =========  ======================================
    Name       Description       
    =========  ======================================
    msgid      The unique message id for this message
    =========  ======================================

If there's invalid parameters given, HTTP ``400 BAD REQUEST`` status code
will be returned. For example, if the ``message`` parameter is missing,
the HTTP response should be like this::

    HTTP/1.1 400 BAD REQUEST
    Content-Type: application/json

    {
        "message": [
            "This field is required."
        ]
    }

Check SMS status API
====================================

To check a message status, make a GET request to the endpoint followed by ``<msgid>``::

    https://api.xoxzo.com/sms/messages/<msgid>/

Every time you send a SMS, you will get a response which contains ``<msgid>``.
Use this ``<msgid>`` to check SMS status.

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/<msgid>/

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status": "OK",
        "sent_time":"2015-08-27 09:22:32",
        "cost": 10,
        "sender": "<sender>",
        "recipient": "<recipient>",
        "url": "https://api.xoxzo.com/sms/messages/<msgid>/",
        "msgid": "<msgid>"
    }

Below is a sample of a response for a message that failed to be delivered,
returned with a HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "status": "FAIL",
        "sent_time": "2015-09-13 12:47:53",
        "cost": 10,
        "msgid": "<msgid>",
        "recipient": "<recipient>",
        "sender": "<sender>",
        "url": "https://api.xoxzo.com/sms/messages/<msgid>/"
    }

Response data
------------------------------------

    =========  ======================================
    Name       Description       
    =========  ======================================
    status     The status of the sent message
    cost       The cost in credits of this message
    msgid      The unique message id for this message
    recipient  The recipient of this message
    sender     The set sender
    sent_time  The sent time of the message in UTC
    url        The URL of this message status
    =========  ======================================

Common message statuses
====================================

This is a list of statuses that you can find in the ``status`` data:

    =================== ===============================
    Message status      Description         
    =================== ===============================
    QUEUED              Message put into queue and will be delivered shortly
    OK                  Message successfully delivered
    DELIVERING          Sending message in progress
    FAIL                Failed to send message
    =================== ===============================

Pull Sent Messages API
====================================
To pull sent messages, make a ``GET`` request to the endpoint::

    https://api.xoxzo.com/sms/messages/

This request will pull sent messages.

Below is an example of request using cURL to pull sent messages::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.0 200 OK
    Content-Type: application/json

    [
        {
           "cost": 0,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": null,
           "status": "QUEUED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 00:00:00",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
    ]

You can also pull sent messages for a specified sent date using
``sent_date`` parameter followed by an operator and a date.

    =========  ====================================  ========
    Name       Description                           Required
    =========  ====================================  ========
    sent_date  Date when the message was sent with   Yes
               following format: YYYY-mm-dd.
               Should be within 90 days from today.
    =========  ====================================  =========

You can use following operator to get a certain date or a
range of sent dates from the sent messages:

    =========  ===================
    Operator   Name
    =========  ===================
    <=         less than equal
    <          less than
    =          equal
    >          greater than
    >=         greater than equal
    =========  ===================

Below is an example of request using cURL to pull sent messages that were sent
on 4 March 2016::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_date=2016-03-04

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.0 200 OK
    Content-Type: application/json

    [
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 10:15:00",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 00:00:00",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
    ]

Below is an example of request using cURL to pull sent messages that were sent
before and on 4 March 2016::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_date<=2016-03-04

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.0 200 OK
    Content-Type: application/json

    [
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 10:15:00",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 00:00:00",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-02-15 11:30:47",
           "status": "OK",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
    ]

.. note::
   * The maximum amount of sent messages that can be pulled are limited to 5000 messages.
   * Only sent messages within 90 days ago that can be be pulled.
   * Support only one operator and one specified sent date on each request.
