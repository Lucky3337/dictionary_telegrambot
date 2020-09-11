def singleton_class(cls):
    """The singleton decorator for class"""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance