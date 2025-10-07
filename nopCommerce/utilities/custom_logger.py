import logging

from openpyxl import DEBUG


class Log_Maker:
    @staticmethod
    def log_gem():
        logging.basicConfig(filename=".\\logs\\nopcommerce.log",filemode='a',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
