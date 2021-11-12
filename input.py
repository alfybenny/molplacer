
class input:
    
    # The filetype could be .xyz, .mol2, .cif etc.
    def __init__(self, filetype):
        self.filetype = filetype

    def readfile(filename)
            # This could also be a virtual function
            # NOTE: To use the attribute defined above (constructor), we can use self.filetype here
            # Read the filename with corresponding filetype attribute
            # Do something with the read matrix based on the filetype attribute
            # Retuen the atom list and coordinates

class xyz(input):

    # Check if input is xyz
    # If yes, proceed with the function

    def readfile(filename):
        # Extract date

class mol2(input):


class cif(input):

