# 가상환경 시작하기 
```
python3 -m venv new_pro
```
```
source bin/activate
```

# django를 시작하기 위한 설치
```
pip3.9 install django
```
```
pip3.9 install channels
```

# django 프로젝트 시작
```
mysite/mysite/setting.py  
python manage.py startapp chat
```

# 데이터 베이스 생성 
```
python3.9 main.py migrate
```

마이그레이션 파일 생성
```
python3 manage.py makemigrations chat
```

실제 데이터베이스에 모델 추가
``` 
python3 manage.py migrate chat
```


# django runserver 실행
```
python manage.py runserver
```
# 발생 에러 
```
AttributeError: Can't pickle local object 'convert_exception_to_response.<locals>.inner'
```
> channel 변수를 잘 못 선언하여 발생한 오류 

```
크롬 드라이버 에러 문제도 
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 97
Current browser version is 101.0.4951.64 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```
> 크롬 드라이버 버전 문제로 인한 에러 
