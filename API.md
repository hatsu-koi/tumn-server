# API Reference 1.0
at `localhost:5000`

모든 요청 및 응답의 MIME 타입은 항상 `application/json` 입니다.

---

# Filters API
## GET `/filterset/`
**설명**
현재 설치된 필터셋 목록과 메세지 큐 출력

**요청 파라미터**
(없음)

**처리**
 * 설치 된 필터 폴더 내부의 filter.json 파일들과 메세지 큐를 출력한다.

**예시 출력**
```json
{
  "filters": [
    {
      "title": "Default FilterSet",
      "id": "default",
      "information": {
        "author": "Tumn Developers",
        "description": "FilterSet related to things",
        "source": {
          "href": "filterset",
          "text": "filterset"
        }
      },
      "options": [
        {
          "name": "MatureContentNN",
          "id": "default.maturecontent",
          "description": "Filters Mature Content by neural network."
        },
        {
          "name": "SwearwordsNN",
          "id": "default.swearwords",
          "description": "Filters Swearwords by neural network."
        },
        {
          "name": "HateSpeechNN",
          "id": "default.hatespeech",
          "description": "Filters Hate Speeches by neural network."
        }
      ],
      "type": "filters",
      "version": "1.0.0"
    }
  ],
  "messages": ["Installing Filter...", "Filter detected : 2017-gongmo", "remote: Counting objects: 1049, done."]
}

```


## POST `/filterset/`
**설명**
새로운 필터셋을 URL로부터 설치  

**요청 파라미터**

|  키  |  타입  |     설명     |                  예시                   |
|------|--------|--------------|----------------------------------------|
|`url`| `String` |  설치할 주소  |`"https://github.com/hatsu-koi/tumn-filter"`|

**출력 파라미터**  

|  키  |  타입  |     설명     |                  예시                   |
|------|--------|--------------|----------------------------------------|
|`id`|`String`|설치중인 필터의 id | `"default"` |

**처리**
1. 필터 폴더에 Git 레포지토리를 클론한다.
2. 필터 폴더 내부의 setup.py를 실행시킨다.

## DELETE `/filterset/:id/`
**설명**  
해당하는 필터셋을 삭제

**출력 예시**
{
    "success": true,
    "message": ""
}

**처리**
 * 해당하는 폴더를 삭제한다.


# Query API
## POST `/query`
**설명**
텍스트와 필터 목록이 주어지면, 텍스트를 차례로 필터 목록에 명시된 필터를 통과시킨다.

**요청 파라미터**  

|  키  |  타입  |     설명     |                  예시                   |
|------|--------|--------------|----------------------------------------|
|`filters`| `Array<String>` |  사용할 필터 목록  |        `["default.swearwords_nn"]`        |
| `text`  | `Array<Array<String>>` | ID-필터링할 텍스트 셋|             (예시 입력 참고)             |

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
{
  "filter": "miszehbrgbk",
  "index": [[9, 13], [19, 23]]
}
```
