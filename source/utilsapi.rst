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


