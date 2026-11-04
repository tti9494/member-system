# 「혈화의 궐」 EP27 1·2차 자체 검수 체크리스트 (2026-11-05)

> **대상**: EP27 「두 번째 밀서」 가변 콘티 시트 8종(가변 28컷) + 실사 프롬프트 마스터 원장(`SAGEUK_EP27_VARIABLE_STORYBOARD_AND_PROMPTS.md`) + 보이스/SRT 원장
> **검수자**: 아르센 님 비서(크리) — 1차(파일·구조 물리) 및 2차(연출·안티슬롭·세이프·정합) 자체 검수. 상대(오이·코덱스) 검수 의존 없는 자체 완결 검수.
> **결함 이력**: 1차 렌더 8장 전부 통과 — 재렌더 0건. 1024×1536 해상도 8장 전량 정상(EP21~EP25에서 관찰된 1px 이탈 결함 미재현). 강채색 최고치 S08 1.33%는 마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**. 그 외 전장 0.22% 이하는 스케치 페이퍼 고유 온색·JPEG 크로마 노이즈(전 화 육안 검독 채색 요소 0건, 컬러 이입 아님).

---

## 1차 검수 (파일 생성·구조 물리 검수)

| # | 항목 | 기준 | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | 판정 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-1 | 파일 생성 | 8장 전부 존재 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-2 | 해상도 | 1024×1536 세로 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-3 | 상단 씬 헤더 | EP27-Sxx + 씬 제목 + SCENE/TIME/LOCATION/DIRECTOR/MOOD 메타 행 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-4 | 컷수 일치 | 설계 컷수=실제 패널 수 (4/4/3/4/3/3/4/3=28컷) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-5 | LENS/CAM/ACTION 표기 | 전 컷 3요소 기재(ACTION 공란 금지) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-6 | MOOD/DIRECTION 박스 | 하단 2박스, MOOD는 `reading exactly` 지문과 정자 일치 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-7 | 결함 유무 | 공란·잘림·파손·글리치·오타 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | **통과** |

**1차 실측 근거 (PIL 전량 실측 — 최종 렌더분 기준)**

| 파일 | 해상도 | 용량 | MD5(앞 8자) | 강채색 픽셀(sat>0.35) |
|---|---|---|---|---|
| EP27_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 1024×1536 | 3.54MB | `e4b34c3b` | 0.05% |
| EP27_S02_…jpg | 1024×1536 | 3.35MB | `15564b9a` | 0.11% |
| EP27_S03_…jpg | 1024×1536 | 3.44MB | `40afbfd6` | 0.22% |
| EP27_S04_…jpg | 1024×1536 | 3.64MB | `802e71bc` | 0.01% |
| EP27_S05_…jpg | 1024×1536 | 3.29MB | `cdd46551` | 0.03% |
| EP27_S06_…jpg | 1024×1536 | 3.56MB | `64b0a42e` | 0.07% |
| EP27_S07_…jpg | 1024×1536 | 3.62MB | `9441bd7f` | 0.08% |
| EP27_S08_…jpg | 1024×1536 | 3.20MB | `bee85b5b` | 1.33% |

강채색 잔존분은 전장 스케치 페이퍼 고유 온색 — S08의 1.33%를 제외한 전장 육안 검독으로 채색 요소 0건 확인(촛불·등불·단창 빛줄기 전부 흑백 명암 렌더, 컬러 이입 아님). S08의 1.33%는 마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**. 설계 컷수(4/4/3/4/3/3/4/3=28컷)와 패널 수 1:1 일치. 컷 배분은 EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)·EP26(3/4/3/4/3/4/3/4)과 다른 가변 배분으로 고정 컷 슬롭 회피.

---

## 2차 검수 (연출·안티슬롭·세이프·정합 검수)

| # | 항목 | 기준 | 결과 | 판정 |
|---|---|---|---|---|
| 2-1 | 텍스트 가독성 | 헤더·표기·노트 손글씨 판독 가능 | 8장 전부 영문 표기 판독 가능. MOOD 박스 8종 전부 지문과 정자 일치(① THE RUMOUR ARRIVES AS PAPER / ② THE READING NEVER LEAVES THE LINE / ③ SHE WEIGHS RUMOUR AGAINST EVIDENCE / ④ THE OLD KING WEPT OVER LEDGERS / ⑤ A DOUBT THE KING CANNOT SET DOWN / ⑥ THE LAMP BURNS TILL DAWN / ⑦ HE WILL NOT FOLD IT AWAY / ⑧ A WIND BEFORE THE SLEEPLESS THRONE) — 오타 0건. S08 3컷 한글 타이틀 「제28화 불면의 어전에서 계속」 단일 세로 열, 자형 정방향·왜곡 0건. S02 3컷의 단일 가독 라인은 정본 허용 규격(한 줄 이내 매크로) 준수 — 밀서 본문이 아닌 단일 조각, 나머지 열 전부 비판독 | **통과** |
| 2-2 | 화풍 일관성 | 정통 흑연 연필 소묘+크로스해칭, 스케치북 종이 질감 | 8장 동일 화풍. 컬러 이입·3D화·디지털 광택 0건. S08 3컷 적색 타이틀만 규격 의도 채색 | **통과** |
| 2-3 | 서사 흐름 | 정본 EP27 8썬표와 순서 일치 | S01 100mm Macro 소매·내관의 소매에서 스며 나오는 등사본 → S02 85mm 푸시인 읽는 왕의 눈·한 줄만 보인다 → S03 50mm 투숙 설화가 아뢴다(소문이냐 증거냐) → S04 100mm Macro 선대 임금의 산실 장부 이야기·곡을 하던 밤들 → S05 85mm 왕의 처음 고백 → S06 24mm 와이드 침전의 등불이 새벽까지 꺼지지 않음 → S07 100mm Macro 종이를 접는 손·밀서를 접지 않고 펴 둔 채 → S08 50mm 초인문 바람→암전→타이틀. 정본 1:1 일치 | **통과** |
| 2-4 | 캐릭터 앵커 정합 | plan 캐릭터 앵커 + characters.md | 이환 — **사복(암색 저녁 로브)+익선관, 붉은 곤룡포 아님**(S02·S03·S05 전컷 육안 확인 — plan 앵커 준수). 설화 — 다크 파스텔 궁녀 한복·**민무늬 옥비녀 단일 로드·귀걸이/가체/떨잠 0건**(S03·S05 전컷 육안 확인). 내관 — **회색 단령+흑색 관모, 소매 인물**(S01 — 어깨 아래만 프레이밍, 얼굴 노출 0건, 본화 신설 앵커 준수) | **통과** |
| 2-5 | 안티슬롭 — 밀서 전문 낭독 배제 | 글자 조각·비판독으로 치환 | S01 DIRECTION 'THE LETTER'S WRITING STAYS ILLEGIBLE TEXTURE — NEVER READABLE LETTERS', S02 DIRECTION 'THE PAGE IS NEVER READ ALOUD, NEVER SHOWN WHOLE' 명시. 렌더 프롬프트 `dense brush-written text rendered only as illegible calligraphic texture — no readable letters` 가드 상설 — 밀서 전문 노출·낭독 0건, S07 밀서는 펴 둔 채로도 붓글씨 질감 물증 렌더만 | **통과** |
| 2-6 | 안티슬롭 — 왕의 소름·과장 연출 배제 | 음성 연출로만 치환 | S02·S05 DIRECTION 'NO GOOSEBUMPS, NO SHAKING — THE TEARING IS CARRIED BY THE LOW BREATH ALONE' 명시, 렌더 프롬프트 `no goosebumps, no trembling hands, no melodrama` 가드 상설 — 소름·전율·발끈 시각 요소 0건, 왕이 아닌 자의 떨림은 S5 이환 보이스 음성 연출(사후 믹싱)로만 존재. 정본 지시문 "그 젊은 군주의 목소리에서 왕이 아닌 자의 떨림이 들렸다"와 정합 | **통과** |
| 2-7 | 선대 임금 회상 배제 | 장부·촛납 물증이 대신 증언 | S04 인물 일체 부재 — 산실 장부·고엽 촛납·묶인 장부만 렌더(DIRECTION 'THE LATE KING NEVER APPEARS — THE LEDGERS AND THE BURNED WAX TESTIFY ALONE'), 렌더 프롬프트 `no flashback, no figure` 가드 상설. EP26 '옥사가 증인' 규격 계승 | **통과** |
| 2-8 | 시즌2 킬러 컷 배정 준수 | EP27은 특수 훅 허용 화 아님 — 프리즈·슬로우 일체 미투입 | 정본 시즌2 킬러 컷 배정(EP30·EP41·EP49·EP50만 허용) 준수 — 특수 연출 훅 0건, S08은 프리즈가 아닌 바람→빛의 소멸 연출. 전 썬 통상 가변 호흡 | **통과** |
| 2-9 | 세이프 필터 | wound/blood/torture/weapon 어휘 전면 배제, 전원 성인 | 원장 블록 프롬프트 전수 조사 — blood·wound·gore·weapon·torture의 **긍정 사용 0건**(grep 전수 확인 — 부정 가드 `no violence, no blood anywhere` 8블록 상설만). 전 등장 인물 성인 명시(`All characters are adults`), 인물 없는 썬(S04·S06·S08) `No people anywhere` 명시 | **통과** |
| 2-10 | 광원 표기 | 시즌2 색 설계 — 촛불·달빛 냉온 교차 | 정본 AG ① 준수 — S01 `warm corridor lantern light against cold night moonlight`, S02~S05·S07 촛불 단일·냉온 교차 소스 명시, S06 `one warm lantern against cold night moonlight giving way to the grey of dawn`, S08 `one lantern at the gate the only warm source in the cold night wind` 상설. `no crushed blacks, no milky flat darkness` 전 썬 공통 — 광원 소스 명시로 완전 암부 슬롭 차단 | **통과** |
| 2-11 | 문자 슬롭 방지 (정본 AG ①) | 판독 가능한 글자 0건 — 한 줄 이내 규격 | S01 2·3컷·S04 2컷·S07 3컷 — `illegible calligraphic texture, no readable letters` 상설, 육안 확인 비판독. S02 3컷 단일 라인만 정본 허용 '한 줄 이내 매크로'로 가독(문장 왜곡 0건). 시트 S05 병풍·S08 편액의 의문자는 스케치 텍스처 — 렌더 프롬프트 클린 프레이밍 가드가 영상 전이 차단 | **통과** |
| 2-12 | 매크로 분포 | 매크로 연타 방지 + 휴먼 스케일 교차 | 매크로 12컷(S01 4·S04 4·S07 4 — 28컷 대비 43%) — S02·S03·S05 휴먼 스케일(85/50mm)·S06 와이드(24mm)가 매크로 썬 사이마다 개입해 연타 회피(S01→S02→S03→S04, S04→S05→S06→S07 모두 휴먼·와이드 썬 개입). S01 소매 매크로로 개회, S07 펴 둔 밀서 매크로 → S08 바람 50mm로 이행하며 수미상관 종결 | **통과** |
| 2-13 | 원장 7요소 8블록 완비 | 8블록 × 7문단(①~⑦) 누락 0 | 8블록 전부 ①시트 차단 ②화풍 전환 ③필름 룩 락 ④캐릭터 가드 ⑤광원 가드 ⑥컷 재현 ⑦물리·프레임 가드 순서로 완비(grep 전수 검증 — `OUTPUT FORMAT — READ FIRST`·`Convert this director's storyboard sheet`·`CHARACTER GUARD`·`LIGHT GUARD`·`Recreate the`·`MOTION — IMPORTANT`·`Absolutely NO text` 각 마커 8블록 기재 확인). 블록별 컷 수 = 시트 패널 수(4/4/3/4/3/3/4/3) 일치 | **통과** |
| 2-14 | 보이스·SRT 정합 | 정본 대사 1:1, 절대 타임코드 정렬 | 8썬 보이스표·SRT 5블록 작성. 절대 시각 2.0(내레이션)·17.5(설화)·24.5(내레이션)·32.0(이환)·58.0(자막) — 정본 rel 수치와 일치. 보이스 3종(내레이션 Wavenet-C·설화 Neural2-A·이환 Neural2-C) — 상이 계열 ID로 충돌 0건, 윤경헌·어의 본화 미등장 배정 제외. S2·S6·S7·S8 무대사 준수. 지정 효과음 0건(정본 썬표 미지정) — 앰비언스만 사후 믹싱 | **통과** |

**2차 검수 최종 판정**: 전 14개 검수 항목 100% 무결 통과 (PASS).

---

## 3. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP27_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536, 각 3.20~3.64MB) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP27_VARIABLE_STORYBOARD_AND_PROMPTS.md` |
| 생성기(재현용) | `projects/sageuk-revenge/ep27_sheets.py` (시트 8종 프롬프트 재생성, `python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP27_QC_CHECKLIST.md` (본 문서) |

**재렌더 시 주의**:
1. **1px 이탈**: 재렌더 시 반드시 PIL 실측으로 1024×1536 확인할 것 — 본화는 미발생이나 렌더러 결함 패턴이 EP21~EP25에서 관찰됨.
2. **밀서 문자 가드**: `illegible calligraphic texture, no readable letters` 가드 삭제 금지(정본 AG ①) — S02 3컷의 단일 라인도 렌더 프롬프트상 비판독 텍스처로 유지(영상에서 가독 텍스트는 왜곡 필연).
3. **소름 과장 배제 가드**: S02·S05 재렌더 시 `no goosebumps, no trembling hands, no melodrama` 가드 삭제 금지 — 왕이 아닌 자의 떨림은 음성 연출(사후 믹싱)로만 운반(정본 안티슬롭).
4. **내관 프레이밍 가드**: S01 재렌더 시 내관은 **어깨 아래만** 프레이밍 — 얼굴 노출 시 소매가 아닌 인물 드라마로 전락(정본 미장센 붕괴).
5. **이환 사복 가드**: `a dark informal royal everyday robe — not the red gonryongpo` 유지 — 붉은 곤룡포 이관 재현 방지. 관모는 `gold royal winged Ikseongwan crown with NO brim, not a gat` 인라인 강제 유지.
6. **설화 장식 금지 가드**: `a single plain jade hairpin only — no earrings, no gache, no tteoljam ornaments` 유지 — 가체·떨잠 이입 시 캐릭터 붕괴.
7. **선대 임금 회상 금지**: S04에 인물·회상 재투입 금지 — 장부·촛납 물증 렌더 유지(EP26 '옥사가 증인' 규격 계승).
8. **S08 엔드카드**: 마지막 패널은 흑바탕 **붉은 한글 타이틀 「제28화 불면의 어전에서 계속」 단일 세로 열** — 암전 프레임으로 되돌리면 정본 요구 불일치 재현. 단, 렌더 프롬프트상 S08 영상은 완전 암전으로 끝나고 타이틀은 편집 단계 삽입.
9. **킬러 컷 규율**: EP27에 프리즈·슬로우 훅 재투입 금지 — 시즌2 특수 훅은 EP30·EP41·EP49·EP50 전용.
10. **대사 무음 렌더**: 본 화는 대사·내레이션 4구가 존재하나 렌더는 무음 — 대사 지문을 프롬프트에 재투입하지 말 것(사후 믹싱 원장 별도).
