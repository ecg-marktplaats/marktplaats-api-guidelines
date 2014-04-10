Introduction
============

Principles
----------

The overarching theme for all following guidelines is "No surprises" since the users of the APIs can expect a certain
behavior and continuity in our APIs.

*   *Changes must never break existing applications*
    We have no idea what our customers are using to talk to our API and if or when they are going to adapt to a change.
    This means that changes must be communicated properly and must be backwards compatible.

*   *Discovery*
    Having just the base URL, it should be possible *for a programmer* to discover all resources and their
    documentation. (Level 3 of the [Richardson Maturity Model](http://restcookbook.com/Miscellaneous/richardsonmaturitymodel/)). We do not believe in automatic discovery.

*   *Consistency*
    These guidelines make it possible to make all our APIs consistent. Consistency should be found in all of these
    aspects:
    * Naming: URLs are structured the same way throughout all our APIs. Field names are always in camelCase and the
      same word is used for the same thing. For example, the postal code should not be called postcode, postalCode and
      zipCode.
    * Data structures: We use the same representation for common data such as timestamps, or links to other resources.
    * Authentication and authorization: We choose one authentication mechanism for all APIs instead of multiple
      different ones.
    * Documentation: We choose one style and documentation format for all of our APIs to make all APIs look like one.

    Note that these guidelines sometimes contain arbitrary decisions that were made solely for consistency.

*   *Community contributions are easy*
    Since we want other people to use our APIs we need to build a community around them to communicate with our users.
    This will help us to find bugs, inconsistencies and learn about usage and improvements.

*   *No technology enforced for the implementations*
    Though we can give some recommendations on tools and libraries for implementing the APIs, API implementers are not
    limited a specific language or tool chain. The APIs must be implementable (both client and server) with multiple
    different tool chains.

*   *Safe*
    Any API should be safe, both for eBay and its clients.
