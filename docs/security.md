Security
========

## Authentication


Authentication should be done using OAuth 2.0. OAuth 2.0 does not prescribe exactly how it should be used, since it is basically a framework for authorization methods. However, there are some industry standards which are nowadays considered the default implementation of OAuth 2.0. Since we strive to a consistent and predictable API, this is the way OAuth 2.0 should be used in our API's.

### What is OAuth 2.0


OAuth 2.0 is an open authorization protocol which enables applications to
access each others data. OAuth 2.0 specification replaces and obsoletes the
OAuth 1.0 protocol and is *not* backward compatible with OAuth 1.0.

### OAuth 2.0 Roles

OAuth 2.0 defines the following roles of users and applications:

* **Resource Owner:** This is the person or application that owns the data
  that is to be shared. In this context *resource owner*
  is the Martkplaats user.

* **Resource Server:** This is the server hosting the resource owned by the
  resource owner. In this context *resource server* is the server hosting
  Marktplaats API.

* **Client:** This is the application requesting access to the resources stored
  on the resource server. In this context *client* is the application wanting
  to use the Marktplaats API.

* **Authorization Server:** The authorization server is the server
  authorizing the client app to access the resources of the resource owner.
  In this context *authorization server* is the server hosting authentication
  and token endpoints.

### Support in our API's

OAuth 2.0 describes four different authorization grants. An authorization grant is basically a certain way of performing the authentication of the user. Those four grant types are:

1. Authorization code grant
2. Implicit grant
3. Resource owner password credentials grant
4. Client credentials grant

In general, the minimum you need to support in you authentication flow should be th Authorization code grant (3-legged OAuth 2.0).

The first three grants, Authorization code grant, Implicit grant and Resource owner password credentials grant, allows the client to authenticate against the API on behalf of the resource owner. For security reasons, the Authorization code grant is the most preferred way to achieve this.

Implicit grant **should not be used**, because it is unsecure and vulnerable for XSS and CSRF attacks. Because this is a problem, the used Authorization Server should not support it, because if you support it your Authorization code grant is in theory not more safe than Implicit grant, unless you enforce the client to register the *response_type* with the *redirect_uri* and check for that. Without this check, it is trivial to change *response_type=code* to *response_type=token*, with all the negative consequences implied with the implicit grant as well.

The Client credential grant enables the client to authenticate itself with the API without a resource owner. This is specifically useful to do 'service' calls to the API, which are not specific for a given user, or to allow a user of the client to access the API without having to authenticate explicitly. This can be useful to allow the client to give the user access to 'public' information (anonymous requests).

In general, it is not preferred to have no authentication at all for any endpoint of your API, because it will be impossible to relate a call to a specific client and it opens up the API for misuse, because it will be impossible to do any rate limiting.

#### Registration of Clients

Before a client application can authenticate against the resource server, it is required that a client can be registered. Some recommendations to improve security of your application regarding registration of clients:

* It is required that a client register at least one *request_uri*.
* It is recommended that it is allowed to register multiple *request_uri* for a client and use it as a whitelist of allowed request_uri's.
* When possible, allow the client to register the allowed scopes for each *request_uri* and verify these when authorizing a user.
* When possible, register the allowed *response_type* (normally only *code* should be allowed) for each *request_uri*. This way, you prevent malicious clients from unauthorized use of resources on behalf of a resource owner.

#### Application specific tokens

It may be desirable to allow an user of your website to create application specific tokens. This will allow the user to create a token for a specific application (or client). Your website will then present the user with an access_token which can be used to perform calls to the API. This is basically a way directly use your API, without the necessity to go through the entire authentication flow. This can be useful to lower the barrier for creating simple clients which are using your API.

### Secure implementation of OAuth 2.0

There are some things to take into consideration when implementing OAuth 2.0. It is recommended to at least apply the following rules to your implementation:

For Authentication Grant:

* Strict checking of the *request_uri* when the client specifies a custom request_uri. The *request_uri* provided when requesting the *authentication_code* has to be exactly the same as the *request_uri* provided when requesting the *access_token*. The custom *request_uri* has to be on the same host as the *request_uri* provided when the client was registered.
* Restrict expiration time of *access_token* and *refresh_token*. The *access_token* could best be compared to a password and should be treated as such. A recommended expire duration for the access_token is 5 minutes. The *refresh_token* could best be compared to a session id, and as such should have a restricted expiration time as well. A recommended expire duration for the *refresh_token* is 24 hours.

## Rate limiting

Rate limiting should be part of the API. The number of request should be limited for a client as well for a resource owner. Exact details TBD.

## General security advice

Some general recommendations for building a secure API:

* Don't expose e-mails in API. Only the e-mail of the resource owner should be accessible for the user of an API. Exposing e-mails of other users is a security risk.
* TBD.
