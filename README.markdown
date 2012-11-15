# BeerSite #
## An example use case for Apache Solr ##

This is an example Django site that allows us to better understand 
how to work with Solr. It is indended to be an accompaniment to the 
screencast collection *Getting Started with Apache Solr Search Server*, to be 
distributed by [Packt Publishing](http://packtpub.com).

An *advanced* branch includes commits outlining how to include:
* spellcheck
* grouped results
* match highlighting
* the MoreLikeThis request handler

### Requirements ###
* [Apache Solr](http://solr.apache.org)
* [solrpy](http://wiki.apache.org/solr/SolPython)
* [pynt](https://github.com/h0ke/pynt) -- *installation was messy so this is included, and does not need to be installed*
* [Django](https://www.djangoproject.com/)

### How To Use ###
* Make sure you have your requirements installed
* Copy the schema file in the solrFiles folder to apache-solr/example/solr/conf/schema.xml (it's optimal to do this from a fresh unzip)
* Start or restart your solr instance ("java -jar start.jar" from apache-solr/example)
* Call "python importBeer.py" from the BeerSite project root directory
* From the BeerSite project root directory, call "python manage.py runserver 8080"
* Navigate to localhost:8080 in your web browser. You should be ready to search!

### Homeworks ###
* *Introduce Filter Queries*
 * Add an optional parameter to the search view function for brewer_name filter query
 * Implement brewer name filter query when querying solr
 * Deliver data to view in such a way that filtering between brewers for the same search term only requires clicking
* *Add ABV*
 * Update the Schema File to Include ABV
 * Update the ETL script to add ABV data
 * Display ABV in each search result
 * Add option to sort by relevance, weakest (ABV ascending) and strongest (ABV descending)