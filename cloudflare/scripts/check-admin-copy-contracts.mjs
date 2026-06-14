import { testables } from "../src/worker.js";
import { readFileSync } from "node:fs";

const sampleBooking = {
  applicant_name: "신청자",
  session_title: "AI 기초 셋팅 및 컨설팅 강의 1:4",
  session_starts_at: "2026-05-24T10:00:00+09:00",
  session_ends_at: "2026-05-24T12:00:00+09:00",
  session_location: "영등포시장역 사무실",
  payment_amount_krw: 50000,
};

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function assertMultilineCopy(name, text, expected) {
  const lineCount = text.split("\n").length;
  assert(!text.includes("\\n"), `${name}: literal backslash-n found`);
  assert(lineCount >= expected.minLines, `${name}: expected at least ${expected.minLines} lines, got ${lineCount}`);
  for (const phrase of expected.phrases) {
    assert(text.includes(phrase), `${name}: missing phrase "${phrase}"`);
  }
}

assertMultilineCopy(
  "payment guide",
  testables.defaultPaymentGuide(sampleBooking, { bank: "은행", number: "000", holder: "예금주" }),
  {
    minLines: 8,
    phrases: ["[입금 안내]", "과정:", "일정:", "시간:", "장소:", "금액:", "입금 계좌:", "예금주:"],
  },
);

assertMultilineCopy(
  "location guide",
  testables.defaultLocationGuide(sampleBooking),
  {
    minLines: 8,
    phrases: ["[장소 안내]", "입금 확인되어 예약이 확정되었습니다.", "과정:", "일정:", "시간:", "장소:", "준비물:"],
  },
);

assertMultilineCopy(
  "refund guide",
  testables.defaultRefundGuide(sampleBooking),
  {
    minLines: 5,
    phrases: ["[환불 확인 안내]", "예약 취소가 접수되었습니다.", "확인 필요 금액:", "환불 계좌"],
  },
);

const workerSource = readFileSync(new URL("../src/worker.js", import.meta.url), "utf8");
const publicBookingStart = workerSource.indexOf("async function handlePublicBooking");
const publicBookingEnd = workerSource.indexOf("async function telegramCallbackResult", publicBookingStart);
const publicBookingSource = workerSource.slice(publicBookingStart, publicBookingEnd);
const duplicateStart = publicBookingSource.indexOf("if (existing) {");
const duplicateEnd = publicBookingSource.indexOf("const bookingId = await createBooking", duplicateStart);
const duplicateSource = publicBookingSource.slice(duplicateStart, duplicateEnd);
assert(duplicateSource.includes("duplicate: true"), "duplicate booking branch not found");
assert(!duplicateSource.includes("sendTelegram"), "duplicate booking branch must not send Telegram");

console.log("admin copy contracts ok");
