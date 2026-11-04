# 「혈화의 궐」 EP04 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제4화 「밤의 밀약」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP03 원장 운용 결과
> **범위**: EP04 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 등불 불꽃·김(증기)·안개·종이·옷자락 등 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다(스케치의 정적 선 추종 차단).
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·시신 묘사 일체 없음. 무결의 환도는 전 썬 **칼집 착용(sheathed)** — 뽑기·위협 동작 없음. 밀정은 폭력 없는 관음·수거 동작만. 종이 반 장 수거는 협박 아닌 은밀한 정보 수집으로 연출(`silent, unobserved`).
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지.
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok
   - **강무결**: 25-year-old warrior captain, tall, sharp jawline, faint scar across cheekbone, dark navy and black military uniform (yungbok), sheathed Korean sword (hwando) at his belt
   - **밀정(신규 조연)**: lean Joseon covert agent in his 40s, short beard stubble, black headcloth, dark commoner jeogori — **characters.md 등록 전까지 임시 앵커**(렌더 전 원장 등록 필요 — HANDOVER_LOG 미결 항목 준용)
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제5화 「중궁전의 장부」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 소매 수거 → 종이 매크로 → 암전 진행까지만.
10. **야간 광원 표기(정본 AG 검수 ① 준수)**: 본 화 전 썬의 키 라이트는 **기름등(oil lamp)** 이다. 전 썬 `warm oil lamp glow`를 광원으로 명시하고 저대비 슬롭을 차단한다 — 광원 모티베이션 없는 인공 키 라이트 금지. 복도 야간이므로 달빛은 보조 광(`pale moonlight through lattice windows`)으로만.

---

## 1. S01 밤참을 나르는 손 (절대 00.0~07.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP04_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 밤참 수송 → 눈동자 매크로 → 복도 끝 왕의 실루엣. 서늘한 관찰 속마음이 개방 컷을 지배한다. [서늘한 관찰 속마음 · 설화/Neural2-A] "시야에 든 눈이 세 개. 그중 하나는 왕의 것이었다." (rel 3.0=절대 2.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, unnervingly calm. At the far end of the corridor, a royal silhouette in a red dragon robe (gonryongpo) and a gold royal winged hat (ikseongwan) half-hidden in shadow, features unreadable. No weapons drawn.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, shallow depth of field, static: the court lady's pale steady hands carrying a lacquered wooden night-meal tray with covered ceramic bowls down a dark royal palace corridor at night, thin steam curling from the bowls, warm oil lamp glow as the only key light.
2. 100mm macro, slow rack focus: her cold dark eyes just above the rising steam, the oil lamp flame burning as a tiny reflection inside her iris, perfectly still.
3. 100mm macro to deep focus, slow rack to the far end: her eyes razor-sharp in the foreground while, far down the lamplit corridor, the faint royal silhouette with a winged hat watches from the shadows — three eyes in her field of view, one of them the king's.

STEAM AND LAMP MOTION — IMPORTANT: physically-based thin steam rising and curling from the covered bowls in slow strands, oil lamp flames flickering with realistic warm falloff along the corridor, hanbok sleeve fabric stirring subtly with each step. Do NOT follow the sketch's static lines — the night meal procession must breathe like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 길을 막지 않는 무결 (절대 07.5~15.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP04_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 기다림의 와이드 → 50mm 비켜섬 → 환도 손잡이 매크로. 막지 않음이 곧 약속 이행이라는 정본 치환(보호 독백 삭제)의 미장센. [묵직한 저음 · 무결/Wavenet-C] "오늘 밤 이 복도를 지나는 나인은 없습니다. 그 약속은 지켰지요." (rel 2.5=절대 9.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, wearing dark navy and black military uniform (yungbok), a traditional Korean sword STAYING SHEATHED at his belt — he steps aside, never blocks, never draws. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, carrying a lacquered wooden night-meal tray.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: a long night palace corridor lit by a row of warm oil lamps, the tall warrior captain standing respectfully aside against a wooden pillar, deliberately leaving the path open, the small figure of the court lady with her tray approaching in the depth of frame.
2. 50mm medium, slight tilt-down: the warrior lowering his gaze and quietly turning his shoulder aside to let her pass — restrained, formal courtesy, a kept promise spoken without words.
3. 100mm macro, shallow depth of field, static: his hand resting calm on the sheathed sword hilt at his belt, fingers loose and unmoving — vigilance without threat, the blade never drawn.

LAMP AND FABRIC MOTION — IMPORTANT: physically-based warm oil lamp flames breathing along the corridor with soft light falloff, uniform and hanbok fabric moving naturally as he steps aside, the tray held perfectly level. No violence, no weapons drawn. Do NOT follow the sketch's static lines — the courtesy must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 거래의 언어 (절대 15.0~22.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP04_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 정면 투숏 고정 → 설화의 조건 제시 → 무결의 단문 → 등불 불꽃 매크로. 두 사람이 처음으로 거래의 언어로 말하는 정본 개수 장면. [절제된 조건 제시 · 설화/Neural2-A] "당신의 침묵의 값은 무엇이지요. 나는 사서 갚을 수 있나이다." (rel 2.5=절대 16.5) / [자책이 깔린 단문 · 무결/Wavenet-C] "값은 아직 없습니다. 그저 — 아무것도 묻지 말라이까." (rel 5.0=절대 19.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, speaking in measured, level tones. The warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, dark navy and black military uniform, a traditional Korean sword STAYING SHEATHED at his belt, answering with a quiet, burdened single sentence. No weapons drawn.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm frontal two-shot, locked-off static: the court lady and the warrior captain facing each other squarely in warm oil lamp light in a night palace corridor, two people speaking the language of trade for the first time.
2. 85mm close-up, static: her calm composed face, eyes level, asking the price of his silence with perfect politeness.
3. 85mm close-up, static: his lowered eyes, jaw tight, answering in a quiet burdened single sentence — do not ask anything.
4. 100mm macro, static: the oil lamp flame standing tall between them, holding in a silent beat.

LAMP FLAME MOTION — IMPORTANT: physically-based oil lamp flame bending and breathing subtly with the night air, micro-detail in eyes and skin rendered realistically, fabric stillness with only breathing movement. Do NOT follow the sketch's static lines — the stillness must be alive, like real filmed footage held on a breath.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 등불에 드러난 검흔 (절대 22.5~30.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP04_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 무거움의 클로즈업 → 검흔 매크로 → 듣는 설화. 십 년 전 그 밤을 아는 사람이 둘뿐이라는 낮은 톤의 폭로. [한이 맺힌 낮은 톤 · 무결/Wavenet-C] "십 년 전 그 밤을 아는 사람은, 궁에 둘뿐이지요." (rel 2.5=절대 24.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint old scar across his cheekbone, dark navy and black military uniform (yungbok), a traditional Korean sword STAYING SHEATHED at his belt, voice low with old grief. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, listening motionless. No injuries, no blood, no weapons drawn — the scar is an old healed mark.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close-up, slow push-in: the warrior captain's face in the night corridor as raking warm oil lamp light slowly reveals the faint old scar across his cheekbone, half his face sinking into deep shadow.
2. 100mm macro, static: hard chiaroscuro macro of the scarred cheekbone, lamplight and shadow dividing the skin, every old fiber of the healed mark rendered realistically.
3. 85mm close-up, static: the court lady listening without a single movement, eyes steady and unreadable, lamp glow living on one cheek.

LAMP RAKE MOTION — IMPORTANT: physically-based oil lamp light wavering gently so the shadow line across his face breathes, micro skin detail realistic, subtle breathing motion in both figures. No violence, no blood, no weapons drawn. Do NOT follow the sketch's static lines — the revelation must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 두 얼굴 사이의 불꽃 (절대 30.0~37.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP04_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 불꽃 → 50mm 전환 두 얼굴 사이 흔들림. 셋째 사람의 이야기를 미루는 서늘한 결의로 썬을 닫는다. [서늘한 결의 · 설화/Neural2-A] "그럼 셋째 사람의 이야기는, 아직 하지 않는 것으로 하지요." (rel 3.0=절대 32.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, coldly resolute. The warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, dark navy and black military uniform, a traditional Korean sword STAYING SHEATHED at his belt. No weapons drawn.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, shallow depth of field, static: the wick flame of a traditional Korean brass oil lamp (deungjan) burning steady on its low wooden stand in a night palace corridor — no glass chimney, no western kerosene lamp.
2. 100mm macro, slow focus pull: the small flame razor-sharp while two blurred faces float out of focus behind it, the lamp standing between them.
3. 50mm medium two-shot, static: the court lady and the warrior captain on either side of the low oil lamp between them, each face half-lit and half in shadow, a pact sealed without witnesses.

FLAME AND FACE MOTION — IMPORTANT: physically-based oil lamp flame bending and breathing, warm light wavering across both faces so the half-shadow line trembles naturally, micro-detail in eyes, hanbok and uniform fabric perfectly still except breathing. Do NOT follow the sketch's static lines — the flame must carry the scene like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 갈라지는 두 그림자 (절대 37.5~45.0 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP04_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 원거리 → 조감 그림자 분리 → 좌우 갈라짐 → 텅 빈 중정. 나레이션이 견디는 자의 서사를 얹는다. [무거운 나레이션 · 내레이션/Wavenet-C 다큐 톤] "밀약에는 조인자가 필요 없다. 견디는 자만 있으면 된다." (rel 3.0=절대 39.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two distant figures only: a court lady in an elegant dark pastel hanbok with a jade hairpin, and a warrior captain in dark navy uniform with a sheathed sword at his belt. Both far from camera, no faces visible, no close-ups.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. Extreme wide 24mm static: a moonlit Joseon palace courtyard at night, the two distant figures walking away from each other across the flagstones, warm oil lamps and pale moonlight through lattice windows.
2. High-angle overhead, slow crane up: two long shadows cast by the oil lamps splitting in opposite directions across the stone flagstones as the figures part.
3. 24mm wide, static: one figure vanishing into the left colonnade and the other into the right, the empty center of the frame left open.
4. 24mm wide, static: the emptied moonlit courtyard with a single oil lamp still burning, moonlight resting on stone, nobody left.

SHADOW AND LAMP MOTION — IMPORTANT: physically-based long lamp shadows stretching and tearing apart as the figures walk, oil lamp flame breathing in the night air, hanbok hem and uniform fabric moving naturally with each distant step, pale night haze drifting low. Do NOT follow the sketch's static lines — the parting must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 담장 너머의 밀정 (절대 45.0~52.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP04_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 엿보기 구도 → 밀정 래터럴 → 손가락 매크로 → 암골 퇴장. 윤경헌의 귀가 밤의 복도를 벌써 들었다는 위압적 협박 조소. [위압적 협박 조소 · 밀정/Neural2-B] "대전 침전의 새 나인 — 이름이 뭐더라." (rel 3.0=절대 47.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the spy is a lean Joseon covert agent in his 40s, short beard stubble, black headcloth, dark commoner jeogori, half his face in shadow, silent and unobserved. He only watches and withdraws — no violence, no weapon, no confrontation.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 135mm compressed telephoto, static peek composition: the view squeezed through wooden fence slats at night — a single narrow unblinking eye visible in the gap between the boards.
2. 135mm, slow lateral track: the middle-aged spy half-hidden behind the palace outer fence, half his face in shadow, watching the lit corridor beyond without moving, a distant oil lamp glowing deep in the background.
3. 100mm macro, static: his rough weathered fingers gripping the fence wood, knuckles tight, wood grain and callused skin rendered realistically.
4. 135mm, static: the spy turning away into a dark alley beyond the fence with a thin cold smile, murmuring a name to himself as he melts into the night.

NIGHT SHADOW MOTION — IMPORTANT: physically-based deep night shadows breathing around the fence, faint warm lamp glow flickering far behind him, fabric of the jeogori shifting with his slow movement, breath vapor in the cold air. No violence, no weapons. Do NOT follow the sketch's static lines — the surveillance must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 종이 반 장과 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP04_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 소매 수거 → 100mm 종이 매크로 → 암전. **붉은 타이틀(제5화 「중궁전의 장부」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the spy is a lean Joseon covert agent in his 40s, short beard stubble, black headcloth, dark commoner jeogori, silent and unobserved. He only hides a piece of paper — no violence, no weapon, nobody else in the frame.

Recreate the panels in order as one continuous ~10 second sequence:
1. 35mm, static: in a dark night alley beyond the palace fence, the spy slipping half a sheet of folded paper into his wide sleeve, half his face in shadow, a distant oil lamp glowing at the alley's end.
2. 100mm macro, static: extreme close-up of the aged folded paper surface in the sleeve — worn fibers, faint illegible aged ledger brush marks, unreadable, secrets almost erased.
3. The frame slowly dims — the distant lamp glow shrinking until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

PAPER AND FADE MOTION — IMPORTANT: physically-based paper flexing and settling into the fabric of the sleeve, cloth folds moving naturally, the lamp glow dying in a smooth cinematic fade to black. No violence, no weapons. Do NOT follow the sketch's static lines — the concealment must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 3컷 | EP04_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 기름등 광원 명시(AG ①) |
| S02 | 07.5~15.0 | 3컷 | EP04_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 환도 칼집 유지 · 길 비켜섬(정본 치환) |
| S03 | 15.0~22.5 | 4컷 | EP04_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 거래의 언어 — 무폭력 대화 |
| S04 | 22.5~30.0 | 3컷 | EP04_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 검흔 = 옛 흉터(유혈 없음) |
| S05 | 30.0~37.5 | 3컷 | EP04_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 등잔(석촌형) 명시 — 서양 등급 금지 |
| S06 | 37.5~45.0 | 4컷 | EP04_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 원거리·무근접 — 인물 클로즈업 없음 |
| S07 | 45.0~52.5 | 4컷 | EP04_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 밀정 무기·폭력 없음 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP04_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 엔드카드·타이틀은 편집 삽입 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 설화 `ko-KR-Neural2-A` (Pitch -1.0) | rel 3.0 | 절대 2.0 | 시야에 든 눈이 세 개. 그중 하나는 왕의 것이었다. |
| 2 | S02 | 무결 `ko-KR-Wavenet-C` (Pitch -1.5) | rel 2.5 | 절대 9.0 | 오늘 밤 이 복도를 지나는 나인은 없습니다. 그 약속은 지켰지요. |
| 3 | S03 | 설화 `ko-KR-Neural2-A` | rel 2.5 | 절대 16.5 | 당신의 침묵의 값은 무엇이지요. 나는 사서 갚을 수 있나이다. |
| 4 | S03 | 무결 `ko-KR-Wavenet-C` | rel 5.0 | 절대 19.0 | 값은 아직 없습니다. 그저 — 아무것도 묻지 말라이까. |
| 5 | S04 | 무결 `ko-KR-Wavenet-C` | rel 2.5 | 절대 24.0 | 십 년 전 그 밤을 아는 사람은, 궁에 둘뿐이지요. |
| 6 | S05 | 설화 `ko-KR-Neural2-A` | rel 3.0 | 절대 32.0 | 그럼 셋째 사람의 이야기는, 아직 하지 않는 것으로 하지요. |
| 7 | S06 | 내레이션 `ko-KR-Wavenet-C` (다큐 톤) | rel 3.0 | 절대 39.5 | 밀약에는 조인자가 필요 없다. 견디는 자만 있으면 된다. |
| 8 | S07 | 밀정 `ko-KR-Neural2-B` (위압적 조소 톤) | rel 3.0 | 절대 47.0 | 대전 침전의 새 나인 — 이름이 뭐더라. |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.0 | 절대 59.0 | 제5화 「중궁전의 장부」에서 계속 |

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,000
시야에 든 눈이 세 개.
그중 하나는 왕의 것이었다.

2
00:00:09,000 --> 00:00:13,000
오늘 밤 이 복도를 지나는 나인은 없습니다.
그 약속은 지켰지요.

3
00:00:16,500 --> 00:00:18,800
당신의 침묵의 값은 무엇이지요.
나는 사서 갚을 수 있나이다.

4
00:00:19,000 --> 00:00:21,800
값은 아직 없습니다.
그저 — 아무것도 묻지 말라이까.

5
00:00:24,000 --> 00:00:27,500
십 년 전 그 밤을 아는 사람은,
궁에 둘뿐이지요.

6
00:00:32,000 --> 00:00:35,500
그럼 셋째 사람의 이야기는,
아직 하지 않는 것으로 하지요.

7
00:00:39,500 --> 00:00:43,000
밀약에는 조인자가 필요 없다.
견디는 자만 있으면 된다.

8
00:00:47,000 --> 00:00:50,000
대전 침전의 새 나인 —
이름이 뭐더라.

9
00:00:59,000 --> 00:01:00,000
제5화 「중궁전의 장부」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 9번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
