# 「혈화의 궐」 EP09 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제9화 「밤의 침입자」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP08 원장 운용 결과
> **범위**: EP09 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 밤 침소 신원 시험극이다. 침입자 = 자객이 아니라 왕의 시험이며, 진짜 자객 그림자는 **왕의 방문에 편승한 기회 침입**으로 재정의한다(구 009본의 편의적 타이밍 해소). 렌더에 흉기 가동·상해·직접 대치 일체 없음 — 진짜 침입자는 처마 그림자와 발소리로만 존재하고, 무결의 수습은 프레임 밖에서 끝난다. 왕의 신원은 S06까지 얼굴을 완전히 비추지 않는다(S01~S05 실루엣·부분광, S06 반광). 침소 장면 전체가 **로맨스 오독 금지** — 두 인물은 항상 격식 거리를 유지한다.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **문틈 달빛·먼지**(dust drifting in the moonlight strip, shadow edge creeping), S02 **달빛 격자·소매**(lattice shadows breathing on the wall, sleeve fabric settling), S03 **눈 매크로**(micro eye motion, focus breathing, unbroken stillness), S04 **기왓장·천**(tile shadow easing, cloth sliver motion), S05 **회랑 그림자**(shadow gliding along the ridge, column shadows holding), S06 **달빛 격자·소매**(moonlight bars on the floor, sleeve settling), S07 **옥비녀·손**(jade glint moving with her hand, finger flex), S08 **퇴장·암전**(door sliding shut, paper fold crispness, light dying smoothly). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·상해·직접 대치 일체 없음. 진짜 침입자는 처마 위 그림자·발소리로만 존재하고(S04), 무결의 수습은 등장자 간 접촉 없이 프레임 밖 처리다(S05 — 무기 미인출, 얼굴 반광만). 침소 두 인물은 신원 시험극 연기 — **침소 로맨스 오독 차단**: `no intimacy, no touching, formal distance held`를 전 썬에 명시한다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07 결함 재발 방지: 설화 앵커에 **귀걸이·수술·가체·입가리개 금지를 전 썬 상향 고정**했다.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok
   - **왕 이환**: a handsome 24-year-old Joseon young king, royal red dragon robe (gollyongpo) with gold embroidered dragon emblem, gold royal winged hat (ikseongwan), composed cold regal charisma, melancholy determined eyes — in S01~S05 rendered as a dim silhouette or partial light only, face never fully revealed until S06
   - **강무결**(S05): a 25-year-old Joseon warrior captain, tall, dark navy and black military robe (yungbok), a faint scar across the cheekbone, sharp heavy calm eyes — no weapon drawn, no violence
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제10화 「옥사의 그림자」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 왕의 퇴장 → 남겨진 물체 → 서서히 어두워지는 암전까지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수 — 침소 야간 안티슬롭 핵심)**: 전 썬 야간 썬이다. 키 라이트 모티베이션 필수 — S01 `cold moonlight strip under the door threshold, no lamp`, S02 `lattice moonlight grids only, no lamp — a lampless darkness`, S03 `thin moonlight crescents in the eyes only`, S04 `moonlit eaves beyond the lattice window`, S05 `cold moonlight on the corridor and eave ridge`, S06 `moonlight bars between the two figures, one faint distant lamp glow beyond the door`, S07 `a single line of moonlight on the jade hairpin`, S08 `moonlit corridor through the open door, then the light dying`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: S08 왕이 남기고 간 접은 물체는 `crisp folded silhouette, unreadable, no characters, no glyphs, no readable marks` — 렌더에서 한글·한자를 만들지 않고 편집 자막으로만 처리한다(한글 왜곡 슬롭 근원 차단).
12. **복식 고증**: 왕은 붉은 곤룡포(금용단)·익선관 규격을 벗어나지 않고, 무결은 남색 융복·뺨 흉터로 통일한다. 관복·군복의 과장 금지.

---

## 1. S01 문틈의 그림자 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP09_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 문틈 로우앵글 — 침소 바닥, 문지방 아래로 그림자가 들어옴. 침입은 소리가 아니라 빛의 침이다. [얼어붙은 긴장 · 설화/Neural2-A] "누구신가." (rel 2.5=절대 1.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. The visitor is only a shadow and never identified — no face, no weapon. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: the chamber is lit ONLY by a cold strip of moonlight under the door threshold and faint lattice moonlight on the wall. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a test of identity, not a romance: no intimacy, formal distance held.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm low-angle, static, at floor level: inside a dark royal bedchamber, the wooden door slightly ajar, a narrow strip of cold moonlight under the threshold, and the dark shadow of standing feet sliding silently into the light gap.
2. 100mm macro insert, static: the strip of moonlight on dark floorboards, the edge of the shadow creeping deeper across the light, dust motes drifting in the beam.
3. 85mm close, static: the court lady awake in darkness, half her face lit by faint moonlight, eyes open, utterly still, the plain jade rod in her bun catching one thin glint.
4. 35mm wide, static: the dark chamber from beside the door, the court lady sitting up against the lattice-moonlight wall, the standing shadow at the door, formal distance held between them.

MOONLIGHT AND DUST MOTION — IMPORTANT: physically-based dust drifting through the moonlight strip, the shadow edge creeping with real weight, lattice shadows breathing faintly on the wall, her breath held once and released. Do NOT follow the sketch's static lines — the silent arrival must feel like real filmed footage. No jump scare, no sting — the shadow is quiet.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 어둠 속 목소리 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP09_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 등불 없는 어둠 속 목소리. 왕은 얼굴을 드러내지 않는다 — 실루엣과 익선관 날갯쇼 광택만. [검사하는 무게 · 이환/Neural2-C] "나인 홍화. 무엇을 두려워하는고." (rel 2.5=절대 8.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king is a handsome 24-year-old Joseon young king in a royal red dragon robe with gold embroidered dragon emblem and a gold winged royal hat, but in this scene he is rendered ONLY as a rim-lit silhouette with his face in shadow — never fully revealed. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: a lampless darkness. The chamber is lit ONLY by cold lattice moonlight grids on the wall and floor. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a test of identity, not a romance: no intimacy, no touching, formal distance held.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the tall standing figure of the king inside the dark bedchamber, a rim-lit silhouette against faint lattice moonlight, the deep dragon-robe reading as darkness with one dim glint of the gold winged hat, his face hidden.
2. 100mm macro insert, static: the king's hand resting motionless at his side, the layered dragon-robe sleeve hanging perfectly still, darkness folded around it.
3. 85mm close, static: the court lady bowing low from her seat, composed and unhurried, pale porcelain skin, cold intelligent eyes lowered, the plain jade rod in her plain bun, bare ears.

LATTICE SHADOW AND FABRIC MOTION — IMPORTANT: physically-based lattice shadows breathing faintly on the wall, the sleeve settling with real fabric weight, her controlled breath in the stillness. Do NOT follow the sketch's static lines — the measured pressure must feel like real filmed footage. No threat staging, no looming — the voice alone carries the weight.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 초를 세는 눈 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP09_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 눈 인서트 — 어둠 속 왕의 눈, 초를 세는 눈. 거짓은 표정이 아니라 타이밍으로 완성된다. [완벽한 거짓 · 설화/Neural2-A] "어둠은 두렵지 않나이다. 어둠이 밝혀지는 것이 두렵지요." (rel 4.0=절대 17.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king's eye belongs to a handsome 24-year-old Joseon young king in a red dragon robe and gold winged royal hat, but only his eye and the faint crown edge are ever seen. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: the only light is thin cold moonlight — a crescent in each eye, moonlight bars on the floor. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a test of identity, not a romance: no intimacy, formal distance held.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: the king's eye in darkness, a thin crescent of moonlight in the iris, unblinking and patient, the faint edge of the gold winged hat above.
2. 100mm extreme macro, static: the court lady's eye, calm and level, the lattice moonlight reflected small and bright in her iris, no flinch.
3. 85mm, static: two profile silhouettes facing each other across the dark chamber, the king standing, the court lady seated, formal distance held, moonlight bars falling between them.

EYE AND STILLNESS MOTION — IMPORTANT: physically-based micro eye motion — the iris contracting once, a slow unhurried blink from the king, her eyes holding steady, subtle focus breathing between the two faces. Do NOT follow the sketch's static lines — the timing duel must feel like real filmed footage. No widened eyes, no sweat, no gasp — the test is timing, not tension.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 처마 위 발소리 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP09_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 창밖 시선 — 창밖 처마, 진짜 침입자의 발소리가 눈에 그침. 왕과 설화가 동시에 듣는 소리. [무대사 — 무음 썬]
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king is a tall standing figure in a red dragon robe and gold winged royal hat, seen from behind or in silhouette only. The court lady is a 21-year-old Korean woman with a single plain undecorated jade hairpin, no tassels, no dangling ornaments, no earrings, no face veil, elegant dark pastel hanbok. The real intruder appears ONLY as a crouched shadow on the roof eaves — no face, no weapon, no attack. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: cold moonlight only — the lattice window glowing faintly from outside moonlight, the eaves rimmed in moonlight against the night sky. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is shared listening, not a romance: no intimacy, formal distance held.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm, static, from inside the dark chamber: the latticed window glowing faint grey with moonlight, the curved roof eave line visible beyond the lattice, the seated court lady and the standing king both facing the window, motionless.
2. 35mm, static: the moonlit palace roof eaves against the night sky with a bright moon, a faint crouched shadow breaking the clean ridge line of the tiles.
3. 100mm macro insert, static: a curved roof tile edge in moonlight, a sliver of dark cloth and the thin shadow of a hand easing silently over the tile.

TILE AND SHADOW MOTION — IMPORTANT: physically-based tile shadow easing across the ridge, the cloth sliver moving with real weight and care, lattice shadows breathing inside the chamber, the two listeners utterly still. Do NOT follow the sketch's static lines — the third presence must feel like real filmed footage. No attack, no sound cue staging — a footfall the whole scene hears.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 처마 위의 수습 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP09_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 회랑 — 무결이 처마 위 그림자를 조용히 수습. 칼은 나오지 않고, 한 문장으로 끝난다. 수습은 프레임 밖. [절제된 위협 · 무결/Wavenet-C] "돌아가라. 오늘 밤 이 자리는 네 무덤이다." (rel 3.0=절대 32.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior is a 25-year-old Joseon warrior captain, tall, in a dark navy and black military robe, a faint scar across the cheekbone, sharp heavy calm eyes — no weapon drawn, no weapon visible. The intruder is only a cloaked shadow on the eave ridge — no face, no weapon. The two never touch, never grapple. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: cold moonlight only on the long wooden corridor and the eave ridge. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The removal happens outside the frame: nothing is shown beyond the warrior's calm presence.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, static, deep-staged: a long moonlit palace wooden corridor with repeating columns, and above it the curved eave ridge where a small cloaked shadow moves along the ridge, tiny in the vast night frame.
2. 24mm ultra-wide, static: the same corridor, a second silhouette — the tall warrior in dark military robes — standing motionless as a pillar in the shadow of a column, waiting where the roof shadow must pass.
3. 85mm close, static: the warrior captain's face half-lit by cold moonlight, the faint scar on his cheekbone, level unhurried eyes, no weapon drawn.
4. 24mm ultra-wide, static: the eave ridge empty again under the moon, only clean tile shadows and moonlight, the corridor below also empty.

SHADOW AND CORRIDOR MOTION — IMPORTANT: physically-based shadow gliding along the ridge, column shadows holding steady, faint night haze drifting across the moonlight, the warrior's absolute stillness with real body weight. Do NOT follow the sketch's static lines — the quiet interception must feel like real filmed footage. No fight, no chase, no sound of struggle — danger handled like housekeeping.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 이미 아는 눈 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP09_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 침소로 돌아온 왕, 시험의 결과를 이미 알았다는 눈. 왕의 얼굴이 처음으로 반광으로 드러난다. [낮은 확신 · 이환/Neural2-C] "…그대는 궁녀가 아니다. 무엇이든 — 아직 말하지 마라." (rel 3.5=절대 39.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king is a handsome 24-year-old Joseon young king, royal red dragon robe (gollyongpo) with gold embroidered dragon emblem, gold royal winged hat (ikseongwan), composed cold regal charisma without triumph, melancholy determined eyes — his face now half-lit for the first time. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: cold moonlight bars falling between the two figures, one faint distant lamp glow beyond the doorway. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a verdict, not a romance: no intimacy, no touching, formal distance held.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot, static: the king standing in the dark bedchamber, red dragon robe and winged crown dim but readable, the court lady seated at a formal distance, cold moonlight bars falling between them.
2. 85mm close, static: the king's face in half-light, composed cold regal certainty, no triumph in it, the gold crown wings dim.
3. 100mm macro insert, static: the court lady's folded hands resting in her lap, knuckles quiet, sleeve edges perfectly aligned, the plain jade rod glinting at the edge of frame.

MOONLIGHT AND FABRIC MOTION — IMPORTANT: physically-based moonlight bars breathing as clouds pass, the dragon-robe sleeve settling with real weight, her hands staying perfectly still, one controlled breath. Do NOT follow the sketch's static lines — the quiet verdict must feel like real filmed footage. No anger, no triumph music staging — he speaks what he already decided.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 옥비녀 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP09_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 설화의 옥비녀, 품속으로 다시 감기는 손. 결의는 손끝에만 산다. [서늘한 결의 속마음 · 설화/Neural2-A] "이미 말할 때가 왔사옵니다." (rel 3.0=절대 47.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. No other person in this scene. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: the only light is a single line of cold moonlight — on the jade rod, on her knuckles, one lattice bar on her cheek. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Her resolve reads in the hands only — never tears, never wide eyes.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: the plain undecorated jade hairpin rod fastening her dark traditional bun, one thin line of moonlight running along the smooth jade.
2. 100mm macro insert, static: her hand smoothing the breast fold of her hanbok, folding something small and unseen back into the fabric, fingers deliberate and calm, moonlight on the knuckle edges.
3. 85mm close, static: her face in near-darkness, pale porcelain skin, cold intelligent dark eyes lifted with quiet resolve, bare ears, no jewelry, one faint lattice moonlight bar on her cheek.

JADE AND FINGER MOTION — IMPORTANT: physically-based jade glint moving with the smallest head motion, the finger flex folding the fabric with real weight, her breath settling into stillness, lattice shadows breathing faintly. Do NOT follow the sketch's static lines — the cold resolve must feel like real filmed footage. No tears, no dramatic music cue — a decision dressed as courtesy.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 남겨진 것 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP09_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드 — 왕이 소매에 무언가를 남기고 사라짐 → 암전. **붉은 타이틀(제10화 「옥사의 그림자」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king is a tall figure in a red dragon robe and gold winged royal hat seen from behind as he departs, his face never visible. No other person in frame. The folded object he leaves behind is a crisp folded silhouette, unreadable, no characters, no glyphs, no readable marks of any kind. No violence, no weapon.

NIGHT LIGHT GUARD — IMPORTANT: moonlight through the open doorway onto the corridor, then the light dying. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no farewell gesture beyond the departure itself.

Recreate the panels in order as one continuous ~10 second sequence:
1. 35mm, static: the king's silhouette stepping out through the chamber doorway into the moonlit corridor beyond, the red dragon robe a deep shape against the light, his back to the room.
2. 100mm macro insert, static: on the low wooden table in a bar of moonlight, a small folded object left behind where the king stood, its folds crisp and unreadable, darkness folded around it.
3. The frame slowly dims — the moonlight thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

DEPARTURE AND LIGHT MOTION — IMPORTANT: physically-based robe fabric swaying with his steps, the door's soft weight settling, dust drifting in the last moonlight bar, the light dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the unannounced departure must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP09_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 50mm 문틈 로우앵글 · 그림자=미확인 방문자 · 설화 기상(공포 연기 금지) |
| S02 | 07.5~15.0 | 3컷 | EP09_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 등불 없는 어둠 · 왕 실루엣(얼굴 은닉) · 소매 무동 |
| S03 | 15.0~22.5 | 3컷 | EP09_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 눈 매크로 2연 · 완벽한 거짓=타이밍 · 과장 표정 금지 |
| S04 | 22.5~30.0 | 3컷 | EP09_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 35mm 창밖 처마 · 진짜 침입자=그림자만 · 동시 청취 무대사 |
| S05 | 30.0~37.5 | 4컷 | EP09_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 24mm 회랑 · 무결 무기 미인출 · 수습은 프레임 밖 |
| S06 | 37.5~45.0 | 3컷 | EP09_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 투숏 · 왕 얼굴 최초 반광 · 판결=이미 결정된 것 |
| S07 | 45.0~52.5 | 3컷 | EP09_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 옥비녀 매크로 · 품속 수납 · 결의=손끝만 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP09_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 퇴장·잔물·암전 · 엔드카드·타이틀은 편집 삽입 · 무음 클리프행어 |

합계: 콘티 27컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 설화 `ko-KR-Neural2-A` (얼어붙은 긴장, Pitch -1.0) | rel 2.5 | 절대 1.5 | 누구신가. |
| 2 | S02 | 이환 `ko-KR-Neural2-C` (검사하는 무게, Pitch -0.5) | rel 2.5 | 절대 8.5 | 나인 홍화. 무엇을 두려워하는고. |
| 3 | S03 | 설화 `ko-KR-Neural2-A` (완벽한 거짓, Pitch -1.0) | rel 4.0 | 절대 17.0 | 어둠은 두렵지 않나이다. 어둠이 밝혀지는 것이 두렵지요. |
| 4 | S05 | 무결 `ko-KR-Wavenet-C` (절제된 위협, Pitch -1.5) | rel 3.0 | 절대 32.0 | 돌아가라. 오늘 밤 이 자리는 네 무덤이다. |
| 5 | S06 | 이환 `ko-KR-Neural2-C` (낮은 확신, Pitch -0.5) | rel 3.5 | 절대 39.5 | …그대는 궁녀가 아니다. 무엇이든 — 아직 말하지 마라. |
| 6 | S07 | 설화 `ko-KR-Neural2-A` (서늘한 결의 속마음, Pitch -1.0) | rel 3.0 | 절대 47.0 | 이미 말할 때가 왔사옵니다. |
| 7 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제10화 「옥사의 그림자」에서 계속 |

- S04는 무대사 썬 — 보이스·자막 블록 없음. 왕과 설화가 동시에 듣는 소리이므로 자막 공백(00:22~00:30)은 침묵 연출 그대로 둔다.
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 이환 `Neural2-C`(Pitch -0.5), 무결 `Wavenet-C`(Pitch -1.5). S07 설화 대사는 속마음 자막이므로 믹싱 시 톤 지문(서늘한 결의)을 우선한다.
- 정본 썬표의 rel·절대 환산(1번 환산식: 절대 = rel + 썬 시작 - 1.0)을 그대로 따랐다.

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:01,500 --> 00:00:03,000
누구신가.

2
00:00:08,500 --> 00:00:10,500
나인 홍화. 무엇을 두려워하는고.

3
00:00:17,000 --> 00:00:20,000
어둠은 두렵지 않나이다.
어둠이 밝혀지는 것이 두렵지요.

4
00:00:32,000 --> 00:00:34,500
돌아가라. 오늘 밤 이 자리는 네 무덤이다.

5
00:00:39,500 --> 00:00:42,500
…그대는 궁녀가 아니다.
무엇이든 — 아직 말하지 마라.

6
00:00:47,000 --> 00:00:49,000
이미 말할 때가 왔사옵니다.

7
00:00:59,000 --> 00:01:00,000
제10화 「옥사의 그림자」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 7번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S04 자막 공백(00:22~00:30)은 정본 무대사 썬 — 발소리는 믹싱 효과음으로만 처리한다.
- S03 3번 블록은 두 문장 한 행 대사 — 길이를 감안해 2행 분할 표기하며, 믹싱 시 실제 발화 길이에 맞춰 편집 단계에서 확정한다.
- 보이스 ID 운용: 왕·설화·무결 모두 주연 고정 ID — 감정 톤 지문(얼어붙은 긴장/검사하는 무게/완벽한 거짓/절제된 위협/낮은 확신/서늘한 결의)으로 썬별 미묘함을 구분한다.
