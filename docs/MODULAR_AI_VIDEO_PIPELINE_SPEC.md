# 🎬 AI 영상 제작 파이프라인 모듈화 아키텍처 및 제작 표준 운영 지침 (SOP)
## Storyboard-to-Video Modular Pipeline Specification v1.0
### (Model-Agnostic, Multi-Agent & Multi-Platform Standard)

---

## 1. 개요 및 설계 원칙 (Architecture Overview & Design Principles)

본 문서는 **스토리보드 기획·생성부터 프롬프트 규격화, AI 영상 렌더링, 프레임 컷오프 및 감독판 정밀 마스터링**에 이르는 전 과정을 모듈화하여, 특정 인공지능 모델(Veo, Kling, Runway, Sora 등)이나 특정 제작 툴에 종속되지 않고 **어떤 엔진과 애플리케이션으로도 즉시 교체·적용할 수 있도록 표준화한 제작 규격서**입니다.

### 핵심 5대 설계 원칙
1. **단일 모델 종속 탈피 (Model-Agnostic Abstraction)**
   - 스토리보드 생성(이미지)과 씬 렌더링(비디오)의 입력/출력 인터페이스를 표준 계약(Contract)으로 추상화하여, 최신 SOTA 모델 등장 시 어댑터(Adapter)만 교체하여 즉시 투입할 수 있도록 설계합니다.
2. **계약 기반 데이터 교환 (Contract-Driven Data Exchange)**
   - 에이전트 및 작업자 간 데이터 교환은 엄격한 `scene_plan.json` 및 `v3.1 프롬프트 원장` 규격으로 강제하여 휴먼 에러와 해석 오차를 0%로 통제합니다.
3. **순수 실사 분리 및 비파괴 재편집 원칙 (Clean Video & Detached Assets)**
   - 영상 원본에는 저품질 AI TTS나 자막을 영구 소부(Hard-sub)하지 않고, **무음성(-an)·무자막 16:9 와이드 클린 마스터본**으로 렌더링한 후 자막(.srt) 및 BGM을 독립 트랙으로 결합합니다.
4. **프레임 단위 경계 검증 (Frame-Accurate Boundary Verification)**
   - 스토리보드 이미지에서 실사로 전환되는 구간(앞 `0.0~1.35초`)을 수학적 알고리즘으로 100% 컷오프하여, 화면 내에 스케치 잔상이나 카메라/삼각대 등 AI 생성 아티팩트가 노출되는 결함을 원천 차단합니다.
5. **Git 기반 버전 관리 및 무결성 추적 (Git-Ops Asset Traceability)**
   - 모든 콘티 시트, 프롬프트 원장, 최종 영상은 SHA-256 체크섬과 Git 커밋 해시로 1:1 매핑되어 전수 무결성을 검증합니다.

---

## 2. 전체 파이프라인 아키텍처 다이어그램 (End-to-End DAG)

```
[원작 시나리오 / 소설 정본]
            │
            ▼ (Stage 1: Script & Scene Decomposition)
[씬/컷 분해 마스터 원장 (8개 씬, 씬당 3~5컷, 총 28~30컷)]
            │
            ▼ (Stage 2: Storyboard Sheet Generation)
[1024×1536 연필 소묘 가변 패널 시트 8장 (S01~S08)] ──> [Git assets/ 동기화]
            │
            ▼ (Stage 3: Visual Prompt Engineering v3.1)
[16:9 와이드 카메라 워크 & 광원·질감·네거티브 프롬프트 원장]
            │
            ▼ (Stage 4: Multi-Model Video Rendering Engine)
    ┌───────┴───────┬──────────────┬─────────────┐
    ▼               ▼              ▼             ▼
[Google Veo]   [Kling 1.5]   [Runway Gen-3]   [OpenAI Sora] (플러그인 교체 가능)
    └───────┬───────┴──────────────┴─────────────┘
            │
            ▼ (Stage 5: Frame Trimming & Transition Cutoff)
[0.0~1.35s 스토리보드 전환 구간 제거 & 순수 실사 구간(1.35~9.75s) 추출]
            │
            ▼ (Stage 6: Director's Cut Assembly & Master Remuxing)
[유사/중복 서브샷 제거 + 정확히 60.00초(1,440f) 24fps 무음·무자막 마스터본 리먹싱]
            │
            ▼ (Stage 7: Automated QA & Multi-Platform Distribution)
[전 8씬 입출력 1:1 QA 대조표 + 프레임 경계 검증표 + 분리형 SRT 자막 납품]
```

---

## 3. 각 Stage별 세부 모듈 규격 (Module Specifications)

### [Stage 1] 각본 및 씬/컷 단위 분해 (Scene Decomposition)
- **목적**: 1회 분량(약 60초)의 스토리 라인을 시각적 인과관계와 텐션 곡선에 맞춰 8개 핵심 씬(Scene)으로 분할.
- **입력 (Input)**: 회차별 시놉시스, 대사, 인물 관계도.
- **출력 (Output)**: `EPxx_SCENE_PLAN.json` (각 씬의 공간, 시간, 등장인물, 핵심 행동, 감정선).
- **규격**:
  - 에피소드당 8개 씬 고정 (`S01 ~ S08`).
  - 씬당 3~5개의 세부 컷(서브샷)으로 구성 (총 28~30컷).
  - 마지막 씬(`S08`) 4번 패널에는 차기작 예고 타이틀(엔드카드) 반드시 배치.

---

### [Stage 2] 스토리보드 시트 생성 (Storyboard Generation)
- **목적**: 영상 생성 모델이 인물의 외모, 의상, 조명, 구도, 카메라 앵글을 왜곡하지 않도록 연필 소묘 선화 기반의 가변 콘티 시트를 생성.
- **호환 엔진**: Midjourney v6, Flux.1 Pro/Dev, SDXL, DALL-E 3, Gemini Imagen 3.
- **표준 사양**:
  - **해상도**: `1024 × 1536` (2:3 세로 비율).
  - **화풍 스타일**: 극사실 연필 소묘 선화 질감 (`Charcoal and graphite pencil sketch on aged parchment, architectural cross-hatching, highly detailed line art, dynamic shadows`).
  - **패널 구성**: 씬의 호흡에 따라 3분할, 4분할(2×2 그리드), 5분할 가변 그리드 적용.
  - **출력 파일명 규칙**: `EPxx_S01~S08_DIRECTOR_STORYBOARD_VARIABLE.jpg` (8장 전량 필수 완비).

---

### [Stage 3] 시각 프롬프트 원장 작성 (Prompt Engineering v3.1)
- **목적**: 영상 모델의 특성에 맞춰 카메라 앵글, 렌즈 초점거리, 물리 시뮬레이션(바람, 화염, 연기, 비), 조명 조건을 표준 구문으로 기술.
- **표준 구문 템플릿**:
  ```markdown
  [화면 비율 & 카메라]: 16:9 ultra-wide cinematic ratio, 35mm anamorphic lens, slow camera push-in / pan.
  [인물 & 의상]: Korean historical period drama (Joseon era), authentic silk hanbok, subtle facial micro-expressions.
  [환경 & 조명]: Volumetric cinematic fog, candle flickering light, low-key lighting, 8k resolution, photorealistic.
  [행동 & 물리]: Natural fabric physics, steady breathing, rain droplets falling on granite palace stones.
  [네거티브 가드레일]: --no tripod, camera crew, modern artifacts, blur, 2d illustration, morphing, cartoon, text watermark.
  ```

---

### [Stage 4] 멀티 모델 렌더링 추상화 계층 (Rendering Engine Adapter)
- **목적**: 프롬프트와 시트를 입력받아 고화질 씬 클립을 생성하는 비디오 생성 엔진.
- **지원 모델 및 어댑터 매핑**:
  | 엔진명 | 어댑터 클래스 | 특성 및 권장 용도 |
  | :--- | :--- | :--- |
  | **Google Veo** | `VeoBatchAdapter` | 극사실 인물 피부 질감, 복잡한 군중 씬, 시네마틱 카메라 무빙 최적화 |
  | **Kling 1.5** | `KlingApiAdapter` | 역동적인 검술 액션, 화염/연기 물리 시뮬레이션, 긴 시간 일관성 |
  | **Runway Gen-3** | `RunwayGen3Adapter` | 섬세한 바람·물결 모션, 감성적인 클로즈업 씬 |
  | **OpenAI Sora** | `SoraAdapter` | 롱테이크 카메라 트래킹, 3D 공간 왜곡 없는 회랑 씬 |
  | **Minimax Hailuo** | `HailuoAdapter` | 자연스러운 인물 보행 모션, 표정 변화 |
- **표준 출력 포맷**:
  - 해상도: `1920 × 1080` (16:9 가로 와이드).
  - 프레임레이트: `24 fps`.
  - 클립 길이: 엔진당 6.0 ~ 10.0초 원본 클립 출력.

---

### [Stage 5] 프레임 트리밍 및 전환 구간 컷오프 (Frame Trimming)
- **목적**: AI 비디오 모델이 정지된 스토리보드 이미지에서 실사 모션으로 전환될 때 발생하는 **초반부 스케치 뭉개짐(Morphing artifact)**을 완벽히 제거.
- **절대 원칙 (Cutoff Rule)**:
  - 앞 **`0.0초 ~ 1.35초`** 구간은 **100% 영구 삭제(Cut-off)**.
  - 모션과 광원이 완벽하게 실사로 안착된 **`1.35초 ~ 9.75초`** 구간의 순수 실사 프레임만 채택.
  - 화면 내 카메라 렌즈, 삼각대, 스튜디오 조명 등 AI 환각 요소 노출 0건 검증.

---

### [Stage 6] 감독판 재편집 및 마스터본 리먹싱 (Director's Cut Remuxing)
- **목적**: 8개 씬의 순수 실사 클립들을 유기적으로 결합하고, 유사/중복 서브샷을 압축하여 정확한 규격 시간으로 패키징.
- **표준 사양**:
  - **총 러닝타임**: 정확히 **`60.00초`** (24fps 기준 정확히 **`1,440프레임`**, 오차 ±0프레임).
  - **오디오 채널**: `-an` (무음성 순수 영상 트랙).
  - **자막 채널**: 순수 영상에 텍스트를 태우지 않고 독립된 분리형 자막 파일(`*_ko.srt`)로 동봉.
  - **출력 파일명**: `EPxx_혈화의궐_제xx화_[에피소드명]_Veo_NoTTS_Master.mp4`.

---

### [Stage 7] 자동 품질 검수(QC) 및 배포 (Automated QA & Delivery)
- **품질 보증 산출물 (3종 세트)**:
  1. `EPxx_ALL8_CANONICAL_PENCIL_STORYBOARDS.jpg`: 원안 연필 콘티 8장 합본 시트.
  2. `EPxx_ALL8_CANONICAL_PENCIL_STORYBOARD_VS_RENDER_QA.jpg`: 원안 콘티와 최종 렌더링 실사 프레임의 **1:1 씬별 입출력 대조표**.
  3. `EPxx_DIRECTORS_CUT_BOUNDARY_VERIFY.jpg`: 8개 씬의 시작·종료 타임코드 및 프레임 경계 무결성 검증표.
- **체크섬 무결성**: SHA-256 해시를 생성하여 슬랙 관제 및 깃허브 릴리즈 노트에 명기.

---

## 4. 실전 자동화 스크립트 모듈 (Production Automation Scripts)

### 4.1 씬 분해 표준 스키마 (`scene_plan_schema.json`)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ScenePlan",
  "type": "object",
  "required": ["episode", "title", "total_runtime_sec", "target_fps", "scenes"],
  "properties": {
    "episode": { "type": "integer", "minimum": 1 },
    "title": { "type": "string" },
    "total_runtime_sec": { "type": "number", "enum": [60.0] },
    "target_fps": { "type": "integer", "enum": [24] },
    "scenes": {
      "type": "array",
      "minItems": 8,
      "maxItems": 8,
      "items": {
        "type": "object",
        "required": ["scene_id", "canonical_storyboard", "trim_start_sec", "trim_end_sec", "camera_motion", "prompt"],
        "properties": {
          "scene_id": { "type": "string", "pattern": "^S0[1-8]$" },
          "canonical_storyboard": { "type": "string" },
          "trim_start_sec": { "type": "number", "minimum": 1.35 },
          "trim_end_sec": { "type": "number" },
          "camera_motion": { "type": "string" },
          "prompt": { "type": "string" }
        }
      }
    }
  }
}
```

---

### 4.2 FFmpeg 1.35s 컷오프 및 60.00초 정밀 리먹싱 스크립트 (`remux_pipeline.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

# 사용법: ./remux_pipeline.sh <EP_NUM> <EP_TITLE>
EP_NUM="${1:-EP01}"
EP_TITLE="${2:-혈화의궐}"
OUTPUT_DIR="output/${EP_NUM}"
mkdir -p "${OUTPUT_DIR}/trimmed"

echo "=== [Step 1] 개별 씬 1.35s 컷오프 및 순수 실사 트리밍 ==="
# S01 ~ S08 클립별로 1.35초 이전 스토리보드 잔상을 잘라내고 무손실 추출
for s in {1..8}; do
    SCENE_ID=$(printf "S%02d" "${s}")
    RAW_CLIP="${OUTPUT_DIR}/raw_${SCENE_ID}.mp4"
    TRIMMED_CLIP="${OUTPUT_DIR}/trimmed/${SCENE_ID}.mp4"
    
    # 앞 1.35s 컷오프, 24fps 재인코딩, 오디오 스트림 완전 제거(-an)
    ffmpeg -y -ss 00:00:01.350 -i "${RAW_CLIP}" \
        -c:v libx264 -preset slow -crf 18 -r 24 -pix_fmt yuv420p -an \
        "${TRIMMED_CLIP}"
done

echo "=== [Step 2] 씬 결합 파일 리스트 생성 ==="
CONCAT_LIST="${OUTPUT_DIR}/concat_list.txt"
rm -f "${CONCAT_LIST}"
for s in {1..8}; do
    SCENE_ID=$(printf "S%02d" "${s}")
    echo "file 'trimmed/${SCENE_ID}.mp4'" >> "${CONCAT_LIST}"
done

echo "=== [Step 3] 60.00초(1,440프레임) 정밀 마스터본 리먹싱 ==="
MASTER_OUT="${OUTPUT_DIR}/${EP_NUM}_${EP_TITLE}_Veo_NoTTS_Master.mp4"
ffmpeg -y -f concat -safe 0 -i "${CONCAT_LIST}" \
    -t 60.000 -c:v libx264 -preset slow -crf 17 -r 24 -an \
    "${MASTER_OUT}"

echo "=== [Step 4] 무결성 검증 ==="
FRAMES=$(ffprobe -v error -select_streams v:0 -count_packets \
    -show_entries stream=nb_read_packets -of csv=p=0 "${MASTER_OUT}")
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "${MASTER_OUT}")

echo "결과: 총 프레임수 = ${FRAMES} (목표: 1440), 러닝타임 = ${DURATION}s (목표: 60.00s)"
if [ "${FRAMES}" -eq 1440 ]; then
    echo ">> [PASS] 60.00초 마스터본 규격 무결성 검증 통과!"
else
    echo ">> [FAIL] 프레임수 불일치! 트리밍 타임코드를 재조정하세요."
    exit 1
fi
```

---

## 5. 다른 AI 모델 및 툴로 이식 시 전환 매핑 (Adapter Migration Guide)

본 파이프라인을 Veo 외에 다른 생성 도구나 애플리케이션에 적용할 때 변경해야 할 파라미터 규칙입니다:

| 구분 | Google Veo (현재 기준) | Kling AI (클링) | Runway Gen-3 | OpenAI Sora |
| :--- | :--- | :--- | :--- | :--- |
| **입력 방식** | Image-to-Video (시트 1:1) | Image + Text 프롬프트 | Text + First Frame | Multi-modal Prompt |
| **추천 컷오프** | 앞 `1.35초` 컷오프 | 앞 `1.00초` 컷오프 | 앞 `0.80초` 컷오프 | 앞 `0.50초` 컷오프 |
| **권장 지속시간** | 7.0초 생성 (5.65s 채택) | 10.0초 모드 (8.5s 채택) | 10.0초 모드 (9.0s 채택) | 10.0초 모드 (9.5s 채택) |
| **모션 파라미터** | 기본 시네마틱 모션 | Motion Brush: 3~4 | Motion: 4, Pan/Tilt 지원 | 텍스트 자연어 모션 |
| **스타일 보존** | 연필 소묘 ➔ 실사 100% 일치 | 선화 외곽선 약간 잔존 가능 | 피사체 형태 매우 우수 | 물리 법칙 및 입체감 최상 |

---

## 6. 품질 검수 체크리스트 (Quality Assurance Checklist)

모든 회차의 영상 납품 전, 검수자가 반드시 대조해야 하는 필수 판정표입니다:

- [ ] **전 8씬 누락 여부**: S01부터 S08까지 8개 씬이 단 하나도 빠짐없이 렌더링되었는가?
- [ ] **1:1 콘티 매핑**: 각 씬의 연필 소묘 콘티 시트와 최종 영상의 인물, 구도, 조명이 1:1로 일치하는가?
- [ ] **초반부 스케치 잔상 0%**: 앞 1.35초가 정상 컷오프되어 첫 프레임부터 100% 라이브액션 실사인가?
- [ ] **카메라/삼각대 노출 0%**: 화면 내에 삼각대, 스튜디오 조명, 카메라 렌즈, 촬영 크루가 없는가?
- [ ] **무음·무자막 순수 영상**: 오디오 스트림(`-an`)이 0개이며, 화면 내에 자막이나 텍스트 워터마크가 없는가?
- [ ] **정확히 60.00초 (1,440프레임)**: ffprobe 실측 시 프레임 수가 정확히 1,440개인가?
- [ ] **분리형 SRT 자막 동봉**: 타임코드와 대사가 정확히 싱크된 별도 `.srt` 파일이 준비되었는가?
- [ ] **차기작 엔드카드**: S08 마지막 컷에 다음 화 예고 텍스트가 정상적으로 포함되었는가?

---

## 7. 결론 및 향후 확장 방안 (Conclusion & Future Expansion)

본 모듈화 규격을 적용하면 **작업자나 AI 모델이 바뀌더라도 항상 동일한 최상위 품질(16:9 가로 60초 24fps 무음 마스터본)의 영상 산출물을 안정적으로 연속 양산**할 수 있습니다. 

- **외주 및 신규 협력자 전달 시**: 본 문서(`MODULAR_AI_VIDEO_PIPELINE_SPEC.md`)와 함께 `scene_plan_schema.json`, `remux_pipeline.sh`를 패키지로 전달하면 즉시 동일 규격으로 프로덕션에 착수할 수 있습니다.
- **코덱스 및 자율 에이전트 연동**: GitHub 저장소 `member-system/docs/`에 상시 보존되어, 코덱스(Codex) 및 맥브릿지(MacBridge) 러너가 본 규격서를 레퍼런스로 참조하여 자동 렌더링·자동 QC를 수행합니다.
