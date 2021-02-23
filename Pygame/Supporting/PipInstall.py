import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    install('pygame==2.0.0.dev6')
    install('mysql-connector')
    install('tkinter')
    install('pil')
