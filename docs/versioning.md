Versioning
==========

Options for versioning:

* Major version number in base URL

  `http://api.marktplaats.nl/1/categories/96`

* New resource name, deprecate old version

  before: `http://api.marktplaats.nl/1/attributes/96`
  after: 
    `http://api.marktplaats.nl/1/attributes/96`, relation deprecated (see HAL spec)
    `http://api.marktplaats.nl/1/ad_attributes/96`


Alternatives, DO NOT USE
------------------------

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
