from requests import get
import json
from pprint import pprint
from time import sleep

def parse(url, low_price):
	r = get(url)
	js = json.loads(r.text)
	owners = js['ownerUsernames']
	items = js['listings']
	positions = {}
	for item in items:
		if item['currency'] == 'cur_berry':
			positions[item['_id']] = item['price']
	
	for k in sorted(positions, key=positions.get):
		l = [x for x in items if x['_id'] == k]
		owner = owners[l[0]['ownerId']]
		price = positions[k]
		if price <= low_price:
			quantity = l[0]['quantity'] - l[0]['purchasedQuantity']
			return owner, price, quantity
		break

def main():
	items = {
		'itm_scarrotFruit': 26,
		'itm_scarrotLoaf': 78,
		# 'itm_wintermintFruit': 22,
		'itm_grainbow': 8,
		'itm_storageChest6Slot': 3000,
		'itm_woodenbeam': 410,
		'itm_beeswax': 50,
		# 'itm_hard_wood': 1,
		'itm_Glue': 625,
		'itm_scarrotwine': 875,
		'itm_plank': 5,
		'itm_constructionPowder': 1000,
		# 'itm_Shrapnel': 10,
		'itm_Bomb_Shell': 1000,
		# 'itm_void': 270,
		# 'itm_Marble': 1000,
		'itm_hotatoseed': 10000,
		'itm_tree_sap': 10000,
		# 'itm_hot_sauce': 10000,
		'itm_hotato': 100,
		# 'itm_hotato_hotka': 1000,
		# 'itm_hot_sauce': 1000,

	}
	
	for k, v in items.items():
		r = parse('https://pixels-server.pixels.xyz/v1/marketplace/item/{}'.format(k), v*10)
		if r:
			# if r[1] < v:
			print(*r, k)
		sleep(3)
if __name__ == '__main__':
	main()