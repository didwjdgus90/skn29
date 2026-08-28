### 도커네트웍 컨터이너 통신
- Bridge : 도커의 기본 네트워크, 가상의 스위치 역확, 동일한 브릿지에 속한 컨테이너들은 가상 ip주소를 할당받아서 서로 직접 통신
- Host : 호스트os의 네트워크 환경을 그대로 공유
- None : 컨테이너의 네트워크 스택을 비활성화해서 외부 및 컨터이너간의 네트워크를 원천 차단

### 사용자 정의 브리지 네트워크의 장점
default bridge 에서는 컨터이너통신이 ip주로소만 접근이 가능, 사용자 브릿지를 사용하면 도커의 내장 DNS서버가 동작을 해서 컨테이너 이름으로 상대 컨터이너를 찾아가는 서비스 디스커러리 기능을 제공, 보안기능(불필요한 컨터이너 접근을 차단)

### 네트워크 내 컨터이너 가동(호스트 80포트 연동)
```
docker network create app-bridge-net
docker run -d --name test-backend --network app-bridge-net -p 80:80 nginx:alpine
```

### 확인방법
### web  http://127.0.0.1:80  or http://127.0.0.1  
### 컨터이너내부  nginx 화면이 http로 리턴되는것을 확인
```
docker run --rm --network app-bridge-net curlimages/curl curl -s http://test-backend
```
### 리소스 정리
```
docker stop test-backend
docker rm test-backend
docker network rm app-bridge-net
```