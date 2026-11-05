# 「혈화의 궐」 EP94 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-05)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제94화 「낙화원의 봄」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제94화 「낙화원의 봄」` 절, 원전: 제94장 정본) + `characters.md` 캐릭터 앵커(이환 평복 — EP93 신규 앵커 계승, 이설화 사관/궁녀 복식, 강무결 검흔 앵커) + EP22~EP93 원장 템플릿(동일 규격)
> **범위**: EP94 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP93 S8 엔드카드 「제94화 낙화원의 봄에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 24mm 와이드, 만개한 백일홍 — 처음으로 [내레이션/Wavenet-C (0.0): "낙화원의 백일홍은 — 그해 봄에 처음으로 만개했다." (rel 3.0=절대 2.0)], S2 100mm Macro, 하얗게 피었다가 붉게 물드는 꽃 [내레이션/Wavenet-C (0.0): "백일을 피는 꽃이라 그 이름이 붙었고 — 궐의 사람들은 이제야, 왜 그 꽃이 맹세의 문양이 되었는지를 알았다." (rel 5.0=절대 9.5)], S3 50mm, 꽃 아래의 세 사람 (무대사), S4 85mm, 왕의 꿈 이야기 [이환/Neural2-C (-1.5): "과인은 요즘 — 꿈을 꾸지 않는다. 십 년 동안 밤마다 종이의 꿈을 꾸었다. 이제는 — 꽃잎의 꿈을 꾼다." (rel 5.0=절대 24.0)], S5 85mm, 설화의 공로 이동 [설화/Neural2-A (0.0): "그것은 폐하께서 꽃을 심으셨기 때문이옵니다." (rel 2.5=절대 31.5) / 이환/Neural2-C (-1.5): "아니다. 네가 심은 것이다. 과인은 그저 — 그것이 피는 것을 보는 사람이다." (rel 4.0=절대 33.5)], S6 100mm Macro, 세 그림자가 꽃잎 위에 나란히 닿음 (무대사), S7 35mm, 봄의 낮광 (무대사), S8 50mm → 엔드카드, 꽃잎이 바람에 흩어짐(자연 낙하) → 암전 → 타이틀(자막: 제95화 「혈화의 만개」에서 계속).
> **안티슬롭 ① — 봄 낭만 나레이션 난립 배제(plan·정본 안티슬롭 지정)**: 봄 낭만 서정 내레이션 난립·시적 독백 렌더 **0건**. 치환 — **하얗게 피었다가 점차 붉게 물들어가는 백일홍 꽃 하나의 실제 식물 관찰 수준 타임랩스**(S2 5비트): 실제 식물 촬영 수준의 사실성, 꽃잎은 자기 무게로만 움직인다. **꽃 색 전환 소스 명시(정본 AG ①)** — 색은 꽃 자체의 생리로만 옮아간다(the colour shifts by the flower's own living process). `no dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals` 전 썬 상설.
> **안티슬롭 ② — 왕·설화 호감 고양 배제(plan·정본 안티슬롭 지정)**: 로맨스 페이드·설레는 눈빛 교환·호감 고양 렌더 **0건**. 치환 — **"아니다. 네가 심은 것이다. 과인은 그저 — 그것이 피는 것을 보는 사람이다"라는 서로에게 공로를 넘기는 담담하고 평온한 동지적 대화**(S4 6비트·S5 3비트). `no romantic longing gazes, no blushing courtship, no love-theme fade, no romantic exuberance` 전 썬 상설.
> **S6 세 그림자 매크로(plan·정본 지정)** — 떨어진 꽃잎 위에 나란히 드리워진 세 사람의 그림자 매크로(4비트). 그림자는 **사람 형태(머리·몸·다리)**로 나란히 — 나뭇가지 그림자 띠 아님(초벌 결함 재렌더 해소). 세 사람은 프레임 위 어딘가에 서 있을 뿐 화면 노출 0건.
> **S8 자연 낙하(plan·정본 지정)** — 꽃잎이 봄바람에 흩어지는 풍경은 **자연 낙하만**: `natural fall at their own weight, never wind-torn, never swirling, never floating upward` — 부유 연출 절대 금지. → 균일 암전 → 타이틀.
> **백지 설계 교칙(전편 규격)**: 프레임 내 기물 위 가독 글자 **0건** — 본화는 문서·현판·축문 등 노출 문자 요소가 아예 없다. **붉은 색은 S08 타이틀뿐**(시트 유일 의도 채색). 엔드카드 자막(제95화 「혈화의 만개에서 계속」)은 편집 단계 삽입 — 시트에는 편집 참조용 카드로만.
> **무자막 원칙(100화 전편 규격)** — 화면 노출 문자 일체 금지. 내레이션 2구(S1·S2)와 이환 대사 4구(S4 3구·S5 1구)·설화 대사 1구(S5)는 편집 단계 사후 믹싱 — 시트와 렌더에 자막 활자를 그리지 않는다.
> **캐릭터 앵커(plan·characters.md 지정)**: 이환 — **익선관 미착용, 단령/도포 평복, 편안한 청년의 표정**(characters.md 곤룡포·익선관 앵커의 본화 평복 치환 — EP93 평복 앵커 계승, 24세). 이설화 — **사관/궁녀 복식, 소박한 옥비녀**(characters.md 다크 파스텔 궁녀 한복·옥비녀 앵커 준수, 21세·창백한 피부·서늘하고 총명한 눈빛). 강무결 — **정갈한 도포, 뺨의 옅은 검흔**(characters.md 검흔·훤칠한 체격 앵커 준수, 25세). 본화에 관복·익선관·곤룡포 렌더 0건.
> **입모양 배제(100화 전편 규격)** — 내레이션 2구(S1·S2) 전부 무음 렌더 + 사후 믹싱. 이환 대사 4구·설화 대사 1구(S4·S5) — 화면 인물의 입과 무관한 보이스오버·사후 믹싱, 전 썬 `lips closed`. S3·S6·S7·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 본화 `ko-KR-Wavenet-C`는 내레이션(0.0) 2구(S1·S2) — 본화 내 단일 배역, 피치 사다리 충돌 없음. 이환 `Neural2-C`(-1.5 — characters.md 고정치) S4 3구+S5 1구 — 동일 배역 연속, 충돌 없음. 설화 `Neural2-A`(0.0 — plan 확정치, characters.md -1.0 대신 plan 우선 원칙) S5 1구 — 본화 단독 모델. 렌더는 전 썬 무음.
> **가변 컷 배분**: 4/5/2/6/3/4/2/2 = 28컷 — EP13~EP93 전 배분(105종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68 53종)+EP69 배분+EP13~EP93 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP93분 3/5/2/4/3/4/3/4와도 상이). **S4(왕의 꿈 이야기와 공로 이동) 6컷 단독 최장** — 꿈 이야기 3구+설화 정정 1구+이환 반박 1구, 대사 5구가 이루어지는 완급의 본체. S2(백일홍 타임랩스) 5컷 — plan 핵심 치환의 본체. S6(세 그림자 매크로) 4컷, S5(공로 이동) 3컷, S1(개화 선언) 4컷, **S3(꽃 아래 세 사람)·S7(봄의 낮광)·S8(흩어짐→암전→타이틀) 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 14회(초벌 8 + 재렌더 6) 중 최종 채택 8장 — **재렌더 6건**: ① **S07 초벌·2차**(해상도 1023×1537로 1px 이탈 — 1024×1536 규격 위반) → 2회 재렌더 후 1024×1536 정확 해소. ② **S02 초벌 P5**(전장 종지 패널에 나무 아래 인물 3명 렌더 — 타임랩스 관찰 썬 인물 0명 위반) → P5에 `nobody in the frame, no person, no figure, no silhouette` 지문 신설 후 재렌더 해소(인물 0명 확인). ③ **S05 초벌 P2**(이환의 반박 대사 패널 얼굴에 검흔·검은 갓 렌더 — 이환 앵커 위반·무결 오독) → P2에 `NO headwear of any kind, NO scar on his face, hair simply tied back` 앵커 지문 강화 후 재렌더 해소(민머리 평복 청년 확인). ④ **S05 초벌 P3**("둘" 지문에 3인 렌더) → `only the two of them … nobody else in the frame` 지문 신설 후 재렌더 해소(2인 확인). ⑤ **S06 초벌 P3·P4**(세 그림자가 사람 형태가 아닌 나뭇가지 그림자 띠로 렌더) → `three person-shaped human shadows … a head, a body and legs, not tree shadows` 지문 강화 후 재렌더 해소(사람형 그림자 3개 확인). ⑥ **S08 초벌 P1**(종지 풍경 패널에 인물 3명 렌더 — 폐장 풍경 썬 인물 0명 위반) → `nobody in the frame at all` 지문 신설 후 재렌더 해소(빈 정원 확인). 재렌더·초벌 결함 원본은 `images --out` 덮어쓰기로 미보존(실측 수치·크롭으로만 기록). 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.25%(적색 타이틀 — 좌표 확인, 타이틀 열 x390~423·y726~1143 한정 — 의도 채색). **전장 md5: S01 d1567761a69e / S02 3f4648c325d6 / S03 630750fbde5e / S04 cec5a1a28e28 / S05 77bebf0166b0 / S06 c23c2ba0d4f1 / S07 88182121ded6(재렌더 최종본) / S08 4379c3180044(재렌더 최종본)**.
> **검독 운영 교훈(EP67~EP93 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전 첨부를 돌려줄 수 있다** — 본화도 S01·S02 전장 재열람에서 첨부 누락·구버전 반환 발생 — **별도 크롭 경로(`downloads/qc_crops/Z_EP94_*`) 재열람으로 현재본 판정**했다. **어간 부분 문자열 함정 계승** — 금지 어휘의 어간 부분 문자열도 생성기 validate()가 차단(EP66 실측 계승). **본화 신규 함정 2건**: ① **풍경 전용 썬의 인물 침입** — 인물 0명 지문이 없던 S02 P5·S08 P1에 나무 아래 세 사람이 렌더됨 — **인물 0명 지문을 풍경 전용 패널에 명시 기재**로 해소. ② **대사 화자 얼굴의 타배역 오독** — S05 P2 이환의 반박 얼굴에 검흔·갓이 옮아 붙음 — **화자 얼굴 앵커(NO headwear, NO scar)를 패널 지문에 인라인 기재**로 해소. ③ **해상도 1px 이탈(S07)** — 재렌더 후 PIL 전량 재실측 필수 확인.
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제94화 「낙화원의 봄」 절(원전: 제94장 정본) 직접 열람**(345행 이하) — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. **S08 타이틀 슬롯**: 「제95화 혈화의 만개에서 계속」 실제 글자수 13자 = 1자 1슬롯 원칙에 따라 **13슬롯** 확정(확대 크롭 검독 통과, 숫자 9·5 각각 단독 슬롯, **4번째 슬롯 「화」 정자 — ㅘ 모음, 「회」·會 아님**). **보이스 P 보정 병기**: characters.md는 설화 Neural2-A -1.0을 표기하나, plan 확정치(0.0)를 본화에 채택 — plan 우선 원칙. **가변 배분**: plan은 특정 배분 수치를 고정하지 않아 본화 서사에 맞춰 4/5/2/6/3/4/2/2=28컷으로 설계 — **총 컷수 28 규격 준수 + 선행 105종 미중복 기계 스캔**으로 이중 검증.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep94_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep94_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 봄 낙화원(만개한 백일홍), 이환의 평복, 설화의 다크 파스텔 궁녀 한복, 무결의 도포, 흰 꽃잎이 붉게 물드는 색 전환이 실제 색으로 복원된다. **붉은 색은 실사 백일홍의 색 전환과 S08 붉은 타이틀(편집 단계 삽입)뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화는 문서·현판 노출 요소가 아예 없다** — 렌더 프레임 내 가독 문자 일체 0건.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **꽃나무가 자기 꽃을 깨우는 것**(the blossoms at their own weight, the slow push), S2 **꽃 하나의 살아있는 색 전환**(the same one blossom, the tonal deepening across days), S3 **나란히 선 세 사람의 고요**(the even spacing, the still branches), S4 **담담하게 말해지는 꿈**(the settled face, the small calm light), S5 **넘겨지는 공로**(the single head shake, the cool correction), S6 **길어지는 그림자와 가만히 누운 꽃잎**(the low light, the three person-shaped shadows), S7 **가득히 부어대는 낮광**(the even daylight through every blossom, the slow tilt), S8 **꽃잎의 자연 낙하와 물러가는 빛**(the natural fall at their own weight, the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure` 전 썬 상설. `all characters are adults` 전 썬 상설. **정본 대사 원문은 SRT·보이스 원장에만 기재**되고 렌더 프롬프트는 요지의 영문 치환으로 기재된다. **무결의 검흔은 치유된 옛 자국으로만 기술** — 상처·출혈 묘사 0건.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. 본화는 문서·현판·축문 노출이 아예 없다. 엔드카드 자막(제95화 「혈화의 만개에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 2구(S1·S2)·이환 대사 4구(S4 3구·S5 1구)·설화 대사 1구(S5)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S3·S6·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이환 — 평복(plan 지정 본화 앵커)**: the young king Ihwan — a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, a relaxed and unguarded young man's face, quiet warm eyes, lips closed.
   - **이설화 — 사관/궁녀 복식(plan·characters.md 지정)**: the court lady, Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, lips closed.
   - **강무결 — 정갈한 도포(plan·characters.md 지정)**: the warrior Mugyeol in peaceful dress — a 25-year-old Korean man in a clean plain scholar's overcoat, tall and steady, a faint old scar across his cheekbone, a settled calm face at rest, lips closed.
   - **인물 상한**: S01 인물 0명(꽃나무만), S02 인물 0명(꽃 매크로), S03 셋(이환·설화·무결 나란히), S04 이환·설화 2인, S05 이환·설화 2인, S06 인물 0명(사람형 그림자 3개만), S07 인물 0명(빈 정원), S8 인물 0명(빈 정원) → 군중·궁정 인파 렌더 0건.
9. **광원 표기**: S1 — 그 봄의 아침 햇살이 낙화원의 꽃나무 위에 고르게 내려앉는 것. S2 — 같은 봄의 하루 종일의 빛이 꽃 하나 위에 지나가는 것. S3 — 꽃나무 사이로 셋에게 고르게 내려오는 봄의 한낮 빛. S4 — 꽃나무 아래 마주한 둘에게 닿는 부드러운 봄 오후 빛. S5 — 같은 오후 빛이 말하는 얼굴과 꽃 위에. S6 — 낮은 봄 오후 빛이 꽃잎과 그림자 위에 평평하게 눕는 것. S7 — 봄의 낮광이 정원에 가득히 부어대는 것. S8 — 늦은 봄 오후의 빛이 고르게 낮아지다 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설. **EP93 낙화원 가을 혼인 가드를 본화 낙화원 봄 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 꽃잎 자연 낙하·균일 암전 구간 이후의 붉은 타이틀(제95화 「혈화의 만개에서 계속」, 13슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외**).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch 0.0, Speed 0.9, 무거운 나레이션) — S1·S2 2구. 이환 `ko-KR-Neural2-C` (Pitch -1.5, Speed 0.95, 무거운 평온의 꿈 이야기 톤) — S4 3구·S5 1구. 설화 `ko-KR-Neural2-A` (Pitch **0.0** — plan 확정치, characters.md -1.0 대신 plan 우선 원칙, Speed 1.0, 서늘한 정정 톤) — S5 1구. 본화 내레이션 2구 + 캐릭터 대사 5구(S4 3구·S5 2구) + 엔드카드 자막 1건. **무결 대사 0구** — 본화는 꽃의 개화와 왕·설화의 공로 이동으로 이어지는 회차다. S3·S6·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 2구 — 동일 배역 연속이므로 피치 사다리 충돌 없음, 단 별도 세션 트랙 지정 합성 병기. 이환 `Neural2-C`(-1.5) 4구 — 동일 배역 연속, 내레이션과는 상이 모델. 설화 `Neural2-A`(0.0) 1구 — 본화 단독 모델. 파일명 분리 규칙 기재(`EP94_S1_NARRATION`/`EP94_S2_NARRATION`/`EP94_S4_IHWAN`/`EP94_S5_IHWAN`/`EP94_S5_SEOLHWA`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 4/5/2/6/3/4/2/2 = 28컷 — EP13~EP93 전 배분 105종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S4 6컷 단독 최장**(대사 5구의 완급), S2 5컷·S6 4컷·S5 3컷·S1 4컷, **S3·S7·S8 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **봄의 낭만은 낭만이 아니라 관찰이다(본화 핵심)**: 본화에는 서정 내레이션의 난립도 로맨스 고양도 없다 — 꽃나무의 첫 만개(S1)로 시작해, 꽃 하나의 실제 관찰 수준 색 전환 타임랩스(S2)와 꽃 아래 나란히 선 세 사람(S3)으로 이어지며, 왕의 꿈 이야기(S4)와 공로를 서로 넘기는 동지적 대화(S5), 꽃잎 위 세 그림자의 매크로(S6), 봄의 낮광(S7)을 거쳐 꽃잎이 자연 낙하하며 정원이 봄을 보낸다(S8). 전 썬 `no dreamy spring romance reverie, no floating petals defying gravity, no romantic longing gazes, no romantic exuberance` 상설. 봄의 감정은 대사가 아니라 꽃의 색 전환(S2)과 세 그림자(S6)라는 그림이다.

---

## 1. S01 첫째 — 만개한 백일홍, 처음으로 (절대 00.0~07.5 · 콘티 4컷)

- **시트**: `downloads/EP94_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 24mm 와이드 · 낙화원. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "낙화원의 백일홍은 — 그해 봄에 처음으로 만개했다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 4비트)** — 낙화원 고찰 와이드의 첫 만개(1) — 만개한 나무로의 슬로우 푸시(2) — 눈높이 가지의 흰 꽃 만개(3) — 같은 가지의 아직 닫힌 잠들(4). **안티슬롭 가드(plan 지정)** — 봄 낭만 서정 0건 — 실제 식물 관찰의 그림이다. 인물 0명.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in the frame at all: the spring palace garden Nakhwawon and its great zinnia flower tree in full bloom for the first time — no person, no figure, no face, no silhouette, the garden empty. Real plant-observation truthfulness: the blossoms sit at their own weight on the branch, the buds stay closed until their own time. No dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring morning sun settling evenly over the flowering tree is the only light, filling the garden evenly. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the spring light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 24mm wide, high: the spring palace garden Nakhwawon — the great zinnia flower tree in full bloom for the first time, spring morning light over the whole garden.
2. 24mm wide, slow push: the flowering tree — its countless white blossoms dense on every branch.
3. 85mm medium: one branch at eye level — white zinnia blossoms opened wide, the petals freshly spread.
4. 85mm close: buds along the same branch still closed — the tree waking its own flowers one by one.

BLOOM MOTION — IMPORTANT: physically-based the blossoms at their own weight, the slow push — the tree wakes its own flowers one by one in its own time: the high wide view holds the whole garden at once, the slow push closes on the tree without hurry, the branch of white blossoms sways only at its own weight in the cooling morning air, and the closed buds along the same branch wait unopened; a plain botanical observation and nothing more; no dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 하얗게 피었다가 붉게 물드는 꽃 (절대 07.5~15.0 · 콘티 5컷 ★ 타임랩스 본체)

- **시트**: `downloads/EP94_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0, Speed 0.9] "백일을 피는 꽃이라 그 이름이 붙었고 — 궐의 사람들은 이제야, 왜 그 꽃이 맹세의 문양이 되었는지를 알았다." (rel 5.0=절대 9.5, 사후 믹싱)
- **연출 특이**: **타임랩스 썬(가변 5비트 — plan 핵심 치환의 본체)** — 갓 핀 흰 꽃 하나(1) — 꽃잎 가장자리부터 붉게 물드는 물들기(2) — 꽃잎 전체로 건너는 물들기(3) — 아침 이슬이 마르고 물들기 완결(4) — 나무 전체가 저마다의 속도로 물드는 후순(5). **꽃 색 전환 소스 명시(정본 AG ①)** — 색은 꽃 자체의 생리로만 옮아간다. **실제 식물 촬영 수준의 사실성, 부유 절대 금지. 인물 0명.**

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in the frame at all: one single zinnia blossom observed in macro across days — the same one blossom from the same angle in every macro panel, only its colour changing. Real plant-observation truthfulness: the colour shifts by the flower's own living process and by nothing else — white corollas deepening to rose-red across days, the way real zinnias deepen after they open. No person, no figure, no face, no silhouette. No dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals, no time-lapse camera trickery visible — a filmed plant observation. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring day's light passing evenly over the one flower across days is the only light — morning light lying flat across the petals, then afternoon light, then the settling light of later days. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the daylight's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 100mm macro: one white zinnia blossom — freshly opened, its petals the palest white, morning light flat across them.
2. 100mm macro: the same blossom days later — its petal tips deepening to rose-red, the colour climbing in from the edges.
3. 100mm macro: the same blossom still later — the deepening has crossed every petal, the whole flower rose-red.
4. 100mm macro: the flower with the morning dew dried off — the deepened tone settled, the change complete.
5. 50mm medium: the whole tree seen from under the branch — every blossom passing through the same deepening at its own pace, nobody in the frame.

TIME-LAPSE MOTION — IMPORTANT: physically-based the same one blossom, the tonal deepening across days — a time-lapse of one real flower observed at plant-study truthfulness: the blossom holds still at its own weight while the colour crosses it by the flower's own living process and by nothing else, petal tip by petal tip, until the whole corolla has deepened and the dew has dried off; the closing wide shows the whole tree passing through the same deepening at its own pace with nobody beneath it; no dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 꽃 아래의 세 사람 (절대 15.0~22.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP94_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. 무대사 — 렌더 완전 무음.
- **연출 특이**: **세 사람 썬(가변 2비트 절제)** — 꽃나무 아래 나란히 선 셋(1) — 나무와 셋이 함께 가만히 있는 넓은 뷰(2). **캐릭터 앵커(정본 AG ⑥)** — 이환 평복(익선관·곤룡포 미착용), 설화 옥비녀 궁녀 복식, 무결 도포·검흔. 아무도 중앙에 서지 않는 평온한 미장센.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly three people standing side by side beneath the flowering tree, nobody centered: the young king Ihwan — a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, a relaxed and unguarded young man's face, quiet warm eyes, lips closed; the court lady Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, lips closed; the warrior Mugyeol in peaceful dress — a 25-year-old Korean man in a clean plain scholar's overcoat, tall and steady, a faint old scar across his cheekbone, a settled calm face at rest, lips closed. The blossoms hang still at their own weight. No romantic longing gazes, no blushing courtship, no romantic exuberance. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the spring midday light coming down evenly on the three through the branches is the only light, resting on the petals and the plain garments. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the midday light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 50mm medium: the three of them standing side by side beneath the flowering tree — the plain-robed young man, the court lady, the scarred man in the plain overcoat, all three at rest.
2. 50mm wide: the same three seen wider — the tree's blossoms hanging still above them, the garden quiet.

STILLNESS MOTION — IMPORTANT: physically-based the even spacing, the still branches — a peaceful mise-en-scène of three people and one tree: the three stand at even spacing with nobody centering the frame and nobody speaking, the blossoms hang still above them at their own weight, and the wider view holds the three and the tree together in the quiet garden; no romantic longing gazes, no blushing courtship, no floating petals defying gravity; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 왕의 꿈 이야기 (절대 22.5~30.0 · 콘티 6컷 ★ 단독 최장)

- **시트**: `downloads/EP94_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [무거운 평온 · 이환/`ko-KR-Neural2-C`, Pitch -1.5, Speed 0.95] "과인은 요즘 — 꿈을 꾸지 않는다. 십 년 동안 밤마다 종이의 꿈을 꾸었다. 이제는 — 꽃잎의 꿈을 꾼다." (rel 5.0=절대 24.0, 사후 믹싱)
- **연출 특이**: **꿈 이야기 썬(가변 6비트 단독 최장)** — 낮은 돌에 앉아 아무 의식 없이 말을 시작하는 왕(1) — 요즘 꿈을 꾸지 않는다는 얼굴(2) — 십 년 종이의 꿈을 담담히 말하는 눈(3) — 이제는 꽃잎의 꿈을 꾼다는 작은 평온(4) — 꽃을 보며 듣는 설화(5) — 말이 끝나고 다시 고요해지는 둘(6). **안티슬롭 가드(plan 지정)** — 왕좌·단상·시적 독백·로맨스 고양 0건 — 담담한 동지의 대화다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — two people beneath the flowering branch: the young king Ihwan — a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, NO headwear of any kind, a relaxed and unguarded young man's face, quiet warm eyes, lips closed; the court lady Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, lips closed. The blossoms hang still at their own weight on the branch, no floating petals defying gravity. No throne, no dais, no courtiers, no romantic longing gazes, no blushing courtship, no love-theme fade. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the soft spring afternoon light reaching the two of them beneath the tree is the only light, resting on the faces and the plain garments. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 6 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the plain-robed young man seated on a low garden stone beside the court lady, the flowering branch above them both — he begins, without ceremony, the blossoms hanging still at their own weight.
2. 85mm close: his face as he says he does not dream these days — a calm settled statement.
3. 85mm close: his eyes a little way off — ten years of paper dreams told plainly.
4. 85mm close: his face easing into a small calm light — now he dreams of petals.
5. 85mm medium: the court lady listening — her cool eyes resting on the blossoms.
6. 85mm medium: the two of them with the tree between their silence — the dream told, the afternoon quiet again.

DREAM MOTION — IMPORTANT: physically-based the settled face, the small calm light — the dream is told plainly and nothing is staged: he sits on the low stone without any ceremony and begins, the face says what it says at the level of a settled fact, the eyes go a little way off for the ten years of paper dreams with their weight already put down, the face eases into a small calm light for the petals, and she receives the dream with her cool eyes resting on the blossoms; the words arrive later by voice: I do not dream these days — ten years of paper dreams every night — now I dream of petals; no throne, no dais, no romantic longing gazes, no love-theme fade, no floating petals defying gravity, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 설화의 공로 이동 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP94_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [서늘한 정정 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "그것은 폐하께서 꽃을 심으셨기 때문이옵니다." (rel 2.5=절대 31.5, 사후 믹싱) / [가벼워진 반박 · 이환/`ko-KR-Neural2-C`, Pitch -1.5, Speed 0.95] "아니다. 네가 심은 것이다. 과인은 그저 — 그것이 피는 것을 보는 사람이다." (rel 4.0=절대 33.5, 사후 믹싱)
- **연출 특이**: **공로 이동 썬(가변 3비트)** — 꽃에서 그에게로 눈을 돌려 서늘하게 바로잡는 설화(1) — 고개를 한 번 젓고 공로를 돌려보내는 이환(2) — 공로를 내려놓고 다시 꽃을 보는 둘(3). **안티슬롭 가드(plan 지정)** — 호감 고양·설레는 눈빛 0건 — 서로에게 빚을 넘기다 아무도 쥐지 않는 동지의 짧은 정산이다. 화자 얼굴 앵커 인라인(이환 — 관·검흔 없음).

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly two people, nobody else: the court lady Seolhwa — a young 21-year-old Korean woman in a dignified dark-pastel court-lady hanbok, neat traditional hair with a simple jade hairpin, pale porcelain skin, calm clear cool eyes, lips closed; and the young king Ihwan — a 24-year-old Korean man in plain everyday scholar's robes (dallyeong or po), NO royal winged hat (Ikseongwan), NO dragon robe, NO crown of any kind, NO headwear of any kind, NO scar on his face, hair simply tied back, a relaxed and unguarded young man's face, quiet warm eyes, lips closed. The blossoms hang still at their own weight, no floating petals defying gravity. No romantic longing gazes, no blushing courtship, no love-theme fade. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same soft afternoon light on the faces and the blossoms is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm medium: the court lady turning her eyes from the blossoms to him — she corrects him gently and coolly: the flowers grew because he planted them.
2. 85mm close: the plain-robed young man's face shaking his head once — no headwear, no scar — he refuses the credit and gives it back: it was you who planted them.
3. 85mm medium: only the two of them settling back into watching the blossoms — the credit passed and put down between them.

CREDIT MOTION — IMPORTANT: physically-based the single head shake, the cool correction — a quiet comradely exchange of two people handing a debt to each other and finding nobody will hold it: she corrects him plainly without any tenderness beyond it, his face shakes its head once and gives the credit back with a lightened level refusal — it was you who planted them, I am only the one who watches them bloom — and the two settle back into watching the blossoms with the credit put down between them and nothing left to hold; no romantic longing gazes, no blushing courtship, no love-theme fade, no floating petals defying gravity, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 세 그림자가 꽃잎 위에 나란히 닿음 (절대 37.5~45.0 · 콘티 4컷)

- **시트**: `downloads/EP94_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro. 무대사 — 렌더 완전 무음.
- **연출 특이**: **그림자 매크로 썬(가변 4비트)** — 자기 무게로 누운 꽃잎(1) — 그림자 한 개의 가장자리 진입(2) — 사람 형태의 세 그림자가 나란히(3) — 빛만 움직이는 완결(4). **그림자는 사람 형태(머리·몸·다리)** — 세 사람은 프레임 위 어딘가에 서 있을 뿐 화면 노출 0건. 인물 0명.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in the frame at all: fallen zinnia petals lying flat on the ground and three person-shaped human shadows — each shadow the shape of one standing person with a head, a body and legs, three distinct shadows lying side by side, not tree shadows and not branch shadows. The people casting them stand somewhere above the frame and are never shown. The petals lie at their own weight, no floating petals defying gravity. No magical glow on petals. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the low spring afternoon light laying flat across the petals and the shadows is the only light, lengthening slowly as the afternoon goes on. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the low light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro: fallen zinnia petals scattered on the ground — each petal lying flat at its own weight.
2. 100mm macro: one shadow's edge entering the frame of petals — the light lowering.
3. 100mm macro: three person-shaped human shadows lying side by side across the petals — a head, a body and legs each, three distinct shadows.
4. 100mm macro: the three person-shaped shadows resting on the petals as the light goes lower — nothing moving but the light itself.

SHADOW MOTION — IMPORTANT: physically-based the low light, the three person-shaped shadows — the shadows and the petals carry the whole scene: the petals lie still at their own weight, the first shadow's edge slides into the frame as the light lowers, the second and third shadows come to lie beside it until three person-shaped shadows rest side by side across the petals, evenly spaced and unhurried, and the frame holds with nothing moving in it but the light itself lengthening; the people above the frame are never shown; no floating petals defying gravity, no magical glow on petals; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 봄의 낮광 (절대 45.0~52.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP94_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. 무대사 — 렌더 완전 무음.
- **연출 특이**: **낮광 썬(가변 2비트 절제)** — 아무도 없는 만개한 정원의 만낮(1) — 꽃잎 밭을 지나 몸통을 따라 밝은 가지로 오르는 슬로우 틸트(2). **주체는 빛 그 자체** — 봄 낭만 서정·부유 연출 0건. 인물 0명.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in the frame at all: the garden in full spring daylight — the flowering tree, the low garden stone, the ground of fallen petals — nobody in the frame at all, the daylight itself is the subject, filling the garden evenly. The petals lie at their own weight, no floating petals defying gravity. No dreamy spring romance reverie, no magical glow on petals. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the full spring daylight filling the garden evenly is the only light, pouring through every blossom. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the daylight's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 35mm wide: the garden in full spring daylight — the flowering tree, the low stone, the ground of petals, nobody in the frame.
2. 35mm wide, slow tilt: from the petal ground up the trunk into the bright branches — the daylight pouring evenly through every blossom.

DAYLIGHT MOTION — IMPORTANT: physically-based the even daylight through every blossom, the slow tilt — the subject is the daylight itself and nothing else: the wide view holds the empty garden — tree, stone, petal ground — in one even full-day brightness, and the slow tilt climbs from the petal-covered ground up the trunk into the bright branches where the daylight pours evenly through every blossom; the garden is one held breath of light; no dreamy spring romance reverie, no floating petals defying gravity, no magical glow on petals; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 꽃잎이 흩어짐 → 암전 (절대 52.5~60.0 · 콘티 2컷)

- **시트**: `downloads/EP94_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제95화 「혈화의 만개」에서 계속(편집 단계 삽입).
- **연출 특이**: **폐장 썬(가변 2컷)** — 아무도 없는 정원에서 꽃잎이 자기 무게로 떨어지고 마지막 빛이 고르게 물러가 완전 암전까지(1) — 타이틀 카드(편집 단계 참조용, 렌더 제외). **자연 낙하 전용(plan 지정)** — 부유·회오리·바람에 찢김 0건. 인물 0명.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — no person in the frame at all: the flowering tree of Nakhwawon in the late spring afternoon with nobody in the frame — no person, no figure, no face, no silhouette, the garden empty. A few petals let go of the branch and fall in natural fall at their own weight — never wind-torn, never swirling, never floating upward. No finale tableau, no looking back, no romantic exuberance. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the last spring afternoon light of the day is the only light, and it withdraws evenly as the episode closes — the petals pale by degrees and the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the evening light's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence (the sheet's second panel — the red next-episode title card — is edit-stage reference only and is NOT rendered):
1. 50mm medium, slow tilt: the flowering tree in the late afternoon with nobody in the frame — a few petals letting go of the branch and falling at their own weight, the last brightness withdrawing evenly until complete black.

FALL MOTION — IMPORTANT: physically-based the natural fall at their own weight, the even leaving of the light — the episode closes as landscape and not as statement: a few petals let go of the branch and fall through the cooling air in natural fall at their own weight — never wind-torn, never swirling, never floating upward — the slow tilt holds the empty garden as the last brightness withdraws evenly off the blossoms, and the frame darkens until nothing remains — complete black, held; no finale fanfare, no 'the end' mood, no romantic exuberance; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

**— EP94 원장 완결. 콘티 시트 8종(`downloads/EP94_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`)과 본 원장 8블록을 제미나이 웹에 시트 첨부 + 전문 투입으로 실사화한다. 다음: 제95화 「혈화의 만개」 —**
