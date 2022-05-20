# import re
# from cpf_cnpj import Document
# import re
# from br_phone import BrPhone

from datetime import datetime, timedelta
from br_dates import BrDate

# cnpj_example = "35379838000112"
# cpf_example = "32007832062"
#
# doc = Document.create_document(cnpj_example)
# print(doc)

# pattern = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# text = "123 gabriel123@gmail.com.br"

# pattern_mold = "(xx)aaaa-wwww"
# pattern = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# text = "I like the number 2126451234 and also 1231232423"
# answer = re.findall(pattern, text)
# print(answer)

# phone = "552126481234"
# phone_object = BrPhone(phone)
# pattern = "([0-9]{2,3})?([0-9]{2}[0-9]{4,5})([0-9]{4})"
# answer = re.findall(pattern, phone)
# answer = re.search(pattern, phone)
# print(answer.group())

# print(phone_object)

# registration = BrDate()
# print(registration)
# datetime.strftime()
#
# today = datetime.today()
# formatted_today = today.strftime("%d/%m/%Y %H:%M")
# print(today, " - ", formatted_today)

# today = datetime.today()
# tomorrow = datetime.today() + timedelta(days=1, hours=20)

today = BrDate()
print(today.reg_time())
