.. index:: HAL and our deviations

.. _hal-and-our-deviations:

HAL and our deviations
======================

For more information see `HAL homepage <http://stateless.co/hal_specification.html>`_ and `HAL RFC draft <http://tools.ietf.org/html/draft-kelly-json-hal-06>`_.

Content-type
------------

The proper content type for HAL documents is ``application/hal+json``. However, to not confuse browsers, our APIs MUST serve the document with content type ``application/json``.

JSON
----

HAL allows any valid JSON. We apply the following restrictions:

* `UTF-8 <http://en.wikipedia.org/wiki/UTF-8>`_ character encoding is REQUIRED.
* JSON object MUST NOT have multiple fields with the same name.
