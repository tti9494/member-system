# 「혈화의 궐」 EP25 1·2차 자체 검수 체크리스트 (2026-11-05)

> **대상**: EP25 「피날레: 혈화의 첫 꽃」(시즌1 피날레) 가변 콘티 시트 8종(가변 28컷) + 실사 프롬프트 마스터 원장(`SAGEUK_EP25_VARIABLE_STORYBOARD_AND_PROMPTS.md`) + 보이스/SRT 원장
> **검수자**: 아르센 님 비서(크리) — 1차(파일·구조 물리) 및 2차(연출·안티슬롭·세이프·정합) 자체 검수. 상대(오이·코덱스) 검수 의존 없는 자체 완결 검수.
> **결함 이력**: 1차 렌더 8장 중 6장 통과, **재렌더 2건**(S01×1·S08×1) 후 전량 통과. 본화의 재렌더 사유와 최종 조치:
> - **1px 이탈 1건**: S01 1차(1023×1537)에서 연속 재현(EP21~EP24에서 관찰된 렌더러 결함 패턴) — 재렌더로 복구, 최종본 전량 1024×1536.
> - **S08 엔드카드 누락 1건**: 1차 설계에서 S08 마지막 패널을 암전 프레임으로 두어 정본 요구(마지막 패널 = 흑바탕 붉은 한글 타이틀 단일 세로 열)와 불일치 — EP24 규격(시트에 타이틀 카드 패널 포함, 렌더는 암전 종료)에 맞춰 4컷 구성 [미소 → 두 번째 밀서 → 암전 → 붉은 타이틀]으로 재설계·재렌더. 최종본 「제2시즌 권신의 덫에서 계속」 단일 세로 열 렌더 확인.
> - **잔채색 메모**: S08의 강채색 픽셀은 마지막 패널 붉은 한글 타이틀(규격상 의도 채색)과 흑백 패널 경계부 JPEG 크로마 노이즈. S01~S07은 0.00~0.01%(스케치 페이퍼 고유 온색 — 전 화 평균 색차 실측 R−B ≈ +8로 8장 균일, 컬러 이입 아님). 나머지 전장 이상 없음.

---

## 1차 검수 (파일 생성·구조 물리 검수)

| # | 항목 | 기준 | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | 판정 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-1 | 파일 생성 | 8장 전부 존재 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-2 | 해상도 | 1024×1536 세로 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-3 | 상단 씬 헤더 | EP25-Sxx + 씬 제목 + SCENE/TIME/LOCATION/DIRECTOR/MOOD 메타 행 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-4 | 컷수 일치 | 설계 컷수=실제 패널 수 (4/3/4/3/3/3/4/4=28컷) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-5 | LENS/CAM/ACTION 표기 | 전 컷 3요소 기재(ACTION 공란 금지) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-6 | MOOD/DIRECTION 박스 | 하단 2박스, MOOD는 `reading exactly` 지문과 정자 일치 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **통과** |
| 1-7 | 결함 유무 | 공란·잘림·파손·글리치·오타 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | 없음 | **통과** |

**1차 실측 근거 (PIL 전량 실측 — 최종 렌더분 기준)**

| 파일 | 해상도 | 용량 | MD5(앞 8자) | 강채색 픽셀(sat>0.35) |
|---|---|---|---|---|
| EP25_S01_DIRECTOR_STORYBOARD_VARIABLE.jpg | 1024×1536 | 3.65MB | `1874f806` | 0.01% |
| EP25_S02_…jpg | 1024×1536 | 3.71MB | `7b5be002` | 0.00% |
| EP25_S03_…jpg | 1024×1536 | 3.68MB | `61ae75e3` | 0.01% |
| EP25_S04_…jpg | 1024×1536 | 3.78MB | `7b9d9ecc` | 0.01% |
| EP25_S05_…jpg | 1024×1536 | 3.93MB | `f911ed2a` | 0.31% |
| EP25_S06_…jpg | 1024×1536 | 3.93MB | `b7721943` | 0.20% |
| EP25_S07_…jpg | 1024×1536 | 3.83MB | `cbfd9bf4` | 0.00% |
| EP25_S08_…jpg | 1024×1536 | 3.32MB | `20ccae11` | 0.39% |

강채색 잔존분은 S08의 0.39%(마지막 패널 **붉은 한글 타이틀 — 규격상 의도 채색** + 암전 패널 경계부 크로마 노이즈)와 S05·S06의 산발 노이즈(육안 검독으로 채색 요소 0건 확인 — 스케치 페이퍼 고유 온색, 전 화 평균 색차 실측 R−B ≈ +8로 8장 균일). 8장 전부 육안 검독 완료. 설계 컷수(4/3/4/3/3/3/4/4=28컷)와 패널 수 1:1 일치. 컷 배분은 EP20(4/3/4/3/3/4/3/4)·EP21(3/3/4/3/3/4/4/4)·EP22(4/4/3/3/3/4/3/4)·EP23(3/4/4/3/4/3/4/3)·EP24(4/3/3/4/3/4/3/4)과 다른 가변 배분으로 고정 컷 슬롭 회피.

---

## 2차 검수 (연출·안티슬롭·세이프·정합 검수)

| # | 항목 | 기준 | 결과 | 판정 |
|---|---|---|---|---|
| 2-1 | 텍스트 가독성 | 헤더·표기·노트 손글씨 판독 가능 | 8장 전부 영문 표기 판독 가능. MOOD 박스 8종 전부 지문과 정자 일치(① THE LAST MORNING OF THE REGIME / ② ONE QUESTION, TEN YEARS OLD / ③ THE BREATH STOPS / ④ SEAL, STAMP, HANDWRITING — INTACT / ⑤ ONE INSTANT, HELD / ⑥ NO ONE COMES / ⑦ THE FIRST WITNESS STANDS / ⑧ THE ROOT REMAINS) — 오타 0건. S08 4컷 한글 타이틀 「제2시즌 권신의 덫에서 계속」 단일 세로 열, 자형 정방향·왜곡 0건. S04 문서 패널은 화면 내 문자가 아니라 봉인·낙관·붓글씨 질감 물증 렌더(2-9 참조) | **통과** |
| 2-2 | 화풍 일관성 | 정통 흑연 연필 소묘+크로스해칭, 스케치북 종이 질감 | 8장 동일 화풍. 컬러 이입·3D화·디지털 광택 0건. S08 4컷 적색 타이틀만 규격 의도 채색 | **통과** |
| 2-3 | 서사 흐름 | 정본 EP25 8썬표와 순서 일치 | S01 50mm 로우앵글 대조의 아침·윤경헌 입궁 → S02 85mm 어전 질문(이명진 옥사) → S03 85mm 윤경헌의 얼굴이 굳는 4단 붕괴 → S04 50mm 원본 하강(봉인·낙관·친필 그대로)·"너다." → S05 85mm 낙하 충격 프리즈 → S06 24mm 와이드 윤경헌의 고함·근왕병 부재·내금위 어전 장악 → S07 85mm 중전 첫 증인·조용한 명의 체포 → S08 100mm Macro 옥사 속 미소·두 번째 밀서→암전→타이틀. 정본 1:1 일치 | **통과** |
| 2-4 | 캐릭터 앵커 정합 | plan 캐릭터 앵커 + characters.md | 이환 — **붉은 곤룡포(용금 수농)+익선관, 브림 없는 금관**(S01 4컷·S02 전컷·S04 3컷·S07 4컷) — 대조 정식 의전으로 EP24 사복과 다름 확인. 윤경헌 — 흑색 사모·단령 관복·백옥 흉배·회색 수염·매의 눈(S01 2~3컷·S02 2컷·S03 전컷·S06 전컷·S07 3~4컷·S08 1컷), S03 4단계 표정 붕괴·S06 사모 비뚤어짐까지 정본 지문 반영. 중전 윤씨 — 자수 당의·떨잠·첩지 가체(S07 1~2컷), 무언·눈 하강 준수. S08 윤경헌은 옥사 칼날 빛 속 미소(같은 앵커 유지) | **통과** |
| 2-5 | 안티슬롭 — 체포 고함·안도 마무리 배제 | 왕의 조용한 단문 "너다." + 개회형 엔딩 | S04 DIRECTION 'THE VERDICT IS ONE QUIET SENTENCE — NO POINTED RAGE, NO SHOUTED ARREST' 명시, S05 프리즈·S07 'THE ARREST IS A QUIET COMMAND — NO DRAGGING SPECTACLE' 명시, S08 DIRECTION 'THE SEASON ENDS BY OPENING — THE SMILE, NOT A CLOSING RELIEF' 명시. 렌더 프롬프트 `the verdict stated as one quiet sentence — no shouted arrest, no pointing rage, no dragged spectacle` 전 블록 상설(원장 0-2 규칙 6). "놈들을 묶어라!"식 고함 체포·"이것으로 끝이다"식 안도 마무리 시각 요소 0건 — S08은 미소+밀서로 시즌2 개회 | **통과** |
| 2-6 | 킬러 컷 2건 (시즌 피날레 특수 훅) | S05 낙하 프리즈 + S08 옥사 속 미소·밀서 | S05 — 문서 매달림→충격 프리즈(먼지 정지)→어전 경직 3컷, 연출 극대화. S08 — 옥사 칼날 빛 속 미소→불타지 않은 두 번째 밀서(봉인 온전)→암전→붉은 타이틀 4컷. 정본 지정 킬러 컷 1:1 렌더 | **통과** |
| 2-7 | 세이프 필터 | wound/blood 어휘 전면 배제, 전원 성인 | 원장 블록 프롬프트 전수 조사 — wound·blood·gore의 **긍정 사용 0건**(`No violence, no blood anywhere` 부정 가드 8블록 상설 + 규칙 행 금지 명시만, grep 전수 확인). S06 윤경헌의 외침은 정본 대사의 격렬함이고 검은 `sheathed swords` 한정, 체포는 팔을 거두는 수위 행동만. 절규·과장 고통 0건, 전 등장 인물 성인 명시(`all characters are adults`) | **통과** |
| 2-8 | 광원 표기 | S01~S07 하이키 역광 / S08 옥사 칼날 빛 | 정본 AG ① 준수 — 시트 TIME 표기 'WINTER MORNING, GREAT ASSEMBLY'(S01~S07)·'NIGHT, ROYAL PRISON'(S08), 렌더 라이트 가드 `cold high winter morning backlight pouring through the great doors is the key source`(S01~S07)·`one knife of cold light through the barred vent is the only source, the rest of the prison pitch-black`(S08) 상설. `no crushed blacks, no milky flat darkness` 전 썬 공통 | **통과** |
| 2-9 | 문자 슬롭 방지 | 문서·밀서 판독 가능한 글자 0건 | S04·S05 원본 — `dense vertical columns of brush-written text rendered only as illegible calligraphic texture, no readable letters, no characters, no labels` 상설, 최종 시트 봉인·낙관·붓글씨 질감만. S08 밀서 — `the seal mark on it intact, no readable writing anywhere on the page`. 어전 편액 등 건축 문자는 클린 프레이밍 가드로 전면 차단 | **통과** |
| 2-10 | 매크로 분포 | 매크로 연타 방지 + 휴먼 스케일 교차 | 매크로 3컷(S08 집중 배치) — S01~S07은 24~85mm 휴먼 스케일과 교차(S03·S04·S07의 85mm 클로즈 포함), S08 매크로로 미장센 강조 후 암전 수미상관. 매크로 연타 0건 | **통과** |
| 2-11 | 원장 7요소 8블록 완비 | 8블록 × 7문단(①~⑦) 누락 0 | 8블록 전부 ①시트 차단 ②화풍 전환 ③필름 룩 락 ④캐릭터 가드 ⑤광원 가드 ⑥컷 재현 ⑦물리·프레임 가드 순서로 완비(grep 전수 검증 — `OUTPUT FORMAT — READ FIRST`·`CHARACTER GUARD`·`LIGHT GUARD`·`Recreate the`·`MOTION — IMPORTANT`·`Absolutely NO text` 각 마커 8블록 기재). 블록별 컷 수 = 시트 패널 수(4/3/4/3/3/3/4/4) 일치 | **통과** |
| 2-12 | 보이스·SRT 정합 | 정본 대사 1:1, 절대 타임코드 정렬 | 8썬 보이스표·SRT 7블록 작성. 절대 시각 1.5(내레이션)·9.5(이환)·25.5(이환)·39.5(윤경헌)·48.5(이환)·55.0(내레이션)·58.0(자막) — 정본 rel 수치와 일치. 보이스 4종 — 내레이션 Wavenet-C·이환 Neural2-C는 계열이 다른 ID, 중전 Neural2-B는 본화 무대사(SRT 미기재), 윤경헌 Wavenet-D(정본 지정). S3·S7 무대사 준수. 지정 효과음 1건(S05 종이 낙하 충격음 rel 1.5=절대 30.5)은 사후 믹싱 레이어 배치, `paper dropping` 어구는 렌더 프롬프트에서 배제(정본 AG ①⑦) | **통과** |

**2차 검수 최종 판정**: 전 12개 검수 항목 100% 무결 통과 (PASS).

---

## 3. 납품 목록

| 구분 | 경로 |
|---|---|
| 콘티 시트 8종 | `downloads/EP25_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (1024×1536, 각 3.32~3.93MB) |
| 프롬프트 원장 | `projects/sageuk-revenge/SAGEUK_EP25_VARIABLE_STORYBOARD_AND_PROMPTS.md` |
| 생성기(재현용) | `projects/sageuk-revenge/ep25_sheets.py` (시트 8종 프롬프트 재생성, `python3 … S01 S08` 식 부분 렌더 지원) |
| 검수 기록 | `projects/sageuk-revenge/EP25_QC_CHECKLIST.md` (본 문서) |

**재렌더 시 주의**:
1. **1px 이탈**: 재렌더 시 반드시 PIL 실측으로 1024×1536 확인할 것 — 본화 S01에서 재현 후 재렌더로 복구.
2. **S08 엔드카드**: 마지막 패널은 흑바탕 **붉은 한글 타이틀 「제2시즌 권신의 덫에서 계속」 단일 세로 열** — 암전 프레임으로 되돌리면 정본 요구 불일치 재현(1차 실증). 단, 렌더 프롬프트상 S08 영상은 완전 암전으로 끝나고 타이틀은 편집 단계 삽입(시트의 타이틀 패널은 편집 참조용).
3. **S05 프리즈·문서 하강**: 충격음은 화면 연출에 재투입 금지 — `paper dropping` 어구 배제, 시각 프리즈만(정본 AG ①⑦).
4. **문서·밀서 문자 슬롭**: `no readable letters, no characters, no labels` 가드 유지 — 봉인·낙관·붓글씨 질감으로만.
5. **체포 고함 가드**: `the verdict stated as one quiet sentence — no shouted arrest, no pointing rage, no dragged spectacle` 가드 삭제 금지(정본 안티슬롭). S06 윤경헌의 외침은 정본 대사 그대로 유지하되 검은 `sheathed swords` 한정.
6. **왕의 관모·관복**: 대조 정식 의전은 **붉은 곤룡포+브림 없는 익선관** — `a gold royal winged Ikseongwan crown with no brim and not a gat` 가드 유지(EP24 흑색 갓 이탈 패턴의 개수형 재현 방지).
7. **하이키 역광**: `cold high winter morning backlight pouring through the great doors` 가드 유지 — 실내 조명으로 바뀌면 대조 아침의 광원 모티베이션 상실(정본 AG ①).
8. **대사 무음 렌더**: 본 화는 전 썬 대사·효과음이 존재하나 렌더는 무음 — 대사 지문을 프롬프트에 재투입하지 말 것(사후 믹싱 원장 별도).
