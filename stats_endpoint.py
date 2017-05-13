import os
import requests
from requests.auth import HTTPBasicAuth

# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir

# Stats API request object
stats_endpoint_request = {
  "interval": "year",
  "item_types": ["REOrthoTile"],
  "filter": redding_reservoir
}

# fire off the POST request
result = \
  requests.post(
    'https://api.planet.com/data/v1/stats',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], '8583459c783c4f93931ff8252614cb40'),
    json=stats_endpoint_request)

print result.text
