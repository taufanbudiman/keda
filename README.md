# keda
simple django and test case


## Setting virtualenv
buat virtual env dengan python 3
```bash
virtualenv keda_env -p python3
```
aktifkan virtualenv dan install requirements

```bash
source keda_env/bin/active
```

clone repo dan install requirements
```bash
git clone https://github.com/taufanbudiman/keda.git
cd keda
pip install -r requirements.txt
```

makemigrations dan migrate django database
```bash
./manage.py makemigrations
./manage.py migrate
```

jalankan django test
```bash
./manage.py test
```
