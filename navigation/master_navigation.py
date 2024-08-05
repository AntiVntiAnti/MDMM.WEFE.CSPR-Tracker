# from sexy_logger import logger
from logger_setup import logger
from typing import Any


def change_mainStack(mainStack: Any, index: int) -> None:
    """
    Change the current index of the main stack.

    Args:
    mainStack (Any): The main stack object.
    index (int): The new index to set.

    Returns:
    None
    """
    try:
        mainStack.setCurrentIndex(index)
    except Exception as e:
        logger.error(f"main stack Page Change Error: {e}", exc_info=True)


