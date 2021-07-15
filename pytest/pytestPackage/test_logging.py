import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('log_file.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.ERROR)
    logger.debug("Debug statement is executed")
    logger.info("Pytest information is shown")
    logger.warning("Pytest warning is shown")
    logger.error("Pytest error found")
    logger.critical("Pytest critical issue found")
