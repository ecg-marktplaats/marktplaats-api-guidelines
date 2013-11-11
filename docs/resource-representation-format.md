Resource representation format
==============================

Resources
---------

### Serialization format: hal+json;charset=UTF-8

Non binary resources should use the [HAL](http://stateless.co/hal_specification.html) JSON mediatype as the
serialization format and responses should be [UTF-8](http://en.wikipedia.org/wiki/UTF-8) encoded.

Example document :

    {
     "_links": {
        "self": { "href": "/categories/92" },
        "http://api.marktplaats.nl/v1/rels/parent_category": { "href": "/categories/91" }
     },
     "_embedded": {
        "http://api.marktplaats.nl/v1/rels/parent_category": {
             "_links": {
                "self": { "href": "/categories/91" }
             },
             "name": "Auto's",
             "shortName": "Auto's"
        }
     },
     "name": "Alpha romeo",
     "shortName": "Alpha romeo"
    }


### Each resource should contain a 'self' link

Each resource should have a self link :

Example :

    {
        "_links": {
            "self": { "href": "/categories/1" }
        }
    }

### When available IANA registered relation types should be used as link relations

A link relation is a descriptive attribute attached to a hyperlink in order to define the type of the link, or the
relationship between the source and destination resources.

A [standardized link relation](http://www.iana.org/assignments/link-relations/link-relations.xhtml) should be used when
such a relation is available.

Examples of commonly used IANA relation types are : `self`, `first`, `prev`, `next`, and `last`.


### Custom link relation types should be uri's that when dereferenced in a web browser provide relevant documentation, in the form of an HTML page

In accordance with the [web linking RFC](http://tools.ietf.org/html/rfc5988) custom link relation types should be uri's
that when dereferenced in a web browser provide relevant documentation, in the form of an HTML page.

This page should contain the following information

*   A list of request methods (GET, PUT, POST etc) supported for this URI and for each method
*   A description of the responses you can expect from any of the given request methods. This description should contain
    the status code and a description of the links and embedded resources included in the response

Field names
-----------

### Field names are in English unless they represent a product or company name.

The consumers of the API will almost certainly not all be Dutch so field names should be in English unless they
represent a product or company name.

### Field names have consistent semantics and representation

When two fields have the same name (even if they are in different entities), they must mean the same thing and they must
use the same representation.

This rule does not apply to deprecated fields.

### Field names are in camelCase, contain only latin characters `a` - `z`, `A` - `Z`, `0` - `9`.

Fields should only use alphanumeric characters and should use the camelCase notation.

    { "asqEnabled" : true }    // correct
    { "asq_enabled" : true }   // NOT correct
    { "asq_enabled?" : true }  // NOT correct

### Field names start with a lowercase letter, `a` - `z`.

Fields should start with a lower case letter.

### Field names starting with underscore '\_' are reserved for external standards, e.g. Hal.

While HAL only reserves the names detailed in the specification (`_links` and `_embedded`) properties that represent
the resource's state should not start with an underscore to prevent collisions with future versions of the standard.

### Field deprecation

TODO
See versioning.


Field values
------------

TODO: incorporate <https://developers.google.com/discovery/v1/type-format>.

### Structure field values

You are encouraged to represent complex fields with a JSON object. This allows for better composability, the struct
might later move to a separate entity.

TODO: discuss, this might make it harder for clients??

### Field values that represent a date or timestamp are in ISO 8601

Date values are represented using the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format full syntax in UTC (`Z`)
with milliseconds (e.g. `2013-20-02T18:02:24.000Z`).

Some systems will store dates in a lower precision. For consistency even those dates are represented in the full format.
However, clients should be prepared to see dates rounded, for example to the second or to the day.

### Field values that represent countries are in ISO 3166-1 alpha-2 format

Country codes are defined by the ISO 3166-1-alpha-2 code standard. You can find the complete list
[here](http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements). For example `NL`.

The codes are case sensitive.

### Field values that represent a currency are in ISO 4217

Currencies are encoded using the [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency format. For example `EUR`,
and not `€`.

The codes are case sensitive.

### All money types are integers and conform to its smallest currency unit

All money types are integers and conform to its smallest *commonly used* currency unit. For example, if the currency of
a payment is in euros (EUR), the values of money fields conform to euro cents. So an amount of EUR 9,95 is represented
as `995`.

See the currency exponent as defined by [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) to find the smallest commonly
used currency unit for a given currency.

### All numbers are integers unless precision is not important

Most numbers need to be precise, rounding due to using a floating point (64-bit IEEE754, or 32-bit IEEE754) can lead to
unexpected errors. There are two options:

* represent the number in some exponent (e.g. in cm instead of m), this is required with a monetary amount
  (see previous rule),
* represent the precise number as a string.

The first option is preferred. However, for larger numbers (JSON does not support number above 2^52), the second option
must be selected.

There are few exceptions to this rule. Here is the list of known and allowed exceptions:

* WGS84 coordinates

See also the list of supported field types: <https://developers.google.com/discovery/v1/type-format>.

TODO: copy the list from google to our own docs

### Binary field values

See also the list of supported field types: <https://developers.google.com/discovery/v1/type-format>.



Errors
------

### error messages follow a standard format

Error messages take the following form :

    {
        "_links": {
            "describes": { "href":  "http://...", "title": "Error description" }
        },
        "logref": 42,
        "errorCode" : "VALIDATION_FAILURE",
        "message": "Validation failed",
        "errors": [
            { "field": "email", "message": "Not a valid email address" },
            { "field": "password", "message": "Passwords should be at least 8 characters" }
        ]
    }


It is inspired by [vnd.error](https://github.com/blongden/vnd.error) format but adds the ability to add field-by-field messages

#### error document attributes

*logref* **(required)** : For expressing a (numeric/alpha/alphanumeric) identifier to refer to the specific error on the server side for logging purposes (e.g. RequestData.uniqueRequestId).

*message* **(required)** : For expressing a human readable message related to the current error which may be displayed to the user of the api.

*errorCode* **(required)** : an error code

*errors* **(optional)** : Field by field error messages

### an appropriate status code should be used when serving an error resource

When serving an error resource an appropriate status code should be used. E.g. 4xx for client errors and 5xx for processing errors
To determine which error code is appropriate, refer to the status codes section of this document

### Do not include stacktraces in the error message

It may be tempting to include a stack trace for easier support when something goes wrong. Don't do it! This kind of information is too valuable for hackers and should be avoided.

