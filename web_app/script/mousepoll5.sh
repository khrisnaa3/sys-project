echo "Executing script..."
rmmod usbhid
modprobe usbhid mousepoll=5
echo "Executed. Done"
systool -m usbhid -A mousepoll
