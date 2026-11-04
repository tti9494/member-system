# 「혈화의 궐」 EP18 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + 정본 EP18 「사헌부 멸문의 밀서」 8썬표(핸드오프 브리프 원전 서사 — 왕이 비밀 벽장의 비단함을 개봉, 윤경헌 수결 확인, 설화가 밀서를 수수) + `characters.md` 캐릭터 앵커 + EP17 원장 템플릿(100% 동일 규격)
> **범위**: EP18 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 증거 개봉의 밤**: 왕이 십 년을 숨겨온 비단함을 비밀 벽장에서 꺼내 개봉하고, 설화가 아버지 윤경헌의 수결을 확인한 뒤 밀서를 수수하는 핵심 증거 씬. **밀서 전문 낭독 폭로 배제** → 치환 [흘림 먹물 필치만 노출 — 판독 불가 필선]. **설화의 감정 폭발 배제** → 치환 [얼어붙은 시선과 왕이 보고도 모른 척하는 존중]. **복수 선언 대법으로의 응답** → ["그 목은 — 법으로 먼저 꺾어야 하옵니다" 법 집행 선언]. **비단함 개봉 매크로 왜곡 방지(정본 AG ①)** — 밀서 본문은 판독 불가 흘림 먹물 필선, 수결 인주는 기하학적 인주 낙형으로 묘사. **매크로 연타 방지(정본 AG ①)** — 씬당 매크로 1컷 한정 + 휴먼 스케일 교차.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 전면 차단 블록을 고정한다.
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **벽장·비단함**(aged silk cloth sagging with real cloth weight, the wooden alcove panel sliding on worn wooden runners, dust motes rising through candlelight), S02 **봉인끈**(frayed red cord fibres catching candle light, the knot loosening with real friction, the cord falling in a soft coil on the table), S03 **종이·시선**(aged paper unfolding with the stiff careful crackle of old paper, a held breath behind a frozen gaze), S04 **인주·붓필**(matte cinnabar pigment texture on the seal impression, a cursive ink flourish drawn with real brush pressure variation), S05 **주먹·의복**(silk sleeve drawing tight over the knuckles, candle flame breathing in the still air of a held room), S06 **옷깃·종이**(the folded letter sliding into the cloth fold of the hanbok with real cloth weight, a perfectly straight spine holding still), S07 **창·새벽**(deep blue pre-dawn light shifting slowly in value through paper lattice, two silhouettes holding perfectly still), S08 **뚜껑·암전**(the lid lowering with real wooden weight, the light thinning through blue into complete black).
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ②·⑦ 준수)**: 유혈·상해·폭력·위협 일체 없음. 밀서와 수결은 증거 서류일 뿐이며, 왕의 복수 선언은 무음 렌더의 시각 연출(주먹·시선)으로만 처리 — 렌더 프롬프트에 유언·협박·처형 어휘 일체 없음. 전 등장 인물 성인 — `all characters are adults`.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록).
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **이환(왕)**: 24-year-old king, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown, the bearing of a monarch holding ten years of evidence in his hands
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제19화 「사헌부 옥사의 진실」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 비단함이 닫히고 완전 암전으로 끝난다.
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01~S06은 `one candle lamp on the low wooden table as the primary warm amber light source, the hidden alcove's interior remaining unlit, deep shadows around the room, faint cool moonlight in the deep background`. S07~S08은 `deep blue pre-dawn light through the paper lattice window as the dominant source, the candle lamp's flame paling small against it`. 완전 암부 디테일 소실 금지: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`.
11. **문서·물체 텍스트 슬롭 방지(정본 AG ①)**: 밀서 본문은 `faint flowing cursive ink strokes, no legible text, no gibberish glyphs, no readable letters`, 수결 인주는 `one round geometric seal impression, a soft matte disc with faint relief pattern, no characters`. 비단함은 사각형 낡은 명주 보자기 개봉함으로 고정(소품 동일성 — EP18 전 썬 공통).
12. **보이스 모델 배정**: 이환 `ko-KR-Neural2-C` (Pitch -1.0), 설화 `ko-KR-Neural2-A` (Pitch -1.0), 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0) — 본 화 등장 3인 간 음성 모델 충돌 0건. 윤경헌은 등장하지 않음(수결만 등장).

---

## 1. S01 벽장의 비단함 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP18_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 후각 탁자 — 왕이 비밀 벽장 속에서 낡은 비단함을 꺼냄. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "십 년을 숨겨온 종이가 — 세상 빛을 보았다." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown, the bearing of a monarch holding ten years of evidence in his hands. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp on the low wooden table is the primary warm amber light source, the hidden alcove's interior remaining unlit, deep shadows around the rear study hall, faint cool moonlight in the deep background. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm wide, static: the young king standing before a small hidden alcove opened in the dark wooden wall of a rear study hall at night, one candle lamp on the low table beside him as the only light.
2. 50mm, static: his hands drawing a small rectangular aged silk-covered box out of the alcove's darkness, faint dust rising in the lamp light.
3. 85mm close, static: his face looking down at the silk box held in both hands, ten years of keeping in the melancholy eyes.
4. 85mm close, static: the box settling onto the dark wooden table, faint dust motes rising slowly through the warm candle light around it.

ALCOVE AND BOX MOTION — IMPORTANT: physically-based aged silk cloth sagging with real cloth weight, the wooden alcove panel sliding on worn wooden runners, dust motes rising through candlelight. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 붉은 봉인끈 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP18_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 봉인끈 개봉 — 비단함의 붉은 봉인끈이 풀림. [낮게 깔린 애수 · 이환/`ko-KR-Neural2-C`, Pitch -1.0, Speed 1.0] "과인이 지키지 못한 자들의… 피로 쓴 명부다." (rel 3.5=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch, pale refined handsome features, deep melancholy eyes, dark royal informals with a gold winged ikseongwan crown, grief held under a composed still face. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp on the low wooden table is the primary warm amber light source, its glow catching the frayed cord fibres and the faded silk, deep shadows around the room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the rectangular aged silk-covered box on the dark wooden table, a faded red sealing cord wound tight around its lid, the cord fibres frayed with age, candle light glinting along the weave.
2. 50mm, static: the young king's fingers slowly drawing the loosened red sealing cord off the lid, the cord falling in a soft coil beside the box, his sleeve resting on the table.
3. 85mm close, static: his face low over the opened silk box, grief held under composure, resolve layered in the melancholy eyes as he speaks in a low tone.

CORD AND CLOTH MOTION — IMPORTANT: physically-based frayed red cord fibres catching candle light, the knot loosening with real friction, the cord falling in a soft coil on the table. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 아버지의 글씨 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP18_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 펼쳐지는 밀서, 설화의 시선이 얼어붙음. [떨림을 삼킨 중얼거림 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "아버지의 글씨… 그리고." (rel 3.0=절대 16.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The young king is a 24-year-old Korean monarch, pale refined handsome features, dark royal informals with a gold winged ikseongwan crown. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp on the low wooden table, its warm glow on the aged paper and both faces, deep shadows around the rear hall. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot, static: the king and the court lady facing each other across the low table as the secret letter unfolds open between them in the candle light.
2. 85mm close, static: the unfolded secret letter spread flat on the dark table, faint flowing cursive ink strokes across the aged paper with no legible characters, candle light warming the paper's edge.
3. 85mm close, static: the court lady's cold intelligent dark eyes frozen on the letter, one beat of stillness as recognition lands, her folded hands unmoved, candle light on her cheek.

PAPER AND GAZE MOTION — IMPORTANT: physically-based aged paper unfolding with the stiff careful crackle of old paper, a held breath behind a frozen gaze, candle light flickering across the paper grain. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 윤경헌의 수결 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP18_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 수결 인서트 — 밀서 말미 붉은 인주, 윤경헌의 수결. [서늘한 확인 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "윤경헌. 그의 손이 여기 찍혀 있었군요." (rel 3.5=절대 24.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache — elegant dark pastel hanbok. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp nearby, warm light on the aged paper's grain and her hand, the deep room falling into shadow behind. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the secret letter's end on the table, one round matte cinnabar seal impression with a faint geometric relief pattern beside a single cursive ink flourish, no legible characters anywhere on the paper, candle light on the paper grain.
2. 85mm close, static: the court lady's fingertip hovering a breath above the round seal impression, her hand perfectly steady, bare ears with no earrings, candle light on her knuckle.
3. 85mm close, static: her cold intelligent dark eyes lifting from the paper toward the king off-frame, quiet iron in the gaze as she names the hand that signed.

SEAL AND BRUSH MOTION — IMPORTANT: physically-based matte cinnabar pigment texture on the seal impression, a cursive ink flourish drawn with real brush pressure variation, the hovering fingertip never touching the paper. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 왕의 주먹 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP18_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 왕이 주먹을 쥐며 고개를 듦. [억누른 겁화 · 이환/`ko-KR-Neural2-C`, Pitch -1.0, Speed 1.0] "사헌부를 베어낸 칼날의 주인이다. 과인이 직접 그 목을 벨 것이다." (rel 4.0=절대 32.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, elegant dark pastel hanbok, single plain undecorated jade hairpin, no earrings. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp on the low wooden table, its warm glow carving the king's features from below, the folded letter resting on the table between them, deep shadows around the room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the young king's hand closing into a fist at the table's edge, the silk sleeve drawing tight over the knuckles, candle light catching the tension in his hand.
2. 85mm close, static: his head rising, the melancholy eyes banked with quiet fury hardened into resolve, jaw set.
3. 85mm tight close, static: his mouth and jaw as he speaks a low vow, no shouting, the words carried with the flat certainty of a monarch who has decided.
4. 50mm two-shot, static: the vow crossing the table, the court lady receiving it in perfect stillness, the candle lamp between them.

FIST AND FLAME MOTION — IMPORTANT: physically-based silk sleeve drawing tight over the knuckles, candle flame breathing in the still air of a held room, shadows tilting with the flame. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 법으로 먼저 꺾는다 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP18_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 투숏 — 설화가 밀서를 받아 품에 넣음. [얼음장 응답 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "아니옵니다, 전하. 그 목은 — 법으로 먼저 꺾어야 하옵니다." (rel 4.0=절대 39.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache — elegant dark pastel hanbok. The young king is a 24-year-old Korean monarch, pale refined handsome features, dark royal informals with a gold winged ikseongwan crown. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: one candle lamp on the low wooden table between them, warm light on the letter and her hands, deep shadows around the rear hall. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm two-shot, static: the court lady extending both hands to receive the secret letter, the king holding it one beat longer in the candle light.
2. 85mm close, static: the folded secret letter laid into her open hands, her fingers closing around the aged paper with a keeper's care.
3. 50mm profile, static: her profile tucking the folded letter into the breast fold of her dark pastel hanbok, the paper vanishing into the cloth, her spine perfectly straight.
4. 85mm close, static: her calm face in candle light, lips level, cold intelligent dark eyes steady as she corrects the king's vow with the law, not a tremor anywhere.

CLOTH AND PAPER MOTION — IMPORTANT: physically-based the folded letter sliding into the cloth fold of the hanbok with real cloth weight, a perfectly straight spine holding still, candle light breathing across her composed face. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 증좌의 새벽 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP18_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 후각 창밖 여명 직전 푸른 어둠. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "복수의 밤이 지나고 — 증좌의 새벽이 오고 있었다." (rel 3.5=절대 47.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch in dark royal informals with a gold winged ikseongwan crown. The court lady is a 21-year-old Korean woman in elegant dark pastel hanbok with a single plain undecorated jade hairpin, no earrings. Both appear as distant silhouettes only. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: deep blue pre-dawn light through the paper lattice window as the dominant source, the hour just before daybreak, the candle lamp's flame paling small against the growing blue. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the rear hall's paper lattice window glowing with deep pre-dawn blue darkness, the hour just before daybreak, the dark room's edges fading into the cold blue light.
2. 24mm wide, static: two distant silhouettes — the king and the court lady — inside the dark rear hall against the window's deep blue pre-dawn light, the folded letter kept between them.
3. 35mm, static: the single candle lamp's flame paling small against the brightening blue pre-dawn light filling the room, the dark wood catching the first cold light.

WINDOW AND DAWN MOTION — IMPORTANT: physically-based deep blue pre-dawn light shifting slowly in value through paper lattice, two silhouettes holding perfectly still, the candle flame shrinking in contrast as the blue grows. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 비단함이 닫히고 암전 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP18_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 굳게 닫히는 비단함 → 암전 → 타이틀. [자막: 제19화 「사헌부 옥사의 진실」에서 계속]
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch in dark royal informals with a gold winged ikseongwan crown, hands lowering the box lid. All characters are adults. No violence, no weapons drawn, no injury, no blood.

LIGHT GUARD — IMPORTANT: deep blue pre-dawn light through the paper lattice window thinning gradually, the candle lamp's flame shrinking, until the frame sinks into complete darkness. Deep shadow areas must keep readable detail before total black.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm, static: the young king's hands lowering the rectangular silk box's lid closed on the dark table in the blue pre-dawn light, slow and deliberate, a keeper's final rite.
2. 85mm close, static: the loosened red sealing cord lying in a loose open circle on the dark table beside the closed silk box, the candle lamp's light thinning across the wood.
3. The blue light thins and the frame sinks into darkness.
4. Total blackness: screen fades into complete pitch-black cinematic darkness, holding silent and still for the final seconds before end. (Note: Korean title text is inserted in post-production editing).

LID AND LIGHT MOTION — IMPORTANT: physically-based the lid lowering with real wooden weight, the light thinning through blue into complete black, the cord lying still. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 10. SRT 분리형 자막 및 보이스 타임코드 인라인 대응표

### 10-1. 보이스 타임코드 대응표

| 썬 | 절대 시간 | 인물 | Google TTS 모델 | Pitch / Speed | 대사 전문 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 내레이션 | `ko-KR-Wavenet-C` | Pitch 0.0 / Speed 0.9 | 십 년을 숨겨온 종이가 — 세상 빛을 보았다. (절대 2.0초 시작) |
| S02 | 07.5~15.0 | 이환 | `ko-KR-Neural2-C` | Pitch -1.0 / Speed 1.0 | 과인이 지키지 못한 자들의… 피로 쓴 명부다. (절대 9.5초 시작) |
| S03 | 15.0~22.5 | 설화 | `ko-KR-Neural2-A` | Pitch -1.0 / Speed 1.0 | 아버지의 글씨… 그리고. (절대 16.5초 시작) |
| S04 | 22.5~30.0 | 설화 | `ko-KR-Neural2-A` | Pitch -1.0 / Speed 1.0 | 윤경헌. 그의 손이 여기 찍혀 있었군요. (절대 24.5초 시작) |
| S05 | 30.0~37.5 | 이환 | `ko-KR-Neural2-C` | Pitch -1.0 / Speed 1.0 | 사헌부를 베어낸 칼날의 주인이다. 과인이 직접 그 목을 벨 것이다. (절대 32.0초 시작) |
| S06 | 37.5~45.0 | 설화 | `ko-KR-Neural2-A` | Pitch -1.0 / Speed 1.0 | 아니옵니다, 전하. 그 목은 — 법으로 먼저 꺾어야 하옵니다. (절대 39.5초 시작) |
| S07 | 45.0~52.5 | 내레이션 | `ko-KR-Wavenet-C` | Pitch 0.0 / Speed 0.9 | 복수의 밤이 지나고 — 증좌의 새벽이 오고 있었다. (절대 47.5초 시작) |
| S08 | 52.5~60.0 | 자막 전용 | — | — | 제19화 「사헌부 옥사의 진실」에서 계속 (절대 57.0초 삽입) |

### 10-2. 분리형 SRT 한글 자막

```srt
1
00:00:02,000 --> 00:00:05,000
십 년을 숨겨온 종이가 — 세상 빛을 보았다.

2
00:00:09,500 --> 00:00:12,500
과인이 지키지 못한 자들의… 피로 쓴 명부다.

3
00:00:16,500 --> 00:00:19,000
아버지의 글씨… 그리고.

4
00:00:24,500 --> 00:00:28,000
윤경헌. 그의 손이 여기 찍혀 있었군요.

5
00:00:32,000 --> 00:00:36,000
사헌부를 베어낸 칼날의 주인이다. 과인이 직접 그 목을 벨 것이다.

6
00:00:39,500 --> 00:00:43,500
아니옵니다, 전하. 그 목은 — 법으로 먼저 꺾어야 하옵니다.

7
00:00:47,500 --> 00:00:51,000
복수의 밤이 지나고 — 증좌의 새벽이 오고 있었다.

8
00:00:57,000 --> 00:01:00,000
제19화 「사헌부 옥사의 진실」에서 계속
```
