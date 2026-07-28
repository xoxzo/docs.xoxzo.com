====================================
SMS Templates API
====================================

The SMS Templates API allows you to create and manage reusable SMS message templates
with variable placeholders. Templates must be approved before they can be used to send messages.

.. note::

   CRUD operations (create, list, update, delete) are available via both the API and the
   web interface. Sending SMS and checking message status requires the API.


List Templates API
====================================

To retrieve all templates belonging to your account, make a ``GET`` request to the endpoint::

    https://api.xoxzo.com/sms/templates/

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/templates/

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    [
        {
            "id": 6,
            "name": "Welcome SMS",
            "approved_content": "Hi {name}! This is your discount {order_number}",
            "pending_content": null,
            "status": "APPROVED",
            "api_usage_example": "curl -u sid:token -X POST https://api.xoxzo.com/sms/templates/<template_id>/messages/ -H \"Content-Type: application/json\" -d '{\"sender\":\"TestSender\",\"recipient\":\"+81987654321\",\"variables\":{\"name\":\"Sample_name\",\"order_number\":\"Sample_order_number\"}}'"
        },
        {
            "id": 7,
            "name": "Welcome 2",
            "approved_content": null,
            "pending_content": "Variables must {name}",
            "status": "PENDING",
            "api_usage_example": null
        }
    ]

Response data
------------------------------------

    ====================  =====================================================================
    Name                  Description
    ====================  =====================================================================
    id                    Unique template ID
    name                  Template name
    approved_content      The currently approved message content. ``null`` if not yet approved.
    pending_content       Content awaiting approval. ``null`` if no pending revision.
    status                Approval status: ``APPROVED`` or ``PENDING``
    api_usage_example     A ready-to-use cURL command for sending SMS with this template.
                          Only present for ``APPROVED`` templates. ``null`` for non-approved
                          templates.
    ====================  =====================================================================

.. note::

   Notes on the **api_usage_example** field:

   * This field is only returned for ``APPROVED`` templates.
   * The value is a raw JSON string need to remove extra '/' to run it.
   * Placeholder values such as ``Sample_name`` and ``Sample_order_number`` must be
     replaced with actual values before use.


Create Template API
====================================

To create a new SMS template, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/sms/templates/

with the following parameters:

    =========  ===============================================================  ========  =========================================
    Name       Description                                                      Required  Example
    =========  ===============================================================  ========  =========================================
    name       A human-readable label for the template                          Yes       Welcome SMS
    content    Message body with ``{variable}`` placeholders                    Yes       Hello {name}, welcome to Japan!
    =========  ===============================================================  ========  =========================================

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> -X POST \
      -H "Content-Type: application/json" \
      -d '{"name": "Welcome SMS", "content": "Hello {name}, welcome to Japan!"}' \
      https://api.xoxzo.com/sms/templates/

.. note::

   Notes on the **content** parameter:

   * Variables must be wrapped in curly braces, e.g. ``{name}``.
   * Variable names may only contain letters, numbers, and underscores.
   * Newly created templates start in ``PENDING`` status and must be approved before
     they can be used to send SMS.


Retrieve Single Template API
====================================

To retrieve a specific template, make a ``GET`` request to the endpoint followed by ``<template_id>``::

    https://api.xoxzo.com/sms/templates/<template_id>/

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/sms/templates/1/


Update Template API
====================================

To update an existing template, make a ``PATCH`` request to the endpoint followed by ``<template_id>``::

    https://api.xoxzo.com/sms/templates/<template_id>/

with the following parameters:

    =======  ==========================================================  ========
    Name     Description                                                 Required
    =======  ==========================================================  ========
    name     Updated template name                                       No      
    content  Updated message content. Triggers status reset to PENDING.  No      
    =======  ==========================================================  ========

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> -X PATCH \
      -H "Content-Type: application/json" \
      -d '{"content": "Hi {name}, updated message!"}' \
      https://api.xoxzo.com/sms/templates/1/

.. warning::

   Editing the ``content`` field will automatically demote an ``APPROVED`` template back
   to ``PENDING`` status. The previously approved content remains available in
   ``approved_content`` until the new version is approved.


Delete Template API
====================================

To delete a template, make a ``DELETE`` request to the endpoint followed by ``<template_id>``::

    https://api.xoxzo.com/sms/templates/<template_id>/

Examples
------------------------------------

Below is an example request using cURL::

    curl -u <SID>:<AUTH_TOKEN> -X DELETE https://api.xoxzo.com/sms/templates/1/

.. warning::

   Deleting a template is permanent and cannot be undone.