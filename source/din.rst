============================================
Dial In Numbers API
============================================

The Dial In Numbers API allows you to receive and manipulate phone numbers and incoming phone calls via easy APIs

Finding a Dial In Number via API
============================================

This API allows for listing and subscribing to a Dial In Number (DIN).

To list available DINs, make a ``GET`` request to::

    https://api.xoxzo.com/voice/dins/

The response will be a JSON structure, returned with HTTP ``200 OK`` status code like::

    HTTP/1.1 200 OK
    Allow: GET, HEAD, OPTIONS
    Connection: keep-alive
    Content-Type: application/json

    [
        {
            "country_code": "81", 
            "din": "815012345678", 
            "din_uid": "JPafr34rafic76tf", 
            "minute_cost": 1, 
            "monthly_cost": 650.0, 
            "prefix": "50"
        }, 
        {
            "country_code": "81", 
            "din": "81312345678", 
            "din_uid": "JPascfdrwersdf12", 
            "minute_cost": 10, 
            "monthly_cost": 1900.0, 
            "prefix": "3"
        }
    ]

Response data
-------------------------------------------

    =============   ======================================
    Name            Description       
    =============   ======================================
    country_code    The country code for this DIN, dependent on it's country
    din             The E.164 version of the DIN, including country code
    din_uid         A unique identifier for this particular DIN
    minute_cost     The credit cost per minute when receiving calls to this DIN
    monthly_cost    The monthly credit cost of subscribing to this DIN
    prefix          The local area prefix for this DIN, without the 0
    =============   ======================================


You can also filter using a country code or a prefix::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/?country=JP

Or::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/?prefix=813

filtering using country or prefix will only return you the relevant DINs based on your filter.

Subscribing to a Dial In Number via API
============================================

To subscribe to a DIN, send a ``POST`` request like::

    curl -u <SID>:<AUTH_TOKEN> -d'din_uid=<din_uid>' https://api.xoxzo.com/voice/dins/subscriptions/

where ``<din_uid>`` is the value you got from the previous ``GET`` request for the number you want to subscribe to.

The response will return with HTTP ``201 OK`` to indicate that the subscription was succesfull.

.. warning::
   *  Your credits will be charged immediately for the monhtly subscription if your ``POST`` request succeeds

Each Dial In Number can be attached an action that will provide instruction what to do with the call if it was answered::

    curl -u <SID>:<AUTH_TOKEN> -d'action_url=<url>' https://api.xoxzo.com/voice/dins/subscriptions/<din_uid>/

The ``url`` specified for ``action_url`` will be called via ``GET`` when there is incoming call to your subscribed DialIN number to get a command that will be
used to handle the call. 

Unsubscribing to a Dial In Number via API
============================================

To unsubscribe::

    curl -XDELETE -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/subscription/<din_uid>/


What are Actions?
============================================

An Action is something that you tell us to do when a call comes in via your subscribed Dial In Number (DIN).
These can be things like transfering the incoming call to a different number, or playing a music file.

Avaialable Actions are listed at `Available Actions`_

The Actions that you want to do are defined in a simple text file that you make accessible
via a URL. This URL is the ``action_url`` that you set when you subscribe to a DIN.

When a call comes in to your DIN, we'll make a ``GET`` request to your ``action_url`` that will also include
information about the call, like::

    GET /command/?caller=+8180123456789&recipient=+8150123456789

Where ``caller`` is the caller id of the phone making the call and ``recipient`` is your DIN.

Available Actions
-------------------------------------------

The available actions are as follows:

    =============   ======================================
    Action          Description       
    =============   ======================================
    playback        Plays back an mp3 file to the caller
    transfer        Transfers the incoming call to another number
    =============   ======================================


Sample
-------------------------------------------

Your ``action_url`` must return the following output in plain text format::

    playback http://example.com/media.mp3

Where ``playback`` contains a required paramater that points to the URL of the mp3 file you want to play.

For ``transfer``, you'll need to also include a required parameter of the number you want to transfer to::

    transfer +81807181881 --caller=+8190123456789

``caller`` is an optional argument to set the caller id when you transfer the call.

.. warning::
   *  The **caller** is sent as through a best effort method and is not guaranteed to be shown on
      the recipient's mobile as it is and maybe replaced with an arbitary **caller**. This is dependent on the 
      policies of the carriers, intermerdiary networks and governments, and they may not honour your request.


