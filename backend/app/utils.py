def extract(lst): 
    return [item[0] for item in lst] 

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        if column.name != 'password':
            d[column.name] = str(getattr(row, column.name))

    return d