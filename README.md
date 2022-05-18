# wanted-2nd-moadata
2차 원티드 프리온보딩 - 모아데이타 기업 과제

<center>
<div style="display: flex">
    <img src="https://img.shields.io/badge/Python 3.9-FFD43B?style=flat-square&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Flask Resful-000000?style=flat-square&logo=flask&logoColor=white" />
    <img src="https://img.shields.io/badge/Pandas-2C2D72?style=flat-square&logo=pandas&logoColor=white" />
    <img src="https://img.shields.io/badge/json-5E5C5C?style=flat-square&logo=json&logoColor=white" />
</div>
</center>

---

## 개인별 링크
|이름|링크|프레임워크|
|---|---|---|
|최승리|[github](https://github.com/apollo058/Moadata_Django.git)|Django|
|하정현|[github](https://github.com/Vector-7/wanted-2nd-moadata-flask)|Flask|
|남기윤|[github](https://github.com/Chilla-N/Moadata_Wanted/tree/main)|Flask|

---

## 요구사항
* 기존 요구 사항
  * JOB 저장: 입력받은 Job의 정보를 job.json파일에 저장
  * JOB 삭제: 입력 받은 job id를 job.json에 찾아 삭제 후 저장
  * JOB 수정: 전달 받은 job id를 job.json에 찾아 수정 후 저장
  * JOB 실행: 전달 받은 job id를 job.json에 찾아 수행
  * Task
    * read: 해당 파일을 읽어 ```pandas.DataFrame```으로 출력
    * drop: ```panads.DataFrame```의 특정 컬럼을 제거
    * write: ```pandas.DataFrame```의 데이터를 지정된 파일에 저장
* 자체 설정된 요구 사항
  * task process가 ```read a -> read b``` 일 경우, ```a```데이터를 ```b```와 같이 합쳐서 ```c```를 만든다.
    * 이때 ```a```와 ```b``` 이 동일한 컬럼이 있는 경우, 단순히 붙이는 것이 아닌 공통된 컬럼을 중심으로 병합한다.


## How to run Application
### Run
* repository를 다운받습니다
  ```
  git clone <>
  ```
* requirements.txt를 이용해 패키지를 다운받습니다.
  ```
  pip install -r requirements.txt
  ```
* ```api.py```를 실행합니다.
  ```
  python api.py
  ```


## Directory Sturcture
```tree
└─Moadata_Wanted
    └─flask_moa
        ├─data        
        ├─app.py
        ├─views.py
        └─utils
            ├─job.py
            └─logics.py
        
```
* **data**: Job을 관리하는 파일 ```jobs.json```과 ```a.csv```파일이 기본적으로 들어가 있습니다.
* **utils**: 해당 프로젝트를 구현하기 위한 기능 라이브러리 입니다.
  * job: views 내 view 클래스에 필요한 클래스와 내장함수가 정의되어있습니다
  * logics: 실행스케줄을 위한 알고리즘이 정의되어 있습니다.
* **views**: API가 정의되어 있습니다.
* **app.py**: 처음으로 실행되는 최상위 파일 입니다. url을 지정하고 앱 실행을 위한 기능을 합니다.

## API Documentation
### CRUD
#### Job 생성

|Method|uri|
|---|---|
|POST|```/api/jobs```|

* Input[json]
  ```json
  {
    "job_name": "<Job 이름>",
    "task_list": {
      "<출발 지점>": ["<목표 지점1>", "<목표 지점2>", "..."],
      ...
    },
    "property": {
      "<출발 지점1>": {"<task_name>": "<Task 종류>", "..."},
      ...
    }
  }
  ```
* Output
  * (200)
    ```json
    {"job_id": "<job id>"}
    ```
  * (400)
    * 정상적인 데이터가 아님


#### Job 정보 얻기

|Method|uri|
|---|---|
|GET|```/api/jobs/<int:job_id>```|

* Input
  * 없음
* Output
  * (200)
    ```json
    {
      "job_id": "<Job ID>",
      "job_name": "<Job 이름>",
      "task_list": {
        "<출발 지점>": ["<목표 지점1>", "<목표 지점2>", "..."],
        ...
      },
      "property": {
        "<출발 지점1>": {"<task_name>": "<Task 종류>", "..."},
        ...
      }
    }
    ```

#### Job 정보 수정

|Method|uri|
|---|---|
|PATCH|```/api/jobs/<int:job_id>```|

* Input[json]
  ```json
  {
    "job_name": "<Job 이름>",
    "task_list": {
      "<출발 지점>": ["<목표 지점1>", "<목표 지점2>", "..."],
      ...
    },
    "property": {
      "<출발 지점1>": {"<task_name>": "<Task 종류>", "..."},
      ...
    }
  }
  ```
* Output
  * (200) 성공
  * (400) 알맞지 않은 데이터
  * (404) 해당 job id에 대한 데이터를 찾을 수 없음

#### Job 삭제

|Method|uri|
|---|---|
|DELETE|```/api/jobs/<int:job_id>```|

* Input
  * 없음
* Output
  * (200) 성공
  * (404) 데이터 없음

### Run Task

|Method|uri|
|---|---|
|GET|```/api/jobs/<int:job_id>/run```|


* Input
  * 없음
* Output
  * (200) 성공
  * (404) 데이터 없음

## DFD
![](readme-asset/sd6.png)


## Sequence Diagram

### JOB 추가
![](readme-asset/sd1.png)

### JOB 정보 얻기
![](readme-asset/sd2.png)

### JOB 수정
![](readme-asset/sd3.png)

### JOB 제거
![](readme-asset/sd4.png)

### JOB 수행
![](readme-asset/sd5.png)
