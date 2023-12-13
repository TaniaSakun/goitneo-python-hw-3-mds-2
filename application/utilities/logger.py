import logging
import colorlog

# This functionality is used to make a UI output more interactive and meaningful

handler = colorlog.StreamHandler()
    
handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(message)s",
            log_colors = {
                "INFO": "green", 
                "WARNING": "yellow", 
                "ERROR": "red"
            },
        )
    )

logger_instance = colorlog.getLogger() 
logger_instance.addHandler(handler)
logger_instance.setLevel(logging.DEBUG)
