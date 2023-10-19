import pyodbc




# project Class 
class ProjectDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IN-TUSHARLAKHE\SQLEXPRESS;DATABASE=cafe;')
        self.cursor = self.conn.cursor()

# To return all the Information from Project table
    def get_project(self,id=None):
        result=[]
        if(id==None):
            query = "SELECT * FROM Project"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                prod_dict = {}
                prod_dict["project_id"] = row[0]
                prod_dict["project_name"] = row[1]
                prod_dict["project_description"] = row[2]
                result.append(prod_dict)
        else:
            query=" SELECT * FROM Project WHERE ProjectID = '{}'".format(id) 
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                prod_dict = {}
                prod_dict["project_id"] = row[0]
                prod_dict["project_name"] = row[1]
                prod_dict["project_description"] = row[2]
                result.append(prod_dict)       
        return result
# Asset class    
class AssetDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IN-TUSHARLAKHE\SQLEXPRESS;DATABASE=cafe;')
        self.cursor = self.conn.cursor()

# To return all the Information from Asset table
    def get_asset(self,id=None):
        output=[]
        if(id==None):
            query = "SELECT * FROM Asset"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                asset_dict = {}
                asset_dict["AssetID"] = row[0]
                asset_dict["AssetName"] = row[1]
                asset_dict["Information"] = row[2]
                asset_dict["Cost"] = row[3]
                asset_dict["AssetType"] = row[4]
                asset_dict["AssetLocation"] = row[5]
                output.append(asset_dict)
               
        else:
            query=" SELECT * FROM Asset WHERE AssetID = '{}'".format(id) 
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                asset_dict = {}
                asset_dict["AssetID"] = row[0]
                asset_dict["AssetName"] = row[1]
                asset_dict["Information"] = row[2]
                asset_dict["Cost"] = row[3]
                asset_dict["AssetType"] = row[4]
                asset_dict["AssetLocation"] = row[5]
                output.append(asset_dict)    
        return output


# Need Class
class NeedDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IN-TUSHARLAKHE\SQLEXPRESS;DATABASE=cafe;')
        self.cursor = self.conn.cursor()

# To return all the Information from Need table
    def get_need(self,id=None):
        outcome=[]
        if(id==None):
            query = "SELECT * FROM Need"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                need_dict = {}
                need_dict["NeedID"] = row[0]
                need_dict["AssetID"] = row[1]
                need_dict["Critacility"] = row[2]
                need_dict["Descriptions"] = row[3]
                need_dict["Author"] = row[4]
                outcome.append(need_dict)
               
        else:
            query=" SELECT * FROM Need WHERE NeedID = '{}'".format(id) 
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                need_dict = {}
                need_dict["NeedID"] = row[0]
                need_dict["AssetID"] = row[1]
                need_dict["Critacility"] = row[2]
                need_dict["Descriptions"] = row[3]
                need_dict["Author"] = row[4]
                outcome.append(need_dict)    
        return outcome  



#db=ProjectDatabase()
#db.get_project()