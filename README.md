api-guidelines
==============

Guidelines for externally visible APIs.

TODO:
    * rate limiting
    * security




* [Introduction](docs/intro.md)
    * Principles
* [URLs and URIs](docs/urls-and-uris.md)
    * Base URL
        * https.
        * Short.
        * Includes major version (single digit) in path.
        * The base URL is a HAL resource.
    * URL and URI naming
        * Document names should be a singular noun.
        * Collection names should be a plural noun.
        * Forward slash separator (`/`) must be used to indicate a hierarchical relationship.
        * URIs should not have a trailing forward slash (`/`).
        * Hyphens (`-`) should be used to improve the readability of URIs, not underscores (`_`).
        * URI paths must use lowercase letters
    * Query parameters
        * The query component of a URI may be used to filter collections or stores
        * The query component of a URI should be used to paginate collections or store results
        * Use the _body parameter to include/exclude a response body
        * Use POST with a _method url parameter to mimic other request methods
        * Use the _callback parameter to return a jsonp response

* [Resource representation format](docs/resource-representation-format.md)
    * Resources
        * Serialization format: hal+json;charset=UTF-8
        * Each resource should contain a 'self' link
        * Each resource should contain a 'describedby' link
        * Keep collections homogeneous
        * When available IANA registered relation types should be used as link relations
        * Custom link relation types should be uri's that when dereferenced in a web browser provide relevant documentation, in the form of an HTML page
        * Field names are in English unless they represent a product or company name.
        * Field names have consistent semantics and representation
        * Field names are in camelCase, contain only latin characters `a` - `z`, `A` - `Z`, `0` - `9`.
        * Field names start with a lowercase letter, `a` - `z`.
        * Field names starting with underscore '\_' are reserved for external standards, e.g. Hal.
        * Field deprecation
    * Field values
        * Structure field values
        * Field values that represent a timestamp are in ISO 8601
        * Field values that represent a date are in ISO 8601
        * Field values that represent countries are in ISO 3166-1 alpha-2 format
        * Field values that represent a currency are in ISO 4217
        * All money types are integers and conform to its smallest currency unit
        * All numbers are integers unless precision is not important
        * Binary field values
     * Errors
        * Error messages follow a standard format
        * An appropriate status code should be used when serving an error resource
        * Do not include stacktraces in the error message

* [Interaction design](docs/interaction-design.md)
    * Request methods
        * GET must be used to retrieve a representation of a resource
        * POST must be used to create a new resource in a collection
        * PUT must be used to completely update a resource
        * PATCH must be used to partially update a resource
        * DELETE must be used to remove a resource from its parent

    * Response status codes
        * 200 (“OK”) should be used to indicate nonspecific success
        * 201 (“Created”) must be used to indicate successful resource creation
        * 202 (“Accepted”) must be used to indicate successful start of anasynchronous action
        * 204 (“No Content”) should be used when the response body is intentionally empty
        * 301 (“Moved Permanently”) should be used to relocate resources
        * 302 (“Found”) should not be used
        * 303 (“See Other”) should be used to refer the client to a different URI
        * 400 (“Bad Request”) may be used to indicate nonspecific failure
        * 401 (“Unauthorized”) must be used when there is a problem with the client’s credentials
        * 403 (“Forbidden”) should be used to forbid access regardless of authorization state
        * 404 (“Not Found”) must be used when a client’s URI cannot be mapped to a resource
        * 405 (“Method Not Allowed”) must be used when the HTTP method is not supported
        * 409 (“Conflict”) should be used to indicate a violation of resource state
        * 412 (“Precondition Failed”) should be used to support conditional operations
        * 500 (“Internal Server Error”) should be used to indicate API malfunction

* [Documentation](docs/documentation-requirements.md)
    * Document link relations
    * Getting started guide
    * API reference
    * Example code

* [Security](docs/security.md)
    * OAUTH 2 with bearer tokens for actions that should be performed on behalf of a user
    * Ip filtering for systems to systems communication that does not require
`
* [Versioning](docs/versioning.md)
    * Resource versioning
        * Change the major version in the base URL only as a last resort
        * Clients should be able to cope with new link relations added to existing resources
        * Deprecate old links when replacing them with newer non backwards compatible versions
    * Field versioning
        * Clients should be able to cope with new attributes added to existing resources

Changelog
=========

* 1-4-2014 - Added some remarks on optional fields in 'resource-representation'
* 31-3-2014 - Added section on security
