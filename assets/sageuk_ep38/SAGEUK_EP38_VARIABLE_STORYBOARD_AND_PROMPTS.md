# 「혈화의 궐」 EP38 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제38화 「추적의 발자국」 8썬표(`master_screenplay/SEASON_02_MASTER_SCREENPLAY.md` 행 235~255, 원전: 제38장 정본) + `characters.md` 캐릭터 앵커(뱃사공 조연 앵커 본화 착수와 함께 신규 등록) + EP20~EP37 원장 템플릿(동일 규격)
> **범위**: EP38 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 추적의 발자국**: 한양 뒷골목 → 성밖 강가 길 → 나루터 → 집무실 → 강. **추적 도그마 편집 배제(정본 안티슬롭)** → 치환 [신발의 흙·옷깃의 짚·손톱 밑의 기름 때 — 감각 나열로 추적] — S1은 **무인물 매크로 감각 나열 썬**, 발자국·흙·짚·기름 때만으로 밤의 추적이 시작된다(`no figures anywhere`). **"길이 열렸다" 슬롭 배제(정본 안티슬롭)** → 장엄한 완주 몽타주 대신 **무결의 사십 리 주파 보고(S6, 무겁고 절제된 보이스오버)** 와 **왕의 단호한 한마디 "가라"(S7)** 로 종결 — S5의 달리기는 영웅 프레임 없이 젖은 밤길의 물리적 소모(헛간숨, 젖은 겉옷, 성벽에 대는 손)로만 표현. **나루터 밤 풍경(plan 지정)** — 달빛 아래 검은 강물 반사(`moonlight on moving black water`)와 물안개 헤이즈(`mist haze`)가 S2~S4·S8의 광원 축. **무결 나이 앵커(EP37 계승 — plan 지정)**: **28세 청년 무관 앵커 엄격 유지 — 노화 금지** — 시트·프롬프트 전부 `28 years old, clean-shaven, no beard` 인라인. 본화는 밤비 주파 반영으로 **젖은 도포/무관복 앵커**(EP37 마른 무관복에서 갱신 — plan 지정). **뱃사공 조연 신규 앵커 등록(plan 지정)**: 주름진 50대 나루터 노사공, 삼베옷, 갓/패랭이 — `characters.md` 조연 란 본화와 함께 등록 완료(정본 AG ⑥ 이행). **동일 보이스 ID 3중 배역(Wavenet-C)**: 내레이션(0.0)·무결(-1.5)·뱃사공(-2.0) — §0-13 피치 사다리 장치 필수. **세이프티 가드**: 본화는 추적·심문 화로 유혈·흉기 트리거 원천 부재 — 독초는 짐 위장명 **약재** 그대로 `dried medicine roots`(마른 약재 뿌리), 밀서는 `a folded paper packet, its surface blank`(표면 백지), `no blood, no wounds, no injuries anywhere` 전 썬 상설. **킬러 컷 미배정**: EP38은 특수 훅 허용 화(EP30·EP41·EP49·EP50)가 아님 — 초슬로우 훅 재투입 없음.

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (달빛·물반사·헤이즈 / 촛불·야기 교차) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **젖은 돌의 기록**(the wet stone holding the print, clay crumbling from the shoe's heel, straw fragments stirring in the draft), S02 **밤 안개와 발걸음**(mist drifting across the road, the wet robe hem swinging, breath showing in the cold air), S03 **검은 강물의 반사**(moonlight on moving black water, the ferry rocking on its mooring lines, mist sliding past the pier), S04 **마른 뿌리와 종이**(the dried roots shifting faintly in the crate, the folded paper stiff under its cord, the hull's timbers creaking against the posts), S05 **사십 리의 소모**(the boots striking wet earth, breath showing in the cold, the soaked robe hem swinging heavy), S06 **촛불의 정적**(the candle flames steadying, the ink stone dark, the kneeling robe settling), S07 **초의 기울기**(the candle flames leaning as the doors part, the cold night air entering, the king's stillness), S08 **강의 소실**(the ferry shrinking into the mist, moonlight closing over the fading wake, the river closing over).
5. **세이프 필터(본화 최우선 가드)**: 추적·심문 화 — 유혈·흉기·상처 트리거 원천 부재. `no blood, no wounds, no injuries anywhere` 전 썬 상설. 독초는 `dried medicine roots`(짐 위장명 약재 — 정본 대사 그대로), 밀서는 `a folded paper packet, its surface blank` 지칭. 전 등장 인물 성인 — `all characters are adults`. 뱃사공은 무명 조연 — 이름 부여 없이 `the old ferryman`으로만 지칭.
6. **문자 가드**: 화면 노출 문자 요소 일체 금지 — `no readable letters, no characters, no labels anywhere` 상설. 나루터 팻말·선착장 간판에 글자를 새기지 않는다(`no signboards, nothing written anywhere` — 시트 단계에서 「渡船場」 팻말 이입 결함을 재렌더로 교정한 이력, 렌더 가드로 상설). 집무실 병풍·표두 서화는 `faint abstract ink brush strokes, no readable characters` 지정. 엔드카드 자막(제39화 「종이의 먹 냄새」에서 계속)은 편집 단계 삽입.
7. **입모양 배제 가드(100화 전편 규격)**: 무결 발화 3구(S3 질문·S4 속마음·S6 보고)·뱃사공 1구(S3)·이환 1구(S7)·내레이션 1구(S1)은 전부 무음 렌더 + 사후 믹싱 — 화면은 **입모양 배제**, `lips closed throughout` 전 썬 상설. 발화 썬은 보이스오버·리액션 샷으로 처리. S2 무대사·S5 효과음(발 소리)·S8 무대사 — 렌더 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **무결(28세 고정 + 본화 젖은 도포)**: a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone, a solid unbroken silence about him.
   - **뱃사공(신규 조연 앵커 — characters.md 등록)**: a weathered 50-year-old river ferryman, deep wrinkles and sun-darkened skin, grey stubble, coarse hempen commoner clothes (sambe), a worn woven straw rain-hat (paeraengi) pushed back on his head, a poling staff in his hand, a calm unhurried river-man's ease about him.
   - **이환**: a 24-year-old Joseon king, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing.
9. **광원 표기**: 시즌2 색 설계 — **달빛의 냉광과 검은 강물 반사, 물안개 헤이즈 / 집무실 촛불 온광과 창밖 야기 냉광 교차**. S1~S2 성내·성밝 밤길(달빛 + 원경 횃불), S3~S4 나루터(달빛 아래 검은 강물 반사 + 물안개 헤이즈 + 선착장 등화기 소점), S5 밤길 질주(달빛 능선), S6~S7 집무실(촛불 온광 vs 창밖 야기 냉광), S8 강 한가운데(달빛 + 소실하는 물결). 전부 `no crushed blacks, no milky flat darkness` — 광원 소스 명시로 완전 암부 슬롭 차단.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S08 암전 이후의 붉은 타이틀(제39화 「종이의 먹 냄새」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9) — S1 1구. **무결** `ko-KR-Wavenet-C` (Pitch -1.5, Speed 1.0, 묵직하고 절제된 무사 톤) — S3 질문·S4 속마음·S6 보고 3구. **뱃사공** `ko-KR-Wavenet-C` (Pitch -2.0, Speed 0.95, 느긋한 늙은 나루터 톤) — S3 1구. **이환** `ko-KR-Neural2-C` (Pitch -0.5, Speed 0.95, 단단하고 기품 있는 어조) — S7 "가라." 1구. 설화(Neural2-A)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. 동일 ID 3중 배역 차단은 §0-13.
13. **동일 보이스 ID 3중 배역 차단(EP37 §0-13 4중 장치의 3중 확장)**: **내레이션·무결·뱃사공이 모두 `ko-KR-Wavenet-C`**이며 한 화에 공존한다. 혼동 차단 4중 장치 — ① 3배역 TTS는 **반드시 별도 세션에서 트랙 분리 합성**(같은 세션 연속 합성 금지), ② 파일명 규칙 준수: 내레이션 `EP38_S1_NARRATION`, 무결 `EP38_S3_MUGYEOL`·`EP38_S4_MUGYEOL`·`EP38_S6_MUGYEOL`, 뱃사공 `EP38_S3_BOATMAN`, 이환 `EP38_S7_IHWAN`, ③ **피치 사다리를 매 행 강제 표기**: 내레이션 `Pitch 0.0` > 무결 `Pitch -1.5` > 뱃사공 `Pitch -2.0` — 무결-내레이션 차 1.5, 무결-뱃사공 차 0.5(무결이 중간축, 뱃사공이 최하부 — 나이톤과 합류), ④ 믹싱 단계에서 Pitch·톤 축 실측 확인. 하나라도 누락되면 재합성한다.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/3/5/4/3/4/2/3 = 28컷 — EP19(4/3/3/3/4/3/4/4)·EP20(4/3/4/3/3/4/3/4)·EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)·EP26(3/4/3/4/3/4/3/4)·EP27(4/4/3/4/3/3/4/3)·EP28(4/4/3/3/4/4/3/3)·EP29(3/4/3/3/4/3/4/4)·EP30(4/3/4/4/3/3/4/3)·EP31(4/3/3/4/4/3/3/4)·EP32(3/4/3/4/4/3/4/3)·EP33(4/3/4/3/3/4/3/4)·EP34(3/4/4/2/3/3/4/5)·EP35(4/3/4/2/3/4/3/5)·EP36(3/4/4/3/3/3/4/4)·EP37(4/3/5/4/3/3/3/3) 어느 배분과도 다른 신규 배분. S3 나루터 심문-대치 씬에 5컷 최대 배분(대화 템포 가변 원칙 — 와이드 나루터 → 착안 50mm → 뱃사공 클로즈 → 짐 중경 → 무결 클로즈), S1 감각 나열 매크로 4컷 오프닝, S7 왕의 허락 2컷 최소 배분(절제의 종결 — 클로즈 1컷 + 기상 1컷), S8 소실 1컷 + 암전 + 타이틀 3컷.

---

## 1. S01 젖은 돌 위 자객의 신발 흙 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP38_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 발자국, 젖은 돌 위 자객의 신발 흙. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "이번 추적은 — 발을 찾는 것이었다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **무인물 감각 나열 오프닝 썬** — 추적 도그마 편집(뒤따르는 발소리, 도그마 몰이컷)의 배제가 직결되는 썬. 발자국(1컷) → 신발 흙(2컷) → 문설주의 짚(3컷) → 기름 때를 읽는 장갑 끝(4컷) — **흙·짚·기름 때가 유일한 화자**다. `no figures anywhere` — 4컷 전부 무인물 매크로(4컷의 장갑 끝은 손 부분만).
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures anywhere: a dark wet stone back alley of Joseon Hanyang at night, rain on the stones, only close traces — a fresh footprint pressed into wet dust, a commoner's shoe heel with riverbank clay crumbling, straw fragments caught on a wooden door's lintel, a gloved fingertip touching dark grease grime at the stone edge. Nothing written anywhere, no signboards. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: cold moonlight and a distant torch glow on the wet stones, the prints and traces glistening, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a fresh footprint pressed into the wet dust of a dark stone step, rain gathering in its edges.
2. 100mm macro, static: the heel edge of a dark commoner's shoe lifting from the wet stone, riverbank clay crumbling from it, the print left behind.
3. 100mm macro, static: a few straw fragments caught on the wooden lintel of a night door at shoulder height, stirring in the cold draft.
4. 100mm macro, static: a gloved fingertip touching a smear of dark grease grime at the door's stone edge, the trace being read, no face anywhere.

TRACE MOTION — IMPORTANT: physically-based the wet stone holding the print, clay crumbling from the shoe's heel, straw fragments stirring in the draft — the chase is read from the ground and never shown, no figures anywhere, lips closed throughout, the words in voiceover only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 발자국이 한양 성 밖으로, 강가의 밤배로 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP38_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 뒤따름, 발자국이 한양 성 밖으로, 강가의 밤배로. [무대사]
- **연출 특이**: **무대사 추적 썬** — 대사 0건, 발자국의 이행(성문 → 풀 → 강)만이 서사다. 소(집시)문 추적(1컷) → 흙길이 끝나는 지점(2컷) → 달빛 아래 검은 강 와이드(3컷). `no cries, no hoofbeats` — 추적은 조용하다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the inspector only: a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — following a trail of footprints out of the walled city at night. No other figures. Nothing written anywhere, no signboards. No blood, no wounds, no injuries anywhere. No speech. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: cold moonlight on the road and the wet grass, a distant torch glow at the small postern gate, moonlight reflecting on moving black water ahead, mist haze, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm medium tracking: the rain-soaked inspector following a trail of footprints out through a small postern gate of the walled city at night, torch light far behind him.
2. 35mm medium, static: the footprints leaving the road's dust into wet grass, the black river dark ahead under moonlight, mist drifting.
3. 24mm wide, static: the night river road running down to the water, moonlight reflecting on moving black water, a haze of river mist, no boat yet in sight.

TRAIL MOTION — IMPORTANT: physically-based mist drifting across the road, the wet robe hem swinging, breath showing in the cold air — the trail walks itself out of the city, no cries, no hoofbeats, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 뱃사공에게 짐을 묻는 무결 (절대 15.0~22.5 · 콘티 5컷)

- **시트**: `downloads/EP38_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 나루터, 뱃사공에게 짐을 묻는 무결. [낮은 물음 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "이 배 — 어디로 가는가." (rel 2.5=절대 16.5) / [느긋한 · 뱃사공/`ko-KR-Wavenet-C`, Pitch -2.0, Speed 0.95] "약재요. 귀성에서 오는 짐이지." (rel 4.0=절대 18.0) — 전부 사후 믹싱 보이스오버, 입모양 배제
- **연출 특이**: **심문-대치 썬(최대 5컷 배분)** — 본화 유일의 대화 썬. 나루터 와이드(1컷) → 축축한 판자 착안(2컷) → 돌아보는 뱃사공 클로즈(3컷) → 짐 베일 중경(4컷) → 무결 클로즈(5컷). 두 발화 모두 보이스오버 — `lips closed` 엄수, 립싱크 렌더 시도 금지. 뱃사공은 무명 조연 — 이름·배경 서사 없이 풍경의 일부로.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the inspector and the old ferryman only. The inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — stepping onto the wet planks of the pier. And the old ferryman — a weathered 50-year-old river ferryman, deep wrinkles and sun-darkened skin, grey stubble, coarse hempen commoner clothes (sambe), a worn woven straw rain-hat (paeraengi) pushed back on his head, a poling staff in his hand, a calm unhurried river-man's ease about him. Both adults. The question and the answer are carried by voiceover only, no speech in frame. Nothing written anywhere, no signboards. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: moonlight on moving black water and a mist haze over the river, one warm landing lamp on its post, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: a small night ferry landing, a flat-bottomed wooden ferry moored to posts, moonlight reflecting on black moving water, river mist hanging low, no signboards.
2. 50mm medium, static: the rain-soaked inspector stepping onto the wet planks of the pier, his question carried by voiceover only, lips closed.
3. 85mm close, static: the old ferryman turning unhurried on the ferry's deck, straw rain-hat pushed back, his answer carried by voiceover only, lips closed.
4. 50mm medium, static: the ferry's cargo, baskets and bound bundles of dried medicine roots under a woven straw cover, ropes crossed and knotted.
5. 85mm close, static: the young clean-shaven 28-year-old inspector's scarred face, level and unreadable, lips closed, the ferry lamp swinging faintly.

LANDING MOTION — IMPORTANT: physically-based moonlight on moving black water, the ferry rocking on its mooring lines, mist sliding past the pier — a question and an answer pass between two men and the lips never move, both lines are voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 귀성 — 독초의 뿌리, 밀서의 종이, 자객의 배 (절대 22.5~30.0 · 콘티 4컷)

- **시트**: `downloads/EP38_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 연결, 귀성 — 독초의 뿌리, 밀서의 종이, 자객의 배. [서늘한 연결 속마음 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "귀성 — 이 방면이 아닌 것이 없구나." (rel 3.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **짐의 연결 매크로 썬** — "귀성 = 만물의 소통로"라는 정본 서사를 짐의 세 기관으로 운반한다. 약재 뿌리 다발(1컷) → 백지 접지(2컷) → 저돌하는 배 중경(3컷) → 얼굴 클로즈(4컷). 독초는 짐 위장명 **약재** 그대로 `dried medicine roots` 지칭(세이프티 가드), 밀서는 `its surface blank`(문자 가드). 매크로 연타 방지 — 매크로 2컷 → 50mm → 85mm 스케일 이탈.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the inspector only: a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — reading the ferry's cargo in the lamplight. The cargo is baskets and bound bundles of dried medicine roots in straw rope and one small folded paper packet tied under cord, its surface blank. No other figures. Nothing written anywhere, no signboards. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm ferry lamp against cold moonlight on moving black water and a mist haze at the far bank, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: dried medicine roots bundled in straw rope inside an open wooden crate, the straw cover pulled back.
2. 100mm macro, static: a small folded paper packet tied under cord tucked among the bundles, its surface blank, rain-damp at one corner.
3. 50mm medium, static: the same flat-bottomed wooden ferry moored to its wooden posts, one short mast with a furled cloth sail, simple planks and ropes, moonlight sliding on the moving black water, mist at the far bank.
4. 85mm close, static: the young clean-shaven 28-year-old inspector's scarred face in the ferry lamplight, cold and exact, lips closed, the words carried by voiceover only.

CARGO MOTION — IMPORTANT: physically-based the dried roots shifting faintly in the crate, the folded paper stiff under its cord, the hull's timbers creaking against the posts — one glance reads the whole river trade and names the port, the realization is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 사십 리를 달려 돌아오는 무결 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP38_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드, 사십 리를 달려 돌아오는 무결. [효과음] 발 소리 (rel 2.0=절대 31.0, 사후 믹싱 — 렌더 무음)
- **연출 특이**: **소모의 썬** — "길이 열렸다" 완주 슬롭의 배제가 직결되는 썬. 능선 먼 발걸음 와이드(1컷) → 여울 질주 중경(2컷) → 성벽에 손을 대고 헛간숨 쉬는 도착(3컷). 영웅 프레임 없이 젖은 겉옷·헛간숨·기운 난 어깨로 사십 리를 계산한다. 발 소리는 사후 믹싱 — 렌더 무음.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the inspector only: a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — running the night road back to the city, spent and breathing hard. No other figures. Nothing written anywhere, no signboards. No blood, no wounds, no injuries anywhere. No speech. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: cold moonlight on the dark hill road and the shallow ford, a faint warm glow at the far postern gate, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: a single running figure far up the dark hill road at night, small against the moonlit ridge, breath showing in the cold air.
2. 35mm medium, static: the rain-soaked inspector running through a shallow ford in the road, the soaked robe hem heavy and dripping, water scattering from his boots.
3. 50mm medium, static: him arriving bent with breath at a small postern gate, one hand flat against the wet wall stones, the night's forty ri spent in his shoulders.

RUN MOTION — IMPORTANT: physically-based the boots striking wet earth, breath showing in the cold, the soaked robe hem swinging heavy — forty ri spent in the body, no heroic slow motion, no triumphant score-frame, lips closed throughout, footsteps in post-mixed sound only. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 왕에게 아뢰는 무결 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP38_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 왕에게 아뢰는 무결. [묵직한 결의 · 무결/`ko-KR-Wavenet-C`, Pitch -1.5, Speed 1.0] "유배지가 홀로 있지 않습니다. 귀성에서 바다를 타고 내려오는 손이 있습니다. 그 손이 무엇을 쥐고 있는지 — 제가 확인하겠습니다." (rel 6.0=절대 39.5, 사후 믹싱)
- **연출 특이**: **보고 썬** — "길이 열렸다" 슬롭의 종결지. 왕의 긴 보고는 고양된 독백이 아니라 **무겁고 절제된 짧은 절차**로 운반된다. 집무실 와이드(1컷) → 보고하는 무결 클로즈(2컷) → 듣는 왕 중경(3컷) → 더 낮아지는 절(4컷). 보고 전문은 보이스오버 — `lips closed` 엄수.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king and the inspector only. The king — a 24-year-old Joseon king, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing. And the inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — kneeling low on the floor of the king's night office. Both adults. The long report is carried by voiceover only, no speech in frame. The hanging scrolls show only faint abstract ink brush strokes, no readable characters. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: warm candlelight against the cold blue night at the window, the rain-soaked robe steaming faintly in the candle warmth, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the king's night office, warm candles against the cold window night, the king at his desk, the rain-soaked inspector kneeling low on the floor.
2. 85mm close, static: the young clean-shaven 28-year-old inspector's scarred face, level and exact, the long report carried by voiceover only, lips closed.
3. 50mm medium, static: the king listening at his desk, the red dragon robe in warm candle light, his face giving nothing.
4. 85mm close, static: the inspector bowing lower, resolve settling into his shoulders, lips closed, the last line carried by voiceover only.

REPORT MOTION — IMPORTANT: physically-based the candle flames steadying, the ink stone dark, the kneeling robe settling — the report is heavy because it is quiet, no raised voice, no dramatic gesture, the whole speech is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 왕의 허락 (절대 45.0~52.5 · 콘티 2컷)

- **시트**: `downloads/EP38_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 왕의 허락. [억누른 신뢰 · 이환/`ko-KR-Neural2-C`, Pitch -0.5, Speed 0.95] "가라." (rel 1.5=절대 46.5, 사후 믹싱)
- **연출 특이**: **절제의 종결 썬(최소 2컷 배분)** — 왕의 허락은 한마디와 한 번의 기상으로 전부다. 왕의 클로즈(1컷) → 기상하는 무결과 기우는 촛불(2컷). "가라"는 보이스오버 — `lips closed` 엄수. 2컷 최소 배분은 절제의 연출 그 자체다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the king and the inspector only. The king — a 24-year-old Joseon king, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing — giving one word of leave, carried by voiceover only. And the inspector — a young Joseon military inspector, 28 years old, clean-shaven, no beard, of the Euiwisa, in a rain-soaked dark navy and black military official robe (mugwanbok), the wet cloth clinging and dripping, with a black official winged hat, a sheathed sword at his hip, a faint old blade scar across his cheekbone — rising to go. Both adults. The hanging scrolls show only faint abstract ink brush strokes, no readable characters. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: warm candlelight against the cold blue night air entering as the doors part, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the king's face in candle light, quiet iron in the eyes, one word of leave carried by voiceover only, lips closed, the hanging scroll behind him showing only faint abstract ink brush strokes.
2. 50mm medium, static: the young clean-shaven 28-year-old inspector rising, the candle flames leaning as the doors part on the cold night air.

LEAVE MOTION — IMPORTANT: physically-based the candle flames leaning as the doors part, the cold night air entering, the king's stillness — the king's permission is one word and a door, nothing else is spent, the word is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 배가 사라지는 강 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP38_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드, 배가 사라지는 강 → 암전 → 타이틀. [무대사] / 자막: 제39화 「종이의 먹 냄새」에서 계속
- **연출 특이**: **EP39 훅 썬** — 소실 와이드(1컷) → 암전(2컷) → 타이틀(3컷, 편집 단계). 강은 배를 실어 없애고, 다음 화의 단서는 먹 냄새로 넘어간다. 무대사 — 렌더 무음. 렌더는 완전 암전으로 끝난다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures near the camera: the black river at night, a flat-bottomed wooden sailing ferry with a furled cloth sail shrinking into the downstream mist, moonlight closing over its fading wake, the mist taking it, small distant figures on the hull only as dots of silhouette. Nothing written anywhere, no signboards. No blood anywhere. No speech. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: cold moonlight on moving black water and the mist haze taking the boat, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the flat-bottomed wooden sailing ferry shrinking into the downstream mist on the black river at night, moonlight closing over its fading wake, the mist taking it.
2. the frame sinking into complete black, no text, held.
3. end card for the edit stage only — one vertical column of red Korean characters on black (the render must end in complete black; the title card is inserted in editing).

RIVER MOTION — IMPORTANT: physically-based the ferry shrinking into the mist, moonlight closing over the fading wake, the river closing over — the river takes the boat and forgives nothing, the next trace will be ink, the render ends in complete black, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션(S1) — "이번 추적은 — 발을 찾는 것이었다."를 운반하는 목소리 |
| 무결 | `ko-KR-Wavenet-C` | -1.5 | 1.0 | 묵직한 절제의 무사 톤(S3 질문·S4 속마음·S6 보고 3구) — 내레이션과 동일 ID — §0-13 4중 장치 필수 |
| 뱃사공 | `ko-KR-Wavenet-C` | -2.0 | 0.95 | 느긋한 늙은 나루터 톤(S3) — 무결·내레이션과 동일 ID — §0-13 피치 사다리 최하부 |
| 이환 | `ko-KR-Neural2-C` | -0.5 | 0.95 | 억누른 신뢰(S7) — "가라." 단단하고 기품 있는 어조 |

본 화 대사 4구(무결 3 + 뱃사공 1 + 이환 1) + 내레이션 1구 + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션·효과음(S5 발 소리 포함) 사후 믹싱. 발화 4구 전부 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S2 무대사·S5 효과음·S8 무대사 — 렌더 무음. 설화(Neural2-A)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **세이프티 가드 준수**: 본화는 유혈·흉기·상처 트리거 원천 부재 — 독초는 `dried medicine roots`(약재), 밀서는 백지 접지 지칭.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:04,600
이번 추적은 — 발을 찾는 것이었다.

2
00:00:16,500 --> 00:00:17,900
이 배 — 어디로 가는가.

3
00:00:18,000 --> 00:00:20,300
약재요. 귀성에서 오는 짐이지.

4
00:00:24,500 --> 00:00:26,900
귀성 — 이 방면이 아닌 것이 없구나.

5
00:00:39,500 --> 00:00:44,800
유배지가 홀로 있지 않습니다. 귀성에서 바다를 타고 내려오는 손이 있습니다. 그 손이 무엇을 쥐고 있는지 — 제가 확인하겠습니다.

6
00:00:46,500 --> 00:00:47,300
가라.

7
00:00:58,000 --> 00:00:59,800
제39화 「종이의 먹 냄새」에서 계속
```

- 시작 시각은 정본 rel 수치(3.0→2.0 / 2.5→16.5 / 4.0→18.0 / 3.5→24.5 / 6.0→39.5 / 1.5→46.5)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S2(무대사)·S5(효과음)·S8(무대사)은 SRT 미기재 — 효과음은 믹싱 원장 별도.
- 7번 자막(58.0~59.8)은 암전 이후 삽입 — S08 렌더는 완전 암전으로 끝나고 타이틀은 편집 단계 참조.
- TTS 트랙 분리: 내레이션 1구(`EP38_S1_NARRATION`), 무결 3구(`EP38_S3_MUGYEOL`·`EP38_S4_MUGYEOL`·`EP38_S6_MUGYEOL`), 뱃사공 1구(`EP38_S3_BOATMAN`), 이환 1구(`EP38_S7_IHWAN`) — 반드시 별도 세션에서 합성. 동일 ID `ko-KR-Wavenet-C` 3중 배역 차단(§0-13 피치 사다리: 내레이션 0.0 > 무결 -1.5 > 뱃사공 -2.0).

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP38_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP38_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep38_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP38_QC_CHECKLIST.md` |
