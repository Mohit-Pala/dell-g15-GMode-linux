import os
import sys

# evevate privilages and run itself as root, use sudo 
def elevate():
    if os.getuid() == 0:
        return

    args = [sys.executable] + sys.argv
    commands = []
    # uncomment below line to use sudo instead of pkexec
    # commands.append(["sudo"] + args)
    
    # comment out below line to use sudo instad of pkexec
    commands.append(["pkexec"] + args)

    for args in commands:
        os.execlp(args[0], *args)
        
# check if the fan is turned on
def isFanOn():
    try:
        path = "/tmp/g15FanStatus"
        file = open(path, 'r')
        content = file.read()
        file.close()
        if(content == 'on'):
            return True
        else:
            return False
    except:
        print('File not found, turning off fan')
        # call to turn off fan
        turnOff()
        # write off to fan status
        path = "/tmp/g15FanStatus"
        file = open(path, 'w')
        file.write('off')
        return False
    
# turn off GMode
def turnOff():
    print('turnign off')
    # echo "\_SB.AMW3.WMAX 0 0x15 {1, 0xa0, 0x00, 0x00}" > /proc/acpi/call
    # echo "\_SB.AMW3.WMAX 0 0x25 {1, 0x00, 0x00, 0x00}" > /proc/acpi/call
    # from archwiki
    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMW3.WMAX 0 0x15 {1, 0xa0, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')
    
    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMW3.WMAX 0 0x25 {1, 0x00, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')
    
    with open('/tmp/g15FanStatus', 'w') as fanStatus:
        fanStatus.write('off')
    


# turn on GMode  
def turnOn():
    print('turning on')
    # echo "\_SB.AMW3.WMAX 0 0x15 {1, 0xab, 0x00, 0x00}" > /proc/acpi/call
    # echo "\_SB.AMW3.WMAX 0 0x25 {1, 0x01, 0x00, 0x00}" > /proc/acpi/call
    # from archwiki

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMW3.WMAX 0 0x15 {1, 0xab, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')
    
    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMW3.WMAX 0 0x25 {1, 0x01, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')
    
    with open('/tmp/g15FanStatus', 'w') as fanStatus:
        fanStatus.write('on')
    
def main():
    # gain root privilages
    elevate()
    if isFanOn():
        turnOff()
    else:
        turnOn()
    os.system('sleep 3')
        
if __name__ == "__main__":
    main()