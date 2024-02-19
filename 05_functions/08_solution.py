# def print_kwargs(name, power):
#     print("Name ",name , "power ",power)


# print_kwargs(name="Nandan",power="Coding")


def print_kwargs(**kwrargs):
    for key,value in kwrargs.items():
        print(f"{key} : {value}")


print_kwargs(name="Nandan",power="Coding",home= "Bodhra ")