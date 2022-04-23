import utime
import machine

def interruptcall(param):
    print("hello! {}".format(param))

led_onboard = machine.Pin(25, machine.Pin.OUT)
togglingpin = machine.Pin(2, machine.Pin.OUT)
interrupt_pin = machine.Pin(1, machine.Pin.IN)
interrupt_pin.irq(handler=interruptcall, trigger= interrupt_pin.IRQ_RISING)




def toggle_ledpin(ledpin : machine.Pin):
    if ledpin.value():
        ledpin.value(0)
        return 
    else:
        ledpin.value(1)
        return 
    



while(True):
    print("\nhello")
    utime.sleep(0.5)
    toggle_ledpin(led_onboard)
    toggle_ledpin(togglingpin)
    print("\nValue of pin 2 is {}".format(interrupt_pin.value()))
