FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Reads the content of a text file and
    returns in a list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the content of a list
    to a text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return

if __name__ == "__main__":
    print("I am inside")