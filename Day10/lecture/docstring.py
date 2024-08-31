def format_name(f_name, l_name):
    """
    format_name is first name, last name.
    f_name : first name
    l_name : last name
    docstring test
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


