# 「혈화의 궐」 EP05 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-04)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 컨펌) + `master_screenplay/SEASON_01_MASTER_SCREENPLAY.md` 제5화 「중궁전의 장부」 썬표 + `characters.md` 캐릭터 앵커 + EP01 실증 통과 템플릿(`EP01_VARIABLE_DIRECTOR_PROMPTS_v3.md`) + EP04 원장 운용 결과
> **범위**: EP05 전 8썬(S01~S08) — 콘티 시트 8종 + 실사 렌더 프롬프트 8종
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장 프롬프트 전문을 **그대로 복사 투입**한다. 시트 이미지를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다(EP01 S02 v1 결함(시트 텍스트 워밍) 재발 방지).
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)

---

## 0. 공통 규칙 (전 썬 강제)

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **OUTPUT FORMAT READ FIRST 블록**: 전 썬 프롬프트의 첫 문단에 S02식 전면 차단 블록을 고정한다(EP01 실증 결함 재발 방지).
3. **화풍 강제 블록**: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
4. **물리 블록**: 촛불 불꽃·재(잿가루)·종이·옷자락 등 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다(스케치의 정적 선 추종 차단).
5. **클린 프레이밍 블록**: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
6. **세이프 필터(AG 원장 ② 준수)**: 유혈·흉기 가동·시신 묘사 일체 없음. 무결의 환도는 전 썬 **칼집 착용(sheathed)** — 뽑기·위협 동작 없음. 본 화는 대치·추격 씬이 없으므로 전 썬 무폭력 관찰·대話 드라마다. 장부 열람은 협박 아닌 조용한 증거 수집으로 연출(`silent, unobserved`).
7. **인물 일관성(AG 원장 ⑥)**: 등장 인물의 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입했다(CHARACTER GUARD 블록). `characters.md` 고정 프롬프트와 상충하는 묘사 추가 금지.
   - **설화**: 21-year-old court lady, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok
   - **강무결**: 25-year-old warrior captain, tall, sharp jawline, faint scar across cheekbone, dark navy and black military uniform (yungbok), sheathed Korean sword (hwando) at his belt
   - **중전 윤씨**: 22-year-old beautiful villainous Joseon Queen, extravagant ceremonial dangui hanbok in royal purple and jade, elaborate royal hair ornaments (tteoljam, cheopji) with swaying danglings, haughty arrogant eyes, chilling faint smirk
8. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초(원장 공통 1번 환산식). 썬 경계는 클립 상대 8초 정렬.
9. **엔드카드**: S08 암전 이후의 붉은 타이틀(제6화 「발각의 위기」에서 계속)은 **편집 단계에서 삽입**(렌더에서 만들지 않음). S08 렌더는 소매 속 종이 매크로 → 암전 진행까지만.
10. **야간 광원 표기(정본 AG 검수 ① 준수)**: 본 화의 무대는 중궁전 문서고와 회랑이므로 키 라이트는 **촛불(candle flame)** 이다. 문서고 썬(S01~S03)은 `a single candle flame as the only key light`를 명시하고, 회랑 썬(S06~S07)은 `warm candle lanterns`를 명시한다. 달빛은 보조 광(`pale moonlight through lattice windows`)으로만. 광원 모티베이션 없는 인공 키 라이트 금지.
11. **장부 텍스트 슬롭 방지(정본 AG 검수 ① 준수)**: 장부·종이의 글자는 전 썬 `faint illegible aged brush marks, unreadable`로 강제한다. 가독 문자는 렌더에서 만들지 않고 편집 자막으로만 처리한다.

---

## 1. S01 한 줄기 촛불 (절대 00.0~07.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP05_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 크레인 다운 → 서가 사이 촛불 한 줄기 → 반쯤 타지 않은 장부. 나레이션이 EP02 소각의 시간선 모순을 봉합하는 개방 컷이다. [무거운 나레이션 · 내레이션/Wavenet-C 다큐 톤] "중전이 태운 것은 원본의 절반뿐이었다." (rel 3.0=절대 2.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

SETTING GUARD — a vast royal Joseon archive at night, towering dark wooden bookshelves, deep darkness, a single candle flame as the only key light, pale moonlight through lattice windows as faint fill. No people in frame.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, slow crane down from the dark rafters into the great royal archive, towering shelves swallowing the darkness, one thin line of candle glow standing in the depth between the stacks.
2. 24mm, slow push: the single candle flame standing in the gap between the shelves, a fragile island of warm light in the black archive.
3. 24mm low angle tracking along a shelf: half-burned ledger volumes with scorched edges, a faint trace of ash on the wood, candle glow raking across them.

CANDLE AND DUST MOTION — IMPORTANT: physically-based candle flame breathing and bending with the still air, its warm falloff trembling on the shelf wood, faint dust and ash motes drifting through the glow. Do NOT follow the sketch's static lines — the archive must breathe like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 서가 뒤의 설화 (절대 07.5~15.0 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP05_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 핸드헬 텐션 — 설화가 서가 사이로 미끄러지고, 서가에 몸을 붙이고, 책 사이 틈으로 시야를 얻는다. [서늘한 판단 속마음 · 설화/Neural2-A] "숨기는 사람이 많을수록, 종이는 커진다." (rel 3.0=절대 9.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, unnervingly calm, moving like a shadow. No other person in frame. No weapons.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm handheld, tense: the court lady slipping sideways between towering archive shelves, candle glow flickering on the wood.
2. 50mm handheld: she presses her back against a shelf, half her body sinking into shadow, candlelight rimming her face.
3. 50mm, static: her cold dark eyes peering through the narrow gap between stacked books.
4. 50mm handheld over her shoulder: deep in the stacks, an iron-bound document chest and remaining ledger volumes lit by one candle flame — the thing that was not burned.

CANDLE AND HANDHELD MOTION — IMPORTANT: physically-based candle flame breathing with realistic warm falloff, handheld micro-sway alive but restrained, hanbok fabric brushing the shelves silently. Do NOT follow the sketch's static lines — the stealth must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 장부의 잔여 페이지 (절대 15.0~22.5 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP05_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro 랙 포커스 — 잔여 페이지 → 불꽃과 종이의 초점 전환 → 재의 비산 → 얼어붙은 손끝. 숫자 낭독 폭로는 정본 치환대로 배제하고 매크로+단문 해석만 남긴다. [차가운 해석 · 설화/Neural2-A] "월마다 빠진 것은 쌀이 아니라 — 사람의 이름이지요." (rel 4.0=절대 18.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — only the hands of the 21-year-old court lady appear: pale porcelain skin, elegant dark pastel hanbok sleeve. Aged ledger pages — IMPORTANT: all writing on the pages is only faint illegible aged brush marks, unreadable, no readable characters anywhere.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: aged ledger pages, worn paper fibers, faint illegible aged brush marks raked by candlelight.
2. 100mm macro, slow rack focus: the candle flame sharp behind, the pages soft in front — then the focus sliding back to the paper.
3. 100mm macro, static: fine ash scattering and drifting microscopically from a scorched page edge, particles floating through the candle glow.
4. 100mm macro, static: her pale fingertips frozen hovering just above the page — not touching, a cold careful stillness.

ASH AND FLAME MOTION — IMPORTANT: physically-based fine ash particles drifting and settling in slow strands, candle flame breathing with realistic warm falloff, paper fibers rendered realistically. No readable text of any kind on the pages. Do NOT follow the sketch's static lines — the macro must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 문서고를 나서다 (절대 22.5~30.0 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP05_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm 걸어 나옴 — 문서고 문을 나서고, 뒤로 거대한 문이 닫히고, 복도에 홀로 선 각오의 실루엣. [낮은 속삭임 · 설화/Neural2-A] "사라진 이름들의 자리가 — 이제 소녀의 지도가 되겠사옵니다." (rel 3.0=절대 24.5)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, quiet resolve in her stride. No other person in frame. No weapons.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm, slow follow: the court lady walking out through the tall archive door into a dim moonlit corridor, candlelight dying behind her.
2. 35mm from behind: the massive wooden door slowly swinging closed behind her, the last sliver of candlelight narrowing.
3. 35mm wide, static: the door shut, her lone small silhouette standing still in the moonlit corridor, pale moonlight through lattice windows, quiet resolve.

DOOR AND LIGHT MOTION — IMPORTANT: physically-based heavy door movement with weight and drag, the candlelight sliver narrowing and vanishing naturally, hanbok hem settling as she stops, faint night haze in the moonlight. Do NOT follow the sketch's static lines — the exit must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 기둥 사이의 침묵 (절대 30.0~37.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP05_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 투숏 — 기둥 사이에 선 설화, 지나가던 무결, 멈춘 발걸음, 눈만 마주친 프로필 투숏. 말은 없다 — 두 사람의 침묵이 계약의 갱신. 무대사 썬(렌더도 무음 연출).
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok. The warrior is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, dark navy and black military uniform (yungbok), a traditional Korean sword STAYING SHEATHED at his belt. No weapons drawn, no violence, no words spoken — silence only.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm two-shot between thick wooden pillars, static: the court lady standing still in a moonlit palace gallery at night, candle lanterns glowing low.
2. 85mm, static: the warrior captain passing by — both of them freezing mid-step at the same instant.
3. 85mm profile two-shot across the pillars, static: only their eyes meeting in silence, a held beat — a pact renewed without a single word.

MOONLIGHT AND BREATH MOTION — IMPORTANT: physically-based candle lantern flames breathing with soft warm falloff, pale moonlight through lattice windows as fill, subtle breathing motion in both figures, fabric settling as they stop. Do NOT follow the sketch's static lines — the silence must be alive, like real filmed footage held on a breath.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 중전의 회랑 (절대 37.5~45.0 · 콘티 4컷 · 신규)

- **시트**: `downloads/EP05_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 135mm 압축 — 회랑 저편에서 다가오는 중전, 떨잠이 흔들리고, 가식의 온화한 질문, 완벽하게 거짓 없는 대답. [가식의 온화 · 중전/Neural2-B] "홍화. 오늘은 어디를 청소하러 다녔느냐." (rel 2.5=절대 39.5) / [거짓 없는 완벽한 대답 · 설화/Neural2-A] "마마의 발길이 닿는 곳을 지나다 보았사옵니다." (rel 5.0=절대 42.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the Queen is a 22-year-old beautiful yet villainous Joseon Queen, wearing an extravagant ceremonial dangui hanbok in royal purple and jade, elaborate royal hair ornaments (tteoljam, cheopji) with swaying danglings, haughty arrogant eyes, a chilling faint smirk. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a simple jade hairpin, elegant dark pastel hanbok, perfectly composed. No weapons, no violence.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 135mm compressed telephoto, static: a long royal corridor of the Inner Court at night lined with warm candle lanterns, the Queen walking toward camera from far away, the compression swallowing the space behind her.
2. 135mm close detail, shallow depth of field: the tteoljam ornaments in her hair swaying with each step, catching the lantern light.
3. 135mm, half-turn three-quarter profile: the Queen stopping and turning her head, speaking down with a falsely gentle smile — velvet menace.
4. 135mm, front slight high angle: the court lady bowing with perfect composure, answering without a tremor.

LANTERN AND ORNAMENT MOTION — IMPORTANT: physically-based candle lantern flames breathing along the corridor, the tteoljam danglings swinging and settling with each step with real weight, hanbok fabric moving naturally. Do NOT follow the sketch's static lines — the procession must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 첫 균열 (절대 45.0~52.5 · 콘티 3컷 · 신규)

- **시트**: `downloads/EP05_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm 숨 죽임 — 완벽한 가면 → 눈에 스치는 첫 의심 → 조용한 추궁. 중전이 처음으로 흔들리는 썬. [억누른 의심 · 중전/Neural2-B] "…그래서, 무엇이 보였느냐." (rel 2.5=절대 47.0)
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the Queen is a 22-year-old beautiful yet villainous Joseon Queen, wearing an extravagant ceremonial dangui hanbok in royal purple and jade, elaborate royal hair ornaments (tteoljam, cheopji) with danglings, haughty arrogant face, a chilling faint smirk. No other person in frame, no weapons, no violence.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close-up, eye level, static: the Queen's composed face in warm candle lantern light, chin high, mask intact.
2. 85mm close-up, tighter, static: her eyes — for the first time a hairline tremor of doubt crosses them.
3. 85mm close-up, slightly higher, static: her breath held, face lowering slightly as she asks a quiet question, the air charged — suppressed doubt under an impeccable mask.

CANDLELIGHT AND MICRO-EXPRESSION MOTION — IMPORTANT: physically-based lantern light wavering gently across her face so the shadow line breathes, micro-detail in eyes and skin realistic, the tremor rendered as a tiny natural movement — never an exaggerated performance. Do NOT follow the sketch's static lines — the crack in the mask must feel like real filmed footage.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 소매 안 종이와 암전 (절대 52.5~60.0 · 콘티 4컷 · 렌더 2컷+암전)

- **시트**: `downloads/EP05_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 소매 안 종이의 모서리 → 종이 질감 매크로 → 암전. **붉은 타이틀(제6화 「발각의 위기」에서 계속)은 편집 단계 삽입 — 렌더에서 만들지 않는다.** 무음 클리프행어.
- **프롬프트 전문 (신규)**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — only the sleeve and hands of a 21-year-old court lady in an elegant dark pastel hanbok appear. IMPORTANT: all writing on the paper is only faint illegible aged brush marks, unreadable, no readable characters anywhere. No violence, no weapon, nobody else in the frame.

Recreate the panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a folded paper corner hidden inside her wide hanbok sleeve, warm candlelight from a lantern beyond.
2. 100mm macro, static: the worn aged paper corner texture — fragile fibers, faint illegible aged brush marks, unreadable, secrets almost erased.
3. The frame slowly dims — the lantern glow shrinking until the screen fades to complete black, held in darkness. No title card, no text of any kind is rendered.

PAPER AND FADE MOTION — IMPORTANT: physically-based paper flexing slightly with her breath and settling into the silk of the sleeve, fabric folds moving naturally, the lantern glow dying in a smooth cinematic fade to black. No readable text. Do NOT follow the sketch's static lines — the concealment must feel like real filmed footage.

Absolutely NO text, NO labels, NO title cards, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 썬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 지문 컷 수 | 비고 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 3컷 | EP05_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 촛불 단일 광원 명시(AG ①) · 인물 없는 개방 컷 |
| S02 | 07.5~15.0 | 4컷 | EP05_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 50mm 핸드헬 텐션 · 잠입 무폭력 |
| S03 | 15.0~22.5 | 4컷 | EP05_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 장부 글자 비가독 강제(정본 AG 검수 ①) |
| S04 | 22.5~30.0 | 3컷 | EP05_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 문 닫힘 + 달빛 보조 광 |
| S05 | 30.0~37.5 | 3컷 | EP05_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 무대사 — 눈빛만의 계약 갱신 |
| S06 | 37.5~45.0 | 4컷 | EP05_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg | 4 | 135mm 압축 · 떨잠 디테일 |
| S07 | 45.0~52.5 | 3컷 | EP05_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg | 3 | 중전 첫 균열 — 과장 금지 |
| S08 | 52.5~60.0 | 4컷(렌더 2컷+암전) | EP05_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg | 2+페이드 | 엔드카드·타이틀은 편집 삽입 |

합계: 콘티 28컷 / 렌더 클립 8개(렌더 80초 → 편집 60초).

---

## 10. 분리형 SRT 한글 자막 원장 및 보이스 타임코드 (00:00~01:00)

### 10-1. 보이스 타임코드 인라인 대응표 (TTS 사후 믹싱용)

| 순 | 썬 | 보이스(TTS ID) | 클립 rel | 절대 시간 | 대사/자막 |
|---|---|---|---|---|---|
| 1 | S01 | 내레이션 `ko-KR-Wavenet-C` (다큐 톤, Pitch -1.5) | rel 3.0 | 절대 2.0 | 중전이 태운 것은 원본의 절반뿐이었다. |
| 2 | S02 | 설화 `ko-KR-Neural2-A` (Pitch -1.0) | rel 3.0 | 절대 9.5 | 숨기는 사람이 많을수록, 종이는 커진다. |
| 3 | S03 | 설화 `ko-KR-Neural2-A` | rel 4.0 | 절대 18.0 | 월마다 빠진 것은 쌀이 아니라 — 사람의 이름이지요. |
| 4 | S04 | 설화 `ko-KR-Neural2-A` | rel 3.0 | 절대 24.5 | 사라진 이름들의 자리가 — 이제 소녀의 지도가 되겠사옵니다. |
| 5 | S05 | (무대사 · 무성) | — | — | 두 사람의 침묵이 계약의 갱신 — 자막 없음 |
| 6 | S06 | 중전 `ko-KR-Neural2-B` (가식의 온화 톤) | rel 2.5 | 절대 39.5 | 홍화. 오늘은 어디를 청소하러 다녔느냐. |
| 7 | S06 | 설화 `ko-KR-Neural2-A` | rel 5.0 | 절대 42.0 | 마마의 발길이 닿는 곳을 지나다 보았사옵니다. |
| 8 | S07 | 중전 `ko-KR-Neural2-B` (억누른 의심 톤) | rel 2.5 | 절대 47.0 | …그래서, 무엇이 보였느냐. |
| 9 | S08 | (편집 삽입 · 무성) | rel 7.0 | 절대 59.0 | 제6화 「발각의 위기」에서 계속 |

### 10-2. 60초 SRT 풀 리스트 (분리형 자막 파일용 — 편집 단계에서 그대로 저장)

```srt
1
00:00:02,000 --> 00:00:05,000
중전이 태운 것은
원본의 절반뿐이었다.

2
00:00:09,500 --> 00:00:12,500
숨기는 사람이 많을수록,
종이는 커진다.

3
00:00:18,000 --> 00:00:21,500
월마다 빠진 것은 쌀이 아니라 —
사람의 이름이지요.

4
00:00:24,500 --> 00:00:28,000
사라진 이름들의 자리가 —
이제 소녀의 지도가 되겠사옵니다.

5
00:00:39,500 --> 00:00:41,500
홍화. 오늘은 어디를
청소하러 다녔느냐.

6
00:00:42,000 --> 00:00:45,000
마마의 발길이 닿는 곳을
지나다 보았사옵니다.

7
00:00:47,000 --> 00:00:50,000
…그래서, 무엇이 보였느냐.

8
00:00:59,000 --> 00:01:00,000
제6화 「발각의 위기」에서 계속
```

- 자막 표기 원칙: 컷 헤드 1초 내 등장, 하단 15%, 명조체 세리프, 8f 페이드인(시즌3 전환 총칙 준용). 8번 엔드카드 자막은 렌더가 아닌 편집 단계 삽입(§0-9)이다.
- S05는 무대사 썬이므로 SRT 블록이 없다 — 자막 공백 구간(00:30~00:37.5)은 침묵 연출 그대로 둔다.
- S06 5·6번 자막은 중전 대사(rel 2.5=39.5)와 설화 대답(rel 5.0=42.0)이 0.5초 겹쳐 39.5~41.5 / 42.0~45.0으로 분할 배치한다.
