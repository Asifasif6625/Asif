if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Asifasif6625/Asif.git /Asif
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Asif
fi
cd /Asif
pip3 install -U -r requirements.txt
echo "Starting ᗩᒍᗩ᙭....🔥"
python3 bot.py
