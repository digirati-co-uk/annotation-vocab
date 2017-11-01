#!/usr/bin/env python

import glob
import json

from rdflib import Graph
from pyld import jsonld

for ontology in glob.glob('*.rdf'):
    rdf_graph = Graph()
    rdf_graph.load(ontology, format='xml')

    context = {prefix: uri for (prefix, uri) in rdf_graph.namespaces()}
    with open(ontology.replace('rdf', 'jsonld'), 'w') as jsonld_ontology_file:
        jsonld_expanded_ontology = json.loads(rdf_graph.serialize(format='json-ld'))
        jsonld_compacted_ontology = jsonld.compact(jsonld_expanded_ontology, context)

        jsonld_ontology_file.write(json.dumps(jsonld_compacted_ontology, indent=2))
