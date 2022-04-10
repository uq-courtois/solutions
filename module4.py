### Exercise 1

import json

data = {
   "items": [
		 {
			 'shape':'rectangle',
			 'length':4,
			 'width':5
		 },
		 {
			 'shape':'square',
			 'length':4,
			 'width':4
		 },
		 {
			 'shape':'cube',
			 'length':4,
			 'width':4,
			 'height':4
		 },
   ]
}
print(json.dumps(data, sort_keys=True, indent=3)) 
