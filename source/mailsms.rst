.. note::
**Step to send SMS from email using Xoxzo**:
* Signup for Xoxzo X4
* Go to mailsms page and create a MailSMS user 
* Login to the mail site (yahoo/gmail ) using user@gmail.com or user@yahoo.com and 
send message to the number like 9840753098@mailsms.xoxzo.com::
* For example if I am a user of Xoxzo , I want to send messages from my two email addresses 
user@gmail.com and user@yahoo.com then I will create two pokhara users with the email 
user@gmail.com and user@yahoo.com and send sms to number


Add  MailSMS User API
====================================
To add a MailSMS user, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/bo/users/<username>/mailsms/


add_mailsms_user ={'sender': 'kkk',
                'email':'krihnak@xoxzo.com',
                'dkim':'PASS',
                'spf':'PASS',
                'dmarc':'PASS'}
with the following parameters:

    ===============  ===========================  ========  ===================  ===================
    Name             Description                  Required  Data Type            Example
    ===============  ===========================  ========  ===================  ===================
    email            MailSMS User email           Yes       email                krishna@xoxzo.com
    sender           sender info                  Yes       string               XoxzoAPI
    dkim             DKIM email security          Yes       string               PASS
    spf              spf email security           Yes       string               GRAY
    dmarc            dmarc email security         Yes       string               FAIL
    ===============  ===========================  ========  ===================  ===================


.. note::
   Notes on the **Process to add MailSMS  User**:

   * The email should be unique
   * Sender information should be added
   * The security like DKIM,DMARC,SPF should be added

The response would be a JSON structure, returned with HTTP ``201 CREATED`` status code::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
    'message': 'MailSMS User Added successfully'
    }
::
Get  MailSMS User API
====================================
To fetch a MailSMS user, make a ``GET`` request to the endpoint::

    https://api.xoxzo.com/bo/users/<username>/mailsms/


.. note::
   Notes on the **To fetch MailSMS  User**:

   * The endpoint will list all the MailSMS User under a particular user
   * If there is a need to fetch the particular mailsms user we can request the 
   endpoint https://api.xoxzo.com/bo/users/<username>/mailsms/1/

The response would be a list of JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    [{
    'id': 42,
    'email': 'krishna5@xoxzo.com',
    'sender': 'kkk',
    'dkim': 'PASS', 
    'spf': 'PASS', 
    'dmarc': 'PASS',
    'revoked': False, 
    'updated_on': '2023-06-23T07:59:10.172264'
    }, 
    ]
::
Update  MailSMS User API
====================================
To update a MailSMS user, make a ``PUT`` request to the endpoint::

    https://api.xoxzo.com/bo/users/<username>/mailsms/


update_mailsms_user ={'sender': 'kkk',
                'dkim':'PASS',
                'spf':'PASS',
                'dmarc':'PASS'}
with the following parameters:

    ===============  ===========================  ========  ===================  ===================
    Name             Description                  Required  Data Type            Example
    ===============  ===========================  ========  ===================  ===================
    sender           sender info                  Yes       string               XoxzoAPI
    dkim             DKIM email security          Yes       string               PASS
    spf              spf email security           Yes       string               GRAY
    dmarc            dmarc email security         Yes       string               FAIL
    ===============  ===========================  ========  ===================  ===================


.. note::
   Notes on the **Process to update MailSMS  User**:

   * The email field is not needed for the updates

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
    'message': 'MailSMS User Updated successfully'
    }

::
Delete  MailSMS User API
====================================
To delete a MailSMS user, make a ``DELETE`` request to the endpoint::

    https://api.xoxzo.com/bo/users/<username>/mailsms/


.. note::
   Notes on the **Process to delete MailSMS  User**:

   * Delete only acts as a soft delete so when user delete mailsms user
   * When user delete mailsms user we set revoked as true and skip those mailsms user whose revoked status is true
   * If the owner of the mailsms user whose status is revoked try to add mailsms same user 
   we reactivate the mailsms user by setting the revoked status as false
   * If the user try to add mailsms user which is already exist under other user then the system
   will through the Duplicate error as we are maintaining unique mailsms user 

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
    'message': 'MailSMS User deleted successfully'
    }


.. note::
   Notes on the **MailSMS User crud process**:

   * Normal user cannot access these pages
   * Permission and authorization for the mailsms user crud operation is only allowed from BO admin

::
====================================
MailSMS API
====================================

The MailSMS API allows you to send SMS to from email server to the phone number.

Send  MailSMS messages API
====================================
To send a SMS message, make a ``POST`` request to the endpoint::

    https://api.xoxzo.com/mailsms/send-email-sms/

with the following parameters:

    ===============  ===========================  ========  ===================  ===================
    Name             Description                  Required  Data Type            Example
    ===============  ===========================  ========  ===================  ===================
    from_email       MailSMS User email           Yes       email                krishna@xoxzo.Common
    to_number        recipient phone number       Yes       string               +8190123456789
    mail_message     Message body                 Yes       string               This is a test
    dkim             DKIM email security          Yes       string               PASS
    spf              spf email security           Yes       string               GRAY
    dmarc            dmarc email security         Yes       string               FAIL
    ===============  ===========================  ========  ===================  ===================


.. note::
   Notes on the **MailSMS Sending Process**:

   * The from_email is the registered mailsms user in Xoxzo
   * The number should be valid phone number
   * The security like DKIM,DMARC,SPF should be present in the payload.

The response would be a JSON structure, returned with HTTP ``200 OK`` status code::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
    'message': 'Started a process to send sms',
    'mailsmsid': 45
    }

.. note::
   Notes on the **mailsmsid**:

   * It is the id of the mailsmssentmessage table
   * We can do the inquiry of the message status using this id
