import logging

logger = logging.getLogger(__name__)


class Test:
    def test1(self):
        logger.warning("warning")

        pass

    pass


if __name__ == '__main__':
    test = Test()
    test.test1()
