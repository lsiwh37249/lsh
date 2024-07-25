# lah

- [ ] 다음과 같은 기능 추가하기 

### 사용법
```
$ my-history -s ls

ls None None
-s => ls
13920

$ my-history -t 10 -d 2024-07-17

None 10 2024-07-12
-t => 10
-d => 2024-07-12
|     | cmd   |   cnt |
|----:|:------|------:|
| 285 | pwd   |    17 |
| 287 | pwd   |    17 |
| 289 | pwd   |    17 |
| 286 | sl    |     0 |
| 288 | sl    |     0 |
| 290 | sl    |     0 |
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

