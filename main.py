from pymongo import MongoClient
from pymongo.server_api import ServerApi

cat = MongoClient(
    "mongodb+srv://manyasobol:12345@cluster0.90qon.mongodb.net/",
    server_api=ServerApi('1')
)

db = cat.book

def all_rows():
    result = db.cat.find({})
    return result

def find_cat_by_name():
    name = input("Enter cat's name: ")
    cat = db.cat.find_one({"name": name})
    if cat:
        return f"Name: {cat['name']:<10} Age: {cat['age']:<5} Features: {cat['features']}"
    else:
        return "Cat wasn't found" 

def update_age():
    name = input("Enter cat's name: ")

    try:
        age = int(input("Enter cat's new age: "))
    except ValueError:
        return "Age should be a number"
    
    cat = db.cat.find_one({"name": name})
    if cat:
        db.cat.update_one({"name": name}, {"$set": {"age": age}})
    else:
        return "Cat wasn't found" 
    
    return "Age was succesfully updated"

def add_feature():
    name = input("Enter cat's name: ")
    cat = db.cat.find_one({"name": name})
    if cat:
        new_feature = input("Enter cat's new feature: ")
        db.cat.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
    else:
        return "Cat wasn't found"
    return "Feature was successfully added"

def delete_cat():
    name = input("Enter cat's name: ")
    cat = db.cat.find_one({"name": name})
    if cat:
        db.cat.delete_one({"name": name})
    else:
        return "Cat wasn't found"
    return "Cat was successfully deleted"

def delete_all():
    db.cat.delete_many({})
    return "Cats were successfully deleted"


# while True:
#     number = input("1 - Show all cats\n"
#         "2 - Find cat by name\n"
#         "3 - Update cat's age\n"
#         "4 - Add new feature\n"
#         "5 - Delete cat by it's name\n"
#         "6 - Delete all rows\n"
#         "Choose a number of command from the list: "
#         )

#     match number:
#         case "1": 
#             result = all_rows()
#             for el in result:
#                 print(f"Name: {el['name']:<10} Age: {el['age']:<5} Features: {el['features']}")
#         case "2": 
#             print(find_cat_by_name())
#         case "3": 
#             print(update_age())
#         case "4":
#             print(add_feature())
#         case "5": 
#             print(delete_cat())
#         case "6": 
#             print(delete_all())

#         case _: break
                
