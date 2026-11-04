# 「혈화의 궐」 EP24 1·2차 자체 검수 체크리스트 (2026-11-05)

> **대상**: EP24 「세 사람의 동맹」 가변 콘티 시트 8종(가변 28컷) + 실사 프롬프트 마스터 원장(`SAGEUK_EP24_VARIABLE_STORYBOARD_AND_PROMPTS.md`) + 보이스/SRT 원장
> **검수자**: 아르센 님 비서(크리) — 1차(파일·구조 물리) 및 2차(연출·안티슬롭·세이프·정합) 자체 검수. 상대(오이·코덱스) 검수 의존 없는 자체 완결 검수.
> **결함 이력**: 1차 렌더 8장 중 5장 통과, **재렌더 8건**(S05×6·S07×1·S02×1) 후 전량 통과. 본화의 재렌더 사유와 최종 조치:
> - **1px 이탈 2건**: S05 1차(1023×1537)·3차 재렌더(1023×1537)에서 연속 재현 — 재렌더로 복구, 최종본 전량 1024×1536. (EP21~EP23에서 관찰된 렌더러 결함 패턴의 재현)
> - **S05 왕 관모 앵커 이탈 3회 반복**: 1컷 '왕의 기상' 와이드 컷에서 이환 관모가 익선관 아닌 흑색 갓으로 렌더되는 어트랙터 3회 재현 — 가드 문구 강화만으로는 불복종, **컷 구도를 손·무릎 클로즈(관모 프레임 외)로 재설계**하여 구조적 차단. 서약의 무게는 로브 자락의 물리로 운반.
> - **S05 지도 문자 슬롭**: 2컷 지도에 글자형 잔존 — 지도를 백지 등고선 클로즈로 재설계하고 `no characters, no letters, no labels` 가드 적용, 최종본 판독 가능한 문자 0건.
> - **S07 촛대 개수 과다**: 1차 렌더에서 삼각형 3개 외 배경 가화 촛대 다수(EP21~22 '인원수 과다' 패턴의 개수형 재현) — `EXACTLY THREE lit candles, all other stands unlit` 개수 가드로 재렌더, 최종본 정확히 3불.
> - **잔채색 메모**: S08의 0.25% 강채색 픽셀은 마지막 패널 붉은 한글 타이틀(규격상 의도 채색), S04의 0.03%는 촛불 화염부 온색 잔채(EP21 0.21%·EP22 0.43% 수용 선례 이내). 나머지 6장 0.00%.

---

## 1차 검수 (파일 생성·구조 물리 검수)

| # | 항목 | 기준 | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | 판정 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-1 | 파일 생성 | 8장 전부 존재 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-2 | 해상도 | 1024×1536 세로 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-3 | 상단 씬 헤더 | EP24-Sxx + 씬 제목 + SCENE/TIME/LOCATION/DIRECTOR/MOOD 메타 행 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-4 | 컷수 일치 | 설계 컷수=실제 패널 수 (4/3/3/4/3/4/3/4=28컷) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-5 | LENS/CAM/ACTION 표기 | 전 컷 3요소 기재(ACTION 공란 금지) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-6 | MOOD/DIRECTION 박스 | 하단 2박스, MOOD는 `reading exactly` 지문과 정자 일치 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-7 | 결함 유무 | 공란·잘림·파손·글리치·오타 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | **통과** |

**1차 실측 근거 (PIL 전량 실측 — 최종 렌더분 기준)**

| 파일 | 해상도 | 용량 | MD5(앞 8자) | 강채색 픽셀(sat>0.35) |
|---|---|---|---|---|
| EP24_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 1024×1536 | 3.66MB | `6311ca33` | 0.00% |
| EP24_S02_…jpg | 1024×1536 | 3.81MB | `c0877a21` | 0.00% |
| EP24_S03_…jpg | 1024×1536 | 3.71MB | `5745750e` | 0.00% |
| EP24_S04_…jpg | 1024×1536 | 3.59MB | `ed094c9d` | 0.03% |
| EP24_S05_…jpg | 1024×1536 | 3.62MB | `499d2f89` | 0.00% |
| EP24_S06_…jpg | 1024×1536 | 3.80MB | `9fb09cf9` | 0.00% |
| EP24_S07_…jpg | 1024×1536 | 3.82MB | `a32d0ce0` | 0.00% |
| EP24_S08_…jpg | 1024×1536 | 3.40MB | `deac4c57` | 0.25% |

잔채색은 S08의 0.25%(마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**)와 S04의 0.03%(촛불 화염부 온색 잔채, 수용 선례 이내)뿐. 8장 전부 육안 검독 완료. 설계 컷수(4/3/3/4/3/4/3/4=28컷)와 패널 수 1:1 일치. 컷 배분은 EP20(4/3/4/3/3/4/3/4)·EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)과 다른 가변 배분으로 고정 컷 슬롭 회피.

---

## 2차 검수 (연출·안티슬롭·세이프·정합 검수)

| # | 항목 | 기준 | 결과 | 판정 |
|---|---|---|---|---|
| 2-1 | 텍스트 가독성 | 헤더·표기·노트 손글씨 판독 가능 | 8장 전부 영문 표기 판독 가능. MOOD 박스 8종 전부 지문과 정자 일치(① THREE CANDLES, THREE PEOPLE / ② A MISTAKE, MADE BY DESIGN / ③ A RUMOR, LAID LIKE A TRAP / ④ THE SCENE MUST BE THE THRONE ROOM / ⑤ A KING'S OATH, QUIETLY / ⑥ ONE SENTENCE, THE ONLY ONE / ⑦ THREE FLAMES STAND STRAIGHT / ⑧ THE LAST WINTER BEGINS) — 오타 0건. S08 3컷 한글 타이틀 「제25화 피날레: 혈화의 첫 꽃에서 계속」 단일 세로 열, 자형 정방향·왜곡 0건 | **통과** |
| 2-2 | 화풍 일관성 | 정통 흑연 연필 소묘+크로스해칭, 스케치북 종이 질감 | 8장 동일 화풍. 컬러 이입·3D화·디지털 광택 0건. S08 3컷 적색 타이틀만 규격 의도 채색 | **통과** |
| 2-3 | 서사 흐름 | 정본 EP24 8썬표와 순서 일치 | S01 24mm 와이드 삼촉대 삼각 배치·무결이 세 번째 자리 → S02 50mm 지도 펼침·실수 설계 → S03 85mm 설화 소문 공작·등사본 → S04 85mm 무결 보완(어전/역적 구분) → S05 50mm 왕의 서약 → S06 100mm Macro 무결의 유일한 맹세 → S07 24mm 와이드 세 불꽃 기울었다 곧게 → S08 35mm 첫서리→암전→타이틀. 정본 1:1 일치 | **통과** |
| 2-4 | 캐릭터 앵커 정합 | plan 캐릭터 앵커 + characters.md | 설화 — 민무늬 옥비녀 단일 로드(S01 2~4컷·S03 전컷·S06 4컷 손·S07 전컷), 귀걸이/가체/떨잠 0건 육안 확인. 무결 — 남색 융복·뺨 검흔 흉터·흰 붕대(S01 3~4컷·S04 1·2·4컷·S06 1~2컷·S07 전컷), hwan-do 착용. 이환 — 사복/익선관(S01 2·4컷·S02 전컷·S04 3컷·S05 3컷·S07 전컷). S05 1~2컷은 관모 리스크 차단을 위한 손·종이 클로즈(의도 설계). 윤경헌 미등장 | **통과** |
| 2-5 | 안티슬롭 — 동맹 고함·팀 슬롭 배제 | 각자의 역할 분담 + 무결의 단 한 문장 맹세 | S01 DIRECTION 'THE ALLIANCE IS A FACT — NOT A SHOUTED OATH'·'NO TEAM LANGUAGE, NO HANDSHAKE' 명시, S05 'NO SHOUTED OATH, NO RAISED CUP', S06 'NO HANDSHAKE, NO OATH CIRCLE' 명시. 렌더 프롬프트 `the alliance stated as quiet fact — no shouted oath, no raised cup, no handshake, no team language` 전 블록 상설(원장 0-2 규칙 6). 고함 선언·"우리는 이제 팀이다"식 현대어 슬롭 시각 요소 0건 | **통과** |
| 2-6 | EP17 규장각 밀실 동세트 회피 | 촛불 배열 변화 + 카메라 앵글 반전 | EP17(탁자 위 놋촛대 3개·창호지 창 역광·창→향 앵글)과 대비 — 본화는 **바닥 높은 목재 촛대 3개 넓은 삼각형 배치**(시트 전 컷), **문 쪽에서 서가를 향하는 반전 앵글**(S07 문풍 광선 입사 방향으로 확인), **창 역광 0건**, 서가 배경. 원장 LIGHT GUARD에 `no window light anywhere` 상설 | **통과** |
| 2-7 | 세이프 필터 | wound/blood 어휘 전면 배제, 전원 성인 | 원장 블록 프롬프트 전수 조사 — wound·blood 출현 0건(붕대는 AG 지정 어휘 `white cloth bandage wrapping firmly over the shoulder` / `clean bandaged skin`로만 렌더). 절규·과장 고통 0건, 전 등장 인물 성인 명시 | **통과** |
| 2-8 | 광원 표기 | S01~S07 바닥 삼각 촛대 3불 / S08 콜드 야경 | 시트 TIME 표기 'NIGHT CANDLELIGHT'(S01~S07)·'NIGHT, FIRST FROST'(S08), 렌더 라이트 가드 `the three candles on tall wooden floor stands set in a wide triangle are the only light source … no window light anywhere`(S01~S07)·`cold blue starlit night is the only source, no lamp`(S08) 상설. `deep shadow areas must keep readable detail — no crushed blacks, no milky flat darkness` 전 썬 공통 | **통과** |
| 2-9 | 문자 슬롭 방지 | 지도·등사본 등 판독 가능한 글자 0건 | S02·S05 지도 — `pure blank white paper carrying only faint contour lines … no characters, no letters, no labels` 상설, 최종 시트 등고선·지형 기호만. S03 등사본 — `a seal mark and fold lines only, no readable writing anywhere on it`. 1차 S05 지도 글자형 잔존 결함 → 구도 재설계 재렌더로 해소 | **통과** |
| 2-10 | 매크로 분포 | 매크로 연타 방지 + 휴먼 스케일 교차 | 매크로 4컷(S06 집중 배치) — S01~S05·S07은 24~85mm 휴먼 스케일과 교차, S06 매크로로 맹세 강조, S08 와이드→암전 수미상관. 매크로 연타 0건 | **통과** |
| 2-11 | 원장 7요소 8블록 완비 | 8블록 × 7문단(①~⑦) 누락 0 | 8블록 전부 ①시트 차단 ②화풍 전환 ③필름 룩 락 ④캐릭터 가드 ⑤광원 가드 ⑥컷 재현 ⑦물리·프레임 가드 순서로 완비(grep 전수 검증 — `OUTPUT FORMAT — READ FIRST`·`CHARACTER GUARD`·`LIGHT GUARD`·`Recreate the`·`MOTION — IMPORTANT`·`Absolutely NO text` 각 마커 8블록 기재). 블록별 컷 수 = 시트 패널 수(4/3/3/4/3/4/3/4) 일치 | **통과** |
| 2-12 | 보이스·SRT 정합 | 정본 대사 1:1, 절대 타임코드 정렬 | 8썬 보이스표·SRT 8블록 작성. 절대 시각 2.0(내레이션)·9.5(이환)·17.5(설화)·25.0(무결)·32.5(이환)·39.5(무결)·54.5(내레이션)·57.0(자막) — 정본 rel 수치와 일치. 보이스 4종 — 무결·내레이션 동일 ID(Wavenet-C)는 Pitch(-1.5/0.0)·톤 지문으로 구분, 본화는 S01·S08(내레이션)과 S04·S06(무결)이 떨어져 직접 대화 충돌 0건. S7 무대사 준수. 지정 효과음 0건(정본 썬표 준수) | **통과** |

**2차 검수 최종 판정**: 전 12개 검수 항목 100% 무결 통과 (PASS).

---

## 3. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP24_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536, 각 3.40~3.82MB) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP24_VARIABLE_STORYBOARD_AND_PROMPTS.md` |
| 생성기(재현용) | `projects/sageuk-revenge/ep24_sheets.py` (시트 8종 프롬프트 재생성, `python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP24_QC_CHECKLIST.md` (본 문서) |

**재렌더 시 주의**:
1. **1px 이탈**: 재렌더 시 반드시 PIL 실측으로 1024×1536 확인할 것 — 본화에서도 2회 재현 후 재렌더로 복구.
2. **S05 1컷 구도**: '왕의 기상' 전신 와이드로 되돌리면 흑색 갓 이탈이 재현됨(3회 실증) — 손·무릎 클로즈 구도 유지할 것.
3. **S07 촛불 개수**: `EXACTLY THREE lit candles, all other stands unlit` 가드 삭제 금지 — 가드 없이 배경 가화 촛대 다수 렌더 재현(1차 실증).
4. **지도·등사본 문자 슬롭**: `no characters, no letters, no labels` 가드 유지 — 백지 등고선·봉인 접힘으로만.
5. **동맹 고함 가드**: `no shouted oath, no raised cup, no handshake, no team language` 가드 삭제 금지(정본 안티슬롭).
6. **EP17 동세트 회피**: 촛대는 바닥 삼각형 배치 + 문→서가 반전 앵글 + `no window light anywhere` 유지.
7. **대사 무음 렌더**: 본 화는 전 썬 대사가 존재하나 렌더는 무음 — 대사 지문을 프롬프트에 재투입하지 말 것(사후 믹싱 원장 별도).
