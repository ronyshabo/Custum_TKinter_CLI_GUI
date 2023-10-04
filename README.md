This little app should make it easier to find the correct CLI command for all devices,
and hopefully advances into making the call for you by pressing the required command


- Things it will do.

1- collect a CID 
2- figure out the Devices connected to it from the Topologies
3- seprates the devices and the commands that It can do.

- I am thinking of using Templates
- as a start, we hard code the commands.

step 1:
- Collect CID:
    After collecting a CID have a list of the devices that are connecting to it, then save the IP addresses to each one
    if the Ip address is DHCP, then skip it # Maybe later collect the FQDN then try to connect with it
- Beorn Call for Topologies
- Sort each device and it's IP Address


in the future Use Subprocess to run the actuall command 
eg: https://www.youtube.com/watch?v=2Fp1N6dof0Y

