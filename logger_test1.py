import logging

logger = logging.getLogger(__name__)


def test1():
    logging.warning("warning")

    pass


def test2():
    logger.warning("waring")


if __name__ == '__main__':
    # test1()
    test2()
