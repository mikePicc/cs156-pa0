
def check_prime(num: int) -> bool:
    """A function to check if a given number is a prime number. If the input is a prime, it returns True; otherwise, False.

    Args:
        num (int): An input (natural number) integer
    
    Raises:
        TypeError: if the input num is not an integer
        ValueError: if the num is not a natural number

    Returns:
        bool: True if the input number is a prime
    """
    pass


def divide(num: float, denom: float) -> float:
    """A division function

    Args:
        num (float): a numerator
        denom (float): a denominator (cannot be zero.)
    
    Raises:
        ValueError: if the denominator is 0.

    Returns:
        float: the quotient
    """
    pass



class Student:
    def __init__(self, first: str, last: str, id: int) -> None:
        """Initialize a student instance with first name, last name and a student id.

        Args:
            first (str): first name
            last (str): last name
            id (int): student id (5 digits)

        Raises:
            ValueError: if the input id is not 5 digit-length, raise a value error.
        """
        pass

    def fullname(self) -> str:
        """ returns a full name first_name(space)last_name
        """
        pass
    
    def admission_yr(self) -> int:
        """returns the admission year (first two digits of the student ID)

        Returns:
            int: two digits representing a year like 22
        """
        # Hint: Use a string slice in Python by converting the int student id to a string
        pass
