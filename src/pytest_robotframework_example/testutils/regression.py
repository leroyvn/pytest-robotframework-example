from robot.api import logger


class RegressionTest:
    def run(self) -> bool:
        msg = "\n".join(
            ["Some regression test", "Passed"]
        )
        logger.info(msg, also_console=True)
        return True
