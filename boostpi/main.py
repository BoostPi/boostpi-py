"""_summary_
"""
from boostpi.logutils import logger
from boostpi.resources import warnings


def main():
    """_summary_"""
    logger.info("hello world, this will soon be boostpi")
    logger.warning(warnings.EULA_WARNING)
