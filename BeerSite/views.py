from django.shortcuts import render_to_response
from django.http import HttpResponse
import solr

def home(request):
    return HttpResponse('hello');

def search(request, query):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query(query)
    return render_to_response('searchresults.html', {'searchresults':searchresults,
                                                     'title': "Search results for",
                                                     'em' : query
                                                     }
                              )

def brewers(request, brewer_name):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query('brewery_name:"%s"' % brewer_name)
    return render_to_response('searchresults.html', {'searchresults':searchresults,
                                                     'title': 'Beers from',
                                                     'em' : brewer_name
                                                     }
                              )

def morelikethis(request, id):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query('id:%s' % id, mlt='true', mlt_fl='description')
    mlt = searchresults.moreLikeThis[searchresults.moreLikeThis.keys()[0]]

    return render_to_response('searchresults.html', {'searchresults':mlt,
                                                     'title':"More like",
                                                     'em': '%s from %s' % (searchresults.results[0]['name'], searchresults.results[0]['brewery_name'])
                                                     }
                              )
