# 「혈화의 궐」 EP06 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제6화 「발각의 위기」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04·EP05 원장 운용 결과
> **범위**: EP06 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 발각 주체는 **윤경헌의 밀정**으로 통일(구 006본의 '중전 발각' 충돌 제거). 중전 윤씨는 본 화 미등장 — '이용하는 쪽'으로 EP07 이후 배치. 밀정·조사 나인은 신규 조연으로서 얼굴 식별 회피 연출(그림자·모자·등)이 기본이며, **뒷모습만의 컷 금지 — 등+복도 종심 구도 필수**(정본 AG 검수 ①⑥).

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **빗물**(layered rain sheets, beading, wet reflections), S02 **촛불·서류 종이**(flame breathing, paper flexing), S03 **물·약 증기**(water tremble, steam curling), S04~S05 **초롱 불꽃·옷자락**, S06~S08 **옥비녀·한지·명주**(jade specular, silk settling). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·시신·폭력 묘사 일체 없음. 무결의 환도는 전 썬 **칼집 착용(sheathed)** — 뽑기·위협 동작 없음. 본 화는 추격·대치 씬이 없으므로 전 썬 **관찰·검문의 느린 절제의 공포** 드라마다. 정본 안티슬롭 치환(기관총 편집 삭제 → 밤참 물건 낌새를 채가는 절제) 준수 — 컷 전환은 조용하게, 과장된 발각 반응 금지.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지.
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin, elegant dark pastel hanbok
   - **강무결**(S04·S05): 25-year-old warrior captain, tall, sharp jawline, faint scar across cheekbone, dark navy and black military uniform (yungbok), sheathed Korean sword (hwando) at his belt
   - **윤경헌**(S02): 58-year-old Joseon prime minister, sharp hawk eyes, deep wrinkles of power, black horsehair official hat (heungrip), dark crimson and gold embroidered court robes, white jade ornament, cold arrogant faint smirk
   - **밀정**(S01, 신규 조연): a faceless royal spy — wide woven sedge hat brim in deep shadow, dark travel cloak, NEVER a visible face (얼굴 식별 회피 연출)
   - **조사 나인**(S06~S07, 신규 조연): a stern middle-aged palace inspector court lady, plain grey-blue official uniform, hair in a simple tight bun with a plain wooden pin, sharp appraising eyes
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제7화 「이중의 그물」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 비녀 매크로 → 암전 진행까지만.
10. **광원 표기(정본 AG 검수 ① 준수)**: 썬별 키 라이트 모티베이션 필수 — S01 밤비 `pale lantern glow and grey moonlight diffused through rain`, S02 `a single candle flame as the only key light`, S03 새벽 일과 `soft grey dawn daylight, no candles`, S04~S05 저녁 회랑 `warm candle lanterns`, S06~S08 아침 검물 `soft morning daylight through lattice windows`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 밀정의 장부·지정(紙狀) 서류의 글자는 전 썬 `faint illegible aged brush marks, unreadable`로 강제한다. 가독 문자는 렌더에서 만들지 않고 편집 자막으로만 처리한다.
12. **옥비녀 PROP GUARD(본 화 핵심 소도구)**: 옥비녀는 전 썬(S06~S08) `a plain undecorated jade hairpin — a simple smooth jade rod with a small carved cloud-knot head, no tassels, no dangling beads`로 통일한다. 설화가 착용한 비녀와 짐꾸러기 속 비녀·최종 배치 비녀가 전부 동일 소품으로 보이도록 한다.

---

## 1. S01 빗속의 기록 (절대 00.0~07.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP06_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 엿보기 — 빗물에 젖은 담장 너머, 밀정이 기록하는 손. 발각의 주체가 스쳐 지나가는 개방 컷. [차가운 보고 · 밀정/Neural2-B] "이름은 홍화. 입궁 지정(紙狀)이 어딜 가도 끊어져 있사옵니다." (rel 3.0=절대 2.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a faceless royal spy: a wide woven sedge hat with its brim in deep shadow, a dark travel cloak, NEVER a visible face. IMPORTANT: all writing in the ledger is only faint illegible aged brush marks, unreadable, no readable characters anywhere. No violence, no weapon.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 135mm compressed telephoto, voyeuristic long-lens across a rain-soaked Joseon palace outer courtyard at night: a lone cloaked figure standing small in the distance beside a wet stone wall, deep longitudinal depth, his back mostly turned, layered rain between camera and subject.
2. 135mm, tighter past the rain-soaked stone wall: the spy's hand writing with a brush in a small oiled ledger held under his cloak, rain beading on the wet sleeve.
3. 100mm macro insert: the wet hanji ledger page, brush strokes half-smeared by raindrops, faint illegible aged brush marks raked by lantern glow.
4. 85mm, static: the spy's face lost in deep shadow beneath the wide sedge hat brim, rain dripping steadily from its edge, a held beat of cold patience.

RAIN AND PAPER MOTION — IMPORTANT: physically-based rain falling in layered sheets and thinning into mist, drops bursting and beading on stone and hat brim, wet ground reflections trembling and breaking, breath mist in the cold air, the paper flexing faintly with the wind. Do NOT follow the sketch's static lines — the surveillance must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 종이를 두드리는 손 (절대 07.5~15.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP06_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 윤경헌이 손끝으로 지정(紙狀) 서류를 두드림, 초점 전환, 권신의 냉소. 명령은 한 번의 탭으로 끝난다. [낮게 깔린 냉소 · 윤경헌/Wavenet-D] "종이가 끊기는 데는 이유가 있지. …파라. 파헤치는 데 드는 값은 내가 낸다." (rel 4.0=절대 9.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the minister is a 58-year-old Joseon prime minister: sharp hawk eyes, deep wrinkles of power, black horsehair official hat (heungrip), dark crimson and gold embroidered court robes, white jade ornament, a cold arrogant faint smirk. IMPORTANT: all writing on the documents is only faint illegible aged brush marks, unreadable, no readable characters anywhere. No violence, no weapon.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: an aged powerful fingertip tapping — twice, unhurried — the corner of an official paper registry document on dark polished wood, a single candle flame raking the paper.
2. 100mm macro, slow rack focus: the document edge sharp in front, behind it in creamy bokeh the faint cold smile of the old minister — then the focus sliding back to the paper.
3. 85mm, static: the minister seated in his opulent dim study, hands folded over the ledger, chin low, the cold smirk fully formed — power that never raises its voice.

CANDLE AND PAPER MOTION — IMPORTANT: physically-based candle flame breathing and bending, its warm falloff trembling on the polished wood, the paper corner lifting a hair with each tap's air, faint dust motes drifting through the glow. Do NOT follow the sketch's static lines — the menace must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 아무 일도 없는 아침 (절대 15.0~22.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP06_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 핸드헬 — 설화의 일과: 물 뜨고, 약 짓고, 절하고. 아무 일도 없는 얼굴. 정본 안티슬롭 치환의 핵심 썬 — "아무 일도 일어나지 않는 아침이 더 무섭게". [서늘한 자각 속마음 · 설화/Neural2-A] "조사당하는 나인은 조심한다. 그러나 조사당한다는 걸 모르는 나인은 — 움직인다." (rel 4.0=절대 17.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin, elegant dark pastel hanbok, perfectly composed, moving through an ordinary routine. The senior court lady she bows to is a plain background figure, face indistinct. No weapons, no violence.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm handheld, soft: the court lady carrying a large ceramic water jar on her head down wet stone steps in soft grey dawn light, steady unhurried steps.
2. 50mm handheld, close: her hands preparing medicine — dried herbs, a mortar, thin steam curling up through the dawn light.
3. 50mm, static: she bows deeply to a senior court lady in the yard, flawless formal bow, perfect composure.
4. 50mm, tight close-up, static: her face — absolutely nothing on it. A perfect blank morning face, only the eyes holding something too still.

WATER AND STEAM MOTION — IMPORTANT: physically-based water surface trembling subtly in the jar with her steps, steam curling and dissolving in cold dawn air, hanbok fabric swaying naturally, wet stone reflections. Do NOT follow the sketch's static lines — the ordinary morning must breathe like real filmed footage, calm and terrifying.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 회랑의 시야 차단 (절대 22.5~30.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP06_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 회랑 종심 — 회랑 끝에서 무결이 자연스럽게 시야를 가림. 등+복도 종심 구도(정본 AG ①⑥)의 대표 썬. [무언의 경계 · 무결/Wavenet-C] "뒤에 세 명. 걸음이 궁궐 걸음이 아닙니다." (rel 2.5=절대 24.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, dark navy and black military uniform (yungbok), a traditional Korean sword STAYING SHEATHED at his belt, standing casual and unremarkable. The court lady far away is a 21-year-old Korean woman in an elegant dark pastel hanbok. The three strolling men are plain background figures in dull servants' clothes, faces indistinct. No weapons drawn, no violence.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, deep-staged: a long wooden palace corridor at dusk, columns repeating into depth, the tiny lone figure of the court lady walking in the far distance — the whole corridor reading like a diagram of exposure.
2. 24mm wide, static: at the corridor's end the warrior captain stands leaning casually against a column, his body naturally blocking the sightline down the gallery — nothing about him says guard.
3. 24mm, over his shoulder in deep staging: three men strolling along the far corridor behind — and their strides are wrong, too loose, not palace steps.

LANTERN AND STRIDE MOTION — IMPORTANT: physically-based warm candle lantern flames breathing along the corridor, dusk haze in the depth, figures walking with real weight and rhythm — the wrongness carried by stride timing, not by any gesture. Do NOT follow the sketch's static lines — the geometry must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 등을 맞대고 통과 (절대 30.0~37.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP06_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 두 사람이 등을 맞대고 통과. 말은 없다 — 서로 처음 본 얼굴인 것이 오늘의 계약. 무대사 썬(렌더도 무음 연출).
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tteoljam, no dangling ornaments, no earrings — elegant dark pastel hanbok. The warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, dark navy and black military uniform (yungbok), a traditional Korean sword STAYING SHEATHED at his belt. No weapons drawn, no violence, no words spoken — silence only.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot, static: in the dusk-lit corridor the two of them pass each other back to back in profile — neither turns, not by a degree.
2. 85mm close, static: both faces forward and utterly unreadable, eyes never meeting, twin profiles separated by inches of dusk air.
3. 85mm, static: after the pass — she lets out a faint composed breath, he walks on without a glance, two strangers in public.

FABRIC AND BREATH MOTION — IMPORTANT: physically-based hanbok fabric settling after the pass, lantern flames breathing low, subtle breathing motion in both figures, dusk haze drifting. Do NOT follow the sketch's static lines — the silence must be alive, like real filmed footage held on a breath.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 옥비녀에 멈춘 눈 (절대 37.5~45.0 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP06_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 조용한 위기 — 짐꾸러기 검열, 그 안의 옥비녀, 조사 나인의 눈이 멈춤. 가벼운 시비가 곧 위기. [가벼운 시비 · 조사 나인/Neural2-B] "비녀가 여럿이면 옷도 여럿이겠지." (rel 3.0=절대 39.5) / [평온한 거짓 · 설화/Neural2-A] "나인의 물건은 나인의 것입니다." (rel 4.5=절대 41.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin, elegant dark pastel hanbok, kneeling with perfect courtesy. The inspector is a stern middle-aged palace court lady in a plain grey-blue official uniform, hair in a simple tight bun with a plain wooden pin, sharp appraising eyes. PROP GUARD — the jade hairpin in the bundle is a plain undecorated jade hairpin, a simple smooth jade rod with a small carved cloud-knot head, no tassels, no dangling beads. No violence, no weapon.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm, slow push: an open travel bundle on a straw mat, belongings spread neatly for inspection, the court lady kneeling composed beside it in soft morning daylight.
2. 35mm insert, static: among the folded clothes — a single plain jade hairpin, catching a thin blade of morning light.
3. 35mm close, static: the inspector's sharp eyes stopping dead on the hairpin — a stillness inside a routine.
4. 35mm two-shot, static: the inspector leaning in with a light probing half-smile, the court lady serene, courteous, perfectly unbothered.

SILK AND LIGHT MOTION — IMPORTANT: physically-based morning light through lattice windows, silk clothes settling after being handled, faint dust motes in the light blades, micro-expression only in the eyes. Do NOT follow the sketch's static lines — the quiet crisis must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 절반쯤 든 비녀 (절대 45.0~52.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP06_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 조사 나인이 비녀를 절반쯤 들다가, 외람한 소리에 돌아봄. 위기는 우연이 건드린다. 무대사 썬(렌더도 무음 연출) — 소리는 편집 단계 효과음으로만 암시.
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — only the inspector is in frame: a stern middle-aged palace court lady in a plain grey-blue official uniform, hair in a simple tight bun with a plain wooden pin, sharp appraising eyes. PROP GUARD — the jade hairpin is a plain undecorated jade hairpin, a simple smooth jade rod with a small carved cloud-knot head, no tassels, no dangling beads. No violence, no weapon, no words spoken — silence only.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the inspector's fingers lifting the plain jade hairpin halfway out of the open bundle — suspended mid-air, mid-thought.
2. 85mm, static: from somewhere off-screen an out-of-place sound — her head snapping around in profile, the plain jade hairpin frozen half-lifted in her fingers.
3. 85mm, static: the held beat — the whole room balanced on the suspended hairpin, her eyes flicking back toward the bundle, extreme tension in absolute stillness.

STILLNESS AND INTERRUPTION MOTION — IMPORTANT: physically-based fabric settling in the bundle, morning light through lattice windows holding steady, her head-turn rendered as one sharp natural movement — never an exaggerated performance. Do NOT follow the sketch's static lines — the accident must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 반 뼘의 어긋남 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP06_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 비녀가 원래 자리에, 위치 반 뼘 어긋나 있음 → 암전. **붉은 타이틀(제7화 「이중의 그물」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no people in frame. PROP GUARD — the jade hairpin is a plain undecorated jade hairpin, a simple smooth jade rod with a small carved cloud-knot head, no tassels, no dangling beads. No violence, no weapon.

Recreate the panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the plain jade hairpin lying back in place inside the closed travel bundle — and yet off, by half a hand-span, from where it must have rested. One wrongness inside perfect order.
2. 100mm extreme macro, static: the pale jade surface of the hairpin — faint scratches, cold morning light, utter stillness.
3. The frame slowly dims — the morning light thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

JADE AND FADE MOTION — IMPORTANT: physically-based silk folds settling almost imperceptibly, a hair-thin glint traveling along the jade surface as the light shifts, the daylight dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the final image must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP06_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 135mm 압축 엿보기 · 밀정 무얼굴 앵커 · 빗물 물리 명시(AG ①) |
| S02 | 07.5~15.0 | 3컷 | EP06_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 촛불 단일 광원 명시 · 랙 포커스 냉소 |
| S03 | 15.0~22.5 | 4컷 | EP06_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 새벽 자연광 — 촛불 금지 · 안티슬롭 치환 썬 |
| S04 | 22.5~30.0 | 3컷 | EP06_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 종심 · 등+복도 구도(정본 AG ①⑥) · 무결 칼집 착용 |
| S05 | 30.0~37.5 | 3컷 | EP06_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 무대사 — 등 맞대고 통과 · 설화 옥비녀 앵커 명시 |
| S06 | 37.5~45.0 | 4컷 | EP06_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 옥비녀 PROP GUARD 최초 등장 · 조사 나인 신규 앵커 |
| S07 | 45.0~52.5 | 3컷 | EP06_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 무대사 — 절반쯤 든 비녀 · 과장 금지 지문 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP06_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 엔드카드·타이틀은 편집 삽입 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 밀정 `ko-KR-Neural2-B` (차가운 보고 톤, Pitch -0.5) | rel 3.0 | 절대 2.0 | 이름은 홍화. 입궁 지정(紙狀)이 어딜 가도 끊어져 있사옵니다. |
| 2 | S02 | 윤경헌 `ko-KR-Wavenet-D` (낮게 깔린 냉소 톤, Pitch -2.5) | rel 4.0 | 절대 9.5 | 종이가 끊기는 데는 이유가 있지. …파라. 파헤치는 데 드는 값은 내가 낸다. |
| 3 | S03 | 설화 `ko-KR-Neural2-A` (서늘한 자각 속마음, Pitch -1.0) | rel 4.0 | 절대 17.5 | 조사당하는 나인은 조심한다. 그러나 조사당한다는 걸 모르는 나인은 — 움직인다. |
| 4 | S04 | 무결 `ko-KR-Wavenet-C` (무언의 경계 톤, Pitch -1.5) | rel 2.5 | 절대 24.0 | 뒤에 세 명. 걸음이 궁궐 걸음이 아닙니다. |
| 5 | S05 | (무대사 · 무성) | — | — | 등 맞대고 통과 — 자막 없음 |
| 6 | S06 | 조사 나인 `ko-KR-Neural2-B` (가벼운 시비 톤, Pitch -0.5) | rel 3.0 | 절대 39.5 | 비녀가 여럿이면 옷도 여럿이겠지. |
| 7 | S06 | 설화 `ko-KR-Neural2-A` (평온한 거짓 톤, Pitch -1.0) | rel 4.5 | 절대 41.0 | 나인의 물건은 나인의 것입니다. |
| 8 | S07 | (무대사 · 무성) | — | — | 위기는 우연이 건드린다 — 자막 없음 |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제7화 「이중의 그물」에서 계속 |

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,500
이름은 홍화.
입궁 지정(紙狀)이 어딜 가도
끊어져 있사옵니다.

2
00:00:09,500 --> 00:00:13,000
종이가 끊기는 데는 이유가 있지.
…파라. 파헤치는 데 드는 값은
내가 낸다.

3
00:00:17,500 --> 00:00:21,500
조사당하는 나인은 조심한다.
그러나 조사당한다는 걸 모르는
나인은 — 움직인다.

4
00:00:24,000 --> 00:00:27,000
뒤에 세 명.
걸음이 궁궐 걸음이 아닙니다.

5
00:00:32,000 --> 00:00:34,500
오늘은 서로
처음 본 얼굴이겠지요.

6
00:00:39,500 --> 00:00:40,500
비녀가 여럿이면
옷도 여럿이겠지.

7
00:00:41,000 --> 00:00:44,000
나인의 물건은
나인의 것입니다.

8
00:00:59,000 --> 00:01:00,000
제7화 「이중의 그물」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S05·S07은 무대사 썬이므로 SRT 블록이 없다 — 자막 공백 구간(00:30~00:37.5, 00:45~00:52.5)은 침묵 연출 그대로 둔다.
- S06 6·7번 자막은 조사 나인 대사(rel 3.0=39.5)와 설화 대답(rel 4.5=41.0)이 연속이므로 39.5~40.5 / 41.0~44.0으로 분할 배치한다.
- 보이스 ID 운용: 조사 나인·밀정은 중전·서 상궁과 동일 `ko-KR-Neural2-B` — 감정 톤 지문(차가운 보고/가벼운 시비)으로 구분한다(조연 보이스 원장 총칙 준용).
