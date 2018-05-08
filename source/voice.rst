===============================================
Voice API
===============================================

The Voice API allows you to interact with a phone via beautiful HTTP endpoints.

.. warning::
   *  There is a minimum amount of credits which you need to have in order to make a Voice API call,
      regardless of the cost of the call itself. Please refer to the `Help Center <https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/minimum-credits-for-voice-api/>`_ for more information.

.. _simple-playback-api-ref:

Simple Playback API
===============================================

To make a call and playback an audio file when your recipient answers the phone,
make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/voice/simple/playbacks/

with the following parameters:

    =============  ========================  ========  =============  =============================
    Name           Description               Required  Data Type      Example
    =============  ========================  ========  =============  =============================
    caller         Caller number             Yes       Numeric        +8190123456789
    recipient      Call recipient            Yes       E.164          +8190123456789
    recording_url  URL where your mp3 audio  Yes       URL            http://www.mysite.com/123.mp3
                   file is located
    callbackurl    Callback URL              No        URL            http://example.com
    =============  ========================  ========  =============  =============================

.. note::
   Notes on the **recipient** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country
      code then followed directly by the mobile number leaving the local **0** prefix.
   *  Example of a valid recipient is: *+818011234567* with *81* as the Japan country code and *8011234567*
      as the mobile number.

.. _caller-parameter-label:

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
   *  `https` is not supported at this moment.

.. note::
   Samples of valid URL for **recording_url** are as below:

   *  http://a.clyp.it/b3byGhjf.mp3
   *  http://a.clyp.it/b-byghjf.mp3
   *  http://a.clyp.it/b-bygh_f.mp3

.. note::
   Notes on the **callbackurl** parameter:

   *  When this optional parameter is provided, XOXZO cloud will call this URL when the call ended.
   *  XOXZO cloud will call the URL with http POST method. Parameters of the callback is similar to "Checking Call Status API". Please see :ref:`check-call-status-label`.
   *  Callback URL must return http status 200. Until then, we will retry up to a maximum of ten times.


.. _jp-din-caller-label:

JP specific optional parameters
-------------------------------

The additional parameters below are for JP specific usage and recipients:

    ==============  ==================  ========    =================== ===================
    Name            Description         Required    Data Type           Example
    ==============  ==================  ========    =================== ===================
    jp_din_caller   Local caller ID     No          The string **true** true
    ==============  ==================  ========    =================== ===================

Please refer to our `JP Local Caller ID service <https://help.xoxzo.com/xoxzo-cloud-telephony-platform/articles/local-caller-id-for-dial-in-numbers/>`_ for more information.

.. note::
   Notes on the **jp_din_caller** parameter:

   * You are required to subscribe to a Dial In Number in order to use the local caller ID functionality. Please refer to :ref:`subscribe-din-api-ref` for more information.

Examples
-----------------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> \
      --data-urlencode 'caller=<caller>' \
      --data-urlencode 'recipient=<recipient>' \
      --data-urlencode 'recording_url=<recording_url>' \
      https://api.xoxzo.com/voice/simple/playbacks/


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

.. tip:: 
    It's faster to actually try some test code againts the API to see immediate results.
    `Signing up <https://www.xoxzo.com/en/accounts/signup/>`_ takes only a few minutes and it's free


Using Text To Speech with Simple Playback API
-----------------------------------------------

OPTIONAL: For an additional cost, you can use text to speech option instead of pre-recorded mp3 file
when making calls using the Simple Playback API.
To use this option please refer to :ref:`text-to-speech-api-ref`

.. _check-call-status-label:

Checking Call Status
====================================

To check call status, make a GET request to the endpoint followed by
``<callid>``. An example of using curl is below::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/calls/<callid>/

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
        "url": "https://api.xoxzo.com/voice/calls/<callid>/"
    }

.. _call_status_response_label:

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

Simple Conference API
===============================================

The Conference API when executed, will make a call to each of your participants
and connect them automatically to a conference call when they answer the call. 
You can then simultaneously have a conversation with multiple people at
once on the phone. 

To start a conference call, you can use the following API.
make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/voice/simple/conferences/

with the following parameters:

    =============  ========================  ========  ===============  =============================
    Name           Description               Required  Data Type        Example
    =============  ========================  ========  ===============  =============================
    caller         Caller number             Yes       Numeric          +8190123456789
    participants   Conference participants   Yes       E.164            +8190123456789,+8190123456780
    lang           Language of guidance      No        ISO 639-1        en
    =============  ========================  ========  ===============  =============================

.. note::
   Notes on the **participants** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  You need a minimum of 2 participants and up to a maximum of 3 participants,
      separated with a comma (,)
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country
      code then followed directly by the mobile number leaving the local **0** prefix.
   *  Example of a valid participants is: *+818011234567* with *81* as the Japan country code and *8011234567*
      as the mobile number.

.. note::
   Notes on the **lang** parameter:

   *  You can specify the guidance language of the beginning of the conference call with this this parameter.
   *  Two letter language code of the guidance in `ISO 639-1. <https://en.wikipedia.org/wiki/ISO_639-1>`_
   *  This parameter is optional. The default value is **ja**.
   *  Currently, **en** and **ja** are accepted.

.. note::
   Notes on the **caller** parameter:

   * Please see :ref:`caller parameter<caller-parameter-label>`


Response
-----------------------------------------------

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.0 201 CREATED
    Content-Type: application/json

    {
       "conferenceid": "<conferenceid>",
       "participants": [
           {
               "callid": "<callid1>",
               "participant": "<participant1>"
           },
           {
               "callid": "<callid2>",
               "participant": "<participant2>"
           }
       ]
    }

Response Data
-----------------------------------------------

    ============== =============================================
    Name           Description
    ============== =============================================
    conferenceid   The unique conference id for this conference
    participants   A list about each participant's call
    callid         The unique call id for the participant
    participant    The participant number that was called
    ============== =============================================

Checking Conference Status
====================================

To check conference status, make a GET request to the endpoint followed by
``<conferenceid>``. An example of using curl is below::


   curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/simple/conferences/<conferenceid>/

Every time you make a canference, you will get a response containing ``<conferenceid>``.
Use this ``<conferenceid>`` to check call status.

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::


   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "cost": 65,
       "participants": [
           {
               "status": "ANSWERED",
               "recipient": "<recipent1>",
               "cost": 50,
               "caller": "<caller>",
               "callid": "<callid1>",
               "start_time": "2017-10-31 01:17:50",
               "url": "https://api.xoxzo.com/voice/calls/<callid1>/",
               "end_time": "2017-10-31 01:18:00",
               "duration": 1
           },
           {
               "status": "ANSWERED",
               "recipient": "<recipent2>",
               "cost": 15,
               "caller": "<caller>",
               "callid": "<callid2>",
               "start_time": "2017-10-31 01:17:50",
               "url": "https://api.xoxzo.com/voice/calls/<callid2>/",
               "end_time": "2017-10-31 01:18:09",
               "duration": 2
           }
       ],
       "conferenceid": "<conferenceid>",
       "start_time": "2017-10-31 01:17:50",
       "end_time": "2017-10-31 01:18:09",
       "duration": 2
   }


Please see :ref:`call_status_response_label` for details.
