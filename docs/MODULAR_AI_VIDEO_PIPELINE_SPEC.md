# 🎬 AI 영상 제작 파이프라인 모듈화 아키텍처 및 제작 표준 운영 지침 (SOP)
## Storyboard-to-Video Modular Pipeline Specification v1.2
### (독립 재검수 후속 개정판: 엄격한 운영 기준 반영, 해상도/무결성 사전 차단, CLI 실조립 지원 및 실측치 분리)

---

## 1. 개요 및 설계 원칙 (Overview & Architecture Principles)

본 문서는 **스토리보드 기획·생성부터 프롬프트 규격화, AI 영상 렌더링, 씬별 프레임 슬라이스 조립 및 마스터링**에 이르는 전 과정을 모듈화하여, 특정 인공지능 모델(Veo, Kling, Runway, Sora 등)이나 특정 제작 툴에 종속되지 않고 **어떤 엔진과 애플리케이션으로도 즉시 교체·적용할 수 있도록 표준화한 제작 규격서**입니다.

### v1.2 독립 재검수 보완 핵심 사항
1. **[운영 기준 엄격 적용] 부족한 원본 입력 시 인위적 통과 금지 및 즉각 중단 (ABORT)**:
   - 7초 원본 8개는 1.35초 컷오프 적용 시 총 가용 길이가 45.20초에 불과합니다.
   - EP01의 운영 표준(55~65초 유동)이나 60.00초 고정 규격에서, 진단 범위를 인위적으로 낮춰(40~50초) 통과시키는 것은 금지되며, **실제 운영 기준에 따라 명백한 FAIL 및 즉시 중단(ABORT)** 처리합니다.
2. **[해상도 및 컨테이너 무결성 사전 검증] 저해상도 및 손상된 파일 원천 차단**:
   - 목표 해상도(`1920×1080`)와 다른 저해상도 원본(예: `160×90`) 주입 시 사전 검증 단계에서 즉시 FAIL 차단합니다.
   - MP4 파일 손상/헤더 누락 시 기본 7초 가상 메타데이터로 대체하지 않고 즉각 `ValueError` 예외로 파이프라인 가동을 중단합니다.
3. **[CLI 실조립 진입점 제공] 진단과 실제 ffmpeg 조립 실행 분리**:
   - 단순 사전 진단 외에 실제 슬라이스 추출과 Concat 및 후속 ffprobe QC를 실행하는 CLI(`validate`, `assemble`, `test-counterexamples`)를 완비했습니다.
4. **[실측치와 계획 수치 명확한 분리] EP01 Air 마스터 실측 영수증 공인**:
   - 계획 슬롯 이산 합계(`1,406프레임`: 176+175+176+176+176+175+176+176)와 실제 제작된 물리 마스터본(`1,405프레임`: 58.541667초 * 24fps)의 차이를 정직하게 분리 기록합니다.
5. **[이력과 어댑터 코드 상태 분리]**:
   - Google Veo의 80씬 실증 이력(MacBook Air Ego 6계정 브릿지)과 본 레포지토리의 파이썬 어댑터 코드 상태(`ADAPTER_IMPLEMENTED`)를 분리 정의합니다.

---

## 2. 모듈 구성 및 파일 시스템 구조 (Module Architecture)

```
member-system/
├── schemas/
│   └── scene_plan_schema.json      # 씬 계획 및 프로젝트 프로필 JSON 스키마 (Draft-07)
├── scripts/
│   ├── video_assembler.py          # 씬 검증, 클립 프로브, 슬라이스 조립, 실조립 CLI 및 QC 엔진
│   └── adapters/                   # 멀티 모델 렌더링 어댑터 패키지
│       ├── __init__.py
│       ├── base_adapter.py         # 베이스 어댑터 추상 클래스 & EngineStatus Enum
│       ├── veo_batch_adapter.py    # Google Veo 어댑터 (80씬 실증 이력 분리)
│       ├── kling_adapter.py        # Kling 1.5 어댑터 [INTERFACE_ONLY]
│       ├── runway_adapter.py       # Runway Gen-3 어댑터 [INTERFACE_ONLY]
│       ├── sora_adapter.py         # OpenAI Sora 어댑터 [PLANNED]
│       └── engine_registry.py      # 어댑터 레지스트리 및 조회 API
├── docs/
│   └── MODULAR_AI_VIDEO_PIPELINE_SPEC.md   # 본 SOP 명세서 v1.2
└── tests/
    └── video_pipeline/
        └── test_video_assembler.py # 조립기 단위 테스트 및 회귀 검증
```

---

## 3. 각 Stage별 세부 모듈 규격 (Module Specifications)

### [Stage 1] 각본 및 씬/컷 단위 분해 (Scene Plan)
- **에피소드당 8개 씬 고정 (`S01 ~ S08`)**: 순서 엄수, 중복 불가, 누락 불가.
- **씬별 트림 범위 명시**: `trim_start_sec`, `trim_end_sec` 필수 기재.
- **검증 규칙**: `trim_end_sec > trim_start_sec >= 0.0`.

### [Stage 2] 스토리보드 시트 생성 (Storyboard Sheet)
- **해상도**: `1024 × 1536` (2:3 세로 비율).
- **화풍 스타일**: 극사실 연필 소묘 선화 질감 (Charcoal & graphite pencil sketch).
- **출력**: `EPxx_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (8장 전량 필수 완비).

### [Stage 3] 시각 프롬프트 원장 (Prompt Engineering v3.1)
- 16:9 와이드 비율, 카메라 워크, 조명, 인물 의상, 물리 법칙, 네거티브 프롬프트 기술.

### [Stage 4] 멀티 모델 렌더링 추상화 (Engine Adapters)
- 각 엔진의 연동 확인 상태와 제작 이력 분리:
  | 엔진명 | 어댑터 클래스 | 어댑터 코드 상태 | 제작 실증 이력 (Provenance) |
  | :--- | :--- | :--- | :--- |
  | **Google Veo** | `VeoBatchAdapter` | **`ADAPTER_IMPLEMENTED`** | **EP01~EP10 80씬 전수 실사 렌더링 검수 통과** (MacAir M2 6계정 브릿지) |
  | **Kling AI 1.5** | `KlingAdapter` | **`INTERFACE_ONLY`** | 파라미터 규격 정의 완료, 실 API 파이프라인 미확인 |
  | **Runway Gen-3** | `RunwayAdapter` | **`INTERFACE_ONLY`** | First Frame + Text 매핑 완료, 실 API 파이프라인 미확인 |
  | **OpenAI Sora** | `SoraAdapter` | **`PLANNED`** | 상용 배치 API 미출시, 스펙 사전 정의 |

### [Stage 5] 프레임 트리밍 및 전환 구간 컷오프 (Slice Trimming)
- **컷오프 원칙**: 스토리보드 정지화면 잔상 구간(앞 `1.35초`) 영구 제거.
- **경계 검증**: `trim_end_sec <= actual_raw_duration` (원본 길이 초과 금지).
- **해상도 검증**: 원본 클립 해상도 == `target_resolution` (불일치 시 즉각 FAIL).
- **유효 프레임 보장**: 각 씬별 추출 프레임수 `> 0` 필수 (S08 0프레임 원천 방지).

### [Stage 6] 감독판 재편집 및 조립 (Assembly & Remuxing)
- **조립 방식**: 개별 씬 슬라이스 추출(`-ss {start} -t {duration}`) ➔ 비파괴 무손실 Concat (`-c copy`).
- **전역 잘라내기(-t) 금지**: concat 단계에서 임의로 tail을 자르지 않음.
- **규격 모드 분리**:
  - `fixed_exact`: 목표 시간(예: 60.00초), 목표 프레임(1,440프레임) 정확 일치 검증.
  - `flexible_range`: 최소~최대 범위(예: 55.0초 ~ 65.0초, EP01 규격) 수용.

### [Stage 7] 자동 품질 검수 (QC Checklist)
- [ ] S01부터 S08까지 8개 씬 순서 일치, 중복 0건, 누락 0건.
- [ ] S01~S08 각 씬의 추출 프레임수 > 0 (0프레임 잘림 0건).
- [ ] 해상도 `1920×1080` 일치 (저해상도 원본 차단).
- [ ] 오디오 스트림 0개 (`-an` 무음성 클린 마스터).
- [ ] 프레임레이트 24fps.

---

## 4. CLI 도구 사용법 (CLI Execution Guide)

`scripts/video_assembler.py`를 통해 진단 및 실제 조립을 실행합니다:

```bash
# 1. 4대 반례 및 EP01 정본 진단 테스트 실행
python3 scripts/video_assembler.py test-counterexamples

# 2. 씬 계획과 원본 클립 무결성 사전 검증 (해상도, 길이, 프레임)
python3 scripts/video_assembler.py validate --plan schemas/ep01_plan.json --clips-dir /path/to/clips

# 3. 실제 ffmpeg 조립 및 마스터본 생성 (ffprobe 자동 QC 포함)
python3 scripts/video_assembler.py assemble \
  --plan schemas/ep01_plan.json \
  --clips-dir /path/to/clips \
  --output output/EP01_Master.mp4 \
  --work-dir /tmp/assembler_work
```

---

## 5. EP01 실측 영수증 및 계획 대조 (Measurement Provenance)

- **Air 실측 물리 마스터본 (MacBook Air F0CESPS2WH2)**:
  - 파일 크기: `61,512,282` bytes
  - SHA-256: `7b18f28ffc65d6484e1b8b2e50529d3c5f9498a44c9b33a4664c3c3a076cb738`
  - 실측 길이: `58.541667초`
  - 실측 프레임: **`1,405 frames`** (58.541667s * 24fps)
  - 해상도 / 규격: `1920×1080`, 24fps, 무음성(`audio=0`)
- **씬 계획표 이산 프레임 합계**:
  - `176 + 175 + 176 + 176 + 176 + 175 + 176 + 176 = 1,406 frames` (이산 정수 올림 슬롯 합계)
  - *비고: 계획표 상의 1,406은 정수 올림 슬롯 합계이며, 실제 인코딩된 물리 마스터본은 정확히 1,405프레임임을 명확히 구분 기록함.*
