def token(file_name:str='token.txt'):
    with open(file_name) as f:
        return f.readline().rstrip()