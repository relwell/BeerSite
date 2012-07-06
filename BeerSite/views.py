from django.shortcuts import render_to_response
from django.http import HttpResponse
import solr

def home(request):
    return HttpResponse('hello');

def search(request, query):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query(query)
    return render_to_response('searchresults.html', {'searchresults':searchresults, 'query':query})
