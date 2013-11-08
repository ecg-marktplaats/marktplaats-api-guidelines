Resource representation format
==============================

### Serialization format: hal+json;charset=UTF-8

Non binary resources should use the [HAL](http://stateless.co/hal_specification.html) JSON mediatype as the
serialization format and responses should be [UTF-8](http://en.wikipedia.org/wiki/UTF-8) encoded.

Example HAL representation:

```json
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
```

### Each resource should contain a 'self' link

Each resource should have a self link :

Example :

```json
{
    "_links": {
        "self": { "href": "/categories/1" }
    }
}
```

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



Error handling
--------------

### error messages follow a standard format

Error messages take the following form :

```json
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
```

It is inspired by [vnd.error](https://github.com/blongden/vnd.error) format but adds the ability to add field-by-field messages

#### error document attributes

logref (required) : For expressing a (numeric/alpha/alphanumeric) identifier to refer to the specific error on the server side for logging purposes (e.g. RequestData.uniqueRequestId).
message (required) : For expressing a human readable message related to the current error which may be displayed to the user of the api.
errorCode (required) : an error code
errors (optional) : Field by field error messages


Status codes
------------


### 200 (“OK”) should be used to indicate nonspecific success

In most cases, 200 is the code the client hopes to see. It indicates that the REST API successfully carried out 
whatever action the client requested,  and that no more specific code in the 2xx series is appropriate. 
Unlike the 204 status code, a 200 response should include a response body.

### 201 (“Created”) must be used to indicate successful resource creation

A REST API responds with the 201 status code whenever a collection creates, or a store adds, a new resource at the client’s request. 

### 202 (“Accepted”) must be used to indicate successful start of anasynchronous action

A 202 response indicates that the client’s request will be handled asynchronously. This response status code tells the client that the 
request appears valid, but it still may have problems once it’s finally processed.  A 202 response is typically used for actions that 
take a long while to process.

### Rule: 204 (“No Content”) should be used when the response body is intentionally empty

The 204 status code is usually sent out in response to a PUT, POST, or DELETE request, 
when the REST API declines to send back any status message or representation in the response message’s body. 
An API may also send 204 in conjunction with a GET request to indicate that the requested resource exists, 
but has no state representation to include in the body.

### 301 (“Moved Permanently”) should be used to relocate resources

The 301 status code indicates that the REST API’s resource model has been significantly redesigned and 
a new permanent URI has been assigned to the client’s requested re- source. 
The REST API should specify the new URI in the response’s Location header.

### 302 (“Found”) should not be used

The intended semantics of the 302 response code have been misunderstood by programmers and incorrectly 
implemented in programs since version 1.0 of the HTTP protocol. The confusion centers on whether it is 
appropriate for a client to always automatically issue a follow-up GET request to the URI in response’s Location header, 
regardless of the original request’s method. For the record, the intent of 302 is that this automatic redirect behavior 
only applies if the client’s original request used either the GET or HEAD method.
To clear things up, HTTP 1.1 introduced status codes 303 (“See Other”) and 307 (“Temporary Redirect”), either of which should be used instead of 302.


### 303 (“See Other”) should be used to refer the client to a different URI

A 303 response indicates that a controller resource has finished its work, but instead of sending a potentially unwanted response body, 
it sends the client the URI of a response resource. This can be the URI of a temporary status message, or the URI to some already existing, more permanent, resource.
Generally speaking, the 303 status code allows a REST API to send a reference to a resource without forcing the client to download its state. Instead, the client may send a GET request to the value of the Location header.


### 400 (“Bad Request”) may be used to indicate nonspecific failure

400 is the generic client-side error status, used when no other 4xx error code is appropriate.


### 401 (“Unauthorized”) must be used when there is a problem with the client’s credentials

A 401 error response indicates that the client tried to operate on a protected resource without providing the proper authorization. 
It may have provided the wrong credentials or none at all.

### 403 (“Forbidden”) should be used to forbid access regardless of authorization state

A 403 error response indicates that the client’s request is formed correctly, but the REST API refuses to honor it. 
A 403 response is not a case of insufficient client credentials; that would be 401 (“Unauthorized”).
REST APIs use 403 to enforce application-level permissions. 
For example, a client may be authorized to interact with some, but not all of a REST API’s resources. 
If the client attempts a resource interaction that is outside of its permitted scope, the REST API should respond with 403.

### 404 (“Not Found”) must be used when a client’s URI cannot be mapped to a resource

The 404 error status code indicates that the REST API can’t map the client’s URI to a resource.

### 405 (“Method Not Allowed”) must be used when the HTTP method is not supported

The API responds with a 405 error to indicate that the client tried to use an HTTP method that the resource does not allow. 
For instance, a read-only resource could support only GET and HEAD, while a controller resource might allow GET and POST, 
but not PUT or DELETE.
A 405 response must include the Allow header, which lists the HTTP methods that the resource supports. For example:

Allow: GET, POST

### 409 (“Conflict”) should be used to indicate a violation of resource state

The 409 error response tells the client that they tried to put the REST API’s resources into an impossible or inconsistent state. 
For example, a REST API may return this response code when a client tries to delete a non-empty store resource.

### 412 (“Precondition Failed”) should be used to support conditional operations

The 412 error response indicates that the client specified one or more preconditions in its request headers,
effectively telling the REST API to carry out its request only if certain conditions were met.
A 412 response indicates that those conditions were not met, so instead of carrying out the request, the API sends this status code.

### 500 (“Internal Server Error”) should be used to indicate API malfunction

500 is the generic REST API error response. Most web frameworks automatically respond with this response status code whenever they execute some request handler code that raises an exception.
A 500 error is never the client’s fault and therefore it is reasonable for the client to retry the exact same request that triggered this response, and hope to get a different response.
