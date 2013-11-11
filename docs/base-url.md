URLs and URIs
=============

Base URL
--------

Examples of good base URLs:

    https://api.marktplaats.nl/1
    https://api.marktplaats.nl/subsystem/1

Not so good example:

    https://www.marktplaats.nl/api/subsystem/services/v1.2


### Base URL should be short

The base URL should be short and easy to remember. The longer the domain name and path, the harder it is to use.

### Use https

Https must be used. This solves a great deal of otherwise hard to tackle security problems.

### Base URL includes a major version in path

The version in the URL is the escape route to introduce breaking changes to the API. This should not be taken lightly
and therefore a single digit should be enough for a long time. There is no need to prepend a `v` therefore (for
consistency) this is not allowed.


URL and URI naming
------------------

### Document names should be a singular noun

A URI representing a document resource should be named with a singular noun or noun phrase path segment.
For example, the URI for a single seller profile document would have the singular form:

    https://api.martkplaats.nl/v1/users/1/profile


### Collections names should be a plural noun

A URI identifying a store of resources should be named with a plural noun, or noun phrase, as its path segment. 
The URI for a store of categories may use the plural noun form as follows:

    https://api.martkplaats.nl/v1/categories


### Forward slash separator (`/`) must be used to indicate a hierarchical relationship

The forward slash (`/`) character is used in the path portion of the URI to indicate a hierarchical relationship between
resources. For example:

    https://api.martkplaats.nl/v1/categories/91/advertisements


### URIs should not have a trailing forward slash (`/`)

As the last character within a URI’s path, a forward slash (`/`) adds no semantic value and may cause confusion.
REST APIs should not expect a trailing slash and should not include them in the links that they provide to clients.

Many web components and frameworks will treat the following two URIs equally:

    https://api.martkplaats.nl/v1/categories/
    https://api.martkplaats.nl/v1/categories

However, every character within a URI counts toward a resource’s unique identity.
Two different URIs must map to two different resources.
If the URIs differ, then so do the re- sources, and vice versa.
Therefore, a REST API must generate and communicate clean URIs and should be intolerant of any client’s attempts to
identify a resource imprecisely.
Redirects (e.g. 301 Moved Permanently) from one version to the other are not allowed. Some clients don't support
redirects and we need to keep this consistent over our separate APIs.

### Hyphens (`-`) should be used to improve the readability of URIs ,not underscores (`_`)

To make your URIs easy for people to scan and interpret, use the hyphen (`-`) character to improve the readability of
names in long path segments.
Anywhere you would use a space or hyphen in English, you should use a hyphen in a URI. For example:

    https://api.martkplaats.nl/v1/this-is-an-endpoint-with-a-large-name


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

### The query component of a URI should be used to filter collections or stores

A URI’s query component is a natural fit for supplying search criteria to a collection or store.

Example :

    GET http://api.marktplaats.nl/v1/users?casUser=true
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/hal+json
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

### The query component of a URI should be used to paginate collection or store results

A REST API client should use the query component to paginate collection and store results with the pageSize and pageStartIndex parameters.

The pageSize parameter specifies the maximum number of contained elements to return in the response.
The pageStartIndex parameter specifies the zero-based index of the first element to return in the response.

Example :

    GET http://api.marktplaats.nl/v1/users?pageSize=2&pageStartIndex=0
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/hal+json

    {
        "_links": {
            "self": { "href": "/users" },
            "next": { "href": "/users?pageSize=2&page1" },
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


### <a name="_body"></a> Use `_body` parameter to include/exclude a response body

By default responses contain a body, even if it is mostly the same as what was posted. The `_body` parameter can be
used to change this behavior.

Parameter `_body` takes values `true` (the default) or `false`.

Example:

    POST http://api.marktplaats.nl/v1/categories?_body=false
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

Example:

    POST http://api.marktplaats.nl/v1/categories/95?_method=PATCH HTTP/1.1
    Host: api.marktplaats.nl
    Content-Type: application/json-patch+json
    If-Match: "abc123"

    [
        { "op": "replace", "path": "/name", "value": "BMW" },
        { "op": "replace", "path": "/hostName", "value": "BMW" }
    ]

is interpreted as a `PATCH` request.
