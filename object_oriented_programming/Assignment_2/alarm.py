from datetime import datetime

now = datetime.now()

class Alarm_clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_alarm(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    def get_alarm(self):
        return self.hour, self.minute, self.second

    def __str__(self):
        return f"Alarm time is {self.hour}:{self.minute}:{self.second}"
    
def check_time(my_alarm, formated_time):

    if formated_time[0] == my_alarm.hour and formated_time[1] == my_alarm.minute and formated_time[2] == my_alarm.second:
        print("Alarm!")
    else:
        print("No alarm")

def main():
    current_time = now.strftime("%H:%M:%S")
    formated_time = current_time.split(":")
    print(f"Current time is {current_time}")
    print(f"Formated time is {formated_time}")
    my_alarm = Alarm_clock("15", "42", "50")
    print(my_alarm)
    check_time(my_alarm, formated_time)
    

if __name__ == "__main__":
    main()