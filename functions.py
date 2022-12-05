
def write_todos(todos_arg, filepath='todos.txt'):
    """ Write the to-dos in the text file """
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todos_arg)


def get_todos(filepath='todos.txt'):
    """ Read the text files and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
