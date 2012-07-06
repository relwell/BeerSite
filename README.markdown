# BeerSite #
## An example use case for Apache Solr ##

This is an example Django site that allows us to better understand 
how to work with Solr.

### Requirements ###
* [solrpy](http://wiki.apache.org/solr/SolPython)
* [pynt](https://github.com/h0ke/pynt) -- installation was messy so this is included, not as a submodule
* django

### How To Use ###
* Make sure you have your requirements installed (django and solrpy)
* Copy the schema file in the solrFiles folder to apache-solr/example/solr/conf/schema.xml (it's optimal to do this from a fresh unzip)
* Start or restart your solr instance
* Call "python importBeer.py"
* From the BeerSite folder, call "python manage.py runserver 8080".
* Go to localhost:8080. You should be ready to search!