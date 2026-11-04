# 「혈화의 궐」 EP08 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제8화 「서간의 밀서」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP07 원장 운용 결과
> **범위**: EP08 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 중궁전 서간 유통망 추적극이다. 밀서의 **내용은 한 줄도 공개하지 않는다** — 낙관 도장의 형태와 눈금만이 정보다(제17~18장 반전 보호). 렌더에 가독 문자·낭독·폭로 연출 일체 없음. 왕(이환)·중전 윤씨는 **미등장** — 밀실 소환 예고와 서간의 존재로만 존재를 암시한다. 폭력·흉기·상해 없음.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **서가 종이·소매·걸음**(paper flexing, sleeve hem swaying, stride rhythm), S02 **한지·인주**(paper flexing, damp vermilion sheen), S03 **다과 증기**(tea steam curling, cup surface trembling), S04 **오후 그늘·먼지**(long shadows, dust in raking light), S05 **한지·랙 포커스**(paper grain settling, focus breathing), S06 **황혼 안개·소매**(dusk haze drifting, sleeve settling), S07 **등불 불꽃·연기**(flame pinching out, smoke thread rising), S08 **문짝·먼지**(dust falling from the beam, gate wood shuddering). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·시신·폭력 묘사 일체 없음. 전 썬 무기 등장 자체가 없다(서간 운반·다과·추적·소환 전언극). 왕의 밀실 소환은 예고만 — 침입·압박 연출 없음. 정본 안티슬롭 치환(밀서 내용 낭독 폭로 삭제 → 도장 눈금만 보여주기 / "설마 이것은…" 놀람 연기 삭제 → 손가락이 멈추는 것) 준수 — 내용 폭로·놀람 과장 금지.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07 결함 재발 방지: 설화 앵커에 **귀걸이·수술·가체·입가리개 금지를 전 썬 상향 고정**했다.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok
   - **내관**(S01·S02·S03·S06, 신규 조연 — 중궁전 서간 계열 내관): a lean middle-aged royal eunuch (naegwan) in a plain grey-blue official court robe and a black horsehair cap, hands folded in braided sleeves, composed unreadable face — no jewelry, no ornament
   - **왕 이환**(미등장): never on screen — the secret-chamber summons and the tally stick imply him. No king on screen in EP08.
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제9화 「밤의 침입자」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 초인문 닫힘 → 암전 진행까지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 썬별 키 라이트 모티베이션 필수 — S01 낮 `soft overcast daylight, no lamps`, S02 낮 `lattice-filtered daylight raking the walkway shadow`, S03 낮 `soft daylight through a latticed window, one charcoal brazier glow`, S04 늦은 오후 `low golden afternoon sun, long shadows`, S05 `one strong raking window shaft on the desk`, S06 황혼 `fading dusk skylight, one gate lantern just lit`, S07 밤 `cold moonlight and one dying lamp flame`, S08 밤 `moonlight on the gate, then none`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서 텍스트 슬롭 방지(정본 AG 검수 ① 준수 — 본 화 최우선 항목)**: 서간·소환장의 글자는 전 썬 `faint illegible aged brush marks, unreadable`로 강제한다. **낙관 도장은 형태와 기하학적 눈금만** — `abstract geometric seal shape with fine parallel gauge marks, no characters, no glyphs, no readable marks` — 렌더에서 한글·한자를 만들지 않고 편집 자막으로만 처리한다(한글 왜곡 슬롯 근원 차단).
12. **내관 복식 고증(신규 조연)**: 내관은 조선 궁정 내관 규격을 벗어나지 않는다 — `plain grey-blue official court robe (dalryeong style), black horsehair cap, braided sleeves, no jewelry`. 관복 색·형태의 과장 금지.

---

## 1. S01 발 없는 우편 (절대 00.0~07.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP08_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 서가 트래킹 — 규장각 외각, 서간을 옮기는 내관의 발이 겹침. 경로 자체가 정보. [무거운 나레이션 · 내레이션/Wavenet-C] "종이는 발이 없어도 다닌다. 누군가 다리를 빌려줄 뿐이다." (rel 3.0=절대 2.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the eunuch is a lean middle-aged royal eunuch in a plain grey-blue official court robe and a black horsehair cap, hands folded in braided sleeves, composed unreadable face, no jewelry. The court lady seen far away in the last beat is a 21-year-old Korean woman with pale porcelain skin, a single plain undecorated jade hairpin, no tassels, no dangling ornaments, no earrings, no face veil, elegant dark pastel hanbok. IMPORTANT: the folded letter has only faint illegible aged brush marks, unreadable, no readable characters anywhere. No violence, no weapon.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm tracking, smooth: a long low tracking shot gliding alongside a lean middle-aged royal eunuch in a grey-blue robe and black horsehair cap walking the outer wooden walkway of the royal archive, a folded letter hidden in his braided sleeve, the walkway receding into depth.
2. 100mm macro insert: his overlapping feet and padded slippers striking weathered stone flags in an even rhythm, the sleeve hem swaying with each stride.
3. 50mm, static, from behind in deep corridor depth: the eunuch walking away, shoulders composed, the paper corner barely showing at his cuff.
4. 35mm, static, deep-staged: the walkway wide, the eunuch small in the distance, and in the near shadow of a pillar the plain-dressed court lady watching him go, utterly still.

DAYLIGHT AND PAPER MOTION — IMPORTANT: physically-based dust drifting in soft overcast daylight, the hanji letter flexing faintly inside the sleeve with each stride, sleeve hem swaying with real fabric weight, real stride rhythm in the feet. Do NOT follow the sketch's static lines — the moving letter must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 젖은 인주 (절대 07.5~15.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP08_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 내관 소매 안 종이 귀퉁이, 붉은 인주 자국. 발견은 놀람이 아니라 손가락의 정지로. [서늘한 발견 속마음 · 설화/Neural2-A] "인주가 아직 마르지 않았어." (rel 3.0=절대 9.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. The eunuch in the background is a lean middle-aged royal eunuch in a plain grey-blue court robe and black horsehair cap. IMPORTANT: the letter paper shows only faint illegible aged brush marks, unreadable, plus one shapeless damp red cinnabar smudge on the folded corner — a smudge only, not a seal, no characters, no glyphs. No violence, no weapon.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a folded hanji letter corner slipping from a grey-blue eunuch sleeve, a small damp red cinnabar smudge on the paper edge catching lattice-filtered daylight, the folds sharp in shallow focus.
2. 100mm macro, static: the court lady's fingertips rising beside the paper and stopping mid-air — the hand simply halts, a hair from the paper, never touching it.
3. 50mm close, static: her face in the walkway shadow, pale porcelain skin, cold intelligent dark eyes lowering to the paper, the plain jade rod in her plain bun, bare ears, no jewelry anywhere — discovery shown only as stillness.

PAPER AND LIGHT MOTION — IMPORTANT: physically-based hanji flexing faintly in the moving air, the damp vermilion smudge holding a wet sheen, dust drifting through the raking lattice light, her sleeve settling after the stopped hand. Do NOT follow the sketch's static lines — the cold discovery must feel like real filmed footage. No gasp, no widened eyes — only the stopped fingers.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 오가지 않는 서간 (절대 15.0~22.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP08_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 설화와 내관의 사이에 놓인 다과, 서간은 오가지 않음. 예의가 곧 참호. [절제된 응대 · 설화/Neural2-A] "서간은 마마께만 가나이다." (rel 5.0=절대 19.5) / [긴장한 무거움 · 내관/Neural2-C] "…나인은 보는 눈이 많구나." (rel 6.0=절대 20.5 — 보조 배분)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. The eunuch is a lean middle-aged royal eunuch in a plain grey-blue official court robe and black horsehair cap, hands folded in braided sleeves, no jewelry. No letter and no paper is shown or exchanged in this scene. No violence, no weapon.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot, static: the court lady and the eunuch seated across a low tea table in a small tea room off the archive, steam rising from two cups, soft daylight through a latticed window, the space between them held perfectly formal.
2. 85mm close, static: the court lady, chin level, eyes down and pleasant, a faint courteous smile — refusal delivered as perfect courtesy, the plain jade rod in her bun.
3. 100mm macro insert, static: the untouched tea cup and the eunuch's hand resting on his knee, the knuckles tightening once, steam thinning.
4. 85mm close, static: the eunuch's face half-lit, a tight careful smile, eyes cold above it, the horsehair cap brim cutting his brow.

STEAM AND FABRIC MOTION — IMPORTANT: physically-based tea steam curling and thinning, the cup surface trembling faintly, sleeve fabric settling, micro-motion only in faces and hands. Do NOT follow the sketch's static lines — the polite fencing must feel like real filmed footage. No raised voices, no anger — courtesy is the weapon here.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 걸음으로 재는 경로 (절대 22.5~30.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP08_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 뒤따름 — 서간 경로를 걸음으로 재는 설화. 무대사 — 경로 자체가 정보. [무음 썬]
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. No other person is followed or confronted in this scene. No violence, no weapon.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm follow shot, smooth: behind the court lady's shoulder as she walks a long empty palace lane at a quiet even pace, low golden afternoon sun stretching long shadows across the stones, lane walls receding into depth.
2. 35mm, static: her silhouette passing a corner where two lanes meet, her eyes flicking once to the turns, counting doors without slowing.
3. 35mm, static, from ahead: her face in half shadow as she passes the lens, pale skin, cold intelligent eyes, the plain jade rod, then past and out of frame — the lane holds the frame after her.

AFTERNOON LIGHT AND DUST MOTION — IMPORTANT: physically-based long shadows moving with her steps, dust drifting in the raking golden light, hanbok skirt swaying with real weight, her pace never changing. Do NOT follow the sketch's static lines — the patient measurement must feel like real filmed footage. No dialogue, no tension music cues — the route itself is the information.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 십 년 전의 눈금 (절대 30.0~37.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP08_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 랙 포커스 — 도장 눈금 매크로. 밀서 내용은 한 줄도 공개하지 않는다(제17~18장 반전 보호). 십 년 전 종이라는 사실의 그림자만. [낮은 확신 · 설화/Neural2-A] "이 눈금 — 소녀가 본 적이 있사옵니다." (rel 3.0=절대 32.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. CRITICAL DOCUMENT GUARD: the aged paper shows only faint illegible aged brush marks, unreadable. The red cinnabar seal impression on it is rendered ONLY as an abstract shape with fine parallel gauge marks etched inside its border — purely geometric lines, NO characters, NO glyphs, NO readable marks, NO hangul, NO hanja anywhere in or around the seal. No violence, no weapon.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: a red cinnabar seal impression on old aged paper under one strong raking window shaft — an abstract geometric shape with fine parallel gauge lines, its border and lines crisp, the surrounding paper a blur of illegible brush marks.
2. 100mm macro, rack focus: the focus pulling from the seal to the court lady's fingertip hovering a hair above the paper, her nail edge sharpening as the seal softens behind — the finger stops, it does not touch.
3. 85mm close, static: her face low over the document, lamplight raking the page, pale porcelain skin, cold intelligent dark eyes narrowed with old memory, the plain jade rod, bare ears, no jewelry — recognition shown as stillness, not shock.

FOCUS AND PAPER MOTION — IMPORTANT: physically-based focus breathing between seal and fingertip, the aged paper grain settling in the raking light, dust drifting through the window shaft, her breath held once and released. Do NOT follow the sketch's static lines — the ten-year shadow must feel like real filmed footage. The letter's content is NEVER shown or read — the gauge mark alone carries the whole reveal.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 삼경의 전언 (절대 37.5~45.0 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP08_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 왕의 밀실 소환 예고, 인수(引手)가 찾아옴. 왕은 미등장 — 전언 세 낱말이 전부다. [단호한 전언 · 내관/Neural2-C] "삼경. 규장각 후각. 혼자." (rel 2.0=절대 39.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the eunuch messenger is a lean middle-aged royal eunuch in a plain grey-blue official court robe and a black horsehair cap, hands folded in braided sleeves, composed unreadable face, no jewelry. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. The king is never shown. The vermilion summons tally stick is plain wood with no writing on it. No violence, no weapon.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm, static: dusk courtyard, the eunuch messenger standing formal at the court lady quarters gate, hands folded, waiting to be noticed, one gate lantern just lit.
2. 85mm close, static: the court lady facing him at a respectful distance, level gaze, unmoved — receiving an order the way one receives weather.
3. 100mm macro insert, static: the eunuch's hand extending a plain wooden vermilion summons tally stick, wood grain in the fading light, her hand receiving it, no writing anywhere.
4. 85mm, static, deep-staged: the eunuch turning away into dusk down the lane, his back framed by gate posts and lane depth, the court lady small behind, unshaken.

DUSK HAZE AND FABRIC MOTION — IMPORTANT: physically-based dusk haze drifting across the courtyard, the fresh lantern glow falloff breathing on the gate posts, sleeves settling after the handover, real body weight in stillness. Do NOT follow the sketch's static lines — the iron courtesy must feel like real filmed footage. No threat, no pressure staging — the summons is three nouns and a departure.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 꺼지는 등불 (절대 45.0~52.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP08_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 복도 끝 등불 한 점이 꺼짐, 갈림길. 무인물 — 연기는 연기가 아닌 불꽃이 한다. [무거운 나레이션 · 내레이션/Wavenet-C] "문이 열리는 밤이 — 두 번째로 왔다." (rel 3.0=절대 47.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no people in frame. A long moonlit wooden gallery corridor, columns repeating into darkness, one small warm lamp cage at the far end. No violence, no weapon.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, static, deep-staged: night, a long corridor with columns receding into darkness, cold moonlight in shafts, one small warm lamp glowing far at the end like a lone star.
2. 24mm ultra-wide, static: the same frame a breath later — the far lamp flame pinching out, the warm dot dying to a thread of smoke, cold moonlight taking the whole gallery.
3. 24mm ultra-wide, static: the corridor empty with the lamp now dark, a faint wisp of smoke rising from its cage, the mouths of two darker crossing corridors visible at the end — a fork in the night.

FLAME AND SMOKE MOTION — IMPORTANT: physically-based flame behaviour — the flame shrinking, bending once, and pinching out; a thin smoke thread rising and dissolving; moonlight shafts holding steady; faint haze drifting. Do NOT follow the sketch's static lines — the dying lamp must feel like real filmed footage. No people, no footsteps, no jump scares — the smoke is the only actor.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 초인문 닫힘 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP08_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 초인문 닫힘 → 암전. **붉은 타이틀(제9화 「밤의 침입자」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the two gatekeepers are distant silhouetted figures pushing a massive wooden gate shut, faces never visible. No weapons, no violence.

Recreate the panels in order as one continuous ~10 second sequence:
1. 50mm, static: night, a massive wooden inner gate seen from inside, two distant silhouetted gatekeepers sliding its heavy bolt home, deep real wood grain under moonlight.
2. 50mm close, static: the bolt seating into its bracket, dust falling from the beam, the final inch of contact shuddering once through the wood.
3. The frame slowly dims — the moonlight thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

GATE AND DUST MOTION — IMPORTANT: physically-based gate wood shuddering as the bolt seats, dust falling from the beam in the moonlight, the door's heavy weight settling, the daylight dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the closing gate must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP08_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 50mm 서가 트래킹 · 발이 겹침 · 내관 앵커 신설 · 설화 원거리 시선 |
| S02 | 07.5~15.0 | 3컷 | EP08_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 매크로 인주 자국 · 손가락 정지(놀람 금지 치환) · 설화 앵커 전면 강제 |
| S03 | 15.0~22.5 | 4컷 | EP08_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 투숏 다과 · 서간 비등장 · 예의=참호(무음 내기) |
| S04 | 22.5~30.0 | 3컷 | EP08_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 35mm 뒤따름 · 무대사 · 경로=정보 · 오후 장화 |
| S05 | 30.0~37.5 | 3컷 | EP08_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 랙 포커스 도장 눈금 · 가독 글자 일체 배제(AG ① 핵심) · 내용 미공개 |
| S06 | 37.5~45.0 | 4컷 | EP08_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 소환 전언 · 왕 미등장 · 내관 복식 고증 · 황혼 랜턴 |
| S07 | 45.0~52.5 | 3컷 | EP08_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 와이드 등불 소등 · 무인물 · 연기(smoke)가 배우 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP08_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 초인문 닫힘 · 엔드카드·타이틀은 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤, Pitch -1.5) | rel 3.0 | 절대 2.0 | 종이는 발이 없어도 다닌다. 누군가 다리를 빌려줄 뿐이다. |
| 2 | S02 | 설화 `ko-KR-Neural2-A` (서늘한 발견 속마음, Pitch -1.0) | rel 3.0 | 절대 9.5 | 인주가 아직 마르지 않았어. |
| 3 | S03 | 설화 `ko-KR-Neural2-A` (절제된 응대, Pitch -1.0) | rel 5.0 | 절대 19.5 | 서간은 마마께만 가나이다. |
| 4 | S03 | 내관 `ko-KR-Neural2-C` (긴장한 무거움, Pitch -0.5) | rel 6.0 | 절대 20.5 | …나인은 보는 눈이 많구나. |
| 5 | S05 | 설화 `ko-KR-Neural2-A` (낮은 확신, Pitch -1.0) | rel 3.0 | 절대 32.0 | 이 눈금 — 소녀가 본 적이 있사옵니다. |
| 6 | S06 | 내관 `ko-KR-Neural2-C` (단호한 전언, Pitch -0.5) | rel 2.0 | 절대 39.0 | 삼경. 규장각 후각. 혼자. |
| 7 | S07 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤, Pitch -1.5) | rel 3.0 | 절대 47.5 | 문이 열리는 밤이 — 두 번째로 왔다. |
| 8 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제9화 「밤의 침입자」에서 계속 |

- S04는 무대사 썬 — 보이스·자막 블록 없음. 경로 자체가 정보이므로 자막 공백(00:22~00:30)은 침묵 연출 그대로 둔다.
- 내레이션 보이스 ID는 시리즈 내레이션 선례(EP06 원장 `ko-KR-Wavenet-C` 다큐 톤, Pitch -1.5)를 준용했다. 내관은 EP08 신규 조연으로 `ko-KR-Neural2-C`(왕 이환과 동일 ID) — 감정 톤 지문(긴장한 무거움/단호한 전언)으로 배역을 구분한다(조연 보이스 원장 총칙 준용).
- S03 3·4번 행: 정본 썬표는 두 대사를 한 행(rel 5.0=절대 19.5)으로만 표기 — EP07 S07 선행례와 같이 설화(rel 5.0=19.5, 정본 표기 그대로)와 내관(rel 6.0=20.5, 보조 배분)으로 분할했다. 믹싱 시 정본 수치를 우선하되 싱크가 어긋나면 편집 단계에서 보정한다.

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,500
종이는 발이 없어도 다닌다.
누군가 다리를 빌려줄 뿐이다.

2
00:00:09,500 --> 00:00:11,500
인주가 아직 마르지 않았어.

3
00:00:19,500 --> 00:00:21,000
서간은 마마께만 가나이다.

4
00:00:20,500 --> 00:00:22,000
…나인은 보는 눈이 많구나.

5
00:00:32,000 --> 00:00:34,500
이 눈금 —
소녀가 본 적이 있사옵니다.

6
00:00:39,000 --> 00:00:40,000
삼경. 규장각 후각. 혼자.

7
00:00:47,500 --> 00:00:50,000
문이 열리는 밤이 —
두 번째로 왔다.

8
00:00:59,000 --> 00:01:00,000
제9화 「밤의 침입자」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S03 3·4번 자막은 설화 대사(19.5)와 내관 대답(20.5)이 겹치지 않게 19.5~21.0 / 20.5~22.0 중 20.5 교차점에서 0.5초 여백을 둔다 — 실제 믹싱 길이에 맞춰 편집 단계에서 확정한다.
- S05 "이 눈금 — 소녀가 본 적이 있사옵니다."는 정본 그대로 두었으나, 설화가 왕에게 아뢰는 대사가 아닌 속마음 자막이므로 믹싱 시 톤 지문(낮은 확신)을 우선한다.
- 보이스 ID 운용: 내관=왕=서 상궁 계열과 동일 ID(`Neural2-C`) 축은 조연 보이스 원장 총칙에 따라 감정 톤 지문으로만 구분한다.
