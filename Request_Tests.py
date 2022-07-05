import requests

URL = "http://www.ebi.ac.uk/ols/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0043226"
requestResult = requests.get(url=URL)
requestResultList = requestResult.text.split("\n")

URL = "https://www.ebi.ac.uk/spot/oxo/api/terms/UMLS:C0033300"
requestResult = requests.get(url=URL)
requestResultList = requestResult.text.split("\n")

URL = "https://www.ebi.ac.uk/spot/oxo/api/mappings?fromId=UMLS:C0033300"
requestResult = requests.get(url=URL)
requestResultList = requestResult.text.split("\n")

URL = "https://www.ebi.ac.uk/spot/oxo/api/search"
PARAMS = {'ids': ["UMLS:C0033300", "UMLS:C2239176"],
          'mappingTarget': ["OMIM"],
          'mappingSource': ["UMLS"],
          'distance': 1}
requestResult = requests.get(url=URL, params=PARAMS)
data = requestResult.json()
tableList = ['UMLSQuery\tUMLSID\tUMLSLabel\tOMIMID\tOMIMLabel']
for dict in data['_embedded']['searchResults']:
    UMLSQuery = dict["queryId"]
    UMLSID = dict["curie"]
    UMLSLabel = dict["label"]
    for dictCorres in dict["mappingResponseList"]:
        OMIMID = dictCorres["curie"]
        OMIMLabel = dictCorres["label"]
        tableList.append("\t".join([UMLSQuery, UMLSID, UMLSLabel, OMIMID, OMIMLabel]))