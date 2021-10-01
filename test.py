import json
def update(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["num_list"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
print("""
 /$$                       /$$       /$$                             /$$               /$$           /$$      
| $$                      | $$      |__/                            | $$              |__/          | $$      
| $$$$$$$  /$$   /$$      | $$$$$$$  /$$  /$$$$$$  /$$   /$$       /$$$$$$    /$$$$$$  /$$ /$$$$$$$ | $$$$$$$ 
| $$__  $$| $$  | $$      | $$__  $$| $$ /$$__  $$| $$  | $$      |_  $$_/   /$$__  $$| $$| $$__  $$| $$__  $$
| $$  \ $$| $$  | $$      | $$  \ $$| $$| $$$$$$$$| $$  | $$        | $$    | $$  \__/| $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$      | $$  | $$| $$| $$_____/| $$  | $$        | $$ /$$| $$      | $$| $$  | $$| $$  | $$
| $$$$$$$/|  $$$$$$$      | $$  | $$| $$|  $$$$$$$|  $$$$$$/        |  $$$$/| $$      | $$| $$  | $$| $$  | $$
|_______/  \____  $$      |__/  |__/|__/ \_______/ \______/          \___/  |__/      |__/|__/  |__/|__/  |__/
           /$$  | $$                                                                                          
          |  $$$$$$/                                                                                          
           \______/                                                                                                                                                    
                                                         """)
while True:
    menu = input("lua chon:\nnhap du lieu - hoan thanh: ")
    if (menu.lower()=="nhap du lieu"):
        identifer = input("nhap id: ")
        name = input("nhap ten: ")
        dob = input("nhap ngay thang nam sinh (dd/mm/yyyy): ")
        new = {"id": "{}".format(identifer), "name": "{}".format(name), "dob": "{}".format(dob)}
        update(new)
    elif (menu.lower()=="hoan thanh"):
        print("hoan thanh!")
        input()
    else:
        print("cu phap khong hop le")