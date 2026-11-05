# 「혈화의 궐」 EP52 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제52화 「사경의 왕」 8썬표(`master_screenplay/SEASON_03_MASTER_SCREENPLAY.md` 행 39~, 원전: 제52장 정본) + `characters.md` 캐릭터 앵커 + EP20~EP51 원장 템플릿(동일 규격)
> **범위**: EP52 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: 사흘 밤낮 잠들지 못하는 왕 — 독은 살려 두고 부리는 것이었다. 그리고 병든 왕의 곁에서 종이가 움직인다. EP51 S8 엔드카드 「제52화 사경의 왕에서 계속」이 본화 S1 병상 오프닝에서 즉시 회수된다.
> **안티슬롭 ① — 의사 해설 독백 전면 배제(정본)**: 치환 [어의의 단 두 마디 차분한 진단]. 병세 강의·의학 해설 모놀로그 **렌더 0건**. S2의 전부는 발화 1구 — "독은 이미 몸에 있었소. 약이 아니라 — 몸이 기억하고 있던 것이오." 진맥 → 시선 → 약그릇의 3비트만이 진단을 담는다.
> **안티슬롭 ② — 궁 분열 나레이션 난립 배제(정본)**: 치환 [병상 좌우 '두 개의 문' 시각적 대비 하나]. S4는 **익위사의 칼(칼집째, 손은 칼집만) vs 궁녀의 은장도(차고만 있는)** 의 좌우 대칭 구도로 압축한다. 설명 컷·군중 컷·지목 컷 **렌더 0건**.
> **세이프티 가드(plan 절대 준수) — 금지 어휘 0건**: 생성기 `validate()`가 전 씬 소스(헤더·무드·로케이션·패널 5요소·디렉션)를 소문자 전수 스캔해 `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` **프로그램적 차단**(0건 확인). 진단의 '독'은 화면 요소가 아니라 어의의 대사(사후 믹싱)이며 렌더 프롬프트에는 **the substance**로만 기입. **흉기 노출 금지** — 칼은 칼집째, 손은 칼집만, 은장도는 차고만 있는 장식(뽑는 컷 0건). 유혈·상처·시신 요소 0건. `no violence, no blood, no wounds, no injuries anywhere` 전 썬 상설.
> **병상 AG 가드(정본 ①)**: **달빛 창살광(moonlight in bars through the lattice window) + 머리맡 약불(medicine brazier at the head of the bed) 이중 광원 소스**를 전 병상 썬(S1·S2·S4·S7·S8)에 명시. **병상 각도는 EP43과 좌우 반전 구도**(EP43 QC 2-19·재렌더 주의 7번 이월 기록 이행 — 침축 카메라 축을 EP43 서재 구도의 거울상으로, S1 슬로우 팬 좌→우·S7 필로우 축 반전). 등불·약불 가드 — `the brazier burns steady and low, never flickering like horror, never strobing` + `no crushed blacks, no milky flat darkness` 전 썬 상설.
> **백지 설계 교칙(EP45 확립, plan 명시)**: **S3 의정부 상소 종이·S5 옥통 소형 기록지 모두 가독 글자 0건** — 획선·먹 자국·짧은 획만 (`never rows of glyphs, no legible hangul, no legible hanja, no readable script of any kind` 3중 기재). S5의 기록은 **비녀의 옥통이 담을 수 있는 크기의 종이**로, 화면 밖으로는 비녀 안으로 갈무리된다.
> **의도 채색 — 엔드카드 적색 타이틀만**: 시트는 전부 흑연 명도이나 **S08 마지막 패널의 붉은 한글 타이틀만 의도 채색**(시트 크로마 실측 S08 0.17% — EP43 0.20%·EP49 0.18%·EP51 0.30%와 동일 급). **본화는 낙관 인주 없음**(EP51과 동일 — EP50의 낙관 인주 채색 규격 이월 금지). 그 외 채색은 전부 결함.
> **캐릭터 앵커(plan 지정)**: 이환 — **병상에 누운 30세 젊은 왕 앵커**(창백한 안색, 고통으로 찌푸려지는 미간, 백색 내의, **clean-shaven — 수염·스터블 0건**, 침상 안정이라 복식은 백의 단일 앵커, 붉은 곤룡포·익선관 혼입 금지) / 어의 — **조선 내의원 관복의 노어의 앵커**(흑립 관모, 차분하고 서늘한 진단, 주름진 노면) / 이설화 — **궁녀 복식·옥비녀 단일 로드 앵커**(다크 파스텔 궁녀 한복, 비녀 머리 끝에 장착된 **옥통**, 작은 종이를 갈무리하는 서늘한 사관적 눈빛) / 익위사 무관 — **칼집을 쥔 보위 자세 앵커**(남색·흑색 군복·흑립 갓, 칼집째 손쥔 보위, 뽑는 컷 0건). 중전·강무결·윤경헌 본화 미등장 — 앵커 미기재.
> **입모양 배제(100화 전편 규격)**: 내레이션 2구(S1·S4)·어의 1구(S2)·설화 2구(S3·S5) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. **어의의 진단도 화면 발화가 아니다** — 진맥 중의 목소리는 보이스오버로만 존재한다. S6·S7(무대사)·S8 렌더 전면 무음.
> **동일 보이스 ID 점검 — §0-13 불발동**: 본화 Wavenet 계열은 **내레이션 `ko-KR-Wavenet-C`(0.0) 단독 1배역** — 동일 ID 공존 0건(EP51 내레이션+흑영대 2중과 달라 장치 불요). Neural2-C는 어의(−1.5)·이환(−0.5)이 공유하나 **본화 이환 발화 0건**(혼수 썬) — 실질 충돌 없음, 톤 지문 구분(characters.md 조연 원칙). 피치 사다리: **내레이션 0.0 > 설화 −1.0 > 어의 −1.5**.
> **가변 컷 배분**: 3/3/4/4/4/3/4/3 = 28컷 — EP19~EP51 어느 배분과도 다른 신규 배분(생성기 `validate()` 프로그램 확인, PRIOR에 EP51분 4/4/4/3/3/3/4/3 포함). **두 개의 문(S4)·상소(S3)·옥통 기록(S5)·눈썹 4비트(S7) 4컷**이 서사 호흡의 기둥, S1·S2·S6·S8은 3컷 정적 호흡 — "3컷·4컷 고정" 슬롭 회피.

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (달빛 창살광 + 약불 이중 광원 축) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환**이 본화에서 특히 중요하다(달빛 창살광의 찬 기운과 약불의 온기가 흑백으로 굳으면 병상의 색 설계가 사라진다).
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **병상의 정지와 약 기운**(the slow pan across the bed, the breath barely lifting the coverlet, the thin steam rising from the medicine bowl), S02 **진맥의 정지된 접촉**(two fingers resting on the wrist, the head lifting slowly, the steam rising between them), S03 **상소 종이의 물성**(the paper's weight under the hand, the ruled lines under the light, the still air of the antechamber), S04 **두 문의 대칭 정지**(the guard's hand resting on the scabbard, the lady's folded hands, neither door moving), S05 **옥통의 갈무리**(the slip smoothed flat, the jade tube drawn from the hairpin, the slip rolled tight and slid inside), S06 **밤 복도의 공기**(frost holding on the boards, the two pools of lamplight, the dark between them), S07 **미간의 4비트**(the brow knotting and easing, the breath hitching and returning), S08 **가늘어지는 약 기운**(the steam thinning, the glow dimming, the frame sinking evenly into black).
5. **세이프 필터**: `poison`·`dying` 및 `death`·`dead`·`corpse`·`blood`·`suicide`·`necrosis`·`murder` 어휘 사용 절대 금지(plan — 생성기 validate() 차단 확인). `no violence, no blood, no wounds, no injuries anywhere` 전 썬 상설. **흉기 노출 금지** — 칼은 칼집째, 손은 칼집만, 은장도는 차고만 있는 장식. 전 등장 인물 성인 — `all characters are adults`. `no flashbacks, no memory scenes, no time transitions` 전 썬 상설.
6. **문자 가드(정본 AG ①) — 백지 설계 교칙(EP45 확립)**: 화면 노출 문자 요소 일체 금지 — `no readable letters, no characters, no labels anywhere` 상설. **S3 상소·S5 기록지 가독 글자 0건** — 획선과 먹 자국만 (`never rows of glyphs, no legible hangul, no legible hanja, no readable script of any kind` 3중 기재). 엔드카드 자막(제53화 「섭정의 상소」에서 계속)은 편집 단계 삽입 — S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 발화 5구(내레이션 S1·S4 / 어의 S2 / 설화 S3·S5) 전부 무음 렌더 + 사후 믹싱 — `lips closed throughout` 전 썬 상설. **어의의 진단(S2)도 보이스오버** — 진맥 중 입을 여는 컷 0건. S6·S7·S8 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **왕 이환(plan 지정 — 병상 앵커)**: the young King Ihwan — a 30-year-old Joseon king lying unmoving on a raised wooden bed in the royal sickchamber, pale as paper, his brow knotted with pain even in the stillness, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain white inner robe, the coverlet drawn to his chest, lips closed. (**붉은 곤룡포·익선관 혼입 금지** — 침상 백의가 본화의 전부다. 시트 단계에서 수염 기복 2회 발생해 시트 정정 완료 — 원장 가드로 실사 단계 이중 차단.)
   - **어의(plan 지정 — 내의원 앵커)**: the old court physician — a 60-year-old Joseon court physician of the royal infirmary in dark physician's official robes and a black horsehair official hat, calm unhurried hands, the composed cold manner of a man delivering a finding he made his mind up long ago, lips closed. (**신규 조연** — characters.md 조연 보이스 원장에 등록: Neural2-C −1.5, 0.9.)
   - **이설화(plan 지정 — 궁녀 앵커)**: the woman Seolhwa — a 21-year-old Korean noblewoman serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, her cool clerkly eyes reading facts without flinching, lips closed. (EP51 한양 궁궐 궁녀 앵커 계승 + **옥통** 추가 — 여행 복식·두건 망토 혼입 금지.)
   - **익위사 무관(plan 지정 — 보위 앵커)**: a royal guard officer (ikwisa) — a broad-shouldered Joseon military officer in a dark blue and black military uniform and black horsehair war hat, standing rigid at his post, one weathered hand gripping the scabbard of the sheathed sword at his hip, a guarding stance, a disciplined weathered face, lips closed. (**칼 뽑는 컷 0건** — 칼집째가 본화의 조건이다.)
   - **중전 윤씨·강무결·윤경헌 본화 미등장** — 앵커 미기재(대사·내레이션에서만 지칭).
9. **광원 표기(정본 AG ① — 이중 광원)**: 병상 썬(S1·S2·S4·S7·S8) — **달빛 창살광 + 머리맡 약불 이중 광원**(the pale bars of moonlight through the lattice window + the small low glow of the medicine brazier at the head of the bed, two light sources in one room). S3·S5 — 안방 화로의 the steady brazier light on the lacquer, the night dark beyond the paper doors. S6 — 복도 양 끝의 two pools of lamplight and the dark stretch between. 약불 가드 — `the brazier burns steady and low, never flickering like horror, never strobing` + `no crushed blacks, no milky flat darkness` 전 썬 상설.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 암전 이후의 붉은 타이틀(제53화 「섭정의 상소」에서 계속)은 **편집 단계에서 삽입**. S8 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S4 2구. 어의 `ko-KR-Neural2-C` (**Pitch −1.5**, Speed 0.9, **신규 조연 등록** — 이환과 동일 ID나 본화 이환 발화 0건, 중후하고 차가운 진단 톤으로 구분) — S2 1구. 설화 `ko-KR-Neural2-A` (Pitch −1.0, Speed 1.0, 차분하고 서늘한 결의의 톤 — characters.md 고정 등록치) — S3·S5 2구(궁중어 나이다체 그대로). 이환 `ko-KR-Neural2-C` 등록치 보유하나 **본화 발화 0건**(혼수 썬) — 배정 제외. 본화 대사 5구 + 엔드카드 자막 1건. S6·S7(무대사)·S8 — 배정 없음. 중전·강무결·윤경헌·익위사 발화 없음 — 배정 제외.
13. **동일 보이스 ID 점검(§0-13) — 불발동**: Wavenet 계열은 내레이션 단독 1배역 — 동일 ID 공존 0건, 별도 세션 장치 불요(EP51 내레이션+흑영대 2중과 다름). Neural2-C는 어의·이환이 공유하나 이환 무발화 — 실질 충돌 없음. 파일명 분리: `EP52_S1_NARRATION`·`EP52_S4_NARRATION`·`EP52_S2_UUI`(어의)·`EP52_S3_SEOLHWA`·`EP52_S5_SEOLHWA`. 피치 사다리: 내레이션 0.0 > 설화 −1.0 > 어의 −1.5.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 3/3/4/4/4/3/4/3 = 28컷 — EP19~EP51 32종 배분 전수 대조 미중복(생성기 `validate()` `DISTRIBUTION not in PRIOR` 단정 통과). S4 두 개의 문 4컷·S3 상소 4컷·S5 옥통 기록 4컷·S7 눈썹 4비트가 서사 호흡의 기둥, S1·S2·S6·S8은 3컷 정적 호흡.

---

## 1. S01 사흘 밤낮, 깨어나지 못함 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP52_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm 슬로우 팬 — 병상, 사흘째 눈을 뜨지 못하는 왕. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] \\\\"이환은 사흘 밤낮으로 — 잠에서 깨어나지 못했다.\\\\" (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **오프닝 썬(가변 3컷)** — 병상 전경, 이중 광원(1컷) → 슬로우 팬이 침상을 가로지르며 창백한 얼굴(2컷) → 겹쳐놓은 손과 약그릇의 가는 김(3컷). 의사 해설 0건 — 나레이션 한 문장이 전부다. **병상 축은 EP43 서재 구도의 좌우 반전**(AG ①).

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night, one person only: the young King Ihwan — a 30-year-old Joseon king lying unmoving on a raised wooden bed, pale as paper, his brow knotted with pain even in the stillness, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain white inner robe, the coverlet drawn to his chest, his breath barely lifting the coverlet, lips closed. He does not wake. No other person in the scene. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier at the head of the bed. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness. The bed axis runs as the mirrored counterpart of the EP43 chamber composition.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm, slow pan left to right: wide of the royal sickchamber — the king unmoving on the raised bed, moonlight in bars through the lattice window, the brazier glowing at the head of the bed.
2. 50mm, slow pan continued: crossing the bed — the king's pale face, eyes closed, the brow faintly knotted.
3. 50mm, static: his folded hands on the coverlet and the medicine bowl beside the bed, the steam rising thin from it.

CHAMBER MOTION — IMPORTANT: physically-based the slow pan across the bed, the breath barely lifting the coverlet, the thin steam rising from the medicine bowl — the king does not wake and nothing is explained; the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 어의의 두 마디 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP52_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 어의가 판단을 내놓는다. [중후한 진단 · 어의/`ko-KR-Neural2-C`, Pitch −1.5, Speed 0.9 — 신규 조연 등록] \\\\"독은 이미 몸에 있었소. 약이 아니라 — 몸이 기억하고 있던 것이오.\\\\" (rel 4.0=절대 9.5, 사후 믹싱)
- **연출 특이**: **진단 썬(가변 3컷)** — 진맥(1컷) → 고개를 드는 어의의 차갑고 담담한 전달(2컷) → 약그릇으로 옮겨가는 시선(3컷, **처방은 이미 끝났다는 시선**). 의학 강의·병세 해설 모놀로그 0건 — 진단은 정확히 두 문장이며 보이스오버다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night, two people: the old court physician — a 60-year-old Joseon court physician of the royal infirmary in dark physician's official robes and a black horsehair official hat, calm unhurried hands, the composed cold manner of a man delivering a finding he made his mind up long ago — kneeling at the bedside, two fingers resting on the wrist of the patient; and the patient, the young King Ihwan — a 30-year-old Joseon king lying unmoving on the raised wooden bed, pale as paper, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, in a plain white inner robe, lips closed. The diagnosis is delivered as voiceover only — the physician's lips stay closed, no medical lecture, no explanation monologue. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier at the head of the bed, its thin steam rising between the two men. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness. The bed axis runs as the mirrored counterpart of the EP43 chamber composition.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the old court physician kneeling at the bedside, two fingers on the young king's wrist, taking a pulse that barely answers.
2. 85mm close, static: the physician lifting his head — the calm, cold delivery of a finding already decided.
3. 85mm close, static: his eyes moving past the young king's smooth beardless face to the medicine bowl beside the bed, the thin steam rising between them.

DIAGNOSIS MOTION — IMPORTANT: physically-based the two fingers resting on the wrist, the head lifting slowly, the steam rising between them — the finding is exactly two sentences and nothing more, carried only as voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 상소 — 반 시간 뒤의 시각 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP52_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 의정부의 상소, 왕이 의식을 잃은 지 반 시간 뒤의 시각. [서늘한 발견 · 설화/`ko-KR-Neural2-A`, Pitch −1.0, Speed 1.0] \\\\"중전 마마는 폐하가 눈을 감기 전부터 — 눈을 감길 준비를 해 두셨군요.\\\\" (rel 5.0=절대 17.5, 사후 믹싱)
- **연출 특이**: **상소 썬(가변 4컷)** — 상소를 내려놓는 궁녀의 손(1컷) → 펼쳐진 상소(2컷, **백지 설계 교칙 — 가독 글자 0건**, 획선과 먹 자국만) → 획선을 훑는 설화의 서늘한 눈(3컷) → 반쯤 그늘진 얼굴에 도착하는 결론(4컷, **중전은 왕이 눈을 감기 전에 준비했다**). 놀람·전율 0건 — 차갑고 정적인 사관의 독해.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a low lacquer table in the queen's antechamber of a Joseon palace at night: the woman Seolhwa — a 21-year-old Korean noblewoman serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, her cool clerkly eyes reading facts without flinching — her hand laying down a folded state memorial paper and scanning its lines, her face half in shadow as the cold conclusion arrives: the Queen had made her preparations before the king's eyes closed. No shock, no gasp. She is alone in the room. The memorial paper carries NO legible letters anywhere — only ruled lines and inked marks, never rows of glyphs, no legible hangul, no legible hanja, no readable script of any kind. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: one steady brazier light on the lacquer table, the rest of the room falling into soft darkness, the night pressing at the paper doors beyond — the brazier is the only light. It burns steady, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: a court lady's hand laying a folded state memorial paper on the low lacquer table.
2. 100mm macro, static: the memorial unfolded under the light — ruled lines of ink and bare paper below, no legible writing anywhere.
3. 100mm macro, static: her cold eyes scanning the ruled lines — the reading that finds what sits between the lines.
4. 100mm macro, static: her face half in shadow — the cold conclusion arriving in her eyes.

MEMORIAL MOTION — IMPORTANT: physically-based the paper's weight under the hand, the ruled lines under the light, the still air of the antechamber — the discovery is cold and still, no gasps, no shock pose; the line is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 두 개의 문 (절대 22.5~30.0 · 콘티 4컷)

- **시트**: `downloads/EP52_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm — 병상 좌우에 선 익위사의 칼과 궁녀의 은장도. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] \\\\"궐은 두 개의 문으로 갈라졌다 — 하나는 중전의 문이요, 하나는 왕의 문이었다.\\\\" (rel 4.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **분열 압축 썬(가변 4컷, 정본 안티슬롭 ②의 치환체)** — 좌우 대칭 와이드(1컷, 왕은 침상 중앙의 작은 점) → 왼손의 칼집(2컷, **칼집째, 손은 칼집만**) → 은장도의 광택(3컷, **차고만 있는 장식, 손은 접힌 채**) → 한 프레임의 두 문(4컷, 왕을 사이에 둔 두 개의 침묵). 설명 나레이션 난립 0건 — 이 시각 대비 하나가 궁의 분열 전부다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the royal sickchamber of a Joseon palace at night seen down its axis, three people, at most three figures per panel, no crowd: the young King Ihwan — a 30-year-old Joseon king, pale as paper, clean-shaven with a completely smooth young face, no beard and no stubble, in a plain white inner robe — small and unmoving on the raised bed between two doors; at the left door a royal guard officer (ikwisa) — a broad-shouldered Joseon military officer in a dark blue and black military uniform and black horsehair war hat, standing rigid, one weathered hand gripping the scabbard of the sheathed sword at his hip, a guarding stance, no blade drawn anywhere; at the right door a court lady standing still — an elegant dark pastel court-lady hanbok, neat traditional hair with a single jade hairpin — with a small ornamental silver dagger worn sheathed at her skirt band, her hands folded quietly before her, never reaching for it. Neither door looks at the other. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the pale bars of moonlight through the lattice window, and the small low glow of the medicine brazier at the head of the bed between the two doors. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness. The bed axis runs as the mirrored counterpart of the EP43 chamber composition.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm symmetric wide, static: the sickchamber down its axis — the guard officer at the left door, the court lady at the right door, the king small on the bed between them.
2. 35mm close, static: the guard officer's weathered hand closed on the scabbard at his hip, the sword sheathed and still.
3. 35mm close, static: the small ornamental silver dagger worn sheathed at the court lady's skirt band, its sheen caught by the light, her hands folded before her.
4. 35mm wide, static: both doors held in one frame — the two silences facing each other across the sleeping king.

DOORS MOTION — IMPORTANT: physically-based the guard's hand resting on the scabbard, the lady's folded hands, neither door moving — the palace splits into two doors and this visual contrast is the whole statement, no crowd, no explanation, at most three figures per panel; the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 소녀만의 종이 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP52_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro — 기록, 비녀의 옥통이 담을 수 있는 크기의 종이. [서늘한 준비 · 설화/`ko-KR-Neural2-A`, Pitch −1.0, Speed 1.0] \\\\"이 말은 — 소녀만의 종이에 담겠나이다.\\\\" (rel 3.0=절대 32.0, 사후 믹싱)
- **연출 특이**: **갈무리 썬(가변 4컷)** — 옥통 크기로 고른 종이(1컷) → 비녀 머리에서 꺼낸 옥통(2컷) → 붓끝의 짧은 획(3컷, **백지 설계 교칙 — 가독 글자 0건**) → 돌돌 말아 옥통에 넣고 비녀를 되짚어 끼움(4컷, **기록은 비녀 안으로 방을 나간다**).

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a low lacquer table in the queen's antechamber of a Joseon palace at night, one person only, seen in macro: the woman Seolhwa — a 21-year-old Korean noblewoman serving as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court-lady hanbok with clean embroidery, neat traditional hair tied with a single simple jade hairpin (binyeo) with a slim jade tube (oktong) fitted at its head and no other ornament, her cool clerkly eyes reading facts without flinching — her hands smoothing a small slip of paper exactly the size the jade tube can hold, drawing the tube from the head of the hairpin, making short ink strokes on the slip with a brush tip, rolling the slip tight and sliding it into the tube, the hairpin reassembled between her fingers. She is alone in the room. The slip carries NO legible letters anywhere — only ink strokes and marks, never rows of glyphs, no legible hangul, no legible hanja, no readable script of any kind. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: one steady brazier light on the lacquer table, the rest of the room falling into soft darkness, the night pressing at the paper doors beyond — the brazier is the only light. It burns steady, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: her hands smoothing a small slip of paper on the lacquer table — the size that could hide inside a hairpin's jade tube.
2. 100mm macro, static: the slim jade tube drawn from the head of the jade hairpin, lying open on the table.
3. 100mm macro, static: the brush tip drawing short ink strokes on the slip — strokes and marks only, no legible letters.
4. 100mm macro, static: the slip rolled tight and slid into the jade tube, the hairpin reassembled between her fingers.

RECORD MOTION — IMPORTANT: physically-based the slip smoothed flat, the jade tube drawn from the hairpin, the slip rolled tight and slid inside — the paper is exactly the size the tube can hold and the record leaves the room inside a hairpin, no legible letters anywhere, strokes only; the line is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 두 문 사이의 복도 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP52_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 — 밤의 궐, 두 문 사이의 복도. **무대사** — 렌더 전면 무음.
- **연출 특이**: **은유 썬(가변 3컷)** — 서리 맺힌 텅 빈 복도(1컷) → 복도 길 방향의 두 등불과 그 사이의 어둠(2컷) → 상부 하이 와이드, 두 등불 웅덩이 사이의 어두운 판(3컷, **사이의 어둠이 본화의 지도다**). 인물 0건 — 복도 자체가 은유다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the long wooden corridor of a Joseon palace at night, no person in any frame: frost holding on the boards, one lantern at the far end; the corridor seen lengthwise with a lit doorway at either end and the dark stretch of boards between the two lights; then a high wide view from above, the corridor running between the two pools of lamplight, the dark between them. No person, no animal anywhere. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two pools of lamplight at the corridor's ends and the dark stretch between them — the lanterns are the only sources. They burn steady, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the long wooden corridor at night, empty, frost on the boards, one lantern at the far end.
2. 24mm wide, static: seen lengthwise — two lit doorways at either end, the dark stretch of boards between.
3. 24mm high wide, static: from above, the corridor between the two pools of lamplight, no person anywhere.

CORRIDOR MOTION — IMPORTANT: physically-based the frost holding on the boards, the two pools of lamplight, the dark between them — the corridor itself is the statement and nothing moves in it, the render silent, no person in any frame. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 잠결마다 찌푸리는 눈썹 (절대 45.0~52.5 · 콘티 4컷)

- **시트**: `downloads/EP52_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm — 잠결마다 찌푸리는 왕의 눈썹. **무대사** — 렌더 전면 무음.
- **연출 특이**: **4비트 썬(가변 4컷)** — 미간의 안정(1컷) → 첫 주름(2컷) → 고통이 미간을 조이고 턱에 힘이 들어감(3컷) → 다시 풀리는 호흡(4컷, **고통은 네 번 오고 네 번 눈썹 안에서만 산다**). 각성·신음·가슴 부여잡기 0건. 침축 축은 EP43 반전 구도(AG ①).

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a macro close study of the young King Ihwan asleep in the royal sickchamber at night, one person only: a 30-year-old Joseon king, pale as paper, clean-shaven with a completely smooth young face, no beard and no stubble anywhere, bare head with the hair loose on the pillow and no headband, in a plain white inner robe — his brow at rest, then knotting with pain, the crease pulling between the closed eyes, the jaw setting under it, then easing again as the breath returns, the eyes never opening. He does not wake, no gasp, no clutched chest — the pain lives only in the brow. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the faint lattice moonlight on one side of the pillow, and the brazier's small low glow warming the other. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness. The pillow axis runs as the mirrored counterpart of the EP43 chamber composition.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the brow at rest in the brazier's glow, lattice moonlight faint on the pillow.
2. 85mm close, static: the brow beginning to knot — the first crease between the closed eyes, the breath hitching once.
3. 85mm close, static: the knot deepening — the pain drawing the brow tight, the jaw set under it.
4. 85mm close, static: the knot easing again — the breath returning, the smooth beardless young face smoothing before the light, the eyes still closed.

BROW MOTION — IMPORTANT: physically-based the brow knotting and easing, the breath hitching and returning — four beats of pain that never wake the face, no gasp, no clutched chest; the render is silent and the pain lives only in the brow, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 약그릇의 김 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP52_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro → 엔드카드 — 약그릇 김이 가늘어짐 → 암전 → 타이틀. **렌더 무음** / 자막: 제53화 「섭정의 상소」에서 계속
- **연출 특이**: **폐관 썬(가변 3컷)** — 잠든 왕 곁의 약그릇, 가는 김(1컷) → 김이 더 가늘어지고 불빛이 죽으며 균일 암전(2컷) → 붉은 세로 타이틀(3컷, 편집 단계 전용 — 「제53화 섭정의 상소에서 계속」 13슬롯 단일 세로 열). 렌더는 **완전 암전으로 끝난다**.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a macro study of the medicine bowl beside the sleeping young King Ihwan in the royal sickchamber at night, the king only a pale sleeping presence at the frame edge — a 30-year-old Joseon king, clean-shaven with a completely smooth young face, no beard and no stubble, in a plain white inner robe, unmoving: the medicine bowl with its thin steam, the brazier glow low beneath it; then the steam growing thinner still, the glow dimming, the frame sinking evenly toward black, the lattice moonlight the last light to go. No other person, no animal. All characters are adults. No flashbacks, no memory scenes, no time transitions. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere. No violence, no blood, no wounds anywhere.

LIGHT GUARD — IMPORTANT: two light sources in one room — the faint lattice moonlight and the brazier's small low glow under the medicine bowl, and both of them go out as the frame sinks evenly into complete black. The brazier burns steady and low, never flickering like horror, never strobing. No crushed blacks, no milky flat darkness. The bed axis runs as the mirrored counterpart of the EP43 chamber composition.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the medicine bowl beside the sleeping king, the steam rising thin, the brazier glow low beneath it.
2. 100mm macro, static: the steam growing thinner still, the glow dimming — the frame sinking evenly toward black.
3. End card for the edit stage only — one vertical column of red Korean characters on black (the render itself must end in complete black; the title card is inserted in editing).

STEAM MOTION — IMPORTANT: physically-based the steam thinning above the bowl, the glow dimming, the whole frame sinking evenly into complete black — the medicine steams itself out and the render ends in complete black, no figure, no words, no readable marks in the end frame. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션 — S1 사흘 밤낮·S4 두 개의 문 2구 |
| 어의 | `ko-KR-Neural2-C` | **−1.5** (신규 조연 등록) | 0.9 | 중후하고 차가운 진단 — 이환과 동일 ID나 본화 이환 발화 0건, 톤 지문 구분. S2 1구 |
| 설화 | `ko-KR-Neural2-A` | −1.0 | 1.0 | 차분하고 서늘한 결의의 톤 — characters.md 고정 등록치. S3·S5 2구 — 궁중어(나이다체) 그대로 |
| 이환 | `ko-KR-Neural2-C` | −0.5 | 0.95 | 등록치 보유하나 **본화 발화 0건**(혼수 썬) — 배정 제외 |

본화 대사 5구(내레이션 2·어의 1·설화 2) + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사 사후 믹싱. 발화 5구 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S6·S7(무대사)·S8 — 렌더 전면 무음. 중전·강무결·윤경헌·익위사 본화 발화 없음 — 배정 제외.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:04,500
이환은 사흘 밤낮으로 — 잠에서 깨어나지 못했다.

2
00:00:09,500 --> 00:00:13,000
독은 이미 몸에 있었소. 약이 아니라 — 몸이 기억하고 있던 것이오.

3
00:00:17,500 --> 00:00:21,300
중전 마마는 폐하가 눈을 감기 전부터 — 눈을 감길 준비를 해 두셨군요.

4
00:00:24,500 --> 00:00:28,300
궐은 두 개의 문으로 갈라졌다 — 하나는 중전의 문이요, 하나는 왕의 문이었다.

5
00:00:32,000 --> 00:00:34,000
이 말은 — 소녀만의 종이에 담겠나이다.

6
00:00:58,800 --> 00:00:59,800
제53화 「섭정의 상소」에서 계속
```

- 시작 시각은 정본 rel 수치(3.0→2.0 / 4.0→9.5 / 5.0→17.5 / 4.5→24.5 / 3.0→32.0)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S6·S7은 무대사 — SRT 미기재.
- 6번 자막(58.8~59.8)은 암전 이후 삽입 — S8 렌더는 완전 암전으로 끝난다.
- TTS 트랙 파일명: 내레이션 `EP52_S1_NARRATION`·`EP52_S4_NARRATION`, 어의 `EP52_S2_UUI`, 설화 `EP52_S3_SEOLHWA`·`EP52_S5_SEOLHWA`. **동일 ID 공존 0건(Wavenet-C 단독 1배역)** — §0-13 장치 불발동. 피치 사다리: 내레이션 0.0 > 설화 −1.0 > 어의 −1.5.

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP52_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP52_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep52_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원, 세이프 어휘 validate() 내장) |
| 검수 기록 | `projects/sageuk-revenge/EP52_QC_CHECKLIST.md` |
