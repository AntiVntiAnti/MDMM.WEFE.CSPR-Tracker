from PyQt6.QtCore import QDate, QTime
import tracker_config as tkc
from logger_setup import logger


def add_wefe_data(main_window_instance, widget_names, db_insert_method):
    widget_methods = {
        widget_names['wefe_date']: (None, 'date', "yyyy-MM-dd"),
        widget_names['wefe_time']: (None, 'time', "hh:mm:ss"),
        widget_names['wellbeing_slider']: (None, 'value', None),
        widget_names['excite_slider']: (None, 'value', None),
        widget_names['focus_slider']: (None, 'value', None),
        widget_names['energy_slider']: (None, 'value', None),
        widget_names['summing_box']: (None, 'value', None),
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
        reset_wefe_data(main_window_instance, widget_names)
    except Exception as e:
        logger.error(f"Error inserting data into the database: {e}")


def reset_wefe_data(main_window_instance, widget_names):
    try:
        getattr(main_window_instance, widget_names['wefe_date']).setDate(QDate.currentDate())
        getattr(main_window_instance, widget_names['wefe_time']).setTime(QTime.currentTime())
        getattr(main_window_instance, widget_names['wellbeing_slider']).setValue(0)
        getattr(main_window_instance, widget_names['excite_slider']).setValue(0)
        getattr(main_window_instance, widget_names['focus_slider']).setValue(0)
        getattr(main_window_instance, widget_names['energy_slider']).setValue(0)
        getattr(main_window_instance, widget_names['summing_box']).setValue(0)
        getattr(main_window_instance, widget_names['model']).select()
    except Exception as e:
        logger.error(f"Error resetting pain levels form: {e}")
