# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api,abort
from db1 import ProjectDatabase,AssetDatabase,NeedDatabase

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

# making a class for a particular resource 
# they are automatically mapped by flask_restful. 
# This is a project database 
class Project(Resource): 
    def __init__(self):
        self.db1 = ProjectDatabase()
	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
    def get(self, id=None):
         #id = args.get('id')  
        #  id=None
         if id is None:
          return self.db1.get_project()
         else:
            result = self.db1.get_project(id)
            #if result is None:
               # abort(404, message="Record doesn't exist")
         return result  

# making a class for a particular resource 
# they are automatically mapped by flask_restful. 
# This is a Asset database    
          
class Asset(Resource): 
    def __init__(self):
        self.db2 = AssetDatabase()
	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
    def get(self, id=None):
         #id = args.get('id')  
        #  id=None
         if id is None:
            return self.db2.get_asset()
         else:
            output = self.db2.get_asset(id)
            #if result is None:
               # abort(404, message="Record doesn't exist")
         return output 

# making a class for a particular resource 
# they are automatically mapped by flask_restful. 
# This is a Asset database  
  
class Need(Resource): 
    def __init__(self):
        self.db3 = NeedDatabase()
	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
    def get(self, id=None):
         #id = args.get('id')  
        #  id=None
         if id is None:
            return self.db3.get_need()
         else:
            output = self.db3.get_need(id)
            #if result is None:
               # abort(404, message="Record doesn't exist")
         return output 

	





# adding the defined resources along with their corresponding urls 
api.add_resource(Project, '/','/<id>') 
api.add_resource(Asset, '/asset','/asset/<id>') 
api.add_resource(Need, '/need','/need/<id>') 



# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
