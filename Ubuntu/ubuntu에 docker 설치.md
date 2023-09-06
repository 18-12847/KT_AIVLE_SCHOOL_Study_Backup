# Docker 설치
- https://docs.docker.com/engine/install/ubuntu Install using the repository 방법
1. Set up the repository
   - apt 패키지 매니저 업데이트
     ```
     $ sudo apt-get update
     ```
   - Docker의 prerequisite package 설치
     ```
     $ sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
     ```
   - Docker의 GPG key 추가
     ```
     $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
     ```
   - stable 버전의 repository 보게 설정
     ```
     $ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
     ```
2. Install Docker Engine
   - Docker 엔진의 최신 버전 설치
     ```
     $ sudo apt-get update
     $ sudo apt-get install docker-ce docker-ce-cli containerd.io
     ```
3. 정상 설치 확인
   - docker container를 실행시켜 정상적으로 설치되었는지 확인
     ```
     $ sudo docker run hello-world

     Unable to find image 'hello-world:latest' locally
     latest: Pulling from library/hello-world
     719385e32844: Pull complete 
     Digest: sha256:dcba6daec718f547568c562956fa47e1b03673dd010fe6ee58ca806767031d1c
     Status: Downloaded newer image for hello-world:latest

     Hello from Docker!
     This message shows that your installation appears to be working correctly.

     To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
      (amd64)
     3. The Docker daemon created a new container from that image which runs the
      executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
      to your terminal.

     To try something more ambitious, you can run an Ubuntu container with:
       $ docker run -it ubuntu bash

     Share images, automate workflows, and more with a free Docker ID:
       https://hub.docker.com/
 
     For more examples and ideas, visit:
       https://docs.docker.com/get-started/
     ```
     
