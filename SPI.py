from machine import Pin, SPI
import time
def run(mensaje):
    hSPI= SPI(1,baudrate=400000,sck=Pin(14),mosi=Pin(13),miso=Pin(12))
    cs=Pin(15,mode=Pin.OUT,value=1)
    encoded=mensaje.encode('utf-8')
    cs(0)
    #SPI.init(baudrate=400000,sck=Pin(14),mosi=Pin(13),miso=Pin(12))
    write_buffer=bytearray(mensaje,'ascii')
    read_buffer=bytearray(len(mensaje))
    hSPI.write_readinto(write_buffer,read_buffer)
    #hSPI.write(bytearray(encoded))
    print('write spi: ' + str(mensaje))
    
    #hSPI.write(bytearray([4,5,8]))
    time.sleep(2)
    
    
    
    
    