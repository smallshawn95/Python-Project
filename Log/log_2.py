import logging

logger = logging.getLogger(name = "logger")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setFormatter(logging.Formatter("[%(asctime)s]-[%(filename)s %(lineno)d]-[%(levelname)-8s] %(message)s", datefmt = "%Y/%m/%d %H:%M:%S"))

file = logging.FileHandler(filename = "./Log/log.log", encoding = "utf8")
file.setFormatter(logging.Formatter("[%(asctime)s]-[%(filename)s %(lineno)d]-[%(levelname)-8s] %(message)s", datefmt = "%Y/%m/%d %H:%M:%S"))

logger.addHandler(console)
logger.addHandler(file)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
