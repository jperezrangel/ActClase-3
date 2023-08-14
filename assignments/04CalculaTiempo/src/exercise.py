def main():
    edad=int(input('Dame tu edad: \n'))
    año=int(input('Dame el año actual: \n'))

    cien=int(año+(100-edad))

    print('Cumplirás 100 años en el',cien)
    
if __name__ == '__main__':
    main()
