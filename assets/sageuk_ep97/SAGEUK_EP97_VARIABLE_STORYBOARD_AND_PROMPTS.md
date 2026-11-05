# 「혈화의 궐」 EP97 가변 디렉터 실사 시퀀스 프롬프트 마스터 원장 (2026-11-06)

> **근거**: `VARIABLE_STORYBOARD_DIRECTOR_SOP.md` (v3.0, 2026-11-04 아르센 님 직접 컨펌) + 정본 제97화 「사함의 비녀」 8썬표(`master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` `제97화 「사함의 비녀」` 절, 원전: 제97장 정본) + `characters.md` 캐릭터 앵커 + plan 지정 앵커(이설화 — 사헌부 감규 관사 한복, 옥비녀, 십 년 만에 비움과 가벼운 미소를 되찾은 눈빛) + EP22~EP96 원장 템플릿(동일 규격)
> **범위**: EP97 전 8썬(S01~S08) — 콘티 시트 8종(가변 28컷) + 실사 렌더 프롬프트 8블록
> **지위**: 제미나이 웹 Veo 실사화 렌더링 시 본 원장의 블록 프롬프트를 **전문 그대로 복사 투입**한다. 해당 썬의 콘티 시트를 첨부하고, 프롬프트는 편집·축약 없이 전문 사용이 원칙이다.
> **렌더 규격**: 썬당 10초 클립 1개 · 무음 렌더(대사·내레이션·효과음은 사후 믹싱) · 화면비 키워드 미지정(제미나이 웹 기본값 — EP01 실증 통과 조건)
> **정본 배치 준수**: EP96 S8 엔드카드 「제98화 왕관 없는 세 그림자에서 계속」이 본화의 무대다. **서사 인계 라인** — 본화 S1 100mm Macro · 사함, 사함의 세 가지 — 은장도, 목인 조각, 백일홍 비녀 [내레이션/`ko-KR-Wavenet-C` (0.0): "설화의 사함에는 — 세 가지가 들어 있었다." (rel 3.0=절대 2.0)], S2 100mm Macro · 은장도, 관고에 바치기로 한 은장도 [설화/`ko-KR-Neural2-A` (0.0): "그것은 — 역사의 것이 되어야 했으므로." (rel 3.0=절대 9.5)], S3 100mm Macro · 목인, 사함에 남는 목인의 조각 — 완성되어 있던 맹세 (무대사), S4 100mm Macro · 비녀, 창밖의 낙화원을 보며 꺼내 보는 비녀 [내레이션/Wavenet-C (0.0): "십 년 동안 빼앗겨 있던 것이 돌아온 뒤에 남는 것은 — 이상하게도 증오가 아니라, 비움이었다." (rel 4.5=절대 24.5)], S5 50mm, 비녀가 다시 사함으로 [설화/Neural2-A (0.0): "그 비녀는 — 그 십 년 동안, 그녀가 잃지 않은 유일한 것이었다." (rel 4.0=절대 32.0)], S6 85mm, 웃음 [설화/Neural2-A (0.0): "복수가 끝나고 남는 것은 — 언제나, 십 년 전에는 생각하지 못했던 작은 것들이지요." (rel 4.5=절대 39.5)], S7 35mm, 닫히는 사함 (무대사), S8 100mm Macro → 엔드카드, 사함 위 손 → 암전 → 타이틀(자막: 제98화 「왕관 없는 세 그림자」에서 계속).
> **안티슬롭 ① — 감상 회고 나레이션 난사 배제(plan·정본 안티슬롭 지정)**: 감상 회고 나레이션 난사 렌더 **0건**. 치환 — **세 가지 소품(은장도, 목인 조각, 백일홍 비녀)을 하나씩 꺼내 보고 정리하는 각각 절제된 한 동작의 무게**(S1~S5 본체). `no retrospective narration montage, one restrained single action` S1~S7 상설.
> **안티슬롭 ② — "이제야 해방입니다" 슬롭 배제(plan·정본 안티슬롭 지정)**: 해방 선언·눈물의 해방 연기 렌더 **0건**. 치환 — **"증오가 아니라, 비움이었다."** — 비움이라는 단어 하나(S4 내레이션·S6 미소 본체). `no liberation declaration, no tearful release` S4·S6 상설.
> **장소 전환(plan·정본 AG ① 지정)** — 사함 개봉의 EP55 침전 개봉과의 중복 회피: 본화 장소는 **사헌부 감규 관사 방안**(실내, 민가 사랑방 규모). `the magistrate's residence room, not the palace bedchamber` 전 썬 상설 — 생성기 `validate()` residence 가드 전 썬 통과.
> **S2 관고 은장도 매크로(plan·정본 지정)** — 은장도를 사헌부 관고에 바치기로 한 결정의 4비트 매크로(들어 올림 → 천 위 → 전달의 두 손 → 빈 손). **인물 2인 제한 준수(정본 AG ⑥)** — 설화의 손과 관고 수간의 손, 두 쌍의 손뿐이며 얼굴 미노출.
> **S3 목인 조각 매크로(plan·정본 지정)** — 사함 바닥에 남는 백일홍 목인 한 조각 — 완성되어 있던 맹세(무대사 3비트). **은장도 0건** — S2에서 이미 관고로 넘어갔으므로 상자 안에는 목인 조각과 비녀만 남는다(`no dagger anywhere in the frame`·`the silver dagger's place already empty` 가드, 초벌 결함 교정 후 재렌더). 목인은 **머리와 한쪽 어깨만 남은 파단 조각**으로만 렌더(`never a whole figurine`). 얼굴 0건.
> **S4 창밖 낙화원 비녀 매크로(plan·정본 지정)** — 창밖의 낙화원을 바라보며 손에 쥔 백일홍 비녀 매크로(6비트 단독 최장 — "증오가 아니라 비움"의 본체). `natural wind-driven pass, never swirling upward` 가드 — 꽃잎 부유·CG 회오리 0건.
> **S6 십 년 만의 가벼운 미소 매크로(plan·정본 지정)** — "복수가 끝나고 남는 것은 작은 것들이지요"의 85mm 3비트 미소. 해방 선언·눈물 0건 — 미소가 전체 이벤트다.
> **S8 사함 위 손 → 암전(plan·정본 지정)** — 닫힌 사함 뚜껑 위에 얹힌 손 매크로 → 균일 암전 → 타이틀. 인물 1인(손뿐) → 암전 구간 인물 0명.
> **백지 설계 교칙(plan 절대 준수)** — 사함 내부·천·기물 위 텍스트 일체 금지. **붉은 색은 S08 타이틀뿐**(시트 유일 의도 채색). 엔드카드 자막(제98화 「왕관 없는 세 그림자에서 계속」)은 편집 단계 삽입 — 시트에는 편집 참조용 카드로만.
> **무자막 원칙(100화 전편 규격)** — 화면 노출 문자 일체 금지. 내레이션 2구(S1·S4) + 설화 대사 3구(S2·S5·S6)는 편집 단계 사후 믹싱 — 시트와 렌더에 자막 활자를 그리지 않는다.
> **캐릭터 앵커(plan 지정)**: 이설화 — **사헌부 감규 관사 한복, 소박한 옥비녀, 십 년 만에 비움과 가벼운 미소를 되찾은 눈빛**(EP96 사관/궁녀 앵커에서 **감규 관복 앵커로 갱신** — 궁녀 다크 파스텔 한복 렌더 0건, 21세·창백한 피부·서늘하고 총명한 눈빛 계승). **이환·강무결 미등장** — 본화 렌더 0건(생성기 `validate()` 인물 어절 스캔 — king·Ihwan·court lady·Mugyeol 0건 단정 통과).
> **입모양 배제(100화 전편 규격)** — 내레이션 2구(S1·S4)·설화 3구(S2·S5·S6) 전부 무음 렌더 + 사후 믹싱, 전 썬 `lips closed`. S3·S7·S8 무대사 — 렌더 전면 무음.
> **동일 보이스 ID 점검(plan 지정)**: 내레이션 `ko-KR-Wavenet-C`(0.0 — plan 확정치) S1 1구+S4 1구 — 동일 배역(내레이션) 연속, 피치 사다리 충돌 없음. 설화 `ko-KR-Neural2-A`(0.0 — plan 확정치) S2 1구+S5 1구+S6 1구 — 동일 배역 연속(EP95·96 설화 0.0과 동일 — 화간 연속성 유지). **두 배역이 서로 다른 ID — 본화 내 충돌 요소 0건**. 이환 `Neural2-C` — 본화 미등장. 파일명 분리 규칙 기재(`EP97_S1_NARRATION`/`EP97_S4_NARRATION`/`EP97_S2_SEOLHWA`/`EP97_S5_SEOLHWA`/`EP97_S6_SEOLHWA`). 렌더는 전 썬 무음.
> **가변 컷 배분**: 5/4/3/6/3/3/2/2 = 28컷 — EP13~EP96 전 배분(108종 전수 대조) 미중복(생성기 `validate()`가 ep69_sheets.py의 PRIOR 임베디드 목록(EP13~EP68)+EP69 배분+EP13~EP96 형제 생성기 DISTRIBUTION 파일 스캔을 합산 단정 통과, 직전 화 EP96분 4/3/6/3/5/3/2/2와도 상이). **S4(창밖 낙화원의 비녀) 6컷 단독 최장** — "증오가 아니라, 비움이었다"가 이루어지는 본화의 서사 본체. S1(사함의 세 가지) 5컷, S2(관고의 은장도) 4컷, S3(목인 조각)·S5(비녀의 귀환)·S6(웃음) 각 3컷, **S7(닫히는 사함)·S8(사함 위 손→암전→타이틀) 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
> **시트 결함 이력 및 실측 기록**: 총 이미지 생성 11회(초벌 8 + 재렌더 3) 중 최종 채택 8장 — **재렌더 3건**: ① **해상도 1px 이탈(S02·S05)** — 초벌이 **1023×1537**(1024×1536 규격 위반 — EP94 S07·EP95 S05·EP96 S05 동일 결함 계승, 본화는 동시 2건) → 각 **1회 재렌더에서 1024×1536 정확 해소**(md5 S02 6b6c3e468fd8·S05 499d6605b342 — 탈락본 md5 S02 9e7d058c6c13·S05 b9ab42e9cb27 대조). ② **S03 서사 정합 결함** — 재렌더 전 초벌 S03 패널 1에 **S02에서 이미 관고로 넘긴 은장도가 다시 상자 안에 남아 있었고**, 목인이 파단 조각이 아닌 온전한 원숭이 인형으로 렌더됨(라벨 `one fragment`와 그림 불일치) → 프롬프트에 `the silver dagger's place already empty`, `no dagger anywhere in the frame`, `a broken piece only — the carved monkey's head and one shoulder with the rest broken away, never a whole figurine` 지문 보강 후 재렌더, **결함 전량 해소**(md5 9618e0cc3304 — 탈락본 28ca3023fb4d 대조, 3분할 크롭 재검독). 탈락본은 `images --out` 덮어쓰기로 미보존(실측 수치로만 기록). 최종 PIL 전량 실측 **1024×1536 전장 정확 8/8**. 가시 채색(chroma>25 ∧ 최대명도>64, 3픽셀 그리드 샘플링) S01~S07 전장 0.00%, S08 0.24%(적색 타이틀 — 좌표 확인, **타이틀 열 x373~403·y746~1204 한정 — 의도 채색**). **전장 md5: S01 ccc9208f6e07 / S02 6b6c3e468fd8(재렌더) / S03 9618e0cc3304(재렌더) / S04 080160f28808 / S05 499d6605b342(재렌더) / S06 3931679e1b5c / S07 6da2056b2d92 / S08 28990bc264c8**.
> **검독 운영 교훈(EP67~EP96 계승)**: **동일 경로 전장 재열람(`read_file` 같은 경로)은 구버전(또는 컨텍스트 탈락본)을 돌려줄 수 있다** — 본화는 **별도 크롭 경로(`downloads/qc_crops/Z_EP97_*`) 재열람으로 현재본 판정**(전장 3분할 크롭 + S08 타이틀 확대 크롭). **어간 부분 문자열 함정 계승** — 금지 어휘의 어간 부분 문자열도 생성기 validate()가 차단(EP66 실측 계승). **본화 특유 주의** — 본화에는 유혈·흉기 요소 원천이 없으나 은장도는 흉기 직결 소품이므로 **렌더 프롬프트에 전 썬 `no fighting, no combat` 상설**로 기입하고, 은장도는 언제나 칼집·천 위의 정지 소품으로만 기재. **해상도 1px 이탈(S02·S05)** — 렌더 승여 응답은 ok여도 PIL 전량 재실측이 유일한 판정자이며, **동일 결함이 재렌더 1회로 해소되지 않을 수 있으므로 재실측→재렌더 루프를 해소까지 반복**한다.
> **plan 기재 최종성 확인(팩트체크)**: 정본 출처 `master_screenplay/SEASON_04_MASTER_SCREENPLAY.md` **제97화 「사함의 비녀」 절(원전: 제97장 정본) 직접 열람**(399행 이하) — 8썬 시간·렌즈·대사·rel/절대 수치 전부 정본표에서 재대조, plan 기재와 1:1 일치. 원전 소설(`novel_s04_ch76_ch100.md` 제97장) 대조 — 사함의 세 가지(은장도·목인 조각·백일홍 비녀)·은장도의 귀처(사헌부 관고 바침 — "역사의 것이 되어야 했으므로")·목인 조각의 소재(일곱 사람이 각자의 곳에 두었으므로 사함에 남음)·비녀의 귀처(다시 사함으로)·"증오가 아니라 비움" 재확인. **S08 타이틀 슬롯**: 「제98화 왕관 없는 세 그림자에서 계속」 실제 글자수 **16자 = 1자 1슬롯 원칙에 따라 16슬롯** 확정(확대 크롭 검독 통과, 숫자 9·8 각각 단독 슬롯, 4번째 슬롯 「화」 정자 — **plan 기재 「18슬롯」은 실측 16자와 불일치하여 16슬롯으로 정정 채택**, EP96 13슬롯·EP95 15슬롯과 동일 산출 규격). **보이스 피치**: plan 확정치(내레이션 Wavenet-C 0.0·설화 Neural2-A 0.0)를 본화에 채택 — plan 우선 원칙. **가변 배분**: plan은 특정 배분 수치를 고정하지 않아 본화 서사에 맞춰 5/4/3/6/3/3/2/2=28컷으로 설계 — **총 컷수 28 규격 준수 + 선행 108종 미중복 기계 스캔**으로 이중 검증.
> **생성기 무인자 실행 방지(plan 주의문 반영)**: `ep97_sheets.py`는 **무인자 실행 시 렌더 0건**(validate + 프롬프트 파일만 생성하는 dry-run이 기본값). 렌더는 반드시 대상 씬 지정(`python3 projects/sageuk-revenge/ep97_sheets.py S01`), 전체는 `ALL`(명시적).

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
2. **화풍 강제 블록** `Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style` 생략 금지. **흑백 시트 → 컬러 실사 전환** — 실사의 가을 관사 방(창살로 들어오는 가을 햇살과 낙화원), 은장도의 은빛, 백일홍 비녀의 진홍 꽃 모양(시리즈 표준 은유 — 붉은 소품은 본화에서 비녀 꽃 모양으로만), 나무 목인의 옛 나무빛이 색으로 복원된다. **붉은 소품은 비녀의 백일홍 꽃 모양뿐** — 의도 외 적색 액센트 0건.
3. **클린 프레이밍** `Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid. Clean full-bleed cinematic frames only` 생략 금지. **본화는 상자와 세 가지 소품이 주인공** — 렌더 프레임 내 가독 문자 일체 0건.
4. **물리 블록**: 씬 지배 물질의 물리 기반 모션 지문을 매 썬 명시한다 — S1 **상자의 정지와 세 가지의 나열**(the open box, the three things at rest), S2 **천 위의 은장도와 전달의 두 손**(the dagger on the cloth, the quiet passing), S3 **손바닥 위의 나무 조각**(the wooden fragment, the steady palm), S4 **창빛 속 비녀와 지는 꽃잎**(the hairpin in the window light, the natural wind-driven pass), S5 **상자로 돌아가는 비녀**(the lowering hand, the two things together), S6 **십 년의 무게가 내려놓이는 미소**(the light smile, the settling afternoon), S7 **단정하게 닫히는 뚜껑**(the lid lowered evenly, the quiet room), S8 **뚜껑 위 손과 물러가는 빛**(the hand on the lid, the even leaving of the light).
5. **세이프 필터**: `poison`·`dying`·`death`·`dead`·`corpse`·`blood`·`suicide`·`vomit`·`necrosis`·`murder` 어휘 사용 절대 금지(생성기 validate() 차단 확인 — **어간 부분 문자열도 차단된다 — EP66 실측 계승**). `no harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat` 전 썬 상설. `all characters are adults` 전 썬 상설. **은장도는 흉기 직결 소품** — 언제나 칼집·천 위의 정지 상태 소품으로만 기재되고 렌더 전 썬에서 fighting·combat·위협 동작 0건. 본화는 복수가 끝난 뒤의 정리 화면이다.
6. **백지 설계 교칙 + 문자 가드(정본 AG ①)**: 화면 노출 문자 요소 — **S08 붉은 타이틀(편집 단계)뿐**. 상자·천·기물 위 텍스트 일체 금지. 엔드카드 자막(제98화 「왕관 없는 세 그림자에서 계속」)은 편집 단계 삽입, S8 렌더는 완전 암전으로 끝난다.
7. **입모양 배제 가드(100화 전편 규격)**: 내레이션 2구(S1·S4)·설화 3구(S2·S5·S6)로 전부 보이스오버·사후 믹싱 — 화면 인물의 입과 무관. 전 썬 `lips closed` 상설. S3은 얼굴 미노출 매크로, S3·S7·S8 무대사 — 렌더 전면 무음.
8. **인물 일관성(정본 AG ⑥)**: 고정 시각 앵커를 씬 프롬프트 안에 인라인 기입.
   - **이설화 — 사헌부 감규 관사 한복·옥비녀(plan 지정)**: the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok at the Saheonbu magistrate's residence, neat traditional hair with a simple jade hairpin (binyeo), pale porcelain skin, calm clear cool eyes, the light easy smile of one who has come back to smiling after ten long years, lips closed.
   - **이환·강무결 — 본화 미등장**: 렌더 0건. 궁녀 다크 파스텔 한복·왕관·군복 렌더 0건.
   - **인물 상한**: S01 손뿐(얼굴 0건), S02 손 2쌍=인물 2인(얼굴 0건), S03 손뿐(얼굴 0건), S04 손뿐(얼굴 0건), S05 손뿐(얼굴 0건), S06 설화 1인, S07 설화 1인, S8 손뿐 → 암전 구간 인물 0명. 군중·인파 렌더 0건.
9. **광원 표기**: S1 — 관사 창살을 거쳐 낮은 탁자 위 사함에 닿는 오전의 빛. S2 — 같은 오전 빛이 은장도와 천 위에. S3 — 같은 빛이 목인 조각 위에. S4 — 창밖 낙화원의 빛이 비녀와 손 위에. S5 — 같은 창빛이 상자 안의 비녀 위에. S6 — 오후로 누그러진 빛이 미소의 얼굴 위에. S7 — 오후의 빛이 닫히는 뚜껑 위에. S8 — 늦은 오후의 빛이 뚜껑 위 손에 고르게 낮아지다 균일 암전 진입. `never flickering like horror, never strobing` 전 썬 상설. **EP96 어전 창살 가드를 본화 관사 창살 가드에 혼용하지 않음** — 씬별 LIGHT GUARD 분리 유지.
10. **트림**: 렌더 10초 클립에서 시작 1.0초·끝 1.5초 버퍼 컷 → 실사용 1.0~8.5초.
11. **엔드카드**: S8 사함 뚜껑 위 손·균일 암전 구간 이후의 붉은 타이틀(제98화 「왕관 없는 세 그림자에서 계속」, 16슬롯)은 **편집 단계에서 삽입**. S8 렌더는 프레임이 어두워지는 구간 종료 후 완전 암전으로 끝난다(시트 마지막 패널의 붉은 타이틀 카드는 편집 단계 참조용 — **렌더 컷 리스트에서 제외** — 렌더 컷 리스트 합계 27컷 = 시트 28컷 − 타이틀 카드).
12. **보이스 모델 배정(시리즈 고정 — characters.md·plan 준수)**: 내레이션 `ko-KR-Wavenet-C` (Pitch **0.0** — plan 확정치, Speed 1.0, 무겁고 담담한 기록자 톤) — S1 1구·S4 1구. 설화 `ko-KR-Neural2-A` (Pitch **0.0** — plan 확정치, Speed 1.0, 서늘한 정리·십 년 만의 가벼움 톤) — S2 1구·S5 1구·S6 1구. 본화 캐릭터 대사 3구 + 내레이션 2구 + 엔드카드 자막 1건. S3·S7·S8 무대사 — 렌더는 무음.
13. **동일 보이스 ID 점검**: 내레이션 `Wavenet-C`(0.0) 2구 — 동일 배역 연속. 설화 `Neural2-A`(0.0) 3구 — 동일 배역 연속. **두 배역이 서로 다른 ID를 쓰므로 본화 내 충돌 요소 없음**. 파일명 분리 규칙 기재(`EP97_S1_NARRATION`/`EP97_S4_NARRATION`/`EP97_S2_SEOLHWA`/`EP97_S5_SEOLHWA`/`EP97_S6_SEOLHWA`). 렌더는 전 썬 무음.
14. **정본 썬 경계**: 00.0~07.5 / 07.5~15.0 / 15.0~22.5 / 22.5~30.0 / 30.0~37.5 / 37.5~45.0 / 45.0~52.5 / 52.5~60.0 (8×7.5초).
15. **가변 컷 배분**: 5/4/3/6/3/3/2/2 = 28컷 — EP13~EP96 전 배분 108종 전수 대조 미중복(생성기 `validate()` 단정 통과). **S4 6컷 단독 최장**(비움이 이루어지는 완급), S1 5컷·S2 4컷·S3 3컷·S5 3컷·S6 3컷, **S7·S8 각 2컷 절제** — "3컷·4컷 고정" 슬롭 회피.
16. **복수가 끝나고 남는 것은 작은 것들 — 낭독이 아니라 그림이다(본화 핵심)**: 본화에는 감상 회고 난사도 해방 선언도 없다 — 상자가 열리고 세 가지가 나열되는 것(S1)에서 은장도가 관고로 떠나고(S2), 목인 조각이 완성된 맹세로 손바닥에 놓이며(S3), 비녀가 창밖 낙화원의 빛에 쥐어지고(S4), 다시 상자로 돌아가며(S5), 십 년 만의 가벼운 미소가 지어지고(S6), 상자가 단정하게 닫히며(S7), 뚜껑 위 손 위로 빛이 물러간다(S8). 전 썬 `no retrospective narration montage, one restrained single action(S1~S7), no liberation declaration, no tearful release(S4·S6)` 상설. 주제의 감정은 대사 낭독이 아니라 소품 하나의 무게(S1~S3)와 창빛 속 비녀(S4)와 미소(S6)라는 그림이다.

---

## 1. S01 첫째 — 사함의 세 가지 (절대 00.0~07.5 · 콘티 5컷)

- **시트**: `downloads/EP97_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 사함. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0 — plan 확정치, Speed 1.0] "설화의 사함에는 — 세 가지가 들어 있었다." (rel 3.0=절대 2.0, 사후 믹싱)
- **연출 특이**: **개장 썬(가변 5비트 매크로)** — 낮은 탁자 위 열린 사함과 그 안의 세 가지(1) — 은장도(2) — 목인 조각(3) — 백일홍 비녀(4) — 상자 가장자리에 얹힌 설화의 손(5). **안티슬롭 가드(plan 지정)** — 감상 회고 나레이션 난사 0건 — 세 가지는 하나씩, 각각 절제된 한 동작의 무게로만 나열된다. 얼굴 미노출 매크로.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: a young woman magistrate's hand from the sleeve of a dignified magistrate's hanbok at the Saheonbu magistrate's residence. On the low dark table one small wooden private letter box opened — inside it three things at rest: a small silver dagger with a plain worn sheath lying still, one fragment of a small carved wooden monkey figurine, and a slender hairpin with a small deep-red cockscomb-flower motif. The residence room, not the palace bedchamber. No retrospective narration montage, one restrained single action. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the autumn morning light coming through the residence's lattice windows onto the open box and the three things is the only light, resting evenly on the low table. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 5 panels in order as one continuous ~10 second sequence:
1. 100mm macro: a small wooden private letter box opened on the low dark table — inside it three things at rest, seen plain and still.
2. 100mm macro: the first thing — a small silver dagger lying in the box, its sheath plain and worn.
3. 100mm macro: the second thing — one fragment of a small wooden monkey figurine resting in the box's corner.
4. 100mm macro: the third thing — a slender hairpin with a cockscomb-flower pattern resting on the cloth inside the box.
5. 100mm macro: her hand resting on the box's edge — three things, each to be taken out and put back in its own turn.

BOX MOTION — IMPORTANT: physically-based the open box, the three things at rest — the frame shows an inventory and nothing else: the small wooden box lies open on the low table under the lattice light, the silver dagger rests still in its sheath, the little wooden monkey fragment sits in its corner, the hairpin with the deep-red cockscomb motif lies on the cloth, and her hand rests on the box's edge in no hurry at all; no retrospective narration montage, one restrained single action; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 2. S02 둘째 — 관고에 바치기로 한 은장도 (절대 07.5~15.0 · 콘티 4컷)

- **시트**: `downloads/EP97_S02_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 은장도. [서늘한 결정 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "그것은 — 역사의 것이 되어야 했으므로." (rel 3.0=절대 9.5, 사후 믹싱)
- **연출 특이**: **관고 은장도 썬(가변 4비트 매크로)** — 상자에서 은장도를 들어 올리는 손(1) — 두 손받이 천 위에 평평히 놓인 은장도(2) — 관고 수간의 두 번째 손으로 전달되는 포장된 은장도(3) — 무릎 위에 내려놓이는 빈 손(4). **인물 2인 제한 준수(정본 AG ⑥)** — 설화의 손과 관고 수간의 손, 두 쌍뿐 — 얼굴 미노출. **안티슬롭 가드** — 그것은 역사의 것이 되어야 했으므로, 프레임은 전달만 보여준다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame, exactly two people in the room and only their hands seen: a young woman magistrate's hands from the sleeves of a dignified magistrate's hanbok, and a treasury keeper's second pair of plain official hands. One small silver dagger with a plain worn sheath — resting still, sheathed or wrapped in a white cloth at every moment, never drawn, never pointed, never held as a weapon. The residence room, not the palace bedchamber. No sentimental display, no retrospective narration montage, one restrained single action. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same autumn morning light on the dagger and the white cloth is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 4 panels in order as one continuous ~10 second sequence:
1. 100mm macro: her hand lifting the silver dagger out of the box — one unhurried movement of one hand.
2. 100mm macro: the dagger lying flat on a white cloth across her palms — to be given to the Saheonbu's official treasury.
3. 100mm macro: her hands passing the wrapped dagger toward a second pair of hands — the treasury keeper's — two people only in the room.
4. 100mm macro: her empty hands settling back on her knees — the dagger becomes history's thing, and the frame shows only that.

DAGGER MOTION — IMPORTANT: physically-based the dagger on the cloth, the quiet passing — the whole scene is one giving and nothing else: her hand lifts the sheathed dagger out of the box in one unhurried movement, the dagger lies flat on a white cloth across her open palms, the wrapped dagger is passed quietly toward the treasury keeper's second pair of hands, and her empty hands settle back on her knees — it becomes history's thing and the frame shows only the emptied hands; no sentimental display, no retrospective narration montage, one restrained single action; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 3. S03 셋째 — 사함에 남는 목인의 조각 (절대 15.0~22.5 · 콘티 3컷)

- **시트**: `downloads/EP97_S03_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 목인. 무대사 — 렌더 완전 무음.
- **연출 특이**: **목인 조각 썬(가변 3비트 매크로)** — 은장도 자리가 이미 비어 있는 상자 안과 목인 조각(1) — 빛 속으로 들어 올리는 손끝(2) — 열린 손바닥 위에 놓인 조각 — 완성되어 있던 맹세(3). **은장도 0건** — S2에서 이미 관고로 넘어갔으므로 프레임에 등장하지 않는다. **안티슬롭 가드** — 무대사, 조각 하나가 전체를 말한다. 얼굴 미노출 매크로.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: a young woman magistrate's fingertips from the sleeve of a dignified magistrate's hanbok. On the cloth inside the open wooden letter box only one broken wooden fragment now remains beside the hairpin — the silver dagger's place already empty, its sheath gone to the official treasury, no dagger anywhere in the frame. The fragment is a broken piece only: the carved monkey's head and one shoulder, the rest broken away, its broken edge worn smooth by years of handling, small enough to hide in a palm, never a whole figurine. The residence room, not the palace bedchamber. No retrospective narration montage, one restrained single action. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the same autumn morning light on the wooden fragment and the open palm is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the morning light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the box's interior seen close — the silver dagger's place already empty, only the broken wooden fragment and the hairpin left on the cloth.
2. 100mm macro: her fingertips lifting the wooden fragment into the light — a broken piece only, the carved monkey's head and one shoulder with the rest broken away, never a whole figurine.
3. 100mm macro: held still — the broken fragment resting on her open palm — the oath it stood for already complete.

FRAGMENT MOTION — IMPORTANT: physically-based the broken fragment, the steady palm — the scene has no dialogue and no face in it, the little piece of wood says the whole of it: the box lies open with the dagger's place already empty and only the broken fragment left beside the hairpin, her fingertips lift that broken piece up in one unhurried motion, and it settles on her open palm, held still — the oath it stood for already complete; no dagger appears anywhere, it was given away one scene earlier; no retrospective narration montage, one restrained single action; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 4. S04 넷째 — 창밖의 낙화원을 보며 꺼내 보는 비녀 (절대 22.5~30.0 · 콘티 6컷 ★ 단독 최장)

- **시트**: `downloads/EP97_S04_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro · 비녀. [무거운 나레이션 · 내레이션/`ko-KR-Wavenet-C`, Pitch 0.0 — plan 확정치, Speed 1.0] "십 년 동안 빼앗겨 있던 것이 돌아온 뒤에 남는 것은 — 이상하게도 증오가 아니라, 비움이었다." (rel 4.5=절대 24.5, 사후 믹싱)
- **연출 특이**: **비녀 썬(가변 6비트 매크로 단독 최장 — 본화의 서사 본체)** — 천에서 집어 드는 비녀(1) — 창가로 들어 올린 손(2) — 창살 너머 지는 꽃잎(3) — 창빛 속에 쥐어진 정지(4) — 가볍게 감기는 손가락 — 증오가 아니라 비움(5) — 손바닥 위에 내려놓인 비녀 — 상자에서 가장 가벼운 것(6). **안티슬롭 가드(plan 지정)** — 해방 선언·눈물의 해방 0건 — "증오가 아니라 비움"은 프레임에서 비녀와 창빛으로만 도달한다. `natural wind-driven pass, never swirling upward` 가드. 얼굴 미노출 매크로.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: a young woman magistrate's hand from the sleeve of a dignified magistrate's hanbok. One slender hairpin with a small deep-red cockscomb-flower motif — the one thing she did not lose in ten years — lifted from the cloth inside the open wooden letter box and raised toward the lattice window. Beyond the lattice, the autumn garden where the late flowers are falling, seen soft and out of focus. The residence room, not the palace bedchamber. No liberation declaration, no tearful release, no retrospective narration montage, one restrained single action. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the garden window's late-morning light on the hairpin and the hand is the only light, coming past the lattice from outside. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the window light's own depth, no milky flat darkness.

Recreate the 6 panels in order as one continuous ~10 second sequence:
1. 100mm macro: the cockscomb-pattern hairpin taken up from the cloth — the one thing she did not lose in ten years.
2. 100mm macro: her hand raising the hairpin toward the window — beyond the lattice, the autumn garden where the late flowers are falling.
3. 100mm macro: through the lattice beyond her hand — the garden's falling flowers crossing the light, seen past the hairpin in her fingers.
4. 100mm macro: her hand holding the hairpin still in the window light — held, nothing else moving.
5. 100mm macro: her fingers closing lightly around the hairpin — ten years taken away and given back, and what remains is not resentment but a light smile.
6. 100mm macro: the hairpin lowered to rest across her open palm — the lightest thing in the box.

HAIRPIN MOTION — IMPORTANT: physically-based the hairpin in the window light, the natural wind-driven pass — the scene's longest breath and its whole point: the hairpin is taken up from the cloth, raised toward the garden window, held still in the window light while the late flowers fall past the lattice in their natural wind-driven pass and never swirling upward, her fingers close lightly around it — ten years taken away and given back — and the hairpin rests across her open palm, the lightest thing in the box; no liberation declaration, no tearful release, no retrospective narration montage, one restrained single action; the narration arrives later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 5. S05 다섯째 — 비녀가 다시 사함으로 (절대 30.0~37.5 · 콘티 3컷)

- **시트**: `downloads/EP97_S05_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 50mm. [서늘한 이유 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "그 비녀는 — 그 십 년 동안, 그녀가 잃지 않은 유일한 것이었다." (rel 4.0=절대 32.0, 사후 믹싱)
- **연출 특이**: **비녀의 귀환 썬(가변 3비트)** — 상자 안으로 천천히 내려가는 비녀(1) — 목인 조각 곁에 나란히 놓인 비녀(2) — 상자 입구에서 물러나는 손 — 잃지 않은 유일한 것, 간직됨(3). **안티슬롭 가드** — 감상 0건 — 간직하는 손의 움직임 하나가 전부다. 얼굴 미노출 매크로.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — hands only, no face anywhere in the frame: a young woman magistrate's hand from the sleeve of a dignified magistrate's hanbok. One slender hairpin with a small deep-red cockscomb-flower motif lowered back into the open wooden letter box, laid beside the small carved wooden monkey fragment — the two things resting together on the cloth, the silver dagger's place already empty. The residence room, not the palace bedchamber. No sentimental display, no retrospective narration montage, one restrained single action. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light resting on the box and the two things inside it is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 100mm macro: her hand lowering the hairpin back into the box — unhurried, one restrained action.
2. 100mm macro: the hairpin laid beside the wooden fragment in the box — the two things resting together.
3. 100mm macro: her hand withdrawing from the box's mouth — the hairpin she did not lose, kept.

RETURN MOTION — IMPORTANT: physically-based the lowering hand, the two things together — the hairpin is the one thing she did not lose in ten years and she keeps it by her own choice: her hand lowers the hairpin back into the box in one unhurried restrained motion, it is laid beside the wooden monkey fragment with the dagger's place already empty, and her hand withdraws from the box's mouth with nothing more performed around it; no sentimental display, no retrospective narration montage, one restrained single action; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 6. S06 여섯째 — 웃음 (절대 37.5~45.0 · 콘티 3컷)

- **시트**: `downloads/EP97_S06_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 85mm. [십 년 후의 가벼움 · 설화/`ko-KR-Neural2-A`, Pitch 0.0 — plan 확정치, Speed 1.0] "복수가 끝나고 남는 것은 — 언제나, 십 년 전에는 생각하지 못했던 작은 것들이지요." (rel 4.5=절대 39.5, 사후 믹싱)
- **연출 특이**: **미소 썬(가변 3비트)** — 상자에서 고개를 드는 얼굴(1) — 작고 가볍게 지어지는 미소 — 십 년의 무게를 내려놓음(2) — 닫힌 상자를 앞에 둔 채 미소가 머무는 앉은 모습(3). **안티슬롭 가드(plan 지정)** — "이제야 해방입니다" 슬롭 0건 — 해방 선언도 눈물도 없이, 미소 하나가 전체 이벤트다.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — exactly one person in the room: the magistrate Seolhwa — a young 21-year-old Korean woman in her dignified magistrate's hanbok at the Saheonbu magistrate's residence, neat traditional hair with a simple jade hairpin (binyeo), pale porcelain skin, calm clear cool eyes, the light easy smile of one who has come back to smiling after ten long years, lips closed. One small wooden letter box on the low table before her, its lid open at first. The residence room, not the palace bedchamber. No liberation declaration, no tearful release, no retrospective narration montage. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light softening on her face is the only light, coming through the residence's lattice windows. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 3 panels in order as one continuous ~10 second sequence:
1. 85mm close: her face lifting from the box — the light beginning to return to it.
2. 85mm close: the smile forming — small, light, ten years' weight set down; not a declaration, only a smile.
3. 85mm medium: her sitting back in the magistrate's residence room with the closed box before her — the smile staying.

SMILE MOTION — IMPORTANT: physically-based the light smile, the settling afternoon — the smile is the whole event and nothing is performed around it: her face lifts from the box with the light beginning to return to it after ten years, the smile forms small and light — not a declaration and not tears, only a smile arriving as simply as weather — and she sits back with the box before her as the smile stays; no liberation declaration, no tearful release, no retrospective narration montage; the words arrive later by voice, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 7. S07 일곱째 — 닫히는 사함 (절대 45.0~52.5 · 콘티 2컷 ★ 절제)

- **시트**: `downloads/EP97_S07_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 35mm. 무대사 — 렌더 완전 무음.
- **연출 특이**: **폐장 썬(가변 2비트 절제)** — 뚜껑이 단정하게 내려앉는 사함(1) — 낮은 탁자 위에 제자리로 놓인 닫힌 사함(2). **안티슬롭 가드** — 무대사, 닫힘이 전체 이벤트다. 군중·과장 0건.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — at most one person in the room and mostly hands: the magistrate Seolhwa's hands at the lid's edges from the sleeves of a dignified magistrate's hanbok — a young 21-year-old Korean woman, neat traditional hair with a simple jade hairpin, lips closed. One small wooden letter box on the low dark table, its lid lowered gently and squared closed. The lattice window beyond opens onto the autumn garden where the late flowers are falling. The residence room, not the palace bedchamber. No retrospective narration montage. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the afternoon light lying flat across the lid is the only light. The light stays calm, never flickering like horror, never strobing. No crushed blacks beyond the afternoon light's own depth, no milky flat darkness.

Recreate the 2 panels in order as one continuous ~10 second sequence:
1. 35mm medium: the lid lowered gently onto the box — one even, deliberate motion, the day's last task.
2. 35mm medium: the closed box squared on the low table — the room quiet around it.

CLOSE MOTION — IMPORTANT: physically-based the lid lowered evenly, the quiet room — the scene has no dialogue, the closing is the whole event: the lid comes down onto the box in one even deliberate motion with her hands at its edges, and the closed box rests squared on the low table as the afternoon light lies flat across the wood and the room holds its quiet; no retrospective narration montage; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.

---

## 8. S08 여덟째 — 사함 위 손 → 암전 (절대 52.5~60.0 · 콘티 2컷)

- **시트**: `downloads/EP97_S08_DIRECTOR_STORYBOARD_VARIABLE.jpg`
- **미장센 원장**: 100mm Macro → 엔드카드. 무대사 — 렌더 완전 무음. 자막: 제98화 「왕관 없는 세 그림자」에서 계속(편집 단계 삽입).
- **연출 특이**: **종지 썬(가변 2컷)** — 닫힌 사함 뚜껑 위에 얹힌 손 매크로 — 늦은 오후 빛이 고르게 낮아져 균일 암전(1), 타이틀 카드(편집 참조용). **암전 구간 인물 0명** — `no last flicker, no finale tableau` 가드.

- **프롬프트 전문**:

OUTPUT FORMAT — READ FIRST: the output video shows ONLY the filmed live-action scene, full-bleed, edge to edge, from the very first frame. The storyboard sheet's paper background, page layout, title, handwritten captions, logo and panel frames must NEVER appear on screen. No border, no rounded corners, no vignette, no viewfinder, no film-strip edges at any point.

Fictional historical period-drama film scene. Convert this director's storyboard sheet into a PHOTOREALISTIC CINEMATIC LIVE-ACTION historical K-drama sequence. The attached pencil-sketch storyboard is a LAYOUT/COMPOSITION GUIDE ONLY — follow its panel order and mise-en-scène, but render every frame as real filmed footage with real period locations.

Shot on ARRI Alexa 35, Panavision C-Series Anamorphic lens, 35mm film grain, 8k, masterclass cinematic lighting. Full rich cinematic color — NOT monochrome, NOT black and white, NOT animation, NOT 3D, NOT cartoon, NOT sketch style.

CHARACTER GUARD — a hand only, no face anywhere in the frame: a young woman magistrate's hand resting flat on the closed wooden letter box's lid, from the sleeve of a dignified magistrate's hanbok. The lattice window and the falling-flower garden lie soft behind. The residence room, not the palace bedchamber. No finale tableau, no looking back. No letterforms, no hangul, no hanja anywhere. All characters are adults. No harm to any person in the frame, no injury anywhere, no body anywhere, no fallen figure, no fighting, no combat.

LIGHT GUARD — IMPORTANT: the late afternoon light is the only light, and it dims evenly off the lid and the hand as the episode closes — the image goes to complete black, never flickering like horror, never strobing. No crushed blacks beyond the evening light's own depth, no milky flat darkness.

Recreate the 1 panel in order as one continuous ~10 second sequence (the sheet's second panel — the red next-episode title card — is edit-stage reference only and is NOT rendered):
1. 100mm macro: her hand resting flat on the closed box's lid — the last image before black; the late light dims evenly until complete black.

HAND MOTION — IMPORTANT: physically-based the hand on the lid, the even leaving of the light — the episode closes as an object and not as a statement: her hand rests flat on the closed box's lid without pressing, the late afternoon light dims evenly off the wood and the hand until nothing remains — complete black, held; no finale fanfare, no 'the end' mood; the render ends in complete black — the next-episode title is edit-stage only; the scene has no dialogue and stays fully silent, lips closed throughout, the render is fully silent. Do NOT follow the sketch's static lines — render as real filmed cinema.

Absolutely NO text, NO labels, NO panel borders, NO cut numbers, NO watermarks, NO storyboard lines, NO viewfinder grid in the output. Clean full-bleed cinematic frames only, like real filmed footage.
