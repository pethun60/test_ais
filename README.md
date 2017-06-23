# test_ais
This is a small python script to be usd to send serial data received from a ais receiver to marine trafik, aishub or similar 
website. 

sends serial data to tcp as client

optional arguments:
  -h, --help            show this help message and exit
  -s SERIALDEVICE, --serialdevice SERIALDEVICE
                        Serial device /dev/ttyS0
  -n HOSTNAME, --hostname HOSTNAME
                        host name server1
  -n2 HOSTNAME2, --hostname2 HOSTNAME2
                        host name server2
  -n3 HOSTNAME3, --hostname3 HOSTNAME3
                        host name server3
  -n4 HOSTNAME4, --hostname4 HOSTNAME4
                        host name server4
  -p PORT, --port PORT  Port number server1 Integer
  -p2 PORT2, --port2 PORT2
                        Port number server2 Integer
  -p3 PORT3, --port3 PORT3
                        Port number server3 Integer
  -p4 PORT4, --port4 PORT4
                        Port number server4 Integer
ex:
cmd_udpclient2.py -s /dev/ttyACM0 -n data.aishub.net -p 2342 -n2 5.9.207.224 -p2 6690 -n3 192.168.1.103 -p3 5555 >> startais.log; exec bash"

This will send all incoming serial ais data from serial interface /dev/ttyACM0 to AIS hub and Marinetraffic plus my own internal database.

ais serial data from the receiver:

06EuOwiIvIwnSwe7wvlOwwsAwwnSGmwvwt,0*13
"
sending "!AIVDM,1,1,,A,13u>D9?P0OQ<FtLQKk3:q?wP2@M8,0*07
"
sending "!AIVDM,2,1,7,A,53u=`e000001<LQ222058dv2222222222222220m1h43340Ht2P000000000,0*0C
"
sending "!AIVDM,2,2,7,A,00000000000,2*23
"
sending "!AIVDM,1,1,,A,13aSPvh0011:F:6QRoms`CcP00Ro,0*77
"
sending



