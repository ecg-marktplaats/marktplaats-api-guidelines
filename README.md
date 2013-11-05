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
		* Field names are in English unless they represent a product or company name.
		* Field names are in camelCase, contain only latin characters 'a' - 'z', 'A' - 'Z', '0' - '9'.
		* Field names start with a lowercase letter, 'a' - 'z'.
		* Field names starting with underscore '\_' are reserved for external standards, e.g. Hal.
		* Field values that represent a date are in ISO8601 full syntax in UTC ('Z') with milliseconds, e.g. `"2013-20-02T18:02:24.000Z"`, clients should be prepared to see dates truncated in responses, for example to the second or minute.
		* value format (e.g. dates)
	* Semantics
		* TODO: naming standards, camelCase (e.g. postcode vs zipcode, etc.)
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

