# 「혈화의 궐」 EP26 1·2차 자체 검수 체크리스트 (2026-11-05)

> **대상**: EP26 「옥사의 미소」(시즌2 개회) 가변 콘티 시트 8종(가변 28컷) + 실사 프롬프트 마스터 원장(`SAGEUK_EP26_VARIABLE_STORYBOARD_AND_PROMPTS.md`) + 보이스/SRT 원장
> **검수자**: 아르센 님 비서(크리) — 1차(파일·구조 물리) 및 2차(연출·안티슬롭·세이프·정합) 자체 검수. 상대(오이·코덱스) 검수 의존 없는 자체 완결 검수.
> **결함 이력**: 1차 렌더 8장 전부 통과 — 재렌더 0건. 1024×1536 해상도 8장 전량 정상(EP21~EP25에서 관찰된 1px 이탈 결함 미재현). 강채색 최고치 S05 1.03%는 육안 검독으로 채색 요소 0건 — 스케치 페이퍼 고유 온색·JPEG 크로마 노이즈(전 화 평균 색차 실측 R−B ≈ +8 균일, 컬러 이입 아님).

---

## 1차 검수 (파일 생성·구조 물리 검수)

| # | 항목 | 기준 | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | 판정 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-1 | 파일 생성 | 8장 전부 존재 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-2 | 해상도 | 1024×1536 세로 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-3 | 상단 씬 헤더 | EP26-Sxx + 씬 제목 + SCENE/TIME/LOCATION/DIRECTOR/MOOD 메타 행 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-4 | 컷수 일치 | 설계 컷수=실제 패널 수 (3/4/3/4/3/4/3/4=28컷) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-5 | LENS/CAM/ACTION 표기 | 전 컷 3요소 기재(ACTION 공란 금지) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-6 | MOOD/DIRECTION 박스 | 하단 2박스, MOOD는 `reading exactly` 지문과 정자 일치 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-7 | 결함 유무 | 공란·잘림·파손·글리치·오타 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | **통과** |

**1차 실측 근거 (PIL 전량 실측 — 최종 렌더분 기준)**

| 파일 | 해상도 | 용량 | MD5(앞 8자) | 강채색 픽셀(sat>0.35) |
|---|---|---|---|---|
| EP26_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 1024×1536 | 3.54MB | `632ae557` | 0.06% |
| EP26_S02_…jpg | 1024×1536 | 3.71MB | `abf53fec` | 0.18% |
| EP26_S03_…jpg | 1024×1536 | 3.61MB | `711b8a14` | 0.00% |
| EP26_S04_…jpg | 1024×1536 | 3.94MB | `1dac0fe0` | 0.01% |
| EP26_S05_…jpg | 1024×1536 | 3.62MB | `07deda11` | 1.03% |
| EP26_S06_…jpg | 1024×1536 | 3.60MB | `302bc066` | 0.10% |
| EP26_S07_…jpg | 1024×1536 | 3.85MB | `c9ade31f` | 0.12% |
| EP26_S08_…jpg | 1024×1536 | 3.25MB | `f65ba624` | 0.30% |

강채색 잔존분은 S05의 1.03% 포함 전장 스케치 페이퍼 고유 온색 — 8장 전부 육안 검독으로 채색 요소 0건 확인(촛불·김·단창 빛줄기 전부 흑백 명암 렌더, 컬러 이입 아님). S08의 0.30%는 마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색**. 설계 컷수(3/4/3/4/3/4/3/4=28컷)와 패널 수 1:1 일치. 컷 배분은 EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)·EP25(4/3/4/3/3/3/4/4)과 다른 가변 배분으로 고정 컷 슬롭 회피.

---

## 2차 검수 (연출·안티슬롭·세이프·정합 검수)

| # | 항목 | 기준 | 결과 | 판정 |
|---|---|---|---|---|
| 2-1 | 텍스트 가독성 | 헤더·표기·노트 손글씨 판독 가능 | 8장 전부 영문 표기 판독 가능. MOOD 박스 8종 전부 지문과 정자 일치(① THE SMILE DEEPENS THE CASE / ② ONE BY ONE, THE WELLS CLOSE / ③ SHE COUNTS THE VISITORS / ④ A RUMOUR THAT SURVIVED THE FIRE / ⑤ A LETTER MADE TO BE SUSPECTED / ⑥ EYES ON THE STEAM ONLY / ⑦ THE PRISON KEEPS ITS SILENCE / ⑧ THE LIGHT GOES OUT) — 오타 0건. S08 4컷 한글 타이틀 「제27화 두 번째 밀서에서 계속」 단일 세로 열, 자형 정방향·왜곡 0건. S04 등사본 패널은 화면 내 문자가 아니라 봉인·그을음·붓글씨 질감 물증 렌더(2-9 참조) | **통과** |
| 2-2 | 화풍 일관성 | 정통 흑연 연필 소묘+크로스해칭, 스케치북 종이 질감 | 8장 동일 화풍. 컬러 이입·3D화·디지털 광택 0건. S08 4컷 적색 타이틀만 규격 의도 채색 | **통과** |
| 2-3 | 서사 흐름 | 정본 EP26 8썬표와 순서 일치 | S01 100mm Macro 단창 빛줄기·윤경헌 입가 미소 → S02 85mm 투숙 늙은 정승의 어전 보고(이자가 하나씩 물에 빠져 죽는다는 전언) → S03 50mm 다과 쟁반·설화의 시선으로 옥사 드나드는 자들 계수 → S04 100mm Macro 등사본 소문의 조각(그을음 흉터) → S05 85mm 밀실·왕이 결론부터 말함 → S06 85mm 설화의 대답·다과의 김만 바라봄 → S07 24mm 와이드 옥사의 밤·창밖 설하치(무대사) → S08 100mm Macro 빛줄기가 꺼짐→암전→타이틀. 정본 1:1 일치 | **통과** |
| 2-4 | 캐릭터 앵커 정합 | plan 캐릭터 앵커 + characters.md | 윤경헌 — **옥사 죄인복(염색 없는 소복·관모·장식 일체 부재)·회색 수염·매의 눈**, S01·S08 전컷 **입가+수염만 프레이밍(얼굴 전체 노출 0건 — 정본 비판 검수 준수)**. 설화 — 다크 파스텔 궁녀 한복·**민무늬 옥비녀 단일 로드·귀걸이/가체/떨잠 0건**(S03·S05·S06 전컷 육안 확인), 다과 쟁반 실중량. 이환 — **사복(암색 저녁 로브)+익선관, 붉은 곤룡포 아님**(S02·S05·S06 — plan 앵커 준수, EP25 대조 의전 붉은 곤룡포와 차별). 늙은 정승(어의) — 단령·사모·백색 수염(S02) | **통과** |
| 2-5 | 안티슬롭 — 고문 회상·익사 직접 묘사 배제 | 전언·은유로만 치환 | S01 DIRECTION 'THE MENACE IS A SMILE, NOT A SCENE — NO TORTURE, NO FLASHBACK' 명시, S02 DIRECTION 'THE DEATHS ARE SPOKEN, NEVER SHOWN — THE HALL KEEPS ITS SILENCE' 명시, S07 DIRECTION 'THE WELL KEEPS ITS SILENCE — THE SNOW SAYS WHAT IS LOST' 명시. 렌더 프롬프트 `No torture, no flashback`·`No deaths shown, no bodies, no drowning` 가드 상설 — 옥졸 익사·고문 도구·시신·절규 시각 요소 0건, 익사는 대사로만 존재 | **통과** |
| 2-6 | 입가 전용 프레이밍 (정본 비판 검수) | S01·S08 웃는 입가만, 얼굴 전체 노출 회피 | S01·S08 렌더 프롬프트 `only the lower half of the face, never the whole face, never the eyes in full light` 가드 상설(공통 규칙 6), 시트 양쪽 육안 확인 — 칼날 빛 속 수염+입가 마이크로 클로즈업, 눈·이마 풀 노출 0건. 기존 연출표의 배경 인물 혼동 리스크 차단 | **통과** |
| 2-7 | 시즌2 킬러 컷 배정 준수 | EP26은 특수 훅 허용 화 아님 — 프리즈·슬로우 일체 미투입 | 정본 시즌2 킬러 컷 배정(EP30·EP41·EP49·EP50만 허용) 준수 — S05 낙하 프리즈(EP25)류 특수 훅 0건, S08은 프리즈가 아닌 빛의 소멸(수미상관) 연출. 전 썬 통상 가변 호흡 | **통과** |
| 2-8 | 세이프 필터 | wound/blood/torture/drowning 어휘 전면 배제, 전원 성인 | 원장 블록 프롬프트 전수 조사 — blood·wound·gore·torture·drowning의 **긍정 사용 0건**(grep 전수 확인 — 부정 가드 `no violence, no blood anywhere`·`No torture, no flashback`·`no bodies, no drowning` 8블록 상설 + 규칙 행 금지 명시만). 전 등장 인물 성인 명시(`All characters are adults`) | **통과** |
| 2-9 | 광원 표기 | 시즌2 색 설계 — 옥사 칼날 빛 / 궁 안 촛불·달빛 냉온 교차 | 정본 AG ① 준수 — S01·S08 `one knife of cold night light through the small barred window is the only source, the rest of the prison pitch-black`, S02~S06 `warm candle lantern light against cold night moonlight — the season's cold-warm cross`, S07 `the single barred window's light in a night of falling snow` 상설. `no crushed blacks, no milky flat darkness` 전 썬 공통 — 칼날 빛 소스 명시로 완전 암부 슬롭 차단 | **통과** |
| 2-10 | 문자 슬롭 방지 | 등사본 판독 가능한 글자 0건 | S04 등사본 — `dense vertical columns of transcribed brush-written text rendered only as illegible calligraphic texture, no readable letters, no characters, no labels` 상설, 최종 시트 봉인·그을음 흉터·붓글씨 질감만(육안 확인). S05 밀서는 접힌 상태로 등장(글자 노출 0건). 어전·옥사 편액 등 건축 문자는 클린 프레이밍 가드로 전면 차단 | **통과** |
| 2-11 | 매크로 분포 | 매크로 연타 방지 + 휴먼 스케일 교차 | 매크로 9컷(S01 3+S04 4+S08 2) — S02·S03·S05·S06은 50~85mm 휴먼 스케일과 교차, S07 24mm 와이드로 개방. 매크로 3썬이 연속이지만 S03·S05 휴먼 스케일이 사이에 개입해 연타 회피, S01 입가 매크로로 개회·S08 빛 소멸 매크로로 수미상관 | **통과** |
| 2-12 | 원장 7요소 8블록 완비 | 8블록 × 7문단(①~⑦) 누락 0 | 8블록 전부 ①시트 차단 ②화풍 전환 ③필름 룩 락 ④캐릭터 가드 ⑤광원 가드 ⑥컷 재현 ⑦물리·프레임 가드 순서로 완비(grep 전수 검증 — `OUTPUT FORMAT — READ FIRST`·`CHARACTER GUARD`·`LIGHT GUARD`·`Recreate the`·`MOTION — IMPORTANT`·`Absolutely NO text` 각 마커 8블록 기재 확인). 블록별 컷 수 = 시트 패널 수(3/4/3/4/3/4/3/4) 일치 | **통과** |
| 2-13 | 보이스·SRT 정합 | 정본 대사 1:1, 절대 타임코드 정렬 | 8썬 보이스표·SRT 7블록 작성. 절대 시각 2.5(윤경헌)·9.5(어의)·17.0(설화)·24.5(내레이션)·32.0(이환)·39.5(설화)·58.0(자막) — 정본 rel 수치와 일치. 보이스 5종 — 어의·이환 동일 ID(Neural2-C)는 발화 썬 분리(S2→S5)·톤 지문 구분으로 충돌 0건, 내레이션(Wavenet-C)·설화(Neural2-A)·윤경헌(Wavenet-D)은 상이 계열. S7·S8 무대사 준수. 지정 효과음 0건(정본 썬표 미지정) — 앰비언스만 사후 믹싱 | **통과** |

**2차 검수 최종 판정**: 전 13개 검수 항목 100% 무결 통과 (PASS).

---

## 3. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP26_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536, 각 3.25~3.94MB) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP26_VARIABLE_STORYBOARD_AND_PROMPTS.md` |
| 생성기(재현용) | `projects/sageuk-revenge/ep26_sheets.py` (시트 8종 프롬프트 재생성, `python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP26_QC_CHECKLIST.md` (본 문서) |

**재렌더 시 주의**:
1. **1px 이탈**: 재렌더 시 반드시 PIL 실측으로 1024×1536 확인할 것 — 본화는 미발생이나 렌더러 결함 패턴이 EP21~EP25에서 관찰됨.
2. **입가 전용 가드**: S01·S08 재렌더 시 `only the lower half of the face, never the whole face` 가드 삭제 금지 — 얼굴 전체 노출 시 배경 인물 혼동 리스크 재현(정본 비판 검수).
3. **익사 은유 가드**: `the prison keeps its silence` 은유 유지 — 옥졸 익사를 화면에 직접 묘사하면 정본 AG ② 위반 재현.
4. **이환 사복 가드**: `a dark informal royal everyday robe — not the red gonryongpo` 유지 — EP25 대조 의전 붉은 곤룡포 이관 재현 방지. 관모는 `gold royal winged Ikseongwan crown with NO brim, not a gat` 인라인 강제 유지.
5. **설화 장식 금지 가드**: `a single plain jade hairpin only — no earrings, no gache, no tteoljam ornaments` 유지 — 가체·떨잠 이입 시 캐릭터 붕괴.
6. **S08 엔드카드**: 마지막 패널은 흑바탕 **붉은 한글 타이틀 「제27화 두 번째 밀서에서 계속」 단일 세로 열** — 암전 프레임으로 되돌리면 정본 요구 불일치 재현. 단, 렌더 프롬프트상 S08 영상은 완전 암전으로 끝나고 타이틀은 편집 단계 삽입.
7. **킬러 컷 규율**: EP26에 프리즈·슬로우 훅 재투입 금지 — 시즌2 특수 훅은 EP30·EP41·EP49·EP50 전용.
8. **대사 무음 렌더**: 본 화는 대사 5구가 존재하나 렌더는 무음 — 대사 지문을 프롬프트에 재투입하지 말 것(사후 믹싱 원장 별도).
