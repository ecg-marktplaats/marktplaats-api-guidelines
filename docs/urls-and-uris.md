URLs and URIs
=============

Base URL
--------

Examples of good base URLs:

    https://api.marktplaats.nl/v1
    https://api.marktplaats.nl/subsystem/v1

Not so good example:

    https://www.marktplaats.nl/api/subsystem/services/v1.2


### Base URL should be short

The base URL should be short and easy to remember. The longer the domain name and path, the harder it is to use.

### Use https

Https must be used. This solves a great deal of otherwise hard to tackle security problems.

### Base URL includes a major version in path

The version in the URL is the escape route to introduce breaking changes to the API. This should not be taken lightly
and therefore a single digit should be enough for a long time. For clarity, the version MUST be preceded by a `v`.

### The base URL is a HAL resource

The base URL is a HAL resource with appropriate documentation links. It has content type  `application/hal+json`.
However, to not confuse browsers, we serve the document with content type `application/json`.

The resource MUST be encoded with UTF-8.

For example:

    GET /v1 HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json
    ETag: "d9087df677dgh"

    {
        "_links": {
            "self": { "href": "/" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs" },
            "http://api.marktplaats.nl/v1/docs/resources/categories": { "href": "/v1/categories" },
            "http://api.marktplaats.nl/v1/docs/resources/advertisements": { "href": "/v1/advertisements" },
            "http://api.marktplaats.nl/v1/docs/resources/users": { "href": "/v1/users" }
        }
    }

URL and URI naming
------------------

### Document names should be a singular noun

A URI representing a document resource should be named with a singular noun or noun phrase path segment.
For example, the URI for a single seller profile document would have the singular form:

    https://api.marktplaats.nl/v1/users/1/profile


### Collection names should be a plural noun

A URI identifying a store of resources should be named with a plural noun, or noun phrase, as its path segment. 
The URI for a store of categories may use the plural noun form as follows:

    https://api.marktplaats.nl/v1/categories


### Forward slash separator (`/`) must be used to indicate a hierarchical relationship

The forward slash (`/`) character is used in the path portion of the URI to indicate a hierarchical relationship between
resources. For example:

    https://api.marktplaats.nl/v1/categories/91/advertisements


### URIs should not have a trailing forward slash (`/`)

As the last character within a URI’s path, a forward slash (`/`) adds no semantic value and may cause confusion.
REST APIs should not expect a trailing slash and should not include them in the links that they provide to clients.

Many web components and frameworks will treat the following two URIs equally:

    https://api.marktplaats.nl/v1/categories/
    https://api.marktplaats.nl/v1/categories

However, every character within a URI counts toward a resource’s unique identity.
Two different URIs must map to two different resources.
If the URIs differ, then so do the re- sources, and vice versa.
Therefore, a REST API must generate and communicate clean URIs and should be intolerant of any client’s attempts to
identify a resource imprecisely.
Redirects (e.g. 301 Moved Permanently) from one version to the other are not allowed. Some clients don't support
redirects and we need to keep this consistent over our separate APIs.

The root resource `/` is excluded from this rule.

### Hyphens (`-`) should be used to improve the readability of URIs ,not underscores (`_`)

To make your URIs easy for people to scan and interpret, use the hyphen (`-`) character to improve the readability of
names in long path segments.
Anywhere you would use a space or hyphen in English, you should use a hyphen in a URI. For example:

    https://api.marktplaats.nl/v1/this-is-an-endpoint-with-a-large-name


### URI paths must use lowercase letters

Lowercase letters are preferred in URI paths since capital letters can sometimes cause problems.
RFC 3986 defines URIs as case-sensitive except for the scheme and host components. 
For example:

    http://api.example.restapi.org/my-folder/my-doc
    HTTP://API.EXAMPLE.RESTAPI.ORG/my-folder/my-doc
    http://api.example.restapi.org/My-Folder/my-doc

The first URL is fine and RFC3986 considers the second url to be identical to URL #1. But the third URL is not the same
as URIs one and two, which may give unnecessary confusion.

Parameters inside the URI path are excluded from this rule.

Query parameters
----------------

### The query component of a URI should be used to filter collections or stores

A URI’s query component is a natural fit for supplying search criteria to a collection or store.

Example :

    GET /v1/users?casUser=true HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json
    {
        "_links": {
            "self": { "href": "/users" },
        },
        "_embedded": {
            "http://api.marktplaats.nl/v1/rels/user": [{
               "_links": {
                 "self": { "href": "/users/2" },
               },
               "name": "Richard",
               "email": "2@marktplaats.nl",
               "casUser" : true
            }]
        },
        "totalResults": 10
    }

### The query component of a URI should be used to paginate collections or store results

A REST API client should use the query component to paginate collections and store results with the `offset` and `limit` parameters.

The `limit` parameter specifies the maximum number of contained elements to return in the response.
The `offset` parameter specifies the zero-based index of the first element to return in the response.

Example :

    GET /v1/users?offset=0&limit=2 HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_links": {
            "self": { "href": "/users" },
            "next": { "href": "/users?offset=1&limit=2" },
            "find": { "href": "/users{?id}", "templated": true }
        },
        "_embedded": {
            "http://api.marktplaats.nl/v1/rels/user": [{
               "_links": {
                 "self": { "href": "/users/1" },
               },
               "sellername": "Robin",
               "email": "1@marktplaats.nl",
               "casUser" : false
             },{
               "_links": {
                 "self": { "href": "/users/2" },
               },
               "name": "Richard",
               "email": "2@marktplaats.nl",
               "casUser" : true
            }]
        },
        "totalResults": 10
    }


### <a name="_body"></a> Use the `_body` parameter to include/exclude a response body

By default responses contain a body, even if it is mostly the same as what was posted. The `_body` parameter can be
used to change this behavior.

Parameter `_body` takes values `true` (the default) or `false`.

Example:

    POST http://api.marktplaats.nl/v1/categories?_body=false HTTP/1.1
    Host: api.marktplaats.nl

    {
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }


    HTTP/1.1 201 Created
    Location: http://api.marktplaats.nl/v1/categories/95

### <a name="_method"></a> Use `POST` with a `_method` url parameter to mimic other request methods

Some clients do not support all methods (e.g. `DELETE` or `PATCH` is not supported from Javascript in the browser), the
`_method` url parameter can be used to mimic any request method.
Instead of the `_method` parameter, we also should support setting the method using the request header `X-HTTP-METHOD-OVERRIDE` (optionally other headers, like `X-HTTP-METHOD` and `X-METHOD-OVERRIDE` may also be supported).

Example:

    POST /v1/categories/95?_method=PATCH HTTP/1.1
    Host: api.marktplaats.nl
    Content-Type: application/json-patch+json
    If-Match: "abc123"

    [
        { "op": "replace", "path": "/name", "value": "BMW" },
        { "op": "replace", "path": "/hostName", "value": "BMW" }
    ]

is interpreted as a `PATCH` request.

### <a name="_callback"></a> Use the `_callback` parameter to return a jsonp response

You can send a `?_callback` parameter to any `GET` call to have the results wrapped in a JSON function.
This is typically used when browsers want to embed marktplaats content in web pages by getting around cross domain
issues. The response includes the same data output as the regular API, plus the relevant HTTP Header information.

The content type of the response MUST be `application/javascript`.

Example:

    GET /v1/users?_callback=foo HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/javascript
    foo({
        "_links": {
            "self": { "href": "/users" },
        },
        "_embedded": {
            "http://api.marktplaats.nl/v1/rels/user": [{
               "_links": {
                 "self": { "href": "/users/2" },
               },
               "name": "Richard",
               "email": "2@marktplaats.nl",
               "casUser" : true
            }]
        },
        "totalResults": 10
    })

### <a name="_expand"></a> Use the `_expand` parameter for zooming

Zooming is an optional technique that allows linked resources to be embedded. The embedded resources are serializes as
described by [HAL](http://stateless.co/hal_specification.html).

Example :

    GET /v1/categories/92?_expand=parent-category HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json
    ETag: "7dsyiuh44aa"

    {
        "_links": {
            "self": { "href": "/v1/categories/92" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
        },
        "_embedded": {
            "http://api.marktplaats.nl/v1/rels/parent-category": [{
               "_links": {
                 "self": { "href": "/v1/categories/91" },
               },
               "id": 91,
               "name": "Auto's, motors en andere voertuigen",
               "shortName": "Auto's"
            }]
        },
        "id": 92,
        "parentCategoryId": 91,
        "name": "Alpha romeo",
        "shortName": "Alpha romeo"
    }

TODO: look into <http://www.etsy.com/developers/documentation/getting_started/resources> to allow pagination


### <a name="_include_exclude"></a> Use the `_include` and `_exclude` parameters for selecting fields

The `_include` and `_exclude` parameters can be used to select fields. If both parameters are present, only the
`_include` parameter is used.

Both fields have a similar format. A list of comma separated field names are valid arguments for both `_include` and `_exclude`. 

TODO: look into <http://www.etsy.com/developers/documentation/getting_started/resources> to allow pagination

Example :

    TODO

### <a name="_prettyprint"></a> Use the `_prettyprint` parameter to return a pretty printed response

Implementation CAN support the `?_prettyprint` parameter to make it easier for people to view, read and understand
resources. Formatting is enabled when the parameter is present and does not have the value `false`.

Consider enabling pretty printing by default for documentation resources only (e.g. the `/` resource).

Example :

    GET /v1/categories/95?_prettyprint HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_links": {
            "self": { "href": "/v1/categories/95" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent_category": { "href": "/v1/categories/91" }
        },
        "id": 95,
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }
