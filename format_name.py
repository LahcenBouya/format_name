def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "invalid inputs"
    first_name=f_name.title()
    last_name=l_name.title()
    return f"{first_name} {last_name}"
formated_name=format_name(input("please enter your first name: "),input("please enter your last name: "))
print(formated_name)