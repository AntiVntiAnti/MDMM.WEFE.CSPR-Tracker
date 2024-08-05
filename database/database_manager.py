# from sexy_logger import logger
import tracker_config as tkc
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import os
import shutil
from logger_setup import logger

user_dir = os.path.expanduser('~')
db_path = os.path.join(os.getcwd(), tkc.DB_NAME)  # Database Name
target_db_path = os.path.join(user_dir, tkc.DB_NAME)  # Database Name


def initialize_database():
    try:
        if not os.path.exists(target_db_path):
            if os.path.exists(db_path):
                shutil.copy(db_path, target_db_path)
            else:
                db = QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName(target_db_path)
                if not db.open():
                    logger.error("Error: Unable to create database")
                db.close()
    except Exception as e:
        logger.error("Error: Unable to create database", str(e))


class DataManager:
    
    def __init__(self,
                 db_name=target_db_path):
        try:
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(db_name)
            
            if not self.db.open():
                logger.error("Error: Unable to open database")
            logger.info("DB INITIALIZING")
            self.query = QSqlQuery()
            self.setup_tables()
        except Exception as e:
            logger.error(f"Error: Unable to open database {e}", exc_info=True)
    
    def setup_tables(self):
        self.setup_wefe_table()
        self.setup_into_cspr_exam()
        self.setup_mental_mental_table()
    
    def setup_mental_mental_table(self) -> None:
        """
        Sets up the 'mental_mental_table' in the database if it doesn't already exist.

        This method creates a table named 'mental_mental_table' in the database with the following columns:
        - id: INTEGER (Primary Key, Autoincrement)
        - mental_mental_date: TEXT
        - mental_mental_time: TEXT
        - mood_slider: INTEGER
        - mania_slider: INTEGER
        - depression_slider: INTEGER
        - mixed_risk_slider: INTEGER

        If the table already exists, this method does nothing.

        Returns:
            None
        """
        if not self.query.exec(f"""
                                    CREATE TABLE IF NOT EXISTS mental_mental_table (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    mental_mental_date TEXT,
                                    mental_mental_time TEXT,
                                    mood_slider INTEGER,
                                    mania_slider INTEGER,
                                    depression_slider INTEGER,
                                    mixed_risk_slider INTEGER
                                    )"""):
            logger.error(f"Error creating table: mental_mental_table",
                         self.query.lastError().text())
    
    def insert_into_mental_mental_table(self,
                                        mental_mental_date: int,
                                        mental_mental_time: int,
                                        mood_slider: int,
                                        mania_slider: int,
                                        depression_slider: int,
                                        mixed_risk_slider: int) -> None:
        """
        Inserts data into the mental_mental_table.

        Args:
            mental_mental_date (int): The date of the mental_mental record.
            mental_mental_time (int): The time of the mental_mental record.
            mood_slider (int): The value of the mood slider.
            mania_slider (int): The value of the mania slider.
            depression_slider (int): The value of the depression slider.
            mixed_risk_slider (int): The value of the mixed risk slider.

        Returns:
            None

        Raises:
            ValueError: If the number of bind values does not match the number of placeholders in the SQL query.
            Exception: If there is an error during data insertion.

        """
        sql: str = f"""INSERT INTO mental_mental_table(
                    mental_mental_date,
                    mental_mental_time,
                    mood_slider,
                    mania_slider,
                    depression_slider,
                    mixed_risk_slider) VALUES (?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [mental_mental_date, mental_mental_time,
                                              mood_slider, mania_slider, depression_slider,
                                              mixed_risk_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: mental_mental_table Expected {sql.count('?')}
                                bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: mental_mental_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError mental_mental_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: mental_mental_table {e}", exc_info=True)
    
    def setup_into_cspr_exam(self) -> None:
        if not self.query.exec(f"""
                                    CREATE TABLE IF NOT EXISTS cspr_table (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    cspr_date TEXT,
                                    cspr_time TEXT,
                                    calm_slider INTEGER,
                                    stress_slider INTEGER,
                                    pain_slider INTEGER,
                                    rage_slider INTEGER
                                    )"""):
            logger.error(f"Error creating table: cspr_table",
                         self.query.lastError().text())
    
    def insert_into_cspr_exam(self,
                              cspr_date: str,
                              cspr_time: str,
                              calm_slider: int,
                              stress_slider: int,
                              pain_slider: int,
                              rage_slider: int
                              ) -> None:
        
        sql: str = f"""INSERT INTO cspr_table(
                    cspr_date,
                    cspr_time,
                    calm_slider,
                    stress_slider,
                    pain_slider,
                    rage_slider) VALUES (?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [cspr_date, cspr_time,
                                              calm_slider, stress_slider, pain_slider, rage_slider]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: cspr_table Expected {sql.count('?')}
                                bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: cspr_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError cspr_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: cspr_table {e}", exc_info=True)
    
    def setup_wefe_table(self) -> None:
        if not self.query.exec(f"""
                                CREATE TABLE IF NOT EXISTS wefe_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                wefe_date TEXT,
                                wefe_time TEXT,
                                wellbeing_slider INTEGER,
                                excite_slider INTEGER,
                                focus_slider INTEGER,
                                energy_slider INTEGER,
                                summing_box INTEGER
                                )"""):
            logger.error(f"Error creating table: wefe_table",
                         self.query.lastError().text())
    
    def insert_into_wefe_table(self,
                               wefe_date: str,
                               wefe_time: str,
                               wellbeing_slider: int,
                               excite_slider: int,
                               focus_slider: int,
                               energy_slider: int,
                               summing_box: int
                               ) -> None:
        
        sql: str = f"""INSERT INTO wefe_table(
                wefe_date,
                wefe_time,
                wellbeing_slider,
                excite_slider,
                focus_slider,
                energy_slider,
                summing_box) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        bind_values: List[Union[str, int]] = [wefe_date,
                                              wefe_time,
                                              wellbeing_slider,
                                              excite_slider,
                                              focus_slider,
                                              energy_slider,
                                              summing_box]
        try:
            self.query.prepare(sql)
            for value in bind_values:
                self.query.addBindValue(value)
            if sql.count('?') != len(bind_values):
                raise ValueError(f"""Mismatch: wefe_table Expected {sql.count('?')}
                            bind values, got {len(bind_values)}.""")
            if not self.query.exec():
                logger.error(
                    f"Error inserting data: wefe_table - {self.query.lastError().text()}")
        except ValueError as e:
            logger.error(f"ValueError wefe_table: {e}")
        except Exception as e:
            logger.error(f"Error during data insertion: wefe_table {e}", exc_info=True)
    

def close_database(self):
    try:
        logger.info("if database is open")
        if self.db.isOpen():
            logger.info("the database is closed successfully")
            self.db.close()
    except Exception as e:
        logger.exception(f"Error closing database: {e}")
