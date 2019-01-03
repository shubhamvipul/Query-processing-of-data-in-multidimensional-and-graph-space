All libraries will reside in this package. Libraries act as in interface(or drivers) in between the APIs so that a person developing a particalur API does not have to worry about the internals. Please use libraries instead of directly importing external packages in APIs.

	cache.py - may be used if we use caching anywhere(maybe to store data matrix). if not, then will remove this file
	db.py - functions to interact with db
	file.py - functions for file manipulation. again, will delete it if not required
	math.py - common math functions. example - pca, svd, lda, cosine similarity, dot product, vector length 


Following is sample usage for db library:

	from lib.db import database

	db = database("localhost", 27017) 		// read these values from config
	db.connect_to_db("mwdb_p2")				// read this from config
	
	db.table("users")
	db.put({"_id": 1, "username": "guest_user"})   // can pass an object(for one element) or an array of objects(for multiple 												   // elements)
	db.get({"username": "guest_user"}) 	// input is query. will return a single object if just one result is found(findOne) or 
										// will return an array of objects if multiple found(findAll)


