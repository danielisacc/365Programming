import sqlite3

class Data:
    employee_id = 0

    pay_periods = { "weekly": 52,
                    "biweekly":26,
                    "monthly":12}

    conn = sqlite3.connect('Creon_inc.db')
    c = conn.cursor()
    
    
    def __init__(self, first_name:str , last_name:str , age:int, 
                 pay:float, hours:float, position:str,hourly:bool = True,
                 pay_period:str = "biweekly", contract_length: int = 0, 
                 commission_pay:float = 0.0, commissions_made:int = 0,
                 base_pay:float = 0.0):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pay = pay
        self.hours = hours
        self.position = position

        self.pay_period = Data.pay_periods[pay_period]
        self.contract_length = contract_length
        self.commission_pay = commission_pay
        self.commissions_made = commissions_made
        self.base_pay = base_pay

        if hourly: self.hourly = 1
        else: self.hourly = 0 

        Data.employee_id += 1
        self.employee_id = Data.employee_id

    def employee_tables_creation(self):
        try:
            self.c.execute("""
                           CREATE TABLE IF NOT EXISTS employees (
                           emp_ID INTEGER PRIMARY KEY,
                           first_name TEXT,
                           last_name TEXT,
                           age INTEGER,
                           position TEXT
                           )
            """)
        except sqlite3.DataError as DataError:
            print("employee table creation " +DataError)
        except sqlite3.ProgrammingError as ProgrammingError:
            print("employee table creation " +ProgrammingError)
        except sqlite3.Error as Error:
            print(f"employee table creation...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.with_traceback}")


        else:
            print("Employee table created Successfully!")
            try:
                self.c.execute("""
                               CREATE TABLE IF NOT EXISTS emp_paytable (
                               emp_pay_ID INTEGER PRIMARY KEY,
                               is_hourly INTEGER,
                               pay REAL,
                               hours REAL,
                               pay_period INTEGER,
                               contract_length INTEGER,
                               base_pay REAL,
                               commission_pay REAL,
                               commissions_made INTEGER,
                               empIDFK INTEGER,
                               FOREIGN KEY(empIDFK) REFERENCES employees(empID)
                               )
                               """)
            except sqlite3.DataError as DataError:
                print("emp_payable table creation " +DataError)
            except sqlite3.ProgrammingError as ProgrammingError:
                print("emp_payable table creation " +ProgrammingError)
            except sqlite3.Error as Error:
                print(f"emp_payable table creation...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.with_traceback}")
            else:
                print("Employee Paytable created Successfully!")
    
    def insert_emp(self):
        try:
            self.c.execute(f"""
                        INSERT INTO employees
                        (emp_ID, first_name,last_name,age,position)
                        VALUES({self.employee_id},'{self.first_name}',
                        '{self.last_name}',{self.age},'{self.position}')
                        """)
            
        except sqlite3.DataError as DataError:
            print("employee row " +DataError)
        except sqlite3.ProgrammingError as ProgrammingError:
            print("employee row " +ProgrammingError)
        except sqlite3.Error as Error:
            print(f"employee row...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.with_traceback}")
        else:
            print(f"Employee {self.first_name} {self.last_name} created Successfully!")

            try:
                self.c.execute(f"""
                             INSERT INTO emp_paytable
                             (is_hourly,pay,hours,pay_period,contract_length,
                             base_pay,commission_pay,commissions_made,empIDFK)
                             VALUES
                             ({self.hourly},{self.pay}, {self.hours},
                             {self.pay_period},{self.contract_length},{self.base_pay},
                             {self.commission_pay},{self.commissions_made},{self.employee_id})
                            """)

            except sqlite3.DataError as DataError:
                print("emp_paytable row " +DataError)
            except sqlite3.ProgrammingError as ProgrammingError:
                print("emp_paytable row " +ProgrammingError)
            except sqlite3.Error as Error:
                print(f"emp_paytable row...ErrorCode: {Error.sqlite_errorcode}, ErorrName: {Error.sqlite_errorname}\n{Error.__cause__}")
            else:
                print(f"Employee {self.first_name} {self.last_name} added to emp_table Successfully!")
    
    def __str__(self) -> str:
        self.c.execute(f"""SELECT emp_ID, first_name, last_name, age, position,
                                  is_hourly,pay,hours,pay_period,contract_length,
                                  base_pay,commission_pay,commissions_made,empIDFK
                            FROM employees INNER JOIN emp_paytable
                            ON employees.emp_ID = emp_paytable.empIDFK
                            WHERE employees.emp_ID = {self.employee_id}
                        """)
        emp_fetched = self.c.fetchone()
        return f"\n\t\temployee ID: {emp_fetched[0]}\n\
                first name:  {emp_fetched[1]}\n\
                last name:   {emp_fetched[2]}\n\
                age:         {emp_fetched[3]}\n\
                is hourly:   {emp_fetched[4]}\n\
                pay:         {emp_fetched[5]}\n\
                hours:       {emp_fetched[6]}\n\
                position:    {emp_fetched[7]}\n"

    def commit(self):
        self.conn.commit()