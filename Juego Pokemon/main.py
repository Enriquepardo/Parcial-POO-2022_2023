



def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    

    # Get configuration for Game User 2.


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    

    # Choose first pokemons
 

    # Main loop.
    while True:
        print("------------------------------------------------------------------")
        print("Game User 1:")
        print("------------------------------------------------------------------")
        print("Choose an option:")
        print("1. Attack.")
        print("2. Change Pokemon.")
        print("3. End Game.")

        # Get option to execute.
        option = input("Option: ")
        option = int(option)

        # Attack.
        if option == 1:
            print("------------------------------------------------------------------")
            print("Game User 1:")
            print("------------------------------------------------------------------")
            print("Choose an option:")
            print("1. Puñetazo.")
            print("2. Patada.")
            print("3. Codazo.")
            print("4. Cabezazo.")

            # Get option to execute.
            option = input("Option: ")
            option = int(option)

            # Puñetazo.
            if option == 1:
                print("------------------------------------------------------------------")
                print("Game User 1:")
                print("------------------------------------------------------------------")
                print("Choose an option:")
                print("1. Attack.")
                print("2. Change Pokemon.")
                print("3. End Game.")

                # Get option to execute.
                option = input("Option: ")
                option = int(option)

                # Attack.
                if option == 1:
                    # Get a copy of the list of pokemons:
                    

                    # Choose first pokemons
                    
                    # Main loop.
                    while True:
                        print("------------------------------------------------------------------")
                        print("Game User 1:")
                        print("------------------------------------------------------------------")
                        print("Choose an option:")
                        print("1. Attack.")
                        print("2. Change Pokemon.")
                        print("3. End Game.")

                        # Get option to execute.
                        option = input("Option: ")
                        option = int(option)

                        # Attack.
                        if option == 1:
                            print("------------------------------------------------------------------")
                            print("Game User 1:")
                            print("------------------------------------------------------------------")
                            print("Choose an option:")
                            print("1. Puñetazo.")
                            print("2. Patada.")
                            print("3. Codazo.")
                            print("4. Cabezazo.")

                            # Get option to execute.
                            option = input("Option: ")
                            option = int(option)

                            # Puñetazo.
                            if option == 1:
                                print("------------------------------------------------------------------")
                                print("Game User 1:")
                                print("------------------------------------------------------------------")
                                print('Choose an')

    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
