Documentation requirements
==========================

Documentation URLs
------------------

### Documentation base URL

The documentation base URL SHOULD be as the API's base URL but with the following changes:

* `http` instead of `https`
* append /docs

### Documentation URLs

Documentation should live at the following URLs (assuming `http://api.marktplaats.nl/v1/docs/` as documentation base
URL):

Resources: `http://api.marktplaats.nl/v1/docs/resources/{resource-name}`
Relations: `http://api.marktplaats.nl/v1/docs/rels/{relation-name}`

Further documentation (e.g. deprecations) should go below those. For example:

Resource deprecation: `http://api.marktplaats.nl/v1/docs/rels/{relation-name}/deprecation`
Resource other: `http://api.marktplaats.nl/v1/docs/rels/{relation-name}/{detail-subject}`
Field deprecation: `http://api.marktplaats.nl/v1/docs/resources/{resource-name}/{field-name}-deprecation`

Resource documentation
----------------------

### Contents

The following must be documented for each resource:

* name
* description
* URL template
* supported methods
* in which resources it can be embedded
* whether it is deprecated
* For each linked resource:
    * name
    * description
    * URL template
    * link to resource documentation
    * supported methods
    * whether it can be embedded
    * whether it is deprecated
* A list of all fields with for each field:
    * name
    * description
    * type value (see section [field types](#field-types))
    * format value (see section [field types](#field-types))
    * required?
    * writable?

For each deprecation the document MUST describe when the relation/resource/field will no longer be supported.

### Field types

The following field types are in use (inspired by but not the same as <https://developers.google.com/discovery/v1/type-format>):

<table>
<tr><th>Type value</th><th>Format value</th><th>Meaning</th></tr>
<tr><td>any</td><td></td><td>The property may have any type. Defined by the JSON Schema spec.</td></tr>
<tr><td>array</td><td></td><td>A JavaScript array of values. The items property indicates the schema for the array
  values. Defined by the JSON Schema spec.</td></tr>
<tr><td>boolean</td><td></td><td>A boolean value, either "true" or "false". Defined by the JSON Schema spec.</td></tr>
<tr><td>integer</td><td>int32</td><td>A 32-bit signed integer. It has a minimum value of -2,147,483,648 and a maximum
  value of 2,147,483,647 (inclusive).</td></tr>
<tr><td>integer</td><td>uint32</td><td>A 32-bit unsigned integer. It has a minimum value of 0 and a maximum value of
  4,294,967,295 (inclusive).</td></tr>
<tr><td>number</td><td>double</td><td>A double-precision 64-bit IEEE 754 floating point.</td></tr>
<tr><td>number</td><td>float</td><td>A single-precision 32-bit IEEE 754 floating point.</td></tr>
<tr><td>object</td><td></td><td>A JavaScript object. Defined by the JSON Schema spec.</td></tr>
<tr><td>string</td><td></td><td>An arbitrary string. Defined by the JSON Schema spec.</td></tr>
<tr><td>string</td><td>byte</td><td>A padded, base64-encoded string of bytes, encoded with a URL and filename safe
  alphabet (sometimes referred to as "web-safe" or "base64url"). Defined by RFC4648.</td></tr>
<tr><td>string</td><td>date</td><td>An ISO8601 date in the format `YYYY-MM-DD`. Defined in the JSON Schema spec.</td></tr>
<tr><td>string</td><td>date-time</td><td>An ISO8601 timestamp in UTC time. This is formatted as
  `YYYY-MM-DDThh:mm:ss.fffZ`.</td></tr>
<tr><td>string</td><td>int64</td><td>A 64-bit signed integer. It has a minimum value of -9,223,372,036,854,775,808 and
  a maximum value of 9,223,372,036,854,775,807 (inclusive).</td></tr>
<tr><td>string</td><td>uint64</td><td>A 64-bit unsigned integer. It has a minimum value of 0 and a maximum value of
  (2^64)-1 (inclusive).</td></tr>
</table>


Document link relations
-----------------------

Getting started guide
---------------------

API reference
-------------

Example code
------------


TODO
----

* Integrate:
