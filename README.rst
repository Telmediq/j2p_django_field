================
J2P Django Field
================


Description
-----------

This package uses the Jasypt2Python library to decrypt Jasypt-encrypted data (A Java encryption library that includes
Bouncy Castle), and wraps this functionality into a django custom form.

This is a one-way calculation (includes the decryption functionality, but no encryption functionality).


Installation
------------

The following code will clone the "J2P Django Field" project and install the requirements.

.. code-block:: shell

    git clone https://github.com/TelmedIQ/j2p_django_field.git
    cd j2p_django_field
    pip install -r requirements.txt

Features
--------

Current supported fields:

* Encrypted TextField
* Encrypted CharField


Requirements
------------

* The requirements are listed in requirements.txt
* Generally, the requirement is the Jasypt2Python library (https://github.com/TelmedIQ/jasypt-2-python)