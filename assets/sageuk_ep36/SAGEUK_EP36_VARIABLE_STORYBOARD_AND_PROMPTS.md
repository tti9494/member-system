# 「혈화의 궐」 EP36 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제36화 「검은 잔칫집」 8썬표(`master_screenplay/SEASON_02_MASTER_SCREENPLAY.md` 행 200~220, 원전: 제36장 정본) + `characters.md` 캐릭터 앵커 + EP20~EP35 원장 템플릿(동일 규격)
> **범위**: EP36 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 검은 잔칫집**: 검은 깃발 — 사람들의 몸값 위에 세워진 깃발. 잔당의 목적은 왕을 죽이는 것이 아니라 왕이 왕이 아니게 만드는 것. **반역 결사 고함 채비 전면 배제(정본 안티슬롭)** → 치환 [변두리 잔칫집 검은 깃발과 음모 거래의 차가운 긴장] — `no assembly, no crowds, no shouting, no raised voices` 전 썬 상설, 잔칫집은 조용한 거래의 집이다. **결의 고함 슬롭 배제(정본 안티슬롭)** → 설화의 결의는 "여자의 자리에서 여자가 물어야 할 것이 있나이다"의 낮은 단언 — `no raised voice, no gesture, no melodrama`, 세 사람의 침묵이 곧 동의다. **중궁전 방침 매크로** → 화려하지만 차가운 중전의 떨잠(떨잠·첩지 가체)이 한 번 흔들리는 미세 흔들림 — 중전은 **뒷모습·그림자 실루엣만**(plan 지정 앵커, 얼굴 미노출). **소품·복선 인계(EP34~35 → EP36)**: EP35 S6 회랑 저편의 **증인**이 본화 S4에서 「중궁전」으로 지목되고, EP34 S1~S3에서 옥사로 흘러 등사본이 퍼진 밀서의 확산이 S3 "밀서가 퍼지는 순간" 내레이션으로 귀결된다. **S8 발소리 훅**은 EP37 「회랑의 피바람」으로의 연결 — 다가오는 인물은 정체 불명(뒷모습·얼굴 미노출)으로 유지한다. **킬러 컷 미배정**: EP36은 특수 훅 허용 화(EP30·EP41·EP49·EP50)가 아님 — 초슬로우 훅 재투입 없음, 전 썬 통상 가변 호흡. **신규 무대 캐릭터 가드**: S1 잔칫집 거래 인물들은 무명의 서민 — 얼굴 각인 금지, 다음 화 재등장 전제 없음. **무결-내레이션 동일 보이스 ID(`ko-KR-Wavenet-C`) 이중 배역** — EP15 4중 장치 계승(트랙 분리 합성·파일명 규칙·피치 차등·믹싱 실측), §0-13 참조.

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
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **깃발의 정지**(the black cloth hanging heavy and barely breathing in the night air, the coins' weight settling on wood, the oil flame steady), S02 **보고의 침묵**(both nearly still, only breath and cloth, the flame steady), S03 **반 칸의 흔들림**(the sleeve trembling once and going still, the braced hand steady again, the flame steady), S04 **이름의 무게**(the hem of her step settling, the flame steady, the paper unmoving), S05 **세 사람의 정지**(all three nearly still, only breath and cloth, the flame steady), S06 **떨잠의 한 번**(the tteoljam ornaments trembling faintly once, the candle flames bending slightly and recovering, the shadows holding), S07 **문 아래의 빛**(only the lantern light breathing, the hairline of light beneath the doors steady, the night air still), S08 **발소리의 마침**(the hem's step and settling cloth, the lantern light trembling faintly as the figure passes, then nothing).
5. **세이프 필터**: 밀서·거래 종이의 시각적 실체는 **바랜 먹 자국과 낙관 인영 등 시각적 도장뿐** — `faded ink strokes and seal impressions as visual stamps only, never resolving into readable letters` 해당 썬 상설. 검은 깃발은 **무문(無文)의 검은 천** — 깃발에 글자·상징 일체 없음. 독·흉기·피·폭력 일체 없음 — `no violence, no blood anywhere` 상설. 전 등장 인물 성인 — `all characters are adults`. S1 거래는 조용한 판매 — 강압·난동·소란 일체 금지.
6. **문자 가드**: 본화 화면 노출 문자 요소는 인물·사물 뿐 — 판독 가능한 글자 일체 없음(`no readable letters, no characters, no labels anywhere` 상설). S8 발소리 씬에 어떤 간판·문패도 등장시키지 않는다. 엔드카드 자막(제37화 「회랑의 피바람」에서 계속)은 편집 단계 삽입.
7. **입모양 배제 가드(100화 전편 규격)**: 무결 발화 2구(S2·S3)·설화 발화 2구(S4·S5)·내레이션 2구(S1·S7)는 전부 무음 렌더 + 사후 믹싱 — 화면은 **입모양 배제**, `lips closed throughout` 전 썬 상설. 발화 썬은 보이스오버·리액션 샷으로 처리(립싱크 붕괴 원천 차단). S6·S8 무대사 — 렌더 무음. 이환 본화 발화 0구 — 침묵 렌더.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **설화**: a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, facing a woman's place with a woman's cold clarity, her resolve hidden entirely.
   - **이환**: a 24-year-old Korean monarch, young and clean-shaven, handsome and pale with fine clear features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), outwardly calm and composed while the danger settles beneath — in this hour the wavering is the evidence and he does not know it.
   - **무결**: a young Joseon military inspector, 25 years old, clean-shaven, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a faint old blade scar across his cheekbone, a solid unbroken silence about him, his report delivered low and exact.
   - **중전 윤씨(S6·S7)**: seen only from behind and as a shadow — an opulent royal purple and jade ceremonial dangui hanbok, elaborate royal hairpin ornaments (tteoljam, cheopji), her face never shown at any point, a splendid and cold silhouette only.
9. **광원 표기**: 시즌2 색 설계 — **석범·야기(夜氣)의 냉광과 촛불·등불·램프의 온광 교차**. S01 잔칫집 — 회유등 온광/골목 야기 냉광, S02~S05 밀실 — 등불 온광/창호 너머 야기 냉광, S06 중궁전 — 촛불 온광의 화려함과 냉기, S07 중전전 — 창와 등불 온점/야기 냉광, S08 회랑 — 등불 온점이 지나가며 흔들림/냉기. 전 씬 `no crushed blacks, no milky flat darkness` — 광원 소스 명시로 완전 암부 슬롭 차단.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S08 암전 이후의 붉은 타이틀(제37화 「회랑의 피바람」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9) — S1·S7 2구. **무결** `ko-KR-Wavenet-C` (Pitch -1.5, Speed 1.0, 묵직하고 절제된 무사 톤) — S2·S3 발화 2구. **설화** `ko-KR-Neural2-A` (Pitch -1.0, Speed 1.0, 차분하고 서늘한 결의의 톤) — S4·S5 발화 2구. 이환(Neural2-C)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 발화 0구 — 배정 제외. 무결-내레이션 동일 ID 이중 배역 차단은 §0-13.
13. **동일 보이스 ID 이중 배역 차단(정본 AG 검수 ⑦ 계승)**: **무결과 내레이션이 모두 `ko-KR-Wavenet-C`**이며 S1~S3에서 한 화에 공존한다. 혼동 차단 4중 장치 — ① 무결·내레이션 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 파일명 규칙 준수: 내레이션 `EP36_S1_NARRATION`·`EP36_S7_NARRATION`, 무결 `EP36_S2_MUGYEOL`·`EP36_S3_MUGYEOL`, ③ **피치 차등을 매 행 강제 표기**: 무결 `Pitch -1.5` / 내레이션 `Pitch 0.0` — 차 1.5, 무결이 아래로 가라앉고 내레이션은 중립 축, ④ 믹싱 단계에서 Pitch·톤 축 실측 확인. 하나라도 누락되면 재합성한다.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 3/4/4/3/3/3/4/4 = 28컷 — EP21~EP35 어느 배분과도 다른 신규 배분. S1·S7 24mm 와이드 롱테이크 원칙(정적 오프닝·클로징), S6 매크로 연타 방지(매크로 1컷 → 중전 뒷모습 50mm → 그림자 85mm), S8 발소리 2컷 + 암전 + 타이틀 4컷.

---

## 1. S01 검은 깃발이 세워진다 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP36_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 잔칫집, 오맛살 골목 — 검은 깃발이 세워짐. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "검은 깃발은 — 사람들의 몸값 위에 세워졌다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **반역 결사 고함 채비 배제의 핵심 썬** — 잔칫집은 조용한 거래의 집이다. 와이드(골목과 깃발) → 중경(동전과 접힌 종이가 오가는 거래) → 클로즈(무문 깃발 천)의 3컷 롱테이크. 군중·고함·채비 0건 — `no assembly, no crowds, no shouting`. 거래 종이는 판독 불가. 깃발은 무문의 검은 천.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — unnamed commoners only, no principal characters: two seated men of the poorest feast house in the outskirts of Hanyang trading quietly over a low table, coins and folded paper slips changing hands, no assembly, no crowds, no shouting, no raised voices anywhere in the lane. The folded slips carry faded ink strokes as visual marks only, never resolving into readable letters. The black flag over the door is plain unmarked black cloth, nothing written or painted on it. No violence, no blood anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm oil-lamp glow inside the shabby feast house against the cold night air of the empty lane is the season's cold-warm cross, one small flame and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the poor feast-house alley at night, a black flag raised over the shabby wooden feast house, the lane empty and cold, no crowds.
2. 50mm medium, static: coins and folded paper slips changing hands across a low table between two seated men, a quiet cold trade, no raised voices.
3. 85mm close, static: the plain black flag cloth hanging motionless over the feast house door in the cold night air, coarse woven fabric, nothing written on it.

FLAG MOTION — IMPORTANT: physically-based the black cloth hanging heavy and barely breathing in the night air, the coins' weight settling on wood, the oil flame steady — the flag is raised above the sale of merit, the trade is quiet, nothing is shouted, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 무결이 밀실에서 아뢴다 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP36_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 무결이 밀실에서 아뢴다. [묵직한 진단 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "그들은 왕을 죽이는 것에 관심이 없습니다. 왕이 왕이 아니게 만드는 데 — 관심이 있지요." (rel 5.0=절대 10.0, 사후 믹싱 보이스오버 — 입모양 배제)
- **연출 특이**: **무결 재등장 썬(EP15~16 이후)** — 익위사 별감 무관복·뺨 검흔·단단한 침묵 앵커. 보고 → 진단 얼굴 → 듣는 왕 → 왕의 이마에 닿는 말의 4컷. `no melodrama` — 진단은 낮고 정확하다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The inspector Mugyeol — a young Joseon military inspector, 25 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a faint old blade scar across his cheekbone, a solid unbroken silence about him, his report delivered low and exact — seated in report in the lamplit secret chamber at night. And the king — a 24-year-old Korean monarch, young and clean-shaven, no beard, handsome and pale with fine clear features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), outwardly calm and composed while the danger settles beneath — listening across the low table. No melodrama, no raised voices. No violence, no blood anywhere. All characters are adults. Lips closed throughout, the words carried by voiceover only. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm lamplight in the secret chamber against the cold night air beyond the lattice windows is the season's cold-warm cross, one small flame and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm medium, static: the inspector seated in report in the lamplit secret chamber at night, the king listening across the low table.
2. 85mm close, static: the inspector's young scarred face reporting low and exact, lips closed, the words carried by voiceover only.
3. 50mm medium, static: the king listening across the lamplit low table, the words settling, the lamp warm and the night cold beyond the lattice.
4. 85mm close, static: the king's handsome pale face receiving the diagnosis, outwardly calm and composed while the danger settles beneath, lips closed.

REPORT MOTION — IMPORTANT: physically-based both nearly still, only breath and cloth, the flame steady — the diagnosis is delivered low and exact, not to kill the king but to make the king not-king, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 왕이 흔들리는 모습이 반란의 신호 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP36_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm, 왕이 흔들리는 모습이 반란의 신호. [차가운 분석 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "밀서가 퍼지는 순간, 그들이 왕의 친위를 위협합니다. 왕이 흔들리는 모습 — 그것이 반란의 신호입니다." (rel 5.0=절대 17.5, 사후 믹싱 보이스오버 — 입모양 배제)
- **연출 특이**: **시리즈 킬러 모티브 "왕이 흔들리는 모습"의 구도화 썬** — 반란의 신호는 대사가 아니라 반 칸의 흔들림으로 운반된다. 일어나다 반 박자 늦는 왕(1컷) → 책상을 짚은 손 매크로의 한 번 떨림(2컷) → 다시 담담해진 얼굴(3컷) → 그것을 읽는 무결의 고정된 시선(4컷). 매크로 연타 방지 — 매크로 1컷 한정. 밀서 확산(EP34~35)은 내레이션으로만 귀결, 화면 밀서 등장 없음.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The king — a 24-year-old Korean monarch, young and clean-shaven, no beard, handsome and pale with fine clear features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), rising a half-beat too fast, one hand bracing on the desk edge, the wavering a watcher would mark. And the inspector — a young Joseon military inspector, 25 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a faint old blade scar across his cheekbone, his eyes steady and exact as he marks it. No melodrama, no outburst, no raised voices. No violence, no blood anywhere. All characters are adults. Lips closed throughout, the words carried by voiceover only. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm lamplight in the secret chamber against the cold night air beyond the lattice windows is the season's cold-warm cross, one small flame and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the young king rising from his seat a half-beat too fast, one hand bracing on the desk edge, the wavering a watcher would mark.
2. 100mm macro, static: the king's braced hand on the dark desk wood, the red dragon-robe sleeve trembling once and going still, gold embroidery catching the lamplight.
3. 85mm close, static: the king's face grown outwardly calm again, lips closed, the wavering already given away.
4. 50mm medium, static: the young clean-shaven inspector watching the king across the chamber, the faint blade scar on his cheek, his eyes steady and exact, the signal named in voiceover only.

SIGNAL MOTION — IMPORTANT: physically-based the sleeve trembling once and going still, the braced hand steady again, the flame steady — a half-beat of lost balance is already evidence, no outburst, no melodrama, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 설화의 덧붙임, 그 신호를 듣는 귀 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP36_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 설화의 덧붙임, 그 신호를 듣는 귀. [서늘한 확신 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "그리고 그 신호를 듣는 귀가 하나 있나이다. — 중궁전이오." (rel 4.0=절대 25.0, 사후 믹싱 보이스오버 — 입모양 배제)
- **연출 특이**: **증인 복선의 회수 썬** — EP35 S6 회랑 저편의 미지의 인물이 「중궁전」으로 지목되는 순간. 설화는 벽 곁 자리에서 한 걸음 나와 덧붙인다 — 간청이 아니라 덧붙임. 이름이 떨어지고 두 남자가 침묵으로 받는 3컷. 감정 과장 0건.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — three figures only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, facing a woman's place with a woman's cold clarity, her resolve hidden entirely — stepping forward from her place by the chamber wall, unhurried, the addendum offered low. And the king — a 24-year-old Korean monarch, young and clean-shaven, no beard, handsome and pale with fine clear features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), listening behind the desk. And the inspector — a young Joseon military inspector, 25 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a faint old blade scar across his cheekbone. No melodrama, no raised voices. No violence, no blood anywhere. All characters are adults. Lips closed throughout, the words carried by voiceover only. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm lamplight in the secret chamber against the cold night air beyond the lattice windows is the season's cold-warm cross, one small flame and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm medium, static: the court lady stepping forward from her place by the chamber wall, unhurried, the addendum offered low.
2. 85mm close, static: her pale face and cold piercing intelligent dark eyes, the name given low and exact, red lips closed, the words carried by voiceover only.
3. 50mm medium, static: the king and the inspector, both young and clean-shaven, taking the name in silence across the lamplit chamber, the weight of it settling, no one moves.

ADDENDUM MOTION — IMPORTANT: physically-based the hem of her step settling, the flame steady, the paper unmoving — an addendum, not a plea, the ear that listens for the signal is the Inner Palace, the name settles and no one moves, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 결의, 세 사람의 침묵 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP36_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 결의, 세 사람의 침묵. [낮은 결의 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "소녀가 가보겠나이다. 여자의 자리에서 — 여자가 물어야 할 것이 있나이다." (rel 3.5=절대 32.0, 사후 믹싱 보이스오버 — 입모양 배제)
- **연출 특이**: **결의 고함 슬롭 배제의 핵심 썬** — 결의는 높아지지 않는다. 낮고 평준한 단언(1컷) → 이의 없는 세 사람의 정지(2컷) → 옥비녀와 내리는 눈의 홀드(3컷). 침묵이 곧 동의다 — `no raised voice, no gesture, no melodrama`.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — three figures only. The court lady — a 21-year-old Korean woman disguised as a palace court lady, pale porcelain skin, cold piercing intelligent dark eyes, red lips, an elegant dark pastel court lady hanbok, neat traditional hair pinned with a single simple jade hairpin, facing a woman's place with a woman's cold clarity, her resolve hidden entirely — declaring her resolve low and level, no raised voice, no gesture. And the king — a 24-year-old Korean monarch, young and clean-shaven, no beard, handsome and pale with fine clear features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), behind the desk. And the inspector — a young Joseon military inspector, 25 years old, clean-shaven, no beard, of the Euiwisa, in a dark navy and black military official robe (mugwanbok) with a black official winged hat, a faint old blade scar across his cheekbone, by the wall. No melodrama. No violence, no blood anywhere. All characters are adults. Lips closed throughout, the words carried by voiceover only. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm lamplight in the secret chamber against the cold night air beyond the lattice windows is the season's cold-warm cross, one small flame and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm medium, static: the court lady declaring her resolve low and level in the lamplit chamber, no raised voice, no gesture, the resolve hidden entirely.
2. 35mm medium, static: the three of them in the lamplit secret chamber at night, the young king behind the desk, the young inspector by the wall, the court lady before them, no one objects and no one moves.
3. 35mm close static hold: the court lady's neat hair and single jade hairpin, her eyes lowered and settled, the resolve hidden entirely, lips closed.

RESOLVE MOTION — IMPORTANT: physically-based all three nearly still, only breath and cloth, the flame steady — the resolve is low and level, from a woman's place a woman has things to ask, three figures and no objection, the silence is the consent, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 중궁전의 방침 — 떨잠이 흔들림 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP36_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro, 중궁전의 방침 — 떨잠이 흔들림. [무대사]
- **연출 특이**: **중전 첫 등장 썬 — 뒷모습·그림자 실루엣 앵커(plan 지정)** — 얼굴은 단 한 번도 노출되지 않는다. 떨잠 매크로의 한 번 흔들림(1컷) → 화려하고 차가운 중궁전에서 종이 앞에 앉은 뒷모습(2컷) → 병풍 위 그림자 실루엣(3컷). 방침은 종이가 아니라 떨잠의 미세 흔들림으로 운반된다. 매크로 연타 방지 — 매크로 1컷 → 50mm → 85mm. 종이는 판독 불가. 무대사 — 렌더 무음.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure only, never facing camera: the Queen Yun seen only from behind and as a shadow — an opulent royal purple and jade ceremonial dangui hanbok, elaborate royal hairpin ornaments (tteoljam, cheopji) in her hair, her face never shown at any point, a splendid and cold silhouette only — seated amid the splendid candlelit Inner Palace at night, a folded paper laid before her, nothing readable on the paper. Her tall shadow stands on the paper folding screen in the candlelight. No melodrama, no violence, no blood anywhere. All characters are adults. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the splendid warm candlelight of the Inner Palace against the cold night air beyond its lattice is the season's cold-warm cross, many small flames and deep shadow. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: from behind, the elaborate royal tteoljam hairpin ornaments in the queen's hair trembling faintly once in the candlelight, her back to camera, her face never shown.
2. 50mm medium, static: the queen only from behind in the splendid candlelit Inner Palace, a folded paper laid before her, nothing readable on it, her face never shown.
3. 85mm close, static: her tall shadow standing on the paper folding screen in the candlelight, the splendid silhouette unmoving, no face anywhere.

PIN MOTION — IMPORTANT: physically-based the tteoljam ornaments trembling faintly once, the candle flames bending slightly and recovering, the shadows holding — the direction is given without a face, the ornaments tremble once and the palace keeps still, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 중궁전의 문이 열릴 것을 예감하는 밤 (절대 45.0~52.5 · 콘티 4컷)

- **시트**: `downloads/EP36_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드, 중궁전의 문이 열릴 것을 예감하는 밤. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "중전 윤씨 — 아버지의 폐위 계획을 왕에게 밀고하여 살아남은 여자." (rel 4.0=절대 47.0, 사후 믹싱)
- **연출 특이**: **무인물 와이드 클로징 썬(11-02 구도 원칙 — 원경 훅은 무인물 와이드)** — 인물 없이 문과 회랑만으로 밤을 운반한다. 닫힌 중문 와이드(1컷) → 처지 아래 로우 와이드(2컷) → 등불 회랑(3컷) → 문 아래 머리카락만 한 빛의 선(4컷). 중전의 과거(아버지의 밀고)는 회상 없이 내레이션으로만 — `no flashbacks, no memory scenes`. 문은 끝내 열리지 않는다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures anywhere: the queen's hall in the Inner Palace at night, its great doors closed, cold lantern light on the painted woodwork, the lantern-lit corridor running to the doors, empty and quiet. No flashbacks, no memory scenes, no time transitions — the night only waits. No violence, no blood anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere — no signs, no plaques, nothing written on the doors or walls.

LIGHT GUARD — IMPORTANT: the warm points of the lantern light against the cold blue night air of the Inner Palace is the season's cold-warm cross, the distance deep and dim. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the queen's hall in the Inner Palace at night, the great doors closed, cold lantern light on the painted woodwork, no figures.
2. 24mm low wide static, under the hall's eaves: the dark corridor and the closed doors beyond, the night holding its breath, no figures.
3. 50mm medium, static: the lantern-lit corridor leading to the closed doors of the queen's hall, empty and quiet, the warm lantern points against the cold night air.
4. 85mm close, static: the hairline of warm lantern light beneath the closed doors of the queen's hall at night, the door not yet opening.

DOOR MOTION — IMPORTANT: physically-based only the lantern light breathing, the hairline of light beneath the doors steady, the night air still — the doors stay closed, the night only expects them to open, no flashbacks, no memory scenes, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 문 앞까지 다가가는 발소리 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP36_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드, 문 앞까지 다가가는 발소리 → 암전 → 타이틀. [무대사] / 자막: 제37화 「회랑의 피바람」에서 계속
- **연출 특이**: **EP37 훅 썬** — 치마폭이 회랑 바닥을 가로지르고(1컷), 뒷모습 인물이 닫힌 문 앞에 멈추고(2컷), 암전(3컷) → 타이틀(4컷, 편집 단계). 걸어오는 이는 **정체 불명** — 뒷모습만, 얼굴 미노출 — EP37 「회랑의 피바람」의 자객 다섯과의 조우를 위한 복선 유지. 무대사 — 렌더 무음, 발소리는 사후 믹싱.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure only, seen from behind, never identified: a single figure in a dark court lady hanbok walking the lantern-lit corridor toward the closed doors of the queen's hall at night, seen from behind and in hem-first detail, the face never shown, nothing known of them. No violence, no blood anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere — no signs, no plaques, nothing written on the doors or walls.

LIGHT GUARD — IMPORTANT: the warm points of the corridor lanterns against the cold blue night air is the season's cold-warm cross, the distance deep and dim. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 50mm low medium static: the hem of a hanbok skirt crossing the lantern-lit corridor floor toward the closed doors of the queen's hall, the wearer unseen above the frame's edge.
2. 50mm medium static: a single figure in a dark court lady hanbok stopping before the closed doors of the queen's hall at night, seen from behind, the face never shown.
3. the frame sinking into complete black, no text, held.
4. end card for the edit stage only — one vertical column of red Korean characters on black (the render must end in complete black; the title card is inserted in editing).

FOOTSTEP MOTION — IMPORTANT: physically-based the hem's step and settling cloth, the lantern light trembling faintly as the figure passes, then nothing — the footsteps arrive at the doors and go quiet, who walks is not shown, the render ends in complete black, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션(S1·S7) — "검은 깃발은 — 사람들의 몸값 위에 세워졌다." / "중전 윤씨 — 아버지의 폐위 계획을 왕에게 밀고하여 살아남은 여자."를 운반하는 목소리 |
| 무결 | `ko-KR-Wavenet-C` | -1.5 | 1.0 | 묵직한 절제의 진단(S2·S3) — 아래로 가라앉는 낮은 단언. 내레이션과 동일 ID — §0-13 4중 장치 필수 |
| 설화 | `ko-KR-Neural2-A` | -1.0 | 1.0 | 서늘한 확신·낮은 결의(S4·S5) — 차분하고 서늘한 결의의 톤, 거의 속삭임. 지목(S4)과 결의(S5)가 같은 톤 위에서 가중 |

본 화 대사 4구(무결 2 + 설화 2) + 내레이션 2구 + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션·효과음 사후 믹싱. 발화 4구 전부 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S6·S8 무대사 — 렌더 무음. 이환(Neural2-C) 본화 발화 0구 — 침묵, 배정 제외. 중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **세이프티 가드 준수**: 밀서·거래 종이의 시각적 실체는 바랜 먹 자국과 인영뿐 — 검은 깃발은 무문 — 독·흉기·피 일체 미렌더.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:05,600
검은 깃발은 — 사람들의 몸값 위에 세워졌다.

2
00:00:10,000 --> 00:00:14,300
그들은 왕을 죽이는 것에 관심이 없습니다. 왕이 왕이 아니게 만드는 데 — 관심이 있지요.

3
00:00:17,500 --> 00:00:22,000
밀서가 퍼지는 순간, 그들이 왕의 친위를 위협합니다. 왕이 흔들리는 모습 — 그것이 반란의 신호입니다.

4
00:00:25,000 --> 00:00:28,200
그리고 그 신호를 듣는 귀가 하나 있나이다. — 중궁전이오.

5
00:00:32,000 --> 00:00:35,800
소녀가 가보겠나이다. 여자의 자리에서 — 여자가 물어야 할 것이 있나이다.

6
00:00:47,000 --> 00:00:51,000
중전 윤씨 — 아버지의 폐위 계획을 왕에게 밀고하여 살아남은 여자.

7
00:00:58,000 --> 00:00:59,800
제37화 「회랑의 피바람」에서 계속
```

- 시작 시각은 정본 rel 수치(3.0→2.0 / 5.0→10.0 / 5.0→17.5 / 4.0→25.0 / 3.5→32.0 / 4.0→47.0)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S6·S8 무대사는 SRT 미기재.
- 7번 자막(58.0~59.8)은 암전 이후 삽입 — S08 렌더는 완전 암전으로 끝나고 타이틀은 편집 단계 참조.
- TTS 트랙 분리: 내레이션 2구(`EP36_S1_NARRATION`·`EP36_S7_NARRATION`)와 무결 2구(`EP36_S2_MUGYEOL`·`EP36_S3_MUGYEOL`)는 반드시 별도 세션에서 합성 — 동일 ID `ko-KR-Wavenet-C` 이중 배역 차단(§0-13). 설화 2구는 `EP36_S4_SEOLHWA`·`EP36_S5_SEOLHWA`.

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP36_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP36_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep36_sheets.py` (`python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP36_QC_CHECKLIST.md` |
