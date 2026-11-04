# 「혈화의 궐」 EP37 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제37화 「회랑의 피바람」 8썬표(`master_screenplay/SEASON_02_MASTER_SCREENPLAY.md` 행 220~240, 원전: 제37장 정본) + `characters.md` 캐릭터 앵커 + EP20~EP36 원장 템플릿(동일 규격)
> **범위**: EP37 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 회랑의 피바람**: 중궁전 앞마당 회랑 — 자객 다섯. **액션 슬로우모션 남발 배제(정본 안티슬롭)** → 치환 [좁은 목조 회랑의 협소 지형이 유일한 벽이라는 공간 논리] — 회랑의 좁음이 싸움의 조건이며, 스피드램프는 S3 첫 컷 단 한 번(정본 지정 연출), 나머지는 통상 가변 호흡. **피/시신 직접 묘사 배제(AG 검수 ②)** → 빗물 젖은 마루판(`rain-soaked corridor`)·부서진 목재 파편(`wooden debris`)·쇠와 쇠의 충돌로 치환 — "피 위에서 돌아보는 두 사람"(S6)도 젖은 마루판 반사광으로 운반, `no blood, no wounds, no injuries anywhere` 전 썬 상설. **벽 붕괴는 목재 패널 파열** — `wall panel bursting on its joints`, 파편은 목재 한정(AG 검수 ①). **소품·복선 인계(EP36 → EP37)**: EP36 S8 문 앞 발소리의 정체 불명 인물 복선이 본화 회랑에서 회수되고, 본화 S8 엔드카드 「제38화 추적의 발자국에서 계속」이 EP38 강가 밤배 추적(뱃사공 조연 등장 예정 — `characters.md` 등록 필수, 정본 AG ⑥)으로 이어진다. **무결 나이 앵커(EP37 plan 지정)**: **28세 청년 무관 앵커 고정 — 노화 금지** — `characters.md` 시즌1 등록치(25세)를 대신하며 시즌2 경과 반영치다. 시트·프롬프트 전부 `28 years old, clean-shaven, no beard` 인라인(EP36 결함 이력 ①의 재발 방지 지침 이행). **자객 다섯 무명 가드**: 검은 홑이·복면 — 얼굴 각인 금지, 다음 화 재등장 전제 없음, `all characters are adults`. **무결-내레이션 동일 보이스 ID(`ko-KR-Wavenet-C`) 이중 배역** — EP15 4중 장치 계승(트랙 분리 합성·파일명 규칙·피치 차등·믹싱 실측), §0-13 참조. **킬러 컷 미배정**: EP37은 특수 훅 허용 화(EP30·EP41·EP49·EP50)가 아님 — 초슬로우 훅 재투입 없음, S3 스피드램프 1컷은 정본 썬표 지정 연출.

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (온광·냉기 교차 모티베이션) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **등불의 소멸**(the lantern flames dying one by one, the wet boards reflecting the last warm circle, the rain drifting past the open gallery), S02 **복면의 침묵**(the hooded cloth breathing in the cold air, her sleeve settling around the reversed hairpin, the rain sheen holding), S03 **패널의 파열**(the wall panel bursting on its joints, the wooden debris scattering with real weight, the lantern light swinging on its cords), S04 **쇠와 쇠의 한 번**(metal meeting metal once and checking, the hairpin's silver catching the lantern light, the boards' rain sheen holding), S05 **지나간 바람**(the lantern flames bending one way in a cold draft and steadying, the debris settled, the rain thinning), S06 **젖은 마루의 반사**(breath and wet cloth, the relit lantern steady, the rain-soaked boards gleaming), S07 **천 위의 천**(the shadows moving unhurried, cloth settling over cloth, the lantern light barely swinging), S08 **재점화**(the flames taking one by one, the wet boards warming under the returned light, the rain ended).
5. **세이프 필터(본화 최우선 가드)**: 회랑 액션은 **비그래픽 무대화된 사극 액션** — `staged, non-graphical historical action, no blood, no wounds, no injuries anywhere` 전 썬 상설. 시신·유혈·상처 묘사 일체 금지 — 수습(S7)은 천이 천을 감싸는 실루엣만, `no bodies shown`. 은장도는 장식 은비녀(`ornamental silver hairpin`)로 지칭해 흉기 트리거를 회피한다. 전 등장 인물 성인 — `all characters are adults`. 자객 다섯은 무명 — 얼굴 각인·이름 부여 금지.
6. **문자 가드**: 화면 노출 문자 요소 일체 금지 — `no readable letters, no characters, no labels anywhere` 상설. 등불·첩·간판에 글자를 새기지 않는다(`nothing written on the lanterns or plaques`). 엔드카드 자막(제38화 「추적의 발자국」에서 계속)은 편집 단계 삽입.
7. **입모양 배제 가드(100화 전편 규격)**: 설화 발화 1구(S6)·무결 발화 1구(S6)·내레이션 2구(S1·S5)는 전부 무음 렌더 + 사후 믹싱 — 화면은 **입모양 배제**, `lips closed throughout` 전 썬 상설. 발화 썬은 보이스오버·리액션 샷으로 처리. S2 무언(연출 지정)·S3·S4 효과음 씬·S7·S8 무대사 — 렌더 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **설화**: a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, her resolve hidden entirely behind a court lady's stillness.
   - **무결(EP37 plan 앵커 — 28세 고정)**: a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone, a solid unbroken silence about him.
   - **자객 다섯**: five masked figures in black hooded commoner clothes, faces covered by dark cloth masks, unnamed and unremarked, all adults, no principal characters among them.
9. **광원 표기**: 시즌2 색 설계 — **석범·야기(夜氣)의 냉광과 등불의 온광 교차**. 전 썬 공통 무대(비 오는 목조 회랑) — **꺼져 가는 등불 온점/젖은 마루판의 냉 반사/갤러리 너머 야기 냉광**이 본화의 축. S01 소멸(온점이 하나씩 사라짐), S02~S04 잔존 온점과 싸움의 그림자, S05~S08 재점화(온점이 하나씩 돌아옴). 전 씬 `no crushed blacks, no milky flat darkness` — 광원 소스 명시로 완전 암부 슬롭 차단.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S08 암전 이후의 붉은 타이틀(제38화 「추적의 발자국」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9) — S1·S5 2구. **무결** `ko-KR-Wavenet-C` (Pitch -1.5, Speed 1.0, 묵직하고 절제된 무사 톤) — S6 발화 1구. **설화** `ko-KR-Neural2-A` (Pitch -1.0, Speed 1.0, 차분하고 서늘한 톤) — S6 발화 1구. 이환(Neural2-C)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. 무결-내레이션 동일 ID 이중 배역 차단은 §0-13.
13. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ 계승)**: **무결과 내레이션이 모두 `ko-KR-Wavenet-C`**이며 한 화에 공존한다. 혼동 차단 4중 장치 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 파일명 규칙 준수: 내레이션 `EP37_S1_NARRATION`·`EP37_S5_NARRATION`, 무결 `EP37_S6_MUGYEOL`, ③ **피치 차등을 매 행 강제 표기**: 무결 `Pitch -1.5` / 내레이션 `Pitch 0.0` — 차 1.5, 무결이 아래로 가라앉고 내레이션은 중립 축, ④ 믹싱 단계에서 Pitch·톤 축 실측 확인. 하나라도 누락되면 재합성한다.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/3/5/4/3/3/3/3 = 28컷 — EP21~EP36 어느 배분과도 다른 신규 배분. S3 붕괴-진입 액션 씬에 최대 5컷(격투 클라이맥스 가변 원칙 — 스피드램프 1컷 → 협소 지형 35mm → 파열 85mm → 진입 50mm → 와이드 수렴), S1 등불 소멸 4컷 롱테이크 오프닝, S8 재점화 1컷 + 암전 + 타이틀 3컷.

---

## 1. S01 등불이 하나씩 꺼진다 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP37_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 회랑 등불, 회랑의 등불이 하나씩 꺼진다. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "보름 전날 밤 — 회랑의 등불이 하나씩 꺼졌다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **무인물 오프닝 썬** — 인물 없이 등불의 소멸만으로 밤의 긴장을 쌓는다. 온점의 축소(1·2컷) → 꺼지는 화염 클로즈(3컷) → 반쯤 어두워진 회랑 와이드(4컷). `no figures anywhere` — 와이드 클로징까지 무인물 원칙.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures anywhere: the long rain-soaked wooden corridor of a Joseon palace at night, a row of warm paper lanterns, the flames dying out one by one, rain mist beyond the open gallery. Nothing written on the lanterns or the woodwork. No violence, no blood anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the last warm points of lantern light against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm medium-wide, static: the long rain-soaked wooden corridor at night, a row of warm paper lanterns, the nearest flame shrinking inside its paper.
2. 35mm medium, static: the next lantern's warm circle of light shrinking and closing on the rain-wet boards, the far end darkening.
3. 85mm close, static: a paper lantern's flame thinning to a thread and going out, rain mist drifting beyond the open side of the gallery.
4. 24mm wide, static: the corridor half dark, lanterns extinguished one by one down its length, only a few warm points left.

EXTINGUISH MOTION — IMPORTANT: physically-based the lantern flames dying one by one, the wet boards reflecting the last warm circle, the rain drifting past the open gallery — the lights go out in order and the corridor is emptied of light, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 검은 홑이가 회랑을 채움 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP37_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드, 검은 홑이가 회랑을 채움. [낮은 도전 — 무언 · 설화/`ko-KR-Neural2-A`] "…" (소매의 은장도를 거꾸로 쥠 — 무대사, 연출 지정 무언)
- **연출 특이**: **무언의 썬** — 대사·내레이션 0건, 자객 다섯의 침묵한 진입과 설화의 물러서지 않음만으로 대치를 세운다. 와이드(다섯의 진입) → 중경(홀로 선 설화) → 클로즈(거꾸로 쥔 은장도)의 3컷. `no cries, no shouts` — 진입은 조용하다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady and the five only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, her resolve hidden entirely behind a court lady's stillness — standing alone in the corridor and not stepping back. And five masked figures in black hooded commoner clothes, faces covered by dark cloth masks, unnamed and unremarked, all adults, no principal characters among them, filling the far end of the corridor. No cries, no shouts, no speech. Nothing written on the masks or the clothes. No blood anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the surviving warm points of lantern light against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: five masked hooded figures in black filling the far end of the narrow lantern-lit corridor at night, rain-soaked boards, no faces.
2. 35mm medium, static: the court lady standing alone in the corridor facing the far end, unhurried, her hem still in the cold draft.
3. 85mm close, static: her hand inside her sleeve closing around a slim ornamental silver hairpin held reversed along her wrist, the knuckles quiet.

STILLNESS MOTION — IMPORTANT: physically-based the hooded cloth breathing in the cold air, her sleeve settling around the reversed hairpin, the rain sheen holding — five figures fill the corridor and she does not step back, no cries, no shouts, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 첫 칼이 내려오고 — 벽이 무너지며 무결이 들어옴 (절대 15.0~22.5 · 콘티 5컷)

- **시트**: `downloads/EP37_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 스피드램프, 첫 칼이 내려오고 — 회랑 뒷벽이 무너지며 무결이 들어옴. [효과음: 목조 붕괴·금속 충돌] (rel 1.5=절대 15.5, 사후 믹싱 — 렌더 무음)
- **연출 특이**: **본화 액션 클라이맥스 썬(최대 5컷 배분)** — 슬로우모션 남발의 배제가 직결되는 썬. 스피드램프는 첫 칼이 꺾이는 1컷 단 한 번(정본 지정), 이후 통상 시간. 협소 지형이 유일한 벽 — 좁아서 맴돌 수 없고, 좁아서 다섯이 한 번에 들어오지 못한다(2컷). 뒷벽은 목재 패널 파열(3컷) → 무결의 진입(4컷) → 수렴 와이드(5컷). 효과음은 사후 믹싱 — 렌더 무음.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady, the inspector and the five only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin. The inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone, a solid unbroken silence about him — coming through the broken wall panel. And five masked figures in black hooded commoner clothes, faces covered by dark cloth masks, unnamed and unremarked, all adults, no principal characters among them. Staged, non-graphical historical action — no blood, no wounds, no injuries anywhere. Nothing written on the masks or the clothes. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the surviving warm points of lantern light against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm medium speed-ramp: the first blade sweeping down and being turned aside between a masked figure and the court lady, the lantern light swinging on its cord.
2. 35mm medium, static: the corridor's cramped geometry, masked figures checked by the narrow boards and posts, no room to circle wide.
3. 85mm close, static: the corridor's rear wooden wall panel bursting outward on its joints in splinters of wooden debris, lantern light flaring through the gap.
4. 50mm medium, static: the young 28-year-old clean-shaven inspector coming through the broken wall panel into the corridor, a sheathed sword at his hip, wooden debris settling around him.
5. 24mm wide, static: the five masked figures checked in the corridor between the inspector at the broken panel and the court lady, the narrow ground held.

BURST MOTION — IMPORTANT: physically-based the wall panel bursting on its joints, the wooden debris scattering with real weight, the lantern light swinging on its cords — the narrow corridor is the only wall and the fight obeys its geometry, one speed-ramp at the first turned blade and ordinary time after, no slow-motion spree, no blood anywhere, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 두 번째 칼이 은장도에 맞는 소리 (절대 22.5~30.0 · 콘티 4컷)

- **시트**: `downloads/EP37_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 은장도, 두 번째 칼이 은장도에 맞는 소리. [효과음: 금속 충돌] (rel 2.0=절대 23.5, 사후 믹싱 — 렌더 무음)
- **연출 특이**: **은빛 매크로 썬** — 싸움의 소리는 화면이 아니라 쇠와 쇠가 만나는 매크로 2컷으로 운반된다. 소매에서 튀어 오르는 은장도(1컷) → 맞붙는 쇠와 쇠(2컷) → 돌아보는 얼굴(3컷) → 한 걸음 물러나는 자객과 좁혀지는 무결(4컷). 매크로 연타 방지 — 매크로 2컷 → 85mm → 50mm 스케일 이탈. `no blood, no wounds` — 쇠는 맞고 마는다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady, the inspector and the five only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin — meeting a blade on her ornamental silver hairpin. The inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — closing in from the broken wall panel. And five masked figures in black hooded commoner clothes, faces covered by dark cloth masks, unnamed and unremarked, all adults, no principal characters among them. Staged, non-graphical historical action — no blood, no wounds, no injuries anywhere. Nothing written on the masks or the clothes. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the surviving warm points of lantern light against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the reversed ornamental silver hairpin swinging up out of the court lady's sleeve, lantern light running along the silver.
2. 100mm macro, static: a second blade met and held on the silver hairpin, metal on metal, the two checked a hand's width apart, the rain-wet boards sheening below.
3. 85mm close, static: her pale face mid-turn, cold piercing intelligent dark eyes level, red lips closed.
4. 50mm medium, static: a masked figure giving back a step down the corridor, the young clean-shaven 28-year-old inspector closing in from the broken wall panel.

CLASH MOTION — IMPORTANT: physically-based metal meeting metal once and checking, the hairpin's silver catching the lantern light, the boards' rain sheen holding — the second blade is met and turned aside, staged and non-graphical, no blood, no wounds, no injuries anywhere, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 피바람이 회랑을 지나감 — 죽은 자는 없음 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP37_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 피바람, 피바람이 회랑을 지나감 — 죽은 자는 없음. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "다행히 죽은 자는 없었다 — 왕의 어명이 그들의 죽음을 금하고 있었기 때문이다." (rel 4.0=절대 32.0, 사후 믹싱)
- **연출 특이**: **여운의 썬** — 종결의 정적을 무인물에 가깝게 운반한다. 가라앉은 파편과 젖은 마루(1컷) → 찬 바람에 한 방향으로 눕는 화염 와이드(2컷) → 다시 가라앉는 화염 클로즈(3컷). "피바람"은 시각 은유로만 — `no blood anywhere` 상설 유지.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures anywhere: the corridor gone still after the clash, rain-wet boards and settled wooden debris in the warm lantern light, a cold draft moving down the empty gallery, the rain thinning. Nothing written on the lanterns or the woodwork. No blood, no wounds, no injuries anywhere — the aftermath is wet boards and debris only. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the returning warm points of lantern light against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the corridor gone still after the clash, rain-wet boards and settled wooden debris in the warm lantern light.
2. 24mm wide, static: a cold draft moving down the empty corridor, the lantern flames bending one way together, the rain thinning beyond the open gallery.
3. 85mm close, static: a paper lantern's flame steadying again in the cold night air, the warm circle settling back on the wet boards.

DRAFT MOTION — IMPORTANT: physically-based the lantern flames bending one way in a cold draft and steadying, the debris settled, the rain thinning — the wind that passes leaves no one dead, the aftermath is wet boards and settled debris only, no blood anywhere, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 피 위에서 돌아보는 두 사람 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP37_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숙, 피 위에서 돌아보는 두 사람. [억누른 인사 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "당신 — 또." (rel 2.0=절대 39.5) / [묵직한 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "폐하의 길목은 이제 비워두기 어렵습니다. 설화 님의 길목도요." (rel 4.5=절대 41.0) — 전부 사후 믹싱 보이스오버, 입모양 배제
- **연출 특이**: **두 사람의 재회 썬** — "피 위에서"는 젖은 마루판의 반사광으로 치환(세이프티 가드). 함께 돌아섬(1컷) → 돌아보는 설화의 클로즈(2컷) → 받는 무결의 클로즈(3컷) → 침묵의 홀드(4컷). 두 발화 모두 보이스오버 — `lips closed` 엄수, 립싱크 렌더 시도 금지.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, her resolve hidden entirely behind a court lady's stillness — turning toward him over the gleam of the wet boards. And the inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone, a solid unbroken silence about him. No speech in frame, no blood, no wounds, no injuries anywhere. All characters are adults. Lips closed throughout, the words carried by voiceover only. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the relit warm lantern between them against the cold blue rainy night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm medium, static: the two of them in the broken corridor, the rain-soaked boards gleaming under the relit lantern as they turn toward each other.
2. 85mm close, static: her face looking back over her shoulder at him, cool and unreadable, red lips closed.
3. 85mm close, static: the young clean-shaven 28-year-old inspector's scarred face, level and exact, lips closed, the words carried by voiceover only.
4. 50mm medium, static: the two of them holding the silence in the broken corridor, the relit lantern light between them, the wooden debris settled.

TURN MOTION — IMPORTANT: physically-based breath and wet cloth, the relit lantern steady, the rain-soaked boards gleaming — she turns first and he answers low, both lines are voiceover, lips closed throughout, nothing graphic on the boards but their gleam. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 사라지는 자객들을 수습하는 그림자 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP37_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드, 사라지는 자객들의 시체를 수습하는 그림자. [무대사]
- **연출 특이**: **그림자의 썬** — "시체"는 화면에 존재하지 않는다(죽은 자 없음 + 세이프티 가드). 쓰러진 복면의 무리를 그림자가 천으로 감싸 옮기는 실루엣만. 먼 어둠의 실루엣(1컷) → 천 위의 천 중경(2컷) → 텅 빈 회랑 와이드(3컷). `no bodies shown, no blood anywhere` — 수습은 흔적 없음으로 완결된다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — shadowed figures and the hooded five only, no principal characters: shadowed unnamed figures drawing the fallen masked hooded figures away down the dark end of the corridor, wrapped in heavy cloth, unhurried, no faces anywhere, all adults. No bodies shown, no blood, no wounds, no injuries anywhere — only cloth drawn away and an empty corridor. Nothing written on the clothes. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm points of lantern light against the cold blue rainy night air, the far dark of the corridor deep and dim, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: shadowed figures drawing the fallen masked hooded figures away down the dark end of the corridor, unhurried, no faces, no blood anywhere.
2. 50mm medium, static: a dark shoulder and heavy cloth drawing a hooded figure away into the far dark, no faces anywhere.
3. 24mm wide, static: the corridor empty again, only rain-wet boards and warm lantern light, as if no one had come.

SWEEP MOTION — IMPORTANT: physically-based the shadows moving unhurried, cloth settling over cloth, the lantern light barely swinging — the corridor is swept clean of the night's work, no bodies shown, no blood anywhere, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 회랑 불이 다시 켜짐 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP37_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드, 회랑 불이 다시 켜짐 → 암전 → 타이틀. [무대사] / 자막: 제38화 「추적의 발자국」에서 계속
- **연출 특이**: **EP38 훅 썬** — 재점화의 와이드(1컷) → 암전(2컷) → 타이틀(3컷, 편집 단계). S1의 소멸과 정대칭 — 꺼지던 등불이 다시 켜지며 회랑은 흔적을 지운다. 무대사 — 렌더 무음. 렌더는 완전 암전으로 끝난다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures anywhere: the corridor lanterns relit one by one, warm light returning down the rain-wet boards, the rain ended and the night quiet. Nothing written on the lanterns or the woodwork. No blood anywhere — the corridor shows only wet boards and warm light. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the returned warm points of lantern light against the cold blue night air, reflected on the wet boards, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the corridor lanterns relit one by one, warm light returning down the rain-wet boards, the rain ended and the night quiet.
2. the frame sinking into complete black, no text, held.
3. end card for the edit stage only — one vertical column of red Korean characters on black (the render must end in complete black; the title card is inserted in editing).

RELIGHT MOTION — IMPORTANT: physically-based the flames taking one by one, the wet boards warming under the returned light, the rain ended — the lights come back and the corridor forgives nothing, the render ends in complete black, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션(S1·S5) — "보름 전날 밤 — 회랑의 등불이 하나씩 꺼졌다." / "다행히 죽은 자는 없었다 — 왕의 어명이 그들의 죽음을 금하고 있었기 때문이다."를 운반하는 목소리 |
| 무결 | `ko-KR-Wavenet-C` | -1.5 | 1.0 | 묵직한 절제의 무사 톤(S6) — "폐하의 길목은 이제 비워두기 어렵습니다. 설화 님의 길목도요." 내레이션과 동일 ID — §0-13 4중 장치 필수 |
| 설화 | `ko-KR-Neural2-A` | -1.0 | 1.0 | 억누른 인사(S6) — "당신 — 또." 차분하고 서늘한 톤, 거의 속삭임 |

본 화 대사 2구(무결 1 + 설화 1) + 내레이션 2구 + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션·효과음(S3 목조 붕괴·금속 충돌, S4 금속 충돌, S5 발 소리 계열 포함) 사후 믹싱. 발화 2구 전부 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S2 무언·S3·S4 효과음·S7·S8 무대사 — 렌더 무음. 이환(Neural2-C)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **세이프티 가드 준수**: 회랑 액션은 비그래픽 무대화 — 젖은 마루판·목재 파편·쇠와 쇠의 충돌로 치환, 유혈·시신 일체 미렌더.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:05,600
보름 전날 밤 — 회랑의 등불이 하나씩 꺼졌다.

2
00:00:32,000 --> 00:00:36,800
다행히 죽은 자는 없었다 — 왕의 어명이 그들의 죽음을 금하고 있었기 때문이다.

3
00:00:39,500 --> 00:00:40,600
당신 — 또.

4
00:00:41,000 --> 00:00:45,200
폐하의 길목은 이제 비워두기 어렵습니다. 설화 님의 길목도요.

5
00:00:58,000 --> 00:00:59,800
제38화 「추적의 발자국」에서 계속
```

- 시작 시각은 정본 rel 수치(3.0→2.0 / 4.0→32.0 / 2.0→39.5 / 4.5→41.0)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S2(무언)·S3·S4(효과음)·S7·S8 무대사는 SRT 미기재 — 효과음은 믹싱 원장 별도.
- 5번 자막(58.0~59.8)은 암전 이후 삽입 — S08 렌더는 완전 암전으로 끝나고 타이틀은 편집 단계 참조.
- TTS 트랙 분리: 내레이션 2구(`EP37_S1_NARRATION`·`EP37_S5_NARRATION`)와 무결 1구(`EP37_S6_MUGYEOL`)는 반드시 별도 세션에서 합성 — 동일 ID `ko-KR-Wavenet-C` 이중 배역 차단(§0-13). 설화 1구는 `EP37_S6_SEOLHWA`.

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP37_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP37_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep37_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP37_QC_CHECKLIST.md` |
