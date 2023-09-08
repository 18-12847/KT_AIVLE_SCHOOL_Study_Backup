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
---
# Docker 권한 설정
- docker 관련 작업이 root 유저에게만 권한이 있어서 명령을 수행하려면 sudo를 붙여야 했음
- root 유저가 아닌 host의 기본 유저에게도 권한을 주려면 새로운 터미널에서 아래 명령 실행
  ```
  $ sudo usermod -a -G docker $USER
  $ sudo service docker restart
  ```
- VM 재부팅하고 docker ps 실행하면 정상적으로 출력
---
# Docker 기본 명령어
1. Docker pull
  - docker image resptiory 부터 Docker image를 가져오는 커맨드
    ```
    $ docker pull --help
    $ docker pull ubuntu:18.04
    ```
    - docker.io/library 라는 이름의 repository에서 ubuntu:18.04 image 다운로드
    - private 한 repository에서 docker image를 가져오려면 docker login을 통해서 repository를 보게 한 뒤, docker pull을 수행하는 형태로 사용
2. Docker images
   - 어떤 애플리케이션에 대해서 단순히 애플리케이션 코드뿐만 아니라 그 애플리케이션과 dependent 한 모든 것을 함께 패키징한 데이터
   - 어디에서나 컨테이너 형식으로 run 가능한 데이터터
   - 로컬에 존재하는 docker image 리스트를 출력하는 커맨드
     ```
     $ docker images
     REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
     ubuntu        18.04     f9a80a55f492   3 months ago   63.2MB -> docker pull로 다운받은 이미지
     hello-world   latest    9c7a54a9a43c   4 months ago   13.3kB -> docker run을 통해 pull 받았던 이미지
     ```
3. Docker ps
   - 현재 실행중인 도커 컨테이너 리스트 출력하는 커맨드
     ```
     $ docker ps --help
     $ docker ps -a #실행 했었던 리스트 전부 출력
     CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
     839c9da414dd   hello-world   "/hello"   49 minutes ago   Exited (0) 49 minutes ago             nifty_easley
     7d119d00cb0e   hello-world   "/hello"   22 hours ago     Exited (0) 22 hours ago               peaceful_grothendieck
     ```
4. Docker run
   - 도커 컨테이너를 실행시키는 커맨드
     ```
     $ docker run --help
     $ docker run -it --name demo1 ubuntu:18.04 /bin/bash
     $ docker ps -a
     CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS                            PORTS     NAMES
     5b29f0e6e8d0   ubuntu:18.04   "/bin/bash"   About a minute ago   Exited (0) 54 seconds ago                   oh
     8fbb42fb3a75   ubuntu:18.04   "/bin/bash"   About a minute ago   Exited (127) About a minute ago             demo1
     839c9da414dd   hello-world    "/hello"      54 minutes ago       Exited (0) 54 minutes ago                   nifty_easley
     7d119d00cb0e   hello-world    "/hello"      23 hours ago         Exited (0) 23 hours ago                     peaceful_grothendieck
     ```
     - it : -i 옵션 + -t 옵션
       - container를 실행시킴과 동시에 interactive 한 terminal로 접속시켜주는 옵션
     - --name : name
       - 컨테이너 id 대신, 구분하기 쉽도록 지정해주는 이름
     - /bin/bash
       - 컨테이너를 실행시킴과 동시에 실행할 커맨드, /bin/bash는 bash 터미널을 사용하는 것을 의미
         
5. Docker exec
   - Docker 컨테이너 내부에서 명령을 내리거나, 내부로 접속하는 커맨드
     ```
     $ docker exec --help
     $ docker run -it -d --name demo2 ubuntu:18.04
     $ docker ps
     ---------------------------------------------
     oh@oh-VirtualBox:~$ docker run -it -d --name demo2 ubuntu:18.04
     6abb4d3e4210fcbc28c70af28d2c22f9195abae12807621c25c92ad49dea3e6d

     oh@oh-VirtualBox:~$ docker ps
     CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"   3 seconds ago   Up 2 seconds             demo2

     oh@oh-VirtualBox:~$ docker exec -it demo2 /bin/bash
     root@6abb4d3e4210:/#
     ```
     - -d : 백그라운드에서 실행시켜서 컨테이너 접속 종료를 하더라도 계속 실행 중이 되도록 하는 커맨드
     - docker ps를 실행해보면 -d 옵션 때문에 demo2는 그대로 남아있다.
     ```
     oh@oh-VirtualBox:~$ docker ps -a
     CONTAINER ID   IMAGE          COMMAND       CREATED             STATUS                         PORTS     NAMES
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"   10 minutes ago      Up 10 minutes                            demo2
     5b29f0e6e8d0   ubuntu:18.04   "/bin/bash"   22 minutes ago      Exited (0) 21 minutes ago                oh
     8fbb42fb3a75   ubuntu:18.04   "/bin/bash"   22 minutes ago      Exited (127) 22 minutes ago              demo1
     839c9da414dd   hello-world    "/hello"      About an hour ago   Exited (0) About an hour ago             nifty_easley
     7d119d00cb0e   hello-world    "/hello"      23 hours ago        Exited (0) 23 hours ago                  peaceful_grothendieck

     oh@oh-VirtualBox:~$ docker exec -it demo2 /bin/bash
     root@6abb4d3e4210:/#
     ```
     - exec를 통해 container 내부에 접속 가능한 것을 확인
6. Docker logs
   - 도커 컨테이너의 log를 확인하는 커맨드
     ```
     $ docker logs --help
     oh@oh-VirtualBox:~$ docker run --name demo5 -d busybox sh -c "while true; do $(echo date); sleep 1; done"
     Unable to find image 'busybox:latest' locally -> busybox라는 이미지가 없어서 pull 하는 과정
     latest: Pulling from library/busybox
     3f4d90098f5b: Pull complete 
     Digest: sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
     Status: Downloaded newer image for busybox:latest
     63b2da2e5c75bd50b4412a4b6160ae8d6d318a41c0cac9b4745ce59cb50f1ffa
     
     oh@oh-VirtualBox:~$ docker ps
     CONTAINER ID   IMAGE          COMMAND                   CREATED          STATUS          PORTS     NAMES
     21c5f6d059e9   busybox        "sh -c 'while true; …"   3 seconds ago    Up 2 seconds              demo5
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"               18 minutes ago   Up 18 minutes             demo2
     ```
     - demo3 이름의 busybox 이미지를 백그라운드에서 도커 컨테이너로 실행하여, 1초에 한 번씩 현재 시간 출력하는 커맨드
     ```
     oh@oh-VirtualBox:~$ docker logs demo5
     Thu Sep  7 16:17:57 UTC 2023
     Thu Sep  7 16:17:58 UTC 2023
     Thu Sep  7 16:17:59 UTC 2023
     ```
     - -f 옵션 : 실시간으로 출력 가능
7. Docker stop
   - 실행 중인 도커 컨테이너를 중단시키는 커맨드
     ```
     oh@oh-VirtualBox:~$ docker ps
     CONTAINER ID   IMAGE          COMMAND                   CREATED          STATUS          PORTS     NAMES
     1b59662fde2a   busybox        "sh -c 'while true; …"   3 seconds ago    Up 3 seconds              demo6
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"               24 minutes ago   Up 24 minutes             demo2

     oh@oh-VirtualBox:~$ docker stop demo6
     demo6  

     oh@oh-VirtualBox:~$ docker ps
     CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS          PORTS     NAMES
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"   25 minutes ago   Up 25 minutes             demo2
     ```
8. Docker rm
   - 도커 컨테이너를 삭제하는 커맨드
     ```
     oh@oh-VirtualBox:~$ docker ps -a
     CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                          PORTS     NAMES
     6abb4d3e4210   ubuntu:18.04   "/bin/bash"   27 minutes ago   Exited (0) About a minute ago             demo2
     5b29f0e6e8d0   ubuntu:18.04   "/bin/bash"   39 minutes ago   Exited (0) 39 minutes ago                 oh
     8fbb42fb3a75   ubuntu:18.04   "/bin/bash"   39 minutes ago   Exited (127) 39 minutes ago               demo1
     839c9da414dd   hello-world    "/hello"      2 hours ago      Exited (0) 2 hours ago                    nifty_easley
     7d119d00cb0e   hello-world    "/hello"      23 hours ago     Exited (0) 23 hours ago                   peaceful_grothendieck

     oh@oh-VirtualBox:~$ docker rm demo2
     demo2

     oh@oh-VirtualBox:~$ docker ps -a
     CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                        PORTS     NAMES
     5b29f0e6e8d0   ubuntu:18.04   "/bin/bash"   39 minutes ago   Exited (0) 39 minutes ago               oh
     8fbb42fb3a75   ubuntu:18.04   "/bin/bash"   40 minutes ago   Exited (127) 39 minutes ago             demo1
     839c9da414dd   hello-world    "/hello"      2 hours ago      Exited (0) 2 hours ago                  nifty_easley
     7d119d00cb0e   hello-world    "/hello"      23 hours ago     Exited (0) 23 hours ago                 peaceful_grothendieck
     ```
9. Docker rmi
   - 도커 이미지를 삭제하는 커맨드
     ```
     oh@oh-VirtualBox:~$ docker images
     REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
     busybox       latest    a416a98b71e2   7 weeks ago    4.26MB
     ubuntu        18.04     f9a80a55f492   3 months ago   63.2MB
     hello-world   latest    9c7a54a9a43c   4 months ago   13.3kB

     oh@oh-VirtualBox:~$ docker rmi busybox
     Untagged: busybox:latest
     Untagged: busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
     Deleted: sha256:a416a98b71e224a31ee99cff8e16063554498227d2b696152a9c3e0aa65e5824
     Deleted: sha256:3d24ee258efc3bfe4066a1a9fb83febf6dc0b1548dfe896161533668281c9f4f

     oh@oh-VirtualBox:~$ docker rmi ubuntu:18.04
     Untagged: ubuntu:18.04
     Untagged: ubuntu@sha256:152dc042452c496007f07ca9127571cb9c29697f42acbfad72324b2bb2e43c98
     Deleted: sha256:f9a80a55f492e823bf5d51f1bd5f87ea3eed1cb31788686aa99a2fb61a27af6a
     Deleted: sha256:548a79621a426b4eb077c926eabac5a8620c454fb230640253e1b44dc7dd7562

     oh@oh-VirtualBox:~$ docker images
     REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
     hello-world   latest    9c7a54a9a43c   4 months ago   13.3kB
     ```
