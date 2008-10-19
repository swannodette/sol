print "read %s" % ser.read(1)

ser.write("PA0,0;")		# pen absolute (0, 0)
print "read %s" % ser.read(1)

ser.write("PD;")		# pen down
print "read %s" % ser.read(1)

ser.write("PA100,0;")	        # pen absolute (100, 0)
print "read %s" % ser.read(1)

ser.write("PA100,100;")		# pen absolute (100, 100)
print "read %s" % ser.read(1)

ser.write("PA0,100;")		# pen absolute (0, 100)
print "read %s" % ser.read(1)

ser.write("PA0,0;")		# pen absolute (0, 0)
print "read %s" % ser.read(1)

ser.write("PU;")		# pen up
print "read %s" % ser.read(1)
