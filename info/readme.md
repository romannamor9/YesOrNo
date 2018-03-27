інший розділ
https://github.com/achillean/shodan-python    shodan API на Python


ps aux 

/n

for a in $(ls /usr/sbin /usr/bin); do ps -fC $a;done|grep -v PPID
ip=$(curl ip.pla1.net)  ір в змінну

курс біткоіна




echo "1 BTC = $(curl -s https://api.coindesk.com/v1/bpi/currentprice/usd.json | grep -o 'rate":"[^"]*' | cut -d\" -f3) USD"


час перебування в системі


last|grep `whoami`|grep -v logged|cut -c61-71|sed -e 's/[()]//g'|awk '{ sub("\\+", ":");split($1,a,":");if(a[3]){print a[1]*60*60+a[2]*60+a[3]} else {print a[1]*60+a[2] }; }'|paste -s -d+ -|bc|awk '{printf "%dh:%dm:%ds\n",$1/(60*60),$1%(60*60)/60,$1%60}'

