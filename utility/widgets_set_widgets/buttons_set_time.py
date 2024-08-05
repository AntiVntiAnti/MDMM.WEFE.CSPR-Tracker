from typing import Optional
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QPushButton, QTimeEdit
from logger_setup import logger


def btn_times(app_btns: Optional[QPushButton], times_edit: Optional[QTimeEdit]) -> bool:
    """
    Method for Lily's Walk and Diet mods wherein when said QPushButtons are pressed they also
    set the time of the timeEdit widgets respectively.

    :param app_btns: The QPushButton object.
    :param times_edit: The QTimeEdit object.
    :return: True if the operation was successful, False otherwise.
    """
    try:
        if app_btns is None or not isinstance(app_btns, QPushButton) or times_edit is None or not isinstance(
            times_edit,
            QTimeEdit
                ):
            return False
        app_btns.clicked.connect(lambda: times_edit.setTime(QTime.currentTime()))
        return True
    except Exception as e:
        logger.error(f"{app_btns} unable to set {times_edit}, {type(e).__name__}: {str(e)}", exc_info=True)
        return False
