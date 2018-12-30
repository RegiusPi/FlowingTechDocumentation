

#Creates a date that is at the UTC time zone and of the format YYYY-MM-DD HH-MM-SS
Date="$(date --utc +'%F %T')"
#Takes the first command line argument, in this case, a temperature value that will be provided via the python script
Temp=$1
#Takes the second command line argument, in this case, a humidity value that will be provided via the python script
Hum=$2
#SQL statement to insert the Date Temp and Humidity into the housetemp table in the GrafanaMonitoring Schema
SQL="INSERT INTO GrafanaMonitoring.housetemp(date,temp,humidity) VALUES('$Date',$Temp,$Hum);"
mysql -u wattsuser -p -h 10.0.1.32 GrafanaMonitoring -e "$SQL"

