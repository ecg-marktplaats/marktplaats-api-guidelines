TODO
====

The following are tasks -priority ordered- that need to be done to complete the API guidelines.
Each task should be following with the plan and responsible to complete the task.

* Complete this list
  1. Just do it, A: Erik v. O.
* Consider using entity versions
  1. Discuss with current stakeholders, A: Erik v.O., I: Frank S., Martin S./Jelmer K., ETA: 2014 wk. 19/20
* Consider requiring schema.org or other naming conventions
  1. Plan: prepare discussion by finding the relevant schema's, A: Erik v.O., ETA: 2014 wk. 19
  1. Have discussion with stakeholders within ECG, A: Erik v.O., I: Ky, and people from versioning discussion.
* Lots of little edits (see list below)
* Much more details around security (authenticatie, delegation, authorisatie)
* Add more clarity around having multiple APIs acting together as one
* Consider adding information on testing
* Define a change procedure for these guidelines.
* JSONP
* CORS?

Lots of small edits
~~~~~~~~~~~~~~~~~~~

    URL, URI
        Documentation should point to HAL documentation
        underscore means meta parameters (reserved for API)
        X-HTTP-Method-override
        _body parameters applies to every call
        PATCH/DELETE not being supported by browsers => Remove
        _include/ _exclude needs major revamp
        Clearer use of MUST/SHOULD/CAN (consistent)
    - Add something about that RFC martin just mentioned (URL templates), MUST
    Resource Format
        Remove serialization from URLs
        Language of errors more clear
        Add status code as field for errors
        _link.help.href is pointing to an invalid URL (and more URLs)
        Link to type table
        help.href vs describedby
        clarify the help page link
        Add link to currying in HAL
        Clarfiy section on custom link relation types
        Fieldnames cannot be duplicate
    - Come up with field-names standard
    Interaction
        OPTION / HEAD calls missing
        TRACE not supported (security)
        Resource without etag => clarify body response is an error response
    - GZIP/Deflate
    Documentation Requirements
        Recommend order of headers, documentation tools
        Clean up stuff at the bottom
    - Expand further
    Versioning
    - Requires follow-up

    Postponed:

    DELETE call => No more fetch

    GLOBAL:

    HTTPS on all examples
    fix all todos
    Martin wants to re-do the documentation in RST

