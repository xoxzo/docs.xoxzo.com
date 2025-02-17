============================================
Mail2SMS Usage
============================================

.. note::
   **Step to send SMS from email using Xoxzo in summary**:
    * Signup for Xoxzo X4
    * Go to Mail2SMS page and create a Mail2SMS user 
    * Please create a new message from your email address, enter the SMS recipient's number in the subject line, and send the email to mail2sms@xoxzo.com.
    * For example, if you want to send SMS from multiple email addresses, create the same number of Mail2SMS users and configure each email address accordingly. Once set up, send an email from each configured email address to mail2sms@xoxzo.com, with the SMS recipient's number in the subject line and the message in the email body.

Signup for Xoxzo
====================================
#. Go to `Signing up <https://www.xoxzo.com/en/accounts/signup/>`_ if you haven't already.
#. Fill out the signup form where a user need to enter email, fullname, password etc

Create Mail2SMS User
====================================
#. Login to Xoxzo and go to `Mail2SMS User <https://www.xoxzo.com/en/you/mailsmsprofile/>`_  page
#. Click on the `Add Mail2SMS <https://www.xoxzo.com/en/you/mailsmsuser/create/>`_ button

We will see the following parameters

    ======================  ===========================  ========  ===================  ===================
    Name                    Description                  Required  Data Type            Example
    ======================  ===========================  ========  ===================  ===================
    Mail2SMS User Email     Mail2SMS User Email           Yes       email                krishna@xoxzo.com
    Sender                  SMS Sender                    Yes       string               XoxzoAPI
    DKIM                    DKIM email security           Yes       string               PASS
    SPF                     SPF email security            Yes       string               GRAY
    DMARC                   DMARC email security          Yes       string               FAIL
    ======================  ===========================  ========  ===================  ===================

.. note::

   * **Mail2SMS User Email** should be valid and unique
   * **Sender** should be atleast 3 characters and should be less than 10 character
   * To learn more about `DKIM <https://help.xoxzo.com/xoxzo-cloud-telephony/sms-api/articles/how-to-send-via-mail2sms/#dkim>`_, `SPF <https://help.xoxzo.com/xoxzo-cloud-telephony/sms-api/articles/how-to-send-via-mail2sms/#spf>`_, `DMARC <https://help.xoxzo.com/xoxzo-cloud-telephony/sms-api/articles/how-to-send-via-mail2sms/#dmarc>`_, please visit the link.
   * If you don't know the security status please leave the value as Grey. 

Update Mail2SMS User
====================================
#. `Mail2SMS User <https://www.xoxzo.com/en/you/mailsmsprofile/>`_  page list all Mail2SMS user 
#. In this list we will see the Edit option, after clicking that we will go to specific Mail2SMS user edit page

We will see the following parameters

    ======================  ===========================  ========  ===================  ===================
    Name                    Description                  Required  Data Type            Example
    ======================  ===========================  ========  ===================  ===================
    Sender                  SMS Sender                    Yes       string               XoxzoAPI
    DKIM                    DKIM email security           Yes       string               PASS
    SPF                     SPF email security            Yes       string               GRAY
    DMARC                   DMARC email security          Yes       string               FAIL
    ======================  ===========================  ========  ===================  ===================

.. note::

   * **Mail2SMS User Email** can not be updated
   * Validation of other parameter is same as create Mail2SMS user


Delete Mail2SMS User
====================================
#. List of Mail2SMS user will be displayed in `Mail2SMS User <https://www.xoxzo.com/en/you/mailsmsprofile/>`_ page 
#. In this list, we will see the delete option, clicking on that will delete Mail2SMS User

.. note::
   **How delete Mail2SMS user works ?**

   * Delete only acts as a soft delete of Mail2SMS user
   * If the owner add the deleted Mail2SMS user we reactivate the Mail2SMS user
   * If the user try to add Mail2SMS user which is already exist under other user then the system will through the duplicate error as we are maintaining unique Mail2SMS user


Send Mail2SMS messages
====================================
* Go to email portal by logging in with the valid Mail2SMS user (like gmail, yahoo etc)
* Compose the email and send it to the recipient **mail2sms@xoxzo.com**.
* For example, If you want to send sms to +819876543210 then subject of email will be +819876543210.
* We allow only single recipient in subject

.. tip:: 
    Try adding Mail2SMS user and send sms using email.
    `Signing up <https://www.xoxzo.com/en/accounts/signup/>`_ takes only a few minutes and it's free