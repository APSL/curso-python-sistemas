import logging
from logging.handlers import SysLogHandler
from decouple import config

DEBUG=config("DEBUG", False)
#PAPERTRAIL_HOST=("PAPERTRAIL_HOST")
#PAPERTRAIL_PORT=("PAPERTRAIL_PORT")

logging.basicConfig(
    filename="app.log",
    format="[%(asctime)s] %(levelname)s %(name)s:  %(message)s",
    level=logging.DEBUG if debug else logging.INFO
)
#syslog = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
#syslog.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'))

log = logging.getLogger(__name__)
#log.addHandler(syslog)

def main():
    log.error("Error")
    log.info("Info")
    log.debug("Debug")
    logging.error("Error directo logging")

if __name__ == "__main__":
    main()

