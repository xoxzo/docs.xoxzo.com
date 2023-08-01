============================================
Mail2SMS Usage
============================================

.. note::
   **Step to send SMS from email using Xoxzo in summary**:
    * Signup for Xoxzo X4
    * Go to Mail2SMS page and create a Mail2SMS user 
    * Login to the mail site (yahoo/gmail ) using user@gmail.com or user@yahoo.com and send message to the number like +819841753098@mail2sms.xoxzo.com
    * For example if I am a user of Xoxzo , I want to send messages from my two email addresses user@gmail.com and user@yahoo.com then I will create two Mail2SMS users with the email user@gmail.com and user@yahoo.com and send sms to number

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
   * **DKIM**, **SPF**, **DMARC** should match with Mail2SMS user email security
   * To know the DKIM, SPF and DKIM security status. Please send email to **verdict@acrt-mail.jp** using Mail2SMS email address

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

   * **Mail2SMS User Email** is not present as email of Mail2SMS user can not be updated
   * Validation of other parameter is same to create Mail2SMS user


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
* Compose the email and send it the recipient like <phone-number>@mail2sms.xoxzo.com
* For example, If I want to send sms to +819876543210 then recipient will be +819876543210@mail2sms.xoxzo.com

.. tip:: 
    Try adding Mail2SMS user and send sms using email.
    `Signing up <https://www.xoxzo.com/en/accounts/signup/>`_ takes only a few minutes and it's free