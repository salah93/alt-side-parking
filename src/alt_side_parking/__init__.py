from importlib.metadata import version

from .feed import is_suspended_today
from .sms import send_reminder

__version__ = version("wheel")

remind_me = send_reminder
we_not_good = lambda: not is_suspended_today()
