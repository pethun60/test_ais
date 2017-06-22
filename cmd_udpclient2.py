#!/usr/bin/python

import socket
import sys
import serial
import argparse

__author__ = 'Pethun'

parser = argparse.ArgumentParser(description='sends serial data to tcp as client ')
parser.add_argument('-s','--serialdevice', help='Serial device /dev/ttyS0',required=True)
parser.add_argument('-n','--hostname',help='host name server1', required=True)
parser.add_argument('-n2','--hostname2',help='host name server2', required=False)
parser.add_argument('-n3','--hostname3',help='host name server3', required=False)
parser.add_argument('-n4','--hostname4',help='host name server4', required=False)
parser.add_argument('-p','--port',help='Port number server1 Integer', required=True)
parser.add_argument('-p2','--port2',help='Port number server2 Integer', required=False)
parser.add_argument('-p3','--port3',help='Port number server3 Integer', required=False)
parser.add_argument('-p4','--port4',help='Port number server4 Integer', required=False)



args = parser.parse_args()

## show values ##
print ("serialdevice: %s" % args.serialdevice )
print ("Output file: %s" % args.hostname )




# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serialport_name = args.serialdevice
servername = args.hostname
port = int(args.port)
server_address = (servername, port)
server_address2 = ''
server_address3 = ''
server_address4 = ''
serialdata = ''

servername2 = args.hostname2
if args.port2:
   port2 = int(args.port2)
   server_address2 = (servername2, port2)

servername3 = args.hostname3
if args.port3:
    port3 = int(args.port3)
    server_address3 = (servername3, port3)

servername4 = args.hostname4
if args.port4:
    port4 = int(args.port4)
    server_address4 = (servername4, port4)

#set serial port
ser = serial.Serial(serialport_name,timeout=1)


# Get serial data and send to servers
while True:
    try:
        serialdata = ser.readline()

	# print 'bytes to read %s ' % (bytesToRead)
    	# print 'serial data %s ' % (serialdata)
    	# Send data
    	# print "servername %s port %s" % (servername, port)
    	if serialdata:
	    print >>sys.stderr, 'sending "%s"' % serialdata
	    sent = sock.sendto(serialdata, server_address)
	    if server_address2:
	        sentagain = sock.sendto(serialdata, server_address2)
	    if server_address3:
	        sentagain = sock.sendto(serialdata, server_address3)
	    if server_address4:
	        sentagain = sock.sendto(serialdata, server_address4)
	    serialdata=''
    except Exception as e:
        print "nu blev det fel"
        print e.args

    # Receive response
    #print >>sys.stderr, 'waiting to receive'
    #data, server = sock.recvfrom(4096)
    #print >>sys.stderr, 'received "%s"' % data

#finally:
    #print >>sys.stderr, 'closing socket'
    #sock.close()
