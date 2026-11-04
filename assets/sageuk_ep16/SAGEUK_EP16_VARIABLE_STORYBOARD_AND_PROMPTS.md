# 「혈화의 궐」 EP16 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + 정본 EP16 「칼을 갈 밤」 8썬표(`SEASON_01_MASTER_SCREENPLAY.md` 제16화 섹션) + `characters.md` 캐릭터 앵커 + EP15 원장 템플릿(100% 동일 규격) + EP04~EP15 원장 운용 결과
> **범위**: EP16 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 본 화의 서사는 '준비'이지 '분노'가 아니다**: 칼을 가는 밤 한 편 전체를 호흡 하나 고치는 데 쓴다(정본 안티슬롭 치환 준수: [훈련 몽타주 음악 과장]→[호흡 하나 고치는 데 화 한 편을 쓰는 절제], ["내가 갈고닦은 그 칼로" 무기 연애]→[칼은 목적이 아니라 준비라는 대사 반전]). **훈련 몽타주·무기 감상몽유·월권 연출 일절 렌더 금지** — 칼은 복수를 위한 냉혹한 도구이자 호흡의 수단으로만 보인다. **숫돌 불티 화재 필터 오인 방지(정본 AG ②)** — `sparks off a whetstone falling downwards` 명시로 정상 낙하 매크로로만 렌더한다. **무결-최판서 동일 보이스 ID(`ko-KR-Wavenet-C`) 이중 배역** — 트랙 분리 합성과 파일명 규칙(`EP16_S1_MUGYEOL` / `EP16_S4_CHOIPANSEO`)·피치 차등(무결 Pitch -1.5 / 최판서 Pitch +0.5)으로 혼동을 차단한다(정본 AG 검수 ⑦). **설화-무결 어색함 배제**: S03 손목 교정은 두 사람 모두 어색하지 않은 직업적 수업이다 — 로맨스 밀도 0. **왕의 결심은 소리 없이**: S06 발견은 선언이 아니라 고뇌의 굳어짐으로.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **숫돌·칼날**(the blade sliding along the wet stone with real friction and real resistance, sparks off a whetstone falling downwards with real gravity, water thinning on the stone as it is worked), S02 **칼·몸**(the sword's real weight settling into her grip, shoulders lowering with a real exhaled breath, lantern flames swaying with the night air), S03 **두 손**(the grip adjusting with real finger pressure, two bodies breathing at one rhythm, sleeves settling after the correction), S04 **곡물·철**(grain shifting inside the sacks with real mass, iron bars clinking with real metal weight, dust drifting through the slanted light), S05 **촛불·종이**(two candle flames breathing with real air, the folded paper resting with real paper weight, shadows tilting as the flames move), S06 **밤하늘**(stars steady with real sky depth, the hand closing with real tendon effort, the robe hem moving in the night wind), S07 **기둥·복도**(the pillar's shadow holding still, his step quieting with real body control, moonlight lying still on the boards), S08 **칼자루·비단**(the silver needle-dagger sliding into the sleeve with the smallest metal-on-silk friction, the sleeve settling with real fabric weight, the candle flame thinning before the fade). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ②·⑦ 준수 — 본 화 핵심)**: 유혈·상해·폭력·감상몽유 일체 없음. **칼은 도구로만 등장**한다 — `the blade is a tool being maintained on a whetstone and trained with, never pointed at or used on any person, no violence, no one struck, no injury, no blood` 전 썬 명시(S01~S03). S04~S08은 `no drawn weapon, no blade visible`로 복귀. **무기 연애 차단**: `no weapon worship, no romantic framing of the blade — the sword is a chore, not an idol` S01·S02 명시. **전 등장 인물 성인** — `all characters are adults` 전 썬 명시. **설명 대사 차단**: `no exposition speeches`.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07~EP15 재발 방지: 설화 앵커의 **귀걸이·수술·가체·떨잠 금지 전 썬 상향 고정** 유지. 본 화 시트 S03 1차 렌더에서 설화 장식·무결 수염 이탈이 발생해 앵커 인라인 강화로 교정 완료 — 시트·원장 양쪽 모두 강화 문구 탑재.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **무결**: 25-year-old warrior officer, tall solid build, completely clean-shaven, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, earth on his hands, quiet heavy-lidded watchful eyes, economical restrained movements (S01~S03에서는 연마·훈련 중인 도출 칼을 손에 든다 — 인출은 도구 정비 목적에 한정)
   - **이환(왕)**: 24-year-old king, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown, the weary bearing of a monarch who has decided
   - **최판서**: greedy 55-year-old granary keeper official, heavyset, dark official robe with a black cap, narrow greedy eyes, sly fawning half-smile, ink-stained fingers, rings of wealth
   - **왕의 밀정**: a forgettable man in plain grey merchant clothes and a plain cap, unremarkable face, sharp patient eyes that miss nothing
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제17화 「밀실의 맹약」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 은장도가 소매로 들어가고 촛불이 가늘어짐 → 완전 암전 유지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01 `one paper lantern's warm pool of light in the dark training yard, the sparks briefly catching the lantern light as they fall`, S02 `two paper lanterns on wooden stands, warm light on packed earth, the night cold beyond`, S03 `the same lantern's low warm light on two faces and one hilt`, S04 `slanted late-afternoon light across the granary yard, long shadows, dust in the light`, S05 `two candle flames as the only sources, shadows tilting as the flames move`, S06 `moonlight from above and one standing lantern, the vast starlit sky as the key source`, S07 `moonlit terrace beyond the pillar, one low lantern in the corridor behind`, S08 `one candle flame by the sleeve, thinning until the fade to complete black`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 본 화의 서류 소품 — **최판서의 장부·왕의 조서 — 는 전부 `blank paper, no characters, no glyphs, no labels`**. 조서는 접힌 채로만 등장해 **카메라에 글자를 한 번도 노출하지 않는다**(조서의 문구는 SRT·믹싱이 담당). 쌀·철 포개봉·관인 등 모든 표식도 무문자 — **패널 서술 안에서도 반복 기입**한다(EP12 S03 현판 글리프·EP15 재렌더 권고 준수). EP16은 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦)**: **무결과 최판서가 모두 `ko-KR-Wavenet-C`**다. 혼동 차단 4중 장치를 강제한다 — ① 무결·최판서 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 무결 `EP16_S1_MUGYEOL`, 최판서 `EP16_S4_CHOIPANSEO`, ③ **피치 차등을 매 행 강제 표기**: 무결 `Pitch -1.5`(묵직한 훈계, Speed 1.0) / 최판서 `Pitch +0.5`(탐욕스러운 거래, Speed 0.95) — 무결이 **아래로 가라앉고** 최판서는 **위로 뜬다**(차 2.0, 축이 반대다), ④ 믹싱 단계에서 Pitch·톤 축 확인(무결은 인물 톤으로 밀착되고 최판서는 가벼운 탐욕 톤으로 떠 있어야 한다 — 실측 유지). 하나라도 누락되면 재합성한다. 설화 `Neural2-A`·이환 `Neural2-C`는 본 화 단독 배역으로 충돌 없다.

---

## 1. S01 숫돌 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP16_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 숫돌에 갈리는 칼날, 불티는 아래로 떨어진다. [효과음] 칼가는 소리 자—악 (rel 1.5=절대 0.5, 사후 믹싱) / [묵직한 훈계 · 무결/`ko-KR-Wavenet-C`, **Pitch -1.5**, Speed 1.0] "칼은 분노가 아니라 호흡으로 벱니다. 어깨를 내리지요." (rel 3.0=절대 2.0) **매크로 1컷 한정 — 이후 휴먼 스케일 교차(정본 AG ①). 불티는 `sparks off a whetstone falling downwards`로만 명시(정본 AG ②).**
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior officer is a 25-year-old Korean man, tall solid build, completely clean-shaven, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, quiet heavy-lidded watchful eyes, economical restrained movements. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. The blade is a tool being maintained on a whetstone, never pointed at or used on any person — no violence, no one struck, no injury, no blood, no weapon worship.

LIGHT GUARD — IMPORTANT: one paper lantern's warm pool of light in the dark training yard, the sparks briefly catching the lantern light as they fall. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No ominous music staging — a night chore done with a warrior's patience.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a sword blade's edge sliding along a wet whetstone at night, small sparks off a whetstone falling downwards below the edge, lantern light on the wet stone.
2. 35mm, static: the warrior officer kneeling over the whetstone in the lantern corner of a night training yard, the blade moving in long even strokes, one paper lantern.
3. 85mm close, static: his face, steady unhurried breathing, calm heavy-lidded eyes on the blade, shoulders lowered, lantern light on his scarred cheekbone.
4. 50mm, static: at the edge of the lantern light the court lady stands watching silently, hands folded, lantern glow only on her skirt hem.

STONE AND BLADE MOTION — IMPORTANT: physically-based the blade sliding along the wet stone with real friction and real resistance, sparks off a whetstone falling downwards with real gravity, water thinning on the stone as it is worked. Do NOT follow the sketch's static lines — the grinding must feel like real filmed footage. The sparks are small and ordinary and always fall downwards — a maintained tool, not a forge of rage. No weapon worship, no romantic framing of the blade — the sword is a chore, not an idol.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 칼을 잡는 설화 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP16_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 훈련장 와이드 — 설화가 직접 칼을 잡는다. [서늘한 결의 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "그 호흡을… 가르쳐 주십시오." (rel 3.0=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The warrior officer is a 25-year-old Korean man, tall solid build, completely clean-shaven, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, quiet heavy-lidded watchful eyes. All characters are adults. The blade is a training tool held at low guard toward the dark, never pointed at or used on any person — no violence, no one struck, no injury, no blood, no weapon worship, no training montage energy.

LIGHT GUARD — IMPORTANT: two paper lanterns on wooden stands, warm light on packed earth, the night cold beyond. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No score swell, no montage — one breath is being repaired tonight.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm wide, static: the court lady stepping into the lantern light of a night training yard and taking the sword directly with both hands, the warrior officer watching, two paper lanterns.
2. 85mm, static: her first sword stance, shoulders raised too high, jaw rigid, breath held, lantern shadows hard on her frame.
3. 35mm, static: the warrior officer beside her, one open hand gesturing gently downward toward her shoulders, patient, the drawn sword held low.

BODY MOTION — IMPORTANT: physically-based the sword's real weight settling into her grip, shoulders lowering with a real exhaled breath, lantern flames swaying with the night air. Do NOT follow the sketch's static lines — the stance must feel like real filmed footage. She does not wait to be given the sword — that is the whole character note.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 호흡 교정 (절대 15.0~22.5 · 콘티 4컷 · 무대사 무음)

- **시트**: `downloads/EP16_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 교정 인서트 — 무결의 손이 설화의 손목을 고친다. **무대사 — 두 사람의 호흡만(효과음, 사후 믹싱).** (렌더 무음) **두 사람 모두 어색하지 않다 — 직업적 수업, 로맨스 밀도 0.**
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior officer is a 25-year-old Korean man, tall solid build, completely clean-shaven, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, quiet heavy-lidded watchful eyes, economical restrained movements. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. No violence, no one struck, no injury, no blood — a craft lesson between two professionals, no romance, no lingering touch, neither of them awkward.

LIGHT GUARD — IMPORTANT: the same lantern's low warm light on two faces and one hilt. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No music, no swelling — only breathing.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm insert, static: the warrior officer's steady hand correcting the court lady's wrist grip on the sword hilt, two hands and one hilt in lantern light.
2. 85mm, static: their two faces, neither awkward, both pairs of eyes fixed on the blade between them.
3. 50mm, static: her shoulders finally lowering as her breath settles, the stance softening, his hand withdrawing.
4. 24mm wide, static: the two small figures in the vast dark training yard, one lantern, distant palace rooftops, complete stillness.

HANDS MOTION — IMPORTANT: physically-based the grip adjusting with real finger pressure, two bodies breathing at one rhythm, sleeves settling after the correction. Do NOT follow the sketch's static lines — the correction must feel like real filmed footage. The correction is wordless and professional — the only sound is breath.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 곳간의 밀거래 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP16_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 — 곳간지기 최판서의 밀거래를 엿보는 왕의 밀정. [불경한 거래 · 최판서/`ko-KR-Wavenet-C`, **Pitch +0.5**, Speed 0.95] "쌀 천 석은 별서로, 철 삼백 근은 배로." (rel 3.0=절대 24.5) **무결과 동일 보이스 ID(`Wavenet-C`) — §0-12 4중 차단 장치 필수.**
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the granary keeper is a greedy 55-year-old Korean official, heavyset, dark official robe with a black cap, narrow greedy eyes, sly fawning half-smile, ink-stained fingers, rings of wealth. The royal secret observer is a forgettable man in plain grey merchant clothes and a plain cap, unremarkable face, sharp patient eyes that miss nothing. Porters are ordinary laborers, faces forgettable. All characters are adults. No violence, no drawn weapon, no blade visible, no injury, no blood — theft as administration, a quiet ledger of greed.

LIGHT GUARD — IMPORTANT: slanted late-afternoon light across the granary yard, long shadows, dust in the light. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No shouting, no thuggery — a business running shamelessly in daylight.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 135mm compression, static: a plain-clothed royal observer half-hidden among stacked grain sacks watching the granary yard from afar, long late-afternoon shadows.
2. 50mm, static: the granary keeper directing porters among rice sacks on a scale and a stack of iron bars, a completely blank ledger with no characters under his arm, late-afternoon light.
3. 85mm close, static: the observer's sharp eyes narrowing as he memorizes the yard, then turning quietly away.

GRAIN AND IRON MOTION — IMPORTANT: physically-based grain shifting inside the sacks with real mass, iron bars clinking with real metal weight, dust drifting through the slanted light. Do NOT follow the sketch's static lines — the trade must feel like real filmed footage. Every ledger and tag is blank paper: no characters, no glyphs, no labels — the numbers belong to the sound mix. The observer never moves closer — watching is the whole scene.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 밀회 — 진짜 조서 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP16_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 밀회 — 설화가 왕에게 진짜 조서로 그 자를 잡자는 계략. [서늘한 설계 · 설화/`ko-KR-Neural2-A`, Pitch -1.0] "거짓은 한 번 쓰면 끝나이다. 진짜 조서로 — 그 자의 입을 열겠나이다." (rel 3.5=절대 32.5) / [낮은 질문 · 이환/`ko-KR-Neural2-C`, Pitch -0.5, Speed 0.95] "…방법이 있나." (rel 6.0=절대 35.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The young king is a 24-year-old Korean monarch, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown, the weary bearing of a monarch who has decided. All characters are adults. No violence, no weapon, no injury, no blood, no throne-room theatre — a conspiracy drawn on a kitchen table.

LIGHT GUARD — IMPORTANT: two candle flames as the only sources, shadows tilting as the flames move. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No dramatic sting — two quiet people planning in whispers.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm, static: by two candle flames the court lady kneeling in counsel with the young king across a low table in his night chamber.
2. 85mm, static: her face in candlelight, cold design in the eyes, whispering the plan.
3. 50mm, static: a folded blank memorial paper on the low table beside a candle, the paper completely blank with no characters.
4. 85mm, static: the king's face, guarded, one flicker of hope in the melancholy eyes, mouth silent and firm.

CANDLE AND PAPER MOTION — IMPORTANT: physically-based two candle flames breathing with real air, the folded paper resting with real paper weight, shadows tilting as the flames move. Do NOT follow the sketch's static lines — the counsel must feel like real filmed footage. The memorial paper is folded and completely blank to the camera — no characters, no glyphs, no seal shown — its words belong to the sound mix.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 왕의 결심 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP16_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 왕이 밤하늘을 보며 결심한다. [억누른 결심 · 이환/`ko-KR-Neural2-C`, Pitch -0.5, Speed 0.95] "이명진의 딸이라면 — 과인이 먼저 부르는 것이 옳겠지." (rel 3.5=절대 40.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the young king is a 24-year-old Korean monarch, pale refined handsome features, deep melancholy eyes hiding a quiet fury, dark royal informals with a gold winged ikseongwan crown, the weary bearing of a monarch who has decided. He is alone. All characters are adults. No violence, no weapon, no injury, no blood — no oath shouted at the sky, no thunder.

LIGHT GUARD — IMPORTANT: moonlight from above and one standing lantern, the vast starlit sky as the key source. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No music crescendo — a decision made quietly and alone.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the young king alone on an open wooden palace terrace under a vast cold starlit night sky, dark rooftops below, moonlight and one standing lantern.
2. 85mm close, static: his upturned face, moonlight from above, melancholy hardening into resolve, jaw set.
3. 50mm, static: his hand slowly closing at his side, unhurried and deliberate, the moonlit terrace empty.

SKY AND HAND MOTION — IMPORTANT: physically-based stars steady with real sky depth, the hand closing with real tendon effort, the robe hem moving in the night wind. Do NOT follow the sketch's static lines — the resolve must feel like real filmed footage. The sky gives him nothing — he gives himself.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 엿들은 자 (절대 45.0~52.5 · 콘티 3컷 · 무대사 무음)

- **시트**: `downloads/EP16_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 무결이 그 말을 엿듣고 아무것도 묻지 못한다. **무대사 — 자책 섞인 침묵, 고개만 숙임.** (렌더 무음)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior officer is a 25-year-old Korean man, tall solid build, completely clean-shaven, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, a sheathed sword at his belt with the blade never drawn, quiet heavy-lidded watchful eyes. He is alone in frame. All characters are adults. No violence, no drawn weapon, no blade visible, no injury, no blood — no eavesdropping thriller staging; he heard by accident and pays for it in silence.

LIGHT GUARD — IMPORTANT: moonlit terrace beyond the pillar, one low lantern in the corridor behind. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No music, no sting — guilt and loyalty share one silence.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm tight shot, static: the warrior officer frozen at the dark corridor corner, a wooden pillar between him and the moonlit terrace beyond, having heard everything.
2. 85mm close, static: his face, self-reproach in the heavy-lidded eyes, gaze lowered, jaw tight, completely silent.
3. 50mm, static: he lowers his head and turns away down the dark wooden corridor, his step quiet.

CORRIDOR MOTION — IMPORTANT: physically-based the pillar's shadow holding still, his step quieting with real body control, moonlight lying still on the boards. Do NOT follow the sketch's static lines — the retreat must feel like real filmed footage. He asks nothing — the question he will never ask lives in his stillness.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 은장도, 소매로 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP16_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro → 엔드카드 — 은장도가 다시 소매로 → 암전 → 타이틀. **붉은 타이틀(제17화 「밀실의 맹약」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. All characters are adults. No violence, no drawn weapon, no blade visible as a threat, no injury, no blood — the small silver needle-dagger is resolve put away, not a weapon in use.

LIGHT GUARD — IMPORTANT: one candle flame by the sleeve, thinning until the fade to complete black. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no final line, no music sting staging.

Recreate the panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the slender silver needle-dagger sliding slowly back into a dark silk sleeve by candlelight.
2. 85mm, static: the court lady in her candlelit quarters, the sleeve settling smooth, her face composed, the room ordinary.
3. The frame slowly dims — the candle light thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

SLEEVE AND FADE MOTION — IMPORTANT: physically-based the silver needle-dagger sliding into the sleeve with the smallest metal-on-silk friction, the sleeve settling with real fabric weight, the candle flame thinning before the fade. Do NOT follow the sketch's static lines — the putting-away must feel like real filmed footage. Resolve put away, not abandoned. No horror staging, no dramatic score.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP16_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 100mm 매크로 1컷+휴먼 스케일 교차(AG ①) · 불티 하강 명시(AG ②) · 무기 연애 배제 |
| S02 | 07.5~15.0 | 3컷 | EP16_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 50mm 와이드 · 설화 직접 수검 · 몽타주 음악 과장 배제 |
| S03 | 15.0~22.5 | 4컷 | EP16_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 무대사 무음 · 직업적 수업 · 로맨스 밀도 0 |
| S04 | 22.5~30.0 | 3컷 | EP16_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 135mm 압축 · 밀정 관측 시점 · 장부 무문자 |
| S05 | 30.0~37.5 | 4컷 | EP16_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 밀회 · 조서 무문자·접힌 채 · 촛불 2개 광원 |
| S06 | 37.5~45.0 | 3컷 | EP16_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 와이드 · 고뇌의 굳어짐 · 선언 과장 배제 |
| S07 | 45.0~52.5 | 3컷 | EP16_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 무대사 무음 · 자책의 침묵 · 도청 스릴러 연출 배제 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP16_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 은장도 소매·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 무결 `ko-KR-Wavenet-C` (묵직한 훈계, **Pitch -1.5**, Speed 1.0) | rel 3.0 | 절대 2.0 | 칼은 분노가 아니라 호흡으로 벱니다. 어깨를 내리지요. |
| 2 | S02 | 설화 `ko-KR-Neural2-A` (서늘한 결의, Pitch -1.0, Speed 1.0) | rel 3.0 | 절대 9.5 | 그 호흡을… 가르쳐 주십시오. |
| 3 | S03 | (무대사 — 두 사람의 호흡만 · 효과음) | — | — | 무음 통과 · 자막 없음 |
| 4 | S04 | 최판서 `ko-KR-Wavenet-C` (불경한 거래, **Pitch +0.5**, Speed 0.95) | rel 3.0 | 절대 24.5 | 쌀 천 석은 별서로, 철 삼백 근은 배로. |
| 5 | S05 | 설화 `ko-KR-Neural2-A` (서늘한 설계, Pitch -1.0) | rel 3.5 | 절대 32.5 | 거짓은 한 번 쓰면 끝나이다. 진짜 조서로 — 그 자의 입을 열겠나이다. |
| 6 | S05 | 이환 `ko-KR-Neural2-C` (낮은 질문, Pitch -0.5, Speed 0.95) | rel 6.0 | 절대 35.0 | …방법이 있나. |
| 7 | S06 | 이환 `ko-KR-Neural2-C` (억누른 결심, Pitch -0.5, Speed 0.95) | rel 3.5 | 절대 40.0 | 이명진의 딸이라면 — 과인이 먼저 부르는 것이 옳겠지. |
| 8 | S07 | (무대사 — 자책 섞인 침묵) | — | — | 무음 통과 · 자막 없음 |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제17화 「밀실의 맹약」에서 계속 |

- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: **무결과 최판서가 동일 축 `ko-KR-Wavenet-C`**이며 S01·S03(무결 존재)·S04(최판서)가 한 화에 공존한다. 혼동 차단 4중 장치를 강제한다 — ① 무결·최판서 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 무결 `EP16_S1_MUGYEOL`, 최판서 `EP16_S4_CHOIPANSEO`, ③ **피치 차등을 매 행 강제 표기**(무결 Pitch -1.5 묵직한 훈계 / 최판서 Pitch +0.5 탐욕스러운 거래 — 무결은 아래로 가라앉고 최판서는 위로 뜬다, 차 2.0, 축 반대, 본 표 1·4번 행), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인(무결은 인물 톤으로 밀착되고 최판서는 가벼운 탐욕 톤으로 떠 있는지). 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 설화 `Neural2-A`(S02 결의 1건 + S05 설계 1건), 이환 `Neural2-C`(S05 질문 1건 + S06 결심 1건)는 충돌 없는 단독 배역 축이다.
- S05의 교환은 정본 블록 내 배치다 — 설화의 계략 제안(rel 3.5=절대 32.5)을 블록 선두에, 이환의 회답(rel 6.0=절대 35.0)을 후행에 놓는다. 설화 대사의 자연 발화 길이가 이환 큐(절대 35.0)에 근접하므로, **믹싱에서 설화 테일을 다듬어 이환 큐를 정본 절대 축에 정확히 착지시킨다**(EP15 S04 후행 배치 지문 준용).
- S03·S07은 무대사다 — 각각 두 사람의 호흡, 자책의 침묵을 효과음 레이어로만 깔고 자막을 붙이지 않는다.
- S04의 밀거래 대사는 최판서가 밀정에게가 아니라 일꾼에게 내는 거래 지시다 — 밀정은 대사 없이 관측만 한다(입모양 대화 싱크 0).
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(`SEASON_01_MASTER_SCREENPLAY.md` 제16화 정본 8썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,200
칼은 분노가 아니라
호흡으로 벱니다. 어깨를 내리지요.

2
00:00:09,500 --> 00:00:12,000
그 호흡을…
가르쳐 주십시오.

3
00:00:24,500 --> 00:00:27,300
쌀 천 석은 별서로,
철 삼백 근은 배로.

4
00:00:32,500 --> 00:00:34,800
거짓은 한 번 쓰면 끝나이다.
진짜 조서로 — 그 자의 입을 열겠나이다.

5
00:00:35,000 --> 00:00:36,800
…방법이 있나.

6
00:00:40,000 --> 00:00:43,500
이명진의 딸이라면 —
과인이 먼저 부르는 것이 옳겠지.

7
00:00:59,000 --> 00:01:00,000
제17화 「밀실의 맹약」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 7번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- 1번 블록(무결)은 `EP16_S1_MUGYEOL`, 3번 블록(최판서)은 `EP16_S4_CHOIPANSEO`, 2번 블록(설화 결의)은 `EP16_S2_SEOLHWA`, 4·5번 블록(S05 설화·이환 교환)은 `EP16_S5_SEOLHWA` / `EP16_S5_KING`, 6번 블록(이환 결심)은 `EP16_S6_KING`으로 분리 저장한다 — 무결·최판서 동일 ID 차단(§0-12)에 따라 트랙·파일 모두 분리한다.
- 4·5번 블록(설화 계략·이환 회답)은 정본 절대 축(32.5/35.0)을 유지하되 자막 노출은 비겹침으로 분리 저장해 믹싱에서 붙인다 — 한 파일에 이어 붙이지 않는다.
- SRT 전 블록에 위험 어휘·설명 대사 0건 — 정본 문구 그대로다.
