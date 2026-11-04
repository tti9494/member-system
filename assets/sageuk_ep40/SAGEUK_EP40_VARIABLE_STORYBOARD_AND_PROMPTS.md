# 「혈화의 궐」 EP40 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제40화 「중전의 저울」 8썬표(`master_screenplay/SEASON_02_MASTER_SCREENPLAY.md` 행 270~290, 원전: 제40장 정본) + `characters.md` 캐릭터 앵커(설화 고정 프롬프트) + EP20~EP39 원장 템플릿(동일 규격)
> **범위**: EP40 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수 — 중전의 저울**: 중궁전 단일 공간(옥사 회상 편집 금지 — EP35 규격 계승, `no flashbacks, no memory scenes, no time transitions`). **여자 갈등 고양 극 배제(정본 안티슬롭)** → 눈물·고양·소리 높인 대치 전면 금지, 치환 [거울 속 시선의 전투] — 청동 거울의 어두운 반사와 침묵의 대치만(`no tears, no melodrama, no raised voice` 상설). **중전 자기 연민 독백 배제(정본 안티슬롭)** → "나는 이렇게 되었다" 류의 독백 컷 0건, 치환 [중전이 스스로 페이지를 넘기는 절제된 손동작만](S6). **거울 반사 구도(정본 AG ①⑥)** → 인물 이중 노출 슬롭 주의: 거울 속 얼굴은 **어두운 반사/실루엣 처리 상설**(`only a dim subdued reflection — dark, softened, silhouette-like, never a sharp second face, no double exposure, no duplicated figure`). **협박의 무기화 금지(세이프 가드)** → "협박"은 칼이 아니라 종이와 시선으로만 — 밀서를 탁자에 **내려놓는 제안의 손**(S5 3컷)으로 운반(`no weapons anywhere, no blood, no wounds, no injuries anywhere` 상설). **캐릭터 앵커(plan 지정)**: 중전 윤씨 — 당의, 화려한 가체와 떨잠, 차갑고 가식적인 온화, 거울 앞 30대 중전 / 설화 — 단아한 궁녀 복식, **옥비녀 단일 로드**, 거울 등 뒤에 선 서늘한 지략가. **문자 가드**: 설화가 꺼내는 밀서·장부 페이지는 `worn, faded, soft-edged ink strokes that never resolve into readable character shapes`(EP35 통과 규격), 병풍·액자는 `faint abstract ink brush strokes, no readable characters`, 현판·글씨체 액자 미기입(`no plaques, no inscriptions`). **세이프티 가드**: 본화는 유혈·흉기 트리거 원천 부재 — 촛불은 조명 소스로만(`nothing catching fire`), `no blood, no wounds, no injuries anywhere` 전 썬 상설. **동일 보이스 ID 다중 배역 없음**: 본화 보이스는 내레이션(`Wavenet-C`)·중전(`Neural2-B`)·설화(`Neural2-A`) 3인 3색 — 동일 ID 다중 배역 차단 장치(§0-13)는 본화 불적용(정본 AG 지문의 서 상궁은 8썬표 미등장). **킬러 컷 미배정**: EP40은 특수 훅 허용 화(EP30·EP41·EP49·EP50)가 아님 — 초슬로우 훅 재투입 없음(EP41이 킬러 컷 화).

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
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S01 **떨잠을 고르는 손과 어두운 반사**(the raised hand arranging the ornament, the flame breathing low, the reflection holding still), S02 **옻칠한 인사**(the shallow incline of the head, the folded hands, the smile worn like lacquer), S03 **종이의 꺼냄**(the paper drawn from the sleeve, the fold opening flat, the hands steady), S04 **멈춘 손의 물리**(the hand frozen a finger's width from the pendant, the pendant hanging utterly still, the flame breathing beyond), S05 **제안으로 내려놓는 손**(the paper laid gently down, the two hands apart, the gazes holding), S06 **스스로 넘기는 페이지**(the fingertip lifting the corner, the page turning in one measured gesture, the flame steady), S07 **닫힌 종이의 서명**(the closed sheet between the two at-rest hands, the candle burning lower, the two women still), S08 **어두워지는 거울**(the flame sinking low, the mirror's reflection dimming with it, the hall emptying into black).
5. **세이프 필터(본화 최우선 가드)**: 유혈·흉기·상처 트리거 원천 부재 — "협박"이 화면에 등장하는 유일한 형태는 종이와 시선이다. `no blood, no wounds, no injuries anywhere`, `no weapons anywhere` 전 썬 상설. 촛불은 조명 소스로만 — `nothing catching fire`. 전 등장 인물 성인 — `all characters are adults`.
6. **문자 가드**: 화면 노출 문자 요소 일체 금지 — `no readable letters, no characters, no labels anywhere` 상설. 밀서·장부 페이지 필적은 **바랜 붓 획 질감**으로만(`never resolving into readable character shapes`), 병풍·액자는 추상 수묵, 현판·글씨체 액자 금지(`no plaques, no inscriptions` — EP38 S03 팻말 결함 이력 계승). 엔드카드 자막(제41화 「후원의 죽숲」에서 계속)은 편집 단계 삽입.
7. **입모양 배제 가드(100화 전편 규격)**: 설화 발화 2구(S3 폭로·S5 구함)·중전 3구(S2 인사·S5 질문·S6 귀성)·내레이션 1구(S1)은 전부 무음 렌더 + 사후 믹싱 — 화면은 **입모양 배제**, `lips closed throughout` 전 썬 상설. 발화 썬은 보이스오버·리액션 샷으로 처리. S4·S7·S8 무대사 — 렌더 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **중전 윤씨(plan 지정 — 당의·가체·떨잠)**: a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam), the stillness of a woman who has measured everything.
   - **설화(plan 지정 — 옥비녀 단일 로드)**: a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure, her certainty cool and her resolve hidden entirely.
   - **거울 앵커(정본 AG ①⑥)**: a tall bronze mirror on a dark wooden stand, its polished surface holding only a dim subdued reflection — dark, softened, silhouette-like, never a sharp second face, no double exposure, no duplicated figure.
9. **광원 표기**: 시즌2 색 설계 — **중궁전 촛불 온광과 창밖 야기 냉광의 교차 + 청동 거울의 어두운 반사**가 본화 광원 축(전 썬 야간 동일 공간). S1~S3 화장대 촛불 온광(거울은 냉혹한 어둠), S4~S6 촛불과 거울 반사의 대비 심화, S7 촛불 짧아짐(시간 계산), S8 거울이 촛불과 함께 어두워짐. 전부 `no crushed blacks, no milky flat darkness` — 광원 소스 명시로 완전 암부 슬롭 차단.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S08 암전 이후의 붉은 타이틀(제41화 「후원의 죽숲」에서 계속)은 **편집 단계에서 삽입**. S08 렌더는 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용).
12. **보이스 모델 배정(시리즈 고정 — characters.md 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9) — S1 1구. **중전** `ko-KR-Neural2-B` (Pitch 0.0, Speed 1.0, 가식의 온화 → 억누른 위협 → 처음으로 내비치는 톤) — S2·S5·S6 3구. **설화** `ko-KR-Neural2-A` (Pitch -1.0, Speed 1.0, 차분하고 서늘한 결의의 톤) — S3·S5 2구. 이환(Neural2-C)·무결(Wavenet-C)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **동일 보이스 ID 다중 배역 없음** — §0-13 장치 불적용(정본 AG 지문의 "중전·서 상궁 동일 ID 구분"은 서 상궁이 8썬표 미등장이므로 발동 조건 부재 — 서 상궁 등장 화에서 재검토).
13. **동일 보이스 ID 다중 배역 차단 — 본화 불적용 확인**: 본화 발화 3인의 보이스 ID는 전부 상이(Wavenet-C / Neural2-B / Neural2-A) — EP37·EP38의 피치 사다리 장치가 필요한 동일 ID 공존이 없다. 다만 동일 ID 혼동 방지 규정 자체는 유지 — 서 상궁 등장 화에서 Wavenet-C 등 다중 배역이 재현되면 §0-13 4중 장치를 재가동한다.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 3/3/4/3/5/4/3/3 = 28컷 — EP19(4/3/3/3/4/3/4/4)·EP20(4/3/4/3/3/4/3/4)·EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)·EP26(3/4/3/4/3/4/3/4)·EP27(4/4/3/4/3/3/4/3)·EP28(4/4/3/3/4/4/3/3)·EP29(3/4/3/3/4/3/4/4)·EP30(4/3/4/4/3/3/4/3)·EP31(4/3/3/4/4/3/3/4)·EP32(3/4/3/4/4/3/4/3)·EP33(4/3/4/3/3/4/3/4)·EP34(3/4/4/2/3/3/4/5)·EP35(4/3/4/2/3/4/3/5)·EP36(3/4/4/3/3/3/4/4)·EP37(4/3/5/4/3/3/3/3)·EP38(4/3/5/4/3/4/2/3)·EP39(4/3/5/3/4/3/3/3) 어느 배분과도 다른 신규 배분. S5 협박 질문+구함 대사(본화 최장 대화)에 5컷 최대 배분(대화 템포 가변 원칙 — 질문 클로즈 → 설화 클로즈 → 종이 제안 매크로 → 시선의 전투 → 대치 미디엄), S6 중전이 스스로 페이지를 넘기는 손에 4컷(스스로의 손 → 페이지 전환 → 가면 유지 → 첫 정직한 시선), S3 직격 폭로에 4컷(꺼냄 → 펼침 매크로 → 설화 클로즈 → 거울 속 정지), S1·S2·S4·S7·S8 3컷 정적 호흡.

---

## 1. S01 거울 뒤 — 떨잠을 고르는 중전, 등 뒤로 설화 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP40_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 거울 뒤, 거울 앞에서 떨잠을 고르는 중전 — 등 뒤로 설화. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "중궁전의 문이 열린 것은 — 세 번째 문안에서였다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **오프닝 대치 썬** — 화장대 앞 중전과 등 뒤 몇 걸음 거리의 설화. 갈등 고양 없이 촛불·떨잠·어두운 거울 반사만으로 긴장을 세운다. 화장대 미디엄(1컷) → 거울 가장자리 너머 중전의 온상 클로즈(2컷) → 거울 속 어두운 실루엣(3컷). 내레이션은 보이스오버 — `lips closed` 엄수. 거울 반사는 **실루엣 전용**(이중 노출 슬롭 차단 상설).
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam), the stillness of a woman who has measured everything — seated at her dressing table before a tall bronze mirror on a dark wooden stand, its polished surface holding only a dim subdued reflection — dark, softened, silhouette-like, never a sharp second face, no double exposure, no duplicated figure. And behind her in the room's depth the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure. Plain bare pillars and beams, no plaques, no inscriptions; screens and frames show only faint abstract ink brush strokes, no readable characters. No flashbacks, no memory scenes, no time transitions, only the present hall. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candlelight on the dressing table against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the Queen seated before her bronze mirror arranging the dangling pendant ornament at her hair, the court lady standing a few paces behind her in the depth, still and waiting.
2. 85mm close, static: the Queen's composed face past the mirror's edge — a faint courteous smile that stops at the mouth, cool measuring eyes.
3. 85mm close, static: the bronze mirror's surface holding only a dim darkened silhouette of the seated Queen — softened, silhouette-like, no sharp second face, no double exposure.

MIRROR MOTION — IMPORTANT: physically-based the raised hand arranging the ornament, the flame breathing low, the reflection holding still — the duel is eyes and silence, no melodrama, no tears, no raised voice, the narration is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 중전의 가벼운 겉인사 (절대 07.5~15.0 · 콘티 3컷)

- **시트**: `downloads/EP40_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 중전의 가벼운 겉인사. [가식의 온화 · 중전/`ko-KR-Neural2-B`, Pitch 0.0, Speed 1.0] "홍화. 네가 요즘 대전의 약탕을 맡고 있다며. 수고가 이만저만이 아니겠구나." (rel 4.0=절대 9.5, 사후 믹싱)
- **연출 특이**: **옻칠된 인사 썬** — 친절이 잰다. 반쯤 돌아앉는 가벼운 인사(1컷) → 입가에서 멈추는 미소 클로즈(2컷) → 얕은 고개 숙임에도 움직이지 않는 설화의 눈(3컷). 환영 대사는 보이스오버 — `lips closed` 엄수, 미소가 눈에 닿지 않는 것이 화면의 전부다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam) — half-turning on her seat by the tall bronze mirror, its polished surface holding only a dim subdued reflection — dark, softened, silhouette-like, never a sharp second face, no double exposure, no duplicated figure. And the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), her composure unmoved by the welcome. Plain bare pillars and beams, no plaques, no inscriptions. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candlelight against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium, static: the Queen half-turning on her seat with a light courteous greeting, hands folded neatly in her lap, the mirror dark at the frame edge.
2. 85mm close, static: the Queen's gracious practiced smile in three-quarter view, lips closed, the warmth stopping at the mouth and never reaching the eyes.
3. 85mm close, static: the court lady's head inclining in a shallow formal bow, her eyes level and unmoved beneath it.

GREETING MOTION — IMPORTANT: physically-based the shallow incline of the head, the folded hands, the smile worn like lacquer — no tears, no raised voice, no melodrama, the welcome is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 설화가 조용히 꺼냄 — 직격 폭로 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP40_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm · 직격, 설화가 조용히 꺼냄. [서늘한 폭로 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "마마께서는 아버님을 밀고하신 분이지요. 그러나 아버님께서는 — 마마를 죽이는 밀서를 준비해 두셨나이다." (rel 5.5=절대 17.5, 사후 믹싱)
- **연출 특이**: **직격 폭로 썬(안티슬롭 직결)** — 폭로는 고양되지 않는다: 소매에서 접은 종이를 조용히 꺼냄(1컷) → 창백한 두 손 사이에서 펼쳐지는 매크로(2컷) → 수평의 눈, 평탄한 목소리의 폭로는 보이스오버(3컷) → 거울 속에서 정지하는 중전의 어두운 실루엣(4컷). `no pointing, no rising voice, no accusation gesture` — 종이가 말한다. 거울 반사는 실루엣 전용.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), a still unhurried strategist's composure — stepping quietly forward and drawing a folded paper from inside her sleeve, its writing only worn, faded, soft-edged ink strokes that never resolve into readable character shapes, no legible glyph anywhere on the paper. And the Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam) — present in the bronze mirror only as a dim subdued darkened silhouette, her raised hand pausing at her hair ornament, never a sharp second face, no double exposure, no duplicated figure. Plain bare pillars and beams, no plaques, no inscriptions. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candlelight against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the court lady stepping quietly forward from the depth, one hand drawing a folded paper from inside her sleeve, the motion unhurried and exact.
2. 100mm macro, static: the folded paper opening between her pale hands, its writing only worn faded soft-edged strokes that never resolve into readable characters.
3. 85mm close, static: the court lady's face, her eyes level on the Queen, lips closed, the calm flat revelation carried by voiceover only.
4. 85mm close, static: the bronze mirror's dim darkened silhouette of the Queen, her raised hand pausing at her hair ornament — a silhouette, no sharp second face, no double exposure.

REVELATION MOTION — IMPORTANT: physically-based the paper drawn from the sleeve, the fold opening flat, the hands steady — the accusation laid down flat and cold, no pointing, no rising voice, no accusation gesture, the revelation is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 멈춘 손 — 거울 속 중전의 손이 멈춤 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP40_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 멈춘 손, 거울 속 중전의 손이 멈춤. [처음으로 정면으로 보는 눈 — 무언] 무대사.
- **연출 특이**: **본화의 정적 절정 썬(무대사)** — 충격 전체가 **하나의 멈춘 손**이다. 떨잠 한 뼘 앞에서 얼어붙은 손끝 매크로(1컷) → 거울 속 같이 멈춘 어두운 반사(2컷) → 완전히 정지한 떨잠과 그 너머 숨쉬는 촛불(3컷). `no gasp, no clutched chest, no falling` — 소리 없는 정지가 고양 극을 대체한다. 거울 반사는 손도 실루엣으로만 — 이중 노출 슬롭 차단.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the Queen's hands and hairpiece only in the near frame, no face: the Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam) — her raised hand stopping mid-motion a finger's width from the pendant, the fingertips frozen. The tall bronze mirror on its dark wooden stand holds the same raised hand's dim darkened reflection, stopped as well — softened and silhouette-like, never a sharp second hand or face, no double exposure, no duplicated figure. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candle flame breathing out of focus beyond the ornament against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the Queen's raised hand at her hair ornament stopping mid-motion, the fingertips frozen a finger's width from the dangling pendant, the gold and jade pins sharp against the dark hair.
2. 100mm macro, static: the bronze mirror holding the same raised hand's dim darkened reflection, stopped as well — softened and silhouette-like, no sharp second hand, no double exposure, no duplicated figure.
3. 100mm macro, static: the small dangling pendant ornament hanging utterly still beneath the ornate hairpiece, the candle flame breathing softly out of focus beyond it, nothing else in the frame moving.

STILLNESS MOTION — IMPORTANT: physically-based the hand frozen a finger's width from the pendant, the pendant hanging utterly still, the flame breathing beyond — no gasp, no clutched chest, no falling, the whole shock is one stopped hand, no dialogue, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 협박이 아니라 구함 (절대 30.0~37.5 · 콘티 5컷 — 본화 최장 대화)

- **시트**: `downloads/EP40_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 협박이 아니라 구함. [억누른 위협 · 중전/`ko-KR-Neural2-B`, Pitch 0.0, Speed 1.0] "네가 지금 — 나를 협박하는 것이냐." (rel 3.0=절대 32.0) / [서늘한 구함 · 설화/`ko-KR-Neural2-A`, Pitch -1.0, Speed 1.0] "소녀는 구하는 것이나이다. 마마께서 살 길을 아직 가지고 있더라면 — 그 길을 소녀와 같이 걷는 것입니다. 아버님의 덫에 걸린 것은 폐하만이 아니지요. 윤씨 문중 전부입니다." (rel 5.0=절대 34.0, 사후 믹싱)
- **연출 특이**: **본화의 서사적 중심 썬(최대 5컷 배분)** — 두 대사 전부 보이스오버, 화면은 시선과 종이만. 어깨 너머 돌아보는 중전의 질문 클로즈(1컷) → 움직이지 않는 설화 클로즈(2컷) → 열어 놓은 종이를 **무기가 아니라 제안으로** 탁자에 내려놓는 매크로(3컷) → 탁자 너머 마주 보는 두 시선 — 침묵의 전투(4컷) → 어두운 거울 곁 한 개의 촛불 사이 대치 미디엄(5컷). `no weapon, no raised voice, no melodrama` — "협박"은 종이를 내려놓는 손으로만 존재한다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only. The Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam) — her question held behind closed lips and carried by voiceover only, the gracious lacquer gone from her eyes. And the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo), the stillness of someone offering a way out rather than a threat — her hands laying the opened paper gently down on the dark table, its writing only worn, faded, soft-edged ink strokes that never resolve into readable character shapes, no legible glyph anywhere on the paper. The tall bronze mirror on its dark wooden stand beside them holds only a dim subdued darkened reflection — never a sharp second face, no double exposure, no duplicated figure. Plain bare pillars and beams, no plaques, no inscriptions. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the one warm candle between them against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the Queen's face turning sharp over her shoulder toward the court lady, the question held behind closed lips, carried by voiceover only.
2. 85mm close, static: the court lady's face, unmoved and level, the stillness of someone offering a way out.
3. 100mm macro, static: her hands laying the opened paper gently down on the dark table before the Queen — the gesture an offer and not a weapon.
4. 85mm close, static: the two women's gazes meeting across the table, the Queen's cold measuring eyes and the court lady's level calm ones, the battle carried entirely in silence.
5. 50mm medium, static: the two women facing each other across the small dark table, the opened paper between them, the bronze mirror dim beside them, one candle between, both still.

OFFER MOTION — IMPORTANT: physically-based the paper laid gently down, the two hands apart, the gazes holding — not a threat but a way out, no weapon, no raised voice, no melodrama, both speeches are voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 중전이 스스로 페이지를 넘김 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP40_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro, 중전이 스스로 페이지를 넘김. [처음으로 내비치는 · 중전/`ko-KR-Neural2-B`, Pitch 0.0, Speed 1.0] "귀성에서 오는 짐이 바다를 타고 홍주로 간다. 그것을 — 나도 들었다." (rel 4.0=절대 39.5, 사후 믹싱)
- **연출 특이**: **저울이 기우는 썬(정본 안티슬롭 치환의 직결 지점)** — 자기 연민 독백 컷 0건. 저울은 **중전 자신의 손**이 움직인다: 황금 반지 손가락이 페이지 귀퉁이를 가져옴(1컷) → 한 번의 측정된 동작으로 페이지를 넘기는 매크로(2컷) → 변함없는 가면으로 읽는 얼굴, 내비침은 보이스오버(3컷) → 페이지 가장자리 너머로 설화를 향해 드는 첫 정직한 시선(4컷). `no one else's hand` — 넘김은 반드시 중전의 손이다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — the Queen's hands and face in the near frames: the Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery at the cuffs, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam) — her own pale hand, a gold ring at one finger, reaching across the dark table and taking the page's corner, turning the page over in one measured unhurried gesture, the court lady's hands withdrawn to the frame's edge. The page's writing is only worn, faded, soft-edged ink strokes that never resolve into readable character shapes, no legible glyph anywhere on the paper. The court lady Seolhwa appears in the last panel's depth only — a 21-year-old Korean court lady (gungnyeo), pale porcelain skin, an elegant dark pastel hanbok, neat traditional hair pinned with a single simple jade hairpin (binyeo), receiving the look without moving. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candlelight on the page against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro, static: the Queen's own pale hand — a gold ring at one finger — reaching across the dark table and taking the page's corner, the court lady's hands withdrawn to the frame's edge.
2. 100mm macro, static: her fingertip lifting the page and turning it over in one measured unhurried gesture, the paper's underside carrying only worn faded unreadable strokes.
3. 85mm close, static: the Queen's face reading the page in candle light, the composed mask unchanged, lips closed, the admission carried by voiceover only.
4. 85mm close, static: the Queen's eyes lifting over the page's edge toward the court lady, the first look in the scene that is neither lacquer nor measure, held a moment too long.

PAGE MOTION — IMPORTANT: physically-based the fingertip lifting the corner, the page turning in one measured gesture, the flame steady — the scales move by her own hand and no one else's, her admission is voiceover, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 두 여자의 조용한 거래 성립 (절대 45.0~52.5 · 콘티 3컷)

- **시트**: `downloads/EP40_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm, 두 여자의 조용한 거래 성립. [무대사]
- **연출 특이**: **무대사 성립 썬** — 대사 0건, 닫힌 종이가 서명이다. 탁자 너머 마주 선 두 프로파일(1컷) → 닫힌 종이 양옆에 각자 얹힌 두 손, 서로 닿지 않음(2컷) → 어두운 거울을 뒤로 하고 함께 선 두 여자(3컷). `no shaken hands, no embrace, no smiles` — 악수·포옹 같은 화해 슬롭 없음.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with live actors and real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two figures only, both still. The Queen (Jungjeon Yun) — a stately Korean queen in her mid-thirties, pale composed features, a cold courteous gentleness that never reaches her eyes, an elegant crimson patterned tangui jacket with gold embroidery, an ornate ceremonial hairpiece (gache) set with gold and jade hairpins and small dangling pendant ornaments (ttoljam). And the court lady Seolhwa — a 21-year-old Korean woman disguised as a palace court lady (gungnyeo), pale porcelain skin, cold piercing intelligent dark eyes, an elegant dark pastel court lady hanbok with clean embroidery, neat traditional hair pinned with a single simple jade hairpin (binyeo). The paper now closed and lying between them, its writing only worn faded soft-edged strokes that never resolve into readable characters; the Queen's hand at rest on the table beside it, the court lady's hand at rest on the other side, the two hands not touching. The tall bronze mirror on its dark wooden stand behind them holds only a dim subdued reflection — never a sharp second face, no double exposure, no duplicated figure. Plain bare pillars and beams, no plaques, no inscriptions. No flashbacks, no memory scenes. No blood, no wounds, no injuries anywhere. No weapons anywhere. All characters are adults. Lips closed, no words anywhere. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the warm candle burning lower against the cold blue night beyond the paper lattice windows, the bronze mirror holding its dim reflection — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close, static: the two women's profiles facing across the small dark table, the paper closed and lying between them, neither reaching for it.
2. 100mm macro, static: the Queen's hand coming to rest beside the closed sheet, the court lady's hand at rest on the other side, the two hands not touching, the sheet lying between them like a signature.
3. 50mm medium, static: the two women standing together in the hall's depth, the bronze mirror dark behind them, the candle burning low, both still, the bargain made in silence.

BARGAIN MOTION — IMPORTANT: physically-based the closed sheet between the two at-rest hands, the candle burning lower, the two women still — no shaken hands, no embrace, no smiles, the sheet lying between them is the signature, no dialogue, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 거울이 어두워짐 → 암전 → 타이틀 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP40_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드, 거울이 어두워짐 → 암전 → 타이틀. [무대사] / 자막: 제41화 「후원의 죽숲」에서 계속
- **연출 특이**: **EP41 훅 썬** — 문 쪽에서 바라본 빈 중궁전의 와이드, 촛불이 줄며 거울 반사가 함께 어두워진다(1컷) → 암전(2컷) → 타이틀(3컷, 편집 단계). 두 여자가 나가고 화장대 위 닫힌 종이만 남는다 — 저울의 다음 무게는 죽숲에서 떨어진다. 무대사 — 렌더 무음. 렌더는 완전 암전으로 끝난다.
- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no figures: the emptied queen's hall seen from the door side, the tall bronze mirror on its dark wooden stand dimming as the single candle burns low, its dark polished surface reflecting only the small flame — never a sharp second face, no double exposure, no duplicated figure. The dressing table and the closed paper left on it, its writing only worn faded soft-edged strokes that never resolve into readable characters. Plain bare pillars and beams, no plaques, no inscriptions. No blood anywhere. No speech. Lips closed. No readable letters, no characters, no labels anywhere.

LIGHT GUARD — IMPORTANT: the one warm candle burning low against the cold blue night beyond the paper lattice windows, the bronze mirror's reflection dimming with the flame — the season's cold-warm cross. No crushed blacks, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm wide, static: the emptied queen's hall from the door side, the tall bronze mirror dimming as the single candle burns low, the dressing table and the closed paper left on it, no figures.
2. the frame sinking into complete black, no text, held.
3. end card for the edit stage only — one vertical column of red Korean characters on black (the render must end in complete black; the title card is inserted in editing).

DARK MOTION — IMPORTANT: physically-based the flame sinking low, the mirror's reflection dimming with it, the hall emptying into black — the weight will fall in the bamboo grove, the render ends in complete black, lips closed throughout, no words anywhere. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 9. 보이스·SRT 원장 (사후 믹싱)

### 9-1. 보이스 모델 배정

| 화자 | 모델 | Pitch | Speed | 톤 지문 |
|---|---|---|---|---|
| 내레이션 | `ko-KR-Wavenet-C` | 0.0 | 0.9 | 무거운 나레이션(S1) — "중궁전의 문이 열린 것은 — 세 번째 문안에서였다."를 운반하는 목소리 |
| 중전 | `ko-KR-Neural2-B` | 0.0 | 1.0 | 가식의 온화(S2) → 억누른 위협(S5) → 처음으로 내비치는(S6) 3구 — plan 지정 Pitch 0.0, 겉인사의 온화가 S5에서 억누른 위협으로, S6에서 처음으로 내비치는 어조로 미세 이동하는 톤 설계 |
| 설화 | `ko-KR-Neural2-A` | -1.0 | 1.0 | 차분하고 서늘한 결의의 톤(S3 직격 폭로·S5 구함 2구) — characters.md 고정 등록치 그대로 |

본화 대사 5구(중전 3 + 설화 2) + 내레이션 1구 + 엔드카드 자막 1건, 전부 정본 썬표 1:1. 렌더는 무음 — 전 대사·내레이션 사후 믹싱. 발화 5구 전부 **입모양 배제**(100화 전편 규격) — 보이스오버·리액션 샷으로 처리. S4·S7·S8 무대사 — 렌더 무음. 이환(Neural2-C)·무결(Wavenet-C)·윤경헌(Wavenet-D) 본화 미등장·무발화 — 배정 제외. **동일 보이스 ID 다중 배역 없음** — 3인 3색(Wavenet-C/Neural2-B/Neural2-A), §0-13 피치 사다리 장치 불적용. 정본 AG 지문의 "중전·서 상궁 동일 ID 엄격 구분"은 서 상궁이 8썬표 미등장이므로 발동 조건 부재 — 서 상궁 등장 화에서 재검토. **세이프티 가드 준수**: 본화는 유혈·흉기 트리거 원천 부재 — "협박"은 종이와 시선으로만 운반.

### 9-2. SRT 블록 (절대 타임코드)

```srt
1
00:00:02,000 --> 00:00:04,600
중궁전의 문이 열린 것은 — 세 번째 문안에서였다.

2
00:00:09,500 --> 00:00:13,200
홍화. 네가 요즘 대전의 약탕을 맡고 있다며. 수고가 이만저만이 아니겠구나.

3
00:00:17,500 --> 00:00:21,800
마마께서는 아버님을 밀고하신 분이지요. 그러나 아버님께서는 — 마마를 죽이는 밀서를 준비해 두셨나이다.

4
00:00:32,000 --> 00:00:33,800
네가 지금 — 나를 협박하는 것이냐.

5
00:00:34,000 --> 00:00:37,400
소녀는 구하는 것이나이다. 마마께서 살 길을 아직 가지고 있더라면 — 그 길을 소녀와 같이 걷는 것입니다. 아버님의 덫에 걸린 것은 폐하만이 아니지요. 윤씨 문중 전부입니다.

6
00:00:39,500 --> 00:00:41,900
귀성에서 오는 짐이 바다를 타고 홍주로 간다. 그것을 — 나도 들었다.

7
00:00:58,000 --> 00:00:59,800
제41화 「후원의 죽숲」에서 계속
```

- 시작 시각은 정본 rel 수치(3.0→2.0 / 4.0→9.5 / 5.5→17.5 / 3.0→32.0 / 5.0→34.0 / 4.0→39.5)의 절대 시각 그대로. 종료 시각은 각 구의 음절 길이에 맞춘 권장치 — 실제 TTS 합성 길이에 맞아 조정.
- S4·S7(무대사)은 SRT 미기재.
- 7번 자막(58.0~59.8)은 암전 이후 삽입 — S08 렌더는 완전 암전으로 끝나고 타이틀은 편집 단계 참조.
- TTS 트랙 분리: 내레이션 1구(`EP40_S1_NARRATION`), 중전 3구(`EP40_S2_JUNGJEON`·`EP40_S5_JUNGJEON`·`EP40_S6_JUNGJEON`), 설화 2구(`EP40_S3_SEOLHWA`·`EP40_S5_SEOLHWA`) — 보이스 ID 3인 3색이라 동일 ID 혼동은 없으나, 파일명 규칙으로 트랙을 분리 관리한다(EP38~EP39 규격 계승).

---

## 10. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP40_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP40_VARIABLE_STORYBOARD_AND_PROMPTS.md` (본 문서) |
| 생성기(재현용) | `projects/sageuk-revenge/ep40_sheets.py` (`python3 … S01 S03` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP40_QC_CHECKLIST.md` |
