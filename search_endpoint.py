import os
import requests
from requests.auth import HTTPBasicAuth

# our demo filter that filters by geometry, date and cloud cover
from demo_filters import Vessel_Search

# Search API request object
search_endpoint_request = {
  "item_types": ["PSScene3Band"],
  "filter": Vessel_Search,
  "satellite_id": "1005"
}

result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''),
    json=search_endpoint_request)

print result.text
