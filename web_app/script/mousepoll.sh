echo "Executing script..."
rmmod usbhid
modprobe usbhid mousepoll=3
echo "Executed. Done"
systool -m usbhid -A mousepoll
