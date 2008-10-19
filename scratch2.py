# open up a connection, good defaults, should explore this more
ser = serial.Serial("/dev/tty.USA19H3d1P1.1", 9600,
              timeout = 	1,
              bytesize = 	serial.EIGHTBITS,
              stopbits = 	serial.STOPBITS_ONE,
              parity =		serial.PARITY_ODD,
              xonxoff = 	1)

# open the connection
ser.open()

# write some data out
#ser.write("IN;")		# initialize the plotter
#print "read %s" % ser.read(1)

# the first instruction works
#ser.write("IP0,0,4000,4000;")	# setup the plotter units (interesting)
#print "read %s" % ser.read(1)

#ser.write("SC0,100,0,100;")	# the scaling units
#print "read %s" % ser.read(1)

ser.write("SP6;")		
ser.write("PA20,20;")		
ser.write("PD;")
ser.write("PA80,20;")		
ser.write("PA80,80;")		
ser.write("PA20,80;");
ser.write("PA20,20;");
ser.write("PU;")

# close the connection
ser.close()

print "Done"
