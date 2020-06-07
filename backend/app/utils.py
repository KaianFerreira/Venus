def extract(lst): 
    return [item[0] for item in lst] 

def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True

def row2dict(ret):
    if iterable(ret):
        posts_ret = [i.__dict__ for i in ret]
        [i.pop('_sa_instance_state',None) for i in posts_ret]
        [i.pop('password',None) for i in posts_ret]
        return posts_ret
    ret = ret.__dict__ 
    ret.pop('_sa_instance_state',None) 
    ret.pop('password',None) 
    return ret