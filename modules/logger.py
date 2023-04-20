import logging
from .formatter import Colorate, Colors

class liftloghandler(logging.Handler):
    def emit(self, record):
        level = record.levelname.lower()
        msg = record.getMessage()
        color = Colors.green_to_yellow if level == 'warning' else Colors.red_to_yellow if level == 'error' or level == 'critical' else Colors.white_to_blue
        log_msg = f"{Colorate.Horizontal(color, msg)}"
        print(log_msg)