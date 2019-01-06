#####################################################################################
#
#   Project name:   USEQ
#       Searching for unique sequences of an organism genome
#       based on sequence comparision.
#   
#   Module for sequence manipulation.
#
#   Author:     Javier Montalvo-Arredondo.
#   Contact:    Biotechnology division at Universidad Autonoma Agraria Antonio Narro
#               Sendero a la Narro, San Buenavista, Saltillo, Coahuila, Mexico.
#               email: buitrejma@gmail.com
#
#####################################################################################
#
#   TASKS
#   
#   o   Load sequences.
#   o   Transfrom sequences.
#
###################################

from sys import argv, exit

#############################
#///////////////////////////#
#           OBJECTS         #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#############################



class SEQUENCE(object):
    """
        This object is dedicated to store a sequence and its name
        and its sequence type.
        This object contains the following methods:
        o   name
        o   sequence
        o   sequence_type
        o   write_to_file
    """
    #   [DEBUGING] - [WARNING!] - CHANGE THE VARIABLE "name" NAME
    name = None
    sequence = None
    sequence_type = None
    leng = None
    #   [TESTING] - [OK]
    def __init__(self, name, sequence, sequence_type="dna"):
        """
            Initialiser for SEQUENCE object
        """
        self.name = name
        self.sequence = sequence
        self.sequence_type = sequence_type
        self.leng = len(self.sequence)

    #   [TESTING] - [OK]
    def __str__(self, ranges=None):
        """
            Prints out the object content.
            Requires ranges; an integer vector of ranges of sequence
            to be printed out to screen.
        """
        if ranges == None:
            ranges = [0, self.leng]
        return "[PRINTING SEQUENCE OBJECT] - "\
                + self.name\
                + "\n"\
                + self.sequence[ranges[0] : ranges[1]]\
                + "\n"\
                + "This sequence is of "\
                + self.sequence_type\
                + " type"\
                + "\n"
    #   [DEBUGGING] - [WARNING!] -  CHANGE THE NAME OF THE FUNCTION OR
    #                               CHANGE THE NAME OF SELF.NAME
    def name(self):
        """
            Returns the name of the SEQUENCE object
        """
        return self.name

    def sequence(self, ranges=None):
        """
            Returns the sequence of the SEQUENCE object.
            Requires ranges; an integer vector of ranges of sequence
            to be printed out to screen.
        """
        if ranges == None:
            ranges = [0, self.leng]
        elif max(ranges) > self.leng:
            return "[ERROR!] - Index out of range"
        elif min(ranges) < 0:
            return "[ERROR!] - Index out of range"
        else:
            return self.sequence[ranges[0]:ranges[1]]

    def sequence_type(self):
        """
            Returns the sequence type
        """
        return self.sequence_type

    #   [TESTING] - [OK]
    def length(self):
        """
            Returns the sequence length
        """
        return self.leng

    #   [TESTING] - []
    def write_to_file(self, filename):
        """
            Writes the SEQUENCE Object to an output file.
            Requires the full name of the output file.
        """
        FHOUT = open(filename, "w+")
        string_out = ">" + self.name + "|" + self.type + "\n" + self.sequence
        FHOUT.write(string_out)
        FHOUT.close()


class SEQ_CONTAINER(object):
    """
        This container object is dedicated to store SEQUENCE objects and
        contains the following methods:
            1 add_last.
            2 add_first.
            3 add_in.
            4 length.
            The first three methods are used to add items in container.
            The last method is used to return the length of the container.

            Creates an SEQUENCE CONTAINER object.
            myContainer = SEQ_CONTAINER(name, first_item).
            If first_item is None, it creates an empty object.
            if not, initialiser adds the first item to the array.

    """
    name = None
    counter = None
    leng = None
    sequences = None

    #   [TESTING] - [OK]
    def __init__(self, name, item=None):
        """
            Initialiser for a SEQUENCE CONTAINER.
        """
        self.name = name
        self.counter = 0
        if item == None:
            self.sequences = []
            self.leng = len(self.sequences)
        else:
            self.add_last(item)

    #   [TESTING] - [OK]
    def __str__(self):
        """
            prints to screen SEQUENCE CONTAINER information.
        """
        return "[PRINTING SEQUENCE CONTAINER] - "\
                + self.name\
                + "\n"\
                + "It contains "\
                + str(self.leng)\
                + " SEQUENCE object."\
                + "\n"

    #   [TETING] - [OK]   
    def add_last(self, item):
        """
            Adds an item at the last position.
        """
        self.sequences.extend(item)
        self.leng = len(self.sequences)

    #   [TESTING] - [OK]
    def add_first(self, item):
        """
            Adds an item at the first position.

        """
        item.extend(self.sequences)
        self.sequences = item
        self.leng = len(self.sequences)

    #   [TESTING] - []
    def add_in(self, item, index):
        """
            Adds an item at an index position.
        """
        first = self.sequences[:index]
        second = self.sequences[index:]
        self.sequences = first.extend([item].extend(second))
        self.leng = len(self.sequences)

    #   [TESTING] - [OK]    
    def length(self):
        """
            Returns the length of the SEQUENCE CONTAINER.
        """
        return self.leng

    #   [TESTING] - [OK]
    def next(self):
        """
            Returns the next element of the container.
            If it is the first time, it returns the first
            element, if not, it returns the element which
            index is stored at a counter.
        """
        if self.counter == self.leng:
            self.clear()
            self.counter += 1
            return self.sequences[self.counter-1]
        else:
            self.counter += 1
            return self.sequences[self.counter-1]
    
    # [TESTING] - [OK]
    def next_at(self, index):
        """
            Returns an item of the container at specified index.
            [WARNING!] - It does not modify internal counter.
            Requires an index
        """
        if index == self.leng or index < 0:
            return "[ERROR!] - Index out of range."
        else:
            return self.sequences[index]
    
    #    [TESTING] - [OK]
    def get_position(self):
        """
            Returns the position of iteration along container
        """
        return self.counter
    
    #   [TESTING] - [OK]
    def clear(self):
        """
            Clears the counter and next method starts from the
            begining.
        """
        self.counter = 0

