api-guidelines
==============

Guidelines for externally visible APIs.

[Documentation is here](https://github.scm.corp.ebay.com/pages/ecg-marktplaats/api-guidelines/)

Go to [The source](source/index.rst).


Build the API Guidelines
------------------------

Edit the source and then do:
    git commit -a && make clean && make html && git checkout gh-pages && git merge -s subtree master && git push && git checkout master

Update rendered version
-----------------------

It is a Github Page. So you need to checkout the `gh-pages` branch of this project and copy the `build` directory to it. 
