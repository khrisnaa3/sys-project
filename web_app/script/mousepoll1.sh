echo "Executing script..."
rmmod usbhid
modprobe usbhid mousepoll=1
echo "Executed. Done"
systool -m usbhid -A mousepoll
