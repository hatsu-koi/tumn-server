# API Reference 1.0
at `localhost:7532`

---

# Filters API
## GET `/filter`
**설명**  
현재 설치된 필터셋 목록 출력

**요청 파라미터**  
(없음)

**처리**  
 * 설치 된 필터 폴더 내부의 filter.json 파일들을 배열로 리턴해준다.  

**예시 출력**  
```json
[
  {
    "title": "Default FilterSet",
    "id": "default",
    "information": {
      "author": "Tumn Developers",
      "description": "FilterSet related to things",
      "source": {
        "href": "https://github.com/hatsu-koi/tumn-filter",
        "text": "https://github.com/hatsu-koi/tumn-filter"
      }
    },
    "options": [
      {
        "name": "MatureContentNN",
        "id": "default.maturecontent",
        "description": "Filters Mature Content by neural network.",

      },
      {
        "name": "SwearwordsNN",
        "id": "default.swearwords",
        "description": "Filters Swearwords by neural network.",

      },
      {
        "name": "HateSpeechNN",
        "id": "default.hatespeech",
        "description": "Filters Hate Speeches by neural network.",

      }
    ],
    "type": "filters",
    "version": "1.0.0"
  }
]
```


## PUT `/filter`
**설명**  
새로운 필터셋을 URL로부터 설치  

**요청 파라미터**

|  키  |     설명     |                  예시                   |
|------|-------------|----------------------------------------|
|filter|  설치할 주소  |https://github.com/hatsu-koi/tumn-filter|

**처리**  
1. 필터 폴더에 Git 레포지토리를 클론한다.  
2. 필터 폴더 내부의 setup.py를 실행시킨다.  

## GET `/filter/installing`
**설명**  
현재 설치중인 필터셋들의 커맨드 아웃풋을 출력한다.

**요청 파라미터**  
(없음)

**처리**
 * 한번 요청이 들어올 경우 아웃풋 큐를 리턴하고 초기화 시킨다.  

**예시 출력**  
```
Cloning into 'tumn-filter'...
remote: Counting objects: 2222, done.
remote: Total 2222 (delta 0), reused 0 (delta 0), pack-reused 2222
```

## DELETE `/filter/:id`
**설명**  
존재하는 필터셋을 삭제

**URL 파라미터**

|  키  |     설명      |                  예시                   |
|------|--------------|----------------------------------------|
|  id  |삭제할 필터셋 ID|                default                 |

**처리**
 * 해당하는 폴더를 삭제한다.


# Query API
## POST `/query`
**설명**  
텍스트와 필터 목록이 주어지면, 텍스트를 차례로 필터 목록에 명시된 필터를 통과시킨다.

**요청 파라미터**  

|   키  |        설명       |                  예시                   |
|-------|------------------|-----------------------------------------|
|filters|  사용할 필터 목록  |        ['default.swearwords_nn']        |
| text  |ID-필터링할 텍스트 셋|             (예시 입력 참고)             |

**출력**  
필터에 걸린 텍스트만 id, 범위의 배열 쌍을 출력한다.  
범위는 정수로 된 배열로 출력한다.

**처리**  
 * 명시된 필터 목록에 텍스트를 차례로 통과시킨다.  

**예시 입력**  
```json
{
  "filters": ["default.swearwords_nn"],
  "text": [
    [
      ["l1kt86yj92q", "Code"],
      ["itro6738cle", "Issues"],
      ["cgjg5uz67w9", "4"],
      ["1d040yvu4cs", "Pull requests"],
      ["iomsrxxa6mf", "7"],
      ["wkct6fcfhd", "Projects"],
      ["eyw6alkyxna", "0"],
      ["fdmct7vxcvp", "Insights"]
    ],

    [
      ["miszehbrgbk", "What the fuck asdf f***"]
    ]
  ]
}
```

**예시 출력**
```json
[
  ["miszehbrgbk", [ [9, 13], [19, 23] ]]
]
```
