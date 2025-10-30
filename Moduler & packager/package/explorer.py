def explore_module(module_name):
    
    try:
        module = __import__(module_name)
        print(dir(module))
    except ModuleNotFoundError:
        print("Module not found!")