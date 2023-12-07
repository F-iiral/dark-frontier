import datetime

class ConsoleShortcuts():
    def log():   return f"{Colors.MAGENTA}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE}"
    def ok():    return f"{Colors.GREEN}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE}"
    def warn():  return f"{Colors.YELLOW}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE}"
    def error(): return f"{Colors.RED}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}]{Colors.WHITE}"

class Colors():
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"