import re


class BrPhone:
    def __init__(self, phone):
        if self.is_phone_valid(phone):
            self.phone = phone
        else:
            raise ValueError("Invalid phone number")

    def is_phone_valid(self, phone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, phone)
        if answer:
            return True
        return False

    def format_number(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.phone)
        formatted_number = "+{}({}){}-{}".format(
            answer.group(1),
            answer.group(2),
            answer.group(3),
            answer.group(4)
        )
        return formatted_number

    def __str__(self):
        return self.format_number()