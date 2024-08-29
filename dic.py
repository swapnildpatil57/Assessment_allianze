import pickle
 
# Define a Python object
person = {
    "name": "Alice",
    "age": 30,
    "gender": "female"
}
 
# Pickle the object to a binary file
with open("person.pickle", "wb") as file:
    pickle.dump(person, file)
 
print("Pickling completed")



import pickle
 
# load the data from a file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
 
# print the data
print(data)