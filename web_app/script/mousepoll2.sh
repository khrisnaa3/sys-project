echo "Executing script..."
rmmod usbhid
modprobe usbhid mousepoll=2
echo "Executed. Done"
systool -m usbhid -A mousepoll
