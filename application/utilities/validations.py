from functools import wraps
from application.utilities.constants import (Constants, InvalidBirthdayError, InvalidNameError, 
                                             InvalidPhoneError, InvalidPhoneLengthError)

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Constants.invalid_input
        except KeyError:
            return Constants.contact_not_exist
        except IndexError:
            return Constants.invalid_parameters
        except FileNotFoundError:
            return Constants.file_not_found
        except EOFError:
            return Constants.eof_error
        except InvalidBirthdayError:
            return Constants.invalid_birthday
        except InvalidPhoneLengthError:
            return Constants.phone_number_length
        except InvalidPhoneError:
            return Constants.phone_number_value
        except InvalidNameError:
            return Constants.invalid_name
        except Exception as mein:
            return Constants.invalid_command

    return inner