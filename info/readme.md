інший розділ
https://github.com/achillean/shodan-python    shodan API на Python

/n

ip=$(curl ip.pla1.net)  ір в змінну

курс біткоіна
echo "1 BTC = $(curl -s https://api.coindesk.com/v1/bpi/currentprice/usd.json | grep -o 'rate":"[^"]*' | cut -d\" -f3) USD"
