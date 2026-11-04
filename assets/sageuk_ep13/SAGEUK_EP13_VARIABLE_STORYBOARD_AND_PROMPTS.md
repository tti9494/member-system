# 「혈화의 궐」 EP13 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제13화 「후궁의 등장」 썬표(행 255~274) + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP12 원장 운용 결과
> **범위**: EP13 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 **후궁 등장이 중전의 귀(耳)를 무너뜨리는 정치적 균열**이다. **후궁 로맨스 떡밥 전면 금지(AG 정본 치환)**: 귀인 정씨는 애정·질투의 대상이 아니라 **중전 견제 전선의 새 변수**로만 기능하며, 설화와의 첫 대면도 로맨스가 아닌 **상호 측정**의 그림이다(`no romance, no flirtation, no seduction, no jealousy over a man`). **"세상 모든 것을 갖고도 부족한 여자" 식 서술 금지** — 감정은 대사가 아닌 행동(떨잠을 고르다 멈추는 손, 찻잔을 누르는 손)으로만 보인다. **자식 떡밥 절대 금지**: 시즌2 혈통 소문의 충격을 위해 본 화는 아이·후사·출산 관련 언급·소품·시선을 **한 건도** 두지 않는다(`no child, no pregnancy, no heir reference in any frame`). **중전-귀인 동일 보이스 ID(Neural2-B) 이중 배역** — 트랙 분리 합성과 파일명 규칙(`EP13_S2_QUEEN` / `EP13_S3_CONSORT`)·피치 차등(중전 0.0 서늘함 / 귀인 +0.5 부드러움)으로 혼동을 차단한다(정본 AG 검수 ⑦). **무흉기·무폭력 화**: 전 썬 무기 미등장, 신체 접촉은 S05의 **소매 자락 스침** 하나뿐이며 붙잡기·밀치기·고성 일절 없다. **귀인 정씨 고정 외형 앵커 신설(AG ⑥)**: `characters.md` 미등록 신규 인물이므로 본 원장 §0-7에 고정 시각 프롬프트를 등록해 전 썬 동일 문구로 투입한다.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **행렬·징**(palanquin swaying with real load on the bearers' shoulders, banner cloth lifting in the wind, stone dust under feet, the bronze gong's rim still vibrating), S02 **거울·떨잠**(true parallax inside the bronze mirror, dangling ornaments settling with pendulum weight, the stopped hand with real tendon tension), S03 **직물·눈**(silk sleeves settling after each small movement, measured breathing, eye lines travelling with real micro-saccades), S04 **종이·초저녁**(paper fiber flattening under an old hand, dusk light dying in the yard, the kneeling weight far off in true perspective), S05 **회랑·소매**(cloth-on-cloth resistance as sleeve hems brush, floorboards and pillars sliding past with real parallax, long dusk shadows on the boards), S06 **등불·그림자**(lantern flame breathing, the shadow edge creeping across her face, one reflected flame moving inside the iris), S07 **찻잔·도자기**(porcelain flexing under real thumb pressure, the hairline crack creeping grain by grain, the tea surface trembling), S08 **파편·액체**(two ceramic halves rocking to rest with true weight, tea spreading with real surface tension and pooling). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기·상해·폭력 일체 없음. 본 화는 **무흉기 화**다 — 궁정의 압력은 손과 시선으로만 작동한다. **폭력·접촉 차단**: `no violence, no weapon, no grabbing, no shoving, no slapping, no shouting` 전 썬 명시. S05의 유일한 접촉은 **소매 자락이 스치는 것**으로 한정하고, S02·S07의 손은 물건(떨잠·찻잔)에만 닿는다. **로맨스 떡밥 차단**: `no romance, no flirtation, no seduction, no romantic tension, no jealousy over a man` — 두 여자의 대면은 측정과 견제다. **자식 떡밥 차단**: `no child, no pregnancy, no heir, no baby — nothing of the kind in frame`. **설명 대사·정치 해설 차단**: `no exposition speeches, no political commentary spoken aloud` — 균열은 그림으로만 보인다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07~EP12 재발 방지: 설화 앵커의 **귀걸이·수술·가체·떨잠 금지 전 썬 상향 고정** 유지. EP13 신설: **귀인 정씨 고정 외형 앵커** — 본 화 신규 인물로 `characters.md` 미등록이므로 본 원장에서 신설 등록, S01·S03·S05 전 등장 썬에 동일 문구 투입. 소품 무문자 지문을 패널 서술 안에서도 반복 기입.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **중전(윤소혜)**: a 22-year-old Joseon queen, deep red court dangui, tall elaborate gache hair with lavish tteoljam dangling ornaments and a cheopji, proud cold beautiful face, dignity and a cold fury held perfectly still — she never raises her voice
   - **귀인 정씨(신설 조연 앵커)**: the newly entered royal consort, a young Korean noblewoman, soft gentle features with a hidden ambitious glint behind the eyes, neat low chignon with a single modest cheopji, muted jade-green and pale rose dangui, restrained ornament only — no heavy gache, no lavish dangling ornaments — the same woman in every scene
   - **윤경헌**: a 58-year-old Joseon prime minister (fictional court minister Yoon Gyeong-heon), dark crimson danryeong official court robe with rank embroidery, black horsehair samo official hat, thin gray beard, cold suspicious hawk eyes, deep wrinkles of power — his menace is a quiet satisfaction only, no shouting, no threats
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제14화 「독의 초승달」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 찻잔 파손 → 완전 암전 유지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01 `late-afternoon natural sunlight raking across the outer gate courtyard, no lamps`, S02 `one window's daylight crossed with a single oil lamp in the queen's chamber`, S03 `soft daylight through the corridor lattice, both faces fully readable`, S04 `dusk afterglow dying in the yard, lamplight inside the sarangchae`, S05 `dusk light through the corridor lattice, the first lanterns just lit`, S06 `a single corridor lantern, shadow winning the rest`, S07 `candlelight on the hand, half the face in shadow`, S08 `the same candle burning low, then darkness`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수 + EP10~EP12 관찰 메모 반영)**: S04의 접힌 보고 종이, 회랑·전각의 현판·휘장 등 모든 소품 문서·간판은 `blank paper texture, no letters, no glyphs, no readable marks`, `blank wood plaque, no characters` — **패널 서술 안에서도 반복 기입**한다(EP12 S03 현판 글리프 결함 재발 방지). EP13은 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦)**: **중전과 귀인 정씨가 모두 `ko-KR-Neural2-B`**다. EP13은 이 화에서 처음으로 두 배역이 같은 썬 축에 동시 등장한다. 혼동 차단 4중 장치를 강제한다 — ① 중전·귀인 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 중전 `EP13_S2_QUEEN`·`EP13_S7_QUEEN`, 귀인 `EP13_S3_CONSORT`, ③ **피치 차등을 매 행 강제 표기**: 중전 `Pitch 0.0`(서늘하고 가라앉은 위협) / 귀인 `+0.5`(부드럽게 파고드는 가시), ④ 믹싱 단계에서 Pitch·톤 축 확인(중전 0.0 → 귀인 +0.5의 상승 폭이 0.5 이상 벌어졌는지 실측). 하나라도 누락되면 재합성한다.

---

## 1. S01 새 귀 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP13_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 입궁 행렬 — 귀인 정씨의 행렬이 궁의 정문을 삼킨다. 징소리 두 번. [무거운 나레이션 · 내레이션/Wavenet-C] "궁에는 새 귀가 들어왔다. 그러나 소리는 중궁전이 먼저 냈다." (rel 3.5=절대 2.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the newly entered royal consort, a young Korean noblewoman, soft gentle features with a hidden ambitious glint behind the eyes, neat low chignon with a single modest cheopji, muted jade-green and pale rose dangui, restrained ornament only — no heavy gache, no lavish dangling ornaments. Palace maids and bearers in plain neat court dress with plain hair. No queen on screen, no king on screen, no royal figure other than the consort. No violence, no weapon, no physical contact.

LIGHT GUARD — IMPORTANT: late-afternoon natural sunlight raking across the outer gate courtyard, no lamps. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is an arrival, not a celebration: no romance, no flirtation, no wonder, no crowd cheering.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm crane down, wide: a long consort's entrance procession winding through a vast palace outer gate in late-afternoon sun — palanquin, banners, a column of maids.
2. 50mm tracking, side: the procession moving past camera, the new consort glimpsed behind a lifted palanquin curtain, calm and unreadable.
3. 100mm macro, static: a bronze gong struck once with a padded mallet, the metal rim still vibrating, no other figure in frame.
4. 135mm compressed, static: far across stacked palace roofs a single dark hall window, empty of figures — the second stroke belongs to another building.

PALANQUIN AND GONG MOTION — IMPORTANT: physically-based palanquin swaying with real load on the bearers' shoulders, banner cloth lifting in the wind, stone dust under feet, the bronze rim still quivering after the strike. Do NOT follow the sketch's static lines — the procession must feel like real filmed footage. No triumph, no spectacle music staging — an administrative arrival that happens to be a political event.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 멈춘 손 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP13_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 로우앵글 — 중전이 징소리를 듣고, 떨잠을 고르는 손이 멈춘다. [가라앉은 위협 · 중전/Neural2-B, Pitch 0.0] "징은 한 번이면 된다." (rel 2.5=절대 9.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the queen is a 22-year-old Joseon queen, deep red court dangui, tall elaborate gache hair with lavish tteoljam dangling ornaments and a cheopji, proud cold beautiful face, dignity and a cold fury held perfectly still — she never raises her voice, and no jealousy over a man ever crosses her face. One maid's hands only at the frame edge. No consort in this scene, no king on screen. No violence, no weapon, no physical contact.

LIGHT GUARD — IMPORTANT: one window's daylight crossed with a single oil lamp in the queen's chamber. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The sound arrives before the anger does: no rage yet, only a hand betraying her.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm low angle, static: the queen seated before a bronze dressing mirror, red dangui, tall gache, the dangling ornaments still swinging after her movement.
2. 100mm macro, static: her fingers frozen above an open box of gold tteoljam ornaments — stopped in mid-air, the hand alone carrying the alarm.
3. 85mm close, slow push-in: a fraction of her face turning toward the door, cold and unsurprised, the mouth closed.

MIRROR AND ORNAMENT MOTION — IMPORTANT: physically-based true parallax inside the bronze mirror, dangling ornaments settling with real pendulum weight, the stopped hand holding real tendon tension. Do NOT follow the sketch's static lines — the interruption must feel like real filmed footage. No thrown box, no snapped command — a stopped hand and a still face do all the work.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 첫 마주 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP13_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 투숏 — 귀인 정씨와 설화의 첫 마주. 서로를 헤아리는 눈. [부드럽게 파고드는 가시 · 귀인/Neural2-B, Pitch +0.5] "당신 눈은… 궁녀의 눈이 아닌 것 같은데." / [거짓 평온 · 설화/Neural2-A] "나인의 눈이오니, 마마께서는 처음 보셨을 뿐이지요." (rel 5.5=절대 19.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the newly entered royal consort, a young Korean noblewoman, soft gentle features with a hidden ambitious glint behind the eyes, neat low chignon with a single modest cheopji, muted jade-green and pale rose dangui, restrained ornament only — no heavy gache, no lavish dangling ornaments. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. Two maids waiting far behind, plain dress. No queen in this scene, no king on screen. No violence, no weapon, no physical contact — they never touch.

LIGHT GUARD — IMPORTANT: soft daylight through the corridor lattice, both faces fully readable, neither woman shadowed into anonymity. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is appraisal, not attraction: no romance, no flirtation, no romantic spark, no exchanged smiles of warmth.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm, static two-shot: a wooden palace corridor, the consort and the court lady facing each other at speaking distance, two maids held far back.
2. 85mm close, static: the consort's soft face — a small polite smile that is doing arithmetic, eyes travelling over the other woman's face.
3. 85mm close, static: the court lady's head slightly bowed but eyes lifting just enough to answer, bare ears, one plain jade pin.
4. 100mm macro, rack focus: the plain jade hairpin sharp in front, the consort's jewelled cheopji dissolving soft behind it — blank surfaces only, no letters, no glyphs.

SILK AND EYE-LINE MOTION — IMPORTANT: physically-based silk sleeves settling after each small movement, measured breathing, eye lines travelling with real micro-saccades. Do NOT follow the sketch's static lines — the first meeting must feel like real filmed footage. No romantic framing, no soft-focus glamour — two minds taking each other's measure in plain daylight.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 쓸만한 균열 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP13_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 — 사랑채, 윤경헌이 귀인 입궁 보고를 읽는다. [낮게 깔린 냉소 · 윤경헌/Wavenet-D] "조카따위가 징을 울리게 뒀는가. …쓸만한 균열이로군." (rel 3.5=절대 25.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the minister is a 58-year-old Joseon prime minister (fictional court minister Yoon Gyeong-heon), dark crimson danryeong official court robe with rank embroidery, black horsehair samo official hat, thin gray beard, cold suspicious hawk eyes, deep wrinkles of power — his menace is a quiet satisfaction only, no shouting, no threats, no gestures. A servant kneeling in the yard, plain dress, unremarkable face, far from camera. No queen, no consort, no king on screen. No violence, no weapon.

LIGHT GUARD — IMPORTANT: dusk afterglow dying in the yard, warm lamplight inside the sarangchae room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. He is not gloating — he is a carpenter who has just found a usable piece of wood.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 135mm compressed telephoto, static: across the sarangchae yard at dusk, a servant kneeling small and distant before the lamplit room where the old minister sits, roof lines stacking the distance between them.
2. 100mm macro, static: his aged hand flattening a folded paper report on the low desk — blank paper texture, no letters, no glyphs, no readable marks anywhere.
3. 85mm close, slow push-in: his eyes lifting from the paper, an ancient cold smile settling, no shouting, no gesture.

PAPER AND DUSK MOTION — IMPORTANT: physically-based paper fiber flattening under an old hand, the dusk light dying in the yard, the kneeling weight far off in true compressed perspective. Do NOT follow the sketch's static lines — the reading of the report must feel like real filmed footage. No gleeful laugh, no fist on the table — a quiet appraisal of a crack he did not create.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 어긋나는 소매 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP13_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 회랑 — 중전과 귀인이 회랑에서 어긋난다. 등짝 시선 전투. **무대사 — 두 여자의 소매 자락만 스친다.** (렌더 무성 · 대사 자막 없음)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the queen is a 22-year-old Joseon queen, deep red court dangui, tall elaborate gache hair with lavish tteoljam dangling ornaments and a cheopji, proud cold beautiful face, head held level — she never raises her voice and never glares openly. The newly entered royal consort, a young Korean noblewoman, soft gentle features with a hidden ambitious glint, neat low chignon with a single modest cheopji, muted jade-green and pale rose dangui, restrained ornament only. No court lady in this scene, no king on screen. No violence, no weapon, no grabbing, no shoving — the only contact is sleeve fabric brushing sleeve fabric.

LIGHT GUARD — IMPORTANT: dusk light through the corridor lattice, the first lanterns just lit, long shadows laid along the floorboards. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is a passing, not a confrontation: no glaring, no stopping, no turning to face each other.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static, symmetrical: a long wooden palace corridor, the queen entering from the far end and the consort from the near end, walking toward each other.
2. 50mm, static: they pass at close quarters, only their wide sleeve hems touching as they pass, both faces held forward, neither stopping.
3. 85mm over-shoulder from behind the queen: her back to camera walking away, head level, eyes sliding sideways, nothing else moving.
4. 85mm, static, from behind the consort: her back to camera, her chin turning a fraction toward the other woman, measured, then still.

CORRIDOR AND SLEEVE MOTION — IMPORTANT: physically-based cloth-on-cloth resistance as the sleeve hems brush, floorboards and pillars sliding past with real parallax, long dusk shadows on the boards, both women's strides with real body weight. Do NOT follow the sketch's static lines — the passing must feel like real filmed footage. No glaring, no shoulder check, no hissed whisper — backs that refuse to turn are the whole scene.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 계산하는 눈 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP13_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 설화가 이 틈을 계산하는 눈. [서늘한 계산 속마음 · 설화/Neural2-A] "균열은 — 쓰기 나름이지요." (rel 3.0=절대 39.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. Two distant figures walk away in the far background, faces not visible. No queen close to camera, no king on screen. No violence, no weapon.

LIGHT GUARD — IMPORTANT: a single corridor lantern, shadow winning the rest of the corridor. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. She does not smile and does not explain herself — the arithmetic happens behind the eye and nowhere else.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm wide, static: the long corridor, the court lady alone at the far end, small between heavy pillars, watching two distant women walk away.
2. 85mm close, static: her face turning half into shadow, eyes narrowing in quiet thought, absolutely no smile.
3. 100mm macro, static: one dark eye, a corridor lantern reflected small inside the iris, the lid not moving.

LANTERN AND SHADOW MOTION — IMPORTANT: physically-based lantern flame breathing, the shadow edge creeping across her face, one reflected flame shifting inside the iris, her stillness with real body weight. Do NOT follow the sketch's static lines — the calculation must feel like real filmed footage. No smirk, no whispered plan, no villain's glow — only an eye doing sums.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 찻잔을 누르는 손 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP13_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 중전의 손. 찻잔이 갈라지기 직전까지 눌린다. [억누른 격노 · 중전/Neural2-B, Pitch 0.0] "홍화. 그놈의 눈 — 언제부터였느냐." (rel 3.5=절대 47.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the queen is a 22-year-old Joseon queen, deep red court dangui, tall elaborate gache hair with lavish tteoljam dangling ornaments and a cheopji, proud cold beautiful face, the fury kept entirely behind the eyes, mouth closed — she never raises her voice. No other face in frame. No violence, no weapon, no blood — the cup is pressed, not struck.

LIGHT GUARD — IMPORTANT: candlelight on the hand, half the face in shadow, the room otherwise dark but readable. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Anger here is compression, not explosion: nothing is thrown and nothing breaks yet.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a pale hand pressed flat on a white porcelain tea cup on a lacquered table, knuckles pale under the pressure.
2. 100mm macro, slow: a hairline crack opening along the cup's rim beneath her thumb, the crack creeping grain by grain.
3. 85mm close, static: her face perfectly still, eyes fixed forward, the fury entirely behind the eyes, the mouth not opening.

PORCELAIN AND CANDLE MOTION — IMPORTANT: physically-based porcelain flexing under real thumb pressure, the hairline crack creeping, the tea surface trembling from the pressure wave, the candle flame steady. Do NOT follow the sketch's static lines — the pressure must feel like real filmed footage. No shout, no thrown cup, no snapped command — the hand does the shouting.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 갈라진 찻잔 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP13_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 갈라진 찻잔 → 암전 → 타이틀. **붉은 타이틀(제14화 「독의 초승달」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations and real objects.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — objects only, no face in frame, no hands in frame at the end. No violence, no weapon, no blood — this is a cup giving way under pressure, nothing living is harmed.

DYING LIGHT GUARD — IMPORTANT: the same candle burning low on the table, then darkness gathering. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no final line, no music sting staging.

Recreate the panels in order as one continuous ~10 second sequence:
1. 50mm, static: the porcelain tea cup parting in two on a black lacquer table, dark tea spreading across the surface in a thin sheet.
2. 100mm macro, static: the two halves rocking to rest, tea pooling in the split between them, the candle light steady on the glaze.
3. The frame slowly dims — the candle light thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

CERAMIC AND LIQUID MOTION — IMPORTANT: physically-based ceramic halves rocking to rest with true weight, tea spreading with real surface tension and pooling, the candle flame dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the quiet after the sound must feel like real filmed footage. No slow-motion gush, no dramatic score — a cup that finally gave way.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP13_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 24mm 크레인다운 · 입궁 행렬 · 징 두 번 · 로맨스 0 |
| S02 | 07.5~15.0 | 3컷 | EP13_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 로우앵글 · 멈춘 떨잠 손 · 격노 유예 |
| S03 | 15.0~22.5 | 4컷 | EP13_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 50mm 투숏 · 상호 측정 · 로맨스/접촉 0 |
| S04 | 22.5~30.0 | 3컷 | EP13_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 135mm 압축 · 무문자 보고 종이 · 냉소 |
| S05 | 30.0~37.5 | 4컷 | EP13_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 35mm 회랑 · 소매 스침 · 무대사 · 눈싸움 0 |
| S06 | 37.5~45.0 | 3컷 | EP13_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 계산하는 눈 · 설화 단독 · 미소 0 |
| S07 | 45.0~52.5 | 3컷 | EP13_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 매크로 · 눌린 찻잔 · 고성 0 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP13_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 찻잔 파손·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤) | rel 3.5 | 절대 2.5 | 궁에는 새 귀가 들어왔다. 그러나 소리는 중궁전이 먼저 냈다. |
| 2 | S02 | 중전 `ko-KR-Neural2-B` (가라앉은 위협, Pitch 0.0) | rel 2.5 | 절대 9.0 | 징은 한 번이면 된다. |
| 3 | S03 | 귀인 정씨 `ko-KR-Neural2-B` (부드럽게 파고드는 가시, Pitch +0.5) | rel 5.5 | 절대 19.5 | 당신 눈은… 궁녀의 눈이 아닌 것 같은데. |
| 4 | S03 | 설화 `ko-KR-Neural2-A` (거짓 평온, Pitch -1.0) | rel 5.5 | 절대 21.8 | 나인의 눈이오니, 마마께서는 처음 보셨을 뿐이지요. |
| 5 | S04 | 윤경헌 `ko-KR-Wavenet-D` (낮게 깔린 냉소, Pitch -2.5, Speed 0.9) | rel 3.5 | 절대 25.0 | 조카따위가 징을 울리게 뒀는가. …쓸만한 균열이로군. |
| 6 | S05 | (무대사 · 무성) | — | — | 두 여자의 소매 자락만 스침 — 자막 없음 |
| 7 | S06 | 설화 `ko-KR-Neural2-A` (서늘한 계산 속마음, Pitch -1.0) | rel 3.0 | 절대 39.5 | 균열은 — 쓰기 나름이지요. |
| 8 | S07 | 중전 `ko-KR-Neural2-B` (억누른 격노, Pitch 0.0) | rel 3.5 | 절대 47.5 | 홍화. 그놈의 눈 — 언제부터였느냐. |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제14화 「독의 초승달」에서 계속 |

- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: **중전과 귀인 정씨가 동일 축 `ko-KR-Neural2-B`**이며, EP13은 이 두 배역이 **한 화에 동시 등장하는 첫 화**다. 혼동 차단 4중 장치를 강제한다 — ① 중전·귀인 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 중전 `EP13_S2_QUEEN`·`EP13_S7_QUEEN`, 귀인 `EP13_S3_CONSORT`, ③ **피치 차등 매 행 강제 표기**(중전 Pitch 0.0 서늘함 / 귀인 Pitch +0.5 부드러움 — 본 표 2·3·8번 행), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인(두 트랙의 피치 차가 0.5 이상 벌어졌는지, 중전은 가라앉고 귀인은 얹히는지). 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 내레이션 `Wavenet-C`는 본 화에서 무결이 미등장하므로 충돌 배역이 없다(S01 내레이션 단독). 설화 `Neural2-A`는 본 화 내 유일 배역으로 충돌 없음.
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 중전 `Neural2-B`(Pitch 0.0), 윤경헌 `Wavenet-D`(Pitch -2.5, Speed 0.9), 내레이션 `Wavenet-C`(다큐 톤). 귀인 정씨는 신설 조연 — §0-7 시각 앵커와 짝을 이루는 음성 지문(`Neural2-B`, Pitch +0.5)을 본 원장에서 확정한다.
- S03은 한 썬 안에서 **귀인 → 설화 순차 발화**다(정본 rel 5.5 단일 표기). 두 화자를 자막·보이스 모두 분리 블록으로 쪼개고, 설화의 대답은 컷 경계(22.5)를 넘겨 S04 헤드까지 이월시킨다(25.0 윤경헌 대사와 충돌 없음). 컷을 넘는 대답은 편집 리듬상 의도된 설계다.
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(마스터 각본 제13화 썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,500 --> 00:00:07,000
궁에는 새 귀가 들어왔다.
그러나 소리는 중궁전이 먼저 냈다.

2
00:00:09,000 --> 00:00:11,000
징은 한 번이면 된다.

3
00:00:19,500 --> 00:00:21,800
당신 눈은… 궁녀의 눈이
아닌 것 같은데.

4
00:00:21,800 --> 00:00:24,600
나인의 눈이오니, 마마께서는
처음 보셨을 뿐이지요.

5
00:00:25,000 --> 00:00:28,500
조카따위가 징을 울리게 뒀는가.
…쓸만한 균열이로군.

6
00:00:39,500 --> 00:00:42,000
균열은 — 쓰기 나름이지요.

7
00:00:47,500 --> 00:00:50,500
홍화. 그놈의 눈 —
언제부터였느냐.

8
00:00:59,000 --> 00:01:00,000
제14화 「독의 초승달」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- 3·4번 블록(귀인→설화)은 한 썬 안의 연속 발화 — 자막 사이 간격 없이 붙여 두 화자의 대화 리듬을 보존한다. 화자가 바뀌므로 자막 파일은 `EP13_S3_CONSORT` / `EP13_S3_SEOLHWA`로 분리 저장한다.
- 5번 블록(윤경헌)은 한 호흡 두 문장 — 중간 줄바꿈에서 끊되 노트의 냉소가 이어지도록 28.5까지 노출한다.
- 2·7·8번 블록은 모두 중전 `Neural2-B`다 — 파일명 규칙(`EP13_S2_QUEEN`/`EP13_S7_QUEEN`)으로 트랙을 분리하고 피치 0.0을 동일 적용한다(§0-12).
- 보이스 ID 운용: 고정 ID + 감정 톤 지문(무거운 나레이션/가라앉은 위협/부드럽게 파고드는 가시/거짓 평온/낮게 깔린 냉소/서늘한 계산 속마음/억누른 격노)으로 썬별 미묘함을 구분한다.
