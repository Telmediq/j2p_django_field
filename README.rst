================
J2P Django Field
================

Description
-----------

This package uses the Jasypt2Python library to decrypt Jasypt-encrypted data (A Java encryption library that includes
Bouncy Castle), and wraps this functionality into a django custom form.

This is a one-way calculation (includes the decryption functionality, but no encryption functionality).

Features
--------

Current supported fields:

* Encrypted TextField
* Encrypted CharField

Requirements
------------

* The requirements are listed in requirements.txt
* Generally, the requirement is the Jasypt2Python library (accessible via pip: pip install Jasypt2Python)