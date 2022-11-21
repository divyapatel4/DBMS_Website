def CheckLogin(User_ID, Password):
    if User_ID == 'admin' and Password == 'admin':
        return True
    else:
        return False

def CheckQuery(table, Type_of_Query, Args):
    if len(table) == 0: return False
    if len(Type_of_Query)==1:
        if Type_of_Query=='Insert':
            if len(table)==1:
                return True
            else:
                return False
        elif Type_of_Query=='Delete':
            if len(table)==1:
                return True
            else:
                return False
        else:
            return True
    else:
        return False