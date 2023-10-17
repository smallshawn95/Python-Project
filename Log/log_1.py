import logging

logging.basicConfig(
    level = logging.DEBUG,
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler("log.log")
    ],
    format = "[%(asctime)s]-[%(filename)s %(lineno)d]-[%(levelname)-8s] %(message)s",
    datefmt = "%Y/%m/%d %H:%M:%S",
    encoding = "utf8"
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
