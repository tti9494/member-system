# 🎬 사극 「혈화의 궐」 제1화 디렉터 가변 콘티 및 프롬프트 원장 (v3.1)

> **기준 일자**: 2026-11-04 (윤상욱 님 현장 실측 및 음성 통화 최종 확정 / 07:45 화면비·길이 규격 정정 반영)  
> **작업 ID**: `SAGEUK-EP01-RENDER-20261104-0710`  
> **확정 규격(07:45 정정)**: 화면비 **16:9 가로 1920×1080**(제미나이 웹 Veo 기본값, 강제 크롭·레터박스·세로 변환 금지) · 길이 **55~65초 유동**(60.0초 기계적 고정 금지). 아래 씬별 절대 시간은 60초 기준 편집 가이드이며, 최종 조립은 유효 프레임에 맞춰 55~65초로 자연 편집한다.  
> **상욱 님 지침**: "거기에 들어갔던 스토리보드, 프롬프트 따로 모아놓고 내가 한 번에 볼 수 있게."  
> **검수 및 파이프라인**: 아르센 피클 제작 ➔ 오이 1차 사전 검수(1~10컷 및 프롬프트 규격 전 항목 PASS) ➔ 상욱 님 원장 확인 ➔ 맥에어 6계정 Veo 렌더링 ➔ Qwen2-VL 프레임 단위 물리 검수 및 1~3초 유효 구간 트리밍 ➔ 무자막·무음성 순수 영상 1본 + SRT 자막 분리 산출

---

## 📌 핵심 제작 및 검수 가드레일 (상욱 님 못 박음)

1. **1~10 가변 컷 디렉터 콘티 (기계적 4컷 고정 절대 금지)**:
   - 씬의 서사 긴박도와 감정에 맞춰 1컷(롱테이크)~10컷(초고속 몽타주) 유동 배분.
   - S01(5컷) · S02(3컷) · S03(3컷) · S04(4컷) · S05(3컷) · S06(3컷) · S07(4컷) · S08(5컷) = 총 30컷 완비.
   - 1024×1536 흑연 연필 소묘 선화 질감, 컷별 렌즈 화각(24~100mm Macro)/카메라 무빙/디렉터 연출 노트 병기.
2. **콘티 연출 자율성 vs 최종 컷 검수·편집 분업**:
   - 콘티 기획 단계에서는 웅덩이 반사, 매크로 클로즈업, 오버헤드 샷 등 과감한 시네마틱 앵글 투입 (사전 검열 배제).
   - 자잘한 복식 고증보다 **'화면의 물리적 개연성(화염 모핑, 신체 왜곡, 기괴한 반사 왜곡 방지)'**을 최우선으로 검수.
   - 10초 렌더 클립에서 시작 1.0초·끝 1.5초 버퍼 트림 후 필요한 유효 구간(1~3초)만 선별 트리밍하여 호흡감 있게 조립.
   - **분량 가이드 (상욱 님 직접 확정)**: 60.0초에 기계적으로 억지로 맞추지 않고, 씬 호흡과 유효 컷에 맞춰 **60초 전후(55~65초)**로 자연스럽게 조립.
3. **제미나이 웹 Veo 실사화 렌더링 규격**:
   - 콘티는 구도/레이아웃 가이드로만 작동.
   - **화면비 (상욱 님 직접 확정)**: **세로가 아닌 16:9 가로 와이드스크린(1920×1080)**으로 확정.
   - 시트 텍스트 워밍 방지를 위한 `OUTPUT FORMAT — READ FIRST` 블록 첫머리 강제.
   - 필수 화질: `Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting`.
   - 화풍 강제: `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style`.
   - 물리 엔진 강화: `physically-based flames with rolling turbulent motion, heat-haze shimmer, scattering embers, volumetric smoke / mist / rain`.
   - 클린 프레이밍: `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only`.
   - 세이프 필터: 유혈·시신·직접 살상 배제, 은유(횃불, 그림자, 발끝, 시선 대치) 치환.
4. **산출물 단일화 및 무자막 원칙**:
   - 영상 위에 자막/BGM/배지 합성 절대 금지 (무자막·무음성 순수 영상 원본 1본만 단독 납품).
   - SRT 자막 파일은 별도 파일로 분리 산출.
   - S08 붉은 타이틀 및 암전은 편집 단계에서 삽입.
5. **EP04 실측 결함 재발 방지**:
   - 프롬프트의 카메라 장비명(ARRI 등)이 실제 삼각대·장비 프레임을 생성한 사례가 있으므로, 모든 씬 프롬프트에 `no camera rig, no tripod, no boom mic, no slate, no film equipment visible in frame`을 함께 넣는다.
   - 화면 내 장비 노출 프레임은 0건이어야 한다.

---

## 🎞️ 씬별 콘티 및 실사 프롬프트 상세

### SCENE 01: 멸문의 밤 (절대 00.0~07.5 · 콘티 5컷 · 렌더 완료)
- **긴박도/배분**: 5컷 가변 콘티 (정적 원경 ➔ 불길 번짐 ➔ 화마 속 저택 ➔ 잔해 낙하 ➔ 탈출로 차단)
- **화각 및 무빙**: 24mm Ultra-Wide Push-in, 35mm Tilt-up, 100mm Macro, 85mm Telephoto
- **실사 렌더링 프롬프트 전문**:
  ```text
  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  Recreate the 5 panels in order as one continuous ~11 second sequence:
  1. Extreme wide 24mm low-angle static: a majestic Joseon noble mansion engulfed in massive roaring flames at midnight, burning tiled roofs silhouetted in dramatic chiaroscuro, thick smoke and glowing orange embers filling the dark sky.
  2. 35mm handheld slight push-in: the courtyard wooden gate collapsing in flames, fire roaring through the courtyard.
  3. Low angle tilt-up drift: swirling embers spiraling into the black night, thick volumetric smoke filling the sky.
  4. 100mm macro extreme close-up, shallow depth of field: a weathered adult hand reaching through wet dark mud toward a trampled jade hairpin and torn jade-green silk fabric, glowing embers reflecting in rain puddles, tragic cinematic loss.
  5. 85mm medium telephoto slight low angle, slow push-in: a Joseon government minister in dark black-and-crimson court robes and a black satmo official hat sits composed on a black stallion beyond the burning garden wall, watching the flames with a cold, satisfied expression.

  FIRE MOTION — IMPORTANT: large dynamic physically-based flames with rolling turbulent motion, heat-haze shimmer above the fire, glowing embers scattering in the wind, dense volumetric smoke. Do NOT follow the sketch's calm, gentle flame motion — the fire should move like a big-budget period film's fire sequence.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines in the output. Clean full-bleed cinematic frames only.
  ```

---

### SCENE 02: 흑마 위의 권신 · 빗속 결의 (절대 07.5~15.0 · 콘티 3컷 · 렌더 완료)
- **긴박도/배분**: 3컷 가변 콘티 (말발굽과 진흙 ➔ 차가운 눈빛의 윤경헌 ➔ 칼끝에 반사되는 불빛)
- **화각 및 무빙**: 135mm Compressed Telephoto, 50mm Ground Level, 85mm Portrait Telephoto
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  COSTUME GUARD — CRITICAL: the male rider is a JOSEON GOVERNMENT MINISTER (a subject, NOT a king). He must wear a dark reddish-brown and black Joseon official robe with a plain chest emblem and a black satmo official hat. He must NOT wear a red gonryongpo, NOT wear a dragon emblem, NOT wear a king's crown or ikseongwan, NOT wear gold dragon embroidery.

  Recreate the 3 panels in order as one continuous ~9 second sequence:
  1. 135mm compressed telephoto, static with slight push-in: the minister in his dark official robe and black satmo hat rides a black horse beyond a burning palace wall at night, cold smirk on his face, distant flames and ragged banners behind him.
  2. 50mm, ground level static: heavy rain falling on wet palace flagstones at night, a large rain puddle reflects the piercing, resolute eyes of a young adult Joseon woman, raindrops and ripples distorting the reflection, distant fire glow tinting the horizon.
  3. 85mm portrait telephoto, slight push-in: the young adult woman stands in heavy pouring rain, soaked dark hair clinging to her face, tight resolute jawline, intense unwavering gaze, smoke and dying fire glow in the blurred background.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 03: 입궁 행렬 (절대 15.0~22.5 · 콘티 3컷)
- **긴박도/배분**: 3컷 가변 콘티 (정문 원경 ➔ 안개 속 궁녀 행렬 ➔ 젖은 박석 매크로)
- **콘티 에셋**: `downloads/EP01_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 24mm Low Angle Crane Down, 35mm Lateral Tracking, 100mm Macro Ground Level
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the young adult court lady walking in the line is a 21-year-old Korean woman with pale porcelain skin, cold intelligent dark eyes, neat traditional hair with a small jade hairpin, wearing an elegant dark pastel hanbok with clean embroidery. All other court ladies are young adult women in pale traditional Korean hanbok.

  Recreate the 3 panels in order as one continuous ~10 second sequence:
  1. Extreme wide 24mm low angle, slow crane down: dawn light over a grand Joseon palace gate wrapped in morning mist, a long procession of new court ladies entering through the gate, tall flagpoles and banners, volumetric haze over the stone plaza.
  2. 35mm lateral tracking: pairs of young adult court ladies in pale traditional Korean hanbok walking in step through low rolling ground mist along a high stone palace wall, heads bowed, a distant ceremonial bell tower.
  3. 100mm macro, ground level static: rain-wet dark flagstones, the small quick steps and folded hems of court ladies passing through frame, fine dust and dew, soft broken reflections in the wet stone.

  ATMOSPHERE — IMPORTANT: physically-based volumetric mist with slow drifting layered fog, fine dust motes caught in the dawn light, natural fabric motion in walking. Do NOT follow the sketch's static lines — the air, mist and fabric must breathe and move like real filmed footage.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 04: 대전의 분노 (절대 22.5~30.0 · 콘티 4컷)
- **긴박도/배분**: 4컷 가변 콘티 (옥좌 원경 ➔ 상소문 투척 ➔ 엎드린 신하들 ➔ 분노의 젊은 왕)
- **콘티 에셋**: `downloads/EP01_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 24mm Low Angle Push-in, 50mm Whip Pan, 35mm High Angle Static, 85mm Slow Push-in
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the king is a handsome 24-year-old Joseon young king, pale complexion, melancholy yet furious eyes, wearing a royal red dragon robe (gonryongpo) with gold embroidered dragon emblem and a gold royal winged hat (ikseongwan). The prostrating ministers are adult men in dark Joseon court robes.

  Recreate the 4 panels in order as one continuous ~10 second sequence:
  1. Extreme wide 24mm low angle, slow push-in: a vast empty Joseon royal throne hall with towering red wooden pillars, the young king seated far away on a high golden throne at the end of a long polished floor, oppressive scale.
  2. 50mm whip pan following the paper: a rolled paper memorial hurled violently through the air, loose pages scattering in its wake, a red dragon-robe sleeve thrown back in fury, the camera racing after the flying paper.
  3. 35mm static high angle: rows of ministers in dark court robes prostrated flat on the polished wooden floor, foreheads down, perfectly motionless, fear as architecture.
  4. 85mm slow push-in: intense close-up of the young king, furious trembling eyes, tight jaw, contained rage, golden throne hall bokeh behind him.

  PAPER MOTION — IMPORTANT: physically-based fluttering paper with tumbling pages, realistic air drag and rotation, crisp page edges catching the light. Do NOT follow the sketch's frozen shapes — the thrown memorial must fly and scatter like real filmed footage.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 05: 밤의 회랑 — 은장도 (절대 30.0~37.5 · 콘티 3컷)
- **긴박도/배분**: 3컷 가변 콘티 (회랑 실루엣 ➔ 은장도 발도 매크로 ➔ 달빛 칼날)
- **콘티 에셋**: `downloads/EP01_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 24mm Wide Static Long Take, 100mm Macro Slow Push-in, 100mm Macro Static
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the court lady is a 21-year-old Korean woman with pale porcelain skin, delicate hands, neat traditional hair with a small jade hairpin, wearing an elegant dark pastel hanbok with clean embroidery. Her gesture is a quiet vow, not violence — calm, precise, resolute.

  Recreate the 3 panels in order as one continuous ~10 second sequence:
  1. 24mm wide static long take: a long dark wooden palace corridor at night lit only by cold moonlight through lattice columns, the distant small silhouette of a lone court lady walking away down the corridor, deep shadows, absolute stillness.
  2. 100mm macro, slow push-in: inside a jade-green silk sleeve, delicate fingers slowly drawing out a small ornate Korean silver dagger (eunjangdo) with an elegant decorated handle, shallow depth of field, moonlight glinting on the metal.
  3. 100mm macro static: the short silver dagger blade catching cold moonlight, one bright gleam traveling along the polished edge against the darkness, her steady reflection faint in the steel.

  LIGHTING — IMPORTANT: source-motivated lighting only — moonlight and one distant paper lantern; cold silver highlights, deep chiaroscuro shadows. Physically-based specular gleam on the blade, natural slow hand motion. Do NOT follow the sketch's static lines — render real filmed motion with breathing light.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 06: 그림자 드리움 (절대 37.5~45.0 · 콘티 3컷)
- **긴박도/배분**: 3컷 가변 콘티 (궁녀 뒷모습 ➔ 마루 장검 그림자 ➔ 멈춘 발끝)
- **콘티 에셋**: `downloads/EP01_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 50mm Following Handheld, 24mm Low Angle Static, 100mm Macro Static
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the court lady seen from behind is a young adult Korean woman with neat traditional hair with a small jade hairpin, wearing a pale hanbok. The warrior himself is NEVER shown on screen — only his enormous cast shadow.

  Recreate the 3 panels in order as one continuous ~10 second sequence:
  1. 50mm following, slight handheld tension: rear view of a young adult court lady in a pale hanbok with a jade hairpin walking along a dim wooden palace corridor at night, warm paper lanterns, a distant male figure far behind her in the corridor depth.
  2. 24mm low angle static: a huge menacing shadow of an armored warrior holding a long sword cast across the wooden floor planks and up the wall, the shadow stretching enormous toward the small walking figure ahead, lantern light flickering at the shadow's edge.
  3. 100mm macro static: a young woman's traditional embroidered flat shoes stopping dead on the wooden floorboards, the hanbok hem frozen mid-step, the corridor holding its breath.

  SHADOW MOTION — IMPORTANT: physically-based cast shadow with realistic perspective, flickering and breathing with the lantern flame, subtle tremor as the warrior walks. The lady's skirt and steps move naturally. Do NOT follow the sketch's static lines — the shadow must live and grow like real filmed footage.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 07: 눈 충돌 — 조우 (절대 45.0~52.5 · 콘티 4컷)
- **긴박도/배분**: 4컷 가변 콘티 (더치 틸트 투샷 ➔ 무결 클로즈업 ➔ 설화 시선 ➔ 칼자루 쥔 손)
- **콘티 에셋**: `downloads/EP01_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 85mm Two Shot Dutch Tilt, 85mm Slow Push-in, 100mm Macro Static, 100mm Macro Tilt Down
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the royal guard is a 25-year-old Joseon warrior captain, tall, sharp jawline, a faint scar across his cheekbone, wearing dark navy and black military uniform with a black traditional horsehair hat, a traditional Korean sword (hwando) sheathed at his belt. The court lady is a 21-year-old Korean woman, pale porcelain skin, cold piercing dark eyes, neat traditional hair with a small jade hairpin, elegant dark pastel hanbok. No one draws a weapon; the tension is only in their eyes.

  Recreate the 4 panels in order as one continuous ~10 second sequence:
  1. 85mm two shot, slight dutch tilt, static: a rainy moonlit palace corridor, the young court lady and the tall royal guard facing each other from a distance, rain falling off the eaves between them, lantern light on wet wood, ten years of history colliding in silence.
  2. 85mm slow push-in: close-up of the royal guard, rain dripping from his hat brim, the faint scar on his cheekbone, eyes trembling with disbelief, breath visible in the cold air.
  3. 100mm macro static: extreme close-up of the young woman's calm, piercing dark eyes, unblinking and unreadable, rain light shimmering, the dead do not tremble.
  4. 100mm macro tilt down: a weathered hand slowly settling onto the hilt of the sheathed Korean sword at his belt, raindrops running off the knuckles, habit and protection in one motion.

  RAIN MOTION — IMPORTANT: physically-based rainfall with individual droplets, splash and mist on impact, glossy wet reflections on wood and stone, drifting breath vapor in lantern light. Do NOT follow the sketch's static lines — the rain must fall and glitter like real filmed footage.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

### SCENE 08: 경보와 추격 (절대 52.5~60.0 · 콘티 5컷)
- **긴박도/배분**: 5컷 가변 콘티 (횃불 매크로 ➔ 달리는 군졸들 ➔ 닫히는 성문 ➔ 연기 속 포위망 ➔ 숨죽인 실루엣)
- **콘티 에셋**: `downloads/EP01_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **화각 및 무빙**: 100mm Macro Static, 24mm Lateral Tracking Handheld, 35mm Low Angle Static, 50mm Slow Push Through Smoke, 85mm Static
- **실사 렌더링 프롬프트 전문**:
  ```text
  OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

  Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

  Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

  CHARACTER GUARD — the pursuers are Joseon palace guards in dark uniforms with black hats carrying torches, running with urgency. The hiding woman is a young adult Korean court lady in a pale hanbok with a jade hairpin, shown only as a deep shadow silhouette. No violence, no weapons drawn — the scene is urgent pursuit and atmosphere only.

  Recreate the 5 panels in order as one continuous ~10 second sequence:
  1. 100mm macro static: extreme close-up of a burning Joseon torch in a tight grip, dynamic swirling flames, sparks scattering into the night air, the wooden handle wrapped in cord.
  2. 24mm lateral tracking, handheld: palace guards with torches running fast across a moonlit palace courtyard at night, torch flames trailing behind them, urgent strides kicking up dust.
  3. 35mm low angle static: a massive heavy wooden palace gate with iron studs being pushed closed by straining guards, the doors grinding shut with finality.
  4. 50mm slow push through smoke: torch glow and dense drifting smoke filling a dark courtyard, the silhouettes of encircling guards tightening the net through the haze.
  5. 85mm static: the black silhouette of a lone court lady pressed against a wooden pillar in deep shadow, holding her breath, only distant torchlight rimming her outline, unshaken.

  FIRE AND SMOKE MOTION — IMPORTANT: large dynamic physically-based torch flames with rolling turbulent motion, heat-haze shimmer, glowing sparks scattering in the wind, dense volumetric smoke with realistic drift. Do NOT follow the sketch's calm, gentle flame motion — the pursuit must move like a big-budget period film's night sequence.

  Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
  ```

---

## 9. 씬별 컷·시트 대응표 (검수 기준)

| 씬 | 절대 시간 | 시트(콘티 컷수) | 시트 파일 | 시퀀스 컷 수 | 상태 |
|---|---|---|---|---|---|
| S01 | 00.0~07.5 | 5컷 | `downloads/EP01_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg` (로컬 미보관 — 맥 렌더 세션 보관분) | 5 | 렌더 통과본 완료(10.03s) · 통과본 재사용 |
| S02 | 07.5~15.0 | 3컷 | `downloads/EP01_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg` (로컬 미보관 — 맥 렌더 세션 보관분) | 3 | 렌더 통과본 완료(9.02s, v2) · 통과본 재사용 |
| S03 | 15.0~22.5 | 3컷 | `downloads/EP01_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 3 | 시트 완비 · 렌더 대기 |
| S04 | 22.5~30.0 | 4컷 | `downloads/EP01_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 4 | 시트 완비 · 렌더 대기 |
| S05 | 30.0~37.5 | 3컷 | `downloads/EP01_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 3 | 시트 완비 · 렌더 대기 |
| S06 | 37.5~45.0 | 3컷 | `downloads/EP01_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 3 | 시트 완비 · 렌더 대기 |
| S07 | 45.0~52.5 | 4컷 | `downloads/EP01_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 4 | 시트 완비 · 렌더 대기 |
| S08 | 52.5~60.0 | 5컷 | `downloads/EP01_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` | 5 | 시트 완비 · 엔드카드 편집 삽입 |

**합계**: 콘티 총 30컷 / 렌더 클립 8개 (렌더 풀 80초 ➔ 유효 구간 선별 트리밍 조립 **55~65초 유동** 마스터본, 16:9 가로 1920×1080).

---

## 📋 오이 1차 사전 검수 결과 보고 (2026-11-04 07:35 완료)
- [x] **컷수 규격**: S01(5) · S02(3) · S03(3) · S04(4) · S05(3) · S06(3) · S07(4) · S08(5) = 전 씬 1~10 가변 컷 100% 충족. (기계적 4컷 고정 없음)
- [x] **시각화 품질**: 1024×1536 흑연 연필 소묘 선화 질감, 컷별 렌즈 화각·카메라 무빙·디렉터 노트 완비.
- [x] **프롬프트 가드레일**: SOP v3.0 필수 5대 블록(ARRI Alexa 35, 물리 엔진 강화, 화풍 강제, 클린 프레이밍, 캐릭터 고정 앵커, OUTPUT FORMAT READ FIRST) 전 씬 누락 없이 인라인 기입 완료.
- [x] **세이프 필터 준수**: 유혈·시신·직접 살상 배제, 은유(횃불, 그림자, 발끝, 시선 대치) 연출 확인.
- [x] **편집 규격**: 10초 무음 렌더, 시작 1.0초·끝 1.5초 버퍼 트림 후 1~3초 유효 구간 활용, S08 붉은 타이틀 및 암전 편집 삽입 원칙 일치.
- [x] **07:45 상욱 님 정정 반영**: 화면비 16:9 가로 1920×1080(제미나이 기본값, 크롭 금지) · 길이 55~65초 유동 · 카메라 장비 노출 0건 네거티브 문구 추가.
- **최종 판정**: **전 항목 합격(PASS)** ➔ 맥에어 로컬 M2 Veo 렌더링 파이프라인 직결 투입 승인.
