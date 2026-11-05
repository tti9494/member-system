# 「혈화의 궐」 EP64 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제64화 「흑영대의 깃발」 8썬표(`master_screenplay/SEASON_03_MASTER_SCREENPLAY.md` `제64화 「흑영대의 깃발」` 절, 원전: 제64장 정본) + `characters.md` 캐릭터 앵커 + EP21~EP63 원장 템플릿(동일 규격)
> **범위**: EP64 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP63 S8 엔드카드 「제64화 흑영대의 깃발에서 계속」이 본화의 무대다. **서사 인계 라인** — EP63의 백일홍 백 명 선전포고와 중전의 첫 공포에서 본화 S1 선창의 깃발·문서 매크로로 직결되고, 본화 S2 무결의 보고(왕의 이름으로 세워진 암살단·중궁전)가 S3~S4 설화의 분석·예측으로, S6~S7의 선왕의 사인 매크로와 왕의 침묵으로 귀결된다. **등장 인물** — 깃발·문서 매크로(S01, 무인물) + 강무결(S02 단독 보고) + 이설화(S03~S04) + 익명 인물 실루엣(S05) + 손 매크로·무결·이환(S06~S07) + 익명 손(S08). 중전 윤씨·윤경헌·이정현 **도상 0건** — 이름 인용으로만 존재.
> **안티슬롭 ① — 암살단 위협 과장 배제(plan·정본)**: 흑영대를 위협적 암살단 연기로 시각화 **렌더 0건**. 치환 — **깃발의 낙관이라는 종이의 무게**(S01 킬러 썬): 도장 하나가 찍힌 깃발·문서의 물리적 무게만이 공포의 전부. `no threatening poses, no menace, no lurking assassins, no action scene, no fighting` S01 상설.
> **안티슬롭 ② — 배 습격 액션 과장 생략(plan AG ①)**: 습격·전투 렌더 **0건**. 치환 — **붙잡힌 선창의 깃발·문서 매크로로 압축**. `no assault, no battle, no fighting, the attack itself is never shown` S01 상설.
> **안티슬롭 ③ — "순서가 그렇게 되어 있습니다" 해설 반복 배제(정본)**: 설화의 예측(S4)은 정본 대사 1:1로 **한 번만** 말해지고 반복 해설 금지 — 예측의 증명은 EP65 서사가 가져간다. `no explanatory monologue, no one repeats the order` S03~S04 상설.
> **백지 설계 교칙(plan 절대 준수) — 깃발 낙관 가독 글자 차단**: 선왕의 사인(낙관)은 **추상적 압착 문양만** — `abstract pressed shape only, strokes that never form letters, no legible hangul, no legible hanja, no readable words of any kind` S01·S06 상설. 시트 단계부터 가독 글자 0건(시트 결함 이력 — S08 P1 한자형 낙관 1건 --edit 정정 완료, 아래 결함 기록).
> **세이프티 가드(plan 절대 준수) — 유혈·흉기 가동 0건**: 본화는 **칼이 한 번도 뽑히지 않는 화다** — `no weapon drawn anywhere, the sheathed sword is never touched` 전 썬 상설, `no violence, no wounds, no injuries anywhere` 전 썬 상설, `all characters are adults` 전 썬 상설, `no flashbacks, no memory scenes, no time transitions` 전 썬 상설. `blood` 어휘는 **부정 가드 나열(`no blood`)로만** 사용 — 시트 프롬프트 소스에는 일절 미기재(생성기 validate() 차단).
> **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 일체 금지 — **깃발 낙관(S01·S06)은 추상 압착 문양만**, `no readable letters, no characters, no labels anywhere` 상설. **붉은 색은 S08 타이틀뿐**(시트 0.34% — 타이틀 열 한정). 엔드카드 자막(제65화 「남하하는 격문」에서 계속)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
> **금지 어휘 0건**: 생성기 `validate()`가 전 씬 소스(헤더·무드·로케이션·패널 5요소·디렉션)를 소문자 전수 스캔해 `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` **프로그램적 차단**(0건 확인). 원장 실사 블록도 전수 수동 스캔 — 금지 어휘 잔입 0건(부정 가드 나열 `no blood`만 허용).
> **캐릭터 앵커(plan 지정)**: 강무결 — **무관복, 차분한 보고**(characters.md EP37~EP41 28세 청년 무관 앵커 계승 — clean-shaven, 뺨 검흔, 남색 융복·환도). 이환 — **병상에서 깃발을 내려다보는 왕의 침묵**(EP62 병상 앵커 계승 — 염백 병살복·관·장식 0건, clean-shaven 무참 가드 포함, 붉은 곤룡포·익선관 혼입 금지). 이설화 — **궁녀 복식, 옥비녀 앵커, 차가운 정세 분석**(characters.md 등록 앵커). 익명 인물(S05)·익명 손(S08) — `no identifiable features`.
> **입모양 배제(100화 전편 규격)**: 내레이션 2구(S1·S5)·무결 1구(S2)·설화 2구(S3·S4) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S6·S7·S8(무대사) 렌더 전면 무음.
> **동일 보이스 ID 점검 — 발동(EP38·EP41 선례의 2중 배역)**: 내레이션 `ko-KR-Wavenet-C`(0.0)와 무결 `ko-KR-Wavenet-C`(plan 지정 −1.0)가 한 화에 공존 — §0-13 4중 장치 필수. 설화 `ko-KR-Neural2-A`(−1.0)는 타 계열 — 충돌 없음.
> **가변 컷 배분**: 4/5/4/3/3/5/2/2 = 28컷 — EP19~EP63 44종 배분 전수 대조 미중복(생성기 `validate()` `DISTRIBUTION not in PRIOR` 단정 통과, PRIOR에 EP63분 4/5/3/4/3/3/3/3·EP60분 4/5/4/3/4/3/2/3 포함). **무결의 보고(S2)와 선왕의 사인 매크로(S6) 5컷 최장** — 보고의 비트 분해와 종이의 무게가 축적되는 매크로 연쇄를 본화 최대 훅으로. 설화의 분석(S3) 4컷, S1 4컷, S4·S5 3컷, **S7·S8 2컷 최소**(침묵 → 접힘 → 암전의 소진 종결) — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 정정 기록**: 총 이미지 생성 11회 중 최종 채택 8장. 결함 3종 — ① **S08 P1 서류 꾸러미의 한자형 낙관 렌더**(백지 설계 교칙 위반) → 원본 보존(`qc_ep64/ORIG_S08_before_edit.jpg`) 후 패널 한정 `--edit`로 추상 압착 문양 치환 — 텍스트·타이틀 열 전량 생존 ② **S04 P1 설화 머리 꽃 장식 앵커 위반 + P3 벽 두루마리 한자형 낙서**(문자 가드 위반) → 원본 보존 후 패널 한정 `--edit` 1차(꽃 제거·두루마리 백지화는 반영, 단 P3가 재생성되며 침상 양옆 등불 2개의 신규 이중 광원 유입) → **v2 재정정으로 등불 소등 완료**(`EDIT_S04_v1.jpg` 중간본 보존) ③ **S05 P3 원경 내전 등불·창광 노출**(DIRECTION 박스의 달빛 단일 광원 지문과 상충) → 원본 보존 후 패널 한정 `--edit`로 전 건물 소등·달빛 단일 광원 확보. 최종 PIL 전량 실측 1024×1536 전장 정확, 가시 채색 S01~S07 0.00%·S08 0.34%(적색 타이틀 — 좌표 전수 확인, 타이틀 열 x404~434·y764~1230 한정). 생성기 `validate()`(컷수·배분 중복·세이프 어휘) → 렌더 → PIL 전량 실측 → **8장 전량 육안 검독 + 확대 크롭 검독(S08 타이틀 14슬롯, S01/S06 낙관 추상성, S04 P1 머리 장식)**.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep64_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep64_sheets.py S01`), 전체는 `ALL`(명시적).

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (장소별 광원 가드) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 본화의 적색은 **S08 붉은 타이틀(편집 단계 삽입)뿐**이며, 그 외 적색 액센트 0건이 기준이다(혈액 표현 없는 화 — 붉은 선 가드도 없다).
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **젖은 천과 바다 바람**(the wet cloth, the sea wind, the snapping folds), S2 **단정한 무릎과 약불 김**(the kneeling stillness, the brazier steam, the resting fist), S3 **접힌 손과 등란 빛**(the folded hands, the lamp glow, the thin line of light), S4 **불꽃과 한기**(the small flame, the cold draught, the standing glow), S5 **서리와 달빛**(the frost, the moonlight, the long shadow), S6 **천의 조직과 누르는 손가락**(the coarse weave, the pressed mark, the hovering finger), S7 **이불 위 손과 약불**(the quiet knuckles, the steady brazier, the moonlit lattice), S8 **접히는 천과 암전**(the folding cloth, the dimming light, the frame emptying to black).
5. **세이프 필터**: `poison`·`dying` 및 `death`·`dead`·`corpse`·`blood`·`suicide`·`necrosis`·`murder` 어휘 사용 절대 금지(plan — 생성기 validate() 차단 확인). `no violence, no wounds, no injuries anywhere` 전 썬 상설. **본화는 칼이 한 번도 뽑히지 않는다** — `no weapon drawn anywhere, the sheathed sword is never touched` 전 썬 상설. `all characters are adults` 전 썬 상설. `no flashbacks, no memory scenes, no time transitions` 전 썬 상설.
6. **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 일체 금지 — **깃발 낙관(S01·S06)은 추상 압착 문양만 — 글자 0건**(백지 설계 교칙). **붉은 색은 S08 타이틀뿐**. 엔드카드 자막(제65화 「남하하는 격문」에서 계속)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 발화 구(내레이션 S1·S5 / 무결 S2 / 설화 S3·S4) 전부 무음 렌더 + 사후 믹싱 — `lips closed throughout` 전 썬 상설. S6·S7·S8(무대사) 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **강무결(plan 지정 — 무관복, 차분한 보고)**: the guard captain Kang Mugeol — a lean upright 28-year-old Korean military officer, clean-shaven, no beard, a faint old scar on one cheek, heavy quiet eyes, a dark navy military officer's coat (yungbok), a single-edged Korean sword (hwando) sheathed at his hip and never drawn, the stillness of a man reporting only what he has verified, lips closed. (**환도 미발도 — 본화 전 썬에서 칼은 한 번도 뽑히지 않는다.**)
   - **이환(plan 지정 — 병상의 왕)**: the young king Ihwan — a pale, refined 24-year-old Korean man, ill and thin, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain undyed white sickbed robe with no crown and no ornament, his hair simply tied back, propped upright on the bedding, alone, his dark eyes carrying deep quiet sorrow, never wide in shock, no rage, no gesturing, lips closed. (**붉은 곤룡포·익선관 착용 금지 — 병상 본화는 염백 병살복이 본화의 전부.**)
   - **이설화(plan 지정 — 차가운 정세 분석)**: the court lady Seolhwa — a 21-year-old Korean woman with East Asian Korean features and straight black Korean hair, serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes holding a calm that never widens in shock — the cold, unhurried composure of a woman reading the whole board before she speaks, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, absolutely no earrings anywhere, no veil and no cloth covering her face, no tassels, no dangling hair ornaments, no flowers in the hair, no other pin, lips closed. (**가체·떨잠·귀걸이·베일·꽃 장식 혼입 금지 — 단일 옥비녀가 본화의 전부.**)
   - **미등장 인물**: 중전 윤씨·윤경헌·이정현 **본화 도상 0건** — 이름 인용으로만 존재하는 화면 구성. 앵커 미기재. S05의 벽 그늘 인물·S08의 접는 손은 `no identifiable features` 익명 규격.
9. **광원 표기(장소별 광원 — AG 가드)**: 붙잡힌 배의 선창(S01) — **돛대에 묶인 폭풍 등 하나가 유일 광원**(the single storm lantern lashed to the mast is the only light source). 왕의 병상 침전(S02·S03·S04·S06·S07) — **창살 달빛 + 약불의 두 광원 축**(two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier — EP52 확립 병상 규격 계승; 등불·촛불 추가 혼입 금지). 서리 어전 마당(S05) — **달빛이 유일 광원**(cold moonlight is the single light source — 원경 창광·등불 혼입 금지). `never floating, never glowing supernaturally`·`no crushed blacks, no milky flat darkness` 전 썬 상설.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 암전 이후의 붉은 타이틀(제65화 「남하하는 격문」에서 계속)은 **편집 단계에서 삽입**. S8 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S5 2구. **무결** `ko-KR-Wavenet-C` (**Pitch −1.0, Speed 1.0, 묵직하고 절제된 무사 톤 — plan 지정치**) — S2 1구. 설화 `ko-KR-Neural2-A` (**Pitch −1.0**, Speed 1.0, 서늘한 분석·예측 — characters.md 등록치 기반) — S3·S4 2구. 본화 대사 5구(합성 5구) + 엔드카드 자막 1건. S6·S7·S8(무대사) — 배정 없음.
13. **동일 보이스 ID 2중 배역 차단(§0-13 재가동 — EP38·EP41 선례)**: **내레이션·무결이 모두 `ko-KR-Wavenet-C`**이며 한 화에 공존한다. 혼동 차단 4중 장치 — ① 2배역 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 파일명 규칙 준수: 내레이션 `EP64_S1_NARRATION`·`EP64_S5_NARRATION`, 무결 `EP64_S2_MUGYEOL`, 설화 `EP64_S3_SEOLHWA`·`EP64_S4_SEOLHWA`, ③ **피치 사다리를 매 행 강제 표기**: 내레이션 `Pitch 0.0` > 무결 `Pitch −1.0` — 차 1.0(내레이션이 상부, 무결이 하부 — 사다리 이탈 시 재합성), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인. 하나라도 누락되면 재합성한다. (characters.md 무결 등록치 Pitch −1.5와 plan 지정치 −1.0의 차이는 **plan 우선** — 본화는 −1.0으로 합성.) 설화 Neural2-A는 타 계열 — 2중 배역 충돌 없음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/5/4/3/3/5/2/2 = 28컷 — EP19~EP63 44종 배분 전수 대조 미중복(생성기 `validate()` 단정 통과). **S2·S6 5컷 최장**(보고의 비트 분해·사인 매크로 연쇄), **S3 4컷**(분석의 단계적 전개), S1 4컷(깃발·문서의 축적), S4·S5 3컷, **S7·S8 2컷 최소**(침묵과 접힘의 소진 종결) — "3컷·4컷 고정" 슬롭 회피.

---

## 1. S01 첫째 — 깃발에 찍힌 도장 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP64_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 붙잡힌 배의 선창 — 흑영대의 깃발과 문서. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "흑영대의 깃발에도 — 도장이 찍혀 있었다." (rel 3.5=절대 2.5, 사후 믹싱)
- **연출 특이**: **종이의 무게 썬(가변 4컷, 무인물)** — 흑영대의 깃발, 바다 바람에 젖은 천이 펄럭임(1컷) — 깃발 아래 줄로 묶인 문서 꾸러미, 낙관이 찍힌 면(2컷) — 문서 면의 낙관 — 글자가 되지 않는 추상 압착 문양(3컷) — 선창 판자 위 깃발과 문서가 함께 놓인 전경(4컷, **종이의 무게**). 배 습격·암살단 위협 렌더 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures at all in this scene: macro shots of a plain black corps banner's wet cloth snapping in the sea wind on the captured ship's bow deck at night, and the bundle of papers bound with cord beneath it — the papers' faces blank, the stamped seal mark an abstract pressed shape only, strokes that never form letters, no legible hangul, no legible hanja, no readable words of any kind. No person anywhere, no identifiable features, no hands. No assault, no battle, no fighting, the attack itself is never shown. No flashbacks, no memory scenes, no time transitions. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: the single storm lantern lashed to the mast is the only light source of the captured ship's bow deck — a low warm pool of lantern glow grazing the banner's folds and the wet deck planks, the sea beyond holding the dark of night. The lantern burns only as a physically-based flame, never floating, never glowing supernaturally. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the black banner's wet cloth edge snapping in the sea wind on the captured ship's bow.
2. 100mm macro, static: beneath the flag — a bundle of papers bound with cord, sea-sprayed.
3. 100mm macro, static: a stamped seal mark on the papers' face — an abstract pressed shape, never letters.
4. 100mm macro, static: flag and papers together on the deck planks — the whole weight of the corps in paper.

CLOTH MOTION — IMPORTANT: physically-based the wet cloth, the sea wind, the snapping folds — the corps is not shown as a threat: its whole danger is a stamped seal, the weight of paper; nothing moves but the wind, no one is seen, no action scene; the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 무결의 보고 (절대 07.5~15.0 · 콘티 5컷 · ★ 최장 썬)

- **시트**: `downloads/EP64_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 무결의 보고. [묵직한 폭로 · 무결/`ko-KR-Wavenet-C`, Pitch −1.0, Speed 1.0 — plan 지정치] "십 년 전에 세워진 어전 직속의 암살단이오. 왕의 명이 아니라 — 왕의 눈을 피하기 위하여 왕의 이름으로 세워진 자들. 지금 그 깃발을 쥔 것은 — 중궁전이오." (rel 6.5=절대 10.0, 사후 믹싱)
- **연출 특이**: **보고 썬(가변 5컷 — 본화 최장)** — 침전 전경, 침상 발치에 정식으로 무릎 꿇은 무결과 이불에 기대 앉은 이환(1컷) — 보고하는 무결의 얼굴, 한 치 흔들림 없음(2컷) — 아무 말 없이 듣는 이환, 눈은 내려감(3컷) — 무릎에 얹힌 주먹, 보고의 유일한 무게(4컷) — 보고 후의 침묵이 덮이는 왕의 얼굴(5컫). 고함·폭로극 연기 0건 — 차분한 보고의 물리만. **동일 보이스 ID 2중 배역(내레이션 0.0 > 무결 −1.0) — §0-13 4중 장치 필수.**

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night, two people only: the guard captain Kang Mugeol — a lean upright 28-year-old Korean military officer, clean-shaven, no beard, a faint old scar on one cheek, heavy quiet eyes, a dark navy military officer's coat (yungbok), a sheathed Korean sword (hwando) at his hip that is never touched and never drawn, kneeling formally at the foot of the raised bed, the stillness of a man reporting only what he has verified, lips closed; and the young king Ihwan — a pale, refined 24-year-old Korean man, ill and thin, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain undyed white sickbed robe with no crown and no ornament, his hair simply tied back, propped upright on the bedding listening without a word, eyes lowered, lips pressed shut. No other person anywhere. No weapon drawn anywhere, the sheathed sword is never touched. All characters are adults. No shouting, no accusation scene, no dramatic reveal pose. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm wide, static: the royal sickchamber at night — the guard captain kneeling at the foot of the bed, the king propped in the bedding.
2. 85mm medium, static: the captain's face in report — steady, level, unhurried.
3. 85mm close, static: the king listening — the eyes lowered, saying nothing.
4. 85mm close, static: the captain's fist resting on his knee — the report's one visible weight.
5. 85mm close, static: the king's face again — the silence after the report.

REPORT MOTION — IMPORTANT: physically-based the kneeling stillness, the brazier steam, the resting fist — the report is delivered on his knees and in a level voice: no one shouts, no accusation scene, no dramatic reveal pose; the king says nothing; the words are voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 흑영대가 사발을 깬 이유 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP64_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 흑영대가 사발을 깬 이유. [서늘한 분석 · 설화/`ko-KR-Neural2-A`, Pitch −1.0, Speed 1.0] "그들은 윤경헌을 구한 것이 아니라 — 그의 입을 다시 열리게 한 것이지요. 윤경헌은 십 년 전 계약서를 아는 — 유일한 산 증인이나이다." (rel 5.5=절대 17.5, 사후 믹싱)
- **연출 특이**: **분석 썬(가변 4컷)** — 침전 가장자리 등란 빛으로 걸어 들어오는 설화(1컷) — 차갑고 서두르지 않는 눈, 분석의 시작(2컷) — 그녀의 어깨 너머 이불 속의 왕, 판독 불가한 얼굴(3컷) — 접힌 두 손, 측정된 정지(4컫). 고함·폭로·해설 과장 0건 — 정세 분석의 서늘함만.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night, two people: the court lady Seolhwa — a 21-year-old Korean woman with East Asian Korean features and straight black Korean hair, serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes holding a calm that never widens in shock — the cold, unhurried composure of a woman reading the whole board before she speaks, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, absolutely no earrings anywhere, no veil and no cloth covering her face, no tassels, no dangling hair ornaments, no flowers in the hair, no other pin, lips closed; and the young king Ihwan — a pale, refined 24-year-old Korean man, ill and thin, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain undyed white sickbed robe with no crown and no ornament, propped upright on the bedding beyond her shoulder, listening, his pale face unreadable, lips pressed shut. No weapon anywhere. All characters are adults. No explanatory monologue beyond the scripted words, no one repeats the order. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the court lady stepping into the lamplight at the chamber's edge — come to give her reading.
2. 50mm close, static: her cold unhurried eyes — the analysis beginning.
3. 50mm medium, static: past her shoulder — the king in the bed, listening, his face unreadable.
4. 50mm close, static: her folded hands — measured, still, certain.

STILLNESS MOTION — IMPORTANT: physically-based the folded hands, the lamp glow, the thin line of light — she does not accuse, she analyses: the corps broke the bowl not to spare the regent but to open his mouth again, the only living witness to the contract of ten years ago; her voice is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 입이 열리면 섭정이 유업을 얻는다 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP64_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 입이 열리면 섭정이 유업을 얻는다. [서늘한 예측 · 설화/`ko-KR-Neural2-A`, Pitch −1.0, Speed 1.0] "중전 마마는 숙부를 살려서 쓰실 것이오. 그러고 나서 — 그 숙부를 죽이실 것이오. 순서가 그렇게 되어 있나이다." (rel 5.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **예측 썬(가변 3컷)** — 그림자에 반쯤 가린 얼굴로 미동 없이 내뱉는 예측(1컷) — 둘 사이의 작은 불꽃, 한기에 단 한 번 굽음(2컷) — 방 전체, 예측 후의 침묵(3컷). **해설 반복 배제** — 예측은 한 번 말해지고 그 증명은 EP65가 가져간다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night, three people, no crowd: the court lady Seolhwa — a 21-year-old Korean woman with East Asian Korean features and straight black Korean hair, serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes holding a calm that never widens in shock, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, no earrings, no veil, no tassels, no flowers, no other pin, lips closed; the young king Ihwan — a pale, refined 24-year-old Korean man, ill and thin, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain undyed white sickbed robe with no crown and no ornament, propped unmoving in the bed; and the guard captain Kang Mugeol — a lean upright 28-year-old Korean military officer, clean-shaven, no beard, in a dark navy military officer's coat, a dark still shape by the door, his sheathed sword never touched. No weapon drawn anywhere. All characters are adults. The prediction is stated once and never explained — no explanatory monologue, no one repeats the order. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: her face half in shadow — the prediction delivered without a tremor.
2. 85mm close, static: the small flame between them — bending once in the cold draught.
3. 85mm wide, static: the whole chamber — the two of them and the silence after the prediction.

FLAME MOTION — IMPORTANT: physically-based the small flame, the cold draught, the standing glow — the prediction is stated once and never explained: its proof belongs to a later night; no one repeats the order, no one reacts with a gesture; her voice is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 백일홍의 내기 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP64_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 백일홍의 내기, 그 순서의 끝자락에 백일홍이 서기로 함. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "그 순서의 끝자락에 백일홍이 서기로 한 것 — 그것이 이번 겨울의 진짜 내기였다." (rel 4.5=절대 32.0, 사후 믹싱)
- **연출 특이**: **내기 썬(가변 3컷)** — 겨울 달 아래 첫서리 내린 궐의 지붕들(1컷) — 벽의 긴 그늘 속, 담당을 맡기로 한 익명 인물 한 명이 홀로 서 있음(2컷) — 마당 저편, 중궁전의 담장 뒤 불빛(3컷, **끝자락**). 군중·집회·고함 0건 — 달빛 아래 조용한 인수인계의 종점.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one anonymous figure only: the palace roofs under a cold winter moon with the first frost white on the dark tiles, and a single anonymous figure standing apart in the long shadow of the wall — a plain dark cloak, no identifiable features, standing the way a person stands who has agreed to hold a position. No crowd, no gathering, no council scene, no chanting, no second figure anywhere. All characters are adults. No weapon anywhere. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: cold moonlight is the single light source of the frosted courtyard — silver moonlight on the frost-white stones and tiles, the buildings standing dark and unlit, no lamp glow, no window light anywhere in the scene. The moon never floats, never glows supernaturally. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the palace roofs under a winter moon — the first frost white on the tiles.
2. 35mm medium, static: in the wall's long shadow — one anonymous figure standing apart, holding.
3. 35mm wide, static: across the courtyard — the Inner Court's lamps burning behind their walls.

WAGER MOTION — IMPORTANT: physically-based the frost, the moonlight, the long shadow — the real wager of this winter stands quietly at the end of the sequence: the corps agreed to stand there, and the paper of the palace will turn on it; no gathering, no council scene, no chanting; the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 깃발 위 도장, 선왕의 사인 (절대 37.5~45.0 · 콘티 5컷 · ★ 최장 썬)

- **시트**: `downloads/EP64_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 깃발 위 도장 — 선왕의 사인. **무대사** — 렌더 전면 무음.
- **연출 특이**: **사인 매크로 썬(가변 5컷 — 본화 최장)** — 낮은 목기 탁자 위에 펼쳐진 흑영대의 깃발, 모서리의 낙관(1컷) — 낙관 자체, 글자가 되지 않는 추상 압착 문양(2컫) — 압착 문양을 뚫고 이어지는 천의 거친 조직(3컷) — 문양 위 한 뼘을 맴도는 손가락, 아직 닿지 않음(4컷) — 천 가장자리를 따라 쏟아지는 약불 빛, 어둠 속으로 가라앉는 문양(5컷, **약불 너머**). 대사 0건 — 종이의 무게가 천으로 이어지는 조용한 축적.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — cloth, hands and one hovering finger: macro shots of the black banner lying unfolded across the low wooden table, sea-salt still in its folds, its stamped seal mark at its corner — the mark an abstract pressed shape only, strokes that never form letters, no legible hangul, no legible hanja, no readable words of any kind — the coarse weave of the cloth running unbroken through the pressed mark, a single fingertip hovering an inch above the mark and never touching it, the hand seen only as fingers, no face in the frame. No weapon anywhere. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: the small low glow of the medicine brazier is the only light on the cloth — one warm pool of brazier light falling off toward the banner's edge, beyond which the mark sinks into darkness the light cannot reach. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the black banner lying unfolded across a low wooden table — the seal mark at its corner.
2. 100mm macro, static: the seal mark itself — an abstract pressed shape in darker pigment, never letters.
3. 100mm macro, static: the coarse weave of the cloth running unbroken through the pressed mark.
4. 100mm macro, static: a fingertip hovering an inch above the mark — not yet touching.
5. 100mm macro, static: the brazier glow falling off the cloth's edge — the mark sinking into the dark.

MARK MOTION — IMPORTANT: physically-based the coarse weave, the pressed mark, the hovering finger — the flag carries the late king's own mark: the corps was raised under the king's name, against the king's eyes; the cloth says it without a single readable word; the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 왕이 그 깃발을 볼 때 (절대 45.0~52.5 · 콘티 2컷)

- **시트**: `downloads/EP64_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 왕이 그 깃발을 볼 때. **무대사** — 렌더 전면 무음.
- **연출 특이**: **침묵 썬(가변 2컷 — 본화 최단)** — 침상에 기대 앉은 이환, 낮은 탁자 위 펼쳐진 깃발의 낙관을 내려다봄(1컷) — 약불 빛 속 그의 얼굴, 앞 왕의 도장을 읽는 왕의 침묵(2컫). 분노·제스처·독백 0건 — 침묵이 판독의 전부.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure only: the young king Ihwan — a pale, refined 24-year-old Korean man, ill and thin, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain undyed white sickbed robe with no crown and no ornament, his hair simply tied back, propped upright on the bedding of the royal sickchamber, alone, the unfolded black banner on the low table before him, his eyes fixed on the abstract pressed seal mark at its corner, saying nothing, the silence of a king reading the mark of the king before him, his grief kept where grief is kept, no tears, no rage, no gesture, lips pressed shut. No attendant anywhere in the frame. The banner carries an abstract pressed shape only — no legible hangul, no legible hanja, no readable words of any kind. No weapon anywhere. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 85mm medium, static: the king propped in his bed — the unfolded flag on the low table before him.
2. 85mm close, static: his face in the brazier glow — the silence of a king reading the mark of the king before him.

SILENCE MOTION — IMPORTANT: physically-based the quiet knuckles, the steady brazier, the moonlit lattice — the king looks at the flag and says nothing: what he reads in the mark is his alone; no rage, no gesture, no speech; the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 깃발이 접힘 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 2컷)

- **시트**: `downloads/EP64_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드 — 깃발이 접힘 → 암전 → 타이틀. **무대사** — 렌더 전면 무음 / 자막: 제65화 「남하하는 격문」에서 계속
- **연출 특이**: **접힘 썬(가변 2컷)** — 익명의 두 솘이 나무 궤짝 속으로 깃발을 접어 넣고, 방의 빛이 접힘을 따라 고르게 어두워짐(1컷) — 붉은 세로 타이틀(2컷, 편집 단계 전용 — 「제65화 남하하는 격문에서 계속」 14슬롯 단일 세로 열). **렌더는 완전 암전으로 끝난다.**

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a pair of anonymous hands only: the black banner being folded away into a wooden chest by a pair of anonymous hands, no face anywhere, no identifiable features, the room dimming evenly around the fold — the lattice moonlight thinning, the brazier glow low. No other person anywhere. The banner carries an abstract pressed shape only — no legible hangul, no legible hanja, no readable words of any kind. No weapon anywhere. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds, no injuries anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier — both thinning as the banner folds away. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 35mm medium, static: the flag being folded away into a wooden chest by anonymous hands — the room dimming around the fold.
2. End card for the edit stage only — one vertical column of red Korean characters on black (the render itself must end in complete black; the title card is inserted in editing).

FOLD MOTION — IMPORTANT: physically-based the folding cloth, the dimming light, the frame emptying evenly to complete black without a sound — the flag goes into the chest and the light goes with it; the render ends in complete black, no figure, no words, no readable marks in the end frame; the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션 — S1·S5 2구 |
| 무결 | `ko-KR-Wavenet-C` | **−1.0** | 1.0 | 묵직한 폭로 · 차분한 보고 — **plan 지정치**(characters.md 등록치 −1.5와의 차이는 plan 우선 — §0-13) — S2 1구 |
| 설화 | `ko-KR-Neural2-A` | **−1.0** | 1.0 | 서늘한 분석·예측 — characters.md 등록치 기반. S3·S4 2구 |

본화 대사 5구(내레이션 2 + 무결 1 + 설화 2) + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션 사후 믹싱. 발화 구 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S6·S7·S8(무대사) 렌더 전면 무음.

### 9-2. 동일 보이스 ID 2중 배역 차단 (§0-13 재가동 — 발동)

**내레이션·무결이 모두 `ko-KR-Wavenet-C`**이며 한 화에 공존 — EP38(내레이션·무결·뱃사공 3중)·EP41(나인·중전 2중) 선례의 4중 장치 적용:
1. 2배역 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지).
2. 파일명 분리: `EP64_S1_NARRATION`·`EP64_S5_NARRATION` / `EP64_S2_MUGYEOL` / `EP64_S3_SEOLHWA`·`EP64_S4_SEOLHWA`.
3. **피치 사다리 매 행 강제 표기**: 내레이션 `Pitch 0.0` > 무결 `Pitch −1.0` — 차 1.0(내레이션이 상부, 무결이 하부). 사다리 이탈 시 재합성.
4. 믹싱 단계에서 Pitch·톤 축 실측 확인.

설화 `ko-KR-Neural2-A`는 타 계열 ID — 2중 배역 충돌 없음.

### 9-3. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,500 --> 00:00:06,000
흑영대의 깃발에도 — 도장이 찍혀 있었다.

2
00:00:10,000 --> 00:00:15,000
십 년 전에 세워진 어전 직속의 암살단이오. 왕의 명이 아니라 — 왕의 눈을 피하기 위하여 왕의 이름으로 세워진 자들. 지금 그 깃발을 쥔 것은 — 중궁전이오.

3
00:00:17,500 --> 00:00:22,000
그들은 윤경헌을 구한 것이 아니라 — 그의 입을 다시 열리게 한 것이지요. 윤경헌은 십 년 전 계약서를 아는 — 유일한 산 증인이나이다.

4
00:00:24,500 --> 00:00:29,000
중전 마마는 숙부를 살려서 쓰실 것이오. 그러고 나서 — 그 숙부를 죽이실 것이오. 순서가 그렇게 되어 있나이다.

5
00:00:32,000 --> 00:00:35,500
그 순서의 끝자락에 백일홍이 서기로 한 것 — 그것이 이번 겨울의 진짜 내기였다.

6
00:00:58,800 --> 00:00:59,800
제65화 「남하하는 격문」에서 계속
```

- 시작 시각은 정본 rel 수치(3.5→2.5 / 6.5→10.0 / 5.5→17.5 / 5.5→24.5 / 4.5→32.0)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S6·S7·S8은 무대사(정본 지문 「무대사」 그대로) — 음성 블록 없음.
- 6번 자막(58.8~59.8)은 암전 이후 삽입 — S8 렌더는 완전 암전으로 끝난다.

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP64_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP64_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep64_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원, 워크스페이스 루트에서 실행. 무인자 실행 = dry-run, 세이프 어휘 validate() 내장) |
| 검수 기록 | `projects/sageuk-revenge/EP64_QC_CHECKLIST.md` |
| 정정 전 원본 보존 | `downloads/qc_ep64/ORIG_S08_before_edit.jpg`(한자형 낙관)·`ORIG_S04_before_edit.jpg`(꽃 장식+두루마리 낙서)·`ORIG_S05_before_edit.jpg`(원경 등불) + `EDIT_S04_v1.jpg`(1차 정정 — 등불 재유입 중간본) + 의심부 확대 크롭 검독 파일(`Z_*`) |
