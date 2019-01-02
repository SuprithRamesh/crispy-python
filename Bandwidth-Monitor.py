#Bandwidth Monitor
import time
import psutil

def main():
    buf_low = 0

    while True:
        buf_high = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if buf_low:
            send_stat(buf_high - buf_low)

        buf_low = buf_high

        time.sleep(1)

def convert_to_gbit(value):
    return value/1024./1024./1024.*8

def send_stat(value):
    print ("%0.3f" % convert_to_gbit(value))

main()
