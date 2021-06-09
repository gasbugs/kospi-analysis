# Dockerfile
# 이미지를 빌드하는데 사용할 베이스 이미지를 선택한다.
FROM docker.io/library/python:3

# /app 디렉토리를 작업 공간으로 사용한다.
WORKDIR /app

# 앞서 구성한 모든 파일은 /app으로 옮긴다.
COPY . .

# pip install 을 사용해 flask를 설치한다.
RUN apt-get update 
RUN pip install --no-cache-dir -r /app/requirements.txt

# 80포트를 사용한다.
EXPOSE 80

# 컨테이너 실행 시 사용할 명령어를 등록한다.
CMD ["python", "/app/app.py"]
