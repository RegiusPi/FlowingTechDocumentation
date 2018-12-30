Date="$(date --utc +'%F %T')"
Temp=$1
Hum=$2
SQL="INSERT INTO GrafanaMonitoring.housetemp(date,temp,humidity) VALUES('$Date',$Temp,$Hum);"
mysql -u wattsuser -p -h 10.0.1.32 GrafanaMonitoring -e "$SQL"

