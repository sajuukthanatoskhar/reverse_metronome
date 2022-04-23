"""
Micropython library for RPico to handle speaker functions
"""
from machine import PWM, Pin
from utime import sleep

class Speaker:
    def __init__(self, pin_pos):

        self.volume = 0 
        self.location = pin_pos
        self.buzzer = PWM(Pin(self.location))
        self.turned_on = False

    def init_pwm_buzzer(self):
        """
        Sets the speaker up for buzzing at 250, should be at 0 volume
        """
        
        self.buzzer.freq(250)
        self.set_volume(0)

    def set_volume(self, vol):
        """
        Sets the volume
        @param vol: volume, set between 0 or 1000
        """
        if vol < 0 or vol > 1000:
            self.volume = vol
            return False
        
        self.volume = vol

        return True

    def buzz_speaker(self, speakerfreq = 250): 
        """
        Buzzes speaker at a certain frequency
        
        @param freq: 
        """
        self.turned_on = True
        self.buzzer.freq(speakerfreq)
        self.buzzer.duty_u16(self.volume)
        
    def turn_off_speaker(self):
        """
        Turns off speaker by setting volume to 0
        """
        self.turned_on = False
        self.buzzer.duty_u16(0)
    








