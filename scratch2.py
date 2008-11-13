import serial

# open up a connection, good defaults, should explore this more
ser = serial.Serial("/dev/tty.KeySerial1", 9600,
              timeout = 	1,
              bytesize = 	serial.EIGHTBITS,
              stopbits = 	serial.STOPBITS_ONE,
              parity =		serial.PARITY_ODD,
              xonxoff = 	1)

print ser

# open the connection
ser.open()

# initialize the plotter
#print "Initializing"

def hpglcom(command):
  print "send %s" % command
  # issue the command, should probably auto add semis
  ser.write(command)
  # for handshaking
  ser.read()

hpglcom(".(;")
hpglcom(".I81;")
hpglcom(";")
hpglcom("17:.N;")
hpglcom("19:IN;")	
hpglcom("IP0,0,4000,4000;")
hpglcom("SC0,100,0,100;")
hpglcom("SP4;")

hpglcom("PD;")

hpglcom("PA20,20;")	
hpglcom("PA80,20;")		
hpglcom("PA80,80;")		
hpglcom("PA20,80;");
hpglcom("PA20,20;");
hpglcom("PU;")

hpglcom("PA90,90;")
# set the terminator
hpglcom("DT*,1;")
hpglcom("LBHello world*;")
hpglcom("PU;")

# close the connection
ser.close()

print "Done"
print "Cool"
