import logging
from logging.handlers import SysLogHandler
from decouple import config

debug=config("DEBUG", False)

logging.basicConfig(
    #filename="app.log",
    format="[%(asctime)s] %(levelname)s %(name)s:  %(message)s",
    level=logging.DEBUG if debug else logging.INFO
)
#syslog = SysLogHandler(address=('logs4.papertrailapp.com', 46006))

log = logging.getLogger(__name__)
#log.addHandler(syslog)

def main():
    log.error("Error")
    log.info("Info")
    log.debug("Debug")

if __name__ == "__main__":
    main()

