import json
import uuid
print("###########  TODOLIST IN PYTHON  ############")
jsonfile = "sample.json"

# def unique_id():
#     return str(uuid.uuid4())

def getdata():
    id = input("enter id: ")
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    todo = input("todo: ")

    dictionary = {
        "id:" : id,
        "firstname:" : firstname,
        "lastname:" : lastname,
        "todo:" : todo
    }

    with open(jsonfile, "r") as getdata:
        data = json.load(getdata)

        data[id] = dictionary

        with open(jsonfile, "w") as save:
            json.dump(data, save)
        print("saved successfully ")
        print("\n")

def delete():

    id = input("enter id number: ")

    with open(jsonfile, 'r') as delete:
        data = json.load(delete)

        if id in data:
            data.pop(id)

            with open(jsonfile, 'w') as deleted:
                json.dump(data, deleted)
                print("successfully deleted")
                print("\n")
def view():
    with open(jsonfile, 'r') as view:
        data = json.load(view)
        if not data:
           print("no logs existing")
           print("\n")
        else:
            print("\nShowing logs")
            for x, i in data.items():
                for y, t in i.items():
                    print(y, t)
                print("\n")
def search():
    id = input("search for id number: ")
    with open(jsonfile, 'r') as search:
        data = json.load(search)
        print("\n")
        for identification, dic in data.items():
            if identification == id:
                print(identification, dic)
def update():
    id = input("enter id number: ")
    with open(jsonfile, 'r') as update:
        data = json.load(update)

        if id in data:
            firstname = input("enter new firstname: ")
            lastname = input("enter new lastname: ")
            todo = input("enter new todo: ")

            dictionary = {
                "id:" : id,
                "firstname:" : firstname,
                "lastname:" : lastname,
                "todo:" : todo
            }

            data[id] = dictionary

            with open(jsonfile, 'w') as updated:
                json.dump(data, updated)
                print("succesfully updated")
                print("\n")
def main():
    print("1. Add data")
    print("2. view data")
    print("3. delete data")
    print("4. update data")
    print("5. search data")
    print("6. exit.")
    print("\n")
    choices = int(input("Choose a number: "))
    if choices == 1:
        getdata()
        main()
    elif choices == 2:
        view()
        main()
    elif choices == 3:
        delete()
        main()
    elif choices == 4:
        update()
        main()
    elif choices == 5:
        search()
        main()
    elif choices == 6:
        print("it's a pleasure to serve you sir")
    else:
        print("wrong number entered, pls cho0se again!")
        main()
main()