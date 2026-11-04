# 「혈화의 궐」 EP15 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + 아르센 님 확정 EP15 「조사의 그림자」 8썬표(2026-11-05 메인 재검수 정본) + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP14 원장 운용 결과
> **범위**: EP15 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 조사는 '짐을 지우는 일'이다**: 본 화의 공포는 추적과 대치가 아니라 **흔적이 하나씩 없어지는 사극적 침묵**이다(정본 안티슬롭 치환 준수: [추적자 추격 연출 오락화]→[조사가 짐을 지우는 일이 되는 공포], ["위험해! 정신 차려!"]→[무결의 행동으로 대신함]). **추격·단말마·폭력 스태징 일절 렌더 금지** — 긴장은 봉인지·지워진 장부·덮인 흙·떨어진 쪽지가 말한다. **설화의 나약한 의존·로맨스 맹세 배제**: 설화와 무결은 동등한 동지로서 마주치고, 두 마디로 계약한다. **흔적 지우기 매크로 연타 방지(정본 AG ①)** — S03·S07의 매크로는 각 썬 1컷 한정, 와이드·클로즈 교차를 시트와 원장 양쪽에 고정했다. **무결-내레이션 동일 보이스 ID(`ko-KR-Wavenet-C`) 이중 배역** — 트랙 분리 합성과 파일명 규칙(`EP15_S1_NARRATION` / `EP15_S3_MUGYEOL` / `EP15_S4_MUGYEOL`)·피치 차등(무결 Pitch -1.5 / 내레이션 Pitch 0.0)으로 혼동을 차단한다(정본 AG 검수 ⑦). **무흉기·무폭력 화**: 무결의 환도는 **칼집만**(인출 금지), 군관들은 무기 미인출, 신체 접촉·강제 물리력 0 — 조사는 행정처럼 조용하다.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **봉인지·문**(the paper seal smoothing onto the wood under a real palm's pressure, gate hinges carrying real wooden mass, the thin ribbon of vapor threading the door gap with real air movement), S02 **장부·종이**(paper pages turning with real dry stiffness, a fingertip tracing with real pressure, dust drifting through the slanted morning light), S03 **흙**(loose earth crumbling grain by grain under fingertips, a palm sweeping with real body weight, soil dragging under a sleeve hem), S04 **우물길**(two bodies passing with real walking rhythm, sleeves stirring the still air, a low voice carried only as far as one listener), S05 **회랑**(sliding doors opening with real panel weight, hands feeling under shelves with real pressure, long shadows stretching as the column moves), S06 **쪽지**(the folded note falling with real paper weight, silk sleeves settling after the bow, a held breath visible in the shoulders), S07 **버선**(the note sliding with the smallest paper friction, white cloth settling with real fabric weight, measured breathing), S08 **문·암전**(gate leaves closing with real wooden mass, the last slit of light narrowing, lamplight thinning until complete black). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ②·⑦ 준수 — 본 화 핵심)**: 유혈·흉기 가동·상해·폭력·강제 개입 일체 없음. `no violence, no drawn weapon, no blade visible, no injury, no blood, no forced entry, nothing broken, no one struck — the search is an inventory, not a raid` 전 썬 명시. 무결의 환도는 **칼집만** 등장한다(`a sheathed sword at his belt, never drawn`). **전 등장 인물 성인** — `all characters are adults` 전 썬 명시. **설명 대사 차단**: `no exposition speeches` — 조사의 진행은 물건과 행동으로만 보인다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07~EP14 재발 방지: 설화 앵커의 **귀걸이·수술·가체·떨잠 금지 전 썬 상향 고정** 유지.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **무결**: 25-year-old warrior officer, tall solid build, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, a sheathed sword at his belt with the blade never drawn, earth on his hands, quiet heavy-lidded watchful eyes, economical restrained movements
   - **윤경헌**: 58-year-old chief minister, dark official dalryeong court robe, black samo hat, gray-flecked beard, hawk-like cold eyes, deep wrinkles of power, a chilling calculating stare
   - **서 상궁**: the senior court lady, a stern Korean woman in her late forties, deep navy-blue court dangui, neatly ordered middle-aged gache hair with restrained pin ornament only — no lavish dangling ornaments — cool precise eyes, quietly severe and composed, the controlled posture of long authority
   - **사헌부 군관들**: royal investigation officers in plain dark government uniforms with plain black caps, faces ordinary and forgettable, no drawn weapons, methodical unhurried movements
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제16화 「궁의 비밀통로」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 문이 닫히고 마지막 빛 틈이 좁아짐 → 완전 암전 유지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01 `cold blue-grey first light on the sealed gate, the vapor crossing the light in the door gap`, S02 `slanted morning light through a lattice window, one bright blade of daylight on the desk`, S03 `flat overcast daylight on the courtyard earth, cold and nearly shadowless`, S04 `late-afternoon light down the well path, long shadows, the two figures meeting in a bar of light`, S05 `pale daylight cutting across the floorboards through opened doors, the lanterns unlit`, S06 `early evening gloom in the walkway, one paper lantern glowing dimly behind`, S07 `the last evening light at the window, one low oil lamp`, S08 `moonlight on the closing gates, the officers' lanterns beyond as the only light`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 본 화의 서류 소품 — **봉인지·장부·쪽지 — 는 전부 `blank paper, no characters, no glyphs, no labels`**. 장부 페이지는 `ruled lines only, one scraped blank patch`, 낙점(낙점)은 글자가 아니라 **긁어낸 자국**으로만 보인다. 쪽지는 접힌 채로만 등장해 **카메라에 글자를 한 번도 노출하지 않는다**(쪽지의 문구는 SRT·믹싱이 담당). 간판·현판 등 모든 표식도 `blank wood plaque, no characters` — **패널 서술 안에서도 반복 기입**한다(EP12 S03 현판 글리프·EP14 운용 결과 준수). EP15는 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦)**: **무결과 내레이션이 모두 `ko-KR-Wavenet-C`**다. 혼동 차단 4중 장치를 강제한다 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 내레이션 `EP15_S1_NARRATION`, 무결 `EP15_S3_MUGYEOL`·`EP15_S4_MUGYEOL`, ③ **피치 차등을 매 행 강제 표기**: 무결 `Pitch -1.5`(묵직한 절제, Speed 1.0) / 내레이션 `Pitch 0.0`(다큐 톤) — 무결이 **아래로 가라앉고** 내레이션은 **중립 축**에서 둔다(차 1.5), ④ 믹싱 단계에서 Pitch·톤 축 확인(무결은 인물 톤으로 밀착되고 내레이션은 다큐 중립으로 떠 있어야 한다 — 실측 유지). 하나라도 누락되면 재합성한다. 설화 `Neural2-A`·윤경헌 `Wavenet-D`·서 상궁 `Neural2-B`는 본 화 단독 배역으로 충돌 없음.

---

## 1. S01 봉인된 문 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP15_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 새벽 — 사헌부 군관들이 수라간을 봉쇄한다. [무거운 다큐 톤 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0] "문은 닫혔으나 — 문틈으로 새는 숨은 막지 못했다." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — royal investigation officers in plain dark government uniforms with plain black caps, faces ordinary and forgettable, no drawn weapons, methodical unhurried movements. All characters are adults. No violence, no drawn weapon, no blade visible, no injury, no blood, no forced entry, nothing broken — the sealing of a kitchen is an administrative act, not a raid.

LIGHT GUARD — IMPORTANT: cold blue-grey first light on the sealed gate, the vapor crossing the light in the door gap. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No drama, no shouting — dawn paperwork with a chilling meaning.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: at first light, officers in plain dark uniforms pressing blank paper seals onto the royal kitchen's heavy wooden gate, cold dawn light.
2. 50mm, static: an officer's palm smoothing a blank paper seal onto the wooden gate, real palm pressure, the paper completely blank.
3. 24mm wide, static: the sealed compound, officers withdrawing in single file, long shadows across the empty courtyard.
4. 85mm close, static: the gap beneath the sealed gate, a thin ribbon of warm vapor slipping out through the crack, catching the pale light.

PAPER AND GATE MOTION — IMPORTANT: physically-based the paper seal smoothing onto the wood under a real palm's pressure, gate hinges carrying real wooden mass, the thin ribbon of vapor threading the door gap with real air movement. Do NOT follow the sketch's static lines — the sealing must feel like real filmed footage. The seal paper and every plaque are blank: no characters, no glyphs, no labels. No ominous sting — a door closing that does not close the matter.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 지워진 장부 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP15_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 윤경헌이 약재 반출 장부를 훑는다. [서늘한 만족 · 윤경헌/`ko-KR-Wavenet-D`, Pitch -2.5, Speed 0.9] "청분이 나간 날 — 기록이 지워진 자가 있다." (rel 3.5=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the chief minister is a 58-year-old Korean man, dark official dalryeong court robe, black samo hat, gray-flecked beard, hawk-like cold eyes, deep wrinkles of power, a chilling calculating stare. He is alone in the room. All characters are adults. No violence, no weapon, no injury, no blood — a man reading a ledger and finding an erasure.

LIGHT GUARD — IMPORTANT: slanted morning light through a lattice window, one bright blade of daylight on the desk. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No anger, no outburst — the accusation never leaves his mouth.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the chief minister at a dark desk turning the pages of a bound herbal export ledger, the ledger cover completely plain and blank with no label and no characters, slanted morning light through a lattice window.
2. 100mm macro, static: his aged fingertip resting on a scraped blank patch in a ledger page of ruled lines, no readable characters, morning light raking the paper grain.
3. 85mm close, static: his face, a thin cold almost-smile that never reaches the hawk-like eyes.

LEDGER AND PAPER MOTION — IMPORTANT: physically-based paper pages turning with real dry stiffness, a fingertip tracing with real pressure, dust drifting through the slanted morning light. Do NOT follow the sketch's static lines — the reading must feel like real filmed footage. The ledger pages show ruled lines only and one scraped blank patch: no characters, no glyphs, no labels anywhere on cover, spine or page. The erasure itself is the confession.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 발자국은 셋 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP15_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 무결의 손이 담장 밑 흙을 덮는다. [묵직한 절제 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5] "발자국은 셋이었으나 — 이제 둘입니다." (rel 3.0=절대 16.5) **매크로 1컷 한정 — 와이드 교차로 연타 차단(정본 AG ①).**
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior officer is a 25-year-old Korean man, tall solid build, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, a sheathed sword at his belt with the blade never drawn, earth on his hands, quiet heavy-lidded watchful eyes, economical restrained movements. He is alone. All characters are adults. No violence, no drawn weapon, no blade visible, no injury, no blood — covering footprints is the entire event.

LIGHT GUARD — IMPORTANT: flat overcast daylight on the courtyard earth, cold and nearly shadowless. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No chase, no tense music staging — housework done with a warrior's economy.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a man's fingertips crumbling loose dry earth over shallow footprints beneath a wooden fence, soil moving grain by grain.
2. 24mm wide, static: the warrior officer crouched alone by the palace back fence under flat overcast daylight, loose earth around his boots.
3. 50mm, static: his open palm sweeping the last footprints flat, his sleeve hem dragging through the soil.
4. 85mm close, static: his face, breath held, heavy-lidded eyes still counting along the ground, earth smudged on his hands.

SOIL MOTION — IMPORTANT: physically-based loose earth crumbling grain by grain under fingertips, a palm sweeping with real body weight, soil dragging under a sleeve hem. Do NOT follow the sketch's static lines — the erasure must feel like real filmed footage. Only one macro passage, then out to human scale. The ground forgets on order — nothing is said aloud.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 말을 아낀 마주침 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP15_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 투숏 — 설화와 무결의 짧은 마주침, 말을 아낀다. [낮은 합의 · 설화/`ko-KR-Neural2-A`, Pitch -1.0] "장부는." / [묵직한 절제 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5] "돌아오지 못할 곳으로 보냈습니다." (교환 블록 rel 4.5=절대 24.5, 무결 후행 — §10-1 4·5번 행)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The warrior officer is a 25-year-old Korean man, tall solid build, faint pale scar across his right cheekbone, dark navy military yungbok uniform, hair tied simply, a sheathed sword at his belt with the blade never drawn, quiet heavy-lidded watchful eyes. All characters are adults. No violence, no drawn weapon, no blade visible, no physical contact, no bowing of either to the other — two equals crossing paths.

LIGHT GUARD — IMPORTANT: late-afternoon light down the well path, long shadows, the two figures meeting in a bar of light. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No romance vow, no rescue posture, no dependence — an alliance signed in two syllables.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm two-shot, static: the court lady and the warrior officer crossing paths on a narrow well path in late-afternoon light, both mid-stride, neither bowing.
2. 85mm tight two-shot, static: their eyes meeting in passing, level and equal, nothing sentimental.
3. 50mm, static: she speaks two quiet words without turning her head, he answers facing forward, both walking apart.

WELL PATH MOTION — IMPORTANT: physically-based two bodies passing with real walking rhythm, sleeves stirring the still air, a low voice carried only as far as one listener. Do NOT follow the sketch's static lines — the crossing must feel like real filmed footage. No lingering gaze, no swelling score — equals exchanging facts and walking on.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 길어지는 그림자 (절대 30.0~37.5 · 콘티 4컷 · 무대사 무음)

- **시트**: `downloads/EP15_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 사헌부 군관들이 회랑을 수색, 그림자가 길어진다. **무대사 — 군관들의 발소리만(효과음, 사후 믹싱).** (렌더 무음)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — royal investigation officers in plain dark government uniforms with plain black caps, faces ordinary and forgettable, no drawn weapons, methodical unhurried movements. No court lady, no principal character in frame. All characters are adults. No violence, no drawn weapon, no blade visible, no injury, no blood, no forced entry, nothing broken — a household being inventoried, not ransacked.

LIGHT GUARD — IMPORTANT: pale daylight cutting across the floorboards through opened doors, the lanterns unlit. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No drama — the search has no music, only footsteps.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: officers in plain dark uniforms searching a long wooden palace corridor, sliding doors opened one by one, pale daylight on the floorboards.
2. 50mm, static: an officer's hands carefully lifting a stack of lacquered boxes and feeling beneath a shelf, nothing broken.
3. 35mm, static: the search column moving down a cross corridor, their long shadows stretching across the boards.
4. 24mm wide, high: looking down the corridor, the searchers small shapes with long shadows, the palace quiet around them.

CORRIDOR MOTION — IMPORTANT: physically-based sliding doors opening with real panel weight, hands feeling under shelves with real pressure, long shadows stretching as the column moves. Do NOT follow the sketch's static lines — the search must feel like real filmed footage. Every box and plaque is blank: no characters, no glyphs, no labels. The palace lets them — that is the horror.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 떨어진 쪽지 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP15_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 서 상궁이 설화의 곁을 지나며 작은 쪽지를 떨어뜨린다. [비밀스러운 낮은 속삭임 · 서 상궁/`ko-KR-Neural2-B`, Pitch -0.5, Speed 0.95] "오늘 밤 — 아무도 만나지 마라." (rel 3.0=절대 39.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the senior court lady: a stern Korean woman in her late forties, deep navy-blue court dangui, neatly ordered middle-aged gache hair with restrained pin ornament only — no lavish dangling ornaments — cool precise eyes, quietly severe and composed. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. Passing maids in plain dress, faces forgettable. All characters are adults. No violence, no weapon, no physical contact, no eye contact between the two women — the drop is the whole letter.

LIGHT GUARD — IMPORTANT: early evening gloom in the walkway, one paper lantern glowing dimly behind. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No whispered urgency visible — the face never changes.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the senior court lady passing the court lady in a narrow evening walkway, both bowing slightly, one dim paper lantern behind.
2. 85mm, static: a small folded blank paper note slipping from the senior lady's silk sleeve, falling between the two women unseen.
3. 85mm close, static: the court lady's face perfectly composed, only her eyes dropping a fraction toward the falling note.

NOTE AND SLEEVE MOTION — IMPORTANT: physically-based the folded note falling with real paper weight, silk sleeves settling after the bow, a held breath visible in the shoulders. Do NOT follow the sketch's static lines — the passing must feel like real filmed footage. The note is folded and blank to the camera — its words belong to the sound mix, no characters, no glyphs.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 버선발 밑으로 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP15_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 떨어진 쪽지가 설화의 버선발 밑으로 감춰진다. [서늘한 각성 속마음 · 설화/`ko-KR-Neural2-A`, Pitch -1.0] "만나지 않아도 — 이미 시작되었나이다." (rel 3.5=절대 47.5) **매크로 1컷 한정 — 이후 휴먼 스케일로 탈출(정본 AG ①).**
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. She is alone in her quarters. All characters are adults. No violence, no weapon, no injury, no blood — a note being hidden by a foot is the entire event.

LIGHT GUARD — IMPORTANT: the last evening light at the window, one low oil lamp. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No trembling, no glancing around — she has done this before.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a small folded blank paper note sliding out of sight beneath the white beoseon sock of a kneeling woman's foot on dark floorboards.
2. 85mm close, static: her face by one low oil lamp, serene, the words already memorized behind her eyes.
3. 50mm, static: she smooths her skirt down over her knees and feet, the plain room ordinary again.

CLOTH AND FLOOR MOTION — IMPORTANT: physically-based the note sliding with the smallest paper friction, white cloth settling with real fabric weight, measured breathing. Do NOT follow the sketch's static lines — the hiding must feel like real filmed footage. One macro passage only, then out to human scale. The note is folded and blank to the camera — no characters, no glyphs.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 닫히는 문 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP15_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 닫히는 수라간 문 → 암전 → 타이틀. **붉은 타이틀(제16화 「궁의 비밀통로」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations and real objects.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — objects only, no face in frame, no figures close to camera, only distant officer silhouettes with lanterns beyond the gate. No violence, no drawn weapon, no blade visible, no injury — only a gate closing in the night.

LIGHT GUARD — IMPORTANT: moonlight on the closing gates, the officers' lanterns beyond as the only light. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no final line, no music sting staging.

Recreate the panels in order as one continuous ~10 second sequence:
1. 50mm, static: at night the two heavy wooden gate leaves swinging slowly together, officers' lanterns glowing beyond, moonlight on the wood.
2. 50mm, static: the last narrow gap closing, a thin vertical slit of lamplight on the ground narrowing.
3. The frame slowly dims — the slit of light thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

GATE AND FADE MOTION — IMPORTANT: physically-based gate leaves closing with real wooden mass, the last slit of light narrowing, lamplight thinning until complete black. Do NOT follow the sketch's static lines — the closing must feel like real filmed footage. The gate seals and every plaque on it is blank: no characters, no glyphs, no labels. No horror staging, no dramatic score — a door that closes on a matter it cannot close.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP15_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 35mm 새벽 봉인 · 봉인지 무문자 · 문틈 김 내레이션 착지 |
| S02 | 07.5~15.0 | 3컷 | EP15_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm · 장부 낙점은 긁어낸 자국만 · 매크로 1컷 |
| S03 | 15.0~22.5 | 4컷 | EP15_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 100mm 매크로 1컷+와이드 교차(AG ①) · 무결 손에 흙 |
| S04 | 22.5~30.0 | 3컷 | EP15_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 50mm 투숏 · 동등한 동지 · 로맨스 맹세·의존 배제 |
| S05 | 30.0~37.5 | 4컷 | EP15_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 24mm 와이드 · 무대사 무음 · 강제 개입·파손 0 |
| S06 | 37.5~45.0 | 3컷 | EP15_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm · 쪽지는 접힌 무문자 · 신체 접촉·시선 접촉 0 |
| S07 | 45.0~52.5 | 3컷 | EP15_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 매크로 1컷 한정 · 버선발 은닉 · 속마음 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP15_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 문 닫힘·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤, **Pitch 0.0**) | rel 3.0 | 절대 2.0 | 문은 닫혔으나 — 문틈으로 새는 숨은 막지 못했다. |
| 2 | S02 | 윤경헌 `ko-KR-Wavenet-D` (서늘한 만족, Pitch -2.5, Speed 0.9) | rel 3.5 | 절대 9.5 | 청분이 나간 날 — 기록이 지워진 자가 있다. |
| 3 | S03 | 무결 `ko-KR-Wavenet-C` (묵직한 절제, **Pitch -1.5**) | rel 3.0 | 절대 16.5 | 발자국은 셋이었으나 — 이제 둘입니다. |
| 4 | S04 | 설화 `ko-KR-Neural2-A` (낮은 합의, Pitch -1.0) | rel 4.5 | 절대 24.5 | 장부는. |
| 5 | S04 | 무결 `ko-KR-Wavenet-C` (묵직한 절제, **Pitch -1.5**) | rel 6.5 | 절대 26.5 | 돌아오지 못할 곳으로 보냈습니다. |
| 6 | S05 | (무대사 — 군관들의 발소리만 · 효과음) | — | — | 무음 통과 · 자막 없음 |
| 7 | S06 | 서 상궁 `ko-KR-Neural2-B` (비밀스러운 낮은 속삭임, Pitch -0.5, Speed 0.95) | rel 3.0 | 절대 39.5 | 오늘 밤 — 아무도 만나지 마라. |
| 8 | S07 | 설화 `ko-KR-Neural2-A` (서늘한 각성 속마음, Pitch -1.0) | rel 3.5 | 절대 47.5 | 만나지 않아도 — 이미 시작되었나이다. |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제16화 「궁의 비밀통로」에서 계속 |

- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: **무결과 내레이션이 동일 축 `ko-KR-Wavenet-C`**이며 S01·S03·S04가 한 화에 공존한다. 혼동 차단 4중 장치를 강제한다 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 내레이션 `EP15_S1_NARRATION`, 무결 `EP15_S3_MUGYEOL` / `EP15_S4_MUGYEOL`, ③ **피치 차등을 매 행 강제 표기**(무결 Pitch -1.5 묵직한 절제 / 내레이션 Pitch 0.0 다큐 중립 — 무결은 아래로 가라앉고 내레이션은 중립 축, 차 1.5, 본 표 1·3·5번 행), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인(무결은 인물 톤으로 밀착되고 내레이션은 다큐 중립으로 떠 있는지). 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 설화 `Neural2-A`(S04 발화 1건 + S07 속마음 1건), 윤경헌 `Wavenet-D`(S02 단독), 서 상궁 `Neural2-B`(S06 단독 — 본 화 나인들 대사 없음)는 충돌 없는 단독 배역 축이다.
- S04의 교환은 정본 블록(rel 4.5=절대 24.5) 내 배치다 — 설화 단문을 블록 선두(절대 24.5)에, 무결의 회답을 후행 2.0초(절대 26.5)에 놓는다. 후행 간격은 믹싱 배치 지문이며 정본 절대 축은 그대로 유지한다.
- S07의 설화 대사는 **속마음**이다 — 렌더는 무음이며, 믹싱에서 잔향 얕은 클로즈 보이스로 처리하고 자막은 정본 문구 그대로 노출한다.
- S05는 무대사다 — 군관들의 발소리를 효과음 레이어로만 깔고 자막을 붙이지 않는다.
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(확정 EP15 8썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:04,500
문은 닫혔으나 —
문틈으로 새는 숨은 막지 못했다.

2
00:00:09,500 --> 00:00:12,800
청분이 나간 날 —
기록이 지워진 자가 있다.

3
00:00:16,500 --> 00:00:19,300
발자국은 셋이었으나 —
이제 둘입니다.

4
00:00:24,500 --> 00:00:25,400
장부는.

5
00:00:26,500 --> 00:00:29,800
돌아오지 못할 곳으로 보냈습니다.

6
00:00:39,500 --> 00:00:42,000
오늘 밤 — 아무도 만나지 마라.

7
00:00:47,500 --> 00:00:51,000
만나지 않아도 —
이미 시작되었나이다.

8
00:00:59,000 --> 00:01:00,000
제16화 「궁의 비밀통로」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- 1번 블록(내레이션)은 `EP15_S1_NARRATION`, 3·5번 블록(무결)은 `EP15_S3_MUGYEOL` / `EP15_S4_MUGYEOL`, 4번 블록(설화 발화)은 `EP15_S4_SEOLHWA`, 7번 블록(서 상궁)은 `EP15_S6_SENIOR`, 8번 블록(설화 속마음)은 `EP15_S7_SEOLHWA`로 분리 저장한다 — 무결·내레이션 동일 ID 차단(§0-12)에 따라 트랙·파일 모두 분리한다.
- 4·5번 블록(설화 단문·무결 회답)은 2.0초 간격으로 분리 저장해 믹싱에서 붙인다 — 한 파일에 이어 붙이지 않는다.
- SRT 전 블록에 위험 어휘·설명 대사 0건 — 정본 문구 그대로다.
