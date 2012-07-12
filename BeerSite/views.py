from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
import solr

def home(request):
    form = SearchForm()
    return render_to_response('searchresults.html', {'form':form})

def search(request):
    s = solr.SolrConnection('http://localhost:8983/solr')

    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        group = 'true' if form.cleaned_data['group'] == True else 'false'

    searchresults = s.query(query, \
                                facet='true', \
                                facet_field='brewery_name', \
                                group=group, \
                                group_field='brewery_name',
                                group_limit=25)

    searchresults = searchresults if not form.cleaned_data['group'] else searchresults.grouped['brewery_name']['groups']

    return render_to_response('searchresults.html', {'searchresults':searchresults,
                                                     'title': "Search results for",
                                                     'em' : query,
                                                     'form' : form,
                                                     'group': form.cleaned_data['group']
                                                     }
                              )

def brewers(request, brewer_name):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query('brewery_name:"%s"' % brewer_name)
    form = SearchForm()
    return render_to_response('searchresults.html', {'searchresults':searchresults,
                                                     'title': 'Beers from',
                                                     'em' : brewer_name,
                                                     'form': form
                                                     }
                              )

def morelikethis(request, id):
    s = solr.SolrConnection('http://localhost:8983/solr')
    searchresults = s.query('id:%s' % id, mlt='true', mlt_fl='description')
    mlt = searchresults.moreLikeThis[searchresults.moreLikeThis.keys()[0]]
    form = SearchForm()
    return render_to_response('searchresults.html', {'searchresults':mlt,
                                                     'title':"More like",
                                                     'em': '%s from %s' % (searchresults.results[0]['name'], searchresults.results[0]['brewery_name']),
                                                     'form':form
                                                     }
                              )

class SearchForm(forms.Form):
    query = forms.CharField()
    group = forms.BooleanField(required=False)
