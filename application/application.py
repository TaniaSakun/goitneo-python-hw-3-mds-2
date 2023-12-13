from application.bot.handler import get_handler
from application.utilities.constants import Constants
from application.utilities.logger import logger_instance
from application.utilities.objects import AddressBook

class Application:
    
    def bot_task(self):
        contacts = AddressBook()

        while True:
            logger_instance.info(f"\n" + Constants.enter_command)
            user_input = input()

            result = get_handler(user_input, contacts)
            if not result:
                logger_instance.warn(Constants.good_bye_message)
                break
            logger_instance.warn(result)
        return self