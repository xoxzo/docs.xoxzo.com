====================================
SMS API
====================================

The SMS API allows you to send/receive SMS to supported carriers via beautiful HTTP endpoints.

Send SMS messages API
====================================
To send a SMS message, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/sms/messages/

with the following parameters:

    ===============  ===========================  ========  ===================  ===================
    Name             Description                  Required  Data Type            Example
    ===============  ===========================  ========  ===================  ===================
    message          Message body                 Yes       UTF-8                こんにちは
    recipient        Message recipient            Yes       E.164                +8190123456789
    sender           Sender ID                    Yes       Alphanumeric         Xoxzo1
    callbackurl      Callback URL                 No        URL                  http://example.com
    tags             Tags                         No        UTF-8                tag1,tag2
    track_link       Enable link tracking         No        The string **true**  true
    lt_callbackurl   Link tracking callback URL   No        URL                  http://example.com
    ===============  ===========================  ========  ===================  ===================

JP specific optional parameters
------------------------------------

The additional parameters below are for JP specific usage and recipients:

    ==============  ===========================   ========    =================== ===================
    Name            Description                   Required    Data Type           Example
    ==============  ===========================   ========    =================== ===================
    jp_kp           K-Premium flag                No          The string **true** true
    jp_kpl          K-Premium Lite flag           No          The string **true** true
    jp_kp_sender    Sender ID for kddi, docomo    No          Numeric             0312341234
    ==============  ===========================   ========    =================== ===================

Please refer to our `K-Premium Service FAQ <https://help.xoxzo.com/xoxzo-cloud-telephony/articles/the-k-premium-service/>`_ for more information on the K-Premium Service.

.. note::
   Notes on the **message** parameter:

   * This is the main message that you'll be sending to the recipient.
   * All messages must be encoded in UTF-8

.. note::
   Notes on **message length**:

   * Message length is counted by the total number of characters in all parts of a message.
   * For single-part ASCII messages, the maximum length is 140 characters.
   * For single-part non-ASCII messages, the maximum length is 70 characters.
   * A long multi-part message is a message that exceeds 140 characters for ASCII and 70 characters for non-ASCII messages.
   * The maximum length for multi-part messages is 660 characters.
   * Multi-part ASCII messages can have up to 5 parts and each part can have up to 132 characters in each part.
   * Multi-part non-ASCII messages can have up to 10 parts and each part can have up to 66 characters in each part.

   ==================== === === === === === === === === === ===
   SMS part count       1   2   3   4   5   6   7   8   9   10
   ==================== === === === === === === === === === ===
   ASCII characters     140 264 396 528 660                 
   non-ASCII characters 70  132 198 264 330 396 462 528 594 660
   ==================== === === === === === === === === === ===

.. note::
   Notes on the **jp_kp** and **jp_kpl** parameter:

   * You cannot specify **jp_kp** and **jp_kpl** together at the same time. These are mutually exclusive.
   * The difference between **jp_kp** and **jp_kpl** is the sender id display for Softbank numbers.
     Please refer **jp_kp_sender** parameter section.

.. note::
   Notes on the **jp_kp_sender** parameter:

   * If the jp_kp or jp_kpl parameter is set to true, you must specify this parameter with your pre-registered number for KDDI/docomo.
   * If the recipient is KDDI/docomo, the value specified for this parameter will be shown on the recipient's mobile.
   * If the **jp_kp** is set and the recipient is Softbank, a fixed number will be shown on the the recipient's mobile instead.
   * If the **jp_kpl** is set and the recipient is Softbank, **sender** will be shown on the the recipient's mobile instead.

.. note::
   Notes on the **jp_kddi_sender** parameter:

   * This parameter is deprecated and can be used until Aug. 31 2020.

.. note::
   Notes on the **recipient** parameter:

   * Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
     when specifying phone numbers.
   * `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country 
     code then followed directly by the mobile number leaving the local **0** prefix .
   * Example of a valid recipient is: *+818011234567* with *81* as the Japan country code and *8011234567* 
     as the mobile number.

.. note::
   Notes on the **sender** parameter:

   * The **sender** parameter does not require a + sign prefix.
   * You can also specify alphanumeric **sender** such as *XOXZO1* or *XOXZO* for the sender. In this case, 
     the maximum length for the **sender** parameter is 10.
   * If the **sender** parameter contains only digits, the maximum length is 15.

.. warning::
   The **sender** is sent as through a best effort method and is not guaranteed to be shown on
   the recipient's mobile as it is and maybe replaced with an arbitrary **sender**. This is dependent on the policies of the carriers, intermerdiary networks and governments, and they may not honour your request.

.. note::
   Notes on the **callbackurl** parameter:

   * When this optional parameter is provided, XOXZO cloud will call this URL when the carrier network notifies us of the SMS delivery status(DLR).
   * XOXZO cloud call the URL with http POST method. Parameters of the callback is similar to "Check SMS status API". Please see :ref:`check-sms-status-label`.
   * Callback URL must return http status 200. Until then, we will retry up to a maximum of ten times.

.. note::
   Notes on the **tags** parameter:

   * When this optional parameter is provided, you can put tags for each API calls and you can retrieve the tags using the check sms status API later.
   * You can put multiple tags separated by the comma. The leading and trailing spaces are removed from the tags.

.. note::
   Notes on the **track_link** parameter:

   * When this optional parameter is provided, link tracking function is enabled. The first URL/domain name
     in the **message** will be replaced with our private short url and you can get the information
     if the user has clicked the link on the mobile terminal. In order to get this information, you have to use
     the :ref:`check-sms-status-label`.
   * Additional credit will be deducted when this parameter is used. Please consult with the `pricing information <https://www.xoxzo.com/about/pricing/>`_.
   * The shortlink will expire in 90 days after it is generated.

.. note::
   Notes on the **lt_callbackurl** parameter:

   * When this optional parameter is provided, XOXZO cloud will call this URL when the user clicks the link tracking short url.
   * XOXZO cloud call the URL with http POST method. Parameters of the callback is similar to "Check SMS status API"
     and it contains the **link_tracking** key with information about when the link has been accessed.
     Please see :ref:`check-sms-status-label`.
   * Callback URL must return http status 200. Until then, we will retry up to a maximum of ten times.
   * The URL called only once when the user clicked the short URL for the first time.

.. warning::
    You need to put at least one ASCII white space(0x20) before and after the link
    in the **message** in order to link tracking work properly.

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

.. tip:: 
    It's faster to actually try some test code againts the API to see immediate results.
    `Signing up <https://www.xoxzo.com/en/accounts/signup/>`_ takes only a few minutes and it's free

.. _check-sms-status-label:

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
        "tags": [
            "tag1",
            "tag2"
        ],
        "url": "https://api.xoxzo.com/sms/messages/<msgid>/",
        "recipient": "<recipient>",
        "cost": 10,
        "sent_time": "2019-03-05 00:37:44",
        "sender": "<sender>",
        "msgid": "<msgid>",
        "status": "DELIVERED"
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
    tags       The tags assigned to this message.
               If no tags are assigned, empty list [] will be set.
    =========  ======================================

If the **track_link** is enabled, following information are also included.

    =============  ============  ========================================
    Name           Key           Description
    =============  ============  ========================================
    link_tracking  accessed      true if the link is accessed already, false if not
    \              accessed_on   The time when the link was first accessed
    \              link          The link originally set in the message
    \              shortlink     The shortened link
    =============  ============  ========================================

example of the response::

    {
        "cost": 15.0,
        "link_tracking": {
            "accessed": false,
            "accessed_on": "",
            "link": "http://www.example.com",
            "shortlink": "https://xoz.so/dbNL4"
        },
        "msgid": "oxgyFO6tfwYkHLIMbURrz5smCv9QT423",
        "recipient": "+818012345678",
        "sender": "XOXZO",
        "sent_time": "2020-10-09 02:37:47",
        "status": "DELIVERED",
        "tags": [],
        "url": "https://api.xoxzo.com/sms/messages/oxgyFO6tfwYkHLIMbURrz5smCv9QT423/"
    }

Sent Messages List API
====================================
You can pull a list of sent messages by making a ``GET`` request to the endpoint::

    https://api.xoxzo.com/sms/messages/

The sent messages results will be sorted based on their newest ``sent_time``. 
This API is useful for creating logs.

You can also pull sent messages for a specified sent date using
``sent_date`` parameter followed by an operator and a date.

    =========  ==================================== ========
    Name       Description                          Required
    =========  ==================================== ========
    sent_date  UTC based date when the message      Yes          
               was sent with following format: 
               YYYY-mm-dd.
               Should be within 90 days from today.
    =========  ==================================== ========

You can use following operator to get a certain date or a range of sent dates from 
the sent messages:

    =========  ===================
    Operator   Name
    =========  ===================
    <=         less than equal
    <          less than
    =          equal
    >          greater than
    >=         greater than equal
    =========  ===================

.. note::
   * The maximum amount of sent messages that can be pulled are limited to 30,000 messages.
   * Only sent messages within 90 days ago that can be be pulled.
   * This API supports only one operator and one specified sent date on each request.
   * All dates are based on UTC.

.. warning::
   * This API call is limited to use up to 3 requests/hour.

Examples of response data
--------------------------

The response data returned by the API is equivalent to what you get from the `Check SMS status API`_

Pull all sent messages
''''''''''''''''''''''

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
           "status": "DELIVERED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
    ]

Pull sent messages on a specified date
''''''''''''''''''''''''''''''''''''''

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
           "status": "DELIVERED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 00:00:00",
           "status": "DELIVERED",
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
           "status": "DELIVERED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-03-04 00:00:00",
           "status": "DELIVERED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
        {
           "cost": 10,
           "msgid": "<msgid>",
           "recipient": "<recipient>",
           "sender": "<sender>",
           "sent_time": "2016-02-15 11:30:47",
           "status": "DELIVERED",
           "url": "https://api.xoxzo.com/sms/messages/<msgid>"
        },
    ]

No sent messages on a specified date
''''''''''''''''''''''''''''''''''''

If there's no sent messages on specified date, empty list with HTTP
``200 OK`` status code will be returned.

Below is an example of request using cURL to pull sent messages that were
sent on 30 January 2016::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_date=2016-01-30

Since there's no message sent on 30 January 2016, the response would an empty
list returned with HTTP ``200 OK`` status code::

    HTTP/1.0 200 OK
    Content-Type: application/json

    []

Invalid requests example
''''''''''''''''''''''''

If the specified date is in invalid format, HTTP ``400 BAD REQUEST`` status
code will be returned.

Below is an example of request using cURL to pull sent messages with
invalid sent date format::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_date=2016-02-30

Since 30 February 2016 is invalid date, HTTP ``400 BAD REQUEST`` status code
will be returned explaining that the ``sent_date`` format is invalid::

    HTTP/1.0 400 Bad Request
    Content-Type: application/json

    {
        "sent_date": [
            "Invalid sent_date format"
        ]
    }

If the specified date is more than 90 days ago, HTTP ``400 BAD REQUEST`` status
code will be returned.

Below is an example of request using cURL to pull sent messages with
sent date more than 90 days ago::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_date=2015-02-28

Since 28 February 2015 is more than 90 days ago, HTTP ``400 BAD REQUEST`` status code
will be returned asking for a valid ``sent_date``::

    HTTP/1.0 400 Bad Request
    Content-Type: application/json

    {
        "sent_date": [
            "Invalid sent_date"
        ]
    }

If the parameter is incorrectly specified, HTTP ``400 BAD REQUEST`` status code
will be returned.

Below is an example of request using cURL to pull sent messages with
incorrect parameter::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/messages/?sent_data=2016-02-28

Since ``sent_data`` is not a correct parameter, HTTP ``400 BAD REQUEST`` status code
will be returned asking for ``sent_date`` parameter::

    HTTP/1.0 400 Bad Request
    Content-Type: application/json

    {
        "sent_date": [
            "This field is required"
        ]
    }


Common message statuses
====================================

This is a list of statuses that you can find in the ``status`` data:

    =================== ===============================
    Message status      Description         
    =================== ===============================
    QUEUED              Message put into queue and will be delivered shortly
    DELIVERED           Message successfully delivered
    DELIVERING          Sending message in progress
    FAIL                Failed to send message
    =================== ===============================
