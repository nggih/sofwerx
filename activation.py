import os
import requests

item_id = "" #"20170429_012701_1005"
item_type = "PSScene3Band"
asset_type = "visual"

list_id = ["20170429_012655_1005", "20170429_012658_1005", "20170429_012700_1005", "20170429_012659_1005", "20170429_012656_1005", "20170429_012701_1005"]

for i in list_id:
	item_id = i
	# setup auth
	session = requests.Session()
	session.auth = (os.environ['PLANET_API_KEY'], '')

	# request an item
	item = \
	  session.get(
		("https://api.planet.com/data/v1/item-types/" +
		"{}/items/{}/assets/").format(item_type, item_id))

	# extract the activation url from the item for the desired asset
	item_activation_url = item.json()[asset_type]["_links"]["activate"]

	# request activation
	response = session.post(item_activation_url)

	print response.status_code
	print ("https://api.planet.com/data/v1/item-types/" + "{}/items/{}/assets/").format(item_type, item_id)
