# 「혈화의 궐」 EP84 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제84화 「어전의 대치」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제84화 「어전의 대치」` 절, 원전: 제84장 정본) + `characters.md` 캐릭터 앵커(이환 붉은 곤룡포·익선관, 윤경헌 흑립·홍단령, 이설화 옥비녀 궁녀 복식) + EP21~EP83 원장 템플릿(동일 규격)
> **범위**: EP84 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP83 S8 엔드카드 「제84화 어전의 대치에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 24mm 와이드 · 빈 어전, 근정전의 뜰 — 옥좌의 왕과 그 옆의 설화, 둘뿐 [내레이션/Wavenet-C (0.0): "윤경헌이 근정전의 뜰에 들어섰을 때 — 어전은 비어 있었다." (rel 3.5=절대 2.5)], S2 50mm, 왕의 사실 열거 [이환/Neural2-C (-1.5): "네 군사는 문 밖에서 멈추었다. 너는 이제 — 칼도, 종이도, 군사도 없이 어전에 와 있다." (rel 4.5=절대 9.5)], S3 85mm, 윤경헌의 반박 [윤경헌/Wavenet-D (-2.0): "종이는 칼이 아니다. 종이는 — 사람이 사람을 부르는 이름이다. 나는 지금도 — 사람들을 부를 수 있다." (rel 5.0=절대 17.0)], S4 50mm, 설화가 계단에서 내려와 세 걸음 앞에 섬 [설화/Neural2-A (0.0): "그렇다면 — 불러 보시옵소서." (rel 2.5=절대 24.0)], S5 85mm, 이름들의 소진 [설화/Neural2-A (0.0): "호남의 군벌 세 곳, 흑영대의 잔당 서른, 그리고 궐 안의 상궁 하나 — 폐하께서는 그것을 다 아시옵니다. 마마께서는 폐하께 그 이름들을 바치셨사옵니다. 어젯밤에." (rel 6.0=절대 32.0)], S6 100mm Macro, 윤경헌의 웃음이 멎는 얼굴 [처음으로 멎는 무언 — 윤경헌/Wavenet-D (-2.0): "…" 무대사] **★ 킬러 매크로**, S7 85mm, 세 걸음의 거리 (무대사), S8 35mm → 엔드카드, 어전에 남은 세 사람 → 암전 → 타이틀(자막: 제85화 「계약서의 이름」에서 계속).
> **안티슬롭 ① — 권신 마지막 저주 고함 배제(plan·정본 안티슬롭 지정)**: 저주 고함·절규·분노 그리마스·마지막 협박 대사 렌더 **0건**. 치환 — **십 년간 얼굴에 새겨져 있던 서늘한 미소가 스르륵 사라지는 윤경헌의 얼굴 매크로**: 공포는 소리가 아니라 미소가 빠지는 속도다. `no cursed shouting, no rage grimace, no screaming old man` 전 썬 상설.
> **안티슬롭 ② — 왕의 승리 연설 배제(plan·정본 안티슬롭 지정)**: 승리 연설·오라이언·주먹 치켜든 왕·개선 포즈 렌더 **0건**. 치환 — **"네 군사는 문 밖에서 멈추었다"의 담담한 사실의 열거**: 왕은 옥좌에 앉아 손을 모은 채 사실만 놓는다. `no victory oration, no raised voice, no triumph` 전 썬 상설.
> **S6 ★ 킬러 매크로(plan 지정)** — 윤경헌의 웃음이 멎는 순간 — **십 년 만에 처음으로 멎는 무언("…")**. 사람을 향한 위협 동작 0건, 대사 0구 — 매크로 7비트로 미소의 소멸만을 세운다(1~10 가변 원칙). `the pivotal cut` 지칭(`kill` 어간 차단 계승 — EP66 실측). 정본 무언 지문은 사후 믹싱 — 렌더 완전 무음.
> **백지 설계 교칙(전편 규격)** — 프레임 내 문서·기물 위 가독 글자 **0건** — 아예 판독 불가. 본화는 화면에 종이가 등장하지 않는 회차지만 **S5 이름들의 소진도 이름을 화면에 쓰지 않는다** — 이름은 말로만 존재하고 목록·문서 렌더 0건. `no letterforms, no hangul, no hanja` 전 썬 상설.
> **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계 참조용)뿐**(본화는 가독 허용 인서트 없음). 엔드카드 자막(제85화 「계약서의 이름에서 계속」)은 편집 단계 삽입, S08 렌더는 암전으로 끝난다.
> **세이프티 가드(plan 절대 준수) — 유혈 직결 어휘 0건**: 본화는 전투 접촉이 화면에 없다 — 대치는 말과 세 걸음의 거리로만 이루어진다. `no blood, no wound, no injury anywhere` 전 썬 상설. `all characters are adults` 전 썬 상설. 참견 어휘 가드(`slash`·`stab`·`execution`·`kill` 등)도 생성기 `validate()`로 전수 차단 확인 — **'킬러 매크로' 지칭도 렌더 텍스트에서는 `the pivotal cut`으로 치환**(어간 부분 문자열 차단 — EP66 실측 계승). **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이환 — **옥좌 위 붉은 곤룡포·익선관, 군왕의 담담한 사실 열거**(characters.md 이환 앵커 계승, 24세 — 창백하나 수려한 이목구비, 깊은 우수와 숨겨진 분노가 서린 눈빛, 금용단). 윤경헌 — **홍단령 흑립 노년 권신, 십 년 만에 처음으로 웃음이 멎는 얼굴**(짙은 흑립·금실 홍단령·백옥 흉배·매의 눈·권력의 무게가 담긴 주름 앵커 계승, 58세). 이설화 — **옥비녀 궁녀 복식, 계단을 내려와 세 걸음 앞에 서서 이름의 소진을 고하는 차가운 눈빛**(다크 파스텔 톤 단아한 궁녀 한복, 소박한 옥비녀, 창백한 피부, 서늘하고 총명한 눈빛, 21세). **인물 상한(정본 AG ⑥)** — S01 2인(이환·설화), S02~S06 1인 주연(+S02 원경 병사 실루엣·얼굴 0건), S07 3인(거리 유지), S08 3인.
> **S1 인원 정본 우선(plan 표기 대조)**: plan 연출 목록의 "S1 빈 어전의 하이키 역광과 **세 사람**의 기하학적 정적"은 정본 S1 미장센 "옥좌의 왕과 그 옆의 설화, **둘뿐**"과 상충 — **정본표 기계 대조 우선 원칙**에 따라 S1은 둘뿐으로 렌더하고, **세 사람의 기하학적 정적은 정본 S7(세 걸음의 거리)·S8(어전에 남은 세 사람)에서 실현**(S07·S08 시트 확인).
> **입모양 배제(100화 전편 규격)** — 캐릭터 대사 4구(S2 이환, S3 윤경헌, S4·S5 설화) + 내레이션 1구(S1) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S6(무언 "…")·S7·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검**: 내레이션 `ko-KR-Wavenet-C`(Pitch 0.0, Speed 0.9, 무거운 나레이션) 1구(S1), 이환 `ko-KR-Neural2-C`(Pitch -1.5, 무거운 사실의 열거) 1구(S2), 윤경헌 `ko-KR-Wavenet-D`(Pitch -2.0, 나이 들어 날카로워진 냉소) 1구(S3 — S6은 무언), 설화 `ko-KR-Neural2-A`(Pitch 0.0, 서늘한 응수) 2구(S4·S5) — **동일 ID 충돌 없음**(Wavenet-C 대 Wavenet-D, Neural2-C 대 Neural2-A는 보이스 문자가 상이 — 사다리 충돌 0건, 단일 트랙 연속 합성 가능). 파일명: `EP84_S1_NARRATION` / `EP84_S2_HWAN` / `EP84_S3_YOON` / `EP84_S4_SEOLHWA` / `EP84_S5_SEOLHWA`. 렌더는 전 썬 무음.
> **가변 컷 배분**: 2/4/3/4/5/7/1/2 = 28컷 — EP13~EP83 전 배분(95종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP83 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP83분 2/4/3/7/5/2/3/2와도 상이). **S6(★ 킬러 매크로, 멎는 미소) 7컷 단독 최장** — 십 년 미소가 스르륵 빠지는 것을 7비트로 세움(1~10 가변 원칙). S5(이름들의 소진) 5컷, S2(사실의 열거)·S4(세 걸음의 하강) 각 4컷, S3(반박) 3컷, **S1(빈 어전)·S8(남은 세 사람→암전→타이틀) 각 2컷, S7(세 걸음의 거리, 무대사) 1컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 정정 기록**: 총 이미지 생성 11회(초벌 8 + 재렌더 3) 중 최종 채택 8장 — **초벌 결함 2류**. ① S02 초벌의 MOOD 박스 "FACTS, QUIETLY"가 **적색 렌더**(S01~S07 무채색 규격 위반 — PIL 크로마 실측 0.47%로 포착, 픽셀 좌표 y≈1366 하단 MOOD 박스) → 생성기에 **비 S08 시트 전면 무채색 락 문단 신설**(MOOD 붉은 글씨 명시 차단) 후 재렌더, 재실측 **0.00%** 정정. ② S05 초벌의 마지막 패널이 설화를 **폐하께 고개 숙인 자세로 렌더**(캐릭터 앵커·S06~S07 기립 연속성 위반) → 패널 지문에 `no one kneels, no one bows` 명시 후 재렌더 정정. **단, S02 초벌 결함본은 재렌더 과정에서 덮어써 증적 미보존**(운영 실수 — S05 결함본은 `downloads/_EP84_S05_V1_defect_kneeling.jpg` 보존, S02의 정정 전 테이크 1회분 `downloads/_EP84_S02_superseded_take_clean.jpg`만 남음). 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**, 가시 채색(chroma>25 ∧ 최대명도>64) S01~S07 전장 0.00%·S08 0.25%(적색 타이틀 — 좌표 전수 확인, 타이틀 열 x377~408·y714~1146 한정). 생성기 `validate()`(컷수·배분 중복·세이프 어휘·uprising/letterform/light/lips 가드) → 렌더 → PIL 전량 실측 → **8장 전량 육안 검독 + 확대 크롭 검독(S08 타이틀 14슬롯 `downloads/qc_crops/Z_EP84_S08_TITLE_ZOOM.png`, 4번째 슬롯 6배 확대 `downloads/qc_crops/Z_EP84_S08_TITLE_SLOT4.png`, S05 초벌 결함 증적 `downloads/_EP84_S05_V1_defect_kneeling.jpg`)**. **검독 캐시 함정 재확인(EP67~EP83 계승)**: 재렌더 판정은 신규 실측(PIL)+재열람으로 수행.
> **plan 기재 대사·슬롯 최종성 확인(팩트체크)**: plan 기재 엔드카드 「제85화 계약서의 이름에서 계속」은 타이틀 실제 글자수가 **14자**(제/8/5/화/계/약/서/의/이/름/에/서/계/속) — **1자 1슬롯 원칙에 따라 14슬롯** 확정(**plan 기재 "13슬롯"은 글자수 오차** — 공백 슬롯 삽입 없음, 숫자 8·5는 각각 단독 슬롯 — EP73~EP83 1자 1슬롯 규격 계승, 확대 크롭 검독 통과). **plan 기재 "13슬롯 단일 세로 열" 대신 실제 글자수 14슬롯으로 렌더·기록** — 1자 1슬롯 원칙과 기계 실측(글자수 14)이 우선(EP83의 12→13슬롯 정정과 동일 유형). 정본 대사·보이스 ID·rel/절대 수치는 `SEASON_04_MASTER_SCREENPLAY.md` 제84화 절(164~178행) 직접 열람 재대조 — plan과 1:1 일치. **plan의 썬별 rel/절대 수치(S1 rel 3.5=절대 2.5, S2 rel 4.5=절대 9.5, S3 rel 5.0=절대 17.0, S4 rel 2.5=절대 24.0, S5 rel 6.0=절대 32.0)와 렌즈·무빙·보이스 지문 전 항목 정본표와 일치**. **plan 배분 기재 "선행 전 배분 95종"과 실측 95종 일치** — 기계 스캔 수치가 우선.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep84_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep84_sheets.py S01`), 전체는 `ALL`(명시적).

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (빈 어전 하이키 역광 가드) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 이환 붉은 곤룡포(금용단)의 채색, 윤경헌 홍단령의 검붉은 채색, 빈 어전 하이키 역광의 실제 색이 실제 색으로 복원된다. **붉은 색은 S08 붉은 타이틀(편집 단계 삽입)뿐** — 그 외 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **열린 문으로 쏟아지는 역광과 가만히 선 두 사람**(the pouring backlight, the standing stillness), S2 **모아 둔 손과 문 밖에서 멈춘 병사**(the folded hands, the halted soldiers), S3 **새겨진 미소와 가만히 선 노신**(the carved smile, the standing stillness), S4 **측정된 하강 걸음과 멈춘 거리**(the measured descent, the stopped distance), S5 **말해지는 이름과 가만히 알고 있는 손**(the spoken names, the knowing hand), S6 **빠져나가는 미소와 가라앉는 주름**(the dissolving smile, the settling wrinkles), S7 **움직이지 않는 거리와 역광의 먼지**(the held distance, the dust in the backlight), S8 **어두워지는 새벽과 남은 세 사람**(the darkening dawn, the three who remain).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no blood, no wound, no injury anywhere` 전 썬 상설. `all characters are adults` 전 썬 상설. **'킬러 매크로' 지칭은 렌더 텍스트에서 `the pivotal cut`으로 치환**(`kill` 어간 차단). **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. `no letterforms, no hangul, no hanja` 전 썬 상설. **이름·목록은 말로만 존재 — 화면 문서·목록 렌더 0건**. 엔드카드 자막(제85화 「계약서의 이름에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 대사 4구(S2·S3·S4·S5)와 내레이션 1구(S1)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S6·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이환(plan·characters.md 지정)**: the young King, Hwan — a 24-year-old Korean king with a pale but finely handsome face, wearing a red gonryongpo royal robe and a black silk crown, deep sorrow and hidden fury settled into stillness in his eyes, seated perfectly calm, lips closed.
   - **윤경헌(plan·characters.md 지정)**: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power, hawk eyes, standing in the empty throne hall with an unhurried cold bearing, lips closed.
   - **이설화(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes, a resolved unyielding bearing, lips closed.
   - **인물 상한(정본 AG ⑥)**: S01 2인(이환·설화), S02 이환 1인(+문 밖 원경 병사 실루엣·얼굴 0건), S03 윤경헌 1인, S04 설화·윤경헌, S05 설화·윤경헌(+이환 손), S06 윤경헌 1인, S07 3인(거리 유지), S08 3인 — 군중·대열 렌더 0건.
9. **광원 표기**: 전 썬 — **열린 큰문으로 쏟아지는 빈 어전의 하이키 역광이 유일한 광원**(S1~S7 고명도 역광, S8 후반 균일 암전 진입). `The high-key backlight through the open doors is the only light, never flickering like horror, never strobing` 전 썬 상설. **EP83의 새벽 수문 회색빛 가드를 본화 실내 어전에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지(EP78 밤 등불 가드와 동일 원칙).
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 남은 세 사람·균일 암전 구간 이후의 붉은 타이틀(제85화 「계약서의 이름에서 계속」)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1 1구. 이환 `ko-KR-Neural2-C` (Pitch -1.5) — S2. 윤경헌 `ko-KR-Wavenet-D` (Pitch -2.0) — S3. 설화 `ko-KR-Neural2-A` (Pitch 0.0) — S4·S5. 본화 캐릭터 대사 4구 + 내레이션 1구 + 엔드카드 자막 1건, 효과음 0건. S6·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0)·이환 `Neural2-C`(-1.5)·윤경헌 `Wavenet-D`(-2.0)·설화 `Neural2-A`(0.0) — **동일 모델 내 상이 보이스 문자, 사다리 충돌 없음, 단일 트랙 연속 합성 가능**. 파일명 분리 규칙 기재(`EP84_S1_NARRATION`/`EP84_S2_HWAN`/`EP84_S3_YOON`/`EP84_S4_SEOLHWA`/`EP84_S5_SEOLHWA`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 2/4/3/4/5/7/1/2 = 28컷 — EP13~EP83 전 배분 전수 대조 미중복(생성기 `validate()` 단정 통과). **S6 7컷 단독 최장**(킬러 매크로 — 멎는 미소), S5 5컷(이름들의 소진), S2·S4 각 4컷, S3 3컷, **S1·S8 각 2컷, S7 1컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **말과 거리의 대치 가드(본화 핵심)**: 어전의 대치는 칼도 종이도 없이 — 말의 열거와 세 걸음의 거리로만 이루어진다. 전 썬 `no fighting, no combat, no crowd-uprising spectacle` 상설. 승부의 순간(S6 미소 멎음)은 소리 없이 얼굴에서만 일어난다.

---

## 1. S01 첫째 — 빈 어전 (절대 00.0~07.5 · 콘티 2컷)

- **시트**: `downloads/EP84_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 빈 어전. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "윤경헌이 근정전의 뜰에 들어섰을 때 — 어전은 비어 있었다." (rel 3.5=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 2컷 절제)** — 뜰에서 본 빈 어전의 하이키 역광(1) — 옥좌의 왕과 그 옆의 설화, 둘뿐의 기하학적 정적(2). **안티슬롭 가드(plan 지정)** — 빈 어전은 무기가 아니라 무대 자체다. **정본 우선 확인** — plan 기재 "세 사람의 기하학적 정적"은 정본 미장센 "둘뿐"과 상충하여 S1은 둘뿐으로 렌더, 세 사람 정적은 S7·S8에서 실현.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly two figures in the hall: the young King, Hwan — a 24-year-old Korean king with a pale but finely handsome face, wearing a red gonryongpo royal robe and a black silk crown, deep sorrow and hidden fury settled into stillness in his eyes, seated perfectly calm on the high throne — and the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes, a resolved unyielding bearing — standing beside the dais; the vast empty hall holds no one else, no guards, no ministers, no court; no crowd-uprising spectacle, no battle carnage. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, a bright cold wash down the vast empty hall. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 24mm wide: the throne hall Geunjeongjeon from the courtyard — the great doors open, high-key backlight pouring through, the hall beyond empty.
2. 24mm wide: inside the hall — on the high throne the young king in red, and beside the dais the court lady — the only two, in geometric stillness.

BACKLIGHT MOTION — IMPORTANT: physically-based the pouring backlight, the standing stillness — the empty stage: the hall seen empty from the courtyard in high-key backlight, then the only two figures — the king on the throne and the court lady beside the dais — in geometric stillness; no guards, no ministers, no crowd — the emptiness is the weapon; the narration arrives later by voice, lips closed throughout, the scene is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 왕의 사실 열거 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP84_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [무거운 사실의 열거 · 이환/`ko-KR-Neural2-C`, Pitch -1.5] "네 군사는 문 밖에서 멈추었다. 너는 이제 — 칼도, 종이도, 군사도 없이 어전에 와 있다." (rel 4.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **사실의 열거 썬(가변 4컷)** — 옥좌에 앉아 손을 모은 왕(1) — 담담한 얼굴(2) — 문 밖에서 멈춘 병사(3) — 아무것도 없는 어전 중축(4). **안티슬롭 가드(plan 지정)** — 승리 연설 0건 — **왕은 설교하지 않고 사실을 놓는다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one principal figure: the young King, Hwan — a 24-year-old Korean king with a pale but finely handsome face, wearing a red gonryongpo royal robe and a black silk crown, deep sorrow and hidden fury settled into stillness in his eyes, seated perfectly calm on the high throne, hands folded on his knees, no triumph anywhere on him; far beyond the great open doors, the halted soldiers motionless in the distance, kept far and unfocused, seen only as distant silhouettes, no faces; no soldiers inside the hall, no victory oration, no raised voice, no triumph, no battle panorama, no crowd-uprising spectacle. The king's words arrive later by voice — lips closed, the render fully silent. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, resting cold on the throne and the empty axis. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the young king seated on the high throne — red royal robe, black silk crown, hands folded on his knees, perfectly calm.
2. 50mm close: the king's face — level and quiet, not angry, not victorious, merely stating.
3. 24mm wide: from beside the throne toward the open doors — the halted soldiers far outside the gate, motionless in the distance.
4. 50mm medium: the empty hall between throne and doors — the empty central axis with no one on it, the fact standing in the space: no swords, no papers, no soldiers within.

FACT MOTION — IMPORTANT: physically-based the folded hands, the halted soldiers — the king does not preach: seated and calm, the level face, the halted soldiers far beyond the doors, the empty space between; no victory oration, no raised voice, no triumph — the facts do the work; the king's words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 윤경헌의 반박 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP84_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [나이 들어 날카로워진 냉소 · 윤경헌/`ko-KR-Wavenet-D`, Pitch -2.0] "종이는 칼이 아니다. 종이는 — 사람이 사람을 부르는 이름이다. 나는 지금도 — 사람들을 부를 수 있다." (rel 5.0=절대 17.0, 사후 믹싱)
- **연출 특이**: **반박 썬(가변 3컷)** — 빈 어전 중앙에 홀로 선 노신(1) — 십 년째 새겨진 냉소(2) — 냉소 위의 매의 눈(3). **안티슬롭 가드(plan 지정)** — 악역 대사 과장 0건 — **그의 냉소가 그 공포다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure only: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power, hawk eyes — standing alone in the center of the empty throne hall facing the throne without haste; the cold smile still carved into the deep wrinkles, ten years of it, undimmed, the hawk eyes steady above it; no cursed shouting, no ranting, no villain speech, no theatrical menace — his coldness is the menace; the reply arrives later by voice — lips closed. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat, no crowd-uprising spectacle.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, rimming the old man's shoulders and hat. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the old minister standing alone in the center of the empty hall — unhurried, black hat and crimson robes, facing the throne.
2. 85mm close: the cold smile still carved into the face — ten years of it, undimmed.
3. 85mm close: the hawk eyes over the smile — paper is a name that calls people, the reply arriving later by voice.

SMILE MOTION — IMPORTANT: physically-based the carved smile, the standing stillness — the reply without heat: alone and facing the throne, the cold smile still carved, the hawk eyes over the smile; no cursed shouting, no ranting, no villain speech — his coldness is the menace; the reply arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 설화가 계단에서 내려와 세 걸음 앞에 섬 (절대 22.5~30.0 · 콘티 4컷)

- **시트**: `downloads/EP84_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [서늘한 응수 · 설화/`ko-KR-Neural2-A`, Pitch 0.0] "그렇다면 — 불러 보시옵소서." (rel 2.5=절대 24.0, 사후 믹싱)
- **연출 특이**: **측정된 응수 썬(가변 4컷)** — 단(壇) 계단의 첫 하강(1) — 역광을 가르는 두 번째 걸음(2) — 세 걸음 앞에 멈추는 거리(3) — 차고 평온한 얼굴(4). **안티슬롭 가드(plan 지정)** — 대항 연설 0건 — **그녀는 최고 권력자에게 논거가 아니라 거리로 답한다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures: the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes, a resolved unyielding bearing — stepping down from the dais stairs unhurried and stopping three steps ahead of the old minister, the measured distance between them exactly kept, she the smaller figure and the stiller one; and the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power — standing and listening; no one kneels, no one bows; the reply arrives later by voice — lips closed, the render fully silent. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat, no crowd-uprising spectacle.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, crossing the descent in geometric bands. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the court lady stepping down from the dais stairs beside the throne — unhurried, the jade hairpin still.
2. 50mm medium: her second step — the descent crossing the hall's geometric light.
3. 50mm medium: she stops three steps ahead of the old minister — the measured distance between them.
4. 85mm close: her face — cold, level, the reply arriving later by voice — then call them.

STEP MOTION — IMPORTANT: physically-based the measured descent, the stopped distance — the measured answer: the first step down, the second step crossing the light, the stop at three steps ahead, the cold face; she answers the most powerful man in the realm with a distance, not an argument; no one kneels, no one bows; the reply arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 이름들의 소진 (절대 30.0~37.5 · 콘티 5컷)

- **시트**: `downloads/EP84_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 열거 · 설화/`ko-KR-Neural2-A`, Pitch 0.0] "호남의 군벌 세 곳, 흑영대의 잔당 서른, 그리고 궐 안의 상궁 하나 — 폐하께서는 그것을 다 아시옵니다. 마마께서는 폐하께 그 이름들을 바치셨사옵니다. 어젯밤에." (rel 6.0=절대 32.0, 사후 믹싱)
- **연출 특이**: **소진 썬(가변 5컷)** — 열거를 시작하는 얼굴(1) — 경청하는 노신(2) — 모든 이름을 이미 아는 왕의 손(3) — 어젯밤의 봉납(4) — 부를 것이 남지 않은 어전(5). **안티슬롭 가드(plan 지정)** — 목록 공개 극 0건 — **폭력은 산술이고, 이름은 화면에 쓰이지 않는다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — three figures: the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes — her face beginning the quiet enumeration, flat, unhurried, no heat, a bookkeeper's cold precision; the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, deep wrinkles of power, hawk eyes — framed beyond her listening, the cold smile still in place; and the king's hand resting motionless on the throne's armrest — he already knows every name; no written lists, no documents, no letterforms anywhere — the names are spoken and never shown; no one kneels, no one bows; the words arrive later by voice — lips closed, the render fully silent. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat, no crowd-uprising spectacle.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, resting cold on the faces and the still hand. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm close: her face beginning the quiet enumeration — flat, unhurried, no heat.
2. 50mm medium: over her shoulder — the old minister framed beyond her, listening.
3. 100mm macro: the king's hand resting motionless on the throne's armrest — he already knows every name.
4. 85mm close: her final beat — the names were surrendered to the king last night — her eyes level on the old minister.
5. 35mm wide: the hall holding its breath — the enumeration finished, nothing left to call.

ENUMERATION MOTION — IMPORTANT: physically-based the spoken names, the knowing hand — the list runs out: the names beginning, the listener, the king's hand that already knows, the surrender of last night, the hall holding its breath; the violence is arithmetic — and then nothing left to call; no written lists, no letterforms anywhere — the names are spoken and never shown; no one kneels, no one bows; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 윤경헌의 웃음이 멎는 얼굴 ★ 킬러 매크로 (절대 37.5~45.0 · 콘티 7컷 단독 최장)

- **시트**: `downloads/EP84_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. [처음으로 멎는 무언 — 윤경헌/Wavenet-D] "…" (무대사 — 렌더 전면 무음)
- **연출 특이**: **★ 킬러 매크로 썬(가변 7컷 단독 최장)** — 아직 새겨진 미소(1) — 계산을 시작하는 매의 눈(2) — 한 박자 길게 버티는 미소 끝(3) — 모서리부터 얇아지는 미소(4) — 십 년이 흘러내리는 미소(5) — 그 아래 드러난 맨얼굴(6) — 소리 없이 유지되는 멈춤(7). **안티슬롭 가드(plan 지정)** — 저주 고함·분노 그리마스 0건 — **공포는 십 년이 한 얼굴에서 얼마나 조용히 빠지는가다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one face only: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister with a graying beard, deep wrinkles of power, hawk eyes, a black horsehair official hat — his face filling the frame, the cold smile still sitting in the deep wrinkles, ten years of power carved around it; the hawk eyes beginning to compute, the first arithmetic of loss crossing behind them; the smile's edge holding one beat too long, the smile thinning from the corners, ten years of it sliding off the face like a mask losing its grip, the bare old face beneath — stopped, for the first time in ten years; no cursed shouting, no rage grimace, no screaming old man, no final threat — the horror is how quietly ten years fall off one face; the face is wordless throughout — lips closed, the render fully silent. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat, no crowd-uprising spectacle.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, rimming the wrinkles of the stopping face. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 7 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the old minister's face filling the frame — the cold smile still sitting in the deep wrinkles.
2. 100mm macro: the hawk eyes above the smile — beginning to compute.
3. 100mm macro: the smile's edge holding — one beat too long.
4. 100mm macro: the smile thinning — a hair of it gone from the corners.
5. 100mm macro: the smile dissolving — ten years of it sliding off the face.
6. 100mm macro: the face beneath — bare, old, stopped — for the first time in ten years.
7. 100mm macro: the stopped face held in silence — no curse, no shout, only the quiet.

STILLNESS MOTION — IMPORTANT: physically-based the dissolving smile, the settling wrinkles — the pivotal cut — the smile, stopping: the smile still there, the eyes computing, the edge holding, the thinning, the dissolving, the bare face beneath, the stop held; no cursed shouting, no rage grimace, no screaming old man — the horror is how quietly ten years fall off one face; the face is wordless throughout — lips closed, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 세 걸음의 거리 (절대 45.0~52.5 · 콘티 1컷 · 무대사)

- **시트**: `downloads/EP84_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. 무대사 — 렌더 전면 무음.
- **연출 특이**: **유지 썬(가변 1컷 절제)** — 멈춘 노신과 궁녀가 세 걸음의 돌바닥을 사이에 두고 마주 서고, 그 너머 옥좌의 왕 — 하나로 유지되는 기하학적 정적. **안티슬롭 가드(plan 지정)** — 기계적 "3컷·4컷 고정" 슬롭 회피 — **1컷 롱테이크가 이 썬의 전부다**. plan 기재 "세 사람의 기하학적 정적"이 정본표 기준 실현되는 썬.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three figures: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power — stopped; and the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes — facing each other across three steps of stone; and the young King, Hwan — a 24-year-old Korean king in a red gonryongpo royal robe and a black silk crown — on his high throne beyond them; the whole arrangement one held geometric stillness under the high-key backlight; nothing moves but the dust in the backlight; the scene has no dialogue and stays fully silent — lips closed. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat, no crowd-uprising spectacle.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, holding the three figures in its geometry. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence:
1. 85mm medium wide: the stopped old minister and the court lady facing each other across three steps of stone — the king on his throne beyond — a held geometric stillness.

HOLD MOTION — IMPORTANT: physically-based the held distance, the dust in the backlight — one held frame: the three-step distance between the stopped minister and the court lady, the king beyond; nothing moves but the dust in the backlight; the scene is fully silent — no dialogue, lips closed, the render fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 어전에 남은 세 사람 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 2컷 · 엔드카드)

- **시트**: `downloads/EP84_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드. 무대사 / 자막: 제85화 「계약서의 이름」에서 계속 (편집 단계 삽입)
- **연출 특이**: **종장 썬(가변 2컷 절제)** — 텅 빈 어전에 남은 세 사람의 거리감(1) — 암전·타이틀(2, 편집 단계 참조용). **안티슬롭 가드(plan 지정)** — 승리 팡파레 0건 — **어전은 비어 있고 세 사람만 남는다**. 렌더는 어두워지는 구간 후 완전 암전으로 종결.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three figures: the young King, Hwan — a 24-year-old Korean king in a red gonryongpo royal robe and a black silk crown — on his high throne; the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes; and the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat — stopped; the empty throne hall holding the three who remain, the distances between them kept like an architecture, no one moving; the image darkening evenly toward the end until it holds in complete black; no victory fanfare, no triumph, no crowd-uprising spectacle. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight wearing out evenly is the only light, sinking over the empty hall; no lamps lit, no warm interior glow, no sudden cut to black. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 35mm wide: the empty hall holding the three — the king on the throne, the court lady, the stopped old minister — the distances between them; the image darkening evenly.
2. The frame fades to complete black and holds.

REMAIN MOTION — IMPORTANT: physically-based the darkening dawn, the three who remain — the hall holds the king, the court lady and the stopped minister, the distances kept like an architecture; the frame darkens evenly, then complete black; no victory fanfare, no 'the end' mood; the render ends in complete black and is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP84 원장 끝. 다음: 제85화 「계약서의 이름」 — SEASON_04_MASTER_SCREENPLAY.md 정본 계수 —**
