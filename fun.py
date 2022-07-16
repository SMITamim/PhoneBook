class PyDictionary:
    def __init__(self):
        while True:
            print("Choose an option:")
            print("1. Insert a keyword.")
            print("2. Update a keyword.")
            print("3. Delete a keyword.")
            print("4. Search a keyword.")
            print("5. Display")
            print("6. Exit")

            choice = int(input("Enter a number(1-6) to begin:"))

            if choice == 1:
                self.insert()
            elif choice == 2:
                self.update()
            elif choice == 3:
                self.delete()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.display()
            else:
                break
    def insert(self):
        while True:
            try:
                keyword = input("Enter a keyword:")
                definition = input("Enter definition of the keyword:")

                class_dict = {}
                class_dict[keyword] = definition

                with open("dictionary.txt", 'a') as file_object:
                    file_object.write(f"{class_dict}")
                    file_object.write(f" \n")
                break
            except:
                print("Unexpected error!")
                break
    def update(self):
        with open("dictionary.txt", 'r+') as file_object:
            search = input("keyword you want to update:")
            str = ' '
            while(str):
                str = file_object.readline()
                linelist = str.split(" , ")
                if len(str)> 0:
                    if linelist[0] == "Name:"+search:
                        keyword = input("Enter a keyword:")
                        definition = input("Enter definition of the keyword:")

                        class_dict = {}
                        class_dict[keyword] = definition
                        file_object.write(f"{class_dict}")

            else:
                print("No data found")

    def search(self):
        with open("dictionary.txt", 'r') as file_object:
            search = input("Keyword you want to search:")
            for i in file_object:
                if search in i:
                    print(i)

    def delete(self):
        with open('dictionary.txt', 'r') as file_object:
            lines = file_object.readlines()

            search = input("Enter a keyword you want to delete:")

            with open('dictionary.txt', 'w') as file_object:
                for line in lines:
                    if line.find(f"{search}") == -1:
                        file_object.write(line)
        print("Deleted")

    def display(self):
        with open("dictionary.txt", 'r') as file_object:
            dict = file_object.read()
        print(dict)

