# 「혈화의 궐」 EP92 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제92화 「풀려난 이름들」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제92화 「풀려난 이름들」` 절, 원전: 제92장 정본) + `characters.md` 캐릭터 앵커(이설화 — 설화 Neural2-A 0.0은 plan 우선 원칙 채택) + EP22~EP91 원장 템플릿(동일 규격)
> **범위**: EP92 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP91 S8 엔드카드 「제92화 풀려난 이름들에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 35mm · 그 봄, 명단들이 풀려남 [내레이션/Wavenet-C (0.0): "십 년 동안 궐의 어둠 속에서 잊혔던 이름들이 — 하나씩 이름을 얻었다." (rel 4.0=절대 2.5)], S2 100mm Macro · 조서, 복권되는 죄 — 지워지는 죄명 (무대사), S3 50mm, 백일홍 결사대의 끝 [내레이션/Wavenet-C (0.0): "백일홍 결사대는 — 이제 그 목적이 끝나 있었다." (rel 3.0=절대 16.5)], S4 35mm, 일곱 사람이 각자의 길로 [내레이션/Wavenet-C (0.0): "상궁이 된 자는 상궁으로서, 내관이 된 자는 내관으로서, 군졸이 된 자는 군졸로서." (rel 4.0=절대 24.0)], S5 100mm Macro · 목인, 목인이 팔개의 조각으로 갈라짐 [효과음: 나무 갈라짐 (rel 2.0=절대 31.5 — 사후 믹싱)], S6 85mm, "퍼지는 것" [설화/Neural2-A (0.0): "우리는 해체되는 것이 아니라 — 퍼지는 것이옵니다. 뿌리는 — 꽃을 하나만 피우지 않사옵니다." (rel 4.5=절대 39.5)], S7 24mm 와이드, 각자의 곳으로 흩어지는 일곱 그림자 (무대사), S8 35mm → 엔드카드, 흩어진 그림자들 → 암전 → 타이틀(자막: 제93화 「새로운 길」에서 계속).
> **안티슬롭 ① — 해산 통쾌 고양 극 배제(plan·정본 안티슬롭 지정)**: 해산·환호·정산 고양 테이블로·함성 렌더 **0건**. 치환 — **이름이 하나씩 회복되어 명예를 되찾는 조용한 그림의 나열**: 명단이 풀려나고(S1), 조서로 죄명이 지워지고(S2), 결사대의 목적이 조용히 끝나며(S3). `no cheering, no triumphant exultation, no disbanded-toast tableau, no celebration` 전 썬 상설.
> **안티슬롭 ② — "팀은 끝났다" 슬롭 배제(plan·정본 안티슬롭 지정)**: 팀 해산 선언·이별의 눈물·마지막 만찬 무드 렌더 **0건**. 치환 — **"우리는 해체되는 것이 아니라 퍼지는 것이옵니다. 뿌리는 꽃을 하나만 피우지 않사옵니다"라는 단호하고 서늘한 선언**(S6 6비트 단독 최장): 끝이 아니라 확산이다. `no 'the team is over' mood, no farewell weeping, no last-supper tableau` 전 썬 상설.
> **S2 복권 조서 매크로(plan·정본 지정)** — 복권되는 죄, 지워지는 죄명의 조서 매크로. **복권 조서 1줄 한계 엄수(정본 AG ①)** — 조서는 단 한 줄의 복권 기재만, 날짜·관직·죄목 2줄째 0건. 먹 줄로 지워지는 죄명 위에 복권되는 단 한 줄.
> **S5 목인 8조각 매크로(plan·정본 지정)** — 비밀을 간직해 온 백일홍 목인이 여덟 개의 조각으로 **정갈하게** 갈라지는 매크로. **조각 소품 일관성(정본 AG ①)** — `exactly eight (8) pieces` 수 카운트 지문 유지(일곱 사람의 몫과 사헌부의 몫, never seven, never nine). 갈라짐은 맞물린 마디를 따르는 정돈된 분할 — 파괴·격노·내던짐 0건.
> **백지 설계 교칙(전편 규격)**: 프레임 내 기물 위 가독 글자 **0건** — 조서·명단은 줄선 낱행 라인과 공란으로만. **본화에는 EP91식 묘비각 예외도 없다** — 화면 노출 문자는 S08 타이틀(편집 단계 참조용)뿐. **붉은 색은 실사 화면의 백일홍 문양(EP62 선례 — 시트는 흑연 에칭, 실사에서만 적색 채문)과 S08 타이틀뿐**. 엔드카드 자막(제93화 「새로운 길에서 계속」)은 편집 단계 삽입 — 시트에는 편집 참조용 카드로만.
> **무자막 원칙(100화 전편 규격)** — 화면 노출 문자 일체 금지. 내레이션 3구(S1·S3·S4)와 설화 선언 1구(S6)는 편집 단계 사후 믹싱 — 시트와 렌더에 자막 활자를 그리지 않는다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이설화 — **사관/궁녀 복식, 소박한 옥비녀, 결사대원들을 배웅하며 새로운 생명력을 선언하는 결연한 눈빛**(21세 — characters.md 다크 파스텔 궁녀 한복·서늘하고 총명한 눈빛·옥비녀 앵커 준수; S6 선언). 백일홍 결사대원들 — **상궁, 내관, 군졸 등 각자의 본연 복식으로 흩어지는 실루엣**(S3·S4·S6·S7·S8 — **개별 신원·이름·얼굴 클로즈업 렌더 0건**, 그림자·실루엣·뒷모습·원경으로만 처리). 강무결·이환·윤경헌·중전: 본화 등장 0건.
> **입모양 배제(100화 전편 규격)** — 내레이션 3구(S1·S3·S4) + 설화 선언 1구(S6) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S2·S5·S7·S8 무대사 — 렌더 전면 무음. S5 효과음(나무 갈라짐)도 사후 믹싱 — 렌더 무음.
> **동일 보이스 ID 점검(plan 지정)**: 본화 `ko-KR-Wavenet-C`는 **내레이션(0.0) 3구(S1·S3·S4) — 동일 배역 연속이므로 피치 충돌 없음, 단 별도 세션 트랙 지정 합성**. 설화 `ko-KR-Neural2-A`(0.0 — plan 확정치, characters.md -1.0 대신 plan 우선 원칙) S6 1구 — 본화 단독 모델, 사다리 충돌 없음. 무결·이환·윤경헌·중전·금군·뱃사공 대사 0구. 파일명: `EP92_S1_NARRATION` / `EP92_S3_NARRATION` / `EP92_S4_NARRATION` / `EP92_S6_SEOLHWA`. 렌더는 전 썬 무음.
> **가변 컷 배분**: 4/2/5/3/2/6/2/4 = 28컷 — EP13~EP91 전 배분(103종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP91 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP91분 4/2/5/3/3/5/2/4와도 상이). **S6("퍼지는 것"의 선언) 6컷 단독 최장** — 본화 안티슬롭 치환의 본체(해체가 아니라 확산이라는 선언의 완급). S3(결사대의 끝) 5컷, S1(명단이 풀려남)·S8(흩어짐→암전→타이틀) 각 4컷, S4(각자의 본연 복식) 3컷, **S2(복권 조서)·S5(목인 8조각)·S7(일곱 그림자) 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 9회(초벌 8 + 재렌더 1) 중 최종 채택 8장 — **재렌더 1건**: ① S02 초벌(설계 2패널 아래로 이면 씬 미리보기 패널 5개가 추가로 렌더됨 — 시트 자체연장 위반) → **생성기 `build_prompt()`에 전 썬 `EXACTLY N panels` 가드 신설** 후 재렌더 해소(2패널·종결 박스 확인, 이후 화 계승 가드). **정규화 1건**: S07 초벌 1023×1537 → LANCZOS 1024×1536 정규화(EP91 S03 선례 계승). 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.13%(적색 타이틀 — 좌표 확인, 타이틀 열 x387~405·y1062~1281 한정 — 의도 채색). **전장 md5: S01 1a3b1bd7c776 / S02 a8dbd95ba121(재렌더 최종본) / S03 8873a3689a82 / S04 95647f58627f / S05 2bdb854a6d9c / S06 1a20f305ccd2 / S07 aca2b18f1fde(정규화 최종본) / S08 cb6b0e869cb7**.
> **검독 운영 교훈(EP67~EP91 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전 첨부를 돌려줄 수 있다** — 본화 S02 재렌더 후 전장 재열람에서 초벌본과 동일한 첨부가 재반환돼(md5는 변경 확인) **별도 크롭 경로(`downloads/qc_crops/Z_EP92_*`) 재열람으로 현재본 판정**했다. **어간 부분 문자열 함정 계승** — 금지 어휘의 어간 부분 문자열도 생성기 validate()가 차단(EP66 실측). **본화 신규 함정**: 2패널 절제 시트에서 생성기가 남은 면적을 이면 씬 미리보기로 채우는 자체연장 결함 — **`EXACTLY N panels` 전 썬 가드 신설로 해소**(EP91의 n==1 전용 가드를 전 썬으로 확장).
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제92화 「풀려난 이름들」 절(원전: 제92장 정본) 직접 열람**(309행 이하) + 소설 원전 `SEASON_04_COMPLETE_NOVEL_v1.4.md` 제92장 직접 열람 — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. **S08 타이틀 슬롯**: 「제93화 새로운 길에서 계속」 실제 글자수 12자 = 1자 1슬롯 원칙에 따라 **12슬롯** 확정(확대 크롭 검독 통과, 숫자 9·3 각각 단독 슬롯, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). **보이스 P 보정 병기**: characters.md는 설화 Neural2-A -1.0을 표기하나, plan 확정치(설화 0.0)를 본화에 채택 — plan 우선 원칙. **plan 배분 기재 "가변 28컷, 선행 전 배분 103종 미중복"과 실측 103종 일치** — 기계 스캔 수치가 우선.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep92_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep92_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 설화 다크 파스텔 궁녀 한복, 봄 궐의 실제 꽃과 햇살, 흩어지는 일곱 인영이 실제 색으로 복원된다. **붉은 색은 실사 S05 백일홍 문양(EP62 선례)과 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화는 EP91식 묘비각 예외가 없다** — 렌더 프레임 내 가독 문자 일체 0건(조서·명단도 줄선 라인뿐).
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **풀려나는 명단**(the released lists, the paper waking into light), S2 **지워지는 죄명**(the struck line, the dry ink), S3 **풀어지는 어깨**(the unformed standing, the loosened hands), S4 **각자의 자리**(the plain returning, the marching-out), S5 **정갈한 갈라짐**(the fitted seams, the eight pieces), S6 **퍼짐의 선언**(the open palm, the many blooms on split stems), S7 **흩어지는 그림자**(the long shadows, the separating steps), S8 **고르게 물러가는 저녁빛**(the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. 조서·명단은 줄선 낱행과 공란으로만 — 가독 글자 렌더 0건. 엔드카드 자막(제93화 「새로운 길에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 3구(S1·S3·S4)·설화 선언 1구(S6)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S2·S5·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이설화(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, resolved clear eyes declaring a new life as she sees her comrades off, lips closed.
   - **백일홍 결사대원들(plan 지정)**: the seven comrades as shadowed silhouettes and far small figures only — court-lady silhouettes, an eunuch's silhouette, soldiers' silhouettes — faces never shown, no identifiable features, no name, no close-up of any face.
   - **인물 상한**: S01 인물 0명(손 1한정), S02 인물 0명, S03 일곱 실루엣, S04 그림자 인물들(얼굴 비노출), S05 인물 0명(목인 매크로), S06 설화 1인+일곱 실루엣, S07 일곱 그림자 원경, S8 원경 실루엣 → 소실 — 군중·환호 인파 렌더 0건. 강무결·이환·윤경헌·중전 등장 0건.
9. **광원 표기**: S1~S5 — **그 봄의 늦은 아침 햇살이 궐의 처마와 마루에 비치는 것**이 유일한 광원(씬별 각도·면 변주 분리 유지: S1 격자창 투과, S2 종이 위 평평하게 눕는 빛, S3 마루 처마 그늘의 옆빛, S4 마당 개활 평광, S5 사무청 책상 위 한 줄 빛). S6 — 낙화원의 오후 빛이 살 사이로. S7 — 늦은 오후 빛이 일곱 길 위에 긴 그림자로 고르게 내려앉는 것. S8 — 하루의 마지막 저녁빛이 고르게 낮아지다 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설. **EP91 묘소 가을 가드를 본화 궁 봄 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 흩어진 그림자·균일 암전 구간 이후의 붉은 타이틀(제93화 「새로운 길에서 계속」, 12슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S3·S4 3구. 설화 `ko-KR-Neural2-A` (Pitch **0.0** — plan 확정치, characters.md -1.0 대신 plan 우선 원칙, Speed 1.0, 서늘하고 단호한 선언 톤) — S6 1구. 본화 내레이션 3구 + 캐릭터 대사 1구(S6) + 엔드카드 자막 1건. **무결·이환·윤경헌·중전 대사 0구** — 본화는 이름들이 풀려나는 회차다. S2·S5·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 3구 — 동일 배역 연속이므로 피치 사다리 충돌 없음, 단 별도 세션 트랙 지정 합성 병기. 설화 `Neural2-A`(0.0) 1구 — 상이 모델, 단독. 파일명 분리 규칙 기재(`EP92_S1_NARRATION`/`EP92_S3_NARRATION`/`EP92_S4_NARRATION`/`EP92_S6_SEOLHWA`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/2/5/3/2/6/2/4 = 28컷 — EP13~EP91 전 배분 103종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S6 6컷 단독 최장**(선언의 완급), S3 5컷, S1·S8 각 4컷, S4 3컷, **S2·S5·S7 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **해산의 끝은 함성이 아니라 그림의 나열이다(본화 핵심)**: 본화에는 고양도 환호도 해산 선언도 이별 눈물도 없다 — 십 년의 이름이 하나씩 회복되는 조용한 그림의 나열(S1~S2)로 시작해, 결사대의 목적이 말없이 끝나며(S3~S4), 비밀의 목인이 정갈하게 여덟 조각으로 나뉘고(S5), "퍼지는 것"의 선언(S6)이 일곱 그림자의 흩어짐(S7~S8)으로 이어진다. 전 썬 `no cheering, no triumphant exultation, no disbanded-toast tableau, no celebration` 상설. S3·S6 `no 'the team is over' mood, no farewell weeping, no last-supper tableau` 상설. 종식(S8)은 대사가 아니라 풍경이다 — 흩어진 그림자들, 고르게 낮아지는 저녁빛, 균일한 어둠.

---

## 1. S01 첫째 — 그 봄, 명단들이 풀려남 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP92_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "십 년 동안 궐의 어둠 속에서 잊혔던 이름들이 — 하나씩 이름을 얻었다." (rel 4.0=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 4비트)** — 궁 마루에 풀려난 명단들(1) — 궤에서 한 줄 꺼내는 손(2) — 마루에 펼쳐지는 낱행들(3) — 전각 마루에 가로 누운 명단들(4). **안티슬롭 가드(plan 지정)** — 회생 만세·환호 인파 0건 — 이름 회복은 조용한 그림의 나열이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame except one hand and forearm: a quiet Joseon palace hall in spring, long paper lists of names lying released from their storage box on the wooden floor of the hall, morning light through the lattice; one hand drawing one long list out of the box into the light. The list papers show only blank ruled lines and never readable characters. No figure, no face, no crowd, no ceremony, no cheering, no triumphant exultation, no disbanded-toast tableau, no celebration. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late spring morning sun coming through the lattice of the hall is the only light, laying soft bars across the wooden floor and the opened papers. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 35mm wide: a quiet palace hall in that spring — long paper lists of names lying released from their storage box on the wooden floor, morning light through the lattice.
2. 35mm medium: a hand drawing one long list out of the storage box into the light — the ten years of kept names beginning to be given back.
3. 35mm close: the list unrolled flat on the wooden floor — row after row waking into the morning light, each line a name remembered.
4. 35mm wide: the lists spread open across the hall's wooden floor — the darkness of ten years letting go of its names.

LISTS MOTION — IMPORTANT: physically-based the released lists, the paper waking into the light — ten years of names kept in the palace's darkness are returned one by one as a quiet picture-sequence of recovery and not a celebration: the lists slide out of the box with the soft drag of paper on wood, unroll flat with the weight of the roll, and settle in the light bars; the papers show only blank ruled lines and never readable characters; no cheering, no triumphant exultation, no disbanded-toast tableau, no celebration; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 복권되는 죄, 지워지는 죄명 (절대 07.5~15.0 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP92_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 조서. 무대사 — 렌더 완전 무음.
- **연출 특이**: **조서 썬(가변 2비트 절제)** — 먹 줄로 지워지는 죄명이 놓인 복권 조서(1) — 아침빛을 받는 지워진 줄(2). **복권 조서 1줄 한계 엄수(정본 AG ①)** — 날짜·관직·죄목 2줄째 0건. 종이로 죄인이 되었던 자들의 죄가 종이 위에서 지워진다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: only a restoration warrant laid flat on a wooden desk — a single dark ink brush-line drawn through an old written charge, the guilt of those made criminals by paper being wiped away; the warrant carries one short ruled line only: no second line, no dates, no official titles, no charge list, no other lettering anywhere in frame; no figure, no hand, no shadow of a person. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same spring morning light lying flat across the paper is the only light, putting one quiet brightness along the dry ink stroke. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 100mm macro: a restoration warrant laid flat — a single dark ink brush-line drawn through an old written charge, the guilt being wiped away.
2. 100mm macro, slow travel: the struck line under the morning light — a name restored, a crime no longer written anywhere.

WARRANT MOTION — IMPORTANT: physically-based the struck line, the dry ink — the camera travels the warrant's face at macro distance and almost nothing moves: the paper's weave passes, the dry ink of the struck line holds its matte sheen, and the one ruled line of the restoration sits quiet in the grazing light; the warrant carries exactly one short ruled line and no second line, no dates, no official titles, no charge list; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 백일홍 결사대의 끝 (절대 15.0~22.5 · 콘티 5컷)

- **시트**: `downloads/EP92_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "백일홍 결사대는 — 이제 그 목적이 끝나 있었다." (rel 3.0=절대 16.5, 사후 믹싱)
- **연출 특이**: **끝의 썬(가변 5비트)** — 대열 없이 느슨히 선 일곱 사람(1) — 두 사람의 작은 고개 끄덕임(2) — 어깨에 얹히는 짧은 손(3) — 제 힘을 빼는 손들(4) — 하나씩 비워지는 마루(5). **안티슬롭 가드(plan 지정)** — "팀은 끝났다" 무드·이별 눈물·마지막 만찬·해산 만세 0건 — 목적은 조용히 다해서, 사람들은 하루로 돌아간다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly seven figures, shadowed and plain only: the seven comrades standing loosely together on a palace wooden veranda in spring light — no formation, no ranks, no drill, just people whose long purpose has quietly ended; court-lady figures, an eunuch figure, soldier figures in their own plain dress; faces never shown, no identifiable features, no close-up of any face — back views, hats, and shadows only. No farewell weeping, no 'the team is over' mood, no last-supper tableau, no disbanded-toast tableau, no cheering, no triumphant exultation. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring light lying along the veranda's wood is the only light, holding the loose group in one long soft band. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the side light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 50mm wide: the seven comrades standing loosely together on a palace veranda in spring light — no formation, no ranks, just people whose long purpose has quietly ended.
2. 50mm medium: two of the seven exchanging a small nod — the acknowledgment of comrades whose shared purpose is fulfilled.
3. 50mm medium: another resting a hand briefly on a comrade's shoulder — gratitude carried in a touch and not in a speech.
4. 50mm close: their hands loosening at their sides — the tension of ten years quietly leaving the bodies.
5. 50mm wide: the veranda emptying one by one — the purpose ended, the people simply dispersing into the day.

EASING MOTION — IMPORTANT: physically-based the unformed standing, the loosened hands — the company is not mourned and not celebrated, its purpose is simply fulfilled and its people are taken back by the day: the seven stand easy with no formation, a nod passes between two, a hand rests a moment on a shoulder and leaves, fingers open at their sides for the first time without a task, and the veranda empties one by one without speech or salute; no farewell weeping, no 'the team is over' mood, no last-supper tableau, no disbanded-toast tableau, no cheering, no triumphant exultation; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 일곱 사람이 각자의 길로 (절대 22.5~30.0 · 콘티 3컷)

- **시트**: `downloads/EP92_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "상궁이 된 자는 상궁으로서, 내관이 된 자는 내관으로서, 군졸이 된 자는 군졸로서." (rel 4.0=절대 24.0, 사후 믹싱)
- **연출 특이**: **본연의 썬(가변 3비트)** — 자기 자리에 선 상궁(1) — 문서고의 내관(2) — 변경길의 군졸들(3). **안티슬롭 가드** — 임명식·배치 발표·성대한 출발 0건 — 각자의 본연 복식으로 묵묵히 제자리로 돌아간다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — shadowed plain figures only, faces never shown, no identifiable features: a court-lady figure standing at her post in the women's quarters with a folded stack of linens in her arms; an eunuch silhouette standing among tall document shelves with one folded paper in his hands, the papers showing only blank ruled lines; small soldier silhouettes marching out along the north border road in the distance. No triumph, no ceremony, no cheering, no triumphant exultation, no disbanded-toast tableau. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring morning light over the palace and the wide yard is the only light, laying flat even brightness on the quarters, the shelves and the distant road. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 35mm medium: the one who became a senior court lady standing at her post in the women's quarters — serving the palace's women as her own chosen charge.
2. 35mm medium: the one who became a palace eunuch standing among the document shelves — the watcher of papers in his own plain office.
3. 35mm wide: the ones who became soldiers marching out along the north border road in the distance — going out to the frontier as soldiers, each person back inside their own station.

RETURNING MOTION — IMPORTANT: physically-based the plain returning — each person goes back inside their own station and serves it plainly, a court lady as a court lady, an eunuch as an eunuch, a soldier as a soldier: the linen stack settles into its place, the folded paper is laid on the shelf without hurry, and the border road takes the small column of soldiers at a steady marching pace; no triumph, no ceremony, no cheering, no triumphant exultation, no disbanded-toast tableau; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 목인, 팔개의 조각 (절대 30.0~37.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP92_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 목인. 무대사 — [효과음: 나무 갈라짐] (rel 2.0=절대 31.5, 사후 믹싱) — 렌더 완전 무음.
- **연출 특이**: **갈라짐 썬(가변 2비트 절제)** — 천 위의 온전한 목인(1) — 맞물린 마디를 따라 정갈하게 갈라져 놓이는 여덟 조각(2). **조각 소품 일관성(정본 AG ①)** — 정확 여덟 조각(일곱 사람의 몫과 사헌부의 몫), never seven, never nine. 파괴가 아니라 분배다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: only a small carved wooden figure with a zinnia flower pattern resting on a cloth on a wooden desk — the figure that held the secret for ten years, whole for the last time; then the figure coming apart cleanly along its fitted seams — exactly eight (8) pieces, not shattered, not broken in anger, not thrown — seven shares and the inspectorate's share laid out in order on the cloth: count them one by one, one, two, three, four, five, six, seven, eight — never seven pieces, never nine; each piece keeping part of the zinnia flower pattern, a flower motif only, never letters, never rows of glyphs, no legible hangul, no legible hanja, no readable script of any kind. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same spring morning light putting one even line across the desk is the only light, lifting the wood grain and the cloth weave. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the side light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the small carved wooden figure with the zinnia flower pattern resting on a cloth — the figure that held the secret for ten years, whole for the last time.
2. 100mm macro, slow pull: the figure coming apart cleanly along its fitted seams — exactly eight pieces, seven shares and the inspectorate's share, laid out in order.

SPLIT MOTION — IMPORTANT: physically-based the fitted seams, the eight pieces — the split is tidy and deliberate, a secret handed out and not a destruction: the figure halves along its hidden seam with the soft grind of dry wood, the fitted wedges lift apart and are laid out in a neat order on the cloth, each piece carrying its share of the flower pattern, exactly eight pieces never seven never nine; no shattering, no anger, no throwing, no cheering, no triumphant exultation, no disbanded-toast tableau; the wood-crack sound arrives later in the edit and the render is fully silent, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output — the flower pattern on the figure and its pieces is a flower motif only, never letters. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — "퍼지는 것" (절대 37.5~45.0 · 콘티 6컷 ★ 단독 최장)

- **시트**: `downloads/EP92_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 선언 · 설화/`ko-KR-Neural2-A`, Pitch **0.0** — plan 확정치, characters.md -1.0 대신 plan 우선 원칙, Speed 1.0] "우리는 해체되는 것이 아니라 — 퍼지는 것이옵니다. 뿌리는 — 꽃을 하나만 피우지 않사옵니다." (rel 4.5=절대 39.5, 사후 믹싱)
- **연출 특이**: **선언 썬(가변 6비트 단독 최장)** — 일곱 앞에 선 설화(1) — 수평의 눈(2) — 손바닥을 펴서 올리는 손(3) — 발밑의 백일홍 뿌리(4) — 선언을 머금은 얼굴(5) — 제 자리를 받고 돌아서는 일곱(6). **안티슬롭 가드(plan 지정)** — 해산 선언 무드·이별 눈물 0건 — 끝이 아니라 확산의 선언이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one woman in focus: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, resolved clear eyes declaring a new life as she sees her comrades off. Behind and beside her exactly seven comrades as shadowed plain figures only — court-lady figures, an eunuch figure, soldier figures — faces never shown, no identifiable features, no close-up of any face. No farewell weeping, no 'the team is over' mood, no last-supper tableau, no disbanded-toast tableau, no cheering, no triumphant exultation, no applause. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring garden's afternoon light coming through the blossoms is the only light, laying soft moving brightness on her face and hands. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the garden light's own depth, no milky flat darkness.

Recreate the 6 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the court lady Seolhwa standing before the seven comrades in the spring flower garden — the declaration gathering in her, calm and cool.
2. 85mm close: her level eyes on the seven — the sentence about to be said that answers ten years.
3. 85mm close: her open hand turning palm-up — not a dismissal but an offering of ground, roots meant to spread.
4. 85mm medium: a zinnia root-mass in the garden bed at her feet — one plant holding many blooms on its own split stems.
5. 85mm close: her face as the declaration completes — cool, resolute, the new life declared and not mourned.
6. 85mm medium: the seven comrades beginning to turn away — each accepting their own ground, the declaration received with no applause.

DECLARATION MOTION — IMPORTANT: physically-based the open palm, the many blooms on split stems — the sentence carries the scene: we are not being disbanded, we are spreading, and a root never grows into one flower only: she stands calm before the seven, her level eyes rest on them without warmth and without anger, her hand opens palm-up offering ground and not dismissal, the zinnia root-mass at her feet holds many blooms on its own split stems, her face completes the declaration cool and resolute, and the seven accept their own ground and turn away without applause; no farewell weeping, no 'the team is over' mood, no last-supper tableau, no disbanded-toast tableau, no cheering, no triumphant exultation; her line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 각자의 곳으로 흩어지는 일곱 그림자 (절대 45.0~52.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP92_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드. 무대사 — 렌더 완전 무음.
- **연출 특이**: **흩어짐 썬(가변 2비트 절제)** — 정원의 중심에서 일곱 갈래 길로 흩어지는 일곱 그림자의 고찰 와이드(1) — 빠져나가 소일(平常日)로 돌아가는 길들(2). **안티슬롭 가드** — 이별 정창·뒤돌아보는 아쉬움 연출 0건 — 흩어짐이 그 자체로 확산의 완성이다. 긴 여운 와이드.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — seven small shadowed figures only, far and never in focus: a wide high view of a Joseon palace courtyard garden in late afternoon — seven shadowed figures dispersing from the garden's heart along seven separate paths, each toward their own place; long shadows stretching, faces never shown, no identifiable features. No farewell tableau, no cheering, no triumphant exultation, no disbanded-toast tableau. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late afternoon light laying the long shadows across the courtyard is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the evening light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 24mm wide, high: the palace courtyard garden in late afternoon — seven shadowed figures dispersing from the garden's heart along seven separate paths, each toward their own place.
2. 24mm wide: the paths emptying into the ordinary day — the shadows farther apart at every step, the garden keeping only the evening light.

SCATTERING MOTION — IMPORTANT: physically-based the long shadows, the separating steps — the scattering is the point, not a loss but a spreading, held long and quiet: the seven figures walk away from the garden's heart at an unhurried pace, their long shadows thinning as the paths divide, no one looking back, and the paths empty into the ordinary evening of the palace; no farewell tableau, no cheering, no triumphant exultation, no disbanded-toast tableau; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 흩어진 그림자들 → 암전 (절대 52.5~60.0 · 콘티 4컷)

- **시트**: `downloads/EP92_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제93화 「새로운 길」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 4컷)** — 저녁빛 속 멀어진 일곱 그림자(1) — 비워진 정원(2) — 균일 암전(3) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **안티슬롭 가드** — 종반 고양·해산 만세·에필로그 0건 — 사람들은 제 삶으로 퍼지고 빛은 그저 떠난다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — small distant figures only, never in focus: the seven shadows far apart on their separate ways through a Joseon palace courtyard garden in the last evening light, each one walking into their own life, growing smaller until the paths are empty. No finale tableau, no looking back, no cheering, no triumphant exultation, no disbanded-toast tableau. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the last evening light of the day is the only light, and it withdraws evenly as the episode closes — the garden pales by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the grey's own depth, no milky flat darkness.

Recreate the first 2 panels in order as one continuous ~10 second sequence (the sheet's third and fourth panels — the complete black hold and the red next-episode title card — are edit-stage reference only and are NOT rendered):
1. 35mm wide: the courtyard garden in the last evening light — the seven shadows now far apart on their separate ways, small and plain in the wide frame.
2. 35mm wide: the garden emptying — the paths holding no figures now, the evening light lowering evenly.

EVENING MOTION — IMPORTANT: physically-based the even leaving of the light — the episode closes as landscape and not as statement: the seven small figures walk apart on their separate ways without looking back, the paths hold no one, and the last evening light lowers evenly off the garden; no finale fanfare, no 'the end' mood, no aftermath tableau, no cheering, no triumphant exultation, no disbanded-toast tableau; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP92 원장 완결. 콘티 시트 8종(`downloads/EP92_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제93화 「새로운 길」 —**
