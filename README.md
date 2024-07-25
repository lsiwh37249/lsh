# lah

- [ ] 다음과 같은 기능 추가하기 

### 사용법
```
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Dev env setting
```
$ git clone <URL>
$ cd <PJT_NAME>
$ pdm install
$ [pdm test|pytest]

#option
pdm add -dG test pytest pytest-cov
```

### ref
- https://pdm-project.org/latest/usage/dependency/ 

### deploy
```bash
# main branch
$ pip install git+https://github.com/lsiwh37249/lsh.git
```
#  option 
$ pdm init
$ pdm venv create
$ source .venv/bin/activate
$ pdm add -dG test pytest pytest-cov
$ pytest

