from typing import Union
# slider_spinbox_connections.py
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QLineEdit, QTimeEdit
from logger_setup import logger


def line_edit_times(line_edit: Union[QLineEdit, str], time_edit: Union[QTimeEdit, QTime]) -> None:
    """
    Connect the line_edit's textChanged signal to a lambda function that updates the time_edit

    :param line_edit: The QLineEdit object to connect the signal to
    :type line_edit: Union[QLineEdit, str]
    :param time_edit: The QTimeEdit object to update when the line_edit's text changes
    :type time_edit: Union[QTimeEdit, QTime]
    """
    try:
        if line_edit is not None and time_edit is not None:
            if isinstance(line_edit, QLineEdit) and isinstance(time_edit, QTimeEdit):
                line_edit.textChanged.connect(lambda: time_edit.setTime(QTime.currentTime()))
    except SpecificException as e:
        logger.error(f"An error occurred: {e}")

        