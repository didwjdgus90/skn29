### Django , PostgreSQL 컨터이너 통합
- 두 앱은 독립된 컨테이너에서 격리되어 실행
- 호스트와 공유하는 볼륨을 설계
- 장고가 데이터베이스를 찾아가려면 호스트 정보로 데이터베이스 별칭을 사용하도록 구성, 사용자 브릿지 망에 소속된 장고 컨테이너가 내장 dns 기능을 통해서 db-container라는 이름을 postgreSQL의 내부 ip 주소로 변환해서 연결


### Dockerfile 생성
### Django-admin startproject confing .
### settings.py에 postgreSQL 사용하도록 생성
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SQL_DATABASE', 'django_db'),
        'USER': os.environ.get('SQL_USER', 'django_user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'django_pwd'),
        'HOST': os.environ.get('SQL_HOST', 'db-container'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}
```
### 도커 이미지 로컬 빌드
```
docker build -t my-django-app:1.0 .
```

1. 전용 벡앤트 브릿지 네트웍 생성
```
docker network create app-bridge-net
```
2. postgreSQL 데이터 볼륨 생성, 데이터베이스 컨테이너 가동
```
docker volume create pg-data-vol
docker run -d --name db-container   --network app-bridge-net   -e POSTGRES_DB=django_db   -e POSTGRES_USER=django_user   -e POSTGRES_PASSWORD=django_pwd   -v pg-data-vol:/var/lib/postgresql/data   postgres:16-alpine
```

3. Django 웹 컨테이너를 데이터베이스 정보와 함께 가동
```
docker run -d --name web-container       --network app-bridge-net       -p 8000:8000       -v %CD%:/app       -e SQL_DATABASE=django_db       -e SQL_USER=django_user       -e SQL_PASSWORD=django_pwd       -e SQL_HOST=db-container       -e SQL_PORT=5432       my-django-app:1.0
```
4. 부팅 로그 확인
```
docker logs web-container
```

5. 웹앱 컨테이너 내부로 데이터 마이그레이션 주입
```
docker exec -it web-container python manage.py migrate
```
6. 데이터베이스 내부 접속 및 스키마 검증
```
docker exec -it db-container psql -U django_user -d django_db
```
7. 내부 콘솔 명령어
```
-- 테이블 목록 조회 (마이그레이션된 장고 기본 테이블 출력 검증)
\dt

-- psql 종료
\q
```
8. 확인방법
http://localhost:8000

9. 리소스 정리
```
docker stop web-container db-container
docker rm web-container db-container
docker network rm app-bridge-net
```
