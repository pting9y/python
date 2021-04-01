"""
function.py
"""


def format_position(latitude, longitude):
    # string object "Lat: ~ {}" has a format function.
    pattern = "Lat: {} - Long: {}"
    print(pattern)
    print(pattern.format(30, 50))
    formattedPosition = "Lat: {} - Long: {}".format(latitude, longitude)
    return formattedPosition


def cal_sum(p1, p2):
    return p1 + p2


def read_input():
    return "reading input"


def add(data):
    return data + " " + data


def send_mail(body, to):
    # ...
    return True


print(format_position(-52.23, 120.00))
print(format_position(30, 50))

print(cal_sum(5, 10))


def main():
    get_data = read_input()
    result = add(get_data)
    to = "allison9y@gmail.com"
    is_mail_sent = send_mail(result, to)
    if is_mail_sent:
        print("Successful")
    else:
        print("Failed")
    return
