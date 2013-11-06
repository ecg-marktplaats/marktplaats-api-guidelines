URLs and URIs
=============

Document names should be a singular noun
----------------------------------------

A URI representing a document resource should be named with a singular noun or noun phrase path segment.
For example, the URI for a single seller profile document would have the singular form:

https://api.martkplaats.nl/v1/users/1/profile


Collections names should be a plural noun
-----------------------------------------

A URI identifying a store of resources should be named with a plural noun, or noun phrase, as its path segment. 
The URI for a store of categories may use the plural noun form as follows:

https://api.martkplaats.nl/v1/categories


Forward slash separator (/) must be used to indicate a hierarchical relationship
--------------------------------------------------------------------------------

The forward slash (/) character is used in the path portion of the URI to indicate a hierarchical relationship between resources. 
For example:

https://api.martkplaats.nl/v1/categories/91/advertisements


URIs should not have a trailing forward slash (/)
-------------------------------------------------

As the last character within a URI’s path, a forward slash (/) adds no semantic value and may cause confusion. 
REST APIs should not expect a trailing slash and should not include them in the links that they provide to clients.

Many web components and frameworks will treat the following two URIs equally:

https://api.martkplaats.nl/v1/categories/ https://api.martkplaats.nl/v1/categories

However, every character within a URI counts toward a resource’s unique identity. 
Two different URIs map to two different resources. 
If the URIs differ, then so do the re- sources, and vice versa. T
Therefore, a REST API must generate and communicate clean URIs and should be intolerant of any client’s attempts to identify a resource imprecisely. 


Hyphens (-) should be used to improve the readability of URIs. Not underscores (_)
----------------------------------------------------------------------------------

To make your URIs easy for people to scan and interpret, use the hyphen (-) character to improve the readability of names in long path segments. 
Anywhere you would use a space or hyphen in English, you should use a hyphen in a URI. For example:

https://api.martkplaats.nl/v1/this-is-an-endpoint-with-a-large-name


Lowercase letters should be preferred in URI paths
--------------------------------------------------

When convenient, lowercase letters are preferred in URI paths since capital letters can sometimes cause problems. 
RFC 3986 defines URIs as case-sensitive except for the scheme and host components. 
For example:

http://api.example.restapi.org/my-folder/my-doc 
HTTP://API.EXAMPLE.RESTAPI.ORG/my-folder/my-doc 
http://api.example.restapi.org/My-Folder/my-doc

The first URL is fine and RFC3986 considers the second url to be identical to URL #1. But the third URL is not the same as URIs one and two, 
which may unnecessary confusion

