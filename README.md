api-guidelines
==============

Guidelines for externally visible APIs.


* [Introduction](docs/intro.md)
    * Principles
    * Externally used standards and guidelines
    * Contact
* [URLs and URIs](docs/base-url.md)
    * Base URL
		* https.
		* Short.
		* Includes major version (single digit) in path.
    * Naming
		* Document names should be a singular noun.
		* Collections names should be a plural noun.
		* Forward slash separator (/) must be used to indicate a hierarchical relationship.
		* URIs should not have a trailing forward slash (/).
		* Hyphens (-) should be used to improve the readability of URIs. Not underscores (_).
		* Lowercase letters should be preferred in URI paths.
* [Resource representation format](docs/resource-representation-format.md)
    * Syntax
		* Serialization format: hal+json;charset=UTF-8
		* Each resource should contain a 'self' link
		* When available IANA registered relation types should be used as link relations
		* Custom link relation types should be uri's that when dereferenced in a web browser provide relevant documentation, in the form of an HTML page
		* Field names are in English unless they represent a product or company name.
		* Field names are in camelCase, contain only latin characters 'a' - 'z', 'A' - 'Z', '0' - '9'.
		* Field names start with a lowercase letter, 'a' - 'z'.
		* Field names starting with underscore '\_' are reserved for external standards, e.g. Hal.
		* Field values that represent a date are in ISO 8601
		* Field values that represent a currency are in ISO 4217
		* Field values that represent countries are in ISO 3166-1 alpha-2 format, eg : NL
		* All money types are integers and conform to its smallest currency unit.
		
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
	* Semantics
		* TODO: naming standards, camelCase (e.g. postcode vs zipcode, etc.)
		
* [Response status codes](docs/response-status-codes.md)

		
		
		
* [Versioning](docs/versioning.md)



* error handling
* authentication
* authorization, privileges/permissions, including on-behalf-of permissions
    * provide an authorization model that can be adopted by any platform
* documentation style (layout, search, examples, etc.)
* change management (process around changing the api)
* status page
* sandbox
* example client code
* user questions/discussions
    * idea: use stackoverflow
* external contributions to documentation
    * idea: use github for issues and push requests
* organizational issues
    * consult marketing for external communications on documentation sites, github, stackoverflow, etc.

















* GET must be used to retrieve a representation of a resource
* POST must be used to create a new resource in a collection
* DELETE must be used to remove a resource from its parent



* Status codes: http://i.stack.imgur.com/whhD1.png


* Location must be used to specify the URI of a newly created resource
* ETag should be used in responses



* 


