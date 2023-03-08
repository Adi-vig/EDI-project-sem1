import pymongo as pm

if __name__ == "__main__":
    print("welcome to pymongo")
    client_0 = pm.MongoClient("mongodb://localhost:27017")
    print(client_0)


    db_1= client_0["Students_DB"]
    collection = db_1["Students_Col"]
    collection.drop()


    test1=[
        {'_id':12200001, 'name':'Aditya Sakhare'       ,'rol_no':1  ,'email': 'aditya.sakhare22@vit.edu'          },
        {'_id':12200002, 'name':'Saif Khan'            ,'rol_no':2  ,'email': 'salim.saif22@vit.edu'              },
        {'_id':12200003, 'name':'Prathmesh Salokhe'    ,'rol_no':3  ,'email': 'prathamesh.salokhe22@vit.edu'      },
        {'_id':12200004, 'name':'Sakshi Salunke'       ,'rol_no':4  ,'email': 'sakshi.salunke22@vit.edu'          },
        {'_id':12200005, 'name':'Rahul Sakpal'         ,'rol_no':5  ,'email': 'rahul.sakpal22@vit.edu'            },
        {'_id':12200006, 'name':'Rushikesh Sakhare'    ,'rol_no':6  ,'email': 'rushikesh.sakhare22@vit.edu'       },
        {'_id':12200007, 'name':'Sankalp Savane'       ,'rol_no':7  ,'email': 'sankalp.savane22@vit.edu'          },
        {'_id':12200008, 'name':'Riddhi Shende'        ,'rol_no':8  ,'email': 'riddhi.shende22@vit.edu'           },
        {'_id':12200009, 'name':'Aadil Shaikh'         ,'rol_no':9  ,'email': 'aadil.shaikh22@vit.edu'            },
        {'_id':12200010, 'name':'Rohitashwa Kumawat'   ,'rol_no':10 ,'email': 'rohitashwa.kumawat22@vit.edu'      },
        {'_id':12200011, 'name':'Rajnandini Dharashiwe','rol_no':11 ,'email': 'rajnandini.dharashive22@vit.edu'   },
        {'_id':12200012, 'name':'Samarveer Moray'      ,'rol_no':12 ,'email': 'samarveer.moray22@vit.edu'         },

    ]

    collection.insert_many(test1)