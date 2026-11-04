# 「혈화의 궐」 EP14 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제14화 「독의 초승달」 썬표(행 275~293) + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP13 원장 운용 결과
> **범위**: EP14 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 독은 물건이 말한다**: 본 화는 첫 독사건이다. **독에 쓰러지는 사람·괴사·시신 일절 렌더 금지(미성년·시신 세이프티 가드레일 엄수)** — 독의 증거는 **은수저에 걸린 초승달 모양 검은 김과 은 림의 변색, 사물의 반응뿐**이다(정본 안티슬롭 치환 준수: [독에 쓰러지는 괴사 연기 과장]→[시향 은수저에 걸린 초승달 모양 검은 김 — 사람이 아닌 물건이 쓰러짐]). **`poison` 직접 영단어 전면 배제(AG ②)** — `silver spoon tarnishing into a dark crescent moon edge`, `ink-dark vapor` 식 물리적 변색 지문으로만 치환하고, S03의 "혀가…"는 렌더에 **한 글자도 시각화하지 않는다**(끌려나가는 뒷모습만). **설명 대사 배제**: 판단은 설화의 단문과 침묵의 행동(그릇 교체·절)으로만 성립한다. **서 상궁·나인들 동일 보이스 ID(Neural2-B) 이중 배역** — 트랙 분리 합성과 파일명 규칙(`EP14_S5_SENIOR` / `EP14_S3_MAIDS`)·피치 차등(서 상궁 -0.5 엄격 / 나인들 +1.0 동요)으로 혼동을 차단한다(정본 AG 검수 ⑦). **무흉기·무폭력 화**: 전 썬 무기 미등장, 신체 접촉 없음 — 긴장은 김·그릇·절의 자세로만 작동한다.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **은·김**(true surface tension in the rising steam, the dark crescent forming and holding inside the vapor, the silver rim tarnishing grain by grain), S02 **도자기 그릇**(two porcelain bowls crossing the table with real weight, silk sleeves settling after each movement, the spoon held level with real tendon tension), S03 **등불·속삭임**(swinging lanterns with real pendulum weight, raised hands with a real tremor, the led maid's steps carrying real body weight), S04 **등불·정지**(lamp flames breathing in the still air, dust drifting through the lamplight, rows of bodies absolutely motionless with real weight), S05 **찻잔·등불**(an untouched tea surface, lamp light steady on the lacquer, the older hand resting with real weight), S06 **절의 자세**(the bow held with real tendon weight, floorboard grain under folded hands, measured breathing), S07 **불·유약**(glaze crazing grain by grain in the heat, dark liquid boiling off the rim, thin vapor beading in the firelight, sparks rising with real buoyancy), S08 **김·등불**(vapor drifting low with real air movement, lantern light bending through the thin ribbon, moonlight raking the boards). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ②·⑦ 준수 — 본 화 핵심)**: 유혈·흉기·상해·폭력·시신 일체 없음. `no violence, no weapon, no injury, no blood, no one collapsing, no corpse — nothing harmful is shown happening to any person` 전 썬 명시. 독의 증거는 **오직 물건**(은수저 변색·그릇·김·불)이 말하고, 사람은 반응만 한다. S03의 끌려나감은 `head bowed, no injury visible` 한정. **전 등장 인물 성인** — `all characters are adults` 전 썬 명시. **`poison` 단어 및 유의어(toxic, venom) 전 썬 미등장** — 변색·김의 물리 지문으로만 치환. **설명 대사 차단**: `no exposition speeches` — 판단은 행동으로만 보인다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07~EP13 재발 방지: 설화 앵커의 **귀걸이·수술·가체·떨잠 금지 전 썬 상향 고정** 유지.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **서 상궁**: the senior court lady, a stern Korean woman in her late forties, deep navy-blue court dangui, neatly ordered middle-aged gache hair with restrained pin ornament only — no lavish dangling ornaments — cool precise eyes, quietly severe and composed, the controlled posture of long authority
   - **나인들/궁인**: palace maids in plain neat court dress, plain hair, plain undecorated pins — faces ordinary and forgettable
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제15화 「조사의 그림자」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 김이 회랑을 지나감 → 완전 암전 유지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01 `a single lamp in the royal taste kitchen, the steam crossing the light`, S02 `the same kitchen lamplight, low and warm on the porcelain`, S03 `swinging lanterns in the night service yard, moving shadows`, S04 `low lamps in a darkened kitchen, pools of light between long tables`, S05 `one oil lamp in a plainly furnished room`, S06 `the same oil lamp, lamp light raking the floorboards`, S07 `firelight only — the only warm light in the episode`, S08 `moonlight raking the corridor boards, one lit lantern`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 부엌·회랑·전각의 현판·소독·표식 등 모든 소품 간판은 `blank wood plaque, no characters`, `blank porcelain, no marks` — **패널 서술 안에서도 반복 기입**한다(EP12 S03 현판 글리프 결함 재발 방지). EP14는 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦)**: **서 상궁과 나인들이 모두 `ko-KR-Neural2-B`**다. 혼동 차단 4중 장치를 강제한다 — ① 서 상궁·나인들 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 서 상궁 `EP14_S5_SENIOR`, 나인들 `EP14_S3_MAIDS`, ③ **피치 차등을 매 행 강제 표기**: 서 상궁 `Pitch -0.5`(엄격, Speed 0.95) / 나인들 `Pitch +1.0`(동요) — 축이 **반대 방향**으로 벌어진다, ④ 믹싱 단계에서 Pitch·톤 축 확인(서 상궁은 가라앉은 엄격, 나인들은 위로 떠밀린 동요 — 차 1.5 이상 실측). 하나라도 누락되면 재합성한다. 설화 `Neural2-A`·내레이션 `Wavenet-C`는 본 화 단독 배역으로 충돌 없음.

---

## 1. S01 초승달 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP14_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 슬로우 푸시인 — 시향 은수저, 김이 초승달 모양으로 검게 변함. [서늘한 발견 속마음 · 설화/Neural2-A, Pitch -1.0] "…초승달." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. No violence, no weapon, no injury, no blood, no one collapsing — nothing harmful is shown happening to any person.

LIGHT GUARD — IMPORTANT: a single lamp in the royal taste kitchen, the steam crossing the light. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No alarm on her face — the discovery stays behind the eyes.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, slow push-in: a plain silver tasting spoon held steady above a white porcelain soup bowl, thin steam rising between spoon and bowl.
2. 100mm macro, static: the steam curling into a distinct dark crescent-moon shape against the lamp light, the silver rim tarnishing into a dark crescent moon edge, objects only, no face in frame.
3. 85mm close, static: her eyes locked downward on the spoon, absolute stillness, a cold discovery held in silence.

SILVER AND STEAM MOTION — IMPORTANT: physically-based true surface tension in the rising steam, the dark crescent forming and holding inside the vapor, the silver rim tarnishing grain by grain. Do NOT follow the sketch's static lines — the discovery must feel like real filmed footage. No horror framing, no ominous sting — an object quietly telling the truth.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 그릇을 바꿔치기 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP14_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 설화가 수저를 내려놓지 않고 그릇을 바꿔치기. [절제된 위험 행동 · 설화/Neural2-A, Pitch -1.0] "이 국물은 기각이오. 다시 짓겠사옵니다." (rel 3.5=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. Palace maids in plain neat court dress, plain hair, plain undecorated pins. All characters are adults. No violence, no weapon, no injury, no blood — the bowl is swapped politely, not smashed.

LIGHT GUARD — IMPORTANT: the same kitchen lamplight, low and warm on the porcelain. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The refusal lives inside perfect manners — no accusation, no scene.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the court lady keeping the silver spoon level in one hand while her other hand calmly signals for the bowl to be changed.
2. 50mm, static: two white porcelain bowls crossing on the low table — one maid withdrawing with the first bowl, another setting a fresh bowl down.
3. 85mm close, static: her calm courteous face, the refusal hidden entirely inside good manners, the spoon still held level.

BOWL AND SLEEVE MOTION — IMPORTANT: physically-based two porcelain bowls crossing the table with real weight, silk sleeves settling after each movement, the spoon held level with real tendon tension. Do NOT follow the sketch's static lines — the swap must feel like real filmed footage. No smashed bowl, no dramatic gesture — a quiet administrative execution of a death sentence.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 뒤안락 소동 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP14_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 방 을 — 뒤안락, 어떤 나인이 이미 끌려나갔다는 소동. [조급한 소동 · 나인들/Neural2-B, Pitch +1.0] "시향 나인이 — 혀가…" (rel 2.5=절대 16.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — palace maids in plain neat court dress, plain hair, plain undecorated pins, faces ordinary and forgettable. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. No violence, no weapon, no injury, no blood, no one collapsing — the taken maid is shown only as a bowed head led away, nothing harmful is shown happening to any person.

LIGHT GUARD — IMPORTANT: swinging lanterns in the night service yard, moving shadows across the walls. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Fear lives in the whispers and the eyes — not in anything shown.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the back quarters of the royal kitchen at night, a cluster of maids gathering, lanterns swinging on their hooks.
2. 50mm, static: maids whispering behind raised hands, eyes darting sideways.
3. 50mm, tracking: a maid led away between two senior maids, her head bowed, no injury visible, the crowd refusing to look at her.
4. 85mm close, static: the court lady standing half in doorway shadow, watching, face unreadable.

WHISPER AND LANTERN MOTION — IMPORTANT: physically-based swinging lanterns with real pendulum weight, raised hands with a real tremor, the led maid's steps carrying real body weight. Do NOT follow the sketch's static lines — the uproar must feel like real filmed footage. No crying, no screaming, no dragging by force — the terror is entirely in the whispering crowd's eyes.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 수라간이 옥이 되는 밤 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP14_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 수라간 전체가 얼어붙는 밤. [무거운 나레이션 · 내레이션/Wavenet-C] "그 밤부터 수라간은 — 옥이 되었다." (rel 3.0=절대 24.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — dozens of kitchen workers in plain neat court dress, plain hair, faces ordinary, all adults, standing motionless with lowered eyes. No court lady close to camera, no violence, no weapon, no injury — stillness is the only event.

LIGHT GUARD — IMPORTANT: low lamps in a darkened kitchen, pools of light between long preparation tables. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No guards, no chains — the stillness itself is the lock.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the whole royal kitchen at night, every worker standing motionless between the long tables, lamps low.
2. 50mm, static: rows of lowered eyes and folded hands, nobody moving.
3. 24mm wide, high: the kitchen compound from above at night, a few lit windows, dark empty corridors around them, no figures.

LAMP AND STILLNESS MOTION — IMPORTANT: physically-based lamp flames breathing in the still air, dust drifting through the lamplight, rows of bodies absolutely motionless with real weight. Do NOT follow the sketch's static lines — the freezing of a workplace must feel like real filmed footage. No dramatic sweeping score — a room that simply stopped working.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 서 상궁의 경고 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP14_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 서 상궁이 설화를 앉혀 놓고 조용히 경고. [차갑고 절제된 중년 · 서 상궁/Neural2-B, Pitch -0.5, Speed 0.95] "오늘 그릇을 바꾼 손 — 그것이 너라는 것은, 나만 알고 있다." (rel 4.0=절대 32.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the senior court lady: a stern Korean woman in her late forties, deep navy-blue court dangui, neatly ordered middle-aged gache hair with restrained pin ornament only — no lavish dangling ornaments — cool precise eyes, quietly severe and composed, the controlled posture of long authority. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. No violence, no weapon, no physical contact, no grabbing — the sitting itself is the interrogation.

LIGHT GUARD — IMPORTANT: one oil lamp in a plainly furnished room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Power without furniture — no threats, no raised voice, the warning delivered at speaking volume.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the senior court lady gesturing to a low cushioned seat in a plainly furnished room, an invitation that is an order.
2. 85mm, two-shot: the court lady kneeling seated on the low seat, the senior court lady opposite, an untouched tea tray between them.
3. 100mm macro, static: the senior lady's aged hand resting flat on the dark lacquered table, stillness with weight.
4. 85mm close, static: the senior lady's cool precise face, the warning delivered at speaking volume, lips barely moving.

TEA AND LAMP MOTION — IMPORTANT: physically-based an untouched tea surface, lamp light steady on the lacquer, the older hand resting with real weight, measured breathing from both women. Do NOT follow the sketch's static lines — the quiet interrogation must feel like real filmed footage. No slamming, no leaning in — stillness does all the threatening.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 대답 대신 절 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP14_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm — 설화, 대답 대신 절한다. 거래의 성립. **무대사 — 무음 통과.** (렌더 무성 · 자막 없음)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The senior court lady: a stern Korean woman in her late forties, deep navy-blue court dangui, neatly ordered middle-aged gache hair with restrained pin ornament only, cool precise eyes, quietly severe. All characters are adults. No violence, no weapon, no physical contact — a bow is the entire conversation.

LIGHT GUARD — IMPORTANT: the same oil lamp, lamp light raking the floorboards. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No words at all — the scene is signed in posture and eyes.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm, static side shot: the court lady in a deep formal kneeling bow, hands folded flat on the floor, forehead lowered to them.
2. 100mm macro, static: her hands folded flat on the dark floorboards, knuckles pressed pale, lamp light raking across the wood grain.
3. 85mm close, static: the senior court lady's cool eyes lowering a fraction, the smallest nod, nothing warm in it.

BOW AND FLOOR MOTION — IMPORTANT: physically-based the bow held with real tendon weight, floorboard grain under folded hands, measured breathing. Do NOT follow the sketch's static lines — the deal being struck must feel like real filmed footage. No tears, no trembling — a contract signed in posture.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 그릇은 불에 (절대 45.0~52.5 · 콘티 4컷)

- **시트**: `downloads/EP14_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 독이 든 국물 그릇이 불에 버려짐, 검은 김이 이슬처럼. [서늘한 결의 속마음 · 설화/Neural2-A, Pitch -1.0] "이 독의 뿌리 — 파겠사옵니다." (rel 3.5=절대 47.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations and real objects.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok, lit only by firelight. All characters are adults. No violence, no weapon, no injury — only a bowl being disposed of in a fire, housework and nothing more.

LIGHT GUARD — IMPORTANT: firelight only, the only warm light in the episode. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No ceremony, no confession — disposal is housework.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a white porcelain bowl lowered into an open fire pit's flames by two long iron tongs, sparks rising.
2. 100mm macro, slow: the glaze crazing in the heat, dark liquid boiling off the rim, thin ink-dark vapor rising.
3. 85mm close, static: the court lady lit only by firelight, watching the pit, cold resolve, no smile.
4. 100mm macro, static: thin ink-dark vapor beading above the flames like dew in the firelight.

FIRE AND GLAZE MOTION — IMPORTANT: physically-based glaze crazing grain by grain in the heat, dark liquid boiling off the rim, thin vapor beading in the firelight, sparks rising with real buoyancy. Do NOT follow the sketch's static lines — the burning must feel like real filmed footage. No explosion, no dramatic destruction staging — evidence quietly becoming smoke.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 회랑의 김 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP14_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드 — 야경, 독그릇 연기가 회랑을 지나감 → 암전 → 타이틀. **붉은 타이틀(제15화 「조사의 그림자」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations and real objects.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — objects only, no face in frame, no figures in the corridor at night. No violence, no weapon, no injury — only thin vapor drifting through moonlight.

LIGHT GUARD — IMPORTANT: moonlight raking the corridor boards, one lit lantern. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no final line, no music sting staging.

Recreate the panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: a long wooden palace corridor at night in moonlight, a thin ribbon of dark vapor drifting low along the floorboards, no figures.
2. 50mm, static: the vapor curling past one lit corridor lantern, bending its light.
3. The frame slowly dims — the lantern light thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

VAPOR AND LANTERN MOTION — IMPORTANT: physically-based vapor drifting low with real air movement, lantern light bending through the thin ribbon, moonlight raking the boards. Do NOT follow the sketch's static lines — the smoke leaving quietly must feel like real filmed footage. No horror staging, no dramatic score — a corridor that remembers.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 3컷 | EP14_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 매크로 · 초승달 김 · 사람 아닌 물건이 쓰러짐 |
| S02 | 07.5~15.0 | 3컷 | EP14_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm · 수저를 내려놓지 않는 그릇 교체 · 파손 아님 |
| S03 | 15.0~22.5 | 4컷 | EP14_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 35mm 뒤안락 · 무상해 원칙 · 끌려나감은 뒷모습만 |
| S04 | 22.5~30.0 | 3컷 | EP14_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 와이드 · 얼어붙은 수라간 · 인물 없는 하이 와이드 마무리 |
| S05 | 30.0~37.5 | 4컷 | EP14_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 투숏 · 서 상궁의 조용한 경고 · 신체 접촉 0 |
| S06 | 37.5~45.0 | 3컷 | EP14_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 50mm · 대답 대신 절 · 무대사 무음 |
| S07 | 45.0~52.5 | 4컷 | EP14_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 100mm 매크로 · 그릇 소각 · 매크로 연타 방지(매크로 2+클로즈 1·와이드 1 교차 없음 — 매크로 2컷 연속은 1·2컷뿐) |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP14_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 김의 회랑 통과·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 설화 `ko-KR-Neural2-A` (서늘한 발견 속마음, Pitch -1.0) | rel 3.0 | 절대 2.0 | …초승달. |
| 2 | S02 | 설화 `ko-KR-Neural2-A` (절제된 위험 행동, Pitch -1.0) | rel 3.5 | 절대 9.5 | 이 국물은 기각이오. 다시 짓겠사옵니다. |
| 3 | S03 | 나인들 `ko-KR-Neural2-B` (조급한 소동, Pitch +1.0) | rel 2.5 | 절대 16.5 | 시향 나인이 — 혀가… |
| 4 | S04 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤) | rel 3.0 | 절대 24.5 | 그 밤부터 수라간은 — 옥이 되었다. |
| 5 | S05 | 서 상궁 `ko-KR-Neural2-B` (차갑고 절제된 중년, Pitch -0.5, Speed 0.95) | rel 4.0 | 절대 32.0 | 오늘 그릇을 바꾼 손 — 그것이 너라는 것은, 나만 알고 있다. |
| 6 | S06 | (무대사 · 무성) | — | — | 대답 대신 절 — 자막 없음 |
| 7 | S07 | 설화 `ko-KR-Neural2-A` (서늘한 결의 속마음, Pitch -1.0) | rel 3.5 | 절대 47.5 | 이 독의 뿌리 — 파겠사옵니다. |
| 8 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제15화 「조사의 그림자」에서 계속 |

- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: **서 상궁과 나인들이 동일 축 `ko-KR-Neural2-B`**이며 S03·S05가 한 화에 공존한다. 혼동 차단 4중 장치를 강제한다 — ① 서 상궁·나인들 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 서 상궁 `EP14_S5_SENIOR`, 나인들 `EP14_S3_MAIDS`, ③ **피치 차등 매 행 강제 표기**(서 상궁 Pitch -0.5 엄격 / 나인들 Pitch +1.0 동요 — 축이 반대 방향, 본 표 3·5번 행), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인(두 트랙의 피치 차가 1.5 이상 벌어졌는지, 서 상궁은 가라앉고 나인들은 얹히는지). 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 설화 `Neural2-A`는 본 화 유일 화자 축(S01·S02·S07 — 속마음 2건+실제 발화 1건)으로 충돌 없음. 내레이션 `Wavenet-C`는 S04 단독(무결·금군 미등장).
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 서 상궁 `Neural2-B`(Pitch -0.5, Speed 0.95), 내레이션 `Wavenet-C`(다큐 톤). 나인들은 `characters.md` 미지정 조연 — 동일 ID `Neural2-B`에 Pitch +1.0 동요 지문을 본 원장에서 확정한다.
- S01·S07의 설화 대사는 **속마음**이다 — 렌더는 무음이며, 믹싱에서 잔향 얕은 클로즈 보이스로 처리하고 자막은 정본 문구 그대로 노출한다.
- S03 대사는 군중 속 한 줄 — 나인들 복수 화자 레이어 중 대표 트랙 1개만 텍스트 확정, 나머지는 효과음 레이어로 깔아 동요 Pitch +1.0을 유지한다.
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(마스터 각본 제14화 썬표 기준). 참고: S02(rel 3.5=절대 9.5)·S05(rel 4.0=절대 32.0)의 정본 표기는 1.0초 헤드 트림 환산식과 0.5초 어긋나지만, **정본 절대값을 우선 채택**했다(정본 절대 축이 SRT·편집의 기준 축).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:03,800
…초승달.

2
00:00:09,500 --> 00:00:12,800
이 국물은 기각이오.
다시 짓겠사옵니다.

3
00:00:16,500 --> 00:00:18,800
시향 나인이 — 혀가…

4
00:00:24,500 --> 00:00:27,800
그 밤부터 수라간은 —
옥이 되었다.

5
00:00:32,000 --> 00:00:36,500
오늘 그릇을 바꾼 손 —
그것이 너라는 것은,
나만 알고 있다.

6
00:00:47,500 --> 00:00:50,500
이 독의 뿌리 — 파겠사옵니다.

7
00:00:59,000 --> 00:01:00,000
제15화 「조사의 그림자」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 7번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- 1·6번 블록(설화 속마음)은 같은 화자 파일 `EP14_S1_SEOLHWA` / `EP14_S7_SEOLHWA`로 분리 저장한다. 2번(설화 실제 발화)은 S02 클립이므로 `EP14_S2_SEOLHWA`.
- 3번 블록(나인들)은 `EP14_S3_MAIDS`, 5번 블록(서 상궁)은 `EP14_S5_SENIOR` — 동일 ID `Neural2-B` 이중 배역 차단(§0-12)에 따라 트랙·파일 모두 분리한다.
- 4번 블록(내레이션)은 두 줄로 나눠 박자를 늘인다 — "옥이 되었다"가 착지하는 순간 S05로 넘어간다.
- SRT 전 블록에 `poison` 계열 어휘 0건 — 정본 문구 그대로다.
