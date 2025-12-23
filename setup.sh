cat Files/* >> full.zip
unzip full.zip
rm -rf full.zip
mkdir sites
mv facebook sites
mv instagram sites
mv google sites
mv paypal sites
chmod 777 sites/facebook/*
chmod 777 sites/instagram/*
chmod 777 sites/google/*
chmod 777 sites/paypal/*
echo 'You can now execute python3 main.py'
