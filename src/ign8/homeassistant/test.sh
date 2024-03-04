

#for ip in $(sudo masscan -p 80 192.168.86.0/24 2>&1|grep Discove|awk -F' on ' '{ print $2 }')
for ip in $(cat test.lst)
do
	curl http://$ip/rpc/WIFI.GetStatus 2>/dev/null|grep '"status":"got ip' >/dev/null 2>&1
	if [[ $? == 0 ]];
	then
		SSID=$(curl "http://$ip/rpc/WIFI.GetConfig" 2>/dev/null | jq .ap.ssid -r)
		echo "$ip $SSID"
		#curl "http://${ip}/rpc/Switch.GetConfig?id=0" |jq .
		curl "http://${ip}/rpc/Switch.Set?id=0&on=false" |jq .
		sleep 10
		curl "http://${ip}/rpc/Switch.Set?id=0&on=true" |jq .
	fi
done
