# 「혈화의 궐」 EP93 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제93화 「새로운 길」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제93화 「새로운 길」` 절, 원전: 제93장 정본) + `characters.md` 캐릭터 앵커(이설화 혼례 복식·이환 평복 — 본화 신규 앵커, 이환 Neural2-C -1.5는 plan 확정치 우선) + EP22~EP92 원장 템플릿(동일 규격)
> **범위**: EP93 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP92 S8 엔드카드 「제93화 새로운 길에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 24mm 와이드 · 낙화원, 가을 — 낙화원의 혼인 [내레이션/Wavenet-C (0.0): "설화와 무결의 혼인은 — 그해 가을에 이루어졌다." (rel 3.0=절대 2.0)], S2 50mm, 왕의 서약 [이환/Neural2-C (-1.5): "과인은 이 자리에서 임금이 아니라 — 너희의 친구로 있겠다." (rel 3.5=절대 9.5)], S3 100mm Macro, 검흔이 웃음으로 가득한 무결의 얼굴 (무대사), S4 100mm Macro · 백일홍, 백색 저고리 머리의 백일홍 한 가지 — 일곱 송이가 나란히 [내레이션/Wavenet-C (0.0): "그것은 꽃의 목록이었다 — 사람들의 이름 대신, 꽃으로 맹세했던 사람들의 목록." (rel 4.5=절대 24.0)], S5 85mm, 왕의 작은 말 [이환/Neural2-C (-1.5): "이 나라는 — 이제 꽃으로 맹세하는 사람들이 늘어야 한다." (rel 3.5=절대 32.0)], S6 35mm, 두 사람의 절 (무대사), S7 24mm 와이드, 하객들 속의 왕 — 임금이 아니었던 오후 (무대사), S8 50mm → 엔드카드, 낙화원의 나무 → 암전 → 타이틀(자막: 제94화 「낙화원의 봄」에서 계속).
> **안티슬롭 ① — 혼인 낭만 과장 배제(plan·정본 안티슬롭 지정)**: 화려한 대례복·궁중 대례 절차·축의 고양 렌더 **0건**. 치환 — **낙화원의 소박하고 담담한 가을 혼인**: 소박한 백색 저고리와 옥비녀의 신부, 정갈한 도포의 신랑, 익선관 없는 평복의 왕. "과인은 이 자리에서 임금이 아니라, 너희의 친구로 있겠다"는 **진실한 서약 한 줄**(S2 5비트 단독 최장). `no ornate ceremonial wedding dress, no grand royal ceremony, no romantic exuberance, no cheering` 전 썬 상설.
> **안티슬롭 ② — 혼례 절차 설명 배제(plan·정본 안티슬롭 지정)**: 혼례 절차·의식 순서 해설 렌더 **0건**. 치환 — **일곱 송이의 백일홍이 나란히 놓이는 침묵의 미장센**(꽃의 목록): 사람들의 이름 대신 꽃으로 맹세했던 사람들의 목록(S4 4비트). `no ceremony procedure, no ritual explanation` S4·S6 상설.
> **S3 검흔 미소 매크로(plan·정본 지정)** — 검흔이 웃음으로 가득한 무결의 얼굴 매크로. **캐릭터 앵커(정본 AG ⑥)** — 뺨의 옅은 검흔은 characters.md 고정 앵커 준수, 흉터는 **치유된 옛 자국으로만** — 상처·출혈 0건. 잔잔하고 맑은 미소, 발웃음·환호 0건. 2비트 절제.
> **S4 백일홍 꽃의 목록 매크로(plan·정본 지정)** — 백색 저고리 머리의 백일홍 한 가지와 나란히 놓인 일곱 송이. **꽃의 목록 소품 일관성(정본 AG ①)** — `exactly seven (7) blooms` 수 카운트 지문 유지(never six, never eight). 꽃잎은 꽃일 뿐 글자 0건.
> **백지 설계 교칙(전편 규격)**: 프레임 내 기물 위 가독 글자 **0건** — 본화는 문서·현판·축문 등 노출 문자 요소가 아예 없다(EP91 묘비각·EP92 조서 라인 예외조차 없음). **붉은 색은 실사 화면의 백일홍 문양(EP62 선례 — 시트는 흑연 에칭, 실사에서만 적색 채문)과 S08 타이틀뿐**. 엔드카드 자막(제94화 「낙화원의 봄에서 계속」)은 편집 단계 삽입 — 시트에는 편집 참조용 카드로만.
> **무자막 원칙(100화 전편 규격)** — 화면 노출 문자 일체 금지. 내레이션 2구(S1·S4)와 이환 대사 2구(S2·S5)는 편집 단계 사후 믹싱 — 시트와 렌더에 자막 활자를 그리지 않는다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이설화 — **혼례 복식, 소박한 백색 저고리와 옥비녀, 머리에 꽂힌 단아한 백일홍 한 가지**(본화 신규 앵커 등록 — characters.md 다크 파스텔 궁녀 한복·옥비녀 앵커의 본화 혼례 치환, 21세·창백한 피부·서늘하고 총명한 눈빛 계승). 강무결 — **검흔이 맑은 미소로 가득 찬 얼굴, 정갈한 도포 차림의 신랑**(characters.md 뺨의 검흔·훤칠한 체격 앵커 준수). 이환 — **익선관 미착용, 단령/도포 평복으로 친구로서 하객들 사이에 소박하게 자리한 청년**(본화 신규 앵커 등록 — characters.md 곤룡포·익선관 앵커의 본화 평복 치환). 하객들 — **소박한 평복의 배경 인물·실루엣**(S6·S7 원중경 이상, 얼굴 클로즈업 0건).
> **입모양 배제(100화 전편 규격)** — 내레이션 2구(S1·S4) 전부 무음 렌더 + 사후 믹싱. 이환 대사 2구(S2·S5) — 화면 이환의 입과 무관한 보이스오버·사후 믹싱, 전 썬 `lips closed`. S3·S6·S7·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 본화 `ko-KR-Wavenet-C`는 내레이션(0.0) 2구(S1·S4) — 본화 내 단일 배역, 피치 사다리 충돌 없음. 이환 `ko-KR-Neural2-C`(-1.5 — plan 확정치, characters.md -0.5 대신 plan 우선 원칙) S2·S5 2구 — 동일 배역 연속, 충돌 없음. 렌더는 전 썬 무음.
> **가변 컷 배분**: 3/5/2/4/3/4/3/4 = 28컷 — EP13~EP92 전 배분(104종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP92 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP92분 4/2/5/3/2/6/2/4와도 상이). **S2(왕의 서약) 5컷 단독 최장** — "임금이 아니라 친구로 있겠다"는 서약이 이루어지는 완급의 본체. S8(나무→암전→타이틀) 4컷 종지, S4(꽃의 목록)·S6(맞절) 각 4컷, S1(낙화원의 혼인)·S5(왕의 작은 말)·S7(임금이 아니었던 오후) 각 3컷, **S3(검흔의 미소) 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 11회(초벌 8 + 재렌더 3) 중 최종 채택 8장 — **재렌더 3건**: ① S04 초벌 P4(손이 들어간 클로징 패널의 꽃이 8송이로 렌더 — 꽃의 목록 7송이 위반) → P3·P4에 `the same exactly seven (7) blooms carried over` 수 카운트 지문 강화 후 재렌더 해소(P2·P3·P4 전부 7송이 확인). ② S05 초벌 P1(탁자 위 꽃 8송이) → P1·P3에 `exactly seven (7)` 지문 신설 후 재렌더 해소(P1·P3 7송이 확인). ③ S08 초벌 타이틀 말미 「계속」이 패널 하단 경계를 넘어 흘러나옴 → 타이틀 패널에 `the first character 제 starting well below the panel's top edge and the last character 속 ending well above the panel's bottom edge` 여백 지문 신설 후 재렌더 해소. 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.18%(적색 타이틀 — 좌표 확인, 타이틀 열 x369~390·y1020~1272 한정 — 의도 채색). **전장 md5: S01 fe17ac667115 / S02 f3b9dac93e3e / S03 bdd626308efe / S04 2f45bac1f2b9(재렌더 최종본) / S05 5c84ba5efcb1(재렌더 최종본) / S06 002da7cf9caf / S07 690355f747c5 / S08 0fc0a1362e87(재렌더 최종본)**.
> **검독 운영 교훈(EP67~EP92 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전 첨부를 돌려줄 수 있다** — 본화 S04 재렌더 후 전장 재열람에서 초벌본과 동일한 첨부가 재반환돼(md5는 변경 확인) **별도 크롭 경로(`downloads/qc_crops/Z_EP93_*`) 재열람으로 현재본 판정**했다. **어간 부분 문자열 함정 계승** — 금지 어휘의 어간 부분 문자열도 생성기 validate()가 차단(EP66 실측). **본화 신규 함정 2건**: ① **소품 수 카운트가 지문 없는 패널에서 이탈하는 결함** — S04·S05의 7송이 백일홍이 지문 없는 패널(P4·P1)에서 8송이로 렌더 → **수 카운트 지문을 소품이 등장하는 전 패널에 기계적 반복 기재**로 해소(이후 화 소품 일관성 계승 규격). ② **타이틀 세로 열이 패널 경계를 넘는 결함**(S08 초벌) — 상하 여백 명시 지문으로 해소.
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제93화 「새로운 길」 절(원전: 제93장 정본) 직접 열람**(327행 이하) — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. **S08 타이틀 슬롯**: 「제94화 낙화원의 봄에서 계속」 실제 글자수 13자 = 1자 1슬롯 원칙에 따라 **13슬롯** 확정(확대 크롭 검독 통과, 숫자 9·4 각각 단독 슬롯, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). **보이스 P 보정 병기**: characters.md는 이환 Neural2-C -0.5를 표기하나, plan 확정치(-1.5)를 본화에 채택 — plan 우선 원칙. **가변 배분**: plan은 특정 배분 수치를 고정하지 않아 본화 서사에 맞춰 3/5/2/4/3/4/3/4=28컷으로 설계 — **총 컷수 28 규격 준수 + 선행 104종 미중복 기계 스캔**으로 이중 검증.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep93_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep93_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 가을 낙화원(은행잎·단풍), 설화의 백색 저고리와 붉은 치마, 무결의 남색 도포, 이환의 평복, 백일홍이 실제 색으로 복원된다. **붉은 색은 실사 백일홍 문양(EP62 선례)과 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화는 문서·현판 노출 요소가 아예 없다** — 렌더 프레임 내 가독 문자 일체 0건.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **가을 낙엽과 소박한 혼인의 기척**(the falling leaves, the unhurried gathering), S2 **서약의 몸짓**(the folded hands, the level eyes), S3 **미소로 가득 찾는 얼굴**(the quiet clear smile, the scar at rest), S4 **꽃의 목록**(the row of seven blooms, the petals), S5 **작은 말의 기울임**(the lean toward the couple, the glance exchanged), S6 **맞절의 동작**(the single deep bow, the falling leaves crossing), S7 **하객들의 오후**(the tea cup passed, the ordinary evening talk), S8 **낙엽과 물러가는 빛**(the leaves letting go, the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다. **무결의 검흔은 치유된 옛 자국으로만 기술** — 상처·출혈 묘사 0건.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. 본화는 문서·현판·축문 노출이 아예 없다. 엔드카드 자막(제94화 「낙화원의 봄에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 2구(S1·S4)·이환 대사 2구(S2·S5)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S3·S6·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이설화 — 혼례 복식(본화 신규 앵커)**: the bride, Seolhwa — a young 21-year-old Korean woman in a plain white jeogori bridal jacket and simple red chima skirt, neat traditional bridal hair with the same simple jade hairpin and a single dignified zinnia flower tucked in her hair, pale porcelain skin, calm clear eyes, lips closed.
   - **강무결 — 신랑(plan·characters.md 지정)**: the groom, Mugyeol — a 25-year-old Korean man in a clean plain dark durumagi overcoat, tall and steady, a faint old scar across his cheekbone, his scarred face full of a quiet clear smile, lips closed.
   - **이환 — 평복(본화 신규 앵커)**: the young king Ihwan as a friend among the guests — a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, standing simply among a few guests, quiet warm eyes, lips closed.
   - **하객들(plan 지정)**: plain background figures and silhouettes — servants and companions in simple Joseon everyday dress, faces never shown in close-up, a small quiet gathering and never a banquet.
   - **인물 상한**: S01 신부 1·신랑 1+하객 배경, S02 이환 1+신부·신랑+하객 배경, S03 무결 1인 매크로, S04 인물 0명(손 1한정), S05 이환 1+신부·신랑, S06 신부·신랑+하객 실루엣, S07 이환+하객, S8 인물 0명(나무만) → 군중·연회 인파 렌더 0건.
9. **광원 표기**: S1 — 낙화원의 가을 오전 햇살이 마당에 고르게 내려앉는 것. S2 — 같은 가을 오후의 햇살이 하객들 사이로. S3 — 마주 보는 얼굴 위에 부드럽게 눕는 오후 빛. S4 — 낮은 탁자 위에 평평하게 눕는 오후 빛. S5 — 셋에게 닿는 오후 빛 한 줄. S6 — 맞절의 두 사람 위로 빠지는 오후 빛. S7 — 늦은 오후 빛이 하객들 사이에 고르게 앉는 것. S8 — 낙화원의 나무 위로 하루의 마지막 빛이 고르게 낮아지다 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설. **EP92 궁 봄 가드를 본화 낙화원 가을 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 낙화원의 나무·균일 암전 구간 이후의 붉은 타이틀(제94화 「낙화원의 봄에서 계속」, 13슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S4 2구. 이환 `ko-KR-Neural2-C` (Pitch **-1.5** — plan 확정치, characters.md -0.5 대신 plan 우선 원칙, Speed 0.95, 임금이 아닌 자의 낮고 진실한 서약 톤) — S2·S5 2구. 본화 내레이션 2구 + 캐릭터 대사 2구(S2·S5) + 엔드카드 자막 1건. **무결·설화·윤경헌·중전 대사 0구** — 본화는 서약과 절, 꽃의 목록으로 말없이 이어지는 회차다. S3·S6·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 2구 — 동일 배역 연속이므로 피치 사다리 충돌 없음, 단 별도 세션 트랙 지정 합성 병기. 이환 `Neural2-C`(-1.5) 2구 — 동일 배역 연속, 내레이션과는 상이 모델. 파일명 분리 규칙 기재(`EP93_S1_NARRATION`/`EP93_S4_NARRATION`/`EP93_S2_IHWAN`/`EP93_S5_IHWAN`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 3/5/2/4/3/4/3/4 = 28컷 — EP13~EP92 전 배분 104종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S2 5컷 단독 최장**(서약의 완급), S8·S4·S6 각 4컷, S1·S5·S7 각 3컷, **S3 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **혼인의 낭만은 과장이 아니라 절제다(본화 핵심)**: 본화에는 대례복도 궁중 예식도 축의 환호도 없다 — 소박한 가을 혼인(S1)으로 시작해, 익선관 없는 왕이 친구로서 서약하고(S2), 검흔이 미소로 가득 찬 얼굴의 매크로(S3)와 일곱 송이 백일홍의 침묵하는 목록(S4)으로 이어지며, 왕의 작은 말(S5)과 두 사람의 맞절(S6), 임금이 아니었던 오후(S7)를 거쳐 낙화원의 나무 아래 빛이 떠난다(S8). 전 썬 `no ornate ceremonial wedding dress, no grand royal ceremony, no romantic exuberance, no cheering` 상설. S4·S6 `no ceremony procedure, no ritual explanation` 상설. 혼례의 감정은 대사가 아니라 검흔의 미소(S3)와 맞절(S6)이라는 그림이다.

---

## 1. S01 첫째 — 가을, 낙화원의 혼인 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP93_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 낙화원. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "설화와 무결의 혼인은 — 그해 가을에 이루어졌다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 3비트)** — 낙화원의 고찰 와이드(1) — 신부·신랑의 나란히 선 지면 뷰(2) — 마주 보는 두 사람으로의 슬로우 푸시(3). **안티슬롭 가드(plan 지정)** — 화려한 대례복·궁중 예식·낭만 과장 0건 — 혼인은 낙화원의 소박하고 담담한 가을 풍경이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a small quiet wedding gathering, plain and unhurried: the bride, Seolhwa — a young 21-year-old Korean woman in a plain white jeogori bridal jacket and simple red chima skirt, neat traditional bridal hair with a simple jade hairpin and a single dignified zinnia flower tucked in her hair, pale porcelain skin, calm clear eyes, lips closed; the groom, Mugyeol — a 25-year-old Korean man in a clean plain dark durumagi overcoat, tall and steady, a faint old scar across his cheekbone, lips closed; a few plain guests in simple Joseon everyday dress as background figures, faces never in close-up. No ornate ceremonial wedding dress, no grand royal ceremony, no romantic exuberance, no cheering, no banquet. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the autumn morning sun settling evenly over the palace garden Nakhwawon is the only light, laying soft bars across the ground and the plain garments. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the autumn light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, high: the autumn palace garden Nakhwawon — a small quiet wedding gathering under ginkgo and maple trees, falling leaves, no grand ceremony.
2. 24mm wide: a few plain guests, the bride in a plain white jeogori and the groom in a plain dark durumagi standing side by side.
3. 24mm wide, slow push: the two of them facing each other under the trees — the wedding beginning without any ritual display.

GARDEN MOTION — IMPORTANT: physically-based the falling leaves, the unhurried gathering — the wedding of Seolhwa and Mugyeol is plain and unassuming, a quiet garden marriage and not a royal ceremony: leaves drift down through the frame at their own weight, the gathering stands loosely with no formation and no protocol, and the slow push closes on the two simply facing each other; no ornate ceremonial wedding dress, no grand royal ceremony, no romantic exuberance, no cheering; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 왕의 서약 (절대 07.5~15.0 · 콘티 5컷 ★ 단독 최장)

- **시트**: `downloads/EP93_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [임금이 아닌 자의 서약 · 이환/`ko-KR-Neural2-C`, Pitch -1.5, Speed 0.95] "과인은 이 자리에서 임금이 아니라 — 너희의 친구로 있겠다." (rel 3.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **서약 썬(가변 5비트 단독 최장)** — 하객 사이에서 빠져나오는 평복의 청년(1) — 아무 권위도 없이 모인 손(2) — 서약이 이루어지는 얼굴(3) — 왕좌 없는 삼각 구도(4) — 침묵으로 서약을 받는 하객들(5). **안티슬롭 가드(plan 지정)** — "임금이 아니라 친구로 있겠다"는 서약의 완급이 본체 — 왕좌·단상·계급 구도 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king Ihwan as a friend among the guests: a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, standing simply among a few plain guests, quiet warm eyes, lips closed; with the bride Seolhwa in a plain white jeogori bridal jacket with a jade hairpin and a single zinnia in her hair, and the groom Mugyeol in a plain dark durumagi overcoat with a faint old scar on his cheekbone. No throne, no dais, no canopy, no royal regalia, no guards, no grand royal ceremony, no cheering. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same autumn afternoon sun coming down among the guests is the only light, laying one soft brightness on the three of them and none of it staged. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the young man in plain everyday robes stepping forward from among the guests — no crown, no royal robe, just a friend coming to stand before the couple.
2. 50mm close: his open hands folded loosely before him — a gesture with no authority in it at all.
3. 50mm close-medium: his face as the vow is made — quiet, level, the promise of being a friend and not a king.
4. 50mm wide: the couple and the friend standing in a plain triangle — no throne, no dais, no hierarchy in the framing.
5. 50mm medium, slow pull: the guests receiving the vow in silence — a small bow of the head here and there, no applause.

VOW MOTION — IMPORTANT: physically-based the folded hands, the level eyes — the vow carries the scene: I will stand here not as your king but as your friend: he steps out from among the guests with no retinue and no ceremony, his hands fold loosely without authority, his face settles on the promise without weight, the three stand on the same level of earth, and the guests receive it in silence with a small bow of a head here and there; no grand royal ceremony, no ornate ceremonial wedding dress, no cheering; the vow arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 검흔이 웃음으로 가득한 무결의 얼굴 (절대 15.0~22.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP93_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. 무대사 — 렌더 완전 무음.
- **연출 특이**: **미소 매크로 썬(가변 2비트 절제)** — 검흔이 고요히 누운 뺨(1) — 미소로 가득 차는 얼굴, 검흔도 함께 웃는다(2). **캐릭터 앵커(정본 AG ⑥)** — 검흔은 치유된 옛 자국, 상처·출혈 0건. 사적인 기쁨이지 공개된 성토(聲討)가 아니다 — 발웃음 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one man's face at macro distance: the groom, Mugyeol — a 25-year-old Korean man with a faint old scar across his cheekbone, the scar a healed old mark only, a settled feature of the face, no wound, no cut; his plain dark durumagi collar at the frame edge. No other figure in frame. No laughing aloud, no cheering, no romantic exuberance. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light laying softly across the face is the only light, resting evenly on the scar and the skin. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the groom's scarred cheek in macro — the faint old scar across the cheekbone resting quiet under the afternoon light.
2. 100mm macro, slow travel: the scarred face filling with a quiet clear smile — the whole face smiling, the scar smiling with it.

SMILE MOTION — IMPORTANT: physically-based the quiet clear smile, the scar at rest — ten years of watchfulness settle into one private afternoon of joy: the scar holds still as the skin around it relaxes, the smile grows from the eyes down without a sound, and the scar smiles with the rest of the face; a private joy and not a public performance; no laughing aloud, no cheering, no romantic exuberance; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 백색 저고리 머리의 백일홍 한 가지 — 일곱 송이가 나란히 (절대 22.5~30.0 · 콘티 4컷)

- **시트**: `downloads/EP93_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 백일홍. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "그것은 꽃의 목록이었다 — 사람들의 이름 대신, 꽃으로 맹세했던 사람들의 목록." (rel 4.5=절대 24.0, 사후 믹싱)
- **연출 특이**: **꽃의 목록 썬(가변 4비트)** — 머리의 백일홍 한 가지(1) — 나란히 놓인 일곱 송이(2) — 낱행을 훑는 슬로우 트래블(3) — 손이 스치고 물러나는 클로징(4). **꽃의 목록 소품 일관성(정본 AG ①)** — `exactly seven (7) blooms` never six, never eight. **안티슬롭 가드(plan 지정)** — 혼례 절차 설명 0건 — 침묵하는 미장센이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no full figure in frame: macro details only — the bride Seolhwa's white jeogori collar and neat bridal hair with the jade hairpin and a single dignified zinnia flower tucked above her ear; and the low wooden table carrying exactly seven (7) zinnia blooms in one straight row: count them one by one, one, two, three, four, five, six, seven — never six, never eight, no eighth bloom anywhere in frame. Only one hand of hers enters to hover and withdraw. No ceremony officiant, no ritual objects, no vow papers. The flowers are flowers only, never letters. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light lying flat across the table and the petals is the only light, holding one even brightness along the row. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the bride's white jeogori collar and hair — the single dignified zinnia flower tucked above her ear, one bloom for the bride herself.
2. 100mm macro: the low wooden table — exactly seven zinnia blooms laid side by side in a straight row, no vase, no ribbon, no ornament.
3. 100mm macro, slow travel: the row under the afternoon light — each bloom a person who once swore by a flower, a list written in blossoms instead of names.
4. 100mm macro: the seven blooms holding the frame alone in the settling light — the bride's hand hovers above the row without touching, exactly seven blooms, never eight.

FLOWER-LIST MOTION — IMPORTANT: physically-based the row of seven blooms, the petals — it is a list of flowers, people sworn by blossoms instead of names: the single zinnia in her hair sits still as the camera finds it, the row of exactly seven blooms lies untouched on the wood, the slow travel passes each bloom at the same unhurried weight, and her hand hovers above the row and withdraws without touching anything; it is a list of flowers and nothing is read aloud and no rite is explained; no ceremony procedure, no ritual explanation, no cheering; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 왕의 작은 말 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP93_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [아주 작게 · 이환/`ko-KR-Neural2-C`, Pitch -1.5, Speed 0.95] "이 나라는 — 이제 꽃으로 맹세하는 사람들이 늘어야 한다." (rel 3.5=절대 32.0, 사후 믹싱)
- **연출 특이**: **작은 말 썬(가변 3비트)** — 일곱 송이 탁자 곁에 선 평복의 왕(1) — 작게 나오는 말의 얼굴(2) — 눈빛 교환으로 받는 신부·신랑(3). **안티슬롭 가드** — 왕명 선언·거례 연설 무드 0건 — 둘만의 작은 말이다. 꽃의 목록 일관성(정본 AG ①) — 탁자는 정확 일곱 송이.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — three people at a low wooden table: the young king Ihwan as a friend — a 24-year-old Korean man in plain everyday scholar's robes, NO royal winged hat, NO dragon robe, NO crown of any kind, quiet warm eyes, lips closed; the bride Seolhwa in a plain white jeogori bridal jacket with a jade hairpin and a single zinnia in her hair; the groom Mugyeol in a plain dark durumagi overcoat with a faint old scar on his cheekbone. The low wooden table carries exactly seven (7) zinnia blooms in one straight row: count them one by one, one, two, three, four, five, six, seven — never six, never eight. No courtiers taking note, no ceremony resuming, no cheering. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: a single line of afternoon light reaching the three of them and the blooms is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the young man in plain robes standing beside the low table of seven blooms — leaning a little toward the couple, a private word gathering.
2. 85mm close: his voice pitched small — the words meant for the two of them and for the country they will live in.
3. 85mm medium: the couple receiving the small words — a glance exchanged between bride and groom, the row of exactly seven blooms on the table before them.

SMALL-WORDS MOTION — IMPORTANT: physically-based the lean toward the couple, the glance exchanged — the words arrive small and meant for three people only: he leans a little toward them without ceremony, his face speaks at the volume of a confidence, and the couple answer with a glance and a settled quiet, the seven blooms untouched on the table before them; this country must now grow more people who swear by flowers — the words arrive later by voice; no ceremony procedure, no applause, no cheering, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 두 사람의 절 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP93_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. 무대사 — 렌더 완전 무음.
- **연출 특이**: **맞절 썬(가변 4비트)** — 마주 보는 두 사람(1) — 단 한 번의 깊은 절(2) — 일어나며 마주치는 눈(3) — 나란히 선 완결(4). **안티슬롭 가드(plan 지정)** — 혼례 절차 해설·진행자·의식 테이블 0건 — 절은 두 사람 사이의 맹세 그 자체다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the couple and a loose ring of guests: the bride, Seolhwa — a young 21-year-old Korean woman in a plain white jeogori bridal jacket and simple red chima skirt, neat traditional bridal hair with a simple jade hairpin and a single dignified zinnia flower tucked in her hair, pale porcelain skin, calm clear eyes, lips closed; the groom, Mugyeol — a 25-year-old Korean man in a clean plain dark durumagi overcoat, tall and steady, a faint old scar across his cheekbone, lips closed; the guests as plain background figures in simple Joseon everyday dress, standing loosely in a wide ring, faces never in close-up. No ritual officiant, no ceremonial table, no ritual objects, no ceremony procedure, no ritual explanation, no cheering. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light crossing the open garden ground over the bowing two is the only light, and falling leaves carry small shadows through it. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide: the open garden ground — the bride and groom turning to face each other, guests standing loosely in a wide ring behind them.
2. 35mm wide: the two bowing to each other — a single deep bow, unhurried, falling leaves crossing the frame.
3. 35mm medium: the two rising from the bow and meeting each other's eyes — the vow of the bow kept between two people.
4. 35mm wide: the two standing upright side by side, the garden quiet around them — the bow completed without a single spoken word.

BOW MOTION — IMPORTANT: physically-based the single deep bow, the falling leaves crossing — the marriage rite is a bow between two people and nothing else: they turn to face each other with no officiant and no procedure, the bow goes down unhurried to its full depth with the bride's zinnia nodding with the motion, leaves drift through the light as they rise, and their eyes meet on the level; the bow is kept between the two of them and not performed to a hall; no ceremony procedure, no ritual explanation, no applause, no cheering; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 하객들 속의 왕 — 임금이 아니었던 오후 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP93_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드. 무대사 — 렌더 완전 무음.
- **연출 특이**: **하객의 왕 썬(가변 3비트)** — 벤치에 앉은 평복의 청년(1) — 아무에게나 건네지는 찻잔(2) — 아무도 왕을 부르지 않는 고찰 와이드(3). **안티슬롭 가드** — 왕의 은둔 서정·과한 상징 연출 0건 — 평범한 오후의 풍경 그 자체다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king Ihwan as a friend among the guests: a 24-year-old Korean man in plain everyday scholar's robes, NO royal winged hat, NO dragon robe, NO crown of any kind, sitting on a plain wooden bench among a few plain guests in simple Joseon everyday dress, indistinguishable from them but for his face, quiet warm eyes, lips closed; nobody addressing him by title, nobody bowing to the ground, no crowd exultation, no ceremony, no cheering. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late afternoon light settling evenly among the guests is the only light, sitting soft and low under the trees. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide: the gathering in late afternoon — the young man in plain robes sitting among a few guests on a bench, indistinguishable but for his face.
2. 24mm medium: a guest passing him a cup of tea as one passes a cup to anyone — received with a small nod.
3. 24mm wide, high: the whole quiet gathering — the small wedding afternoon dissolving into ordinary evening talk, the king nowhere singled out.

AFTERNOON MOTION — IMPORTANT: physically-based the tea cup passed, the ordinary evening talk — it was an afternoon where nobody addressed a king, and nobody was addressing a king: the gathering sits and talks at the tempo of any small village gathering, the cup passes hand to hand as it would to anyone, and the high wide view lets the afternoon dissolve into ordinary evening talk with no one singled out; no crowd exultation, no ceremony, no cheering; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 낙화원의 나무 → 암전 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP93_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제94화 「낙화원의 봄」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 4컷)** — 마지막 저녁빛의 낙화원 나무(1) — 트렁크에서 가지로의 슬로우 틸트와 물러가는 빛(2) — 균일 암전(3) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **안티슬롭 가드** — 혼인 회상 몰입·종반 고양·에필로그 0건 — 하루가 그저 정원을 떠난다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: the great tree of Nakhwawon — the tree under which the two were married — in the last evening light, its autumn leaves turning slowly in the cooling air, the garden empty around it. No figure, no face, no silhouette, no finale tableau, no looking back, no wedding-cherishing mood, no romantic exuberance, no cheering. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the last evening light of the day is the only light, and it withdraws evenly as the episode closes — the leaves pale by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the evening light's own depth, no milky flat darkness.

Recreate the first 2 panels in order as one continuous ~10 second sequence (the sheet's third and fourth panels — the complete black hold and the red next-episode title card — are edit-stage reference only and are NOT rendered):
1. 50mm medium: the great tree of Nakhwawon in the last evening light — the tree under which the two were married, its autumn leaves turning slowly in the cooling air.
2. 50mm medium, slow tilt: the tilt up the trunk into the branches — a few leaves letting go and drifting down through the fading light, the last brightness withdrawing evenly.

TREE MOTION — IMPORTANT: physically-based the leaves letting go, the even leaving of the light — the episode closes as landscape and not as statement: the leaves turn in the cooling air at their own weight, a few let go and drift down through the last light in natural fall and never wind-torn, the slow tilt climbs the trunk into the branches, and the last brightness withdraws evenly off the leaves as the frame cools toward grey; no finale fanfare, no 'the end' mood, no romantic exuberance, no cheering; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP93 원장 완결. 콘티 시트 8종(`downloads/EP93_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제94화 「낙화원의 봄」 —**
