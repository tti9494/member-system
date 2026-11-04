# 「혈화의 궐」 EP28 1·2차 자체 검수 체크리스트 (2026-11-05)

> **대상**: EP28 「불면의 어전」 가변 콘티 시트 8종(가변 28컷) + 실사 프롬프트 마스터 원장(`SAGEUK_EP28_VARIABLE_STORYBOARD_AND_PROMPTS.md`) + 보이스/SRT 원장
> **검수자**: 아르센 님 비서(크리) — 1차(파일·구조 물리) 및 2차(연출·안티슬롭·세이프·정합) 자체 검수. 상대(오이·코덱스) 검수 의존 없는 자체 완결 검수.
> **결함 이력**: 1차 렌더 8장 전부 통과 — 재렌더 0건. 1024×1536 해상도 8장 전량 정상(EP21~EP25에서 관찰된 1px 이탈 결함 미재현). 강채색 최고치 S08 40.11%는 마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**. 본화는 스케치 페이퍼 톤이 EP27 배치보다 온색(크림)으로 나와 sat>0.35 전수치가 높게 측정되나, **가시 채색 한도(sat>0.35 ∧ v>0.25) 재측정 시 S01~S07 0.00%·S08 0.26%(색상 빈 0°=적, 타이틀 렌더뿐)** — 컬러 이입 아님, 육안 검독과 일치.

---

## 1차 검수 (파일 생성·구조 물리 검수)

| # | 항목 | 기준 | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | 판정 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-1 | 파일 생성 | 8장 전부 존재 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-2 | 해상도 | 1024×1536 세로 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-3 | 상단 씬 헤더 | EP28-Sxx + 씬 제목 + SCENE/TIME/LOCATION/DIRECTOR/MOOD 메타 행 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-4 | 컷수 일치 | 설계 컷수=실제 패널 수 (4/4/3/3/4/4/3/3=28컷) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-5 | LENS/CAM/ACTION 표기 | 전 컷 3요소 기재(ACTION 공란 금지) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-6 | MOOD/DIRECTION 박스 | 하단 2박스, MOOD는 `reading exactly` 지문과 정자 일치 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-7 | 결함 유무 | 공란·잘림·파손·글리치·오타 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | **통과** |

**1차 실측 근거 (PIL 전량 실측 — 최종 렌더분 기준)**

| 파일 | 해상도 | 용량 | MD5(앞 8자) | 강채색(sat>0.35) | 가시 채색(sat>0.35∧v>0.25) |
|---|---|---|---|---|---|
| EP28_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 1024×1536 | 3.49MB | `83f4e1e5` | 6.52% | 0.00% |
| EP28_S02_…jpg | 1024×1536 | 3.27MB | `ca196ae2` | 19.63% | 0.00% |
| EP28_S03_…jpg | 1024×1536 | 3.30MB | `f72e1cee` | 7.38% | 0.00% |
| EP28_S04_…jpg | 1024×1536 | 3.36MB | `a49fcc4e` | 8.59% | 0.00% |
| EP28_S05_…jpg | 1024×1536 | 3.50MB | `b58defc6` | 7.35% | 0.00% |
| EP28_S06_…jpg | 1024×1536 | 3.25MB | `00fa659a` | 5.85% | 0.00% |
| EP28_S07_…jpg | 1024×1536 | 3.50MB | `cb6987a3` | 10.32% | 0.00% |
| EP28_S08_…jpg | 1024×1536 | 3.27MB | `0bcb3315` | 40.11% | 0.26%(적색 빈 0°) |

본화 배치의 스케치 페이퍼가 EP27 대비 온색 크림톤으로 렌더되어 sat>0.35 전수치가 높게 나옴 — 가시 채색 한도 재측정으로 분리 실증: S01~S07 육안 검독 포함 채색 요소 0건(촛불·등불·화톳불·은수저 청록변색 전부 흑백 명암 렌더, 컬러 이입 아님). S08의 가시 채색 0.26%는 마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**. 설계 컷수(4/4/3/3/4/4/3/3=28컷)와 패널 수 1:1 일치. 컷 배분은 EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)·EP26(3/4/3/4/3/4/3/4)·EP27(4/4/3/4/3/3/4/3) 어느 것과도 다른 가변 배분으로 고정 컷 슬롭 회피.

---

## 2차 검수 (연출·안티슬롭·세이프·정합 검수)

| # | 항목 | 기준 | 결과 | 판정 |
|---|---|---|---|---|
| 2-1 | 텍스트 가독성 | 헤더·표기·노트 손글씨 판독 가능 | 8장 전부 영문 표기 판독 가능. MOOD 박스 8종 전부 지문과 정자 일치(① A SLEEPLESS KING, THIRD NIGHT / ② WHAT IS A KING IN A COUNTRY EATEN BY PAPER / ③ PAPER IS BEATEN BY A PERSON / ④ CAN PAPER REALLY BE BEATEN / ⑤ BEFORE THE LAUGHTER FILLS, THE KITCHEN STIRS / ⑥ THE SPOON FALLS, THE TASTER IS LED AWAY / ⑦ …POISON. / ⑧ THE SHADOW OF THE ROYAL KITCHEN) — 오타 0건. S08 3컷 한글 타이틀 「제29화 수라간의 그림자에서 계속」 단일 세로 열, 자형 정방향·왜곡 0건 | **통과** |
| 2-2 | 화풍 일관성 | 정통 흑연 연필 소묘+크로스해칭, 스케치북 종이 질감 | 8장 동일 화풍. 컬러 이입·3D화·디지털 광택 0건(가시 채색 실측 0.00% 실증). S08 3컷 적색 타이틀만 규격 의도 채색 | **통과** |
| 2-3 | 서사 흐름 | 정본 EP28 8썬표와 순서 일치 | S01 50mm 투숏 새벽 침전·옥새를 감싸 쥔 불면의 왕 → S02 85mm 왕이 약탕을 지키는 설화에게 질문 → S03 100mm Macro 그릇·설화가 약그릇을 내려놓음 → S04 85mm 왕이 처음으로 옅게 웃음 → S05 24mm 와이드 수라간·웃음이 차오르기 전에 불이 일어남 → S06 100mm Macro 떨어진 은수저·끌려 나가는 원경 → S07 85mm 왕의 웃음이 사라짐 → S08 50mm 등불이 달아오름→암전→타이틀. 정본 1:1 일치 | **통과** |
| 2-4 | 캐릭터 앵커 정합 | plan 캐릭터 앵커 + characters.md | 이환 — **사복(암색 저녁 로브)+익선관, 붉은 곤룡포 아님, 옥새를 감싸 쥔 불면의 피로**(S01·S02·S04·S07 전컷 육안 확인 — plan 앵커 준수). 설화 — 다크 파스텔 궁녀 한복·**민무늬 옥비녀 단일 로드·귀걸이/가체/떨잠 0건·약탕 그릇**(S02·S03 전컷 육안 확인). 시향 궁녀 — **원경 그림자로만 존재, 얼굴 노출 0건**(S06 3컷 한정, 본화 신설 앵커 준수) | **통과** |
| 2-5 | 안티슬롭 — 불면 몽타주 음악 과장 배제 | 초침 소리와 약탕 김의 리듬으로 치환 | S01 DIRECTION 'THE NIGHT IS CARRIED BY THE TICK OF TIME AND THE STEAM'S SLOW RHYTHM — NO MUSIC MONTAGE, NO EXAGGERATION' 명시, 렌더 프롬프트 `no music montage, no visual exaggeration of insomnia, no melodrama` 가드 상설 — 불면 몽타주·과장 연출 0건, 물시계 적하·약탕 김·낮은 호흡의 리듬으로만 운반. 정본 지시문과 정합 | **통과** |
| 2-6 | 안티슬롭 — 감정 중복 배제 | '종이를 이기는 사람'의 논리로 치환 | S03 DIRECTION 'SHE ANSWERS WITH LOGIC, NOT SYMPATHY — A PERSON BEATS PAPER, AND REMAINS' 명시, 렌더 프롬프트 `no tears, no shared sorrow, no melodrama` 가드 상설 — 동정·눈물·감정 동조 요소 0건, 설화의 응답은 서늘한 논리만 | **통과** |
| 2-7 | 세이프 — 독 시향 죽음 직접 묘사 전면 배제 | 은수저 매크로 + 원경 그림자 은유로 치환 | S06 — 시신·발작·구탁 렌더 0건, 떨어진 은수저(1·2·4컷 매크로)와 끌려 나가는 원경 그림자(3컷, 얼굴 노출 0건)만 렌더. DIRECTION 'THE DEATH IS NEVER SHOWN — A FALLEN SPOON AND A LED-AWAY SHADOW CARRY ALL OF IT' 명시, 렌더 프롬프트 `no graphic poison death, no vomit, no convulsing on screen` 가드 상설. 죽음은 내레이션(보고)으로만 운반(정본 AG ②) | **통과** |
| 2-8 | 옥새 인서트 분리 (정본 AG ①) | 05 연출표 S2 재사용 아님 — 옥새 클로즈업 인서트 분리 | S01 옥새 매크로를 2컷 인서트로 분리(50mm 투숙 개회 → 옥새 매크로 → 약탕 김 → 물시계), S04 3컷·S07 3컷의 옥새 그립은 상태 변화 서사(손가락 풀림→되감음)로 기능 — 중복 샷 아닌 인서트 분리 준수 | **통과** |
| 2-9 | 시즌2 킬러 컷 배정 준수 | EP28은 특수 훅 허용 화 아님 — 프리즈·슬로우 일체 미투입 | 정본 시즌2 킬러 컷 배정(EP30·EP41·EP49·EP50만 허용) 준수 — 특수 연출 훅 0건, S08은 프리즈가 아닌 등불 연쇄 점화→빛의 소멸 연출. 전 썬 통상 가변 호흡 | **통과** |
| 2-10 | 세이프 필터 | wound/blood/torture/weapon 어휘 전면 배제, 전원 성인 | 원장 블록 프롬프트 전수 조사 — blood·wound·gore·weapon·torture·vomit·convulsing의 **긍정 사용 0건**(grep 전수 확인 — 부정 가드 `no violence, no blood anywhere` 8블록 상설 + `no graphic poison death, no vomit, no convulsing on screen` S06 상설만). 전 등장 인물 성인 명시(`All characters are adults`), 인물 없는 썬(S05·S08 원경·전무) `No people anywhere` 명시 | **통과** |
| 2-11 | 광원 표기 | 시즌2 색 설계 — 새벽 냉광·등불 냉온 교차 | 정본 AG ① 준수 — S01~S04·S07 `the first cold dawn light through the high window against one warm lamp`, S05·S08 `cold dawn grey against warm torch and lamp flames`, S06 `warm torchlight lying along the cold stone corridor` 상설. `no crushed blacks, no milky flat darkness` 전 썬 공통 — 광원 소스 명시로 완전 암부 슬롭 차단 | **통과** |
| 2-12 | 문자 슬롭 방지 | 판독 가능한 글자 0건 | 본화 화면 요소에 문자 매체(밀서·장부·편액) 미등장 — 원장 블록 프롬프트 `no readable letters, no characters, no labels anywhere` 8블록 상설, 시트 병풍·편액 의문자는 스케치 텍스처 — 렌더 프롬프트 클린 프레이밍 가드가 영상 전이 차단. S06 은수저 변색도 `bluish-green tinge` 시각 표기 한도 — 문자 아님 | **통과** |
| 2-13 | 매크로 분포 | 매크로 연타 방지 + 휴먼 스케일 교차 | 매크로 12컷(S01 3·S03 2·S04 1·S06 3·S07 1 등 — 28컷 대비 43%) — S02·S03·S04·S07 휴먼 스케일(85/50mm)·S05 와이드(24mm)가 매크로 썬 사이마다 개입해 연타 회피. S01 물시계 매크로로 개회, S08 등불 50mm로 이행하며 수미상관 종결 | **통과** |
| 2-14 | 원장 7요소 8블록 완비 | 8블록 × 7문단(①~⑦) 누락 0 | 8블록 전부 ①시트 차단 ②화풍 전환 ③필름 룩 락 ④캐릭터 가드 ⑤광원 가드 ⑥컷 재현 ⑦물리·프레임 가드 순서로 완비(grep 전수 검증 — `OUTPUT FORMAT — READ FIRST`·`Convert this director's storyboard sheet`·`CHARACTER GUARD`·`LIGHT GUARD`·`Recreate the`·`MOTION — IMPORTANT`·`Absolutely NO text` 각 마커 블록 수 8+표기 확인). 블록별 컷 수 = 시트 패널 수(4/4/3/3/4/4/3/3) 일치 | **통과** |
| 2-15 | 보이스·SRT 정합 | 정본 대사 1:1, 절대 타임코드 정렬 | 8썬 보이스표·SRT 6블록 작성. 절대 시각 10.5(이환)·17.5(설화)·24.5(이환)·39.5(내레이션)·47.0(이환)·58.0(자막) — 정본 rel 수치(6.0/5.0/3.0/3.5/2.0)와 일치. 보이스 3종(내레이션 Wavenet-C·설화 Neural2-A·이환 Neural2-C) — 상이 계열 ID로 충돌 0건, 최상궁(Neural2-B)·윤경헌(Wavenet-D) 본화 미등장 배정 제외. S1·S8 무대사 준수. 지정 효과음 1건(S5 원거리 소동, 절대 31.5) — 정본 썬표 1:1, 사후 믹싱 | **통과** |

**2차 검수 최종 판정**: 전 15개 검수 항목 100% 무결 통과 (PASS).

---

## 3. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP28_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536, 각 3.25~3.50MB) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP28_VARIABLE_STORYBOARD_AND_PROMPTS.md` |
| 생성기(재현용) | `projects/sageuk-revenge/ep28_sheets.py` (시트 8종 프롬프트 재생성, `python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP28_QC_CHECKLIST.md` (본 문서) |

**재렌더 시 주의**:
1. **1px 이탈**: 재렌더 시 반드시 PIL 실측으로 1024×1536 확인할 것 — 본화는 미발생이나 렌더러 결함 패턴이 EP21~EP25에서 관찰됨.
2. **독 시향 가드**: S06 재렌더 시 `no graphic poison death, no vomit, no convulsing on screen` 가드 삭제 금지(정본 AG ②) — 시신·발작 렌더 시 안전 필터 차단 및 정본 미장센 붕괴. 시향 궁녀는 원경 그림자로만.
3. **불면 과장 배제 가드**: S01·S02 재렌더 시 `no music montage, no visual exaggeration of insomnia, no melodrama` 가드 삭제 금지 — 불면은 물시계·약탕 김·낮은 호흡의 리듬으로만 운반(정본 안티슬롭).
4. **감정 중복 배제 가드**: S03 재렌더 시 `no tears, no shared sorrow, no melodrama` 가드 삭제 금지 — 설화의 응답은 논리로만(정본 안티슬롭).
5. **이환 사복 가드**: `a dark informal royal everyday robe — not the red gonryongpo` 유지 — 붉은 곤룡포 이관 재현 방지. 관모는 `gold royal winged Ikseongwan crown with NO brim, not a gat` 인라인 강제 유지. 옥새(황색 비단 포 fold 속 금인) 앵커 병기 유지.
6. **설화 장식 금지 가드**: `a single plain jade hairpin only — no earrings, no gache, no tteoljam ornaments` 유지 — 가체·떨잠 이입 시 캐릭터 붕괴. 약탕 그릇(흑색 도기 김) 소품 앵커 유지.
7. **S05 원거리 규율**: 소동 인물은 끝까지 벌레만 하게 — 근접 인물·판독 가능한 얼굴 재투입 금지.
8. **S08 엔드카드**: 마지막 패널은 흑바탕 **붉은 한글 타이틀 「제29화 수라간의 그림자에서 계속」 단일 세로 열** — 암전 프레임으로 되돌리면 정본 요구 불일치 재현. 단, 렌더 프롬프트상 S08 영상은 완전 암전으로 끝나고 타이틀은 편집 단계 삽입.
9. **킬러 컷 규율**: EP28에 프리즈·슬로우 훅 재투입 금지 — 시즌2 특수 훅은 EP30·EP41·EP49·EP50 전용.
10. **대사 무음 렌더**: 본 화는 대사·내레이션 5구가 존재하나 렌더는 무음 — 대사 지문을 프롬프트에 재투입하지 말 것(사후 믹싱 원장 별도).
