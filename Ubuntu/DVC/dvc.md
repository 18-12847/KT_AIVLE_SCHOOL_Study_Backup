# 1. DVC 설치
- Python 설치
  - python 3.8 이상 환경 준비(ubuntu 20.04 이상 사용하면 최신 버전으로 설치 되어있음)
    ```
    oh@oh-VirtualBox:~$ python3 --version
    Python 3.10.12
    oh@oh-VirtualBox:~$ sudo apt install python3-pip
    ```
    - pip는 따로 설치 필요

- GIT 설치
  ```
  oh@oh-VirtualBox:~$ sudo apt install git
  패키지 목록을 읽는 중입니다... 완료
  의존성 트리를 만드는 중입니다... 완료
  상태 정보를 읽는 중입니다... 완료        
  패키지 git는 이미 최신 버전입니다 (1:2.34.1-1ubuntu1.10).
  git 패키지는 수동설치로 지정합니다.
  0개 업그레이드, 0개 새로 설치, 0개 제거 및 3개 업그레이드 안 함.

  oh@oh-VirtualBox:~$ git --version
  git version 2.34.1
  ```

- DVC 설치
  - dvc[all] : [all]은 dvc의 remote storage로 s3, gs, azure, oss, shh 모두 사용 가능하게 관련 패키지 함께 설치하는 옵션
  ```
  oh@oh-VirtualBox:~$ pip install dvc[all]
  oh@oh-VirtualBox:~$ dvc --version
  명령어 'dvc' 을(를) 찾을 수 없습니다. 그러나 다음을 통해 설치할 수 있습니다:
  sudo snap install dvc

  oh@oh-VirtualBox:~$ echo 'export PATH=$PATH:/home/oh/.local/bin' >> ~/.bashrc
  oh@oh-VirtualBox:~$ source ~/.bashrc
  oh@oh-VirtualBox:~$ dvc --version
  3.19.0
  ```
  - pip install dvc[all] 설치했는데 dvc를 찾을 수 없는 것은 PATH 환경변수에 없어서 그럼
  - echo 'export PATH=$PATH:/home/oh/.local/bin' >> ~/.bashrc 추가 후 source ~/.bashrc 으로 적용

# 2. DVC 저장소 세팅
1) 새 Directory 생성 및 git 저장소, dvc 저장소로 초기화
   ```
   oh@oh-VirtualBox:~/dvc-tutorial$ git init
   힌트: Using 'master' as the name for the initial branch. This default branch name
   힌트: is subject to change. To configure the initial branch name to use in all
   힌트: of your new repositories, which will suppress this warning, call:
   힌트: 
   힌트: 	git config --global init.defaultBranch <name>
   힌트: 
   힌트: Names commonly chosen instead of 'master' are 'main', 'trunk' and
   힌트: 'development'. The just-created branch can be renamed via this command:
   힌트: 
   힌트: 	git branch -m <name>
   /home/oh/dvc-tutorial/.git/ 안의 빈 깃 저장소를 다시 초기화했습니다

   oh@oh-VirtualBox:~/dvc-tutorial$ ls -al
   합계 20
   drwxrwxr-x  4 oh oh 4096  9월 14 21:55 .
   drwxr-x--- 18 oh oh 4096  9월 14 21:54 ..
   drwxrwxr-x  3 oh oh 4096  9월 14 21:55 .dvc
   -rw-rw-r--  1 oh oh  139  9월 14 21:55 .dvcignore
   drwxrwxr-x  7 oh oh 4096  9월 14 21:55 .git

   oh@oh-VirtualBox:~/dvc-tutorial$ cd .git
   oh@oh-VirtualBox:~/dvc-tutorial/.git$ ls
   HEAD  branches  config  description  hooks  index  info  objects  refs

   oh@oh-VirtualBox:~/dvc-tutorial$ dvc init
   Initialized DVC repository.
   You can now commit the changes to git.
   +---------------------------------------------------------------------+
   |                                                                     |
   |        DVC has enabled anonymous aggregate usage analytics.         |
   |     Read the analytics documentation (and how to opt-out) here:     |
   |             <https://dvc.org/doc/user-guide/analytics>              |
   |                                                                     |
   +---------------------------------------------------------------------+

   What's next?
   ------------
   - Check out the documentation: <https://dvc.org/doc>
   - Get help and share ideas: <https://dvc.org/chat>
   - Star us on GitHub: <https://github.com/iterative/dvc>
   ```

2) DVC 기본 명령1
   1) dvc로 버전 tracking 할 data 생성
      ```
      oh@oh-VirtualBox:~/dvc-tutorial$ mkdir data
      oh@oh-VirtualBox:~/dvc-tutorial$ cd data
      oh@oh-VirtualBox:~/dvc-tutorial/data$ vi demo.txt
      ```
      
   2) 방금 생성한 데이터를 dvc로 tracking
      ```
      oh@oh-VirtualBox:~/dvc-tutorial/data$ cd ..
      oh@oh-VirtualBox:~/dvc-tutorial$ dvc add data/demo.txt
      100% Adding...|█████████████████████████████████████████████████████████|1/1 [00:00, 24.53file/s]
      To track the changes with git, run:
    	git add data/demo.txt.dvc data/.gitignore
      To enable auto staging, run:
      dvc config core.autostage true

      oh@oh-VirtualBox:~/dvc-tutorial$ git add data/demo.txt.dvc data/.gitignore
      ```
      - DVC가 data/demo.txt 파일에 대한 메타데이터를 data/demo.txt.dvc라는 새로운 파일에 저장했다는 것을 알려줌
      - 이 파일과 변경된 .gitignore 파일을 git에 추가하여 변경 사항을 추적하도록 권장

   3) dvc add에 의해 자동 생성된 파일들 확인
      ```
      oh@oh-VirtualBox:~/dvc-tutorial$ cd data
      oh@oh-VirtualBox:~/dvc-tutorial/data$ ls
      demo.txt  demo.txt.dvc

      oh@oh-VirtualBox:~/dvc-tutorial/data$ cat demo.txt.dvc
      outs:
      - md5: 8b0e95993765251de57ac3d13a5d2946
        size: 8
        hash: md5
        path: demo.txt
      ```
      - demo.txt 파일의 메타정보를 가진 파일
      - git에서는 demo.txt.dvc 파일만 관리

   4) git commit 수행
      ```
      oh@oh-VirtualBox:~/dvc-tutorial/data$ cd ..
      oh@oh-VirtualBox:~/dvc-tutorial$ git commit -m "Add demo.txt.dvc"
      Author identity unknown
      *** 내가 누구인지 설정하십시오.
      다음을 실행하면,
      git config --global user.email "you@example.com"
      git config --global user.name "내 이름"
      계정의 기본 신원 정보를 설정합니다.
      --global 옵션을 빼면 이 저장소서만 신원 정보를 설정합니다.
      fatal: 메일 주소를 자동 검사할 수 없습니다 ('oh@oh-VirtualBox.(none)' 찾음)

      oh@oh-VirtualBox:~/dvc-tutorial$ git config --global user.email "jae2933@naver.com"
      oh@oh-VirtualBox:~/dvc-tutorial$ git config --global user.name "SeungJae Oh"
      oh@oh-VirtualBox:~/dvc-tutorial$ git commit -m "Add demo.txt.dvc"
      [master (최상위-커밋) eddab21] Add demo.txt.dvc
       5 files changed, 12 insertions(+)
       create mode 100644 .dvc/.gitignore
       create mode 100644 .dvc/config
       create mode 100644 .dvcignore
       create mode 100644 data/.gitignore
       create mode 100644 data/demo.txt.dvc

      #GitHub에서 Repositories 생성 후
      oh@oh-VirtualBox:~/dvc-tutorial$ git remote add origin https://github.com/18-12847/DVC_Tuto.git

      oh@oh-VirtualBox:~/dvc-tutorial$ git pull origin main --rebase

      remote: Enumerating objects: 3, done.
      remote: Counting objects: 100% (3/3), done.
      remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
      오브젝트 묶음 푸는 중: 100% (3/3), 595 바이트 | 595.00 KiB/s, 완료.
      https://github.com/18-12847/DVC_Tuto URL에서
       * branch            main       -> FETCH_HEAD
       * [새로운 브랜치]   main       -> origin/main
      Successfully rebased and updated refs/heads/master.

      oh@oh-VirtualBox:~/dvc-tutorial$ git push origin master:main

      Username for 'https://github.com': 18-12847
      Password for 'https://18-12847@github.com': 
      오브젝트 나열하는 중: 10, 완료.
      오브젝트 개수 세는 중: 100% (10/10), 완료.
      Delta compression using up to 6 threads
      오브젝트 압축하는 중: 100% (6/6), 완료.
      오브젝트 쓰는 중: 100% (9/9), 768 바이트 | 768.00 KiB/s, 완료.
      Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
      To https://github.com/18-12847/DVC_Tuto.git
         c2abd56..077dd51  master -> main
      ```
      - 개인 액세스 토큰 발급 방법
        ```
        1. GitHub Settings - Developer settings
        2. Personal access tokens - Fine-grained tokens - Generate new token
        3. Token name, Expiration, Repository access 설정
        4. Permissions - Repository permissions : Contents, Pull requests, Commit statuses read and write 설정
        5. Generate token 후 복사하여 입력
        ```
        
   5) data가 실제로 저장될 remote storage 세팅
      - google drive에 새로운 폴더 생성 후 url로부터 ID 복사
        ```
        oh@oh-VirtualBox:~/dvc-tutorial$ dvc remote add -d storage gdrive://1Ndq7-VSpyG9w1ct1rq-Pf1KFphQ3d0sS
        Setting 'storage' as a default remote.
        ```
   6) dvc config git coomit
      ```
      oh@oh-VirtualBox:~/dvc-tutorial$ git add .dvc/config
      oh@oh-VirtualBox:~/dvc-tutorial$ git commit -m "add remote storage"
      [master c51a0c5] add remote storage
       1 file changed, 4 insertions(+)

      oh@oh-VirtualBox:~/dvc-tutorial$ git push origin master
      
      Username for 'https://github.com': 18-12847
      Password for 'https://18-12847@github.com': 
      오브젝트 나열하는 중: 7, 완료.
      오브젝트 개수 세는 중: 100% (7/7), 완료.
      Delta compression using up to 6 threads
      오브젝트 압축하는 중: 100% (4/4), 완료.
      오브젝트 쓰는 중: 100% (4/4), 503 바이트 | 503.00 KiB/s, 완료.
      Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
      remote: 
      remote: Create a pull request for 'master' on GitHub by visiting:
      remote:      https://github.com/18-12847/DVC_Tuto/pull/new/master
      remote: 
      To https://github.com/18-12847/DVC_Tuto.git
       * [new branch]      master -> master
      ```
      - git push origin master는 github에서 pull request를 생성하고 main 브랜치로 merge
      - 하지만 git push origin master:main은 pull request가 필요없고 main 브랜치로 바로 푸쉬

   7) dvc push
      - 데이터를 remote storagae에 업로드
        ```
        oh@oh-VirtualBox:~/dvc-tutorial$ dvc push

        0% Checking cache in '1Ndq7-VSpyG9w1ct1rq-Pf1KFphQ3d0sS/files/md5'| |0/? [00:00<?,    ?files/s]/home/oh/.local/lib/python3.10/site-packages/oauth2client/_helpers.py:255: UserWarning: Cannot access /home/oh/.cache/pydrive2fs/710796635688-iivsgbgsb6uv1fap6a3311635dhvuei09o66c.apps.googleusercontent.com/default.json: No such file or directory
        warnings.warn(_MISSING_FILE_MESSAGE.format(filename))
        Your browser has been opened to visit:

        https://accounts.google.com/o/oauth2/auth?client_id=710796635688-iivsgbgsb63321auv1fap6635dhvuei09o66c.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.appdata&access_type=offline&response_type=code&approval_prompt=force

        Authentication successful.
        1 file pushed
        ```
        - 해당 링크로 이동해서 구글 로그인 후 인증하면 Authentication successful 메시지
        - 해당 폴더로 이동하면 폴더가 하나 생성되고 파일이 업로드
   8) dvc pull
      - 데이터를 remote storage에서 다운로드
        ```
        # dvc 캐시 삭제
        oh@oh-VirtualBox:~/dvc-tutorial$ rm -rf .dvc/cache/

        #dvc push 했던 데이터 삭제
        oh@oh-VirtualBox:~/dvc-tutorial$ rm -rf data/demo.txt

        #dvc pull로 google drive에 업로드했던 데이터 다운로드
        oh@oh-VirtualBox:~/dvc-tutorial$ dvc pull
        A       data/demo.txt 
        1 file added and 1 file fetched

        oh@oh-VirtualBox:~/dvc-tutorial$ ls
        README.md  data

        #데이터 확인
        oh@oh-VirtualBox:~/dvc-tutorial$ cat data/demo.txt
        hello
        ```
   9) dvc checkout
       - data의 버전 변경하는 명령어
       - 버전 변경 테스트를 위해 새로운 버전의 data를 dvc push
         ```
         oh@oh-VirtualBox:~/dvc-tutorial$ cd data
         oh@oh-VirtualBox:~/dvc-tutorial/data$ ls
         demo.txt  demo.txt.dvc

         oh@oh-VirtualBox:~/dvc-tutorial/data$ vi demo.txt
         oh@oh-VirtualBox:~/dvc-tutorial/data$ cat demo.txt
         hello!!

         oh@oh-VirtualBox:~/dvc-tutorial/data$ cd ..
         oh@oh-VirtualBox:~/dvc-tutorial$ dvc push
         1 file pushed

         oh@oh-VirtualBox:~/dvc-tutorial$ git pull origin main

         remote: Enumerating objects: 1, done.
         remote: Counting objects: 100% (1/1), done.
         remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
         오브젝트 묶음 푸는 중: 100% (1/1), 633 바이트 | 105.00 KiB/s, 완료.
         https://github.com/18-12847/DVC_Tuto URL에서
          * branch            main       -> FETCH_HEAD
            077dd51..4683d2a  main       -> origin/main
         힌트: You have divergent branches and need to specify how to reconcile them.
         힌트: You can do so by running one of the following commands sometime before
         힌트: your next pull:
         힌트: 
         힌트:   git config pull.rebase false  # merge (the default strategy)
         힌트:   git config pull.rebase true   # rebase
         힌트:   git config pull.ff only       # fast-forward only
         힌트: 
         힌트: You can replace "git config" with "git config --global" to set a default
         힌트: preference for all repositories. You can also pass --rebase, --no-rebase,
         힌트: or --ff-only on the command line to override the configured default per
         힌트: invocation.
         fatal: Need to specify how to reconcile divergent branches.

         oh@oh-VirtualBox:~/dvc-tutorial$ git merge origin/main
         Merge made by the 'ort' strategy. 

         oh@oh-VirtualBox:~/dvc-tutorial$ git push origin master:main
         
         Username for 'https://github.com': 18-12847
         Password for 'https://18-12847@github.com': 
         오브젝트 나열하는 중: 8, 완료.
         오브젝트 개수 세는 중: 100% (8/8), 완료.
         Delta compression using up to 6 threads
         오브젝트 압축하는 중: 100% (5/5), 완료.
         오브젝트 쓰는 중: 100% (5/5), 565 바이트 | 565.00 KiB/s, 완료.
         Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
         remote: Resolving deltas: 100% (2/2), completed with 1 local object.
         To https://github.com/18-12847/DVC_Tuto.git
         4683d2a..e7e2580  master -> main
         ```
         - git push 전에 pull로 최신 버전 가져오고 충돌 일어나면 git merge origin/main
         - nano 텍스트 편집기가 뜨는데 ctrl + o -> Enter -> ctrl + x로 merge 후 push
         - dvc push 이후 구글 드라이브 들어가면 새로운 파일이 정상적으로 업로드
           - 역시 새로운 폴더 및 파일이 추가로 생성, 열어보면 방금 수정한 파일
       
       - 이전 버전의 data로 돌아가기
         ```
         #git log 확인
         oh@oh-VirtualBox:~/dvc-tutorial$ git log --oneline
         e7e2580 (HEAD -> master, origin/main) Merge remote-tracking branch 'origin/main'
         04f7bcb Update demo.txt
         4683d2a Merge pull request #1 from 18-12847/master
         c51a0c5 (origin/master) add remote storage
         077dd51 Add demo.txt.dvc #해당 해시 값으로 돌아간다
         c2abd56 Initial commit

         #이전 commit 버전으로 되돌린다
         oh@oh-VirtualBox:~/dvc-tutorial$ git checkout 077dd51 data/demo.txt.dvc
         1 경로가 0a2f9e1에서 갱신되었습니다

         oh@oh-VirtualBox:~/dvc-tutorial$ dvc checkout
         M       data/demo.txt

         oh@oh-VirtualBox:~/dvc-tutorial$ cd data
         oh@oh-VirtualBox:~/dvc-tutorial/data$ cat demo.txt
         hello

         oh@oh-VirtualBox:~/dvc-tutorial/data$ cd ..
         oh@oh-VirtualBox:~/dvc-tutorial$ git add data/demo.txt.dvc
         oh@oh-VirtualBox:~/dvc-tutorial$ git commit -m "checkout and commit"
         [master 20fc26b] checkout and commit
          1 file changed, 2 insertions(+), 2 deletions(-)

         oh@oh-VirtualBox:~/dvc-tutorial$ git pull origin main
         https://github.com/18-12847/DVC_Tuto URL에서
          * branch            main       -> FETCH_HEAD
         이미 업데이트 상태입니다.

         oh@oh-VirtualBox:~/dvc-tutorial$ git push origin master:main
         
         Username for 'https://github.com': 18-12847
         Password for 'https://18-12847@github.com': 
         오브젝트 나열하는 중: 7, 완료.
         오브젝트 개수 세는 중: 100% (7/7), 완료.
         Delta compression using up to 6 threads
         오브젝트 압축하는 중: 100% (4/4), 완료.
         오브젝트 쓰는 중: 100% (4/4), 420 바이트 | 420.00 KiB/s, 완료.
         Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
         To https://github.com/18-12847/DVC_Tuto.git
            e7e2580..20fc26b  master -> main
         ```
# 3. DVC의 추가 기능
- Python API를 이용한 제어 : https://dvc.org/doc/api-reference
- S3, HDFS, SSH 등의 remote storage 연동
- DAG를 통한 Data pipeline 관리 : https://dvc.org/doc/start/data-management/data-pipelines
- dvc metrics, dvc plots을 사용한 각 실험의 metrics 기록 및 시각화 등
