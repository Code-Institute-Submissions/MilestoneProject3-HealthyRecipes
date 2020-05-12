{"changed":true,"filter":false,"title":"mongo.py","tooltip":"/mongo.py","value":"import pymongo\nimport os\n\nMONGODB_URI = os.getenv(\"MONGO_URI\")\nDBS_NAME = \"myTestDB\"\nCOLLECTION_NAME =\"myFirstMDB\"\n\ndef mongo_connect(url):\n    try:\n        conn= pymongo.MongoClient(url)\n        print(\"Mongo is connected!\")\n        return conn\n    except pymongo.errors.ConnectionFailure as e:\n        print(\"Could not connect to MongoDB: %s\") % e\n        \nconn = mongo_connect(MONGODB_URI)\n\ncoll = conn[DBS_NAME][COLLECTION_NAME]\n\ncoll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})\n\ndocuments = coll.find({'nationality': 'american'})\n\nfor doc in documents:\n    print(doc)","undoManager":{"mark":101,"position":100,"stack":[[{"start":{"row":17,"column":0},"end":{"row":22,"column":21},"action":"remove","lines":["coll = conn[DBS_NAME][COLLECTION_NAME]","","new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},","{'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]","","coll.insert(new_docs)"],"id":338}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["d"],"id":339},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["o"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"remove","lines":["s"],"id":340}],[{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["c"],"id":341},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["u"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["m"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["n"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["t"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":[" "],"id":342},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":[" "],"id":343},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["c"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["o"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["l"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["l"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["."]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["f"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["i"]}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["n"],"id":344},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":23},"action":"insert","lines":["()"],"id":345}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":24},"action":"insert","lines":["{}"],"id":346}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":25},"action":"insert","lines":["''"],"id":347}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["f"],"id":348},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["i"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["r"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["s"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":[":"],"id":349}],[{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":[" "],"id":350}],[{"start":{"row":17,"column":32},"end":{"row":17,"column":34},"action":"insert","lines":["''"],"id":351}],[{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":[" "],"id":352}],[{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":[" "],"id":353}],[{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["d"],"id":354},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["o"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["u"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["g"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["l"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["a"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"remove","lines":[")"],"id":355},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"remove","lines":["("]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"remove","lines":["d"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"remove","lines":["n"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"remove","lines":["i"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"remove","lines":["f"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"remove","lines":["."]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"remove","lines":["l"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["l"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"remove","lines":["o"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["c"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":[" "]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["="]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":[" "]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"remove","lines":["s"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["t"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["n"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["e"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["m"]}],[{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"remove","lines":["u"],"id":356},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"remove","lines":["c"]},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"remove","lines":["o"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["d"]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""]},{"start":{"row":17,"column":43},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":43},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":357}],[{"start":{"row":17,"column":43},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":358}],[{"start":{"row":17,"column":43},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":359}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":360},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["c"],"id":361},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["o"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["l"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":[" "],"id":362},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":[" "],"id":363}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":[" "],"id":364},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["="]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":[" "]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"remove","lines":["l"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"remove","lines":["l"]},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"remove","lines":["o"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["c"],"id":365},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["o"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["l"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":[" "],"id":366},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":[" "],"id":367},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["c"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["o"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["n"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":13},"action":"insert","lines":["[]"],"id":368}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["D"],"id":369},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["B"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["S"]}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":15},"action":"remove","lines":["DBS"],"id":370},{"start":{"row":17,"column":12},"end":{"row":17,"column":20},"action":"insert","lines":["DBS_NAME"]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":23},"action":"insert","lines":["[]"],"id":371}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["C"],"id":372},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["O"]}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":24},"action":"remove","lines":["CO"],"id":373},{"start":{"row":17,"column":22},"end":{"row":17,"column":37},"action":"insert","lines":["COLLECTION_NAME"]}],[{"start":{"row":19,"column":42},"end":{"row":19,"column":43},"action":"remove","lines":[")"],"id":374},{"start":{"row":19,"column":41},"end":{"row":19,"column":42},"action":"remove","lines":["}"]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"remove","lines":["'"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"remove","lines":["s"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"remove","lines":["a"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"remove","lines":["l"]},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"remove","lines":["g"]},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"remove","lines":["u"]},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"remove","lines":["o"]},{"start":{"row":19,"column":33},"end":{"row":19,"column":34},"action":"remove","lines":["d"]},{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"remove","lines":["'"]},{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"remove","lines":[" "]},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":[":"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"remove","lines":["'"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"remove","lines":["t"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"remove","lines":["s"]},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"remove","lines":["r"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"remove","lines":["i"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"remove","lines":["f"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"remove","lines":["'"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"remove","lines":["{"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"remove","lines":["("]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"remove","lines":["d"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"remove","lines":["n"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"remove","lines":["i"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"remove","lines":["f"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"remove","lines":["."]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"remove","lines":["l"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["l"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"remove","lines":["o"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["c"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":[" "]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["="]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":[" "]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"remove","lines":["s"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["t"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["n"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["e"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["m"]},{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"remove","lines":["u"]}],[{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"remove","lines":["c"],"id":375},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"remove","lines":["o"]},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["d"]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["c"],"id":376},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["o"]},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["l"]},{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["l"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["."]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["r"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["e"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["m"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["o"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["v"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":13},"action":"insert","lines":["()"],"id":377}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":14},"action":"insert","lines":["{}"],"id":378}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":15},"action":"insert","lines":["''"],"id":379}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["f"],"id":380},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["i"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["r"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["s"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":[":"],"id":381}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":[" "],"id":382}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":24},"action":"insert","lines":["''"],"id":383}],[{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["d"],"id":384},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["o"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["g"]}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"remove","lines":["g"],"id":385}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["u"],"id":386},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["g"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["l"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["a"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":33},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":387}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":388}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["d"],"id":389},{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":["o"]},{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"insert","lines":["c"]},{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"insert","lines":["u"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["m"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["e"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["n"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["t"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":[" "],"id":390},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":[" "],"id":391},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["c"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["o"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["l"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["l"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["."]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["f"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["i"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["n"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":21},"end":{"row":21,"column":23},"action":"insert","lines":["()"],"id":392}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"remove","lines":[")"],"id":393},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"remove","lines":["("]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"remove","lines":["d"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"remove","lines":["n"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"remove","lines":["i"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"remove","lines":["f"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"remove","lines":["."]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"remove","lines":["l"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"remove","lines":["l"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"remove","lines":["o"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"remove","lines":["c"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"remove","lines":[" "]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"remove","lines":["="]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"remove","lines":[" "]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["s"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"remove","lines":["t"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"remove","lines":["n"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"remove","lines":["e"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":["m"]},{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"remove","lines":["u"]},{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"remove","lines":["c"]},{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"remove","lines":["o"]},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["d"]},{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"remove","lines":["",""]},{"start":{"row":19,"column":33},"end":{"row":20,"column":0},"action":"remove","lines":["",""]},{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"remove","lines":[")"]},{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"remove","lines":["}"]},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":["'"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"remove","lines":["s"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"remove","lines":["a"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"remove","lines":["l"]},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"remove","lines":["g"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"remove","lines":["u"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"remove","lines":["o"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"remove","lines":["d"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"remove","lines":["'"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"remove","lines":[" "]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"remove","lines":[":"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"remove","lines":["'"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"remove","lines":["t"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"remove","lines":["s"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"remove","lines":["r"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"remove","lines":["i"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["f"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"remove","lines":["'"]}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["{"],"id":394},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["("]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["e"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":["v"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"remove","lines":["o"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["m"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["e"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["r"]}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["u"],"id":395},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["p"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["d"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["a"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["t"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["_"],"id":396},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["o"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["n"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":17},"action":"insert","lines":["()"],"id":397}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":18},"action":"insert","lines":["{}"],"id":398}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":19},"action":"insert","lines":["''"],"id":399}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["n"],"id":400},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["a"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["t"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["i"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["o"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["n"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["a"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["l"]},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["i"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["t"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":[":"],"id":401}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":[" "],"id":402}],[{"start":{"row":19,"column":32},"end":{"row":19,"column":34},"action":"insert","lines":["''"],"id":403}],[{"start":{"row":19,"column":33},"end":{"row":19,"column":34},"action":"insert","lines":["a"],"id":404},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"insert","lines":["m"]},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["e"]},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["r"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["i"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["c"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["a"]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":43},"end":{"row":19,"column":44},"action":"insert","lines":[","],"id":405}],[{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"insert","lines":[" "],"id":406}],[{"start":{"row":19,"column":45},"end":{"row":19,"column":47},"action":"insert","lines":["{}"],"id":407}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["$"],"id":408},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["s"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["e"]},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"remove","lines":["t"],"id":409},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"remove","lines":["e"]},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"remove","lines":["s"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"remove","lines":["$"]}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":48},"action":"insert","lines":["''"],"id":410}],[{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["$"],"id":411}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["s"],"id":412},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["s"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"remove","lines":["e"],"id":413},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"remove","lines":["s"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"remove","lines":["s"]}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["s"],"id":414},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["e"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":[":"],"id":415}],[{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":[" "],"id":416}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":56},"action":"insert","lines":["{}"],"id":417}],[{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["h"],"id":418}],[{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"remove","lines":["h"],"id":419}],[{"start":{"row":19,"column":55},"end":{"row":19,"column":57},"action":"insert","lines":["''"],"id":420}],[{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["h"],"id":421},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":["a"]},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"insert","lines":["i"]},{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"insert","lines":["r"]},{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":["_"]}],[{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":["c"],"id":422},{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":["o"]},{"start":{"row":19,"column":63},"end":{"row":19,"column":64},"action":"insert","lines":["l"]},{"start":{"row":19,"column":64},"end":{"row":19,"column":65},"action":"insert","lines":["o"]},{"start":{"row":19,"column":65},"end":{"row":19,"column":66},"action":"insert","lines":["u"]},{"start":{"row":19,"column":66},"end":{"row":19,"column":67},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":68},"end":{"row":19,"column":69},"action":"insert","lines":[":"],"id":423}],[{"start":{"row":19,"column":69},"end":{"row":19,"column":70},"action":"insert","lines":[" "],"id":424}],[{"start":{"row":19,"column":70},"end":{"row":19,"column":72},"action":"insert","lines":["''"],"id":425}],[{"start":{"row":19,"column":71},"end":{"row":19,"column":72},"action":"insert","lines":["m"],"id":426},{"start":{"row":19,"column":72},"end":{"row":19,"column":73},"action":"insert","lines":["a"]},{"start":{"row":19,"column":73},"end":{"row":19,"column":74},"action":"insert","lines":["r"]},{"start":{"row":19,"column":74},"end":{"row":19,"column":75},"action":"insert","lines":["o"]},{"start":{"row":19,"column":75},"end":{"row":19,"column":76},"action":"insert","lines":["o"]},{"start":{"row":19,"column":76},"end":{"row":19,"column":77},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":427}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["d"],"id":428},{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":["o"]},{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"insert","lines":["c"]},{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"insert","lines":["u"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["m"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["e"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["n"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["t"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":[" "],"id":429},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":[" "],"id":430},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["c"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["o"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["l"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["l"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["."]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["f"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["i"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["n"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":21,"column":21},"end":{"row":21,"column":23},"action":"insert","lines":["()"],"id":431}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":24},"action":"insert","lines":["{}"],"id":432}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":25},"action":"insert","lines":["''"],"id":433}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["n"],"id":434},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["a"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["t"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["i"]},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["o"]},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["n"]},{"start":{"row":21,"column":30},"end":{"row":21,"column":31},"action":"insert","lines":["a"]},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["l"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["i"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["t"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["y"]}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":[":"],"id":435}],[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":[" "],"id":436}],[{"start":{"row":21,"column":38},"end":{"row":21,"column":40},"action":"insert","lines":["''"],"id":437}],[{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["a"],"id":438},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["m"]},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["e"]},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["r"]},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":["i"]},{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":["c"]},{"start":{"row":21,"column":45},"end":{"row":21,"column":46},"action":"insert","lines":["a"]},{"start":{"row":21,"column":46},"end":{"row":21,"column":47},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["m"],"id":440},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["a"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["n"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["e"],"id":439},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"remove","lines":["n"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["o"]}]]},"ace":{"folds":[],"scrolltop":40,"scrollleft":0,"selection":{"start":{"row":19,"column":12},"end":{"row":19,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":88,"mode":"ace/mode/python"}},"timestamp":1581932119842}