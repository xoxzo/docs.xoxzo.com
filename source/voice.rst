===============================================
Voice API
===============================================

The Voice API allows you to interact with a phone via beautiful HTTP endpoints.

.. warning::
   *  There is a minimum amount of credits which you need to have in order to make a Voice API call,
      regardless of the cost of the call itself. Please refer to the `Help Center <http://bit.ly/1TxHmrR>`_ for more information.

.. _simple-playback-api-ref:

Simple Playback API
===============================================

To make a call and playback an audio file when your recipient answers the phone,
make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/voice/simple/playback/

with the following parameters:

    =============  ========================  ========  =============  =============================
    Name           Description               Required  Data Type      Example
    =============  ========================  ========  =============  =============================
    caller         Caller number             Yes       Numeric        +8190123456789
    recipient      Call recipient            Yes       E.164          +8190123456789
    recording_url  URL where your mp3 audio  Yes       URL            http://www.mysite.com/123.mp3
                   file is located
    =============  ========================  ========  =============  =============================

.. note::
   Notes on the **recipient** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country
      code then followed directly by the mobile number leaving the local **0** prefix.
   *  Example of a valid recipient is: *+818011234567* with *81* as the Japan country code and *8011234567*
      as the mobile number.

.. note::
   Notes on the **caller** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country
      code then followed directly by the mobile number leaving the local **0** prefix.

.. warning::
   *  The **caller** is sent as through a best effort method and is not guaranteed to be shown on
      the recipient's mobile as it is and maybe replaced with an arbitary **caller**. This is dependent on the
      policies of the carriers, intermerdiary networks and governments, and they may not honour your request.

.. _playback-usable-url-ref:

.. note::
   Notes on the **recording_url** parameter:

   *  The mp3 file specified by the URL **MUST** be publicly accessible.
   *  The URL can **ONLY** contain ascii letters or digits, underscores, slash or hyphens.

.. note::
   Samples of valid URL for **recording_url** are as below:

   *  http://a.clyp.it/b3byGhjf.mp3
   *  http://a.clyp.it/b-byghjf.mp3
   *  http://a.clyp.it/b-bygh_f.mp3


Examples
-----------------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> \
      --data-urlencode 'caller=<caller>' \
      --data-urlencode 'recipient=<recipient>' \
      --data-urlencode 'recording_url=<recording_url>' \
      https://api.xoxzo.com/voice/simple/playback/


Response
-----------------------------------------------

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.0 201 CREATED
    Content-Type: application/json

    [
        {
            "callid": "<callid>"
        }
    ]

If there's invalid parameters given, HTTP ``400 BAD REQUEST`` status code will
be returned. For example, if the ``caller``
parameter is missing, the HTTP response should be like this::

    HTTP/1.0 400 BAD REQUEST
    Content-Type: application/json

    {
        "caller": [
            "This field is required."
        ]
    }


Response Data
-----------------------------------------------

   =========   ======================================
   Name        Description
   =========   ======================================
   callid      The unique call id for this call
   =========   ======================================


Using Text To Speech with Simple Playback API
-----------------------------------------------

OPTIONAL: For an additional cost, you can use text to speech option instead of pre-recorded mp3 file
when making calls using the Simple Playback API.
To use this option please refer to :ref:`text-to-speech-api-ref`

Checking Call Status
====================================

To check call status, make a GET request to the endpoint followed by
``<callid>``. An example of using curl is below::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/simple/playback/<callid>/

Every time you make a call, you will get a response containing ``<callid>``.
Use this ``<callid>`` to check call status.

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.0 200 OK
    Content-Type: application/json

    {
        "callid": "<callid>",
        "cost": 10,
        "duration": 11,
        "start_time": "2015-09-08 12:50:05",
        "end_time": "2015-09-08 12:50:16",
        "status": "ANSWERED",
        "caller": "<caller>",
        "recipient": "<recipient>",
        "url": "https://api.xoxzo.com/voice/simple/playback/<callid>/"
    }

Response data
-----------------------------------------------

    =========== ======================================
    Name        Description
    =========== ======================================
    callid      The unique call id for this call
    cost        The cost in credits for this call
    duration    The duration of the call
    start_time  The time when the call was made (in UTC)
    end_time    The time when the call ended (in UTC)
    caller      The caller number
    recipient   The recipient number
    =========== ======================================

Common call statuses
-----------------------------------------------

This is a list of statuses that you can find in the ``status`` data:

   ===================  ==================
   Call status          Description
   ===================  ==================
   ANSWERED             The call was answered by the recipient, or was passed to
                        a mailbox
   FAILED               The call failed to connect to the recipient
   IN PROGRESS          The call is still in progress
   NO ANSWER            The call was not answered by the recipient
   ===================  ==================

