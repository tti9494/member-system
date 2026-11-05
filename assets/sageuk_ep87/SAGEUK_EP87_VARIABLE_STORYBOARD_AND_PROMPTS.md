# 「혈화의 궐」 EP87 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제87화 「단죄」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제87화 「단죄」` 절, 원전: 제87장 정본 · ★ 킬러 컷 회차) + `characters.md` 캐릭터 앵커(이설화 옥비녀 궁녀 복식, 윤경헌 흑립·홍단령) + EP22~EP86 원장 템플릿(동일 규격)
> **범위**: EP87 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP86 S8 엔드카드 「제87화 단죄에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 35mm, 계단을 내려가는 설화 — 기다리는 윤경헌 [내레이션/Wavenet-C (0.0): "그는 무릎을 꿇지 않았다. 서 있기를 — 택했다." (rel 4.0=절대 2.5)], S2 85mm, 마지막 인간의 값 [윤경헌/Wavenet-D (-2.0): "나는 그 불 속에서 그것을 취했다. 그것이 그 집안에서 유일하게 불에 타지 않을 것이라고 생각했으므로. 나는 그것을 팔지 않았고, 두지도 않았다. 나는 그저 — 가졌다. 그것이 나의 죄 중에서 — 가장 인간다운 죄였다." (rel 6.5=절대 10.0)], S3 100mm Macro · 비녀 회수, 윤경헌의 허리에서 받아 드는 백일홍 문양의 비녀 [내레이션/Wavenet-C (0.0): "십 년 만의 무게였다. 그녀의 손은 — 그 무게를 기억하고 있었다." (rel 4.5=절대 17.5)], S4 85mm, 설화의 선고 [설화/Neural2-A (0.0): "아버님의 이름으로 — 어머님의 은장도로." (rel 3.0=절대 24.0)], S5 100mm Macro · 초슬로우, 칼이 나감 — 한 번 [효과음: 바람·새 소리로 절단] (rel 2.0=절대 31.0) **★ 킬러 컷**, S6 24mm 와이드, 돌바닥 위 — 십 년 만의 겨울이 끝남 [내레이션/Wavenet-C (0.0): "근정전의 돌바닥 위에서 — 십 년 만의 겨울이, 그 자리에서 끝났다." (rel 4.0=절대 39.5)], S7 100mm Macro, 돌바닥 위 남은 은장도 (무대사), S8 35mm → 엔드카드, 서 있는 자리만 남음 → 암전 → 타이틀(자막: 제88화 「백일홍 비녀」에서 계속).
> **안티슬롭 ① — 처형 고양 극·비명 배제(plan·정본 안티슬롭 지정)**: 군중·처형대·비명·고양 연출 렌더 **0건**. 치환 — **선 채로 죽기를 택한 권신의 마지막 인간의 값**(S2 7컷 단독 최장): 무릎을 꿇지 않고 선 채로 고백하는 당당하고 쓸쓸한 몸이 전부다. `no appeal, no plea, no kneeling` 전 썬 상설, 군중·위병·집행자 렌더 0건.
> **안티슬롭 ② — "이제 다 끝났어" 슬롭 배제(plan·정본 안티슬롭 지정)**: 마무리 감상 연출·에필로그 태블로 0건. 치환 — **"근정전의 돌바닥 위에서 십 년 만의 겨울이 끝났다"는 차분한 정적**(S6 4비트): 서리가 녹고 첫 빛이 처마에 닿는 **날씨의 변화**만이 감정의 전부다.
> **★ 킬러 컷 — S5(전 100부작 응분, 정본 AG ②)**: 칼이 나가는 초슬로우 모션. **사형 직접 묘사 금지 — 유혈·신체 절단·쓰러진 인물·임팩트 프레임 0건**, 칼날의 은빛 궤적(초슬로우 단일 호) 직후 **바람과 새 소리의 절단 프레임 치환**(2비트 응축). `execution` 어휘 배제 — 시트 생성기 STRIKE_WORDS 전수 차단 가드 확인. `no blood, no wound, no fallen figure, no impact of any kind` 전 썬 상설.
> **S3 비녀 회수 매크로(plan·정본 지정)** — 손끝 3매크로 비트: 허리춤에서의 회수(1) — 손바닥 위의 십 년(2) — 무게를 기억하는 손(3). **십 년 만의 무게는 떨림이 아니라 정지로 렌더** — 손은 떨지 않는다.
> **S8 서 있던 자리만 남음 → 암전(무대사)** — **인물·흔적 0건**: 빈 돌바닥의 정적 → 균일 암전. 붉은 타이틀(제88화 「백일홍 비녀」에서 계속, 13슬롯)은 편집 단계 삽입 — S08 렌더는 암전으로 끝난다.
> **백지 설계 교칙(전편 규격)** — 프레임 내 기물 위 가독 글자 **0건**. 비녀·은장도의 문양은 **조각된 꽃과 잎 무늬로만** 존재하고 글자가 아니다. `no letterforms, no hangul, no hanja` 전 썬 상설. **본화 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기입된다.
> **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계 참조용)뿐**(본화는 가독 허용 인서트 없음). 엔드카드 자막(제88화 「백일홍 비녀」에서 계속)은 편집 단계 삽입, S08 렌더는 암전으로 끝난다.
> **세이프티 가드(plan 절대 준수) — 유혈 직결 어휘 0건**: 본화는 ★ 킬러 컷 회차지만 절단은 전부 치환된다 — `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. 금지 어휘(`poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder`)와 참견 어휘(`slash`·`stab`·`execution`·`kill` 등)는 생성기 `validate()`로 전수 차단 확인 — **`killer`도 `kill`을 포함해 차단된다**(본화 신규 실측: S05 지문의 `KILLER CUT`이 차단되어 `SIGNATURE CUT`으로 기술). 정본 대사 원문은 SRT·보이스 원장에만 기재된다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이설화 — **선 채로 윤경헌을 마주하며 비녀를 회수하고 선고하는 서늘한 눈빛의 궁녀**(다크 파스텔 톤 단아한 궁녀 한복, 소박한 옥비녀, 창백한 피부, 서늘하고 총명한 눈빛, 품속 은장도, 21세 — S1 강림·S3 회수 손·S4 선고·S6 원경 1인). 윤경헌 — **무릎을 꿇지 않고 선 채로 인간의 값을 고백하는 당당하고 쓸쓸한 노년 권신**(짙은 흑립·금실 홍단령·백옥 흉배·매의 눈·권력의 무게가 담긴 주름·허리춤의 비녀, 58세 — S1 기다림·S2 고백 7비트·S4 상대). **이환: 본화 등장 0건**(어전은 비어 있다) — 군왕·위병·궁인·군중·대열 렌더 0건. **인물 상한** — S01 패널당 1인, S02 윤경헌 1인(손 매크로 포함), S03 손·비녀만(얼굴 0건), S04 최대 2인(S4-1)·소품 매크로·설화 1인, S05 인물 0명, S06 최대 1인(원경), S07 인물 0명, S08 인물 0명.
> **입모양 배제(100화 전편 규격)** — 내레이션 3구(S1·S3·S6) + 윤경헌 대사 1구(S2) + 설화 대사 1구(S4) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S5·S7·S8 무대사(효과음 S5 바람·새도 사후 믹싱) — 렌더 전면 무음.
> **동일 보이스 ID 점검**: 내레이션 `ko-KR-Wavenet-C`(0.0) 3구(S1·S3·S6 — 동일 ID 정합성), 윤경헌 `ko-KR-Wavenet-D`(-2.0 — plan 확정치, characters.md -2.5 대신 plan 우선 원칙) 1구(S2), 설화 `ko-KR-Neural2-A`(0.0 — plan 확정치, characters.md -1.0 대신 plan 우선 원칙) 1구(S4) — **인물 간 동일 ID 충돌 없음**(Wavenet-C · Wavenet-D · Neural2-A 상이 모델/문자, 사다리 충돌 0건, 단일 트랙 연속 합성 가능). 파일명: `EP87_S1_NARRATION` / `EP87_S2_YOON` / `EP87_S3_NARRATION` / `EP87_S4_SEOLHWA` / `EP87_S6_NARRATION`. 렌더는 전 썬 무음.
> **가변 컷 배분**: 4/7/3/3/2/4/1/4 = 28컷 — EP13~EP86 전 배분(98종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP86 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP86분 4/5/3/6/2/3/1/4와도 상이). **S2(마지막 인간의 값) 7컷 단독 최장** — 본화 최장 대사(rel 6.5)가 걸린 고백 썬. S1(계단과 기다림)·S6(겨울이 끝남)·S8(서 있던 자리→암전→타이틀) 각 4컷, S3(비녀 회수)·S4(설화의 선고) 각 3컷, **S5(★킬러 컷) 2컷 응축**, **S7(남은 은장도, 무대사) 1컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 8회(초벌 8 + 재렌더 0) 중 최종 채택 8장 — **초벌 재렌더 0건(EP73 이후 최소 생성 회차)**. 최종 PIL 전량 실측 **1024×1536 — S02 초벌만 1023×1537(1px 오차) → LANCZOS 정규화**(원본 증적 `_EP87_S02_1023x1537_pre_normalized.jpg`), 나머지 7장 원본 그대로 정확. 가시 채색(chroma>25 ∧ 최대명도>64) S01~S07 전장 0.00%(S07에 chroma 27의 단일 잡음 픽셀 1개 — 노이즈 수준, 관찰 기록), S08 0.12%(적색 타이틀 — 좌표 전수 확인, 타이틀 열 x400~424·y1022~1294 한정). 생성기 `validate()`(컷수·배분 중복 98종 대조·세이프 어휘·무릎금지/화염금지/letterform/light/lips/no-body 가드) → 렌더 → PIL 전량 실측 → **8장 전량 육안 검독 + 확대 크롭 검독(S08 타이틀 13슬롯 `downloads/qc_crops/Z_EP87_S08_TITLE_ZOOM.png`, 전장 하단 MOOD/DIRECTION 스트립 `downloads/qc_crops/Z_EP87_ALL_BOTTOMS.png`)**. **검독 캐시 함정 재확인(EP67~EP86 계승)**: 동일 경로 전장 재열람은 구버전 첨부를 돌려줄 수 있다 — 재렌더 판정 시 PIL 실측 + md5 해시 대조 + 별도 크롭 경로 재열람으로 수행할 것.
> **plan 기재 대사·슬롯 최종성 확인(팩트체크)**: plan 기재 엔드카드 「제88화 백일홍 비녀에서 계속」은 타이틀 실제 글자수가 **13자**(제/8/8/화/백/일/홍/비/녀/에/서/계/속) — **1자 1슬롯 원칙에 따라 13슬롯** 확정(plan 기재 "13슬롯"과 일치 — 공백 슬롯 삽입 없음, 숫자 8·8은 각각 단독 슬롯 — EP73~EP86 1자 1슬롯 규격 계승, 확대 크롭 검독 통과, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). 정본 대사·보이스 ID·rel/절대 수치는 `SEASON_04_MASTER_SCREENPLAY.md` 제87화 절(218~230행) 직접 열람 재대조 — plan과 1:1 일치. **보이스 P 보정 병기**: characters.md는 윤경헌 Wavenet-D Pitch -2.5, 설화 Neural2-A Pitch -1.0을 표기하나, plan 확정치(윤경헌 -2.0, 설화 0.0)를 본화에 채택 — plan 우선 원칙. **plan 배분 기재 "선행 전 배분 98종"과 실측 98종 일치** — 기계 스캔 수치가 우선.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep87_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep87_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 이설화 다크 파스텔 궁녀 한복, 윤경헌 홍단령의 검붉은 채색, 돌바닥의 실제 회색, 서리의 실제 흰색, 하이키 역광의 실제 색이 실제 색으로 복원된다. **붉은 색은 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **내려가는 계단과 기다리는 몸**(the descending steps, the waiting body), S2 **서 있는 고백과 꿇지 않는 어깨**(the standing confession, the unbent shoulders), S3 **비녀를 빼는 손가락과 닫히는 손**(the drawing fingers, the closing hand), S4 **서 있는 거리와 조용히 드러나는 은**(the standing distance, the quietly emerging silver), S5 **초슬로우의 은빛 호와 몰아치는 바람**(the ultra-slow silver arc, the rushing wind), S6 **녹아 내리는 서리와 도착하는 빛**(the lifting frost, the arriving light), S7 **곧게 누운 은과 얼어 붙은 정적**(the lying silver, the frozen stillness), S8 **빈 돌바닥과 균일한 어둠**(the empty flags, the even darkening).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계슑. 본화 신규 실측: `killer`가 `kill`을 포함해 차단 — `signature cut`으로 기술**). `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. `no letterforms, no hangul, no hanja` 전 썬 상설. **비녀·은장도 문양은 조각된 꽃과 잎 무늬로만** — 가독 글자 렌더 0건. 엔드카드 자막(제88화 「백일홍 비녀」에서 계속)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 3구(S1·S3·S6)와 대사 2구(S2 윤경헌·S4 설화)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S5·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이설화(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes, standing straight and facing the old minister without a tremor, lips closed.
   - **윤경헌(plan·characters.md 지정)**: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power, hawk eyes, standing upright and NOT kneeling, proud and lonely in the same body, lips closed.
   - **인물 상한**: S01 패널당 1인, S02 윤경헌 1인, S03 손·비녀만(얼굴 0건), S04 최대 2인, S05 인물 0명, S06 최대 1인(원경), S07 인물 0명, S08 인물 0명 — 군중·대열·위병·집행자 렌더 0건.
9. **광원 표기**: 전 썬 — **열린 큰문으로 쏟아지는 빈 어전의 하이키 역광이 유일한 광원**(S1~S7 고명도 역광이 돌바닥의 서리를 걷어 올리고, S8은 빛이 균일하게 죽고 암전 진입). `The high-key backlight through the open doors is the only light, never flickering like horror, never strobing` 전 썬 상설(S8은 `the light withdraws evenly as the episode closes` 변형 기재). **EP86 사관의 자리·책상 가드를 본화 돌바닥 궁정에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지(EP78 밤 등불 가드와 동일 원칙).
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 빈 돌바닥·균일 암전 구간 이후의 붉은 타이틀(제88화 「백일홍 비녀」에서 계속, 13슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S3·S6 3구. 윤경헌 `ko-KR-Wavenet-D` (Pitch -2.0 — plan 확정치, Speed 0.9, 시대를 삼킨 고백) — S2 1구. 설화 `ko-KR-Neural2-A` (Pitch 0.0 — plan 확정치, Speed 1.0, 서늘한 선고) — S4 1구. 효과음 — S5 바람·새 소리로 절단(사후 믹싱). 본화 내레이션 3구 + 캐릭터 대사 2구 + 엔드카드 자막 1건 + 효과음 1건. **이환 대사 0구** — 본화는 설화와 윤경헌의 회차다. S5·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 3구·윤경헌 `Wavenet-D`(-2.0) 1구·설화 `Neural2-A`(0.0) 1구 — **인물 간 상이 모델/문자, 사다리 충돌 없음, 단일 트랙 연속 합성 가능**(내레이션 3구는 동일 ID — 정합성 유지). 파일명 분리 규칙 기재(`EP87_S1_NARRATION`/`EP87_S2_YOON`/`EP87_S3_NARRATION`/`EP87_S4_SEOLHWA`/`EP87_S6_NARRATION`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/7/3/3/2/4/1/4 = 28컷 — EP13~EP86 전 배분 98종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S2 7컷 단독 최장**(마지막 인간의 값), S1·S6·S8 각 4컷, S3·S4 각 3컷, **S5 2컷 응축**(★킬러 컷), **S7 1컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **선 채로의 단죄 가드(본화 핵심)**: 단죄는 군중도 처형대도 비명도 없이 — 기다리는 노신과 내려가는 궁녀, 둘의 몸으로만 이루어진다. 전 썬 `no crowd, no guards, no headsman, no kneeling` 상설. 절단의 순간(S5)은 **한 번, 초슬로우의 은빛 호로만** 존재하고 그 직후는 바람과 새뿐이다. 종식(S6~S8)은 감상이 아니라 날씨다 — 서리가 녹고, 빛이 닿고, 은 하나가 돌바닥에 남는다.

---

## 1. S01 첫째 — 계단과 기다림 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP87_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "그는 무릎을 꿇지 않았다. 서 있기를 — 택했다." (rel 4.0=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 4컷)** — 강림(1) — 기다리는 얼굴(2) — 마주 선 둘(3) — 빈 궁정(4). **안티슬롭 가드(plan 지정)** — 처형 고양 극 0건 — 무릎을 꿇지 않기로 택한 자가 기다리고, 내려가는 자가 그 선택을 확인해 준다. **군중·위병·집행자·무릎 꿇음 0건**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly two people in the whole scene, one per frame: the court lady, Seolhwa — a young 21-year-old Korean woman disguised as a palace court lady in an elegant dark pastel hanbok with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes — descending the great stone steps and facing him standing straight without a tremor; and the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power, hawk eyes — waiting on the flags below, standing upright and NOT kneeling, proud and lonely in the same body; no third figure, no king, no guards, no soldiers, no headsman, no crowd, no onlookers, no kneeling figure anywhere in the frame. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, running down the great stone steps and lifting the last of the old frost off the wide grey flags. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide high, slow tilt down: the court lady descending the great stone steps of the hall — the old minister waiting below on the flags, already standing.
2. 85mm close: the old face waiting — the choice already made in it, standing and not kneeling.
3. 50mm medium: the descent ending — the two facing each other across a few last stone flags, she standing, he standing, neither bowing.
4. 35mm wide: the steps above them completely empty — the whole court gone, only the two figures left in the vast stone space.

DESCENT MOTION — IMPORTANT: physically-based the descending steps, the waiting body — she descends at an unhurried, level pace and never once looks down at him from above, he waits standing because standing is what he chose: no kneeling at any point, no crowd, no soldiers, the empty court is the whole world; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 마지막 인간의 값 (절대 07.5~15.0 · 콘티 7컷 ★ 최장)

- **시트**: `downloads/EP87_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [시대를 삼킨 고백 · 윤경헌/`ko-KR-Wavenet-D`, Pitch -2.0 — plan 확정치, Speed 0.9] "나는 그 불 속에서 그것을 취했다. 그것이 그 집안에서 유일하게 불에 타지 않을 것이라고 생각했으므로. 나는 그것을 팔지 않았고, 두지도 않았다. 나는 그저 — 가졌다. 그것이 나의 죄 중에서 — 가장 인간다운 죄였다." (rel 6.5=절대 10.0, 사후 믹싱)
- **연출 특이**: **고백 썬(가변 7컷 단독 최장)** — 고백의 시작(1) — 말로만 존재하는 불(2) — 허리춤의 보물(3) — 꿇지 않은 어깨(4) — 가장 인간다운 죄(5) — 마지막 말(6) — 침묵(7). **안티슬롭 가드(plan 지정)** — 고양·비명·자백 쇼 0건 — 아름다운 것 하나를 취한 인간의 죄를, 서 있는 몸이 침착하게 갚는다. **플래시백·화면 속 화염 0건** — 십 년 전의 불은 그의 말로만 존재한다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one principal figure: the Prime Minister, Yoon Kyeong-heon — an elderly Korean power minister in dark crimson and gold embroidered court robes, a black horsehair official hat, a graying beard, deep wrinkles of power, hawk eyes — standing upright and NOT kneeling, proud and lonely in the same body, confessing with no appeal in his face and no plea in it; a slim ornamental pin with a carved flower is tucked at his waist sash, the flower carving never forming a readable character; no flashback, no dissolve, no fire anywhere in frame, no past image; no second person, no crowd, no king, no guards. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, holding the old face and the wet grey stone flags around it. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 7 panels in order as one continuous ~10 second sequence:
1. 85mm close: the old face lifting to speak — the confession beginning, no appeal in it, no plea.
2. 85mm close, slow push: the steady eyes on her — the fire of ten years ago named in words only, no flashback, no flames in frame.
3. 100mm macro: his old hand resting over the slim object tucked at his waist sash — the thing kept ten years, carried and never shown.
4. 50mm medium: he speaking as he stands — the unbent shoulders of a man who never once knelt, dignity and loneliness in one body.
5. 85mm close: the old face naming its own most human fault — no shame in it and no pride, only the truth.
6. 35mm wide low: the old man standing alone in the vast stone court as the words finish — small against the great hall, and unbowed.
7. 85mm close: the quiet after the confession — his eyes lowering for the first time, the words done.

CONFESSION MOTION — IMPORTANT: physically-based the standing confession, the unbent shoulders — a man paying back a price at last and paying it standing: the shoulders never bend, the hawk eyes stay level on her, the hand rests on the kept thing at his sash as on the only thing that was ever truly his, and when the words are done the eyes lower once, gently, like a room going still when the wind stops; his line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 비녀, 돌아오다 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP87_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 비녀 회수. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "십 년 만의 무게였다. 그녀의 손은 — 그 무게를 기억하고 있었다." (rel 4.5=절대 17.5, 사후 믹싱)
- **연출 특이**: **회수 매크로 썬(가변 3비트)** — 허리춤에서의 회수(1) — 손바닥 위의 십 년(2) — 무게를 기억하는 손(3). **안티슬롭 가드(plan 지정)** — 감정 과장·떨리는 손 0건 — 십 년 만의 무게는 **정지**로 렌더된다. 백일홍 문양은 조각된 꽃 무늬로만 존재한다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands, sleeve and object only, no faces in frame: a young woman's pale steady hand — the court lady Seolhwa's — with the dark embroidered cuff of a hanbok sleeve at the frame's edge, drawing a slim ornamental pin with a carved rose-of-Sharon flower from the waist sash of an elderly minister's dark crimson court robes; the carved flower is only a flower and never a readable character; no letterforms, no hangul, no hanja anywhere; no second person, no faces. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, lifting the weave of the sash cloth and the carved metal of the pin. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro: her fingers drawing the slim ornamental pin with its carved rose-of-Sharon flower from the old minister's waist sash — a slow, exact, unhurried taking.
2. 100mm macro, tilt: the pin lying across her open palm — ten years of weight in one small carved object.
3. 100mm macro: her hand closing around the pin — the fingers steady, remembering the weight without trembling.

HAND MOTION — IMPORTANT: physically-based the drawing fingers, the closing hand — ten years of weight rendered as stillness and not as trembling: the pin leaves the sash slowly and exactly, the cloth settles where it was, the pin lies across the open palm for one long beat, the fingers close around it without a single shake; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 설화의 선고 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP87_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 선고 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "아버님의 이름으로 — 어머님의 은장도로." (rel 3.0=절대 24.0, 사후 믹싱)
- **연출 특이**: **선고 썬(가변 3비트)** — 선고 전의 얼굴(1) — 소매에서 조용히 드러나는 어머니의 은(2) — 수평의 눈(3). **안티슬롭 가드(plan 지정)** — 증오의 열기·환호 0건 — 선고는 속삭임의 온도로 이루어진다. 은장도는 **아직 뽑히지 않은 채** 존재한다 — 드러남만이 렌더된다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — at most two figures, in the first panel only: the court lady, Seolhwa — a young 21-year-old Korean woman in an elegant dark pastel hanbok with a simple jade hairpin, pale porcelain skin, cold piercing intelligent eyes — standing straight and facing the old minister at close distance; and the Prime Minister, Yoon Kyeong-heon — an elderly power minister in dark crimson and gold embroidered court robes, a black horsehair official hat — facing her, standing and not kneeling; the second panel holds hands and sleeve only — a slim ornamental silver sheath with a carved floral fitting emerging quietly from the fold of her sleeve, carried ten years and never yet drawn; the third panel is her cold level eyes alone; no heat of hatred, no triumph, no crowd, no guards. The carved pattern is only flowers and leaves and never a readable character — no letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, holding the distance between the two figures and catching the carved silver as it emerges. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the court lady facing the old minister at the closest distance yet — standing straight, the sentence ready.
2. 100mm macro: the slim ornamental silver sheath emerging quietly from the fold of her sleeve — the mother's small blade, carried and never yet drawn.
3. 85mm close: her cold level eyes at the sentence — no heat of hatred in them, only the temperature of ten years.

SENTENCE MOTION — IMPORTANT: physically-based the standing distance, the quietly emerging silver — the sentence is spoken quietly or not at all: in her father's name, with her mother's silver — and the render is silent, the words arrive later by voice: the two stand their ground without stepping toward each other, the slim silver sheath emerges from the sleeve fold slowly and without ceremony, and her eyes stay level and cold with ten years' temperature and none of hatred's heat; lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 한 번의 움직임 ★ 킬러 컷 (절대 30.0~37.5 · 콘티 2컷 응축)

- **시트**: `downloads/EP87_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 초슬로우. [효과음] 바람·새 소리로 절단 (rel 2.0=절대 31.0, 사후 믹싱) — 무대사, 렌더 완전 무음.
- **연출 특이**: **★ 킬러 컷 썬(전 100부작 응분, 가변 2비트 응축)** — 초슬로우의 은빛 호(1) — 바람과 새(2). **정본 AG ② 절대 준수** — 사형 직접 묘사 금지: 유혈·신체 절단·쓰러진 인물·임팩트 프레임 0건, 절단의 순간은 **은빛 궤적 직후의 바람과 새 소리로 치환**된다. 렌더 텍스트에서 `execution` 어휘 배제 — `signature cut`으로 기술.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: only the slim ornamental silver blade of a small ceremonial sheath leaving it in one single slow arc, and then the wind and the birds; no person's face, no hands, no figure, no impact of any kind shown, no harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure; no letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, catching the polished silver as the single arc takes it and gives it back. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 100mm macro, ultra slow motion: the small silver blade leaving its slim sheath in one single slow arc — the bright silver trajectory crossing the frame once, catching the dawn light.
2. 100mm macro: after the arc — a rush of wind crossing the frame and small birds bursting up beyond the eaves, the stone flags perfectly still.

ARC MOTION — IMPORTANT: physically-based the ultra-slow silver arc, the rushing wind — the moment itself is never shown, the cut is replaced by wind and birdsong exactly as the script orders: the polished silver leaves its slim sheath in one single slow arc crossing the frame exactly once, never twice, and then the wind rushes across the flags, dust and a loose morning thread stir and settle, and small birds burst up beyond the roof eaves into the pale sky while the wide stone flags stay perfectly still; no sound in the render — wind and birdsong arrive later by post mix; lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 겨울이, 끝나다 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP87_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "근정전의 돌바닥 위에서 — 십 년 만의 겨울이, 그 자리에서 끝났다." (rel 4.0=절대 39.5, 사후 믹싱)
- **연출 특이**: **종식 썬(가변 4비트)** — 서리가 뜨는 궁정(1) — 물러나는 서리(2) — 처마에 닿는 첫 빛(3) — 한 방울(4). **안티슬롭 가드(plan 지정)** — "이제 다 끝났어" 슬롭 0건 — 종식은 감상이 아니라 **날씨의 변화**로만 렌더된다. 눈물·움켜쥠·에필로그 태블로 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — at most one figure, far and small, in the first two panels only: the court lady, Seolhwa — a young 21-year-old Korean woman in an elegant dark pastel hanbok with a simple jade hairpin — standing far away on the vast stone court and not moving, not weeping; the third and fourth panels hold no figure at all — the roofline and the flagstone; no crowd, no guards, no second person. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, turning across the frost smoke and the wet grey flags and reaching the great tiled roofline. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide: the vast stone court seen low across the flags — the frost of ten winters lifting off the stones like thin smoke, one small figure standing far.
2. 50mm medium: the frost letting go of the flags around the standing figure's feet — the stones coming up dark and wet.
3. 24mm wide: the first pale morning light reaching the great roofline beyond the court — the winter ending in the sky as well.
4. 100mm macro: one drop of melted frost running off the edge of a flagstone — the ten-year winter ending in a single drop of water.

FROST MOTION — IMPORTANT: physically-based the lifting frost, the arriving light — the ending is weather and nothing else: the frost lifts off the stones like thin smoke, the last white lace of it dissolves around the standing figure's feet, the first pale morning light reaches the great tiled roofline, and one drop of melted frost gathers at a flagstone's edge and falls once, the stone darkening where it lands; no speech, no weeping, no triumph, no 'it is over' mood; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 남은 은장도 (절대 45.0~52.5 · 콘티 1컷 절제)

- **시트**: `downloads/EP87_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. 무대사 — 렌더 완전 무음.
- **연출 특이**: **절제 썬(가변 1컷)** — 돌바닥 위 정갈하게 남은 은장도. **인물 0명 — 손·발·그림자까지 0건**, 사물이 전부다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figure anywhere in frame: only the mother's slim ornamental silver sheath lying alone and perfectly straight on the wide grey stone flags, its carved metal fitting catching one line of pale dawn light, a thread of frost-water beside it; no hand, no feet, no shadow of a person, no figure of any kind; the carved pattern is only flowers and leaves and never a readable character — no letterforms, no hangul, no hanja. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, laying one bright line along the carved silver and wetting the grey stone around it. The backlight stays calm, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence:
1. 100mm macro, static hold: the mother's slim silver sheath lying alone and perfectly straight on the wide stone flags — the carved fitting catching one line of dawn light, no figure anywhere in frame.

SILVER MOTION — IMPORTANT: physically-based the lying silver, the frozen stillness — the object is the whole subject and the stone around it is the rest: nothing moves but a thread of frost-water thinning beside the silver and the dawn line travelling almost imperceptibly along the carved fitting; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 서 있던 자리 → 암전 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP87_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제88화 「백일홍 비녀」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 4컷)** — 인물·흔적 0명: 서 있던 자리(1) — 텅 빈 궁정(2) — 완전한 암전(3) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **안티슬롭 가드** — 종반 연출·유품 태블로·에필로그 0건 — 남는 것은 돌바닥의 한 자리뿐이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figure anywhere in frame, and no trace of one: only the empty place on the wide stone flags where a man stood — nothing left there but the stone itself, the frost melted as evenly on that flag as on every other — and then the whole stone court completely empty at dawn, the winter gone from the flags, the great hall and its open doors beyond; no figure, no shape, no cloth, no mark of any kind, no aftermath tableau. No letterforms, no hangul, no hanja anywhere. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the high-key backlight pouring through the throne hall's great open doors is the only light, and it withdraws evenly as the episode closes — the flags pale by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the backlight's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence (the sheet's fourth panel — the red next-episode title card — is edit-stage reference only and is NOT rendered):
1. 35mm wide low: the empty place on the stone flags where a man stood — nothing left there but the stone, the frost melted evenly everywhere.
2. 24mm wide: the whole stone court completely empty at dawn — the winter gone from it, the great hall beyond.
3. The frame darkens evenly until nothing remains — complete black, held.

PLACE MOTION — IMPORTANT: physically-based the empty flags, the even darkening — the stone simply holds the place where a man chose to stand: nothing is left on it, the court stays empty in the pale dawn, and the light dies evenly, by degrees, until the last thing visible is the grey stone and then nothing; no finale fanfare, no 'the end' mood; the render ends in complete black — the next-episode title is edit-stage only; the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP87 원장 완결. 콘티 시트 8종(`downloads/EP87_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제88화 「백일홍 비녀」 —**
