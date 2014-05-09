.. index:: Versioning

.. _versioning:

Versioning
==========

This document describes the allowed ways of changing an existing API.

Resource versioning
-------------------

Change the major version in the base URL only as a last resort
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before:

.. code-block:: http

    http://api.marktplaats.nl/v1/categories/96

After

.. code-block:: http

    http://api.marktplaats.nl/v2/categories/96

Changing the major version SHOULD be done as little as possible. The old URL SHOULD be available for some time to allow
all clients to update their code.

Clients should be able to cope with new link relations added to existing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clients should be liberal in what they accept and conservative in what they send. And they should not break when a new
link relation is added to an existing resource

Deprecate old links when replacing them with newer non backwards compatible versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case the link replaces an older link, the old link MUST be deprecated. The old link SHOULD stay around until all
clients got the change to update their code.

Before:

.. code-block:: javascript

    {
        "_links": {
            "self": { "href": "/" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs" },
            "http://api.marktplaats.nl/v1/docs/resources/categories": { "href": "/v1/categories" }
        }
    }

After:

.. code-block:: javascript

    {
        "_links": {
            "self": { "href": "/" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs" },
            "http://api.marktplaats.nl/v1/docs/resources/categories": {
              "href": "/v1/categories",
              "deprecation": "http://api.marktplaats.nl/v1/docs/resources/categories/deprecation"
            },
            "http://api.marktplaats.nl/v1/docs/resources/tags": { "href": "/v1/tags" }
        }
    }

The deprecation attribute value of the link relation MUST point to a developer document that describes when and why
the relation is deprecated.


Field versioning
----------------

Clients should be able to cope with new attributes added to existing resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clients should be liberal in what they accept and conservative in what they send. And they should not break when a new
attribute is added to an existing resource

In case the new field replaces another field, the old field SHOULD stay around until existing clients got a chance to
change their code. Before the the older field is removed it SHOULD be deprecated.

Deprecation example:

.. code-block:: javascript

    {
      "_links": {
         "self": { "href": "/v1/categories/92" },
         "describedby": { "href": "http://api.marktplaats.nl/v1/docs/categories" },
         "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
      },
      "name": "Alpha romeo",
      "short-name": "Alpha romeo",
      "shortName": "Alpha romeo",
      "_deprecation": {
        "short-name": "http://api.marktplaats.nl/v1/docs/resources/category/short-name-deprecation"
      }
    }
