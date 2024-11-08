import inspect

def introspection_info(obj):
    info = {
        'Тип объекта': type(obj).__name__,
        'Атрибуты объекта': [],
        'Методы объекта': [],
        'Модуль': []
    }

    for name in dir(obj):
        if callable(getattr(obj, name)):
            info['Методы объекта'].append(name)
        else:
            info['Атрибуты объекта'].append(name)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info['Модуль'] = __name__
    else:
        info['Модуль'] = obj_module.__name__
    
    return info
    

number_info = introspection_info(42)
print(number_info)
string_info = introspection_info('Hello World!')
print(string_info)
