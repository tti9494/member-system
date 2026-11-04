# 「혈화의 궐」 EP39 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제39화 「종이의 먹 냄새」 8썬표(`master_screenplay/SEASON_02_MASTER_SCREENPLAY.md` 행 258~270, 원전: 제39장 정본) + `characters.md` 캐릭터 앵커(설화·이환 주연 고정 프롬프트) + EP20~EP38 원장 템플릿(동일 규격)
> **범위**: EP39 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 종이의 먹 냄새**: 야간 집무실 단일 공간(옥사 회상 편집 금지 — EP35 규격 계승, `no flashbacks, no memory scenes, no time transitions`). **탐정식 반전 고함 배제(정본 안티슬롭)** → "그렇다면 진범은!" 류의 고함·지목 편집 전면 금지, 치환 [설화의 세 가지 질문(S3) — 차분하고 절제된 폭로, `no rising voice, no pointing, no accusation` 상설]. **왕의 분노 폭발 슬롭 배제(정본 안티슬롭)** → 태움 선언(S4)은 고함·집기 투척이 아니라 **촛대를 한 뼘 끌어당기는 한 동작**, 거절(S5)은 **펼쳐진 종이 모서리를 손끝으로 눌러 다시 펴는 설화의 손** — 분노 대신 촛불이 기운다(`no outburst, no thrown object, no rage`). **두 종이 비교 매크로(정본 AG ①)** → 탁자 위 두 밀서를 **나란히 놓는 구도 필수**(S1 1컷·S6 1컷 — `side by side, edges parallel` 상설). **후각의 시각 치환(정본 AG ①)** → 먹 냄새는 화면 불가 — **습기 얼룩·번짐·섬유 팽창의 시각 차이**(S1 3컷·S2 1~2컷)로 치환. **캐릭터 앵커(plan 지정)**: 설화 — 궁녀 복식, **옥비녀 단일 로드**, 태움 대신 펼침을 권하는 서늘한 지략 / 이환 — 붉은 곤룡포·익선관(plan 허용 항목 중 집무실 식별성 보존 선택), 억누른 분노와 침묵의 군주. **문자 가드**: 밀서 필적은 `worn, faded, soft-edged ink strokes that never resolve into readable character shapes`(EP35 통과 규격), 낙관은 `pressed square seal impression, its carved pattern soft and indistinct`, 병풍·표두 서화는 `faint abstract ink brush strokes, no readable characters`. **세이프티 가드**: 본화는 유혈·흉기 트리거 원천 부재 — 화염은 **촛불 하나와 종이 모서리의 열변형**까지만(`no open flame touching the paper, nothing catching fire` 상설), `no blood, no wounds, no injuries anywhere` 전 썬 상설. **동일 보이스 ID 다중 배역 없음**: 본화 보이스는 내레이션(`Wavenet-C`)·설화(`Neural2-A`)·이환(`Neural2-C`) 3인 3색 — 동일 ID 3중 배역 차단 장치(§0-13)는 본화 불적용. **킬러 컷 미배정**: EP39은 특수 훅 허용 화(EP30·EP41·EP49·EP50)가 아님 — 초슬로우 훅 재투입 없음.

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` (촛불 온광 / 창밖 야기 냉광 교차) | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **두 종이의 나란함**(the lamp flame steadying, the papers lying flat under the raking light, the lamp's small shadow crossing the seal impressions), S02 **습기 자국의 물리**(the dried ring's cockled edge, the raised fibres of the old paper, nothing moving but the flame), S03 **질문의 절제**(the folded hands steady, the candle burning between them, the papers unmoving on the desk), S04 **촛대의 한 뼘**(the candle stand sliding its one handspan, the flame leaning as it moves, the paper's corner curling from the heat), S05 **손끝의 반전**(the corner easing flat under her fingertips, the sheet sliding back across the wood, the flame left leaning over empty wood), S06 **펼침의 마무리**(the palm smoothing the sheet, the crease's shadow softening, the flame steady), S07 **밤의 깊어짐**(the cold night air at the lattice, the candle burning shorter, the two figures still), S08 **등불의 혼자 남음**(the lamp burning alone, the paperweight's shadow long on the wood, the flame sinking low).
5. **세이프 필터(본화 최우선 가드)**: 유혈·흉기·상처 트리거 원천 부재. `no blood, no wounds, no injuries anywhere` 전 썬 상설. 화염은 촛불·등불의 단일 소염까지만 — 종이 연소·화염 확산 없음(`no open flame touching the paper, nothing catching fire`). 전 등장 인물 성인 — `all characters are adults`.
6. **문자 가드**: 화면 노출 문자 요소 일체 금지 — `no readable letters, no characters, no labels anywhere` 상설. 밀서 필적은 **바랜 붓 획 질감**으로만(`never resolving into readable character shapes`), 낙관 인영은 **무늬 있는 도장 자국**으로만(`its carved pattern soft and indistinct`). 병풍·표두 서화·벽걸이 현판은 `faint abstract ink brush strokes, no readable characters` 지정 — 현판·액자에 글자를 새기지 않는다(EP38 S03 팻말 결함 이력 계승). 엔드카드 자막(제40화 「중전의 저울」에서 계속)은 편집 단계 삽입.
7. **입모양 배제 가드(100화 전편 규격)**: 설화 발화 3구(S2 속마음·S3 질문·S5 거절)·이환 1구(S4 선언)·내레이션 1구(S1)은 전부 무음 렌더 + 사후 믹싱 — 화면은 **입모양 배제**, `lips closed throughout` 전 썬 상설. 발화 썬은 보이스오버·리액션 샷으로 처리. S6·S7·S8 무대사 — 렌더 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **설화(plan 지정 — 옥비녀 단일 로드)**: a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure, her certainty cool and her resolve hidden entirely.
   - **이환(plan 지정 — 곤룡포 앵커 유지)**: a 24-year-old Joseon king, youthful and clean-shaven, no beard, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing. (EP38 S07 중년 수염 드리프트 결함 이력 — `clean-shaven, no beard` 인라인 상설)
9. **광원 표기**: 시즌2 색 설계 — **집무실 촛불·등불 온광과 창밖 야기 냉광의 교차**가 본화 유일의 광원 축(전 썬 야간 동일 공간). S1~S6 탁자 등불·촛불 온광(그을린 창호지 너머 냉광), S7 창가 냉광 우세(밤이 깊어감 — 촛불 짧아짐), S8 소등 직전의 잔광. 전부 `no crushed blacks, no milky flat darkness` — 광원 소스 명시로 완전 암부 슬롭 차단.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S08 암전 이후의 붉은 타이틀(제40화 「중전의 저울」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9) — S1 1구. **설화** `ko-KR-Neural2-A` (Pitch -1.0, Speed 1.0, 차분하고 서늘한 결의의 톤) — S2·S3·S5 3구. **이환** `ko-KR-Neural2-C` (Pitch -0.5, Speed 0.95, 단단하고 기품 있는 어조) — S4 1구. 무결(Wavenet-C)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. 동일 보이스 ID 다중 배역 없음 — §0-13 장치 불적용(단, 3인 3색 트랙은 파일명 규칙으로 분리 관리 — §9).
13. **동일 보이스 ID 다중 배역 차단 — 본화 불적용 확인**: 본화 발화 3인의 보이스 ID는 전부 상이(Wavenet-C / Neural2-A / Neural2-C) — EP37·EP38의 피치 사다리 장치가 필요한 동일 ID 공존이 없다. 다만 동일 ID 혼동 방지 규정 자체는 유지 — 향후 무결 재등장 화(EP40 이후)에서 Wavenet-C 다중 배역이 재현되면 §0-13 4중 장치를 재가동한다.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/3/5/3/4/3/3/3 = 28컷 — EP19(4/3/3/3/4/3/4/4)·EP20(4/3/4/3/3/4/3/4)·EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)·EP26(3/4/3/4/3/4/3/4)·EP27(4/4/3/4/3/3/4/3)·EP28(4/4/3/3/4/4/3/3)·EP29(3/4/3/3/4/3/4/4)·EP30(4/3/4/4/3/3/4/3)·EP31(4/3/3/4/4/3/3/4)·EP32(3/4/3/4/4/3/4/3)·EP33(4/3/4/3/3/4/3/4)·EP34(3/4/4/2/3/3/4/5)·EP35(4/3/4/2/3/4/3/5)·EP36(3/4/4/3/3/3/4/4)·EP37(4/3/5/4/3/3/3/3)·EP38(4/3/5/4/3/4/2/3) 어느 배분과도 다른 신규 배분. S3 세 가지 질문 씬에 5컷 최대 배분(대화 템포 가변 원칙 — 대치 50mm → 설화 측면 → 왕 클로즈 → 설화 클로즈 → 침묵 와이드), S4 태움 선언 3컷(선언 클로즈 → 촛대 한 뼘 → 모서리 열변형 — 동작의 단계를 3컷으로 압축), S5 거절 4컷(설화 클로즈 → 손끝 매크로 → 종이 복귀 → 왕 클로즈 — 반전을 손으로 운반), S2·S6·S7·S8 3컷 정적 호흡.

---

## 1. S01 두 밀서 — 낙관은 같고 먹이 다름 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP39_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 나란히 놓인 종이, 두 장의 밀서 — 낙관은 같고 먹이 다름. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "두 종이의 낙관은 같았다. 그러나 — 먹이 달랐다." (rel 3.5=절대 2.0, 사후 믹싱)
- **연출 특이**: **비교 매크로 오프닝 썬(AG ① — 나란히 놓는 구도 필수)** — 두 밀서를 한 화면에 나란히 놓는 하이앵글 매크로(1컷) → 낙관 인영 2종 나란히(2컷) → 두 먹의 번짐 차이 85mm(3컷) → 탁자에 선 설화 50mm(4컷). 후각(먹 냄새)은 화면 불가 — **십 년 전 종이의 습기 자국·번짐**으로 치환. 매크로 연타 방지(AG ①) — 매크로 2컷 → 85mm → 50mm 스케일 이탈. 내레이션은 보이스오버 — `lips closed` 엄수.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure standing, seen whole or from behind, no face held: the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure. The two opened secret letters on the dark desk show only worn, faded, soft-edged ink strokes that never resolve into readable character shapes, and each carries a pressed square seal impression with the same soft indistinct carved pattern. No flashbacks, no memory scenes, no time transitions, only the present office and the papers on the desk. No blood, no wounds, no injuries anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: one warm oil lamp raking low across the two sheets against the cold blue night beyond the paper lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, high angle, static: two opened letters laid side by side on the dark desk, edges parallel, one lamp raking across both.
2. 100mm macro, static: the two pressed square seal impressions side by side, the same indistinct carved pattern twice, never resolving into a readable character.
3. 85mm close, static: the two inks compared across both sheets — one flat and clean, one bloomed out with a grainy soaked halo into the paper fibres, the raking lamplight crossing both.
4. 50mm medium, static: the court lady standing over the desk, both letters laid out before her, her hands folded still.

COMPARISON MOTION — IMPORTANT: physically-based the lamp flame steadying, the papers lying flat under the raking light, the lamp's small shadow crossing the seal impressions — the whole proof is two sheets lying side by side and the ink that dried differently, no detective pointing, no rising voice, the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 십 년 전 먹의 습기 자국 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP39_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 먹 얼룩, 십 년 전 먹의 습기 자국. [서늘한 확신 속마음 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "윤경헌은 옥사 안에서 이것을 쓰지 않았나이다." (rel 3.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **후각 치환의 핵심 썬(AG ①)** — "먹 냄새가 다르다"는 화면 불가 정보를 **말라붙은 습기 자국(조수 표식)**의 물성으로 완전히 시각화한다. 습기 자국 매크로(1컷) → 섬유 팽창·쭈글어진 테두리(2컷) → 자국을 내려다보는 설화 클로즈(3컷). 결론 대사(속마음)는 보이스오버 — `lips closed` 엄수. 매크로 2컷 → 85mm 이탈.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one near figure: the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), her certainty cool and her resolve hidden entirely — looking down at the stain on the old sheet. The old letter's paper shows a dried ringed tide-mark left by ink and water long ago, and its writing is only worn, faded, soft-edged ink strokes that never resolve into readable character shapes. No flashbacks, no memory scenes, no time transitions, only the present office and the paper on the desk. No blood, no wounds, no injuries anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm oil lamp on the stain against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the old sheet's dried tide-mark — a ringed bloom where damp once dried, ten years old, its edge gently cockled.
2. 100mm macro, static: the paper fibres at the stain's edge — swollen, raised, hair-fine cracks tracing the ring, the ink pushed dark against it.
3. 85mm close, static: the court lady's lowered face half-lit by the lamp, her eyes on the stain, the certainty carried by voiceover only, lips closed.

STAIN MOTION — IMPORTANT: physically-based the dried ring's cockled edge, the raised fibres of the old paper, nothing moving but the flame — the smell of the ink cannot be filmed, so the dried ring and the bloomed edge carry it, no melodrama, her certainty is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 설화가 왕에게 세 가지를 묻는다 (절대 15.0~22.5 · 콘티 5컷)

- **시트**: `downloads/EP39_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 질문, 설화가 왕에게 세 가지를 묻는다. [차가운 질문 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "첫째 — 밀서를 심은 자를 아시나이다. 둘째 — 그 자는 지금 어디에. 셋째 — 그 밀서가 심어진 후, 누가 그것을 '발견'하기 쉽게 만들었나이다." (rel 6.0=절대 17.5, 사후 믹싱)
- **연출 특이**: **본화의 서사적 중심 썬(최대 5컷 배분)** — 정본 안티슬롭의 직결 지점. 탐정식 반전 고함("그렇다면 진범은!")을 전면 배제하고, 세 가지 질문은 **차갑고 평탄한 목소리의 절제된 폭로**로 운반된다. 대치 50mm(1컷) → 설화 측면, 소매 속 포개진 손(2컷) → 왕 클로즈(3컷) → 눈을 내리깐 설화 클로즈(4컷) → 침묵의 와이드(5컷). 질문 전문은 보이스오버 — `lips closed` 엄수, 립싱크 렌더 시도 금지.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure — standing before the desk, her hands folded inside her sleeves, the three questions carried by voiceover only. And the young King Ihwan — a 24-year-old Joseon king, youthful and clean-shaven, no beard, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes — seated at the desk, giving nothing back. Both adults. The two opened letters lie side by side between them on the dark desk, their writing only worn faded strokes that never resolve into readable characters. The hanging scroll and screens behind show only faint abstract ink brush strokes, no readable characters, no plaques, no inscriptions. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candle between them against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the court lady standing before the seated king, the two opened letters laid side by side between them on the dark desk.
2. 50mm medium, static: the court lady in three-quarter view, her hands folded inside her sleeves, chin level, lips closed.
3. 85mm close, static: the king's face in candle light, his jaw set, giving nothing back.
4. 85mm close, static: the court lady's face, her eyes lowered to the papers, the third question carried by voiceover only, lips closed.
5. 24mm wide, static: the night office from the door side, the king seated and the court lady standing across the desk, both still, one candle between them, the silence after three questions.

QUESTION MOTION — IMPORTANT: physically-based the folded hands steady, the candle burning between them, the papers unmoving on the desk — three questions asked flat and cold, no rising voice, no pointing, no accusation, the questions are voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 왕이 밀서를 태울 뜻을 내놓는다 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP39_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 왕이 밀서를 태울 뜻을 내놓는다. [억누른 분노 · 이환/`ko-KR-Neural2-C`, Pitch -0.5, Speed 0.95] "이 종이를 — 불태우겠다." (rel 2.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **분노 폭발 슬롭 배제의 직결 썬** — 선언은 고함이 아니라 **닫힌 입술 뒤의 한 문장**, 동작은 **촛대를 한 뼘 끌어당기는 측정된 하나**. 왕 클로즈(1컷) → 촛대 이동 50mm(2컷) → 모서리 열변형 매크로(3컷). 선언은 보이스오버 — `lips closed` 엄수. 화염은 종이에 닿지 않는다 — `no open flame touching the paper, nothing catching fire` (세이프티 가드).
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one figure only: the young King Ihwan — a 24-year-old Joseon king, youthful and clean-shaven, no beard, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing — his declaration held behind closed lips and carried by voiceover only. The sheet before him carries only worn, faded, soft-edged ink strokes that never resolve into readable characters. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candle flame at the frame edge against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the king's face in candle light, the declaration held behind closed lips, the candle flame at the frame edge, his eyes on the papers.
2. 50mm medium, static: his hand drawing a small brass candle stand one handspan across the desk toward the sheet, one slow measured movement, no sweeping gesture.
3. 100mm macro, static: the flame bending low toward the sheet's corner, the paper's corner curling and lifting from the heat, nothing catching fire.

DECLARATION MOTION — IMPORTANT: physically-based the candle stand sliding its one handspan, the flame leaning as it moves, the paper's corner curling from the heat — no rage, no thrown object, no outburst, the king's decision is one hand on one candle stand, the declaration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 거절 — 설화가 고개를 저음 (절대 30.0~37.5 · 콘티 4컷)

- **시트**: `downloads/EP39_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 거절, 설화가 고개를 저음. [서늘한 반전 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "태우지 마시옵소서, 폐하. 그자가 만든 덫은 — 그자의 종이로 뒤집을 수 있나이다." (rel 4.5=절대 32.0, 사후 믹싱)
- **연출 특이**: **행동으로 하는 거절 썬** — 거절 대사는 보이스오버로 운반되고, 화면은 **손끝이 반전을 실행한다**: 작은 고개 저음(1컷) → 말리는 모서리를 손끝으로 눌러 펴는 매크로(2컷) → 종이를 탁자 중앙으로 도로 끌어당김(3컷) → 손을 거두는 왕 클로즈(4컷). 소리 없는 손이 대사의 논리를 이긴다 — 정본 치환 지문 [태움 대신 펼침으로 답하는 설화] 그대로. `lips closed` 엄수.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), her refusal one small shake of the head and her hands doing the rest, the words carried by voiceover only. And the young King Ihwan — a 24-year-old Joseon king, youthful and clean-shaven, no beard, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan) — his hand withdrawing from the candle stand, no rage, the decision re-forming behind his eyes. Both adults. The sheet's writing is only worn faded strokes that never resolve into readable characters. No blood, no wounds, no injuries anywhere. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candle flame leaning over the empty wood against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the court lady's face in candle light, one small shake of the head, the refusal carried by voiceover only, lips closed.
2. 100mm macro, static: her fingertips pressing the curled corner of the sheet flat against the dark wood, the paper easing down under her fingers.
3. 50mm medium, static: her hand drawing the sheet back to the centre of the desk, away from the flame, the candle flame left leaning over the empty wood.
4. 85mm close, static: the king's face, his hand withdrawing, no rage, the decision re-forming behind his eyes.

REFUSAL MOTION — IMPORTANT: physically-based the corner easing flat under her fingertips, the sheet sliding back across the wood, the flame left leaning over empty wood — she does not raise her voice, she presses the corner flat and the flame loses its argument, the refusal is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 종이가 도로 펼쳐짐 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP39_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro, 종이가 도로 펼쳐짐. [무대사]
- **연출 특이**: **무대사 반전 완성 썬** — 정본 지정 100mm Macro 썬이지만 매크로 연타 방지(AG ①)로 나란히 놓임 하이앵글 매크로(1컷) → 접힘 테의 85mm 클로즈(2컷) → 손바닥으로 펼치는 50mm 미디엄(3컷) 스케일 이탈. 대사 0건 — 펼침의 손과 고정된 촛불만이 서사다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands and sleeve only in the near frame, no face: the court lady's hand — a 21-year-old court lady's pale hand, the embroidered cuff of a dark pastel court lady hanbok sleeve, her procedure methodical and unhurried. The two sheets on the dark desk show only worn, faded, soft-edged ink strokes that never resolve into readable character shapes, and one dried ringed tide-mark on the older sheet. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm steady candle beyond the frame against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, high angle, static: the two sheets laid side by side again on the dark desk, edges parallel, both corners flat, the older sheet's dried ring and the newer sheet's clean ink in one frame.
2. 85mm close, static: the older sheet's fold crease opened flat under the court lady's fingertips, the ink gathered dark along the crease line.
3. 50mm medium, static: her palm smoothing the sheet flat on the dark desk, the embroidered cuff at the frame edge, the candle flame steady in the soft focus beyond.

OPENING MOTION — IMPORTANT: physically-based the palm smoothing the sheet, the crease's shadow softening, the flame steady — the paper is opened again corner by corner, the reversal is done with palms and not fists, no dialogue, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 밤이 깊어감 — 왕과 설화가 각자 서 있음 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP39_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드, 밤이 깊어감 — 왕과 설화가 각자 서 있음. [무대사]
- **연출 특이**: **정적 와이드 썬** — 대사 0건, 두 사람의 거리가 서사다. 탁자를 사이에 둔 각자(1컷) → 창가 냉광 와이드(2커트) → 짧아진 촛불과 등의 미디엄(3컷). 시간의 경과는 **촛불의 길이**로만 계산된다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only, both still: the young King Ihwan — a 24-year-old Joseon king, youthful and clean-shaven, no beard, pale handsome features, a royal red dragon robe (gollyongpo) with a gold embroidered dragon emblem and a gold royal winged hat (ikseongwan), melancholy yet determined fiery eyes, stillness of a ruler who shows nothing. And the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure. They stand apart with the desk and the two sheets between them, neither looking at the other. Bare pillars and beams, no plaques, no inscriptions; the wall scroll shows only faint abstract ink brush strokes, no readable characters. No blood, no wounds, no injuries anywhere. All characters are adults. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the cold blue night through the paper lattice windows slowly winning the room against the one warm lamp burning low, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 24mm wide, static: the king's night office, the king and the court lady standing apart with the desk and the two sheets between them, the oil lamp burning low.
2. 24mm wide, static, from the window side: cold blue night beyond the paper lattice, two still figures and one lamp inside, the room large around them.
3. 35mm medium, static: the two figures in the room's depth, neither looking at the other, the candle burnt visibly shorter on the desk.

NIGHT MOTION — IMPORTANT: physically-based the cold night air at the lattice, the candle burning shorter, the two figures still — night deepens and nobody wins the room, the cold window light and the shortening candle measure the time, no dialogue, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 등불이 홀로 켜져 있음 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP39_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드, 등불이 홀로 켜져 있음 → 암전 → 타이틀. [무대사] / 자막: 제40화 「중전의 저울」에서 계속
- **연출 특이**: **EP40 훅 썬** — 빈 집무실의 잔등(1컷) → 암전(2컷) → 타이틀(3컷, 편집 단계). 사람이 모두 나가고 등불만 남는다 — 저울은 중궁전에서 다시 기운다. 무대사 — 렌더 무음. 렌더는 완전 암전으로 끝난다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures: the emptied night office, one small shallow brass oil lamp with a single wick and a low flame burning alone on the desk, no glass chimney, no lantern glass, the two sheets laid side by side weighted under a small brass paperweight, their writing only worn faded strokes that never resolve into readable characters. Bare pillars and beams, no plaques, no inscriptions. No blood anywhere. No speech. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the one warm lamp burning low against the cold blue night beyond the lattice windows, is the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the emptied night office, one oil lamp burning alone on the desk, the two sheets laid side by side weighted under a small brass paperweight.
2. the frame sinking into complete black, no text, held.
3. end card for the edit stage only — one vertical column of red Korean characters on black (the render must end in complete black; the title card is inserted in editing).

LAMP MOTION — IMPORTANT: physically-based the lamp burning alone, the paperweight's shadow long on the wood, the flame sinking low — the lamp is left burning for the next hand and the weight will fall in the queen's hall, the render ends in complete black, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션(S1) — "두 종이의 낙관은 같았다. 그러나 — 먹이 달랐다."를 운반하는 목소리 |
| 설화 | `ko-KR-Neural2-A` | -1.0 | 1.0 | 차분하고 서늘한 결의의 톤(S2 확신 속마음·S3 세 가지 질문·S5 거절 3구) — characters.md 고정 등록치 그대로 |
| 이환 | `ko-KR-Neural2-C` | -0.5 | 0.95 | 억누른 분노(S4) — "이 종이를 — 불태우겠다." 단단하고 기품 있는 어조, 고함 아닌 낮은 선언 |

본화 대사 4구(설화 3 + 이환 1) + 내레이션 1구 + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션 사후 믹싱. 발화 4구 전부 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S6·S7·S8 무대사 — 렌더 무음. 무결(Wavenet-C)·중전(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **동일 보이스 ID 다중 배역 없음** — 3인 3색(Wavenet-C/Neural2-A/Neural2-C), §0-13 피치 사다리 장치 불적용. **세이프티 가드 준수**: 본화는 유혈·흉기 트리거 원천 부재 — 화염은 촛불 열변형까지만.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:04,400
두 종이의 낙관은 같았다. 그러나 — 먹이 달랐다.

2
00:00:09,500 --> 00:00:11,900
윤경헌은 옥사 안에서 이것을 쓰지 않았나이다.

3
00:00:17,500 --> 00:00:21,600
첫째 — 밀서를 심은 자를 아시나이다. 둘째 — 그 자는 지금 어디에. 셋째 — 그 밀서가 심어진 후, 누가 그것을 '발견'하기 쉽게 만들었나이다.

4
00:00:24,500 --> 00:00:26,300
이 종이를 — 불태우겠다.

5
00:00:32,000 --> 00:00:35,200
태우지 마시옵소서, 폐하. 그자가 만든 덫은 — 그자의 종이로 뒤집을 수 있나이다.

6
00:00:58,000 --> 00:00:59,800
제40화 「중전의 저울」에서 계속
```

- 시작 시각은 정본 rel 수치(3.5→2.0 / 3.5→9.5 / 6.0→17.5 / 2.5→24.5 / 4.5→32.0)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S6·S7·S8(무대사)은 SRT 미기재.
- 6번 자막(58.0~59.8)은 암전 이후 삽입 — S08 렌더는 완전 암전으로 끝나고 타이틀은 편집 단계 참조.
- TTS 트랙 분리: 내레이션 1구(`EP39_S1_NARRATION`), 설화 3구(`EP39_S2_SEOLHWA`·`EP39_S3_SEOLHWA`·`EP39_S5_SEOLHWA`), 이환 1구(`EP39_S4_IHWAN`) — 보이스 ID 3인 3색이라 동일 ID 혼동은 없으나, 파일명 규칙으로 트랙을 분리 관리한다(EP38 §0-13 규격 계승).

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP39_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP39_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep39_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP39_QC_CHECKLIST.md` |
