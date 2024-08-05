from typing import List
from PyQt6.QtWidgets import QLineEdit
from logger_setup import logger


def calculate_calories(calories_values: List[int], total_calories_widget: QLineEdit) -> None:
    """
    Calculate the total calories and update the total_calories_widget with the result.

    Args:
    calories_values (List[int]): List of calorie values
    total_calories_widget (QLineEdit): Widget to display the total calories
    """
    try:
        total_calories = sum(calories_values)

        # Update the total_calories_widget with the total
        total_calories_widget.setText(str(total_calories))
    except Exception as e:
        logger.error(f"An error occurred while calculating calories: {e}")
