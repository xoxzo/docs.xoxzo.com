==================================== 
Telephony Utilities API
====================================

Telephony Utilities API is a collection of APIs which are useful when dealing with phones and the internet.

Carrier Lookup
====================================
To do a lookup call, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/utilities/carrierlookup/

with the following parameters:

    =========  ==================== ========  ===================  ===================
    Name       Description          Required  Data Type            Example
    =========  ==================== ========  ===================  ===================
    recipient  The number to lookup Yes       E.164                +8190123456789
    =========  ==================== ========  ===================  ===================

.. note::
   Notes on the **recipient** parameter:

   *  Xoxzo uses the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ number format
      when specifying phone numbers.
   *  `E.164 <http://en.wikipedia.org/wiki/E.164>`_ dictates that phone numbers must start with the + prefix and country 
      code then followed directly by the mobile number leaving the local **0** prefix .
   *  Example of a valid recipient is: *+818011234567* with *81* as the Japan country code and *8011234567* 
      as the mobile number.

Examples
------------------------------------

Below is an example request using cURL::
    
    curl -u <SID>:<AUTH_TOKEN> --data-urlencode 'recipient=<recipient>' https://api.xoxzo.com/utilities/carrierlookup/ 

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    [
        {
            "id": "gyt5rrrrrrrrrrr65rfsr43rrrrujgf4"
            "mcc": "440",
            "mnc": "54",
            "mccmnc": "44054",
            "carrier": "KDDI",
            "country": "JP",
            "recipient": "+8190123456789"
            "cost": 5,
        }
    ]

If your lookup failed to identify the carrier for your target recipient, your
response data will be something like this::

   HTTP/1.1 201 Created
   Content-Type: application/json

   [
      {
         "carrier": null, 
         "cost": 5, 
         "country": null, 
         "id": "SPsxrrrrmdCopjYgynTRXrrrrrrDkrrr", 
         "mcc": null, 
         "mccmnc": null, 
         "mnc": null, 
         "recipient": "+8133333333"
      }
   ]


Response data
------------------------------------

    =========  ======================================
    Name       Description       
    =========  ======================================
    id          A unique 32 char id to identify this lookup request
    mcc         The country code of the carrier
    mnc         The network code of the carrier
    mccmnc      The mccmnc code (combination of mcc and mnc) that uniquely identifies this carrier
    carrier     The carrier name
    country     ISO Alpha-2 code of the home country of this carrier
    recipient   The number being queried
    cost        The credits deducted for this API call
    =========  ======================================

.. note::
   Notes on the **mccmnc** data:

   *  The combination of the MCC and MNC code `MCCMNC <https://en.wikipedia.org/wiki/Mobile_country_code>`_ uniquely identifies a certain network operator (carrier)
      anywhere in the world.
   *  Although the operator business name might change due to buyouts or management changes, the MCCMNC code very rarely does.
   *  There are cases where one business entity or operator brand might have multiple MCCMNC codes assigned to it.

If there's invalid parameters given, HTTP ``400 BAD REQUEST`` status code
will be returned. For example, if the ``recipient`` parameter is missing,
the HTTP response should be like this::

    HTTP/1.1 400 BAD REQUEST
    Content-Type: application/json

    {
        "recipient": [
            "This field is required."
        ]
    }


.. _text-to-speech-api-ref:

Text To Speech
====================================
Text to speech is an optional functionality that can be used together with our voice call API.
It is not an API on it's own.

In order to use Text To Speech, you will need to refer to the documentation for the specific
voice API you would like to use. The APIs will have special parameters which you can use
to utilize Text To Speech.

Text to Speech Playback API
====================================

.. warning::

   *  Additional credit will apply. Please check the `priceing page <https://www.xoxzo.com/ja/about/pricing/>`_ for details.


To make a call and playback an text message when your recipient answers the phone,
make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/voice/simple/playback/

with the following parameters:

    =============  ========================  ========  =============  =============================
    Name           Description               Required  Data Type      Example
    =============  ========================  ========  =============  =============================
    caller         Caller number             Yes       Numeric        +8190123456789
    recipient      Call recipient            Yes       E.164          +8190123456789
    tts_message    text to playback          Yes       UTF-8          おはよう
    tts_lang       language of the text      Yes       ISO 639-1      ja
    =============  ========================  ========  =============  =============================

.. note::
   Notes on the **caller** parameter:

   *  Please refer :ref:`simple-playback-api-ref`
.. note::
   Notes on the **recipient** parameter:

   *  Please refer :ref:`simple-playback-api-ref`

.. note::
   Notes on the **tts_message** parameter:

   *  UTF-8 text used for speech synthesis.
   *  Maximum length is 250 characters.
   *  You can not specify **recording_url** parameter with this parameter.

.. note::
   Notes on the **tts_lang** parameter:

   *  Two letter language code of the tts_message in `ISO 639-1. <https://en.wikipedia.org/wiki/ISO_639-1>`_
   *  This paramter must exist when tts_message is used.
   *  Currently, only **'ja'** is accepted.

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN>
         --data-urlencode 'caller=<caller>' \
         --data-urlencode 'recipient=<recipient>' \
         --data-urlencode 'tts_message=おはよう' \
         --data-urlencode　'tts_lang=ja' \
         https://api.xoxzo.com/voice/simple/playback/

Response data
------------------------------------

As for the resopnse, peleae refer :ref:`simple-playback-api-ref`