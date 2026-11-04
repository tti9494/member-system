# 「혈화의 궐」 EP10 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제10화 「옥사의 그림자」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP09 원장 운용 결과
> **범위**: EP10 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 옥사 기록 열람극이다. **회상 플래시뱅크 나열 금지** — 빠진 페이지의 부재는 도려진 자국·먼지·손끝 감촉으로만 보인다(정본 안티슬롭 치환). 밀서의 실체는 다루지 않는다 — 본 화는 **페이지 누락의 흔적만** 다루고, 밀서 실체는 EP18로 완전 이동(비판 검수 확정). 슬롭 명언("진실은 반드시 드러나는 법"류) 일체 금지 — 설화의 대사는 단정 없는 사실 나열이다. 기록관은 자객이 아니라 **자책 어린 늦은 고백자**다 — 협박·위협·흉기 일체 없음. EP08 규장각 동세트 슬롭 회피: 서가 종심 대신 **열람 탁자 상면 구도**로 통일(① AG 검수).

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **촛불·먼지**(candle flame breathing, dust drifting through the halo), S02 **종이·페이지 넘김**(paper flexing with real weight, dust lifting from the gutter), S03 **등불·옷자락**(lantern glow bobbing with his steps, robe settling), S04 **문·접은 종이**(door easing shut, folded page crispness), S05 **촛불·먹 질감**(candlelight flickering on paper fibers, woodblock ink relief), S06 **새벽 전 정적**(thin haze over the roofs, last flame guttering), S07 **기둥 그늘·소매**(pillar shadows passing, sleeve fabric settling, scabbard sway), S08 **소매 수납·암전**(sleeve fabric swallowing the page, light dying smoothly). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·상해·직접 대치 일체 없음. 기록관은 무기 미소지, 접촉 없이 페이지를 내민다. 몰래 건네기는 자발적 고백이지 공갈이 아니다 — 위협 톤 연기 금지. **서사 오독 차단**: 기록관과 설화가 로맨스로 오독되지 않게 전 썬 `no intimacy, formal distance held`를 명시한다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07·EP09 결함 재발 방지: 설화 앵커에 **귀걸이·수술·가체·입가리개 금지를 전 썬 상향 고정**, `smooth jade rod with no carved head` 유지.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok
   - **기록관**: a weary 50-year-old Joseon records keeper, plain dark official robe, black horsehair official hat, deep lines of duty and guilt, self-reproaching careful eyes — no weapon, no ornaments
   - **강무결**(S07): a 25-year-old Joseon warrior captain, tall, dark navy and black military robe (yungbok), a faint scar across the cheekbone, sharp heavy calm eyes — sword stays sheathed, no violence
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제11화 「상궁의 발탁」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 페이지의 소매 수납 → 서서히 어두워지는 암전까지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수 — 열람실 야간 안티슬롭 핵심)**: S01~S05는 **단일 촛불 썬**이다. 키 라이트 모티베이션 필수 — S01 `a single candle on the reading table only`, S02 `the same single candle, page glow`, S03 `the candle plus one small hooded lantern on the newcomer`, S04 `the candle only, the lantern dying by the door`, S05 `the candle low, flame close to the paper`, S06 `pre-dawn grey ambient, a last guttering candle`, S07 `cool pre-dawn ambient along the corridor`, S08 `cool pre-dawn ambient, then the light dying`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 볼륨·페이지·액자 등 모든 소품 문서는 `blank paper texture, no letters, no glyphs, no readable marks`. 유일한 예외는 S05의 **목판 인쇄 한자 두 글자 시상(施賞)** 인서트다 — 렌더 시 프롬프트에 두 글자의 자형을 정확히 지정하고, 검수에서 글자 왜곡이 관측되면 해당 컷을 재렌더하거나 편집 단계에서 매크로 먹물 필치 인서트로 대체한다(정본 허용 경로). 그 외 가독 정보는 편집 자막으로만 처리한다(한글 왜곡 슬롭 근원 차단).
12. **복식 고증**: 기록관은 소박한 관복·흑립 규격을 벗어나지 않고, 무결은 남색 융복·뺨 흉터·환도 칼집으로 통일한다. 관복·군복의 과장 금지. 설화의 옥비녀는 전 썬 수술 없는 매끈한 단일 옥대.

---

## 1. S01 읽히지 않은 기록 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP10_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 열람실 와이드 — 심야 규장각, 혼자 앉은 설화와 촛불 하나. 서가 종심 대신 열람 탁자 상면 구도로 EP08 동세트를 회피한다. [무거운 나레이션 · 내레이션/Wavenet-C] "십 년 전의 기록은, 십 년 동안 누군가에게 읽히지 않았다." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no elaborate hair ornaments — elegant dark pastel hanbok. No other person in this scene. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: the royal archive at midnight is lit ONLY by a single candle on the reading table. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Composition sits on the reading table top — do NOT stage deep bookshelf corridors.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, slow push-in, static height: a vast dark royal archive reading room, the young woman seated alone at a large reading table with one candle, bound record volumes stacked around her, the tabletop composition filling the frame.
2. 85mm close, static: the candle flame and half of her face lit by it, thin dust motes drifting through the warm halo, her cold eyes lowered to the volume.
3. 100mm macro insert, static: her fingertips resting on the closed record volume, a thin film of dust on the blank cover — a book untouched for ten years, blank paper texture, no letters, no glyphs.

CANDLE AND DUST MOTION — IMPORTANT: physically-based candle flame breathing and bending, dust drifting through the light halo, the dust film disturbing faintly under her fingertips, her stillness with real body weight. Do NOT follow the sketch's static lines — ten years of unread silence must feel like real filmed footage. No ghost staging, no creaking doors — the scene is quiet work, not horror.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 도려진 자국 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP10_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 페이지 넘김 — 옥사 공초 페이지, 몇 장이 도려진 자국. 회상 플래시뱅크 대신 부재의 물성(자국·먼지)으로 삭제를 보인다. [서늘한 확신 · 설화/Neural2-A] "도려내는 데는 서관 한 명, 밤 하나면 족하지요." (rel 4.0=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No other person in this scene. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: the same single candle lights the work, its glow falling across the open volume. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. All page surfaces stay blank paper texture — no letters, no glyphs, no readable marks; the crime reads through the cut marks, not through text.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: her bare fingers carefully turning a page of the bound draft record, candlelight warm on the paper edge.
2. 100mm macro, static: the binding revealed — ragged knife-cut paper stubs where pages were sliced out long ago, the cut edges crisp and deliberate.
3. 85mm close, static: her cold intelligent eyes narrowing at the gaps in the record, the candle flame reflected small in her iris.
4. 50mm over-shoulder, static: the open volume across her hands, a row of missing page stubs running along the spine, darkness folded beyond the table.

PAPER AND DUST MOTION — IMPORTANT: physically-based paper flexing with real weight as the page turns, dust lifting from the gutter of the binding, the stub edges catching the candlelight, her fingers unhurried and precise. Do NOT follow the sketch's static lines — the absence must feel physical, like real filmed footage. No flashback montage, no vision effects — absence is shown by touch and dust only.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 누구의 뜻인가 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP10_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 기록관이 찾아와 누구의 뜻인지 물음. 두 사람 모두 탁자를 사이에 두고 격식 거리를 유지한다. [무게 있게 절제 · 기록관/Neural2-C] "몇 장 빠져 있소. 마마는 그것을 알아 무엇에 쓰시려우." (rel 3.5=절대 17.0) / [거짓 평온 · 설화/Neural2-A] "빠진 것을 헤아리는 것이 사헌부의 일이었나이다." (rel 6.0=절대 19.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the records keeper is a weary 50-year-old Joseon official clerk, plain dark official robe, black horsehair official hat, deep lines of duty and guilt, self-reproaching careful eyes — no weapon, no ornaments. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: the candle on the reading table plus one small hooded lantern carried by the newcomer are the only lights. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is an interrogation of intent, not a romance: no intimacy, formal distance held, the table always between them.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the archive door easing open, the middle-aged records keeper entering with a small hooded lantern, the young woman seated far away at the reading table with her single candle, the vast dark room between them.
2. 85mm, static: the clerk standing at the near end of the table while the woman stays seated, formal distance held, stacked volumes between them.
3. 85mm close, static: the clerk's wary testing face, deep lines of duty and guilt, his eyes probing her for the truth.
4. 85mm close, static: the young woman's face in false calm, level eyes, candlelight on one cheek, nothing moving in her expression.

LANTERN AND STILLNESS MOTION — IMPORTANT: physically-based lantern glow bobbing faintly with his steps, the hooded light steadying as he sets it down, robe fabric settling, her absolutely controlled breath. Do NOT follow the sketch's static lines — the measured exchange must feel like real filmed footage. No raised voices, no looming, no threat staging — the pressure lives in the questions, not the bodies.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 늦은 사람의 자비 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP10_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 기다림 — 기록관이 소리 없이 돌아간다. 이윽고 문 앞에서 몰래 페이지를 내민다. 자책이 자국(자비)이 된다. [자책 섞인 조용한 동정 · 기록관/Neural2-C] "…나는 죄인이 아니오. 단지 늦은 사람일 뿐." (rel 4.0=절대 25.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the records keeper is a weary 50-year-old Joseon official clerk, plain dark official robe, black horsehair official hat, deep lines of duty and guilt, self-reproaching careful eyes — no weapon, no ornaments. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: the candle only now — the lantern dies by the door. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. His mercy is voluntary and ashamed: no blackmail tone, no threat staging, no intimacy — formal distance held until the final offering.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm, static: the records keeper turning away from the table and walking toward the door, his back to the candle, shoulders heavy with an old guilt, the woman watching him go.
2. 85mm, static: at the doorway he stops, one hand on the wooden frame, his face half turned and torn — he does not leave.
3. 85mm, static: he holds out a small folded paper page with his eyes averted, ashamed, and her hand reaches across to take it — no touch between them, the folded page blank and unreadable, no letters, no glyphs.

DOOR AND FOLDED PAGE MOTION — IMPORTANT: physically-based robe fabric swaying as he turns, the door frame taking his weight, the folded page held crisp between his fingers with real paper stiffness, her measured reach. Do NOT follow the sketch's static lines — the delayed mercy must feel like real filmed footage. No melodrama, no tears — guilt lives in the shoulders and the averted eyes.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 잉크로 매긴 값 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP10_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 몰래 받은 페이지, 목판 인쇄 '시상(施賞)' 두 글자. 아버지의 목에 매겨진 값이 매크로로만 존재한다. [목이 메는 속마음 · 설화/Neural2-A] "아버지의 목에 값을 매긴 글자들이야." (rel 3.5=절대 32.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No other person in this scene. No violence, no weapon.

CANDLE LIGHT GUARD — IMPORTANT: the candle burns low, the flame close to the paper. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Her rage reads in a tight throat and steady hands — never tears, never wide eyes.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the unfolded stolen page lying in candlelight, old paper fibers and faint woodblock-print column texture, the rest of the page blank — no letters, no glyphs except what comes next.
2. 100mm extreme macro insert, static: exactly two large woodblock-printed Chinese characters side by side on the old paper — first the character 施 (the fang radical on the left with ye on the right), then the character 賞 (the shang roof over a shell base) — thick ink-brush woodblock relief, accurate stroke forms, these two characters are the only readable marks anywhere in the footage.
3. 85mm close, static: her face above the page, throat tight, the candle flame reflected in her cold eyes, jaw set, no tears.

CANDLE AND INK MOTION — IMPORTANT: physically-based candlelight flickering across the paper fibers, the woodblock ink relief catching the flame light, her controlled breath once and released, the page corner trembling faintly in her grip. Do NOT follow the sketch's static lines — the priced life must feel like real filmed footage. No dramatic score staging, no gasp — grief compressed into stillness. If the two printed characters render distorted, the insert must be trimmed to the blank paper with the ink strokes unreadable — text meaning is carried by the subtitle in editing.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 잠들지 않는 궁 (절대 37.5~45.0 · 콘티 3컷 · 무대사)

- **시트**: `downloads/EP10_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 창밖 새벽 전 고요한 궁궐 원경. 무대사 — 건축만이 숨을 죽인다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no human figures anywhere in this scene. Architecture and objects only. No violence, no weapon.

PRE-DAWN LIGHT GUARD — IMPORTANT: cool grey pre-dawn ambient over the palace, the last candle guttering low inside. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The palace never sleeps: stillness, not emptiness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, static: the Joseon palace rooftop ridgeline seen through a lattice window just before dawn, still air, the sky barely lightening behind the tiled roofs.
2. 24mm wide, slow drift: an empty frost-covered courtyard, rows of extinguished stone lanterns, long colonnades holding the dark.
3. 100mm macro insert, static: a candle drowned in its own wax pool, the last flame guttering low and finally dying.

HAZE AND FLAME MOTION — IMPORTANT: physically-based thin haze drifting over the rooftops, frost stillness in the courtyard, the last candle flame guttering and drowning in the wax with real fluid weight, the smoke thread rising after it dies. Do NOT follow the sketch's static lines — the held breath of the palace must feel like real filmed footage. No birds, no bells, no music cue — silence is the scene.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 말없는 배웅 (절대 45.0~52.5 · 콘티 4컷)

- **시트**: `downloads/EP10_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 기둥 그늘 — 돌아가는 길, 무결이 말없이 등을 맞아준다. 한 마디면 충분하다. [낮은 고백 · 무결/Wavenet-C] "복도는 비웠습니다. 천천히 가시지요." (rel 2.5=절대 47.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. The warrior is a 25-year-old Joseon warrior captain, tall, in a dark navy and black military robe, a faint scar across the cheekbone, sharp heavy calm eyes — sword stays sheathed at his hip, no weapon drawn, no violence.

PRE-DAWN LIGHT GUARD — IMPORTANT: cool pre-dawn ambient along the long wooden corridor, deep column shade. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. This is an escort of manners, not a romance: no intimacy, no touching, formal distance held.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the long pre-dawn wooden palace corridor with repeating columns, the young woman walking it while the tall warrior waits in the deep shade of a pillar ahead.
2. 85mm, static: the warrior turning to fall in behind her, his body placed between her and the dark end of the corridor, the sheathed sword at his hip.
3. 85mm tracking, static height: the two walking side by side at formal distance, pillar shadows passing over them in rhythm.
4. 100mm macro insert, static: his hand resting calmly on the sheathed sword at his hip, no draw, the scabbard worn smooth.

PILLAR AND SLEEVE MOTION — IMPORTANT: physically-based pillar shadows passing over the walkers, sleeve fabric settling with real weight, the scabbard swaying once with his stride, their steps quiet on the boards. Do NOT follow the sketch's static lines — the wordless loyalty must feel like real filmed footage. No romantic glance, no lingering look — protection expressed as etiquette.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 소매 속으로 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP10_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro → 엔드카드 — 페이지가 소매 속으로 → 암전. **붉은 타이틀(제11화 「상궁의 발탁」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil — elegant dark pastel hanbok. No other person in frame. The folded page is blank and unreadable — no letters, no glyphs, no readable marks of any kind. No violence, no weapon.

PRE-DAWN LIGHT GUARD — IMPORTANT: cool pre-dawn ambient, the last candle dead, then the light dying in the frame. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no farewell gesture beyond the folding itself.

Recreate the panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: the folded stolen page sliding fully into her hanbok sleeve, the fabric folding over it and swallowing it, the paper blank and unreadable.
2. 85mm close, static: her face composed and cold in profile, walking into darkness, nothing left on her face of what she read.
3. The frame slowly dims — the pre-dawn corridor grey thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

SLEEVE AND LIGHT MOTION — IMPORTANT: physically-based sleeve fabric swallowing the folded page with real weight and a final soft crease, her stride unhurried, the ambient light dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the evidence riding home must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 3컷 | EP10_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 35mm 열람 탁자 상면 · EP08 동세트 회피 · 촛불+먼지 |
| S02 | 07.5~15.0 | 4컷 | EP10_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 100mm 매크로 · 도려진 자국=부재의 물성 · 회상 플래시뱅크 금지 |
| S03 | 15.0~22.5 | 4컷 | EP10_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 기록관 입장 · 격식 거리 · 두 대사 교차 |
| S04 | 22.5~30.0 | 3컷 | EP10_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 50mm 기다림 · 문 앞 비밀 제공 · 무기·협박 0 |
| S05 | 30.0~37.5 | 3컷 | EP10_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 施賞 목판 인서트 · 유일 가독 예외 · 왜곡 시 먹물 필치 대체 |
| S06 | 37.5~45.0 | 3컷 | EP10_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 궁궐 원경 · 무인물 · 무대사 |
| S07 | 45.0~52.5 | 4컷 | EP10_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 기둥 그늘 · 무결 환도 칼집 · 격식 거리 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP10_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 소매 수납·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤) | rel 3.0 | 절대 2.0 | 십 년 전의 기록은, 십 년 동안 누군가에게 읽히지 않았다. |
| 2 | S02 | 설화 `ko-KR-Neural2-A` (서늘한 확신, Pitch -1.0) | rel 4.0 | 절대 9.5 | 도려내는 데는 서관 한 명, 밤 하나면 족하지요. |
| 3 | S03 | 기록관 `ko-KR-Neural2-C` (무게 있게 절제, Pitch -0.5) | rel 3.5 | 절대 17.0 | 몇 장 빠져 있소. 마마는 그것을 알아 무엇에 쓰시려우. |
| 4 | S03 | 설화 `ko-KR-Neural2-A` (거짓 평온, Pitch -1.0) | rel 6.0 | 절대 19.5 | 빠진 것을 헤아리는 것이 사헌부의 일이었나이다. |
| 5 | S04 | 기록관 `ko-KR-Neural2-C` (자책 섞인 조용한 동정, Pitch -0.5) | rel 4.0 | 절대 25.5 | …나는 죄인이 아니오. 단지 늦은 사람일 뿐. |
| 6 | S05 | 설화 `ko-KR-Neural2-A` (목이 메는 속마음, Pitch -1.0) | rel 3.5 | 절대 32.5 | 아버지의 목에 값을 매긴 글자들이야. |
| 7 | S07 | 무결 `ko-KR-Wavenet-C` (낮은 고백, Pitch -1.5) | rel 2.5 | 절대 47.0 | 복도는 비웠습니다. 천천히 가시지요. |
| 8 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제11화 「상궁의 발탁」에서 계속 |

- S06은 무대사 썬 — 보이스·자막 블록 없음. 자막 공백(00:37~00:47)은 정본 무대사 연출 그대로 둔다(침묵이 궁이 잠들지 않음을 말한다).
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 무결 `Wavenet-C`(Pitch -1.5), 내레이션 `Wavenet-C`(다큐 톤). 기록관은 정본 썬표 지정대로 `Neural2-C`(Pitch -0.5) — 왕 이환과 동일 ID 축이지만 본 화에서 왕이 미등장하므로 충돌 없으며, 감정 톤 지문(무게 있게 절제/자책 섞인 조용한 동정)으로 배역을 구분한다.
- S05·S07 설화·무결 대사는 각각 속마음/짧은 고백 — 믹싱 시 톤 지문(목이 메는 속마음/낮은 고백)을 우선한다.
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(마스터 각본 제10화 썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,500
십 년 전의 기록은,
십 년 동안 누군가에게 읽히지 않았다.

2
00:00:09,500 --> 00:00:12,000
도려내는 데는 서관 한 명,
밤 하나면 족하지요.

3
00:00:17,000 --> 00:00:19,000
몇 장 빠져 있소.
마마는 그것을 알아 무엇에 쓰시려우.

4
00:00:19,500 --> 00:00:22,000
빠진 것을 헤아리는 것이
사헌부의 일이었나이다.

5
00:00:25,500 --> 00:00:28,500
…나는 죄인이 아니오.
단지 늦은 사람일 뿐.

6
00:00:32,500 --> 00:00:35,000
아버지의 목에
값을 매긴 글자들이야.

7
00:00:47,000 --> 00:00:49,000
복도는 비웠습니다. 천천히 가시지요.

8
00:00:59,000 --> 00:01:00,000
제11화 「상궁의 발탁」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S06 자막 공백(00:37~00:47)은 정본 무대사 썬 — 새벽 전 궁궐 정적은 믹싱 앰비언스로만 처리한다.
- 3·4번 블록은 S03 기록관-설화 교차 대사 — 믹싱 시 실제 발화 간격(rel 3.5/6.0)에 맞춰 편집 단계에서 확정한다.
- S05 6번 블록은 '시상(施賞)' 두 글자의 의미를 대신 창출하는 자막 — 렌더 인서트 글자 왜곡 시 본 자막이 유일한 정보 운반체다(§0-11 대체 경로).
- 보이스 ID 운용: 고정 ID + 감정 톤 지문(무거운 나레이션/서늘한 확신/무게 있게 절제/거짓 평온/자책 섞인 조용한 동정/목이 메는 속마음/낮은 고백)으로 썬별 미묘함을 구분한다.
