from pddiktipy import api
from pprint import pprint

with api() as client:
    result = client.search_mahasiswa('Restu Imam Syafii')
    pprint(result)
