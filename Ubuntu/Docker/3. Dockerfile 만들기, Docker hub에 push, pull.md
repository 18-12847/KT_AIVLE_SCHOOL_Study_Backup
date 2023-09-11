# 1. Dockerfile

1) Dockerfile 만들기
   ```
   $ cd $HOME
   $ mkdir docker-practice
   $ cd docker-practice
   $ touch Dockerfile #빈 파일 생성
   $ ls
   Dockerfile
   ```
   
2) 기본 명령어
   - vi Dockerfile을 통해 Dockerfile을 연다
   - FROM
     - Dockerfile이 base image로 어떠한 이미지를 사용할 것인지 명시
     - 처음부터 끝까지 만드는 것이 아닌 어느정도 만들어진 Docker image를 가져와서 발전시킨다.
       ```
       FROM ubuntu:18.04     
       ```
   - COPY
     - a 파일 또는 디렉토리를 b 경로에 복사
       ```
       COPY a.txt /aa/b.txt
       COPY my-directory /you-directory
       ```
   - RUN
      - 명시한 커맨드를 도커 컨테이너에서 실행하는 것을 명시하는 명령어
        ```
        RUN pip install torch
        RUN pip install -r requirements.txt
        ```
   - CMD
      - 명시한 커맨드를 도커 컨테이너가 시작될 때, 실행하는 것을 명시하는 명령어
      - 하나의 Docker Image에서는 하나의 CMD만 실행 가능한 점에서 RUN 명령어와 다르다.
        ```
        CMD python main.py
        CMD
        ```
   - WORKDIR
      - 이후 작성될 명령어를 컨테이너 내의 어떤 디렉토리에서 수행할 것인지를 명시하는 명령어
      - 해당 디렉토리가 없으면 생성
         ```
         WORKDIR /home/demo
         ```
   - ENV
     - 컨테이너 내부에서 지속적으로 사용될 environment variable의 값을 설정하는 명령어
       ```
       # default 언어 설정
       RUN locale-gen ko_KR.UTF-8
       ENV LANG ko_KR.UTF-8
       ENV LANGUAGE ko_KR.UTF-8
       ENV LC_ALL ko_KR.UTF-8
       ```
   - EXPOSE
     - 컨테이너에서 뚫어줄 포트/프로토콜 지정
     - protocol을 지정하지 않으면 TCP 디폴트 설정
       ```
       EXPOSE 8080
       ```

3) 간단한 Dockerfile 작성
   - vi Dockerfile
     ```
     # base image 를 ubuntu 18.04 로 설정
     FROM ubuntu:18.04

     # apt-get update 명령을 실행
     RUN apt-get update

     # DOCKER CONTAINER 가 시작될 때, "Hello" 를 출력
     CMD ["echo", "Hello"]
     ```

# 2. Docker build from Dockerfile
- docker build 명령어로 Dockerfile로부터 Docker Image 제작
  ```
  $ docker build -t my-image:v1.0.0 .

  [+] Building 11.7s (6/6) FINISHED                                docker:default
  => [internal] load build definition from Dockerfile                       0.1s
  => => transferring dockerfile: 284B                                       0.0s
  => [internal] load .dockerignore                                          0.1s
  => => transferring context: 2B                                            0.0s
  => [internal] load metadata for docker.io/library/ubuntu:18.04            2.6s
  => [1/2] FROM docker.io/library/ubuntu:18.04@sha256:152dc042452c496007f0  2.8s
  => => resolve docker.io/library/ubuntu:18.04@sha256:152dc042452c496007f0  0.0s
  => => sha256:152dc042452c496007f07ca9127571cb9c29697f42a 1.33kB / 1.33kB  0.0s
  => => sha256:dca176c9663a7ba4c1f0e710986f5a25e672842963d95b9 424B / 424B  0.0s
  => => sha256:f9a80a55f492e823bf5d51f1bd5f87ea3eed1cb3178 2.30kB / 2.30kB  0.0s
  => => sha256:7c457f213c7634afb95a0fb2410a74b7b5bc0ba52 25.69MB / 25.69MB  0.7s
  => => extracting sha256:7c457f213c7634afb95a0fb2410a74b7b5bc0ba527033362  1.9s
  => [2/2] RUN apt-get update                                               5.9s
  => exporting to image                                                     0.3s
  => => exporting layers                                                    0.2s
  => => writing image sha256:c74dbf634d21d68d5ed21b202febb2f71c3464854d7b8  0.0s 
  => => naming to docker.io/library/my-image:v1.0.0                         0.0s 

  $ docker images                               

  REPOSITORY    TAG       IMAGE ID       CREATED          SIZE                    
  my-image      v1.0.0    c74dbf634d21   27 seconds ago   109MB
  hello-world   latest    9c7a54a9a43c   4 months ago     13.3kB

  # grep : my-image가 있는지를 잡아내는 명령어
  $ docker images | grep my-image
  my-image      v1.0.0    c74dbf634d21   3 minutes ago   109MB
  ```
  - . : 현재 경로에 있는 Dockerfile로부터 my-image라는 이름과 v1.0.0 이라는 태그로 이미지를 빌드하겠다는 명령
    
- 빌드한 my-image:v1.0.0 이미지로 docker 컨테이너 run
  ```
  $ docker run my-image:v1.0.0
  Hello
  ```

# 3. Docker Image 저장소
1) Docker Registry
   - 공식 문서 : https://docs.docker.com/registry
   - Docker Registry는 Docker-Hub에 있으므로 쉽게 사용 가능
     ```
     $ docker run -d -p 5000:5000 --name registry registry

     Unable to find image 'registry:latest' locally -> 로컬 시스템에 해당 이미지가 없어서 Docker Hub에서 다운로드
     latest: Pulling from library/registry -> 최신 버전 다운로드
     7264a8db6415: Pull complete 
     c4d48a809fc2: Pull complete 
     88b450dec42e: Pull complete 
     121f958bea53: Pull complete
     7417fa3c6d92: Pull complete 
     Digest: sha256:d5f2fb0940fe9371b6b026b9b66ad08d8ab7b0d56b6ee8d5c71cb9b45a374307
     Status: Downloaded newer image for registry:latest
     6c96dd3b00c502401d27424f5a7a1ff172139da7def54780f732794b4a6164d7
     ```
     - registry라는 이름의 Docker 이미지를 백그라운드에서 실행하여 registry라는 이름의 컨테이너 생성
     - -p 5000:5000 옵션은 호스트 시스템의 5000번 포트와 컨테이너의 5000번 포트 연결
       
   - my-image를 방금 생성한 registry를 바라보게 tag
     ```
     $ docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0
     $ docker images | grep my-image

     my-image                  v1.0.0    c74dbf634d21   About an hour ago   109MB
     localhost:5000/my-image   v1.0.0    c74dbf634d21   About an hour ago   109MB
     ```
     - my-image:v.1.0.0 이미지에 새로운 태그 추가, 새 태그는 localhost:5000/my-image:v1.0.0
     - localhost:5000은 앞서 설정한 로컬 Docker registry의 주소
     - localhost:5000/my-image:v1.0.0 태그를 사용하여 이미지를 로컬 레지스트리에 푸시할 준비
       
   - my-image를 registry에 push 후 확인
     ```
     # 로컬 레지스트리(localhost:5000)에 my-image:v1.0.0 이미지 푸시(로컬 시스템에서 레지스트리로 업로드하는 작업)
     $ docker push localhost:5000/my-image:v1.0.0

     The push refers to repository [localhost:5000/my-image]
     81f12c8f0e7a: Pushed
     548a79621a42: Pushed 
     v1.0.0: digest: sha256:26bbfab68bc3aae62f27776e3fd54aff31edf772682054bb5b7880c1bc507a0c size: 741

     # localhost:5000 이라는 registry에 어떤 이미지가 저장되어 있는지 리스트를 출력하는 명령
     $ curl -X GET http://localhost:5000/v2/_catalog
     {"repositories":["my-image"]}

     # my-image 라는 이미지 네임에 어떤 태그가 저장되어있는지 리스트 출력하는 명령
     $ curl -X GET http://localhost:5000/v2/my-image/tags/list
     {"name":"my-image","tags":["v1.0.0"]}
     ```
2) Docker Hub
   - public한 주소를 통해 docker image를 push 또는 pull 가능
   - 회원 가입 : hub.docker.com
   - Docker login
     ```
     $ docker login
     Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
     You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

     Username: jae2933 
     Password: 
     WARNING! Your password will be stored unencrypted in /home/oh/.docker/config.json.
     Configure a credential helper to remove this warning. See
     https://docs.docker.com/engine/reference/commandline/login/#credentials-store
     Login Succeeded
     ```
   - Docker hub 바라보게 tag 생성 및 Docker Hub에 image push
     ```
     $ docker tag my-image:v1.0.0 jae2933/my-image:v1.0.0
     
     $ docker push jae2933/my-image:v1.0.0
     The push refers to repository [docker.io/jae2933/my-image]
     81f12c8f0e7a: Pushed 
     548a79621a42: Mounted from library/ubuntu 
     v1.0.0: digest: sha256:d3462a87626f864e3e28ff0917bf99cb558b9b2956434229e73b74996f73e894 size: 741
     ```

   - Docker hub에서 이미지 받아오고 실행
     ```
     $ docker pull jae2933/my-image:v1.0.0

     v1.0.0: Pulling from jae2933/my-image
     Digest: sha256:d3462a87626f864e3e28ff0917bf99cb558b9b2956434229e73b74996f73e894
     Status: Image is up to date for jae2933/my-image:v1.0.0
     docker.io/jae2933/my-image:v1.0.0

     $ docker images | grep my-image
     
     jae2933/my-image          v1.0.0    c74dbf634d21   2 hours ago    109MB
     my-image                  v1.0.0    c74dbf634d21   2 hours ago    109MB
     localhost:5000/my-image   v1.0.0    c74dbf634d21   2 hours ago    109MB

     $ docker run -d jae2933/my-image:v1.0.0
     d8c2a2a0565c6a2b34287d0d69e7d4f8f1edc3f4f28ab0e092ca1967be234949
     ```
