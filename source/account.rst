============================================
Account API
============================================

Account API is a collection of APIs which are useful when dealing with your accounts.

Credit Balance Lookup
============================================
To do a lookup credit balance, make a ``GET`` request to the endpoint::

    https://api.xoxzo.com/you/credits/


Examples
--------------------------------------------

Below is an example request using cURL::
    
    curl -u <SID>:<AUTH_TOKEN>  https://api.xoxzo.com/you/credits/

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "credits": 1000.0
    }


Response data
--------------------------------------------

    =========  ======================================
    Name       Description       
    =========  ======================================
    credits    Current credits balance
    =========  ======================================

