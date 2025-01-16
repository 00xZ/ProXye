python3 proxye.py | tee input.txt #can use anew instead of tee
python3 make_list.py
rm input.txt
cat proxies.txt | anew proxy.db
