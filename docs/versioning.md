Versioning
==========

This document describes the allowed ways of changing an existing API.

Resource versioning
-------------------

### Change the major version in the base URL:

Before:

    http://api.marktplaats.nl/v1/categories/96

After

    http://api.marktplaats.nl/v2/categories/96

Changing the major version SHOULD be done as less as possible. The old URL SHOULD be available for some time to allow
all clients to update their code.

### Add another resource

It is always possible to add another link to an existing resource.

In case the link replaces an older link, the old link MUST be deprecated. The old link SHOULD stay around until all
clients got the change to update their code.

Before:

    {
        "_links": {
            "self": { "href": "/" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs" },
            "http://api.marktplaats.nl/v1/docs/resources/categories": { "href": "/v1/categories" }
        }
    }

After:

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

The deprecation URL MUST point to a developer document that describes when and why the relation is deprecated.


Field versioning
----------------

### Add another field

It is always allowed to add more fields to an existing resource.

In case the new field replaces another field, the old field SHOULD stay around until existing clients got a chance to
change their code. Before the the older field is removed it SHOULD be deprecated.

Deprecation example:

    {
      "_links": {
         "self": { "href": "/v1/categories/92" },
         "describedby": { "href": "http://api.marktplaats.nl/v1/docs/categories" },
         "http://api.marktplaats.nl/v1/docs/rels/parent_category": { "href": "/v1/categories/91" }
      },
      "name": "Alpha romeo",
      "short-name": "Alpha romeo",
      "shortName": "Alpha romeo",
      "_deprecation": {
        "short-name": "http://api.marktplaats.nl/v1/docs/resources/category/short-name-deprecation"
      }
    }

Alternative ways of versioning, DO NOT USE
------------------------------------------

* Major/minor version number in base URL

  `http://api.marktplaats.nl/1.1/categories/96`

* Version in entity url
  http://api.marktplaats.nl/categories/96
  http://api.marktplaats.nl/categories.2/96
  http://userapi.marktplaats.nl/users/1234
  http://casapi.marktplaats.nl/ads.2/
  http://casapi.marktplaats.nl/v2/ads/

* Version in HTTP header `Accept`

  request: `Accept: application/hal+json`
  response: `Content-Type: application/hal+json;content_version=1`

  request: `Accept: application/hal+json;content_version=2`
  response: `Content-Type: application/hal+json;content_version=2`

  Optionally values comes from URL parameter.
  `http://base.url/entity?params&content_version=2`
