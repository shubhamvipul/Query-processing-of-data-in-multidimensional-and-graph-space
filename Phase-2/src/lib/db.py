from pymongo import MongoClient 

class Database:

	# create a client(channel) to given host and port
	def __init__(self, host, port):
		self.client = MongoClient(host, port)

	# create session for given client and database
	def connect_to_db(self, dbname):
		self.db = self.client[dbname]

	# close connection
	def close(client):
		self.client.close()

	# create connection to given collection inside given db
	def table(self, collection):
		self.collection = db[collection]

	# retrieve documents from given collection w.r.t. given query
	# implements both findAll and findOne
	# output will be array in case of multiple docs are object in case of single doc
	def get(self, query):
		cursor = self.collection.find(query)
		res = []
		for doc in cursor:
			res.append(doc)
		if len(res) == 1:
			res = res[0]
		return res

	# insert given list of documents into given collection
	def put(docs):
		if isinstance(docs, list):
			return self.collection.insert_many(docs)
		doc_list = []
		doc_list.append(docs)
		return self.collection.insert_many(doc_list)
