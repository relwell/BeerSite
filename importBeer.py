import solr
from pynt.pynt import Beer

solrConnection = solr.SolrConnection('http://localhost:8983/solr')

response = Beer.all()

total = response.get('total', 0)

print "Found %s beers" % total

beers = response.get('beers', [])

docs = [{"id":str(beer['id']),
         "name":beer['name'],
         "description":beer['description'],
         "brewery_id":str(beer['brewery']['id']),
         "brewery_name":beer['brewery']['name']
         } for beer in beers]

solrConnection.add_many(docs)
solrConnection.commit()

print "Successfully imported documents"
