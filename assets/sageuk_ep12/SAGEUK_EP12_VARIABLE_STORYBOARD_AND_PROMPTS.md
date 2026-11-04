# 「혈화의 궐」 EP12 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제12화 「쥐새끼의 반격」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04~EP11 원장 운용 결과
> **범위**: EP12 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 본 화는 설화의 역공 — 밀정 나인을 통과해 윤경헌의 귀를 그 귀의 주인에게 파는 회전이다. **지략 자랑 슬롭 전면 금지**: ["역시 나였다" 식 승리 선언]은 삭제 정본대로 치환됐다 — 함정이 허무하게 무너지는 **그림**만이 존재하고, 설화는 승리를 입으로 밝히지 않는다(AG ①: 역공 설명 대사 배제, 시각만으로 승부). **고문·위협 과장 금지**: 윤경헌의 추궁은 고문 협박이 아니라 **낮게 깔린 질문 한 줄**이며, 정지·붙잡기·난폭함 일체 없다. **대가를 치르는 구조(정본 비판 검수)**: 설화는 밀정 나인 하나를 의도적으로 놓아주는 비용을 치르고(칼로 막지 않고 길을 열어줌), 그 뒤로는 계속 의심받는다(S07 어둠 속 눈) — 쉬운 승리 연출 금지. **밀정 나인 고정 외형 앵커 신설(AG ⑥)**: 본 화 신설 조선(조연) — `characters.md` 미등록이므로 본 원장 §0-7에 고정 시각 프롬프트를 등록해 전 썬 동일 문구 투입한다. **동일 보이스 ID 이중 배역**(무결·내레이션 모두 `Wavenet-C`) — 트랙 분리 합성과 파일명 규칙(`EP12_S6_MUKYEOL` / `EP12_S7_NARRATION`)으로 혼동 차단(정본 AG 검수 ⑦). **무흉기 화**: 전 썬 무기 미인출 — 무결의 환도는 칼집째 존재만 확인된다.

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **우물·소매**(well rope turning, laundry baskets swaying, sleeve fabric settling), S02 **바둑돌·황혼**(the stone held with real finger weight, dusk light dying in the yard), S03 **등불·숨**(lamp flames breathing, a held breath, the kneeling weight), S04 **종이·손**(paper fiber creasing, trembling fingers with real joint stiffness), S05 **문등·밤공기**(gate lantern glow, night air moving the grass, a measured half-turn), S06 **등롱·복식**(lantern glow through paper, uniform fabric settling), S07 **회랑 종심**(receding lanterns thinning, pillar rhythm with real parallax), S08 **눈 감김·암전**(lids lowering with real weight, ambient light dying in a smooth fade). 스케치의 정적 선 추종 차단.
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·상해·직접 대치 일체 없음. 본 화는 무흉기 화다 — 윤경헌의 추궁은 질문이고, 설화의 무기는 길을 열어주는 선택이다. **고문 위협 과장 차단**: `no torture, no threats staged as violence, no grabbing, no shouting` 전 썬 명시. **지략 자랑 차단**: `no triumph, no victory smile, no gloating` — 함정의 붕괴는 결과의 그림으로만 보인다.
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지. (EP07~EP10 재발 방지: 설화 앵커의 **귀걸이·수술·가체·떨잠 금지 전 썬 상향 고정** 유지. EP12 신설: **밀정 나인 고정 외형 앵커** — 정본 AG 검수 ⑥ 요구를 본 원장에서 이행, 전 썬 동일 문구 투입. 소품 무문자 지문을 패널 서술 안에서도 반복 기입.)
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok
   - **윤경헌**: a 58-year-old Joseon prime minister (fictional court minister Yoon Gyeong-heon), dark crimson danryeong official court robe with rank embroidery, black horsehair samo official hat, thin gray beard, cold suspicious hawk eyes, deep wrinkles of power — his menace is a quiet question only, no shouting, no threats
   - **밀정 나인(신설 조연 앵커)**: the spy maid is a young low-ranking court maid, round pale face, hair in a tight braid with a single dull red daenggi ribbon, plain pale blue-grey servant hanbok, no ornaments, anxious darting eyes — the same maid in every scene
   - **무결**: a 25-year-old Joseon warrior captain, faint scar across his cheekbone, dark navy yungbok military uniform, a curved sword remaining sheathed at his hip — the blade never drawn, never touched
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제13화 「후궁의 등장」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 눈 감김 → 완전 암전 유지만. (시트의 4컷 엔드카드 패널은 편집 가이드다.)
10. **광원 표기(정본 AG 검수 ① 준수)**: 키 라이트 모티베이션 필수 — S01 `late-afternoon natural light over the courtyard, no lamps`, S02 `dusk afterglow in the yard, lamplight inside the sarangchae`, S03 `standing paper lamps in the great hall`, S04 `the same standing lamps`, S05 `one gate lantern and moonlight only`, S06 `a single paper lantern`, S07 `thin guttering lanterns down the corridor, darkness at the far end`, S08 `the last lamplight on the eyes, then darkness`. **완전 암부 디테일 소실 금지**: `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness`. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **문서·물체 텍스트 슬롭 방지(정본 AG 검수 ① 준수 + EP10·EP11 관찰 메모 반영)**: S01·S04의 접힌 종이 쪽지, S03의 현판·휘장 등 모든 소품 문서·간판은 `blank paper texture, no letters, no glyphs, no readable marks`, `blank wood plaque, no characters` — **패널 서술 안에서도 반복 기입**한다(EP11 S03 현판 글리프 결함 재발 방지). EP12는 가독 글자 인서트가 **한 건도 없다** — 유일 예외 없음. S08의 붉은 한글 타이틀은 시트 한정 요소이며 실사 렌더에서 금지(§0-9, 편집 삽입).
12. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦)**: **무결과 내레이션이 모두 `ko-KR-Wavenet-C`**다. 혼동 차단 4중 장치를 강제한다 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 무결 `EP12_S6_MUKYEOL`, 내레이션 `EP12_S7_NARRATION`, ③ 무결 대사에 `묵직하고 절제된 무사 톤(Pitch -1.5)` 지문을 **매 행 강제 표기**, ④ 믹싱 단계에서 Pitch·톤 축 확인(무결 -1.5 무사 톤 / 내레이션 다큐 톤). 밀정 나인은 `ko-KR-Neural2-B`(평정심이 무너지는 젊은 나인, Pitch -0.5) — 설화 `Neural2-A`와 별도 축이므로 본 화 내 동일 ID 충돌은 무결-내레이션 1조다. 하나라도 누락되면 재합성한다.

---

## 1. S01 미끼의 자리 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP12_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 뒤따름 — 밀정 나인이 가짜 정보를 풀어놓는 자리. [연기하는 서늘함 · 설화/Neural2-A] "그리 되겠지요. 대전 약탕은 내일 다시 짓겠지요." (rel 3.0=절대 2.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok. The spy maid is a young low-ranking court maid, round pale face, hair in a tight braid with a single dull red daenggi ribbon, plain pale blue-grey servant hanbok, no ornaments, anxious darting eyes. Kitchen maids in plain neat court dress with plain hair. No king on screen, no royal figure in this scene. No violence, no weapon.

DAYLIGHT GUARD — IMPORTANT: late-afternoon natural light over the courtyard, no lamps. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The routine itself is the trap: no villain staging, no scheming looks into camera — only ordinary palace work that happens to carry a lie.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm, tracking follow shot: a sunlit late-afternoon palace courtyard by a stone well, maids carrying laundry baskets, the spy maid pausing to whisper to another maid, the court lady small in the far background with her back half-turned.
2. 85mm close, static: the spy maid's face — a casualness that rehearses itself, a faint smile that never reaches her anxious darting eyes.
3. 50mm, static: the court lady by a wooden pillar at a distance, cold still profile, giving nothing away.
4. 100mm macro insert, static: a folded paper note passed unseen between two maids' sleeves — blank paper texture, no letters, no glyphs, no readable marks anywhere.

WELL AND SLEEVE MOTION — IMPORTANT: physically-based well rope turning, laundry baskets swaying with real weight, sleeve fabric settling, her stillness with real body weight. Do NOT follow the sketch's static lines — the working courtyard must feel like real filmed footage. No triumph, no gloating — the bait is served quietly, inside the routine.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 사랑채에 닿은 귀 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP12_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 — 그 정보가 사랑채에 도달, 윤경헌의 손이 멈춤. [긴 세월의 냉소 · 윤경헌/Wavenet-D] "…이미 아는 것을, 알려주는 건가." (rel 3.0=절대 9.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the minister is a 58-year-old Joseon prime minister (fictional court minister Yoon Gyeong-heon), dark crimson danryeong official court robe with rank embroidery, black horsehair samo official hat, thin gray beard, cold suspicious hawk eyes, deep wrinkles of power — his menace is a quiet question only, no shouting, no threats. A maidservant bowing in the yard, plain dress, unremarkable face. No violence, no weapon.

DUSK LIGHT GUARD — IMPORTANT: dusk afterglow dying in the yard, warm lamplight inside the sarangchae room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Suspicion arrives as stillness, not as drama.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 135mm compressed telephoto, static: across the sarangchae yard at dusk, a maidservant bowing small and distant before the lamplit room where the old minister sits silhouetted, the compression stacking roof lines and distance between them.
2. 100mm macro, static: the minister's aged hand holding a go stone, frozen mid-motion above the wooden board — the stopped hand is the entire alarm.
3. 85mm close, slow push-in: his face turning a fraction, a cold ancient smirk with long years of contempt in it, suspicious narrow eyes.

GO STONE AND DUSK MOTION — IMPORTANT: physically-based finger weight on the stone, the dusk light dying in the yard, the push-in with steady real parallax. Do NOT follow the sketch's static lines — the arrival of the news must feel like real filmed footage. No slammed board, no snarled reaction — a stopped hand and an old smile do all the work.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 되묻는 자리 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP12_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 윤경헌이 밀정에게 되묻는다. [낮게 깔린 위협 · 윤경헌/Wavenet-D] "그 나인의 입 — 어느 쪽 입이냐. 네 것이냐, 그것의 것이냐." (rel 3.5=절대 17.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the minister is a 58-year-old Joseon prime minister (fictional court minister Yoon Gyeong-heon), dark crimson danryeong official court robe with rank embroidery, black horsehair samo official hat, thin gray beard, cold suspicious hawk eyes, deep wrinkles of power — his menace is a quiet question only, no shouting, no threats, no gestures. The spy maid is a young low-ranking court maid, round pale face, hair in a tight braid with a single dull red daenggi ribbon, plain pale blue-grey servant hanbok, no ornaments, anxious darting eyes. No violence, no weapon.

LAMP LIGHT GUARD — IMPORTANT: standing paper lamps light the great hall. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. No torture, no threats staged as violence, no grabbing — a quiet question does the work, and the room's geometry answers for him.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot, static: the minister seated in lamplight, the spy maid kneeling far across the wooden floor, strict hierarchy distance kept between them.
2. 85mm close, static: his face leaning neither forward nor back, the quiet leveled question in his eyes, unhurried.
3. 100mm macro, static: her small fists clenched tight on her skirt, white knuckles, fine trembling.
4. 50mm wide from behind his shoulder, static: a tiny kneeling figure in a vast cold wooden room, bare wooden walls, the hanging wall plaque completely blank wood with no characters.

LAMP AND BREATH MOTION — IMPORTANT: physically-based lamp flames breathing, her held breath, the kneeling weight settling into the floor. Do NOT follow the sketch's static lines — the interrogation must feel like real filmed footage. No raised voice, no slammed table — stillness is the pressure.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 놓친 종이 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP12_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 밀정 나인의 손, 종이를 쥐다 놓침. [평정심의 붕괴 · 밀정 나인/Neural2-B] "저, 저는…" (rel 2.0=절대 23.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the spy maid is a young low-ranking court maid, round pale face, hair in a tight braid with a single dull red daenggi ribbon, plain pale blue-grey servant hanbok, no ornaments, anxious darting eyes. No other face close to camera. No violence, no weapon.

LAMP LIGHT GUARD — IMPORTANT: the same standing lamps light the room. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. The body betrays before the tongue — no tears yet, only the mechanism failing.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm extreme macro, static: her fingers crushing a folded paper note — blank paper texture, no letters, no glyphs, no readable marks — white knuckles, fine trembling line of effort.
2. 100mm macro, static: the grip failing, the paper slipping loose from her fingers and falling toward the wooden floor.
3. 85mm close, static: her round pale face, composure collapsing, eyes wide with darting panic, mouth barely open, words leaving before wits return.

PAPER AND FINGER MOTION — IMPORTANT: physically-based paper fiber creasing under real finger pressure, the trembling with real joint stiffness, the paper falling with true weight. Do NOT follow the sketch's static lines — the composure breaking must feel like real filmed footage. No melodramatic gasp, no fainting — a professional mask coming apart one joint at a time.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 열어주는 길 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP12_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 문 앞 — 설화가 그 나인을 만나, 조용히 길을 내줌. [차가운 계산 · 설화/Neural2-A] "가라. 그리고 사랑채에 — 오늘 밤 무엇을 봤는지 그대로 말해라." (rel 4.0=절대 32.0)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache, no elaborate hair ornaments — elegant dark pastel hanbok, plain collar with a single plain ribbon tie. The spy maid is a young low-ranking court maid, round pale face, hair in a tight braid with a single dull red daenggi ribbon, plain pale blue-grey servant hanbok, no ornaments, anxious darting eyes. No violence, no weapon.

GATE LIGHT GUARD — IMPORTANT: one gate lantern and moonlight only. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Mercy as a ledger entry: she does not block the spy — she opens the way, and no triumph shows on her face.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: a small round moon gate at night lit by one gate lantern, the spy maid hurrying toward it, the court lady standing calmly in her path.
2. 85mm close, static: the court lady's calm face, stepping aside with a measured half-turn to open the way, her bare ears and plain jade rod clearly visible.
3. 50mm, static: the spy maid hurrying past through the opened path, head bowed low, not daring to look up, the court lady still at the frame edge.
4. 100mm macro insert, static: the court lady's dark eyes tracking the fleeing figure, unreadable, a costly choice settling into stillness.

LANTERN AND NIGHT AIR MOTION — IMPORTANT: physically-based gate lantern glow breathing, night air moving the grass, her measured half-turn with real body weight. Do NOT follow the sketch's static lines — the opening of the way must feel like real filmed footage. No victory smile, no villain wink — the price is paid with open eyes and the ledger stays hidden.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 반대하는 목소리 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP12_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 무결이 그 선택을 듣고, 반대한다. [억누른 불안 · 무결/Wavenet-C] "아기씨. 그자의 눈은 이제 아기씨에게 붙습니다." (rel 3.0=절대 39.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the warrior captain is a 25-year-old Joseon military officer, faint scar across his cheekbone, dark navy yungbok military uniform, a curved sword remaining sheathed at his hip — the blade never drawn, never touched. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a single plain undecorated jade hairpin — no tassels, no dangling ornaments, no earrings, no face veil, no gache — elegant dark pastel hanbok. No violence, no weapon drawn.

LANTERN LIGHT GUARD — IMPORTANT: a single paper lantern lights the corridor. Deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness. Objection without a raised voice — the argument is the only weapon in this scene.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm, static: the warrior captain under moonlit corridor eaves, head slightly bowed as he objects, the sheathed sword undisturbed at his hip.
2. 50mm, static: the court lady backlit by a paper lantern, perfectly still, listening, face unreadable.
3. 85mm close, slow push-in: the captain's scarred face, jaw tight, suppressed anxiety held in the eyes, the voice never raised.

LANTERN AND FABRIC MOTION — IMPORTANT: physically-based lantern glow through the paper, uniform fabric settling, her unmoving stillness with real body weight. Do NOT follow the sketch's static lines — the objection must feel like real filmed footage. No grabbing her arm, no anguished outburst — worry he is not permitted to raise his voice into.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 돌아온 눈 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP12_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 회랑 종심 — 회랑 끝, 어둠 속 눈 한 쌍. [무거운 나레이션 · 내레이션/Wavenet-C] "쥐의 반격은 — 쥐의 눈을 돌아오게 한다." (rel 3.5=절대 47.5)
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — figures in shadow and objects only, no visible face close to camera — at most a single pair of eyes catching lamplight in the far darkness. No violence, no weapon.

CORRIDOR LIGHT GUARD — IMPORTANT: thin guttering lanterns down the corridor, darkness thickening at the far end. Deep shadow areas must keep readable detail until the final beat — no crushed blacks, no milky flat darkness. The counterattack gives the mouse its eyes back: suspicion is the price that stays.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm ultra-wide, static: deep one-point perspective of a long moonlit wooden palace corridor at night, repeating pillars receding into total darkness at the far end.
2. 50mm, slow push-in: down the corridor, lanterns thinning, the darkness at the far end thickening.
3. 85mm close, static: deep in the far darkness a single pair of eyes catching the last lamplight, unblinking, watching back — no face visible, only the eyes.

CORRIDOR AND LANTERN MOTION — IMPORTANT: physically-based receding lanterns with real parallax, pillar rhythm sliding past on the push-in, the eyes holding perfectly still. Do NOT follow the sketch's static lines — the watching corridor must feel like real filmed footage. No jump-scare sting, no monster reveal — only the economy of being watched.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 눈 감김 → 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP12_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드 — 어둠 속 눈이 감김 → 암전. **붉은 타이틀(제13화 「후궁의 등장」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — figures in shadow and objects only, no visible face close to camera — a single pair of eyes in darkness, nothing else. No violence, no weapon.

DYING LIGHT GUARD — IMPORTANT: the last lamplight on the eyes, then darkness gathers. Deep shadow areas must keep readable detail until the fade — no crushed blacks, no milky flat darkness. This is a silent cliffhanger: no words, no farewell gesture.

Recreate the panels in order as one continuous ~10 second sequence:
1. 50mm, static: a single pair of dark eyes deep in darkness, holding still, unblinking, catching faint lamplight, no face visible.
2. 50mm, slow: the eyes slowly closing, the lids sinking with real weight into darkness.
3. The frame slowly dims — the last lamplight thinning until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

EYES AND DARKNESS MOTION — IMPORTANT: physically-based lids lowering with real weight, the lamplight dying in a smooth cinematic fade to black. Do NOT follow the sketch's static lines — the mouse being done running for tonight must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 4컷 | EP12_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 50mm 뒤따름 · 우물가 일상의 미끼 · 지략 자랑 0 |
| S02 | 07.5~15.0 | 3컷 | EP12_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 135mm 압축 · 멈춘 바둑돌 손 · 고난 냉소 |
| S03 | 15.0~22.5 | 4컷 | EP12_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 85mm 투숏 · 낮게 깔린 질문 · 고문 협박 과장 0 |
| S04 | 22.5~30.0 | 3컷 | EP12_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 100mm 매크로 · 종이를 쥐다 놓침 · 종이 무문자 |
| S05 | 30.0~37.5 | 4컷 | EP12_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 35mm 문 앞 · 길을 열어주는 대가 · 승리 연출 0 |
| S06 | 37.5~45.0 | 3컷 | EP12_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 85mm 무결 반대 · 환도 미인출 · 고조된 목소리 0 |
| S07 | 45.0~52.5 | 3컷 | EP12_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 24mm 회랑 종심 · 어둠 속 눈 한 쌍 · 인물 얼굴 미등장 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP12_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 눈 감김·암전 · 엔드카드는 편집 삽입 · 무음 클리프행어 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 설화 `ko-KR-Neural2-A` (연기하는 서늘함, Pitch -1.0) | rel 3.0 | 절대 2.0 | 그리 되겠지요. 대전 약탕은 내일 다시 짓겠지요. |
| 2 | S02 | 윤경헌 `ko-KR-Wavenet-D` (긴 세월의 냉소, Pitch -2.5, Speed 0.9) | rel 3.0 | 절대 9.5 | …이미 아는 것을, 알려주는 건가. |
| 3 | S03 | 윤경헌 `ko-KR-Wavenet-D` (낮게 깔린 위협, Pitch -2.5, Speed 0.9) | rel 3.5 | 절대 17.5 | 그 나인의 입 — 어느 쪽 입이냐. 네 것이냐, 그것의 것이냐. |
| 4 | S04 | 밀정 나인 `ko-KR-Neural2-B` (평정심의 붕괴, Pitch -0.5) | rel 2.0 | 절대 23.5 | 저, 저는… |
| 5 | S05 | 설화 `ko-KR-Neural2-A` (차가운 계산, Pitch -1.0) | rel 4.0 | 절대 32.0 | 가라. 그리고 사랑채에 — 오늘 밤 무엇을 봤는지 그대로 말해라. |
| 6 | S06 | 무결 `ko-KR-Wavenet-C` (억누른 불안, Pitch -1.5) | rel 3.0 | 절대 39.5 | 아기씨. 그자의 눈은 이제 아기씨에게 붙습니다. |
| 7 | S07 | 내레이션 `ko-KR-Wavenet-C` (무거운 다큐 톤) | rel 3.5 | 절대 47.5 | 쥐의 반격은 — 쥐의 눈을 돌아오게 한다. |
| 8 | S08 | (편집 삽입 · 무성) | rel 7.5 | 절대 59.0 | 제13화 「후궁의 등장」에서 계속 |

- **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ — 본 원장 핵심 지문)**: 무결과 내레이션이 **동일 축 `ko-KR-Wavenet-C`**를 쓴다. 혼동 차단 4중 장치를 강제한다 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 오디오/자막 파일명 규칙 준수: 무결 `EP12_S6_MUKYEOL`, 내레이션 `EP12_S7_NARRATION`, ③ 무결 대사에 `묵직하고 절제된 무사 톤(Pitch -1.5)` 지문을 **매 행 강제 표기**(본 표 6번 행), ④ 믹싱 단계에서 Pitch·톤 축 확인(무결 -1.5 무사 톤 / 내레이션 다큐 톤). 이는 EP01에서 동일 ID 운용으로 검증된 절차를 EP12에 재적용한 것이다 — 위 4중 장치 중 하나라도 누락되면 재합성한다.
- 밀정 나인 `ko-KR-Neural2-B`는 중전(EP11 등장)과 동일 축이나 본 화 내 중전 미등장으로 충돌 없음 — 단 본 화 내 설화 `Neural2-A`와의 구분을 위해 Pitch -0.5·톤 지문(평정심의 붕괴)을 매 행 유지한다.
- 보이스 ID는 `characters.md` 고정 음성 원장을 그대로 준용했다: 설화 `Neural2-A`(Pitch -1.0), 윤경헌 `Wavenet-D`(Pitch -2.5, Speed 0.9), 무결 `Wavenet-C`(Pitch -1.5), 내레이션 `Wavenet-C`(다큐 톤), 밀정 나인 `Neural2-B`(신설 조연 — §0-7 시각 앵커와 짝을 이루는 음성 원장).
- 정본 썬표의 rel·절대 표기를 그대로 따랐다(마스터 각본 제12화 썬표 기준).

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,000
그리 되겠지요.
대전 약탕은 내일 다시 짓겠지요.

2
00:00:09,500 --> 00:00:11,500
…이미 아는 것을,
알려주는 건가.

3
00:00:17,500 --> 00:00:20,500
그 나인의 입 — 어느 쪽 입이냐.
네 것이냐, 그것의 것이냐.

4
00:00:23,500 --> 00:00:24,500
저, 저는…

5
00:00:32,000 --> 00:00:35,500
가라. 그리고 사랑채에 —
오늘 밤 무엇을 봤는지 그대로 말해라.

6
00:00:39,500 --> 00:00:42,500
아기씨. 그자의 눈은
이제 아기씨에게 붙습니다.

7
00:00:47,500 --> 00:00:50,000
쥐의 반격은 —
쥐의 눈을 돌아오게 한다.

8
00:00:59,000 --> 00:01:00,000
제13화 「후궁의 등장」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- 4번 블록(밀정 나인 "저, 저는…")은 끊긴 대사 — 실제 발화의 침묵(23.5~24.5)까지 자막 노출을 유지해 평정심의 붕괴 리듬을 보존한다.
- 6번 블록(무결)과 7번 블록(내레이션)은 동일 ID 이중 배역 — 자막 파일도 규칙에 따라 분리 저장한다(§10-1 ②).
- 보이스 ID 운용: 고정 ID + 감정 톤 지문(연기하는 서늘함/긴 세월의 냉소/낮게 깔린 위협/평정심의 붕괴/차가운 계산/억누른 불안/무거운 나레이션)으로 썬별 미묘함을 구분한다.
