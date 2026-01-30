import datetime

class Age:
    def __init__(self):
        pass

    def date_time(self) -> list[int]:
        current_date = datetime.datetime.today().date()
        current_day = current_date.day 
        current_month = current_date.month + 1 # INDICE JANEIRO É 0
        current_year = current_date.year

        list_current_date = [current_day, current_month, current_year]
        return list_current_date
    
    def calculate_age(self, day_user: int, month_user: int, year_user: int) -> str:
        age_day = self.date_time()[0] - day_user
        age_month = month_user - self.date_time()[1]
        age_year = self.date_time()[2] - year_user
        age = (f'Você tem {age_day} dias, {age_month} meses e {age_year} anos de idade!')
        return age

