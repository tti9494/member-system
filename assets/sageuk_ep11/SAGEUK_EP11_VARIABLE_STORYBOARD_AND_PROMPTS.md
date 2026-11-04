# 「혈화의 궐」 EP11 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제11화 「상궁의 발탁」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP10 원장 운용 결과
> **범위**: EP11 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 서 상궁의 발탁 — 시향(試香) 라인 진입극이다. **상궁의 다정한 은인 연기 및 칭찬·격려 슬롭 전면 금지** — 발탁은 시험이지 은혜가 아니며, 상궁의 대사는 전부 차가운 시험과 단문 지시다("잘하겠구나"류 격려 슬롭 0건). **은수저 변색 검증 고증**: 은이 독과 반응해 변색되는 실제 궁중 시원 검증 관례에 기반한다 — 환상적 발광·마법 연출 일체 금지, 금속의 밝음과 변색만이 정보다. **동일 보이스 ID 이중 배역**(서 상궁·중전 모두 `Neural2-B`) — 트랙 분리 합성과 파일명 규칙(`EP11_S2_SANGGUNG` / `EP11_S5_JUNGJEON`)으로 혼동 차단(정본 AG 검수 ⑦). 중전의 위협은 **시선 한 번**뿐이다 — 정지·난폭함·접촉 일체 없음.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **물레·증기**(spinning wheel momentum, steam curling off brass trays), S02 **촛불·손**(candle flicker, hand weight), S03 **은수저·열**(heat-haze shimmer, ember glow on metal), S04 **아침 증기·향**(steam in lattice light, incense thread), S05 **행렬·소매**(procession movement, sleeve fabric settling, lattice shadows), S06 **절의 정적**(fabric fold, held breath), S07 **등불·금속**(lamp glow on silver), S08 **소등·암전**(flames doused with real fluid weight, smoke thread, fade). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·상해·직접 대치 일체 없음. 본 화는 무흉기 화다 — 식사 검증과 예절 동작만 존재한다. **은인 슬롭 차단**: 상궁과 설화의 관계는 시험자-피시험자 계위 관계다 — 전 썬 `no warmth, no smiles, no encouragement, formal hierarchy held`를 명시하고 로맨스·모녀 오독을 차단한다. 중전의 경고는 시선뿐 — 정지·붙잡기·접촉 금지.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07·EP09·EP10 재발 방지: 설화 앵커에 **귀걸이·수술·가체·떨잠 금지를 전 썬 상향 고정**, `smooth jade rod with no carved head` 유지. EP10 관찰 메모 반영: 소품 무문자 지문을 패널 서술 안에서도 반복 기입.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **서 상궁**: a cold, restrained, dignified middle-aged senior court lady (Seo Sanggung), neat navy dangui overcoat, proper formal gache with a simple formal hairpin, severe scrutinizing eyes — never smiling warmly, no kind expression, no softness
   - **중전**(S05·S06 배경): a regal 22-year-old Joseon queen, extravagant crimson ceremonial dangui, tall elaborate gache with ornate tteoljam and cheopji hairpins, haughty chilling eyes — the elaborate ornament belongs to the Queen only, never to the others
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제12화 「쥐새끼의 반격」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 화덕 소등 → 서서히 어두워지는 암전까지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: S01~S03은 **수라간 야간 화덕 썬**이다. 키 라이트 모티베이션 필수 — S01 `low hearth fires and one hanging lamp only`, S02 `one candle in the antechamber`, S03 `the low hearth flame under the spoon`, S04 `cool morning lattice light, no lamps`, S05 `bright midday sun through the lattice, hard shadow rhythm`, S06 `the same midday corridor light`, S07 `warm lamplight in the antechamber`, S08 `hearth fires being doused, then darkness`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수 + EP10 관찰 메모 반영)**: 식단지·시향 기록지·권문 등 모든 소품 문서는 `blank paper texture, no letters, no glyphs, no readable marks` — **패널 서술 안에서도 반복 기입**한다(EP10 1차 렌더 결함 재발 방지). EP11은 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **복식 고증**: 서 상궁은 남색 당의+단정한 가체, 중전은 붉은 당의+화려한 가체(떨잠·첩지)로 **시각적으로 완전 분리**한다(동일 보이스 ID 이중 배역과 대응하는 시각 구분 — 화면 혼동 차단). 설화의 옥비녀는 전 썬 수술 없는 매끈한 단일 옥대. 상궁·중전 착장 교차 금지.

---

## 1. S01 왕의 밥상 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP11_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 수라간 원형 트래킹 — 수라간의 밤, 물레 소리. [무거운 나레이션 · 내레이션/Wavenet-C] "왕의 밥상에는, 언제나 목이 하나 늘어 있었다." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. Kitchen maids in plain neat court dress with plain hair. No king on screen, no royal figure in this scene. No violence, no weapon.

HEARTH LIGHT GUARD — IMPORTANT: the royal kitchen at night is lit ONLY by low hearth fires and one hanging lamp. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium-wide, slow circular tracking around the room: a vast Joseon royal kitchen at night, low glowing hearth fires, kitchen maids at long tables preparing the king's covered meal trays, a spinning wheel turning in the corner, steam curling off the brass dishes.
2. 85mm close, static: the young woman among the workers, her cold intelligent eyes reading the trays, her face giving nothing away.
3. 50mm insert, static: the royal meal tray with covered brass dishes, steam curling upward, a blank paper card beside it — blank paper texture, no letters, no glyphs, no readable marks anywhere.

WHEEL AND STEAM MOTION — IMPORTANT: physically-based spinning wheel turning with real spindle momentum, steam curling off the warm brass, hearth flames breathing and bending, her stillness with real body weight. Do NOT follow the sketch's static lines — the routine of the kitchen must feel like real filmed footage. No horror staging, no ghost cues — the routine itself is the menace.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 발탁 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP11_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 서 상궁이 설화의 손을 들여다봄. [차갑고 절제된 중년 · 서 상궁/Neural2-B] "손이 눈보다 빠르구나. 시향으로 옮겨라. 내일부터." (rel 3.5=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the senior court lady is a cold, restrained, dignified middle-aged senior court lady, neat navy dangui overcoat, proper formal gache with a simple formal hairpin, severe scrutinizing eyes — never smiling warmly, no kind expression. The young court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. Two plain maids far back by the wall, unremarkable faces. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: one candle lights the antechamber. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is an examination, not a kindness: no warmth, no smiles, no encouragement, formal hierarchy held — the senior lady issues orders, never praise.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the candlelit antechamber, the senior court lady seated with formal upright posture, the young woman kneeling before her, two plain maids far back by the wall.
2. 85mm, slow push-in: the senior lady lifting and examining the young woman's hands like an appraiser.
3. 100mm macro insert, static: the open palm and steady fingers, candlelight on the skin.
4. 85mm close, static: the senior lady's face delivering a cold verdict, absolutely no warmth.

CANDLE AND HAND MOTION — IMPORTANT: physically-based candle flicker, the hand lifted with real weight, the kneeling woman's stillness, the senior lady's unhurried appraising grip. Do NOT follow the sketch's static lines — the selection must feel like real filmed footage. No gentle smile, no nod of approval — the promotion is a test, and the only award is a colder duty.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 은수저의 검증 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP11_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 은수저가 불에 달아오르는 검증 절차. [차갑고 절제된 중년 · 서 상궁/Neural2-B] "여기서 죽는 나인은 이름이 없다. 기억하고." (rel 3.0=절대 16.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the senior court lady is a cold, restrained, dignified middle-aged senior court lady, neat navy dangui overcoat, proper formal gache with a simple formal hairpin, severe scrutinizing eyes — never smiling warmly. The young court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. No violence, no weapon.

HEARTH LIGHT GUARD — IMPORTANT: the low hearth flame under the spoon is the key light, with darkness folded around the table. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The silver test is a real, historically grounded procedure — bright clean silver must stay untarnished; tarnish means poison. No magic glow, no fantasy effects — the metal's brightness is the only information.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: the silver tasting spoon held over the low hearth flame, heat-haze shimmer bending the light around the metal.
2. 100mm macro, static: the senior lady's fingers turning the spoon in the flame, ember glow crawling across the silver.
3. 85mm close, static: her face over the spoon, strict eyes reading the metal's surface.
4. 50mm, static: across the table the young woman watches the whole procedure, understanding the lesson aimed at her.

FLAME AND METAL MOTION — IMPORTANT: physically-based heat-haze shimmer, the flame breathing around the spoon, the ember glow travelling on real metal as it turns, her unhurried precise grip. Do NOT follow the sketch's static lines — the procedure must feel like real filmed footage. No dramatic speeches staging — the work is the dialogue.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 첫 시향 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP11_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 시향 자리 — 첫 시향, 손이 떨리지 않음. [얼음장 결의 · 설화/Neural2-A] "이 몸은 이미 죽은 몸이오니, 죽음은 새것이 아니나이다." (rel 4.0=절대 24.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. The senior court lady is a cold, restrained, dignified middle-aged senior court lady, neat navy dangui overcoat, proper formal gache with a simple formal hairpin, severe scrutinizing eyes — never smiling warmly. No violence, no weapon.

MORNING LIGHT GUARD — IMPORTANT: cool morning light through the lattice windows only, no lamps. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Her resolve reads as stillness, not as tears.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the formal tasting table in cool lattice morning light, the young woman seated before the royal tray, the senior court lady standing over her like a magistrate.
2. 85mm close, static: her hands lifting the tasting spoon — perfectly steady, not a tremor.
3. 85mm close, static: her face, eyes lowered, ice resolve, no fear and no pride.

STEAM AND STILLNESS MOTION — IMPORTANT: physically-based steam drifting through the lattice light, a thin incense thread rising, her breath measured once and held, the spoon moving with calm real weight. Do NOT follow the sketch's static lines — the first tasting must feel like real filmed footage. No trembling close-up, no swallowed gasp — a body that is already dead has nothing to lose.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 중전의 시선 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP11_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 회랑 — 회랑에서 지나치던 중전, 시선만 주고감. [서늘한 경고 · 중전/Neural2-B] "상궁의 사람이 되면 — 상궁의 죽음도 함께인 것을." (rel 3.0=절대 32.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the Queen is a regal 22-year-old Joseon queen, extravagant crimson ceremonial dangui, tall elaborate gache with ornate tteoljam and cheopji hairpins, haughty chilling eyes — the elaborate ornament belongs to the Queen only. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. Servants in plain neat court dress bowing at the corridor edges. No violence, no weapon.

MIDDAY LIGHT GUARD — IMPORTANT: bright midday sun through the lattice, hard rhythmic shadows across the wooden corridor floor. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The Queen's warning is one glance while passing — no stopping, no words staged as shouting, no physical contact, no scene.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, static: the long sunlit palace corridor, the royal procession passing, servants clearing the way with deep bows.
2. 85mm close, static: the Queen's face turning a fraction — one cold haughty glance landing on the young woman, a chilling faint smirk.
3. 50mm, static: the young woman bowing low at the corridor edge, eyes down, hands folded.
4. 85mm, static: the procession already gone ahead, the young woman still bowed in the empty corridor.

PROCESSION AND SLEEVE MOTION — IMPORTANT: physically-based procession movement, sleeve fabric settling with real weight, lattice shadows sliding over the bowing figure, the Queen's glance a single unhurried beat. Do NOT follow the sketch's static lines — the passing threat must feel like real filmed footage. No shove, no grabbed chin, no raised hand — power spends one look, not one gesture.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 더 깊은 절 (절대 37.5~45.0 · 콘티 3컷 · 무대사)

- **시트**: `downloads/EP11_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 설화, 절만 깊이 함 — 대답하지 않음. 무대사 — 건축과 자세만이 숨을 죽인다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. No other face close to camera — the departed procession stays far and blurred. No violence, no weapon.

MIDDAY LIGHT GUARD — IMPORTANT: the same midday corridor light, hard lattice shadow rhythm. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a no-dialogue scene — architecture and posture carry the beat, and the bow is deeper than etiquette by exactly one degree.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the young woman bowing deeper at the corridor edge, face composed, saying nothing, the departing procession blurred far ahead.
2. 100mm macro insert, static: her folded hands and lowered eyes, her breath held still.
3. 35mm wide, slow pull-back: a tiny bowed figure alone under the vast repeating pillars of the empty corridor.

FABRIC AND BREATH MOTION — IMPORTANT: physically-based fabric folding over the deep bow, one measured breath held and released, the slow pull-back with steady real parallax. Do NOT follow the sketch's static lines — the held silence must feel like real filmed footage. No tears, no trembling, no musical swelling — the silence is the answer.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 재검사 — 합격 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP11_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 손 인서트 — 상궁이 설화의 시향 은수저를 다시 검사 — 통과. [차갑고 절제된 중년 · 서 상궁/Neural2-B] "…합격이다." (rel 2.5=절대 47.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the senior court lady is a cold, restrained, dignified middle-aged senior court lady, neat navy dangui overcoat, proper formal gache with a simple formal hairpin, severe scrutinizing eyes — never smiling warmly. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. No violence, no weapon.

LAMPLIGHT GUARD — IMPORTANT: warm lamplight in the antechamber is the only key light. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The praise never comes — the absence of failure is the only award. Re-examination is the senior lady's discipline, not doubt.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro hand insert, static: the senior lady's fingers picking up and re-examining the silver tasting spoon from the tray, lamp glow sliding on the metal.
2. 85mm close, static: her face in lamplight, strict eyes giving away exactly one millimeter of verdict.
3. 50mm, static: she turns away already, done with her, the young woman still formally bowed.

METAL AND FABRIC MOTION — IMPORTANT: physically-based lamp glow travelling across real silver as it turns, her fingers precise and unhurried, her robe settling as she turns away. Do NOT follow the sketch's static lines — the verdict must feel like real filmed footage. No smile, no approving nod beyond the single breath — passed, not praised.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 소등 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP11_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 수라간 불이 꺼짐 → 암전. **붉은 타이틀(제12화 「쥐새끼의 반격」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — figures in shadow and objects only, no visible face close to camera. No violence, no weapon.

DYING LIGHT GUARD — IMPORTANT: the hearth fires are being doused and darkness gathers. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no farewell gesture.

Recreate the panels in order as one continuous ~10 second sequence:
1. 50mm, static: the royal kitchen at night, maids dousing the hearth fires, darkness gathering under the beams, one young figure leaving through the far door.
2. 50mm, slow push-in: the last hearth flame dying down to a red coal, a thin smoke thread rising.
3. The frame slowly dims — the ember glow thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

FLAME AND SMOKE MOTION — IMPORTANT: physically-based flames doused with real fluid weight, the water hissing invisibly, the last coal dimming, the smoke thread rising after the flame dies, the ambient light dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the day ending at the king's table must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 3컷 | EP11_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 50mm 원형 트래킹 · 물레·증기 · 왕 미등장 |
| S02 | 07.5~15.0 | 4컷 | EP11_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 투숏 · 발탁=시험 · 은인 슬롭 0 |
| S03 | 15.0~22.5 | 4컷 | EP11_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 100mm 매크로 · 은수저 변색 검증 고증 · 환상 연출 금지 |
| S04 | 22.5~30.0 | 3컷 | EP11_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 35mm 첫 시향 · 손이 떨리지 않음 · 아침 격자광 |
| S05 | 30.0~37.5 | 4컷 | EP11_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 24mm 회랑 · 중전 시선 한 번 · 접촉·정지 0 |
| S06 | 37.5~45.0 | 3컷 | EP11_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 절 · 무대사 · 건축과 자세만 |
| S07 | 45.0~52.5 | 3컷 | EP11_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 손 인서트 · 재검사 통과 · 칭찬 0 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP11_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 소등·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤) | rel 3.0 | 절대 2.0 | 왕의 밥상에는, 언제나 목이 하나 늘어 있었다. |
| 2 | S02 | 서 상궁 `ko-KR-Neural2-B` (차갑고 절제된 중년, Pitch -0.5, Speed 0.95) | rel 3.5 | 절대 9.5 | 손이 눈보다 빠르구나. 시향으로 옮겨라. 내일부터. |
| 3 | S03 | 서 상궁 `ko-KR-Neural2-B` (차갑고 절제된 중년, Pitch -0.5, Speed 0.95) | rel 3.0 | 절대 16.5 | 여기서 죽는 나인은 이름이 없다. 기억하고. |
| 4 | S04 | 설화 `ko-KR-Neural2-A` (얼음장 결의, Pitch -1.0) | rel 4.0 | 절대 24.5 | 이 몸은 이미 죽은 몸이오니, 죽음은 새것이 아니나이다. |
| 5 | S05 | 중전 `ko-KR-Neural2-B` (서늘한 경고, Pitch 0.0, Speed 0.95) | rel 3.0 | 절대 32.0 | 상궁의 사람이 되면 — 상궁의 죽음도 함께인 것을. |
| 6 | S07 | 서 상궁 `ko-KR-Neural2-B` (차갑고 절제된 중년, Pitch -0.5, Speed 0.95) | rel 2.5 | 절대 47.5 | …합격이다. |
| 7 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제12화 「쥐새끼의 반격」에서 계속 |

- S06은 무대사 썬 — 보이스·자막 블록 없음. 자막 공백(00:37~00:47)은 정본 무대사 연출 그대로 둔다(침묵이 절의 깊이를 말한다).
- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: 서 상궁과 중전은 **동일 축 `ko-KR-Neural2-B`**를 쓴다. 혼동 차단 4중 장치를 강제한다 — ① 서 상궁·중전 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 상궁 `EP11_S2_SANGGUNG`·`EP11_S3_SANGGUNG`·`EP11_S7_SANGGUNG`, 중전 `EP11_S5_JUNGJEON`, ③ 서 상궁 전 대사에 `차갑고 절제된 중년(Pitch -0.5)` 지문을 **매 행 강제 표기**(본 표 2·3·6번 행), ④ 믹싱 단계에서 Pitch 축 확인(상궁 -0.5 / 중전 0.0). 이는 구본에서 동일 ID 구분 실패 사례가 있었던 화다 — 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 서 상궁 `Neural2-B`(Pitch -0.5, Speed 0.95), 중전 `Neural2-B`(Pitch 0.0, Speed 0.95), 내레이션 `Wavenet-C`(다큐 톤).
- S04 설화 대사는 속마음 결의 — 믹싱 시 톤 지문(얼음장 결의)을 우선한다.
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(마스터 각본 제11화 썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,500
왕의 밥상에는,
언제나 목이 하나 늘어 있었다.

2
00:00:09,500 --> 00:00:12,500
손이 눈보다 빠르구나.
시향으로 옮겨라. 내일부터.

3
00:00:16,500 --> 00:00:18,500
여기서 죽는 나인은
이름이 없다. 기억하고.

4
00:00:24,500 --> 00:00:27,500
이 몸은 이미 죽은 몸이오니,
죽음은 새것이 아니나이다.

5
00:00:32,000 --> 00:00:34,500
상궁의 사람이 되면 —
상궁의 죽음도 함께인 것을.

6
00:00:47,500 --> 00:00:49,000
…합격이다.

7
00:00:59,000 --> 00:01:00,000
제12화 「쥐새끼의 반격」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 7번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S06 자막 공백(00:37~00:47)은 정본 무대사 썬 — 회랑 정적은 믹싱 앰비언스(물레 소리의 잔향)로만 처리한다.
- 5번 블록(중전)과 2·3·6번 블록(서 상궁)은 동일 ID 이중 배역 — 자막 파일도 규칙에 따라 분리 저장한다(§10-1 ②).
- 보이스 ID 운용: 고정 ID + 감정 톤 지문(무거운 나레이션/차갑고 절제된 중년/얼음장 결의/서늘한 경고)으로 썬별 미묘함을 구분한다.
