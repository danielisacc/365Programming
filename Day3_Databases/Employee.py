#Employee classes and how they are paid
class Employee:

    pay_periods = {"weekly": 52,
                  "biweekly":26,
                  "monthly":12}

    def __init__(self, first_name:str , last_name:str , age:int, 
                 pay:float, hours:float, position:str,hourly:bool = True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hourly = hourly
        self.pay = pay
        self.hours = hours
        self.position = position

    def calc_payment(self) -> float:
        if self.hourly: 
            self.payment = self.pay*self.hours
            return self.payment
        else: 
            self.payment = self.pay
            return self.payment

    def __str__(self) -> str:
        self.calc_payment()
        return f"\t\tfirst name:  {self.first_name}\n\
                last name:   {self.last_name}\n\
                age:         {self.age}\n\
                is hourly:   {self.hourly}\n\
                pay:         {self.pay}\n\
                hours:       {self.hours}\n\
                position:    {self.position}\n\
                payment:     {self.payment}"

    def emp_get(self):
        return {"first_name":self.first_name,
                "last_name":self.last_name,
                "age":self.age,
                "hourly":self.hourly,
                "pay":self.pay,
                "hours":self.hours,
                "position":self.position,
                "payment":self.payment}
    
class HourlyWorker(Employee):

    def __init__(self, first_name: str, last_name: str, age: int,
                 pay: float, hours: float, position: str, hourly: bool = True):
        super().__init__(first_name, last_name, age, pay, hours, position, hourly)

    def calc_payment(self) -> float:
        return self.pay*self.hours

class SalaryWorker(Employee):

    def __init__(self, first_name: str, last_name: str, 
                 age: int, pay: float, position: str, pay_period:str):
        super().__init__(first_name, last_name, age, pay, position, hourly=False,hours=0.0)

        self.pay_period = super().pay_periods(pay_period)

    def calc_payment(self) -> float:
        return super().pay/self.pay_period

class ContractWorker(Employee):

    def __init__(self, first_name: str, last_name: str, 
                 age: int, pay: float, position: str,
                 contract_length:int, pay_period:str):
        super().__init__(first_name, last_name, age, pay, position, hours = 0.0, hourly = False)

        self.contract_length = contract_length
        self.pay_period = super().pay_periods(pay_period)

    def calc_payment(self) -> float:
        return super().pay/self.pay_period

class CommissionedEmployee(Employee):

    def __init__(self, first_name: str, last_name: str, 
                 age: int, base_pay: float, position: str,
                 pay: float, hours: float,
                 commission_pay:float, comissions_made:int):
        super().__init__(first_name, last_name, age, hours, position, pay = 0.0,hourly = True)

        self.base_pay = base_pay
        self.comission_pay = commission_pay
        self.comissions_made = comissions_made

    def calc_payment(self) -> float:
        return self.base_pay * self.hours + self.comission_pay * self.comissions_made
    
    def __str__(self) -> str:
        return f"\t\tfirst name:      {self.first_name}\n\
                last name:       {self.last_name}\n\
                age:             {self.age}\n\
                is hourly:       {self.hourly}\n\
                base pay:        {self.base_pay}\n\
                hours:           {self.hours}\n\
                comission pay:   {self.comission_pay}\n\
                comissions made: {self.comissions_made}\n\
                position:        {self.position}\n\
                payment:         {self.payment}"

emp1 = HourlyWorker("daniel","delavega",24,True,21.00,21.00,"Shift-Lead")

print(emp1)
