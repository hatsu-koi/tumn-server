# API Reference 1.0
at `localhost:5000`

모든 요청 및 응답의 MIME 타입은 항상 `application/json` 입니다.

---

# Filters API
## GET `/filterset/`
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
]
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

## GET `/filterset/messsages`
**설명**
설치중인 필터셋들의 로그를 출력한다.

**요청 파라미터**
없음

**처리**
 * 한번 요청이 들어올 경우 메세지 큐를 리턴하고 초기화 시킨다.  

**예시 출력**
```
{
    message: "Downloading FilterSet...\nFilter detected : 2017-gongmo\nremote: Counting objects: 1049, done.\nReceiving objects:   0% (1/1049)\nReceiving objects:   1% (11/1049)\nReceiving objects:   2% (21/1049)\nReceiving objects:   3% (32/1049)\nReceiving objects:   4% (42/1049)\nReceiving objects:   5% (53/1049)\nReceiving objects:   6% (63/1049)\nReceiving objects:   7% (74/1049)\nReceiving objects:   8% (84/1049)\nReceiving objects:   9% (95/1049)\nReceiving objects:  10% (105/1049)\nReceiving objects:  11% (116/1049)\nReceiving objects:  12% (126/1049)\nReceiving objects:  13% (137/1049)\nReceiving objects:  14% (147/1049)\nReceiving objects:  15% (158/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  16% (168/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  17% (179/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  18% (189/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  19% (200/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  20% (210/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  21% (221/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  22% (231/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  23% (242/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  24% (252/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  25% (263/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  26% (273/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  27% (284/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  28% (294/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  29% (305/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  30% (315/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  31% (326/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  32% (336/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  33% (347/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  34% (357/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  35% (368/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  36% (378/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  37% (389/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  38% (399/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  39% (410/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  40% (420/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  41% (431/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  42% (441/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  43% (452/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  44% (462/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  45% (473/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  46% (483/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  47% (494/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  48% (504/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  49% (515/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  50% (525/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  51% (535/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  52% (546/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  53% (556/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  54% (567/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  55% (577/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  56% (588/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  57% (598/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  58% (609/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  59% (619/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  60% (630/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  61% (640/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  62% (651/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  63% (661/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  64% (672/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  65% (682/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  66% (693/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  67% (703/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  68% (714/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  69% (724/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  70% (735/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  71% (745/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  72% (756/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  72% (758/1049), 180.01 KiB | 275.00 KiB/s\nReceiving objects:  73% (766/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  74% (777/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  75% (787/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  76% (798/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  77% (808/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  78% (819/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  79% (829/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  80% (840/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  81% (850/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  82% (861/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  83% (871/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  84% (882/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  85% (892/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  86% (903/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  87% (913/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  88% (924/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  89% (934/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  90% (945/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  91% (955/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  92% (966/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  93% (976/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  94% (987/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  95% (997/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  96% (1008/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  97% (1018/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  98% (1029/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects:  99% (1039/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects: 100% (1049/1049), 844.01 KiB | 737.00 KiB/s\nReceiving objects: 100% (1049/1049), 1.35 MiB | 1.11 MiB/s, done.\nResolving deltas:   0% (0/604)\nResolving deltas:   1% (7/604)\nResolving deltas:   5% (33/604)\nResolving deltas:   7% (44/604)\nResolving deltas:   8% (54/604)\nResolving deltas:   9% (56/604)\nResolving deltas:  10% (64/604)\nResolving deltas:  11% (69/604)\nResolving deltas:  13% (84/604)\nResolving deltas:  14% (86/604)\nResolving deltas:  15% (93/604)\nResolving deltas:  16% (101/604)\nResolving deltas:  17% (106/604)\nResolving deltas:  19% (118/604)\nResolving deltas:  23% (140/604)\nResolving deltas:  24% (145/604)\nResolving deltas:  26% (158/604)\nResolving deltas:  27% (164/604)\nResolving deltas:  28% (170/604)\nResolving deltas:  31% (190/604)\nResolving deltas:  34% (206/604)\nResolving deltas:  35% (213/604)\nResolving deltas:  36% (221/604)\nResolving deltas:  45% (273/604)\nResolving deltas:  46% (278/604)\nResolving deltas:  48% (290/604)\nResolving deltas:  49% (298/604)\nResolving deltas:  50% (304/604)\nResolving deltas:  52% (315/604)\nResolving deltas:  55% (335/604)\nResolving deltas:  56% (342/604)\nResolving deltas:  57% (346/604)\nResolving deltas:  59% (362/604)\nResolving deltas:  60% (363/604)\nResolving deltas:  71% (430/604)\nResolving deltas:  72% (435/604)\nResolving deltas:  73% (445/604)\nResolving deltas:  74% (447/604)\nResolving deltas:  75% (455/604)\nResolving deltas:  76% (461/604)\nResolving deltas:  77% (469/604)\nResolving deltas:  78% (473/604)\nResolving deltas:  79% (478/604)\nResolving deltas:  80% (488/604)\nResolving deltas:  81% (493/604)\nResolving deltas:  82% (498/604)\nResolving deltas:  83% (506/604)\nResolving deltas:  85% (516/604)\nResolving deltas:  88% (532/604)\nResolving deltas:  90% (546/604)\nResolving deltas:  91% (550/604)\nResolving deltas:  92% (556/604)\nResolving deltas:  93% (562/604)\nResolving deltas:  94% (572/604)\nResolving deltas:  95% (574/604)\nResolving deltas:  96% (580/604)\nResolving deltas:  97% (586/604)\nResolving deltas:  98% (592/604)\nResolving deltas:  99% (598/604)\nResolving deltas: 100% (604/604)\nResolving deltas: 100% (604/604), done.\nFilter download complete. Installing FilterSet...\nFilter completely installed.\n"
}
```

## DELETE `/filterset/:id/`
**설명**  
존재하는 필터셋을 삭제

**URL 파라미터**

|  키  |  타입  |     설명     |                  예시                   |
|------|--------|--------------|----------------------------------------|
|  `id`  | `String` |삭제할 필터셋 ID|                `"default"`                 |

**처리**
 * 해당하는 폴더를 삭제한다.


# Query API
## POST `/query`
**설명**
텍스트와 필터 목록이 주어지면, 텍스트를 차례로 필터 목록에 명시된 필터를 통과시킨다.

**요청 파라미터**  

|  키  |  타입  |     설명     |                  예시                   |
|------|--------|--------------|----------------------------------------|
|`filters`| `Array<String>` |  사용할 필터 목록  |        `['default.swearwords_nn']`        |
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
[
  ["miszehbrgbk", [ [9, 13], [19, 23] ]]
]
```
