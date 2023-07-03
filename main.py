# coding=utf-8
import logging
import queue
from logging import handlers

from service.service import Service
from service.mointor import Monitor
from config.config import Config
import spider.spider_init
from service.statistical import Statistical

if __name__ == "__main__":
    print(Config.get())
    print(Config.get())

    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    fmt = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s"

    file_handler = handlers.TimedRotatingFileHandler(
        filename="log/spider.log", when="D", interval=1, backupCount=14
    )

    file_handler.setFormatter(logging.Formatter(fmt))
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    if Config.env() == "test" or Config.env() == "dev":
        pass
        # console_handler.setLevel(logging.DEBUG)
    else:
        pass
        # console_handler.setLevel(logging.ERROR)

    console_handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(console_handler)

    logging.info("start spider ....")
    logging.info("Good luck with you")

    q = queue.Queue(5)

    service = Service(q)
    monitor = Monitor(q)

    stistic = Statistical()

    monitor.start()
    service.start()
    stistic.start()

    service.join()
    monitor.join()
    stistic.join()
