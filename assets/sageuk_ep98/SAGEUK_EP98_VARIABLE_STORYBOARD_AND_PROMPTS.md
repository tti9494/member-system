# 「혈화의 궐」 EP98 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-06)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제98화 「왕관 없는 세 그림자」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제98화 「왕관 없는 세 그림자」` 절, 원전: 제98장 정본) + `characters.md` 캐릭터 앵커 + plan 지정 앵커(이환 — 평복/도포, 익선관을 벗어 풀밭에 내려둔 군왕이자 친구 / 이설화 — 사헌부 감규 관사 한복, 옥비녀, 차분하고 온화한 시선 / 강무결 — 무관복이 아닌 단정한 평복 도포, 편안한 동지) + EP22~EP97 원장 템플릿(동일 규격)
> **범위**: EP98 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP97 S8 엔드카드 「제99화 백일에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 24mm 와이드 · 꽃나무, 겨울 전 — 낙화원의 꽃나무 아래 세 사람 [내레이션/`ko-KR-Wavenet-C` (0.0): "그해 겨울이 오기 전에 — 세 사람은, 마지막으로 만났다." (rel 3.5=절대 2.5)], S2 50mm, 익선관을 벗어 둔 왕 [이환/`ko-KR-Neural2-C` (-1.5): "과인은 이 자리에 임금으로 왔다가 — 친구로 있는 중이다. 다시 가야 할 때가 되면 임금으로 돌아가겠다. 그러나 — 지금은 아니다." (rel 5.5=절대 9.5)], S3 85mm, 설화의 관찰 [설화/`ko-KR-Neural2-A` (0.0): "폐하께서는 임금이 되기 전에 — 사람이 되셨사옵니다." (rel 3.0=절대 17.0)], S4 85mm, 왕의 회수 [이환/Neural2-C (-1.5): "그것은 네가 가르쳐 준 것이다. 너는 과인에게 왕관이 아니라 — 종이의 값을 가르쳤다. 종이는 사람을 죽일 수 있다. 그러므로 종이를 쓰는 자는 — 그것이 누구를 죽일 것인지를 먼저 물어야 한다." (rel 6.5=절대 19.5)], S5 100mm Macro, "그 물음이 — 과인의 왕관보다 무거웠다" [이환/Neural2-C (-1.5): "그 물음을 가르쳐 준 것이 — 과인의 왕관보다 무거웠다." (rel 3.5=절대 32.0)], S6 35mm, 그날 밤까지 꽃나무 아래 (무대사), S7 100mm Macro, 꽃에 관하여 이야기하는 세 사람 [내레이션/Wavenet-C (0.0): "그들은 왕관에 관하여 이야기하지 않았다. 그들은 — 꽃에 관하여 이야기했다." (rel 4.0=절대 47.0)], S8 24mm 와이드 → 엔드카드, 세 그림자가 길어짐 → 암전 → 타이틀(자막: 제99화 「백일」에서 계속).
> **안티슬롭 ① — 삼인 우정 고양 극 배제(plan·정본 안티슬롭 지정)**: 우정 고양·성례식 톤·환한 웃음의 삼인 렌더 **0건**. 치환 — **그들은 왕관에 관하여 이야기하지 않았다 — 꽃에 관하여 이야기했다.** 담담한 대화의 무게(S1~S7 본체, S7이 명시 본체). `no friendship celebration, one quiet conversation` S1~S7 상설.
> **안티슬롭 ② — "당신 덕분입니다" 슬롭 배제(plan·정본 안티슬롭 지정)**: 감사 선언·신하의 예 찬미 렌더 **0건**. 치환 — **"너는 과인에게 왕관이 아니라 종이의 값을 가르쳤다... 그 물음을 가르쳐 준 것이 과인의 왕관보다 무거웠다."** — 종이의 값과 그 물음의 무게(S4·S5 본체). `no crown ode` S3·S4·S5·S7 상설.
> **왕 평복 앵커 유지(plan·정본 AG ⑥ 지정, EP93 계승)** — 이환은 **익선관을 벗어 풀밭 위에 내려둔 평복 차림**. 곤룡포·붉은 왕복·정관 착용 렌더 0건 — 익선관은 S1·S5·S6에서 **풀밭 위 내려둔 물건**으로만 등장(착용 0건, 생성기 `validate()` 앵커 이탈 가드 — gonryongpo·military uniform·red robe 어절 스캔 0건 단정 통과).
> **S2 임금이 아닌 자의 선언(plan·정본 지정)** — "과인은 이 자리에 임금으로 왔다가 — 친구로 있는 중이다"의 50mm 4비트(얼굴 — 빈 손 — 예법 없는 청취 — 친구로 앉는 고개 끄덕임). 예 표·합장·궁정 예법 렌더 0건.
> **S4 왕의 무거운 회수 고백(plan·정본 지정)** — "종이의 값"의 85mm 6비트 단독 최장 — 본화의 서사 본체. 찻잔 내려놓음 → 매트에 펴는 손 → 가르친 자의 눈 → 뒤집힌 빈 손 → 무거운 얼굴 → 침묵.
> **S5 풀밭 위 익선관과 세 사람의 손 매크로(plan·정본 지정)** — 100mm Macro 3비트. 매크로 한 프레임에 익선관과 세 사람의 손 — "왕관보다 무거운"의 본체.
> **S6 밤까지 이어지는 롱테이크(plan·정본 지정)** — 황혼(주전자 한 번 더) → 밤(화로 잔불)의 35mm 2비트 절제. 무대사 — 렌더 전면 무음.
> **S7 떨어진 꽃잎을 손에 쥐고(plan·정본 지정)** — "그들은 꽃에 관하여 이야기했다"의 100mm Macro 손 매크로 4비트 — 왕의 손가락 사이 마른 꽃 → 두 손 사이 전달 → 무결의 흉터 낸 손 → 세 찻잔 사이 내려놓인 꽃.
> **S8 석양→암전(plan·정본 지정)** — 석양에서 어둠으로 넘어가며 길어지는 세 사람의 그림자 24mm 와이드 → 균일 암전 → 타이틀. 암전 구간 인물 0명.
> **백지 설계 교칙(plan 절대 준수)** — 평상·천·기물 위 텍스트 일체 금지. **붉은 샬은 S08 타이틀 뿐**(시트 유일 의도 채색). 엔드카드 자막(제99화 「백일」에서 계속)은 편집 단계 삽입 — 시트에는 편집 참조용 카드로만.
> **무자막 원칙(100화 전편 규격)** — 화면 노출 문자 일체 금지. 내레이션 2구(S1·S7) + 이환 대사 3구(S2·S4·S5) + 설화 대사 1구(S3)는 편집 단계 사후 믹싱 — 시트와 렌더에 자막 활자를 그리지 않는다.
> **캐릭터 앵커(plan 지정)**: 이환 — **평복/도포, 익선관을 벗어 풀밭에 내려둔 군왕이자 친구**(곤룡포 0건). 이설화 — **사헌부 감규 관사 한복, 옥비녀, 차분하고 온화한 시선**. 강무결 — **무관복이 아닌 단정한 평복 도포, 편안한 동지**(융복·환도 0건, 뺨의 옅은 검흔 계승).
> **입모양 배제(100화 전편 규격)** — 내레이션 2구(S1·S7)·이환 3구(S2·S4·S5)·설화 1구(S3) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S6·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 내레이션 `ko-KR-Wavenet-C`(0.0 — plan 확정치) S1 1구+S7 1구 — 동일 배역(내레이션) 연속, 피치 사다리 충돌 없음. 이환 `ko-KR-Neural2-C`(-1.5 — plan 확정치) S2 1구+S4 1구+S5 1구 — 동일 배역 연속. 설화 `ko-KR-Neural2-A`(0.0 — plan 확정치) S3 1구 — 단일. 강무결 대사 0구 — 본화 무성. **세 배역이 서로 다른 ID — 본화 내 충돌 요소 0건**. 파일명 분리 규칙 기재(`EP98_S1_NARRATION`/`EP98_S7_NARRATION`/`EP98_S2_IHWAN`/`EP98_S4_IHWAN`/`EP98_S5_IHWAN`/`EP98_S3_SEOLHWA`). 렌더는 전 썬 무음.
> **가변 컷 배분**: 4/4/3/6/3/2/4/2 = 28컷 — EP13~EP97 전 배분(109종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68)+EP69 배분+EP13~EP97 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP97분 5/4/3/6/3/3/2/2와도 상이). **S4(왕의 회수 고백) 6컷 단독 최장** — "그 물음을 가르쳐 준 것이 과인의 왕관보다 무거웠다"가 이루어지는 본화의 서사 본체. S1(익선관을 벗어 둔 왕)·S2(친구로 있는 중)·S7(꽃에 관하여) 각 4컷, S3(설화의 관찰)·S5(왕관보다 무거운 물음) 각 3컷, **S6(밤까지 롱테이크)·S8(그림자→암전→타이틀) 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 10회(초벌 8 + 재렌더 2) 중 최종 채택 8장 — **재렌더 2건**: ① **해상도 1px 이탈(S02·S06)** — 초벌이 **1023×1537**(1024×1536 규격 위반 — EP94 S07·EP95 S05·EP96 S05·EP97 S02·S05 동일 결함 계승, 본화는 동시 2건) → 각 **1회 재렌더에서 1024×1536 정확 해소**(md5 S02 55660d73d16d·S06 f1901550ff47 — 탈락본 md5 S02 96ac9c5b5fb7·S06 e55ac23f0ab7 대조). 탈락본은 `images --out` 덮어쓰기로 미보존(실측 수치로만 기록). 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.31%(적색 타이틀 — 좌표 확인, **타이틀 열 x388~430·y770~1186 한정 — 의도 채색**). **전장 md5: S01 eefe022b5944 / S02 55660d73d16d(재렌더) / S03 f473d5f5822d / S04 c85ccd27cc0f / S05 1a9d161c2f23 / S06 f1901550ff47(재렌더) / S07 200cbd366cd2 / S08 9b629528b703**.
> **관찰 이력(결함 아님 판정 — 근거 기재)**: ① S03 설화가 검은 관모를 쓴 렌더(옥비녀 미노출) — S04 이후 전 패널 옥비녀·관사 한복 육안 확인. 물리 결함 0건이며 사용자 QA 철학("의상은 사실 상관없고 그냥 물리적으로 이상한 것만", 11-04) 기준 통과 — 이력만 기재. ② S06 패널1의 내려둔 관모가 S01·S05의 돔형 익선관과 달리 챙 달린 형태로 렌더 — 시트는 구도 가이드일 뿐이고 실사 단계는 본 원장의 `his black gilded ikseongwan cap set aside on the grass, never on his head` 지문이 지배하므로 실사 정합에 영향 0건.
> **검독 운영 교훈(EP67~EP97 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전(또는 컨텍스트 탈락본)을 돌려줄 수 있다** — 본화는 **별도 크롭 경로(`downloads/qc_crops/Z_EP98_*`) 재열람으로 현재본 판정**(전장 3분할 크롭 + S08 타이틀 확대 크롭). **어간 부분 문자열 함정 계승** — 금지 어휘의 어간 부분 문자열도 생성기 validate()가 차단(EP66 실측 계승). **정본 대사 직접 인용 주의(본화 신규)** — 정본 S4 대사의 "죽일 수 있다"는 영문 프롬프트에서 참견 어휘(`kill`)로 직역 불가 — `paper can take a person's life`로 치환 기입(생성기 STRIKE_WORDS 가드 통과 확인). **해상도 1px 이탈(S02·S06)** — 렌더 승여 응답은 ok여도 PIL 전량 재실측이 유일한 판정자이며, **동일 결함이 재렌더 1회로 해소되지 않을 수 있으므로 재실측→재렌더 루프를 해소까지 반복**한다(본화는 각 1회차 재렌더에 해소).
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제98화 「왕관 없는 세 그림자」 절(원전: 제98장 정본) 직접 열람**(417행 이하) — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. 원전 소설(`novel_s04_ch76_ch100.md` 제98장) 대조 — 익선관을 벗어 둔 왕("그는 그날, 사관들 앞에서 쓰던 것을 벗어 두고 왔다")·임금이 아닌 자의 선언·설화의 관찰("임금이 되기 전에 사람이 되셨사옵니다")·종이의 값과 그 물음의 무게·밤까지 꽃나무 아래·"왕관에 관하여 이야기하지 않았다 — 꽃에 관하여 이야기했다" 재확인. **S08 타이틀 슬롯**: 「제99화 백일에서 계속」 실제 글자수 **10자 = 1자 1슬롯 원칙에 따라 10슬롯** 확정(확대 크롭 검독 통과, 숫자 9·9 각각 단독 슬롯). **보이스 피치**: plan 확정치 채택(내레이션 Wavenet-C 0.0·이환 Neural2-C -1.5·설화 Neural2-A 0.0) — **characters.md 기재 이환 Pitch -0.5와 상이하나 plan 우선 원칙으로 -1.5 채택, 원장에 병기**. **가변 배분**: plan은 특정 배분 수치를 고정하지 않아 본화 서사에 맞춰 4/4/3/6/3/2/4/2=28컷으로 설계 — **총 컷수 28 규격 준수 + 선행 109종 미중복 기계 스캔**으로 이중 검증.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep98_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep98_sheets.py S01`), 전체는 `ALL`(명시적).

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 겨울 전 낙화원(저무는 하늘과 빛 바랜 잔디), 익선관의 검은 칠과 금장식, 설화 관복의 채도, 화로 잔불의 붉은 빛이 색으로 복원된다. **붉은 소품은 S6~S7 화로 잔불과 S8 석양빛뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화는 세 사람의 담담한 대화가 주인공** — 렌더 프레임 내 가독 문자 일체 0건.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **겨울 전 정지된 정원과 세 사람**(the still garden, the three at their ease), S2 **빈 손과 예법 없는 고개 끄덕임**(the empty hands, the plain nod), S3 **찻잔 너머의 시선**(the cup's rim, the level gaze), S4 **매트에 펴지는 손과 뒤집힌 빈 손**(the flattening hand, the open palm), S5 **풀밭 위 관모와 손**(the cap in the grass, the resting hands), S6 **하루가 저무는 단일 디밍**(the one even dimming, dusk into embers), S7 **마른 꽃의 느린 전달**(the slow passing of the dried flower), S8 **길어지는 그림자와 물러가는 빛**(the lengthening shadows, the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 S4 대사의 "죽일 수 있다"는 `paper can take a person's life`로 치환** — 참견 어휘 가드(`kill` 등) 통과 확인. 본화는 전쟁·유혈 요소 원천이 없는 대화 화이다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. 평상·천·기물 위 텍스트 일체 금지. 엔드카드 자막(제99화 「백일」에서 계속)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 2구(S1·S7)·이환 3구(S2·S4·S5)·설화 1구(S3)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S1·S5·S7 원거리·매크로 중심, S6·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이환 — 평복/익선관 벗어 둠(plan 지정)**: the young king Ihwan — a 24-year-old Korean man, pale with handsome fine features and deep thoughtful eyes, dressed in a plain dark everyday scholar's robe and overcoat with no royal garment at all, his head bare — his black gilded ikseongwan cap set aside on the grass, never on his head — sitting as a friend among friends, lips closed.
   - **이설화 — 감규 관사 한복·옥비녀(plan 지정)**: the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok at ease in the garden, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, a quietly warm and level gaze, lips closed.
   - **강무결 — 평복 도포·흉터(plan 지정)**: the warrior Mugyeol — a tall 25-year-old Korean man with a faint old scar on one cheek, dressed not in his military uniform but in a modest plain everyday robe and overcoat, steady heavy-lidded quiet eyes, an easy settled composure, lips closed.
   - **인물 상한**: S01 세 사람, S02 세 사람(이환 중심), S03 이환+설화, S04 이환+설화(무결 매트 가장자리), S05 손뿐(얼굴 0건), S06 세 사람, S07 손뿐(얼굴 0건), S8 세 사람(원경) → 암전 구간 인물 0명. 군중·인파 렌더 0건.
9. **광원 표기**: 겨울 전 낮광(정본 AG ① 지정) — S1 저무지 않는 낮고 하얀 겨울 전 햇살이 꽃나무 아래 납작하게 깔림. S2 같은 낮광이 왕의 얼굴과 손 위에. S3 같은 낮광이 설화의 시선 위에. S4 오후로 기운 빛이 손과 얼굴 위에. S5 늦은 오후의 낮은 빛이 풀밭 위 관모와 손 위에. S6 황혼의 청회빛에서 화로 잔불의 낮은 붉은빛으로 단일 균일 저하. S7 잔불의 낮은 빛과 마지막 하늘빛이 꽃과 손 위에 고르게 섞임. S8 석양이 세 그림자를 길게 늘이다 균일하게 물러가 균일 암전 진입·종결. `never flickering like horror, never strobing` 전 썬 상설. **EP97 관사 창살 가드를 본화 야외 낙화원 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 세 그림자·균일 암전 구간 이후의 붉은 타이틀(제99화 「백일」에서 계속, 10슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외** — 렌더 컷 리스트 합계 26컷 = 시트 28컷 − 타이틀 카드).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch **0.0** — plan 확정치, Speed 1.0, 무겁고 담담한 기록자 톤) — S1 1구·S7 1구. 이환 `ko-KR-Neural2-C` (Pitch **-1.5** — plan 확정치, Speed 1.0, 군왕의 낮고 무거운 선언 톤) — S2 1구·S4 1구·S5 1구. 설화 `ko-KR-Neural2-A` (Pitch **0.0** — plan 확정치, Speed 1.0, 서늘하고 온화한 확인 톤) — S3 1구. 강무결 — 대사 0구. 본화 캐릭터 대사 5구 + 내레이션 2구 + 엔드카드 자막 1건. S6·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 2구 — 동일 배역 연속. 이환 `Neural2-C`(-1.5) 3구 — 동일 배역 연속. 설화 `Neural2-A`(0.0) 1구 — 단일. **세 배역이 서로 다른 ID를 쓰므로 본화 내 충돌 요소 없음**. 파일명 분리 규칙 기재(`EP98_S1_NARRATION`/`EP98_S7_NARRATION`/`EP98_S2_IHWAN`/`EP98_S4_IHWAN`/`EP98_S5_IHWAN`/`EP98_S3_SEOLHWA`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/4/3/6/3/2/4/2 = 28컷 — EP13~EP97 전 배분 109종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S4 6컷 단독 최장**(회수 고백의 완급), S1·S2·S7 각 4컷, S3·S5 각 3컷, **S6·S8 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **왕관에 관하여 이야기하지 않았다 — 낭독이 아니라 그림이다(본화 핵심)**: 본화에는 우정 고양도 감사 선언도 없다 — 익선관을 벗어 둔 채 앉은 왕(S1)에서 친구로서의 선언(S2), 설화의 관찰(S3), 종이의 값에 대한 회수 고백(S4), 왕관보다 무거운 물음의 매크로(S5), 밤까지 이어지는 침묵의 동석(S6), 꽃잎을 손에 쥐고 꽃에 관하여 이야기하는 손(S7), 길어지는 세 그림자(S8)로 간다. 전 썬 `no friendship celebration, one quiet conversation(S1~S7), no crown ode(S3·S4·S5·S7)` 상설. 주제의 감정은 대사 낭독이 아니라 벗어 둔 관모(S1·S5)와 빈 손(S2·S4)과 꽃(S7)이라는 그림이다.

---

## 1. S01 첫째 — 익선관을 벗어 둔 왕 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP98_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 꽃나무. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0 — plan 확정치, Speed 1.0] "그해 겨울이 오기 전에 — 세 사람은, 마지막으로 만났다." (rel 3.5=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 4비트)** — 겨울 전 정원과 꽃나무 아래 세 사람(1) — 평복 차림 왕의 편안한 착석(2) — 풀밭 위 내려둔 익선관(3) — 세 찻잔의 담담한 마지막 만남(4). **안티슬롭 가드(plan 지정)** — 삼인 우정 고양 0건 — 프레임은 겨울 전 세 사람의 담담한 동석만 보여준다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three people in the garden and no one else. The young king Ihwan — a 24-year-old Korean man, pale with handsome fine features and deep thoughtful eyes, dressed in a plain dark everyday scholar's robe and overcoat with no royal garment at all, his head bare — his black gilded ikseon-gwan cap set aside on the grass, never on his head — sitting as a friend among friends. The magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, a quietly warm and level gaze. The warrior Mugyeol — a tall 25-year-old Korean man with a faint old scar on one cheek, dressed not in his military uniform but in a modest plain everyday robe and overcoat, steady quiet eyes. The royal garden Nakhwawon in the last mild days before winter, one old flowering tree bare of blossoms. No friendship celebration, one quiet conversation. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low white daylight of the last mild days before winter, lying flat under the bare tree, is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the winter daylight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide: the winter-before garden — the old flowering tree standing bare of blossoms, and beneath it three figures gathered around a low wooden mat, seen plain and still.
2. 35mm medium-wide: across the mat — the king among them, at his ease, his head bare and his posture easy.
3. 50mm medium: the black gilded ikseongwan cap set aside on the grass beside the mat — the king came without his crown.
4. 35mm medium-wide: three cups on the mat between them and the winter-before daylight lying flat under the tree — the last meeting kept ordinary.

GARDEN MOTION — IMPORTANT: physically-based the still garden, the three at their ease — the frame shows three friends under a tree and nothing else: the garden holds its stillness in the winter-before light, the king sits easy and bare-headed among his friends, the gilded cap rests in the grass like any left-behind thing, and three cups stand on the mat in an ordinary last meeting; no friendship celebration, one quiet conversation; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 임금이 아닌 자의 선언 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP98_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [임금이 아닌 자의 선언 · 이환/`ko-KR-Neural2-C`, Pitch -1.5 — plan 확정치, Speed 1.0] "과인은 이 자리에 임금으로 왔다가 — 친구로 있는 중이다. 다시 가야 할 때가 되면 임금으로 돌아가겠다. 그러나 — 지금은 아니다." (rel 5.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **친구 선언 썬(가변 4비트)** — 담담하게 말을 시작하는 왕의 얼굴(1) — 무릎 위 예물 없는 빈 손(2) — 예 표 없이 듣는 두 사람(3) — 친구로 앉아 있다는 고개 끄덕임(4). **안티슬롭 가드(plan 지정)** — 우정 고양·예법 연기 0건 — 선언은 프레임에서 자세와 빈 손으로만 도달한다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three people around the low wooden mat under the bare flowering tree. The young king Ihwan — a 24-year-old Korean man, pale with handsome fine features and deep thoughtful eyes, dressed in a plain dark everyday scholar's robe and overcoat with no royal garment at all, his head bare, his gilded ikseon-gwan cap set aside on the grass — sitting as a friend among friends, lips closed. The magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok with a simple jade hairpin, calm clear cool eyes, lips closed. The warrior Mugyeol — a tall 25-year-old Korean man with a faint old scar on one cheek in a modest plain everyday robe, lips closed. No bowing, no ranks observed, no court ceremony anywhere. No friendship celebration, one quiet conversation, no crown ode. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same low white winter-before daylight on his face and hands is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the winter daylight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm close: the king's face settling plainly as he begins — what he says arrives later by voice, the saying itself kept level and unhurried.
2. 50mm close: his hands resting open on his knees — no sceptre, no seal, nothing kingly in them.
3. 50mm medium: Seolhwa and Mugyeol listening without ceremony — no bowing, no ranks, three people around a mat.
4. 50mm close: a nod passing between the three of them — he will go back a king when it is time; today he stays a friend, sitting as a friend.

FRIEND MOTION — IMPORTANT: physically-based the empty hands, the plain nod — the whole scene is one declaration made as a friend and nothing else: his face settles plainly and level as he begins, his hands rest open on his knees empty of every kingly thing, the two friends listen without bowing or ceremony, and a small nod passes between the three — he will go back a king when it is time, and today he stays a friend; no friendship celebration, one quiet conversation, no crown ode; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 설화의 관찰 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP98_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 확인 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "폐하께서는 임금이 되기 전에 — 사람이 되셨사옵니다." (rel 3.0=절대 17.0, 사후 믹싱)
- **연출 특이**: **관찰 썬(가변 3비트)** — 찻잔 너머 왕을 보는 설화의 차분한 시선(1) — 수준 있게 말하는 작고 정중한 고개끄덕임(2) — 신하의 감사가 아니라 사람으로 받는 왕(3). **안티슬롭 가드(plan 지정)** — 찬미·감사 선언 0건 — 그 말은 관찰이지 찬가가 아니다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two people in the frame: the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, a quietly warm and level gaze, lips closed — and the young king Ihwan — a 24-year-old Korean man, pale with handsome fine features and deep thoughtful eyes, in a plain dark everyday scholar's robe, his head bare, his gilded ikseon-gwan cap set aside on the grass, lips closed. Her gaze at him is a cool precise observation, never an upturned admiring look, never a subject's flattery. No friendship celebration, one quiet conversation, no crown ode. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same winter-before daylight on her face and his is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the winter daylight's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close: Seolhwa watching the king over the rim of her cup — a cool, precise and unhurried observation.
2. 85mm close: her small formal nod — the observation said in her level way, the words arriving later by voice.
3. 85mm close: the king receiving it — a man first, and a king only after; the thanks of a subject nowhere in it.

OBSERVATION MOTION — IMPORTANT: physically-based the cup's rim, the level gaze — the scene is one observation said plainly and nothing else: she watches him over the rim of her cup with a cool precise unhurried gaze, she gives one small formal nod as the observation is said in her level way, and he receives it as a man first and a king only after, with no subject's thanks anywhere in it; no friendship celebration, one quiet conversation, no crown ode; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 왕의 회수: 종이의 값 (절대 22.5~30.0 · 콘티 6컷 ★ 단독 최장)

- **시트**: `downloads/EP98_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [무거운 고백 · 이환/`ko-KR-Neural2-C`, Pitch -1.5 — plan 확정치, Speed 1.0] "그것은 네가 가르쳐 준 것이다. 너는 과인에게 왕관이 아니라 — 종이의 값을 가르쳤다. 종이는 사람을 죽일 수 있다. 그러므로 종이를 쓰는 자는 — 그것이 누구를 죽일 것인지를 먼저 물어야 한다." (rel 6.5=절대 19.5, 사후 믹싱)
- **연출 특이**: **회수 고백 썬(가변 6비트 단독 최장 — 본화의 서사 본체)** — 찻잔 내려놓음(1) — 매트에 천천히 펴지는 손(2) — 가르친 자의 고요한 눈(3) — 뒤집힌 빈 손(4) — 무거운 생각의 얼굴(5) — 왕관보다 무거운 침묵(6). **안티슬롭 가드(plan 지정)** — "당신 덕분입니다" 감사 슬롭 0건 — 왕은 가르침을 고백하지 찬사를 받지 않는다. **정본 대사 주의** — "죽일 수 있다"는 `paper can take a person's life`로만 영문 기입.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king Ihwan — a 24-year-old Korean man, pale with handsome fine features and deep thoughtful eyes, in a plain dark everyday scholar's robe and overcoat, his head bare, his gilded ikseon-gwan cap set aside on the grass, lips closed — and the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, lips closed — at the mat's edge, saying nothing. His gaze holds the weight of a lesson confessed, never a king accepting praise, never a subject's thanks. No friendship celebration, one quiet conversation, no crown ode. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon slant of the winter-before daylight on his hand and face is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 6 panels in order as one continuous ~10 second sequence:
1. 85mm close: the king setting his cup down on the mat — the talk turning quietly to what paper is worth.
2. 85mm close: his hand flattening slowly on the mat between them — the weight of the lesson arriving.
3. 85mm close: Seolhwa's eyes steady on him — the one who taught the king the value of paper, saying nothing.
4. 85mm close: his hand turning over, empty and open — paper can take a person's life; the open hand says it first.
5. 85mm close: his face heavy with the thought — the hand that writes must first ask whom the paper will take.
6. 85mm close: the silence after — the lesson sitting on the mat between the three of them, heavier than a crown.

CONFESSION MOTION — IMPORTANT: physically-based the flattening hand, the open palm — the scene's longest breath and its whole point: the king sets his cup down as the talk turns to what paper is worth, his hand flattens slowly on the mat under the weight of the lesson, Seolhwa's eyes stay steady on him saying nothing, his hand turns over empty and open because paper can take a person's life, his face carries the thought that the hand which writes must first ask whom the paper will take, and the silence after sits on the mat heavier than a crown; no friendship celebration, one quiet conversation, no crown ode; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 왕관보다 무거운 물음 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP98_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. [무거운 결론 · 이환/`ko-KR-Neural2-C`, Pitch -1.5 — plan 확정치, Speed 1.0] "그 물음을 가르쳐 준 것이 — 과인의 왕관보다 무거웠다." (rel 3.5=절대 32.0, 사후 믹싱)
- **연출 특이**: **매크로 썬(가변 3비트)** — 매트 위 접힌 왕의 두 손(1) — 한 프레임에 풀밭 위 익선관과 세 사람의 손(2) — 가만히 가라앉는 손(3). **안티슬롭 가드(plan 지정)** — 왕관은 무게에서 지고, 찬사는 없다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: the young king Ihwan's two hands from the sleeves of a plain dark everyday scholar's robe, and beside them in one frame the resting hands of the magistrate Seolhwa (dignified magistrate's hanbok sleeves) and of the warrior Mugyeol (modest plain everyday robe sleeves). One black gilded ikseon-gwan cap lying in the thinning grass — set aside, never worn. No friendship celebration, one quiet conversation, no crown ode. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low late-afternoon winter-before light on the cap and the hands is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the late light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the king's two hands folded together on the mat — the weight of what was taught him resting in them.
2. 100mm macro: the gilded ikseongwan cap in the thinning grass and, beside it in one frame, the three friends' hands at rest — the cap and the lesson together, the lesson heavier.
3. 100mm macro: his hands stilling at their rest — what taught him this outweighs his crown.

WEIGHT MOTION — IMPORTANT: physically-based the cap in the grass, the resting hands — the scene is one held weight and nothing else: the king's folded hands rest on the mat with the weight of what was taught him, one frame carries both the gilded cap in the grass and the three friends' hands beside it with the lesson the heavier of the two, and his hands go still at their rest because what taught him this outweighs his crown; no friendship celebration, one quiet conversation, no crown ode; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 그날 밤까지 꽃나무 아래 (절대 37.5~45.0 · 콘티 2컷 ★ 절제 롱테이크)

- **시트**: `downloads/EP98_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. 무대사 — 렌더 완전 무음.
- **연출 특이**: **롱테이크 썬(가변 2비트 절제)** — 청회빛 황혼, 주전자 한 번 더, 그래도 꽃나무 아래(1) — 밤, 화로 잔불 아래 낮게 비춰지는 세 사람, 말은 침묵과 동석으로(2). **안티슬롭 가드(plan 지정)** — 머무는 것이 전체 이벤트다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three people under the bare flowering tree: the young king Ihwan — a 24-year-old Korean man in a plain dark everyday scholar's robe, head bare, his gilded ikseon-gwan cap set aside on the grass, lips closed; the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok with a simple jade hairpin, calm clear cool eyes, lips closed; the warrior Mugyeol — a tall 25-year-old Korean man with a faint old scar on one cheek in a modest plain everyday robe, lips closed. The teapot refilled once on the mat, then a small brazier of low embers at night. No friendship celebration, one quiet conversation. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the light falls from blue-grey dusk to the brazier's low ember-glow in one even continuous dimming and nothing else — the embers light the three from below without a single flare-up. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the ember light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 35mm wide: dusk gathering blue-grey over the winter-before garden — the teapot refilled once, the three still under the bare tree, the talk going quietly on.
2. 35mm wide: night — the brazier's low embers lighting the three from below, the bare tree over them, the talk settled to silence and company.

STAY MOTION — IMPORTANT: physically-based the one even dimming, dusk into embers — the scene has no dialogue, the staying is the whole event: the day dims blue-grey over the garden while the teapot is refilled once and the three remain under the tree, and night comes with the brazier's low embers lighting them from below as the talk settles into silence and company; no friendship celebration, one quiet conversation; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 꽃에 관하여 이야기하는 세 사람 (절대 45.0~52.5 · 콘티 4컷)

- **시트**: `downloads/EP98_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0 — plan 확정치, Speed 1.0] "그들은 왕관에 관하여 이야기하지 않았다. 그들은 — 꽃에 관하여 이야기했다." (rel 4.0=절대 47.0, 사후 믹싱)
- **연출 특이**: **꽃 매크로 썬(가변 4비트 — "꽃에 관하여 이야기했다"의 명시 본체)** — 왕의 손가락 사이 마른 꽃(1) — 두 손 사이 전달(2) — 무결의 흉터 낸 넓은 손(3) — 세 찻잔 사이 내려놓인 꽃(4). **안티슬롭 가드(plan 지정)** — 왕관은 이야기가 아니라 이야기하지 않은 것이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: the young king Ihwan's fingers from the sleeves of a plain dark everyday scholar's robe; the magistrate Seolhwa's hand from the sleeves of a dignified magistrate's hanbok; and the warrior Mugyeol's broad scarred hand resting open near the mat's edge. One dried last flower of the year — the last of the winter-before garden's flowers — held, passed and set down among three cups on the mat. No friendship celebration, one quiet conversation, no crown ode. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the brazier's low ember light and the last sky-light mixing evenly on the flower and the hands is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the ember light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro: a dried last flower of the year held between the king's fingers — the talk gone quietly to flowers.
2. 100mm macro: the dried flower passing between two hands — the king's to Seolhwa's, its colour talked of rather than shown.
3. 100mm macro: Mugyeol's broad hand resting open nearby — the third friend listening, saying nothing, part of it all the same.
4. 100mm macro: the dried flower set down on the mat between the three cups — they did not talk of crowns; they talked of flowers.

FLOWER MOTION — IMPORTANT: physically-based the slow passing of the dried flower — the scene is one small dried thing carrying the whole night's record: the flower turns slowly between the king's fingers as the talk goes quietly to flowers, it passes from his hand to hers with its last year's colour talked of rather than shown, the third friend's broad scarred hand rests open nearby saying nothing, and the flower is set down on the mat between the three cups — they did not talk of crowns, they talked of flowers; no friendship celebration, one quiet conversation, no crown ode; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 세 그림자 → 암전 (절대 52.5~60.0 · 콘티 2컷)

- **시트**: `downloads/EP98_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제99화 「백일」에서 계속(편집 단계 삽입).
- **연출 특이**: **종지 썬(가변 2컷)** — 석양에서 어둠으로 넘어가며 길어지는 세 사람의 그림자 와이드(1), 타이틀 카드(편집 참조용)(2). **암전 구간 인물 0명** — 우정은 노래하지 않는다, 하루가 끝날 뿐이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — three figures only, seen wide and from a distance, no face in focus: the young king Ihwan in a plain dark everyday scholar's robe, head bare; the magistrate Seolhwa in her dignified magistrate's hanbok with a jade hairpin; the warrior Mugyeol in a modest plain everyday robe — the three at rest by the bare flowering tree as the sun goes down over the Nakhwawon garden and their shadows lengthen long across the thinning grass. No friendship celebration, no finale tableau, no looking back. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the sunset is the only light, and it dims evenly off the garden and the three figures as the episode closes — the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the sunset's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence (the sheet's second panel — the red next-episode title card — is edit-stage reference only and is NOT rendered):
1. 24mm wide: the sun going down over the garden — the three friends' shadows lengthening long across the thinning grass from the tree, then the light dimming evenly until complete black.

SHADOW MOTION — IMPORTANT: physically-based the lengthening shadows, the even leaving of the light — the episode closes as a day and not as a statement: the sun goes down over the garden, the three friends' shadows lengthen long across the thinning grass from the bare tree, and the light withdraws evenly until nothing remains — complete black, held; no friendship celebration, no finale fanfare, no 'the end' mood; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
