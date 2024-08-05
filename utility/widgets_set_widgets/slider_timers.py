from PyQt6.QtWidgets import QSlider, QTimeEdit
from PyQt6.QtCore import QTime
from logger_setup import logger


def connect_slider_timeedits(slider: QSlider, time_edit: QTimeEdit) -> None:
    """
    So that when the sliders value is changed the respective QTimeEdit widget i.e.,
    wellbeing_rate_timer(1-8)
    pain_rate_timer(1-8)
    will be automatically set to the current time

    Parameters:
        slider (QSlider): The slider object.
        time_edit (QtimeEdit): The time_edit object.

    Returns:
        None
    """
    try:
        if slider is not None and time_edit is not None:
            if isinstance(slider, QSlider) and isinstance(time_edit, QTimeEdit):
                # Connect the slider's valueChanged signal to the time_edit's setTime slot
                slider.valueChanged.connect(lambda: time_edit.setTime(QTime.currentTime()))
    except Exception as e:
        logger.error(f"Error Setting Wellbeing and Pain Rating Timers! {e}", exc_info=True)
