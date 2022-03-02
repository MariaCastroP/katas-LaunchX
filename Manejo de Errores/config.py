def main():
    try:
        configuration = open('c:\Users\User\Desktop\LaunchX\CursoIntroPython-main\On Boarding\Manejo de Errores\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()