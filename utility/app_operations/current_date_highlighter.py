from PyQt6.QtWidgets import QDateEdit
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QDate
import tracker_config as tkc
from typing import Dict
from logger_setup import logger


class DateHighlighter:
    def __init__(self, date_widgets: Dict) -> None:
        """
        Initializes the DateHighlighter with a dictionary of QDateEdit widgets.
        :param date_widgets: A dictionary of QDateEdit widgets with keys like
        'sun_date', 'mon_date', etc.
        """
        self.date_widgets = date_widgets
        self.current_date = QDate.currentDate()
        self.update_date_styles()

    def update_date_styles(self) -> None:
        """
        Updates the style of the QDateEdit widgets based on the current date.
        """
        try:
            for day, widget in self.date_widgets.items():
                if widget.date() == self.current_date:
                    self.highlight_current_date(widget)
                else:
                    self.normalize_date(widget)
        except Exception as e:
            logger.error(f"An error occurred while updating date styles: {e}")

    @staticmethod
    def highlight_current_date(widget: QDateEdit) -> None:
        """
        Applies the highlight style to the current date widget.
        :param widget: The QDateEdit widget to be highlighted.
        """
        try:
            font = QFont()
            widget.setFont(font)
            widget.setStyleSheet(tkc.COLOR)
        except Exception as e:
            logger.error(f"An error occurred while highlighting the current date: {e}")

    @staticmethod
    def normalize_date(widget: QDateEdit) -> None:
        """
        Applies the normal style to non-current date widgets.
        :param widget: The QDateEdit widget to be normalized.
        """
        try:
            font = QFont()
            font.setBold(False)
            widget.setFont(font)
            widget.setStyleSheet(tkc.STYLESHEET)
        except Exception as e:
            logger.error(f"An error occurred while normalizing the date: {e}")
