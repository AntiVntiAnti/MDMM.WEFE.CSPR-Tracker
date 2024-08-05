from PyQt6.QtCore import QDate, QTime
import tracker_config as tkc
from logger_setup import logger


def add_mentalsolo_data(main_window_instance, widget_names, db_insert_method):
    """
    Add mental solo data to the database.

    Args:
        main_window_instance: The instance of the main window.
        widget_names: A dictionary containing the names of the widgets.
        db_insert_method: The method used to insert data into the database.

    Returns:
        None
    """
    widget_methods = {
        widget_names['mental_mental_date']: (None, 'date', "yyyy-MM-dd"),
        widget_names['mental_mental_time']: (None, 'time', "hh:mm:ss"),
        widget_names['mood_slider']: (None, 'value', None),
        widget_names['mania_slider']: (None, 'value', None),
        widget_names['depression_slider']: (None, 'value', None),
        widget_names['mixed_risk_slider']: (None, 'value', None),        
    }

    data_to_insert = []
    for widget_name, (widget_attr, method, format_type) in widget_methods.items():
        widget = getattr(main_window_instance, widget_name)
        try:
            value = getattr(widget, method)()
            if format_type:
                value = value.toString(format_type)
            data_to_insert.append(value)
        except Exception as e:
            logger.error(f"Error getting value from widget {widget_name}: {e}")

    try:
        db_insert_method(*data_to_insert)
        reset_mental_mental(main_window_instance, widget_names)
    except Exception as e:
        logger.error(f"Error inserting data into the database: {e}")


def reset_mental_mental(main_window_instance, widget_names):
    """
    Reset the values of the mental_mental form in the main window.

    Args:
        main_window_instance: An instance of the main window.
        widget_names: A dictionary containing the names of the widgets used in the mental_mental form.

    Raises:
        Exception: If there is an error resetting the form.

    Returns:
        None
    """
    try:
        getattr(main_window_instance, widget_names['mental_mental_date']).setDate(QDate.currentDate())
        getattr(main_window_instance, widget_names['mental_mental_time']).setTime(QTime.currentTime())
        getattr(main_window_instance, widget_names['mood_slider']).setValue(0)
        getattr(main_window_instance, widget_names['mania_slider']).setValue(0)
        getattr(main_window_instance, widget_names['depression_slider']).setValue(0)
        getattr(main_window_instance, widget_names['mixed_risk_slider']).setValue(0)
        getattr(main_window_instance, widget_names['model']).select()
    except Exception as e:
        logger.error(f"Error resetting pain levels form: {e}")
