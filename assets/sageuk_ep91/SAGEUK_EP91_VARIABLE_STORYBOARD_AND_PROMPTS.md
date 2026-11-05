# 「혈화의 궐」 EP91 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제91화 「사헌부의 눈」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제91화 「사헌부의 눈」` 절, 원전: 제91장 정본) + `characters.md` 캐릭터 앵커(이설화, 강무결 — 무결 Wavenet-C -1.0·설화 Neural2-A 0.0은 plan 우선 원칙 채택) + EP22~EP90 원장 템플릿(동일 규격)
> **범위**: EP91 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·속마음 자막·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP90 S8 엔드카드 「제91화 사헌부의 눈에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 35mm · 산소, 묘비 앞에 선 설화 [설화/Neural2-A (0.0): "아버님. 이름이 — 도로 새겨졌사옵니다. 종이로 죽으신 아버님이, 종이로 다시 살아나셨사옵니다." (rel 5.0=절대 2.5)], S2 100mm Macro · 묘비, 묘비의 이름 — 이정현 (무대사), S3 85mm, 묘비 앞의 고백 [설화/Neural2-A (0.0): "딸이 미안하옵니다. 그러나 이제 알겠사옵니다 — 종이를 쓰는 것이 죄가 아니었나이다. 사람을 죽이도록 쓰는 종이가 — 죄였나이다." (rel 5.5=절대 9.5)], S4 50mm, 가을 — 사헌부 감규의 직첩 [내레이션/Wavenet-C (0.0): "그 자리는 사람을 벌하기 위한 것이 아니라 — 사람이 사람으로 다뤄지고 있는지를 보기 위한 자리였다." (rel 4.5=절대 17.0)], S5 85mm, 처음으로 아버지의 마음을 앎 [설화/Neural2-A (0.0): (속마음 자막) "아버지가 — 어떤 마음으로 그곳에 계셨는지." (rel 3.0=절대 24.5)], S6 100mm Macro · 환도, 허리의 환도 — 꺼낼 때를 고르는 무결 [내레이션/Wavenet-C (0.0): "환도는 여전히 허리에 있었으나 — 그는 이제, 그것을 꺼낼 때를 골랐다." (rel 4.5=절대 32.0)], S7 85mm, "그것이 자유의 무게였다" [무결/Wavenet-C (-1.0): "그것이 — 자유의 무게이지요." (rel 3.0=절대 47.0) — 내레이션과 동일 보이스 ID이므로 피치 -1.0 분리 및 별도 세션 트랙 지정], S8 35mm → 엔드카드, 가을 산소 → 암전 → 타이틀(자막: 제92화 「풀려난 이름들」에서 계속).
> **안티슬롭 ① — 복수의 완결 고양 극 배제(plan·정본 안티슬롭 지정)**: 복수 완결의 고양·환호·정산 테이블로·눈물 범벅 렌더 **0건**. 치환 — **묘비 앞의 낮고 무거운 보고와 성찰**("사람을 죽이도록 쓰는 종이가 죄였나이다"): 복수의 끝은 함성이 아니라 아버지 묘비 앞의 낮은 보고다. `no triumphant exultation, no revenge-completed tableau, no wailing` 전 썬 상설.
> **안티슬롭 ② — 무결의 변화 설명 배제(plan·정본 안티슬롭 지정)**: 성장 서사 해설·독백·변화 몽타주 렌더 **0건**. 치환 — **"그것이 자유의 무게이지요"라는 단 한 문장**(S7 2비트)과 **꺼낼 때를 고르는 손끝의 물리**(S6 5비트): 변화는 설명되지 않고 고르는 손에 있다. `no explanation of his change, no monologue, no vow ceremony` 전 썬 상설.
> **S2 묘비의 이름(plan·정본 지정)** — 새겨진 단 한 줄의 이름 「이정현」 100mm 매크로. **묘비 텍스트 1줄 한계 엄수(정본 AG ①)** — 돌에는 단 한 줄의 새김만, 날짜·관직·비명 2줄째 0건. **본화의 유일한 가독 문자 요소**이며 렌더 프롬프트의 클린 프레이밍 블록에 죽은 자의비각으로 명시적 허용한다.
> **S4 직첩 매크로(plan·정본 지정)** — 가을빛 아래 사헌부 감규의 직첩 종이 매크로. 백지 설계 교칙 준수 — 직첩은 줄선 낱행 라인일 뿐, 가독 글자 0건.
> **S6 환도 손끝 매크로(plan·정본 지정)** — 허리의 환도 코등이를 쥔 채 꺼낼 때를 고르는 무결의 손끝 매크로. **칼날 전면 인출 0건** — 코등이 한 뼘만 들리고 다시 힘을 뺀다. `the blade never drawn, no fighting, no combat` 가드.
> **백지 설계 교칙(전편 규격) + 본화 예외**: 프레임 내 기물 위 가독 글자 **0건** — 단, **S2 묘비의 단 한 줄 새김 이름만 예외**. 직첩·문서는 줄선 낱행 라인일 뿐. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기입된다. `no letterforms, no hangul, no hanja` 전 썬 상설(S2 묘비각 제외).
> **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S2 묘비 단 한 줄 새김 + S08 붉은 타이틀(편집 단계 참조용)**뿐. S5의 속마음 자막("아버지가 — 어떤 마음으로 그곳에 계셨는지")은 **편집 단계 자막 삽입** — 시트와 렌더에 자막 활자를 그리지 않는다. 엔드카드 자막(제92화 「풀려난 이름들에서 계속」)도 편집 단계 삽입, S08 렌더는 암전으로 끝난다.
> **세이프티 가드(plan 절대 준수) — 유혈 직결 어휘 0건**: `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. 금지 어휘(`poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder`)와 참견 어휘(`slash`·`stab`·`execution`·`kill` 등)는 생성기 `validate()`로 전수 차단 확인 — **어간 부분 문자열도 차단된다**(EP66 실측 계승, 본화 `steadying` 회피 실측).
> **캐릭터 앵커(plan·characters.md 지정)**: 이설화 — **사헌부 감규의 단정한 한복, 품에 품은 직첩, 소박한 옥비녀, 선친 묘비 앞에서 비통함을 넘어선 깊은 성찰을 올리는 눈빛**(21세 — characters.md 다크 파스텔 궁녀 한복·서늘하고 총명한 눈빛·옥비녀 앵커 준수; S1 보고·S3 고백·S4 직첩·S5 깨달음). 강무결 — **무관복(짙은 남색 융복), 허리의 환도 코등이를 쥔 채 칼을 꺼낼 때를 고르는 성숙한 무관**(25세 — characters.md 뺨의 검흔·묵직한 눈빛 앵커 준수; S6 환도·S7 자유의 무게). **인물 상한** — S01 설화 1인+능선 아멈 원경 1인, S02 인물 0명(돌 매크로만), S03 설화 1인, S04 설화 1인, S05 설화 1인, S06 무결 1인(손 매크로), S07 무결 1인, S08 능선 아멈 원경 1인 → 소실. 이환·윤경헌·중전: 본화 등장 0건.
> **입모양 배제(100화 전편 규격)** — 설화 대사 2구(S1·S3) + 속마음 자막 1구(S5) + 내레이션 2구(S4·S6) + 무결 대사 1구(S7) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S2·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 본화 `ko-KR-Wavenet-C`는 **내레이션(0.0) 2구(S4·S6) + 무결(-1.0 — plan 확정치, characters.md -1.5 대신 plan 우선 원칙) 1구(S7) — 동일 ID 공존이므로 피치 -1.0 분리 및 별도 세션 트랙 지정 필수**(피치 사다리: 내레이션 0.0 > 무결 -1.0; 뱃사공 -2.0·금군 -1.0은 본화 등장 0건 — 무결과 금군은 피치값이 같으므로 **세션 트랙 분리 + 감정 톤 지문으로 배역 구분**). 설화 `ko-KR-Neural2-A`(0.0 — plan 확정치, characters.md -1.0 대신 plan 우선 원칙) S1·S3·S5 3구 — 본화 단독 모델, 사다리 충돌 없음. 파일명: `EP91_S1_SEOLHWA` / `EP91_S3_SEOLHWA` / `EP91_S4_NARRATION` / `EP91_S5_SEOLHWA` / `EP91_S6_NARRATION` / `EP91_S7_MUGEOL`. 렌더는 전 썬 무음.
> **가변 컷 배분**: 4/2/5/3/3/5/2/4 = 28컷 — EP13~EP90 전 배분(102종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP90 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP90분 3/6/4/5/3/3/1/3과도 상이). **S3(묘비 앞의 고백) 5컷·S6(환도의 손끝) 5컷 공동 최장** — 본화 안티슬롭 치환의 쌍두마차(고백의 완급, 칼을 고르는 손끝). S1(묘소의 보고) 4컷, S4(직첩)·S5(아버지의 마음) 각 3컷, **S2(이름 한 줄)·S7(자유의 무게) 각 2컷 절제**, S8(가을→암전→타이틀) 4컷 — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 12회(초벌 8 + 재렌더 4) 중 최종 채택 8장 — **재렌더 4건**: ① S02 초벌(하단 패널 따뜻한 세피아 광원 유입, 가시 채색 1.20%) → 재렌더 1차(0.08% 잔여) → 재렌더 2차(0.00% 해소). ② S03 초벌(묘비에 낙서 로마자 각자 "MIN YEONGIK" — 단 한 줄 설계 위반) → 재렌더 해소(빈 돌). ③ S04 초벌(묘비에 낙서 로마자 각자 "JUNG HYUN-MU") → 재렌더 해소(빈 돌). ④ S03·S04 초벌 공통 해상도 1023×1537 → S03은 정규화(LANCZOS 리사이즈), S04는 재렌더로 해소. 재렌더 계기 가드 — 생성기에 **본화 묘비 무각 가드**(S02 시트 외 묘비 각자 금지)를 `build_prompt()`에 신설, 이후 화 계승. 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.10%(적색 타이틀 — 좌표 확인, 타이틀 열 x387~405·y1026~1248 한정 — 의도 채색). **전장 md5: S01 90dad0aa8e48 / S02 28dedd118bd5 / S03 0bc3f84e8b8f(정규화 최종본) / S04 31b4277c0743 / S05 ecf350da44c5 / S06 14f31e2a3fb4 / S07 b80a2b7b8c4c / S08 d9a8178fb916**.
> **검독 운영 교훈(EP67~EP90 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전 첨부를 돌려줄 수 있다** — 본화 S02·S03 재렌더 후 재열람에서 초벌본과 동일한 첨부가 재반환돼(md5는 변경 확인) **별도 크롭 경로(`downloads/qc_crops/Z_EP91_*`) 재열람으로 현재본 판정**했다. **어간 부분 문자열 함정 계승** — `steadying`이 금지 어휘 `dying`을 포함해 생성기 validate()가 차단 — 본화 설계에서 `holding the fold level`로 회피(EP66·EP87~EP90 계승 가드 유효 재확인). **본화 신규 함정**: 콘티 생성기가 묘비 묘사를 받으면 로마자 비문을 지어 새긴다(S03·S04 초벌 동시 발생) — **S02 전용 시트가 아닌 시트에는 묘비를 빈 돌로 그리라는 가드를 프롬프트에 명시**해 해소.
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제91화 「사헌부의 눈」 절(원전: 제91장 정본) 직접 열람**(291행 이하) — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. **S08 타이틀 슬롯**: 「제92화 풀려난 이름들에서 계속」 실제 글자수 14자 = 1자 1슬롯 원칙에 따라 **14슬롯** 확정(확대 크롭 검독 통과, 숫자 9·2 각각 단독 슬롯, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). **보이스 P 보정 병기**: characters.md는 무결 Wavenet-C -1.5·설화 Neural2-A -1.0을 표기하나, plan 확정치(무결 -1.0·설화 0.0)를 본화에 채택 — plan 우선 원칙. **plan 배분 기재 "선행 전 배분 102종 미중복"과 실측 102종 일치** — 기계 스캔 수치가 우선.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep91_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep91_sheets.py S01`), 전체는 `ALL`(명시적).

---

## 0. 공통 규칙 (전 썬 강제) 및 7요소 규격

### 0-1. 7요소 = 블록 프롬프트의 고정 문단 순서

| 요소 | 명칭 | 고정 문단 | 생략 |
|---|---|---|---|
| ① | 시트 차단 (Sheet Block) | `OUTPUT FORMAT — READ FIRST:` 문단 | 금지 |
| ② | 화풍 전환 (Layout → Live Action) | `Fictional historical period-drama film scene. Convert this director's storyboard sheet…` | 금지 |
| ③ | 필름 룩 락 (Stock & Color Lock) | `Shot on ARRI Alexa 35… Full rich cinematic color — NOT monochrome…` | 금지 |
| ④ | 캐릭터 가드 (Character Guard) | `CHARACTER GUARD — …` (해당 썬 등장 인물 앵커 인라인) | 금지 |
| ⑤ | 광원 가드 (Light Guard) | `LIGHT GUARD — IMPORTANT: …` | 금지 |
| ⑥ | 컷 재현 (Cut-by-Cut Reconstruction) | `Recreate the N panels in order as one continuous ~10 second sequence:` + 번호 컷 리스트 | 금지 |
| ⑦ | 물리·프레임 가드 (Physics & Clean Framing) | `… MOTION — IMPORTANT: physically-based …` + `Absolutely NO text, NO labels…` | 금지 |

8개 블록 전부 위 7문단을 같은 순서로 갖는다. 문단 추가는 허용, 삭제는 불가.

### 0-2. 전 썬 공통 규칙

1. **시트 = 구도 가이드일 뿐**: 첨부 연필 콘티는 LAYOUT/COMPOSITION GUIDE. 스케치 화풍이 영상에 묻어나면 결함이다.
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 설화 다크 파스텔 궁녀 한복, 무결 짙은 남색 융복, 가을 산소의 실제 낙엽과 햇살, 늦은 오후 복도 측광이 실제 색으로 복원된다. **붉은 색은 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화 유일 예외 — S02 묘비각**: 돌에 새겨진 단 한 줄의 이름은 죽은 자의 묘비각(diegetic carving)이므로 렌더에 존재하며, 그 외 문자는 일체 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **묘소의 보고**(the standing report, the low bow), S2 **돌과 한 줄 새김**(the weathered stone, the single carving), S3 **고백의 완급**(the kneeling, the settled stillness), S4 **펼쳐지는 직첩**(the unfolding patent), S5 **넓어지는 시선**(the gaze leaving the stone), S6 **칼을 고르는 손끝**(the choosing hand, the guard a finger's width), S7 **짊어진 무게의 정지**(the carried weight), S8 **고르게 물러가는 가을빛**(the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S2 묘비 단 한 줄 + S08 붉은 타이틀(편집 단계)뿐**. 직첩·문서는 줄선 낱행과 공란으로만 — 가독 글자 렌더 0건. S5의 속마음 자막과 엔드카드 자막(제92화 「풀려난 이름들에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 설화 대사 2구(S1·S3)·속마음 1구(S5)·내레이션 2구(S4·S6)·무결 대사 1구(S7)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S2·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이설화(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, a folded paper patent of office carried at her chest, eyes of deep reflection that have gone past grief, lips closed.
   - **강무결(plan·characters.md 지정)**: the warrior, Mugeol — a 25-year-old Korean military officer in a dark navy military uniform, a slight scar across his cheekbone, a plain curved sword at his waist, a mature warrior quietly choosing the hour to draw it, heavy level eyes, lips closed.
   - **인물 상한**: S01 설화 1인+능선 아멈 원경 1인, S02 인물 0명, S03 설화 1인, S04 설화 1인, S05 설화 1인, S06 무결 1인(손 매크로), S07 무결 1인, S08 능선 아멈 원경 1인 → 소실 — 군중·행렬·조문객 렌더 0건.
9. **광원 표기**: S1~S5 — **가을 오후의 낮은 햇살이 나뭇가지 사이로 능선의 묘소에 비치는 것**이 유일한 광원(씬별 각도·면 변주 분리 유지: S1 능선 전면, S2 새김면에 옆으로 스치는 빛, S3 잔디 위 낮은 평광, S4 개활지 평광, S5 나뭇가지 사이 측광). S6~S7 — **늦은 오후의 복도 측광이 살 사이로 비치는 것**. S8 — 하루의 마지막 가을빛이 고르게 낮아지다 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설. **EP90 어전 아침빛 가드를 본화 묘소 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 가을 산소·균일 암전 구간 이후의 붉은 타이틀(제92화 「풀려난 이름들에서 계속」, 14슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S4·S6 2구. 무결 `ko-KR-Wavenet-C` (Pitch **-1.0** — plan 확정치, characters.md -1.5 대신 plan 우선 원칙, Speed 1.0, 묵중한 무사 톤) — S7 1구. **내레이션과 동일 보이스 ID — 피치 -1.0 분리 및 별도 세션 트랙 지정 합성 필수**(피치 사다리: 내레이션 0.0 > 무결 -1.0). 설화 `ko-KR-Neural2-A` (Pitch **0.0** — plan 확정치, characters.md -1.0 대신 plan 우선 원칙, Speed 1.0, 비통함이 정리된 보고 톤) — S1·S3·S5 3구(S5는 속마음 자막 대상). 본화 내레이션 2구 + 캐릭터 대사 3구(S1·S3·S7) + 속마음 자막 1구(S5) + 엔드카드 자막 1건. **이환·윤경헌·중전 대사 0구** — 본화는 설화와 무결의 회차다. S2·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 2구 + 무결 `Wavenet-C`(-1.0) 1구 — **동일 ID 공존: 별도 세션 트랙 분리 + 피치 사다리(0.0 > -1.0) 필수**. 금군(-1.0)과 무결의 피치값이 같아도 본화 등장 0건이므로 실충돌 없음, 단 세션 트랙 분리 규칙 병기. 설화 `Neural2-A`(0.0) 3구 — 상이 모델, 단독. 파일명 분리 규칙 기재(`EP91_S1_SEOLHWA`/`EP91_S3_SEOLHWA`/`EP91_S4_NARRATION`/`EP91_S5_SEOLHWA`/`EP91_S6_NARRATION`/`EP91_S7_MUGEOL`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/2/5/3/3/5/2/4 = 28컷 — EP13~EP90 전 배분 102종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S3 5컷·S6 5컷 공동 최장**(고백, 손끝), S1 4컷, S4·S5 각 3컷, **S2·S7 각 2컷 절제**, S8 4컷 — "3컷·4컷 고정" 슬롭 회피.
16. **복수의 끝은 함성이 아니라 보고다(본화 핵심)**: 본화에는 고양도 환호도 정산 테이블로도 변화 해설도 없다 — 복수의 끝은 아버지 묘비 앞의 낮은 보고로, 무결의 변화는 꺼낼 때를 고르는 손끝과 단 한 문장으로만 존재하고, 화는 가을 산소의 고요한 풍경으로 닫힌다. 전 썬 `no triumphant exultation, no revenge-completed tableau, no wailing` 상설. S6·S7 `no explanation of his change, no monologue, no vow ceremony, the blade never drawn` 상설. 종식(S8)은 대사가 아니라 풍경이다 — 능선을 홀로 내려가는 작은 뒷모습, 고르게 낮아지는 가을빛, 균일한 어둠.

---

## 1. S01 첫째 — 묘비 앞에 선 설화 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP91_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm · 산소. [무거운 보고 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "아버님. 이름이 — 도로 새겨졌사옵니다. 종이로 죽으신 아버님이, 종이로 다시 살아나셨사옵니다." (rel 5.0=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 4비트)** — 능선 길로 다가오는 작은 인영(1) — 직첩을 품고 묘비 앞에 선 설화(2) — 돌을 향한 낮은 정중한 절(3) — 낮고 무겁게 보고하는 얼굴(4). **안티슬롭 가드(plan 지정)** — 복수 완결의 고양·오뇌(오래 울음)·조문 행렬 0건 — 보고는 낮고 무겁다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one woman in focus: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, a folded paper patent of office carried at her chest, eyes of deep reflection that have gone past grief, standing before a single weathered stone tombstone on a quiet autumn ridge; one small distant figure on the path far below stays out of focus and far away; no mourners, no procession, no wailing, no triumphant exultation, no revenge-completed tableau. No letterforms, no hangul, no hanja anywhere — the tombstone stays plain blank weathered granite with no carving visible in this scene. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low autumn afternoon sun coming through the branches onto the ridge is the only light, laying thin long shadows across the worn grass. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide: the mountain grave in autumn — a single weathered stone tombstone standing alone on a quiet ridge under thinning autumn trees, one small figure approaching along the path far below.
2. 35mm medium: the court lady Seolhwa standing before the tombstone — the folded paper patent of office carried at her chest, her eyes carrying a reflection deeper than grief.
3. 35mm close: her low formal bow toward the stone — the report beginning.
4. 35mm close: her face as she reports — a low heavy report and not weeping, grief turned into words of duty.

REPORT MOTION — IMPORTANT: physically-based the standing report, the low bow — the revenge is complete and the scene refuses to celebrate it: the small figure climbs the ridge path at a tired walking pace, the daughter stands with the patent held at her chest and bows once, low and exact, and her face delivers a low heavy report instead of weeping; no triumphant exultation, no revenge-completed tableau, no wailing; her line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 묘비의 이름, 이정현 (절대 07.5~15.0 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP91_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 묘비. 무대사 — 렌더 완전 무음.
- **연출 특이**: **이름 썬(가변 2비트 절제)** — 이끼 낀 풍화 화강암 면과 단 한 줄 새김 이름(1) — 낮은 가을빛을 받는 새김 자리(2). **묘비 텍스트 1줄 한계 엄수(정본 AG ①)** — 날짜·관직·비명 2줄째 0건. 종이에서 빼앗긴 이름이 돌로 돌아온다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: only the face of the tombstone — weathered granite, moss at the lower edge, and ONE single carved line of Korean characters reading 「이정현」, a name newly carved into old stone, and nothing else carved on the stone: no second line, no dates, no official titles, no epitaph, no other lettering anywhere in frame; the carving is a grave-marker's inscription, a dead man's name given back to stone; no figure, no hand, no shadow of a person. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low autumn afternoon sun grazing the carving side-on is the only light, putting one moving brightness along the carved strokes while the moss stays dark. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the tombstone's face — weathered granite, moss at the lower edge, and one single carved line of characters reading 「이정현」, the restored name, and nothing else carved on the stone.
2. 100mm macro, slow travel: the carved name line catching the low autumn light — the name given back to the stone, one line only.

STONE MOTION — IMPORTANT: physically-based the weathered stone, the single carving — the camera travels the stone's face at macro distance and almost nothing moves: the grain of the granite passes, the moss holds its dark edge, and the one carved line of the name catches the grazing light as the angle changes; the stone carries exactly one carved line and no second line, no dates, no epitaph; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output — the ONLY text anywhere is the single carved name line on the stone face, which is a diegetic grave-marker's carving. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 묘비 앞의 고백 (절대 15.0~22.5 · 콘티 5컷 ★ 최장)

- **시트**: `downloads/EP91_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [비통함이 정리된 보고 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "딸이 미안하옵니다. 그러나 이제 알겠사옵니다 — 종이를 쓰는 것이 죄가 아니었나이다. 사람을 죽이도록 쓰는 종이가 — 죄였나이다." (rel 5.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **고백 썬(가변 5비트 공동 최장)** — 묘비 앞에 정좌하는 설화(1) — 치마 아래 낮게 모은 사죄의 손(2) — 이해로 정리된 비통함의 얼굴(3) — 새긴 이름을 올려보며 죄의 본체를 가려내는 눈(4) — 성찰로 가라앉은 정지(5). **안티슬롭 가드(plan 지정)** — 오뇌 붕괴·눈물 과장·고양 0건 — 고백의 무게는 한 구분에 있다: 종이를 쓴 죄가 아니라 사람을 죽이도록 쓴 종이의 죄.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person only: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, kneeling formally on worn grass before the tombstone, grief arranged into understanding, eyes of deep reflection that have gone past grief; no second person, no mourner, no wailing, no collapsed grief, no triumphant exultation, no revenge-completed tableau. No letterforms, no hangul, no hanja anywhere — the tombstone stays plain blank weathered granite with no carving visible in this scene. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low autumn afternoon sun lying flat across the graveside is the only light, holding the kneeling figure and the stone in one even warmth. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm medium: Seolhwa kneeling formally on the worn grass before the tombstone — the confession beginning.
2. 85mm close: her hands folded low at her skirt — the daughter's apology.
3. 85mm close: her face — grief arranged into understanding, the apology finishing.
4. 85mm close: her eyes lifted to the carved name — the fault named for what it was: paper written to destroy people, and not the writing of paper itself.
5. 85mm medium: her stillness after the confession — a daughter whose grief has settled into reflection.

CONFESSION MOTION — IMPORTANT: physically-based the kneeling, the settled stillness — the confession's whole weight lands on one distinction: writing paper was never the fault, paper written to destroy people was: she kneels with a straight back and quiet hands, her folded fingers hold the apology without trembling, the understanding settles on her face without a tear shown, her eyes lift to the stone, and her stillness after is reflection and not despair; no wailing, no collapsed grief, no triumphant exultation, no revenge-completed tableau; her line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 가을, 사헌부 감규의 직첩 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP91_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "그 자리는 사람을 벌하기 위한 것이 아니라 — 사람이 사람으로 다뤄지고 있는지를 보기 위한 자리였다." (rel 4.5=절대 17.0, 사후 믹싱)
- **연출 특이**: **직첩 썬(가변 3비트)** — 저고리 품에서 꺼내는 접힌 직첩(1) — 가을빛에 펼쳐지는 백지(2) — 두 손에 받쳐 돌을 향해 들어 올려지는 직첩(3). **백지 설계 교칙** — 직첩은 줄선 낱행 라인일 뿐. 자리의 정의(벌하는 자리가 아니라 사람이 사람으로 다뤄지는지 보는 자리)는 나레이션이 담당 — 화면은 종이를 받쳐 드는 손으로 답한다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person in frame: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, drawing a folded paper patent of office from the front of her jacket and holding it open in both hands toward the stone; no second person. The patent paper shows only blank ruled lines and never readable characters. No letterforms, no hangul, no hanja anywhere — the tombstone stays plain blank weathered granite with no carving visible in this scene. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late autumn afternoon sun flat across the clearing is the only light, lifting the paper's weave and laying one pale band across the stone. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the graveside clearing in late autumn light — Seolhwa drawing the folded paper patent of the inspectorate from the front of her jacket.
2. 50mm close: the patent paper unfolding in the autumn light — its surface only blank ruled lines.
3. 50mm close: the open patent held in both hands toward the stone — an office that existed to see that people were treated as people, and not to punish them.

PATENT MOTION — IMPORTANT: physically-based the unfolding patent — an office explained by holding its paper to a father's stone: the folded paper comes out from the jacket with the small resistance of cloth, unfolds with the soft pull of the wind, and is held open in both steady hands toward the stone; the paper shows only blank ruled lines and never readable characters; no recitation, no reading aloud, no triumphant exultation, no revenge-completed tableau; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 처음으로 아버지의 마음을 앎 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP91_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [무거운 깨달음 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] (속마음 자막) "아버지가 — 어떤 마음으로 그곳에 계셨는지." (rel 3.0=절대 24.5, 속마음 자막은 편집 단계 삽입, 사후 믹싱)
- **연출 특이**: **깨달음 썬(가변 3비트)** — 돌을 보는 눈(1) — 능선을 넘어 가을 골짜기로 나가는 시선(2) — knowledge로 가라앉는 얼굴(3). **안티슬롭 가드** — 눈물 연기·과장된 깨달음 표정 0건 — 알게 됨이지, 울게 됨이 아니다. 속마음 자막은 편집 단계 삽입 — 시트·렌더에 자막 활자 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person only: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, her eyes on the stone and then travelling out across the autumn valley below the ridge, understanding settling on her face quiet and unforced; no second person, no tears, no wailing, no triumphant exultation, no revenge-completed tableau. No letterforms, no hangul, no hanja anywhere, and NO subtitle text drawn anywhere in frame — the tombstone stays plain blank weathered granite with no carving visible in this scene. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low autumn afternoon sun coming side-on through the branches is the only light, moving in thin bars across her face as the leaves stir. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close: her eyes on the stone — the first seeing of what her father's heart had carried in that seat.
2. 85mm medium: her gaze travelling out from the stone across the autumn valley below the ridge — the width of the watch her father kept.
3. 85mm close: her face as the understanding settles — quiet, unforced, past grief into knowledge.

REALIZATION MOTION — IMPORTANT: physically-based the gaze leaving the stone — the first seeing plays as knowing, not as tears: her eyes rest on the stone, then lift and travel out across the wide autumn valley the way a watchful man's eyes once had to travel every day, and the understanding settles on her face quiet and unforced; no tears, no gasp, no trembling, no triumphant exultation, no revenge-completed tableau; her inner-voice line arrives later as a subtitle by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 허리의 환도, 꺼낼 때를 고르는 무결 (절대 37.5~45.0 · 콘티 5컷 ★ 최장)

- **시트**: `downloads/EP91_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 환도. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "환도는 여전히 허리에 있었으나 — 그는 이제, 그것을 꺼낼 때를 골랐다." (rel 4.5=절대 32.0, 사후 믹싱)
- **연출 특이**: **손끝 썬(가변 5비트 공동 최장)** — 납작히 얹힌 손(1) — 코등이를 쥐는 손가락(2) — 한 뼘 들리는 칼도(3) — 힘을 빼고 다시 앉는 칼(4) — 떠나는 손끝(5). **안티슬롭 가드(plan 지정)** — 변화 해설·독백·맹세 의식·칼 전면 인출·전투 0건 — 칼은 한 번도 칼집을 떠나지 않고, 시간을 고르는 손만 연출된다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person in frame, hands and waist only: the warrior, Mugeol — a 25-year-old Korean military officer in a dark navy military uniform, a plain curved sword at his waist, his hand resting on the scabbard and closing on the sword's guard; his face is not in frame; the blade never drawn, no fighting, no combat, no second person, no explanation of his change, no monologue. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late-day side light along the veranda's wood, putting one line of light on the guard, is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the side light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the palace veranda in late-day light — the plain curved sword at the waist of the standing officer, his hand resting flat on the scabbard.
2. 100mm macro: the fingers closing on the sword's guard — a hand that knows the weight.
3. 100mm macro: the guard lifted a finger's width — the blade never drawn, only the choosing of the hour.
4. 100mm macro: the hand easing open — the sword settling back into its sheath, the hour not yet.
5. 100mm macro: the hand leaving the guard at rest — a warrior who now chooses his moment and does not rush it.

HAND MOTION — IMPORTANT: physically-based the choosing hand, the guard a finger's width — what the scene shows is a warrior who now chooses his hour: the fingers settle on the guard without hurry, the guard lifts one finger's width with a line of light on the bare steel's edge and no more, and then the hand eases open and the sword settles back into its sheath with a soft final click of wood, the fingertips parting from the guard slowly; the blade never leaves the sheath, no vow ceremony, no explanation of his change, no monologue, no fighting, no combat; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — "그것이 자유의 무게였다" (절대 45.0~52.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP91_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [묵중한 · 무결/`ko-KR-Wavenet-C`, Pitch **-1.0** — plan 확정치, characters.md -1.5 대신 plan 우선 원칙, Speed 1.0 — **내레이션과 동일 보이스 ID이므로 피치 -1.0 분리 및 별도 세션 트랙 지정**] "그것이 — 자유의 무게이지요." (rel 3.0=절대 47.0, 사후 믹싱)
- **연출 특이**: **한 문장 썬(가변 2비트 절제)** — 복도 늦은 빛 속에 허리의 칼을 지닌 채 선 무결(1) — 단 한 문장을 머금은 얼굴(2). **안티슬롭 가드(plan 지정)** — 변화 해설·독백·회상 몽타주 0건 — 변화는 단 한 문장("그것이 자유의 무게이지요")으로만 말해진다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person only: the warrior, Mugeol — a 25-year-old Korean military officer in a dark navy military uniform, a slight scar across his cheekbone, a plain curved sword carried at his waist, a mature warrior quietly choosing the hour to draw it, heavy level eyes, his posture settled and unhurried; the blade never drawn, no second person, no explanation of his change, no monologue, no vow ceremony. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late-day light lying along the corridor's wood is the only light, holding the standing figure in one warm band. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the side light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the warrior standing in the corridor's late light, the sword carried at his waist — the weight worn and carried knowingly.
2. 85mm close: his face — the single quiet sentence held in it, no explanation, no narration of change.

WEIGHT MOTION — IMPORTANT: physically-based the carried weight — his change is never explained and the sentence says it whole: he stands settled and unhurried with the sword worn knowingly at his waist, his face holds the one quiet sentence, and the weight of it sits on him like something chosen and not suffered; the blade never drawn, no monologue, no vow ceremony, no explanation of his change, no triumphant exultation; his line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 가을 산소 → 암전 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP91_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제92화 「풀려난 이름들」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 4컷)** — 능선 길로 홀로 내려가는 작은 뒷모습(1) — 나무들과 홀로 남은 돌(2) — 완전한 암전(3) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **안티슬롭 가드(plan 지정)** — 종반 고양·유품 태블로·에필로그 0건 — 산은 이름을 지키고 빛은 그저 떠난다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one small distant figure only, never in focus: a woman walking away down the ridge path, growing smaller and farther until the path is empty; the tombstone stays plain blank weathered granite with no carving visible in this scene; no finale tableau, no looking back, no triumphant exultation, no revenge-completed tableau. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the last autumn light of the day is the only light, and it withdraws evenly as the episode closes — the ridge pales by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the grey's own depth, no milky flat darkness.

Recreate the first 2 panels in order as one continuous ~10 second sequence (the sheet's third and fourth panels — the complete black hold and the red next-episode title card — are edit-stage reference only and are NOT rendered):
1. 35mm wide: the autumn mountain grave in the last light — the figure small and far now, walking away down the ridge path.
2. 35mm wide: the ridge emptying — the stone alone with the autumn trees, the light lowering evenly.

EVENING MOTION — IMPORTANT: physically-based the even leaving of the light — the episode closes as landscape and not as statement: the small figure walks away down the ridge path without looking back, the stone stays alone with the thinning trees, and the last autumn light lowers evenly off the valley; no finale fanfare, no 'the end' mood, no aftermath tableau; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP91 원장 완결. 콘티 시트 8종(`downloads/EP91_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제92화 「풀려난 이름들」 —**
