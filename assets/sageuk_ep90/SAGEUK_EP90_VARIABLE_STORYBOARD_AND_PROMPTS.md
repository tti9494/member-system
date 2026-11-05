# 「혈화의 궐」 EP90 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제90화 「성군의 첫 법도」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제90화 「성군의 첫 법도」` 절, 원전: 제90장 정본) + `characters.md` 캐릭터 앵커(이환, 이설화 — 이환 25세·설화 Neural2-A 0.0은 plan 우선 원칙 채택) + EP22~EP89 원장 템플릿(동일 규격)
> **범위**: EP90 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP89 S8 엔드카드 「제90화 성군의 첫 법도에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 50mm, 전쟁 뒤 첫 조정 — 세 가지 법도 [내레이션/Wavenet-C (0.0): "첫째 — 가져온 종이는 어전에서 읽는다." (rel 3.5=절대 2.5)], S2 100mm Macro · 민원 종이, 십 년 동안 죽어 있던 종이의 길이 다시 삶 [내레이션/Wavenet-C (0.0): "둘째 — 어전에서 읽은 종이는, 반드시 답을 한다." (rel 3.5=절대 9.5)], S3 85mm, 셋째 — 스스로 지키기 어려운 법도 [이환/Neural2-C (-1.5): "셋째 — 임금의 조서는, 두 번 쓰이지 않는다." (rel 3.0=절대 16.5)], S4 85mm, 설화의 경계로서의 축하 [설화/Neural2-A (0.0): "폐하께서는 폐하의 아버지의 조서로부터 이 나라를 구하셨나이다. 이제 폐하의 조서가 — 폐하의 아버지가 되지 않기를, 저도 기도하옵니다." (rel 5.5=절대 24.5)], S5 85mm, 왕의 웃음 — 임금의 웃음이 아니라 [이환/Neural2-C (-1.5): "…" (웃음 — 왕의 웃음이 아닌)], S6 50mm, 새벽 전에 꺼지는 등불 [내레이션/Wavenet-C (0.0): "사경을 넘긴 왕의 — 첫 번째 편안한 밤이었다." (rel 4.0=절대 39.5)], S7 24mm 와이드, 편안해진 대전의 밤 (무대사), S8 35mm → 엔드카드, 꺼진 등불 → 암전 → 타이틀(자막: 제91화 「사헌부의 눈」에서 계속).
> **안티슬롭 ① — 치세 찬양 극 배제(plan·정본 안티슬롭 지정)**: 법도 세 개의 낭독 장면·치세 찬양 나레이션 승리 테이블로·환호하는 신하 군중 렌더 **0건**. 치환 — **종이가 백성에게서 어전으로, 어전에서 답이 되어 다시 백성에게 나가는 살아 움직이는 그림**(S1 개장 3비트 · S2 종이의 길 6비트 단독 최장): 법도는 낭송되는 것이 아니라 종이의 이동으로 지켜진다. `no golden-age praise, no cheering, no triumph tableau` 전 썬 상설.
> **안티슬롭 ② — 설화의 축하 고양 배제(plan·정본 안티슬롭 지정)**: 축하 낭찬·환희 고양·경사 테이블로 렌더 **0건**. 치환 — **"폐하의 조서가, 폐하의 아버지가 되지 않기를" — 경계로서의 축하, 파수꾼의 서약**(S4 5비트): 축하가 곧 경계인 대사이며, 얼굴에는 진실함과 단호함만 남는다. `no celebration exaltation, no delight tableau` 전 썬 상설.
> **S3 셋째 법도(plan·정본 지정)**: "임금의 조서는 두 번 쓰이지 않는다" — 군왕의 무거운 자기 규율. 폐문 뒤 홀로 남은 왕이 스스로의 조서에 스스로 묶이는 그림 — 붓을 내려놓는 손이 법도의 본체다. `never written twice` 가드.
> **S5 왕의 웃음(plan·정본 지정)**: 임금의 위엄 있는 웃음이 아니라 **스물다섯 청년 이환의 편안하고 맑은 웃음** — 눈부터 웃고 고개가 한 번 숙기며 어깨가 늘어진다. `no solemn royal laugh, no raised chin, no performed majesty` 가드. 웃음 소리는 편집 단계 후시 — 렌더 무음.
> **S6 등불(plan·정본 지정)**: **새벽 전에 꺼지는 대전의 등불** — 사경을 넘긴 왕의 첫 번째 편안한 밤. 등불이 제 연료를 다 써서 스러지듯 꺼지는 풍경이 종지다. S7 — 편안해진 대전의 밤 24mm 와이드 1컷 절제. S8 — 꺼진 등불의 재 → 균일 암전.
> **백지 설계 교칙(전편 규격)**: 프레임 내 기물 위 가독 글자 **0건**. **민원 종이·조서는 줄선 낱행 라인일 뿐** — 법도·민원의 글자는 전부 라인과 공란으로만 표현된다. **법도 3문장은 편집 단계 자막 삽입(정본 AG ①)** — 시트와 렌더에 절대 낭독 활자를 그리지 않는다. `no letterforms, no hangul, no hanja` 전 썬 상설. **본화 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기입된다.
> **문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계 참조용)뿐**(본화는 가독 허용 인서트 없음). 엔드카드 자막(제91화 「사헌부의 눈」에서 계속)은 편집 단계 삽입, S08 렌더는 암전으로 끝난다.
> **세이프티 가드(plan 절대 준수) — 유혈 직결 어휘 0건**: `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. 금지 어휘(`poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder`)와 참견 어휘(`slash`·`stab`·`execution`·`kill` 등)는 생성기 `validate()`로 전수 차단 확인 — **어간 부분 문자열도 차단된다**(EP66 실측 계승). 정본 대사 원문은 SRT·보이스 원장에만 기재된다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이환 — **곤룡포 차림, 왕관의 무거운 허세를 벗고 스스로 자기 규율을 세우는 군왕, 스물다섯의 편안한 미소**(25세 — characters.md 24세 대신 **plan 우선 원칙으로 본화 채택**, 원장에 병기; S1 첫 조정·S3 셋째 법도·S4 수취·S5 웃음·S6 수면). 이설화 — **궁녀/사관 복식, 소박한 옥비녀, 왕에게 경계로서의 축하를 올리는 진실하고 단호한 눈빛**(21세 — characters.md 다크 파스텔 궁녀 한복·서늘하고 총명한 눈빛·옥비녀 앵커 준수; S4 축하 5비트). 조정의 관원은 **원경의 작고 흐릿한 배경 인물로 한정** — 개별 인물 조명·군중 환호 렌더 0건. 무결·윤경헌·중전: 본화 등장 0건. **인물 상한** — S01 이환 1인+배경 관원(원경, 무개별 조명), S02 이환의 손 1회+운반인 1인(후모), S03 이환 1인, S04 최대 2인(설화·이환), S05 최대 2인(이환·설화), S06 이환 1인(수면), S07 무인물, S08 인물 0명(초점 밖 실루엣 1인).
> **입모양 배제(100화 전편 규격)** — 내레이션 3구(S1·S2·S6) + 이환 대사 1구(S3) + 설화 대사 1구(S4) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S5의 웃음은 음성 원장 대상 대사가 아니므로 렌더는 무음(웃음 소리는 편집 단계 후시). S7·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 본화 `ko-KR-Wavenet-C`는 **내레이션(0.0) 3구(S1·S2·S6) 단독** — 무결 `Wavenet-C`(-1.5)·뱃사공(-2.0)·금군(-1.0) 등 타 Wavenet-C 배역 **본화 등장 0건**, 동일 ID 공존 없음. 이환 `ko-KR-Neural2-C`(-1.5 — plan 확정치, characters.md -0.5 대신 plan 우선 원칙) S3 1구·설화 `ko-KR-Neural2-A`(0.0 — plan 확정치, characters.md -1.0 대신 plan 우선 원칙) S4 1구 — 각각 본화 단독, 사다리 충돌 없음. 단, characters.md 등록 타 Neural2-C/A 배역과의 전적 대조를 병기하며 **본화 내 등장 0건**이라 실충돌 없음. 파일명: `EP90_S1_NARRATION` / `EP90_S2_NARRATION` / `EP90_S3_KING` / `EP90_S4_SEOLHWA` / `EP90_S6_NARRATION`. 렌더는 전 썬 무음.
> **가변 컷 배분**: 3/6/4/5/3/3/1/3 = 28컷 — EP13~EP89 전 배분(101종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP89 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP89분 3/4/7/3/4/3/1/3과도 상이). **S2(종이의 길) 6컷 단독 최장** — 본화 안티슬롭 치환의 본체(낭독이 아니라 종이가 움직이는 그림). S4(경계로서의 축하) 5컷, S3(셋째 법도) 4컷, S1(첫 조정)·S5(웃음)·S6(등불) 각 3컷, **S7(대전의 밤, 무대사) 1컷 절제**, S8(등불→암전→타이틀) 3컷 — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 9회(초벌 8 + 재렌더 1) 중 최종 채택 8장 — **재렌더 1건은 S03(초벌 메타바 "DIRECTOR: ÁRSEN" 악센트 오타 → 재렌더로 해소, 결함본 `downloads/qc_crops/Z_EP90_S03_DEFECT_1ST_ÁRSEN.jpg` 보존)**. 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**(정규화 필요 0건). 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.14%(적색 타이틀 — 좌표 확인, 타이틀 열 x387~411·y903~1233 한정 — 의도 채색). 생성기 `validate()`(컷수·배분 중복 101종 대조·세이프 어휘·cheering/praise/triumph/exaltation/never-written-twice/young-laugh/letterform/light/lips/no-body 가드) → 렌더 → PIL 전량 실측 → **8장 전량 육안 검독 + 확대 크롭 검독(S08 타이틀 13슬롯 3분할 3배율 크롭 `downloads/qc_crops/Z_EP90_S08_TITLE_3X_TOP.png`·`Z_EP90_S08_TITLE_3X_MID.png`·`Z_EP90_S08_TITLE_3X_BOTTOM.png`, 전장 메타바 DIRECTOR 표기 3배율 크롭 8종 `downloads/qc_crops/Z_EP90_S0x_META_DIRECTOR_3X.png`)**.
> **검독 운영 교훈(EP67~EP89 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전 첨부를 돌려줄 수 있다** — 재렌더 시 PIL 실측 + md5 해시 대조 + 별도 크롭 경로 재열람으로 판정할 것(본화 S03 재렌더 시 md5 03ea652ecb08→8eb8cca92d55 대조로 신규본 판정 — 재렌더 후 메타바 크롭 재검독 실행). **어간 부분 문자열 함정 계승** — `steadying`이 금지 어휘 `dying`을, `stable`이 참견 어휘 `stab`을 포함해 생성기 validate()가 차단 — 본화 설계 단계에서 회피 어휘로 기술(EP66·EP87·EP88 계승 가드 유효 재확인). **본화 신규 함정**: 법도 3문장을 시트에 새길 수 없으므로 종이 이동의 그림으로 치환 — `blank ruled lines` 가드 통과 및 육안 렌더 확인.
> **plan 기재 대사·슬롯 최종성 확인(팩트체크)**: plan 기재 S08 타이틀 슬롯 수 "12슬롯"은 **기계 대조 결과 정정 — 실제 글자수 13자**(제/9/1/화/사/헌/부/의/눈/에/서/계/속)이며, EP73~EP89 확립 **1자 1슬롯 원칙에 따라 13슬롯** 확정(plan 기재 "12슬롯"은 글자수 오차 — 공백 슬롯 삽입 없음, 숫자 9·1은 각각 단독 슬롯 — 확대 크롭 검독 통과, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). 정본 대사·보이스 ID·rel/절대 수치는 `SEASON_04_MASTER_SCREENPLAY.md` 제90화 절(273~283행) 직접 열람 재대조 — plan과 1:1 일치. **보이스 P 보정 병기**: characters.md는 이환 Neural2-C -0.5·설화 Neural2-A -1.0을 표기하나, plan 확정치(이환 -1.5·설화 0.0)를 본화에 채택 — plan 우선 원칙. **이환 연령**: characters.md 24세 대신 plan 기재 25세를 본화 채택 — plan 우선 원칙. **plan 배분 기재 "선행 전 배분 101종 미중복"과 실측 101종 일치** — 기계 스캔 수치가 우선.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep90_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep90_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 이환 붉은 곤룡포, 설화 다크 파스텔 궁녀 한복, 전쟁 뒤 첫 아침빛, 대전 등불의 실제 불빛이 실제 색으로 복원된다. **붉은 색은 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **전쟁 뒤 첫 조정과 기다리는 종이**(the quiet assembly, the waiting paper), S2 **십 년 만에 다시 사는 종이의 길**(the waking paper, the road of the paper), S3 **내려놓는 붓과 스스로 묶이는 왕**(the brush put down, the self-bound king), S4 **축하 안의 파수꾼의 눈**(the guard inside the congratulation), S5 **스물다섯의 웃음의 물리**(the young laugh, the easing shoulders), S6 **새벽 전에 스러지는 등불**(the lamp spending itself), S7 **달빛에 잠든 마당**(the moonlit stillness), S8 **꺼진 등불과 균일한 어둠**(the cold lamp, the even darkening).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no blood, no wound, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. `no letterforms, no hangul, no hanja` 전 썬 상설. **민원 종이·조서는 줄선 낱행과 공란으로만** — 가독 글자 렌더 0건. 법도 3문장은 편집 단계 자막 삽입, 엔드카드 자막(제91화 「사헌부의 눈」에서 계속)도 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 3구(S1·S2·S6)와 캐릭터 대사 2구(S3 이환·S4 설화)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S5의 웃음 소리는 편집 단계 후시, S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이환(plan 우선 원칙 — 본화 25세)**: the king, Ihwan — a young 25-year-old Korean king in a dragon-embroidered royal robe rendered as grey graphite values, his plain black headpiece worn lightly and without ceremony, an easy self-governed young ruler with calm clear eyes, the heavy pretence of the crown set aside, lips closed.
   - **이설화(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold intelligent eyes, true and resolute, lips closed.
   - **인물 상한**: S01 이환 1인+배경 관원(원경·무개별 조명), S02 손 1회+운반인 1인(후모), S03 이환 1인, S04 최대 2인, S05 최대 2인, S06 이환 1인(수면), S07 무인물, S08 인물 0명 — 군중 환호·개별 관원 조명 렌더 0건.
9. **광원 표기**: S1~S5 — **전쟁이 끝난 뒤 첫 날의 맑은 아침 빛이 어전의 높은 열창으로 들어오는 것**이 유일한 광원(씬별 각도·평면도 변주 분리 유지). S6 — **대전 안쪽 침전의 등불 하나의 작고 따뜻한 불빛**. S7 — **마당 돌 위에 눕는 달빛**. S8 — 꺼진 등불의 재와 새벽 전의 마지막 찬 회색빛 → 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설(등불은 불꽃의 자연한 호흡만 명시). **EP89 중궁전 격창 가드를 본화 어전 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지(EP78 밤 등불 가드와 동일 원칙).
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 꺼진 등불·균일 암전 구간 이후의 붉은 타이틀(제91화 「사헌부의 눈」에서 계속, 13슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S2·S6 3구. 이환 `ko-KR-Neural2-C` (Pitch -1.5 — plan 확정치, Speed 1.0, 무거운 자기 규율 톤) — S3 1구. 설화 `ko-KR-Neural2-A` (Pitch 0.0 — plan 확정치, Speed 1.0, 서늘한 경계의 축하 톤) — S4 1구. **본화 Wavenet-C는 내레이션 단독 — 동일 ID 공존 없음**(타 Wavenet-C 배역 본화 등장 0건). 본화 내레이션 3구 + 캐릭터 대사 2구 + 엔드카드 자막 1건. **무결·윤경헌·중전 대사 0구** — 본화는 이환과 설화의 회차다. S5의 웃음 소리는 편집 단계 후시, S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 3구 — **단독 ID, 타 배역 공존 없음** · 이환 `Neural2-C`(-1.5) 1구·설화 `Neural2-A`(0.0) 1구 — 상이 모델, 사다리 충돌 없음. 파일명 분리 규칙 기재(`EP90_S1_NARRATION`/`EP90_S2_NARRATION`/`EP90_S3_KING`/`EP90_S4_SEOLHWA`/`EP90_S6_NARRATION`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 3/6/4/5/3/3/1/3 = 28컷 — EP13~EP89 전 배분 101종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S2 6컷 단독 최장**(종이의 길), S4 5컷, S3 4컷, S1·S5·S6 각 3컷, **S7 1컷 절제**(대전의 밤), S8 3컷 — "3컷·4컷 고정" 슬롭 회피.
16. **법도는 낭독이 아니라 이동이다(본화 핵심)**: 본화에는 낭독도 찬양도 환호도 축하 고양도 없다 — 법도 세 개는 종이가 백성에게서 어전으로, 어전에서 답이 되어 나가는 살아 움직이는 그림으로만 존재하고, 설화의 축하는 파수꾼의 서약이며, 왕의 웃음은 스물다섯 청년의 것, 밤은 등불이 제 연료를 다 쓰는 것으로 닫힌다. 전 썬 `no golden-age praise, no cheering, no triumph tableau, no celebration exaltation` 상설. 종식(S7~S8)은 대사가 아니라 풍경이다 — 잠든 마당의 달빛, 꺼진 등불, 균일한 어둠.

---

## 1. S01 첫째 — 전쟁 뒤 첫 조정 (절대 00.0~07.5 · 콘티 3컷)

- **시트**: `downloads/EP90_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 어전. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "첫째 — 가져온 종이는 어전에서 읽는다." (rel 3.5=절대 2.5, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 3비트)** — 전쟁 뒤 첫 조정의 홀(1) — 백성에게서 가져온 종이가 독서 안에 쌓여 기다림(2) — 왕관의 허세를 벗고 경청하는 젊은 왕(3). **안티슬롭 가드(plan 지정)** — 치세 찬양·환호·승리 테이블로 0건 — 법도는 낭송이 아니라 종이 논리로 시작된다. 관원은 원경 배경 인물.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person in focus only: the king, Ihwan — a young 25-year-old Korean king in a dragon-embroidered royal robe, his plain black headpiece worn lightly and without ceremony, an easy self-governed young ruler with calm clear eyes, the heavy pretence of the crown set aside, listening unhurried at the throne; the rows of officials stay far from the throne and out of focus as distant background figures with no individual lighting, no cheering, no applause, no triumph tableau, no golden-age praise. The papers on the reading desk show only blank ruled lines and never readable characters. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the clear morning light of the first day after the war entering the throne hall's high open windows is the only light, laying long pale bands across the wooden floor and the paper stack. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm wide: the first court assembly after the war — the great hall at morning, the rows of officials standing quiet and small and far from the throne, no cheering, no triumph.
2. 50mm medium: the low reading desk before the throne — the papers brought in from the people lying in a plain stack, waiting to be read at the throne.
3. 50mm medium: the young king at the throne — listening, unhurried, a ruler setting his own discipline.

ASSEMBLY MOTION — IMPORTANT: physically-based the quiet assembly, the waiting paper — the hall is simply at work again: the officials stand still and quiet at their distance, the paper stack waits on the reading desk with its blank ruled lines untouched, and the young king listens with the unhurried stillness of a ruler setting his own discipline and not a conqueror taking his reward; no golden-age praise, no cheering, no triumph tableau; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 십 년 만에 다시 사는 종이 (절대 07.5~15.0 · 콘티 6컷 ★ 최장)

- **시트**: `downloads/EP90_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 민원 종이. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "둘째 — 어전에서 읽은 종이는, 반드시 답을 한다." (rel 3.5=절대 9.5, 사후 믹싱)
- **연출 특이**: **본화의 본체(가변 6컷 단독 최장)** — 십 년 동안 접혀 죽어 있던 민원 종이(1) — 펼쳐지고 새 줄이 놓이는 종이(2) — 긴 복도로 어전으로 향하는 종이의 길(3) — 읽은 종이를 왕의 손이 직접 가른 바(4) — 답이 같은 종이의 뒷면에 놓임(5) — 대문으로 다시 나가는 종이의 길(6). **안티슬롭 가드(plan 지정)** — 낭독·문서 매크로 연타 회피(정본 AG ①) — 종이가 움직이는 살아 있는 그림이다. 종이는 전부 공란 줄선 라인뿐.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no face in focus at any point: only the king's own hand setting one read sheet apart from the stack, and one pair of plain sleeves carrying a tray of the people's sheets down the corridor with the bearer's face never shown; no cheering, no crowd, no waiting officials in focus. The petition sheets show only blank ruled lines and never readable characters, and the paper is never torn and never struck out. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the clear morning light of the first day after the war entering the hall's high open windows is the only light, catching the worn folds of the paper and the long corridor's wooden pillars. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 6 panels in order as one continuous ~10 second sequence:
1. 100mm macro: a plain petition sheet that has lain folded and untouched for ten years — its folds worn soft, its surface only blank ruled lines.
2. 100mm macro: the same sheet opened flat at a low desk — a brush laying one fresh ruled line along its fold, the paper breathing again.
3. 50mm medium: the road of the paper — a plain tray of the people's sheets carried down the long corridor toward the throne, the bearer's face not shown.
4. 50mm medium: at the throne — the king's own hand setting one read sheet apart from the stack, the read apart from the unread.
5. 100mm macro: the answer — a fresh ruled line laid on the back of the worn sheet, the reply riding the same paper home.
6. 50mm wide: the road back out — the answered sheets leaving through the great gate, the paper's road going home the way it came.

PAPER MOTION — IMPORTANT: physically-based the waking paper, the road of the paper — ten years of stillness ending in one morning: the worn folds open with the soft resistance of real paper, the brush lays a fresh line without hurry, the tray travels the corridor at a walking pace, the king's own fingers set the read sheet apart, the answer rides the same sheet's back, and the answered paper leaves through the great gate the way it came; no recitation scene, no montage of documents, no hands tearing or striking out anything; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 스스로 지키기 어려운 법도 (절대 15.0~22.5 · 콘티 4컷)

- **시트**: `downloads/EP90_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [무거운 자기 규율 · 이환/`ko-KR-Neural2-C`, Pitch -1.5 — plan 확정치, Speed 1.0] "셋째 — 임금의 조서는, 두 번 쓰이지 않는다." (rel 3.0=절대 16.5, 사후 믹싱)
- **연출 특이**: **자기 규율 썬(가변 4비트)** — 비워진 홀에서 홀로 남은 왕(1) — 왕의 손이 직접 내려놓는 왕의 붓(2) — 전쟁보다 무거운 자기 통치의 얼굴(3) — 스스로의 법도에 묶이는 젊은 군왕(4). **안티슬롭 가드(plan 지정)** — 위엄 포즈·군주 숭고 테이블로 0건 — 법도의 무게는 붓을 내려놓는 손에 있다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person only: the king, Ihwan — a young 25-year-old Korean king in a dragon-embroidered royal robe, his plain black headpiece worn lightly and without ceremony, an easy self-governed young ruler with calm clear eyes, alone at the reading desk after the court has emptied; no attendant, no guard, no second person anywhere in frame. The royal paper before him shows only blank ruled lines and never readable characters, and it is never written on twice. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the clear morning light now lying flat across the emptied hall is the only light, holding the king and the reading desk in one even band. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the king alone at the reading desk after the court has emptied — the third law before him, the hardest because he alone must keep it.
2. 85mm close: the king's own hand putting down the royal brush — a royal edict never written twice, his own decree bound by his own hand.
3. 85mm close: his face — the weight of a king governing himself, heavier than governing the war.
4. 85mm medium: he straightens, easy in his self-discipline — a young ruler who has set his own law and means to keep it.

DISCIPLINE MOTION — IMPORTANT: physically-based the brush put down, the self-bound king — the law binds the lawmaker: the court has drained away and he stays, his own fingers lay the royal brush down on the desk with quiet finality, the weight of governing himself settles on his face a moment longer than any war ever pressed, and then he straightens, easy, a young ruler who means to keep the law he has just set; no solemn throne pose, no performed majesty, no audience watching; his line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 경계로서의 축하 (절대 22.5~30.0 · 콘티 5컷)

- **시트**: `downloads/EP90_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 경계 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "폐하께서는 폐하의 아버지의 조서로부터 이 나라를 구하셨나이다. 이제 폐하의 조서가 — 폐하의 아버지가 되지 않기를, 저도 기도하옵니다." (rel 5.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **축하=경계 썬(가변 5비트)** — 예를 갖춘 거리에서 선 설화(1) — 번지지 않는 정확한 절(2) — 파수꾼의 경계가 들어 있는 눈(3) — 축하 속의 경계를 알아듣는 왕(4) — 파수꾼의 서약인 축하로 끝나는 두 사람(5). **안티슬롭 가드(plan 지정)** — 축하 고양·환희 테이블로 0건 — 축하는 축하이면서 경계다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly two people in the whole scene: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, cold intelligent eyes, true and resolute — offering congratulation that carries a watchman's warning; and the king, Ihwan — a young 25-year-old Korean king in a dragon-embroidered royal robe, his plain black headpiece worn lightly, hearing the warning inside the congratulation; no third person, no attendants, no crowd. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same clear morning light holding both faces in one pale band is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the court lady Seolhwa standing before the king at a respectful distance — neat court-lady dress, the jade hairpin, true and resolute eyes.
2. 85mm close: her bow — exact and without flourish, the congratulation carried as duty.
3. 85mm close: her eyes lifted to the king — the congratulation in them and the watchman's guard inside it.
4. 85mm close: the king receiving it — hearing the warning inside the congratulation.
5. 85mm medium: the two in the quiet hall — a servant's congratulation that is really a watchman's oath.

GUARD MOTION — IMPORTANT: physically-based the guard inside the congratulation — the congratulation and the warning are one speech: she bows once, exact and without flourish, her eyes come up true and resolute with the watchman's guard inside them, the king receives the words and they land where they were meant to land, and the two hold the distance of trust in the quiet hall; no celebration exaltation, no delight tableau, no clapping, no flowers, no raised cups; her line arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 왕의 웃음, 임금의 웃음이 아니라 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP90_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [스물다섯의 웃음 · 이환/`ko-KR-Neural2-C`, Pitch -1.5 — plan 확정치] "…" (웃음 — 왕의 웃음이 아닌; 웃음 소리는 편집 단계 후시, 렌더 무음)
- **연출 특이**: **웃음 썬(가변 3비트)** — 미끄러지는 군주의 가면(1) — 눈부터 웃고 고개가 숙겨지는 스물다섯의 웃음(2) — 한 호흡만 스물다섯인 왕의 홀(3). **안티슬롭 가드(plan 지정)** — 위엄 있는 임금의 웃음·턱 들어 올린 제왕적 웃음 0건 — 사실을 지켜준 자신의 하인에게 웃는 젊은이의 웃음이다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly two people in the whole scene: the king, Ihwan — a young 25-year-old Korean king in a dragon-embroidered royal robe, his plain black headpiece worn lightly, a young man laughing easily in his own hall; and the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok with a simple jade hairpin, steady at her distance; no officials, no attendants, no third person. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same clear morning light, warmer now as it climbs, is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close: the king's face — the formal mask slipping, something easier arriving behind it.
2. 85mm close: a young twenty-five-year-old's easy clear laugh taking him — the eyes first, then the head dipping, the shoulders easing; no solemn royal laugh, no raised chin.
3. 85mm medium: the laugh passing — the hall quiet and easy around a young king who is, for one breath, only twenty-five.

LAUGH MOTION — IMPORTANT: physically-based the young laugh, the easing shoulders — the laugh arrives in real stages: the throne's solemnity loosens at the shoulders first, the eyes crinkle before the sound would come, the head dips once and the shoulders settle, and the hall sits easy around a king who for one breath is only twenty-five and nothing else; no solemn royal laugh, no raised chin, no performed majesty, no court joining in; the laugh's sound arrives later in the edit — the render is fully silent, lips closed throughout. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 새벽 전에 꺼지는 등불 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP90_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm · 침전. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "사경을 넘긴 왕의 — 첫 번째 편안한 밤이었다." (rel 4.0=절대 39.5, 사후 믹싱)
- **연출 특이**: **첫 편안한 밤 썬(가변 3비트)** — 사경을 넘겨 자는 왕(1) — 낮아지는 등불의 불꽃(2) — 새벽 전에 제 연료를 다 써서 꺼지는 불꽃과 가는 연기(3). **안티슬롭 가드** — 불면의 왕·밤샘 순정 테이블로 0건 — 편안함이 결함이 아니라 결말이다. 등불의 불꽃은 자연한 호흡만.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — one person only, asleep: the king, Ihwan — a young 25-year-old Korean king past the deepest hour of the night, sleeping his first easy night, the dragon robe laid over him as a cover and the headpiece set aside on the stand, his breathing even and slow, lips closed; no attendant, no guard, no second person. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the single oil lamp's small warm glow in the inner bedchamber is the only light, breathing with the flame's natural quiet rhythm and never flickering like horror, never strobing. No crushed blacks beyond the lamp glow's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the king asleep in the inner hall — a young ruler past the deepest hour of the night, sleeping his first easy night.
2. 50mm close: the oil lamp's small flame lowering in the lamp — the night watch burning down toward dawn.
3. 50mm close: the flame going out — a thin straight thread of smoke rising, the lamp out before dawn.

LAMP MOTION — IMPORTANT: physically-based the lamp spending itself, the even sleep — the night closes by itself: the young king's chest rises and falls in slow even breathing, the oil lamp's small flame lowers by degrees as its fuel thins, and it goes out of its own spending before dawn, leaving one thin straight thread of smoke rising from the wick; no hand enters the frame, no wind, no ember drama, no last flicker theatrics; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 편안해진 대전의 밤 (절대 45.0~52.5 · 콘티 1컷 절제)

- **시트**: `downloads/EP90_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드. 무대사 — 렌더 완전 무음.
- **연출 특이**: **절제 썬(가변 1컷)** — 종이 판문 뒤 등불이 꺼진 대전, 마당 돌 위에 눕는 달빛, 아무도 없는 궁 — 90부 동안 잠들지 않던 궁이 한 프레임만 자는다. 경비병 배회·불 켜진 창 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in frame at all: only the great hall at night, at ease — the lamp out behind its paper panels, the pale moonlight lying flat on the courtyard stones, no guard pacing, no lamp burning, nothing on watch, the whole palace quiet for the first time in the story; no figure, no hand, no shadow of a person. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the pale moonlight lying on the courtyard stones is the only light, one even silver-grey with no shadow direction. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the moonlight's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence:
1. 24mm wide, static hold: the great hall at night, at ease — the lamp out behind its paper panels, the pale moonlight lying on the courtyard stones, the whole palace quiet for the first time in the story.

STILLNESS MOTION — IMPORTANT: physically-based the moonlit stillness — one held wide frame in which almost nothing happens: the paper panels hold their dark rest, the moonlight lies flat on the stones, a single thin cloud crosses the moon slow enough to be felt rather than seen, and the palace that spent ninety episodes awake is, for one frame, asleep; no guard pacing, no lamp relighting, no figure anywhere; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 꺼진 등불 → 암전 (절대 52.5~60.0 · 콘티 3컷)

- **시트**: `downloads/EP90_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제91화 「사헌부의 눈」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 3컷)** — 인물 초점 0명: 식은 등불과 다 쓴 심지(1) — 완전한 암전(2) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **안티슬롭 가드** — 종반 연출·유품 태블로·에필로그 0건 — 등불이 제 밤을 다 쓰고 화가 조용히 죽는다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in focus at all: only the cold lamp — its wick a thin grey thread above spent oil, no flame anywhere, the smoke thread gone; beyond it, out of focus, the dark shape of the king's easy sleep; no figure in focus, no hand, no shadow of a person. No letterforms, no hangul, no hanja anywhere. All characters are adults. No blood, no wound, no injury anywhere, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the last grey of the night before dawn is the only light, and it withdraws evenly as the episode closes — the lamp's glass pales by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the grey's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence (the sheet's third panel — the red next-episode title card — is edit-stage reference only and is NOT rendered):
1. 35mm close: the cold lamp — its wick a thin grey thread, the oil spent, no flame, the king's easy sleep beyond it out of focus.
2. The frame darkens evenly until nothing remains — complete black, held.

EMBER MOTION — IMPORTANT: physically-based the cold lamp, the even darkening — nothing burns and nothing moves but the light itself leaving: the spent wick holds its thin grey thread, the glass cools by degrees, and as the night's last grey withdraws the frame darkens evenly until the last thing visible is the lamp's faint outline and then nothing; no finale fanfare, no 'the end' mood, no ember relapse; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP90 원장 완결. 콘티 시트 8종(`downloads/EP90_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제91화 「사헌부의 눈」 —**
