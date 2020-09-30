def get_absolute_url(required, *args, **kwargs):
    """Формирование url адреса из переданного домена и параметров
    :param required: обязательный аргумент
    :param *args: позиционные аргументы
    :param *kwargs: именованные аргументы
    """
    url_string = ''
    # Формирование строки до '?' включительно, использование метода join с итерированием элементов args
    url_string += (required + '/' + '/'.join(i for i in args) + '?')
    # Формирование строки c присоединением именнованых аргументов 
    for k, v in kwargs.items():
        url_string += (k + '=' + v + '&')
    #Возвращение строки без последнего '&'
    return(url_string[:-1])   
    
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))