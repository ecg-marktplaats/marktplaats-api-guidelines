Interaction design
==================

Request methods
---------------

Resources can support one or more of the following methods.

### GET must be used to retrieve a representation of a resource

A REST API client uses the GET method in a request message to retrieve the state of a resource, in some representational
form.
A client’s GET request message may contain headers but no body.

Example :

    GET /v1/categories/92 HTTP/1.1
    Host: api.marktplaats.nl

    HTTP/1.1 200 OK
    Content-Type: application/json
    ETag: "9asoaljnssyd"

    {
        "_links": {
            "self": { "href": "/v1/categories/92" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
        },
        "id": 92,
        "parentCategoryId": 91,
        "name": "Alpha romeo",
        "shortName": "Alpha romeo"
    }

### Resources with `ETag` support

The `ETag` header MUST be sent in response to `GET` requests for resources with ETag support.

The value of `ETag` is an opaque string that identifies a specific “version” of the representational state contained in
the response’s entity (HTTP headers and body). The entity tag can be any string value, so long as it changes along with
the resource’s representation.

Clients may choose to save an `ETag` header’s value for use in future `GET` requests, as the value of the conditional
`If-None-Match` request header. If the REST API concludes that the entity tag hasn’t changed, then it can save time and
bandwidth by not sending the representation again.

Clients must save the `ETag` header’s value (if present) for use in future `POST`, `PUT` and `Patch` requests, as the
value of the conditional `If-Match` request header. If the REST API concludes that the entity tag hasn’t changed, then
it can process the requested change.

### Resources without `ETag` support

The `ETag` header MUST NOT be sent in response to `GET` requests for resources that do not support ETags.

Requests for resources without `ETag` support that contain a `If-Match` or `If-Non-Match` header (or any other
conditional header) MUST be responded to with a `400 Bad Request`. The body of the response must make clear that
conditional headers are not allowed on resources that do not support it.

### `POST` must be used to create a new resource in a collection

Clients use `POST` when attempting to create a new resource within a collection.
The `POST` request’s body contains the **suggested** state representation of the new resource to be added to the
server-owned collection.

Example:

    POST /v1/categories HTTP/1.1
    Host: api.marktplaats.nl
    Accept-Language: nl, en

    {
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }


    HTTP/1.1 201 Created
    Location: http://api.marktplaats.nl/v1/categories/95
    Content-Type: application/json
    E-Tag: "qg7968osihugw"

    {
        "_links": {
            "self": { "href": "/v1/categories/95" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
        },
        "id": 95,
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }

Body in the response is included by default. This can be overridden with the
[`_body` parameter](/docs/base-url.md#_body).

### `PUT` must be used to completely update a resource

Clients use `PUT` when attempting to update all fields of an existing resource. The request body contains the
**suggested** state representation of the resource.

Example:

    PUT /v1/categories/95 HTTP/1.1
    Host: api.marktplaats.nl
    Accept-Language: nl, en
    If-Match: "qg7968osihugw"

    {
        "id": 95,
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }


    HTTP/1.1 200 OK
    Location: http://api.marktplaats.nl/v1/categories/95
    Content-Type: application/json
    E-Tag: "723nfhjasc"

    {
        "_links": {
            "self": { "href": "/v1/categories/95" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
        },
        "id": 95,
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }

The `If-Match` header is NOT allowed for resources that don't support ETag. It is optional (but strongly recommended)
for resources that do support it.

Body in the response is included by default. This can be overridden with the
[`_body` parameter](/docs/base-url.md#_body).

Clients that do not support the `PUT` method may use the [`_method` parameter](/docs/base-url.md#_method).

### `PATCH` must be used to partially update a resource

Clients use `PATCH` when attempting to partially update an existing resource. The request body contains values according
to [RFC 6902](http://tools.ietf.org/html/rfc6902).

Example:

    PATCH /v1/categories/95 HTTP/1.1
    Host: api.marktplaats.nl
    Accept-Language: nl, en
    Content-Type: application/json-patch+json
    If-Match: "qg7968osihugw"

    [
        { "op": "replace", "path": "/name", "value": "BMW" },
        { "op": "replace", "path": "/hostName", "value": "BMW" }
    ]


    HTTP/1.1 200 OK
    Location: http://api.marktplaats.nl/v1/categories/95
    Content-Type: application/json
    E-Tag: "723nfhjasc"

    {
        "_links": {
            "self": { "href": "/v1/categories/95" },
            "describedby": { "href": "http://api.marktplaats.nl/v1/docs/resources/category" },
            "http://api.marktplaats.nl/v1/docs/rels/parent-category": { "href": "/v1/categories/91" }
        },
        "id": 95,
        "parentCategoryId": 91,
        "name": "BMW",
        "shortName": "BMW"
    }

Implementation are recommended to implement `replace` as `add` when the field is not present in the original representation.

The `If-Match` header is NOT allowed for resources that don't support ETag. It is optional (but strongly recommended)
for resources that do support it.

The response codes for the `PATCH` method are similar to other HTTP methods except for `422 (Unprocessable Entity)`.
Return this when the server cannot honor the request because it might result in a bad state for the resource.

Body in the response is included by default. This can be overridden with the
[`_body` parameter](/docs/base-url.md#_body).

Clients that do not support the `PATCH` method may use the [`_method` parameter](/docs/base-url.md#_method).

### DELETE must be used to remove a resource from its parent

A client uses DELETE to request that a resource be completely removed from its parent, which is often a collection or
store.

Once a DELETE request has been processed for a given resource, the resource can no longer be found by clients.
Therefore, any future attempt to retrieve the resource’s state representation, using either GET or HEAD, must result in
a 404 (“Not Found”) status returned by the API.

The DELETE method is idempotent. This implies that the server must return a response indicating success even if the
server deleted the resource in a previous request.

Example:

    DELETE http://api.marktplaats.nl/v1/categories/92
    Host: api.marktplaats.nl
    Accept-Language: nl, en
    If-Match: "9iurffjkqe"

    HTTP/1.1 204 No Content

The `If-Match` header is NOT allowed for resources that don't support ETag. It is optional (but strongly recommended)
for resources that do support it.

Clients that do not support the `DELETE` method may use the [`_method` parameter](/docs/base-url.md#_method).


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
take a long while to process. When responding with a 202 header you may choose to include a link to a resource that can be used to
track the status of your request in the response

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
