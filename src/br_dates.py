from datetime import datetime, timedelta


class BrDate:
    def __init__(self):
        self.reg_moment = datetime.today()

    def __str__(self):
        return self.format_data()

    def reg_month(self):
        months_of_the_year = [
            "January", "February", "March", "April",
            "May", "June", "July", "August", "September",
            "October", "November", "December"
        ]
        reg_month = self.reg_moment.month - 1
        return months_of_the_year[reg_month]

    def weekday(self):
        days_of_the_week = [
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ]
        weekday = self.reg_moment.weekday()
        return days_of_the_week[weekday]

    def format_data(self):
        formatted_data = self.reg_moment.strftime("%d/%m/%Y %H:%M")
        return formatted_data

    def reg_time(self):
        reg_time = (datetime.today() + timedelta(days=30)) - self.reg_moment
        return reg_time
