class Watch:
    def __init__(self, hr, min, sec, alarm=None, type="Digital"):
        self.hr = hr
        self.min = min
        self.sec = sec
        self.alarm = alarm  # Format: "HH:MM:SS"
        self.type = type

    def set_alarm(self, alarm_time):
        """Set an alarm time"""
        self.alarm = alarm_time
        print(f"Alarm set for {alarm_time}")

    def stop_alarm(self):
        """Stop the alarm"""
        self.alarm = None
        print("Alarm stopped")

    def show_time(self):
        """Display current time"""
        print(f"Current time: {self.hr:02}:{self.min:02}:{self.sec:02}")

# Example usage
watch = Watch(10, 30, 45)
watch.show_time()
watch.set_alarm("07:00:00")
watch.stop_alarm()
