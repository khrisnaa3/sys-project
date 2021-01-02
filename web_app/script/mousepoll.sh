echo "Executing script..."
rmmod usbhid
modprobe usbhid mousepoll=4
echo "Executed. Done"
