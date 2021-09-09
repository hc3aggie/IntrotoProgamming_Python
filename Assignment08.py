# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <HChisolm>,<09/06/2021>,Modified code to complete assignment 8
# Script to store product and price information
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <HChisolm>,<9/07/2021>,Modified code to complete assignment 8
    """
    # ------- Constructor -----------
    def __init__(self, product_name: str, product_price: float):
        # ------- Attributes
        self.__product_name = ""
        self.__product_price = ""
        try:
            self.product_name = str(product_name)
            self.product_price = float(product_price)
        except Exception as e:
            raise Exception

# Name
    # Getter
    @property
    def product_name(self):
         return str(self.__product_name)
    # Setter
    @product_name.setter
    def product_name(self, value: str):
        self.__product_name = value
# Price
    # Getter
    @property
    def product_price(self):
        return float(self.__product_price)
    # Setter
    @product_price.setter
    def product_price(self, value: float):
        self.__product_price = float(value)
    # ------- Method ______________
    def __str__(self):
        return self.product_name + " , " + str(self.product_price)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <HChisolm>,<09/07/2021>,Modified code to complete assignment 8
    """
    # -------Read --------process data from a file
    def read_data_from_file(file_name: str):
        """ Reads all string data from a file

        :param file_name: (string) with name of file
        :return: (list) of product objects
        """
        product_list = []
        file = open (file_name, "r")
        try:
            for line in file:
                lstdata = line.split(" , ")
                lstrow = Product(lstdata[0], lstdata[1])
                product_list.append(lstrow)
            file.close()
        except:
            print("No File Found")
        return product_list
    # -------Save -----process data to file
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data to a file from a list of product objects

               :param list_of_product_objects (list of objects)
               :param file_name: (string) with name of file
               :return: nothing
               """
        objFile = open(file_name, "w")
        for row in list_of_product_objects:
            objFile.write(str(row) + "\n")
        objFile.close()
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    # Add code to show menu to user
    @staticmethod
    def print_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View existing List
        2) Add a new Product
        3) Save Data to File        
        4) Exit 
        ''')
        print()  # Add an extra line for looks

    # Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # Add code to show the current data from the file to user
    @staticmethod
    def print_current_product_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products List is: *******")
        for row in list_of_rows:
            print(row.product_name + " , " + str(row.product_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    # Add code to get product data from user
    @staticmethod
    def input_add_new_product_and_price():
        # return name and price
        name = str(input("Enter the Name of Product:"))
        price = float(input("Enter the Price of Product:"))
        product_info = Product(product_name= name, product_price= price)
        return product_info

# Presentation (Input/Output)  -------------------------------------------- #

# ---------- Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
# Show user a menu of options
while True:
    IO.print_menu_options()
    # Get user's menu option choice
    option = IO.input_menu_choice()
    # Show user current data in the list of product objects
    if option == "1":
        IO.print_current_product_list(lstOfProductObjects)
    # Let user add data to the list of product objects
    elif option == "2":
        IO.input_add_new_product_and_price()
     # let user save current data to file and exit program
    elif option == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Data Saved")
    elif option == "4":
        print ("Exit Program")
        break

# Main Body of Script  ---------------------------------------------------- #
