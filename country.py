def my_country(name,country="Uganda"):
    return f"hello {name} from {country} "


def multi_names(*names):
    for name in names:

        print(f"hello {name}")
        

def greet(**kwargs):
        print(kwargs) 

def greet_mult(**kwargs):
    keys=kwargs.keys()
    if "name" in keys:
        print("hello {kwargs['name']}")
    elif "country" in keys:
         print("hello {kwargs['country']}")
    else:
        print("hello anonymous")
        


        



    