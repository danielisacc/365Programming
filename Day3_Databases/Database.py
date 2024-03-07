import sqlite3

class Data:

    conn = sqlite3.connect('Creon_inc.db')
    c = conn.cursor()
    
    
    def __init__(self, first_name:str , last_name:str , age:int, 
                 pay:float, hours:float, position:str,hourly:bool = True,
                 pay_period:str = "bi-weekly", contract_length: int = 0, 
                 commission_pay:float = 0.0, comissions_made:int = 0,
                 base_pay:float = 0.0):
        
        pay_periods = {"weekly": 52,
                       "biweekly":26,
                       "monthly":12}
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hourly = hourly
        self.pay = pay
        self.hours = hours
        self.position = position

        self.pay_period = pay_periods[pay_period]
        self.contract_length = contract_length
        self.comission_pay = commission_pay
        self.comissions_made = comissions_made
        self.base_pay = base_pay

    def db_emp_table_create(self):
        try:
            self.c.execute("""
                           CREATE TABLE employees (
                           emp_ID INTEGER PRIMARY KEY,
                           first_name TEXT,
                           last_name TEXT,
                           age INTEGER,
                           position TEXT
                           )
            """)
            print(f"employee table was created")
        except sqlite3.DataError as DataError:
            print("employee table creation " +DataError)
        except sqlite3.ProgrammingError as ProgrammingError:
            print("employee table creation " +ProgrammingError)
        except sqlite3.Error as Error:
            print(f"employee table creation...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.with_traceback}")
    
    def db_emp_paytable_create(self):
        try:
            self.c.execute("""
                           CREATE TABLE emp_paytable (
                           emp_pay_ID INTEGER PRIMARY KEY,
                           is_hourly BOOLEAN,
                           pay REAL,
                           hours REAL,
                           pay_period INTEGER,
                           contract_length INTEGER,
                           base_pay REAL,
                           comission_pay REAL,
                           commissions_made INTEGER,
                           FOREIGN KEY(empIDFKEY) REFERENCE employees(empID)
                           )
                           """)
        except sqlite3.DataError as DataError:
            print("emp_payable table creation " +DataError)
        except sqlite3.ProgrammingError as ProgrammingError:
            print("emp_payable table creation " +ProgrammingError)
        except sqlite3.Error as Error:
            print(f"emp_payable table creation...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.with_traceback}")

    def commit(self):
        self.conn.commit()