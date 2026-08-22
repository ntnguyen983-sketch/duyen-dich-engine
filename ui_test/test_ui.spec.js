import { test, expect } from '@playwright/test';

const payloadNumber = '369147';
const hexagramPayload = JSON.stringify({
  data_1: { time: '2026-08-21T01:26:43+07:00', gps_show: { lat: 10.75554, lng: 106.611772 }, number: '3458769', dong: 3 },
  data_2: {
    question: 'Ca làm việc shipper từ 01:45 AM đến 06:00 AM, số đơn và thu nhập. Đề xuất có ích cho thu nhập và khách dễ thương.',
    dq_g: '110', dq_b: '100', que_goc_s: 'Phong Lôi Ích', que_bien_s: 'Phong Hỏa Gia Nhân', sl_am: 8, sl_duong: 10,
    dq_gs: 'Đoài (Trạch)', dq_bs: 'Chấn (Lôi)', engine_field: 'HƯỚNG Âm động chuyển Dương',
    truong: { Moc: 2, Hoa: 4, Tho: -2, Kim: -4, Thuy: -6 }, the: 1, quy_tac_luan: 'QT LỰC 1'
  }
}, null, 2);

async function mockAi(page) {
  await page.route('**/api/v31/analyze', async route => {
    const engineResponse = await page.request.post('/api/v31', { data: JSON.parse(route.request().postData() || '{}') });
    const engine = await engineResponse.json();
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        engine_output: engine,
        ai_interpretation: {
          status: 'provisional',
          headline: 'Có lực để tiến, nhưng cần giữ nhịp',
          answer: 'Nếu giữ điều kiện hiện tại, xu hướng là có thể tiến từng bước; tránh quyết định vội.',
          reading: 'Đây là luận giải AI dựa trên output của Engine.',
          signals: [{ name: 'Vector Khí', direction: 'mixed', evidence_paths: ['raw_measurements.khi_vector'], meaning: 'Tín hiệu hỗn hợp nên cần quan sát thêm.' }],
          forecast: { near_term: 'Tiến triển từng bước.', condition: 'Nếu giữ cách làm hiện tại.', turning_point: 'Khi điều kiện thực địa thay đổi.' },
          actions: ['Kiểm tra điều kiện thực tế trước khi chốt.'],
          uncertainty: { score: 0.7, note: 'Mapping còn provisional.' },
          limitations: ['Luận giải AI không phải kết luận CORE.'],
          trace: {
            model: 'test-model',
            engine_execution_id: engine.execution.execution_id,
            engine_input_hash: engine.execution.input_hash,
            engine_content_fingerprint: engine.provenance.content_fingerprint,
            source_version: 'v3.0dd-architecture + v3.1-runtime',
            inference_layer: 'AI_INTERPRETATION',
            generated_at: '2026-08-22T00:00:00+00:00'
          }
        }
      })
    });
  });
}

async function fillValidForm(page) {
  await page.locator('#question').fill('tình cảm');
  await page.locator('#number').fill(payloadNumber);
  await page.locator('#time').fill('2026-08-20T12:00');
  await page.locator('#lat').fill('10.755124');
  await page.locator('#lng').fill('106.616242');
  await page.locator('#address').fill('test');
  await page.locator('#image').setInputFiles({
    name: 'test.png',
    mimeType: 'image/png',
    buffer: Buffer.from('test-image'),
  });
}

test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    await page.screenshot({ path: `test-results/${testInfo.title.replace(/[^a-z0-9]+/gi, '-')}.png`, fullPage: true });
  }
});

test('full v3.1 browser flow renders canonical output and AI interpretation', async ({ page }) => {
  await mockAi(page);
  await page.goto('/');
  await expect(page.locator('#question')).toHaveValue('tình cảm');
  await expect(page.locator('#run')).toHaveText('CHẠY DUYÊN DỊCH v3.1');
  await fillValidForm(page);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  await expect(page.locator('#run-caption')).toContainText('Engine CORE giữ nguyên; lớp AI đã suy diễn có điều kiện từ output.');
  await expect(page.locator('#ai-interpretation')).toContainText('LUẬN GIẢI AI');
  await expect(page.locator('#ai-interpretation')).toContainText('Nếu giữ điều kiện hiện tại');
  await expect(page.locator('#ai-interpretation')).toContainText('raw_measurements.khi_vector');
  await expect(page.locator('#ai-interpretation')).toContainText('Luận giải AI không phải kết luận CORE');
  await expect(page.locator('#out')).toContainText('3.1.0');
  await expect(page.locator('#out')).toContainText('f_net_out_excluded');
  await expect(page.locator('#out')).not.toContainText('INFERRED');
  await expect(page.locator('#out')).not.toContainText('Đây chỉ là suy diễn');
  await expect(page.locator('#layers')).toContainText('L1');
  await expect(page.locator('#layers')).toContainText('L6');
  await expect(page.locator('#checks')).toContainText('canonical vocabulary');
  const l5Check = page.locator('#checks .check', { hasText: 'L5 canonical=true' });
  await expect(l5Check).toHaveClass(/pass/);
  await expect(page.locator('#checks')).toContainText('deterministic request');
  await expect(page.locator('#core-result')).toContainText('Input hash');
  await expect(page.locator('#microscope')).toContainText('Line 1');
  await expect(page.locator('#microscope')).toContainText('Line 6');
  await expect(page.locator('#microscope')).toContainText('CANONICAL_IDENTITY');
  await expect(page.locator('#microscope')).toContainText('bit');
  await expect(page.locator('#matrix')).toContainText('interpretation.source_interaction');
  await expect(page.locator('#matrix')).toContainText('[]');
  await expect(page.locator('#cross-line')).toContainText('interpretation.cross_line');
  await expect(page.locator('#cross-line')).toContainText('[]');
  await expect(page.locator('#timing')).toContainText('interpretation.expected_time_windows');
  await expect(page.locator('#timing')).toContainText('[]');
  await expect(page.locator('#ground-truth')).toContainText('interpretation.ground_truth');
  await expect(page.locator('#ground-truth')).toContainText('null');
  await expect(page.locator('#comparison')).toContainText('comparison');
  await expect(page.locator('#summary')).toContainText('Interpretation coverage');
  await expect(page.locator('#inferred')).toContainText('INFERRED');
  await expect(page.locator('#inferred')).toContainText('Đây chỉ là suy diễn, không phải dữ liệu API trả về.');
  await expect(page.locator('#inferred')).toContainText('API không đánh dấu hào động');
});

test('hexagram data_1/data_2 payload runs through production UI', async ({ page }) => {
  await mockAi(page);
  await page.goto('/');
  await page.locator('#use-hexagram').check();
  await page.locator('#hexagram-payload').fill(hexagramPayload);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  await expect(page.locator('#run-caption')).toContainText('Engine CORE giữ nguyên; lớp AI đã suy diễn có điều kiện từ output.');
  await expect(page.locator('#ai-interpretation')).toContainText('LUẬN GIẢI AI');
  await expect(page.locator('#ai-interpretation')).toContainText('Đã tạo luận giải AI ở trạng thái provisional');
  await expect(page.locator('#out')).toContainText('3.1.0');
  await expect(page.locator('#out')).toContainText('CALIBRATION_REQUIRED');
  await expect(page.locator('#layers')).toContainText('L1');
  await expect(page.locator('#layers')).toContainText('L6');
  await expect(page.locator('#checks')).toContainText('deterministic request');
  await expect(page.locator('#checks .check', { hasText: 'L5 canonical=true' })).toHaveClass(/pass/);
  await expect(page.locator('#core-result')).toContainText('Root code');
  await expect(page.locator('#microscope')).toContainText('Line 1');
  await expect(page.locator('#microscope')).toContainText('Line 6');
  await expect(page.locator('[data-line="3"] .badge')).toHaveText('MOVING');
  await expect(page.locator('[data-line="3"]')).toHaveAttribute('data-moving', 'true');
  for (const line of [1, 2, 4, 5, 6]) {
    await expect(page.locator(`[data-line="${line}"] .badge`)).toHaveText('NOT MOVING');
    await expect(page.locator(`[data-line="${line}"]`)).toHaveAttribute('data-moving', 'false');
  }
  await expect(page.locator('#microscope')).toContainText('CANONICAL_INPUT');
  await expect(page.locator('#microscope')).not.toContainText('Source Evidence');
  await expect(page.locator('#matrix')).toContainText('interpretation.source_interaction');
  await expect(page.locator('#matrix')).toContainText('[]');
  await expect(page.locator('#cross-line')).toContainText('interpretation.cross_line');
  await expect(page.locator('#cross-line')).toContainText('[]');
  await expect(page.locator('#timing')).toContainText('interpretation.expected_time_windows');
  await expect(page.locator('#timing')).toContainText('[]');
  await expect(page.locator('#summary')).toContainText('CALIBRATION_REQUIRED');
  await expect(page.locator('#inferred')).toContainText('Phong Lôi Ích');
  await expect(page.locator('#inferred')).toContainText('Phong Hỏa Gia Nhân');
  await expect(page.locator('#inferred')).toContainText('H3');
  await expect(page.locator('#inferred')).toContainText('raw_measurements.khi_vector');
  await expect(page.locator('#inferred')).toContainText('Đây chỉ là suy diễn, không phải dữ liệu API trả về.');
});

test('mobile interpretation layout has no horizontal overflow or console errors', async ({ page }) => {
  await mockAi(page);
  await page.setViewportSize({ width: 390, height: 844 });
  const consoleErrors = [];
  page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
  page.on('pageerror', error => consoleErrors.push(error.message));
  await page.goto('/');
  await page.locator('#use-hexagram').check();
  await page.locator('#hexagram-payload').fill(hexagramPayload);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  const layout = await page.evaluate(() => ({ width: window.innerWidth, scrollWidth: document.documentElement.scrollWidth }));
  expect(layout.scrollWidth).toBeLessThanOrEqual(layout.width + 1);
  expect(consoleErrors).toEqual([]);
  await expect(page.locator('#timing')).toContainText('Expected time windows');
  await expect(page.locator('#ground-truth')).toContainText('EXACT VALUE');
  await expect(page.locator('#ground-truth')).toContainText('null');
});

test('missing question is blocked before API call', async ({ page }) => {
  await page.goto('/');
  await page.locator('#question').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('input không hợp lệ');
  await expect(page.locator('#checks')).toContainText('required question');
});

test('missing number, invalid number and missing time are blocked', async ({ page }) => {
  await page.goto('/');
  await page.locator('#number').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('input không hợp lệ');
  await page.locator('#number').fill('12345');
  await page.locator('#time').fill('2026-08-20T12:00');
  await page.locator('#run').click();
  await expect(page.locator('#checks')).toContainText('number validation');
  await page.reload();
  await page.locator('#number').fill(payloadNumber);
  await page.locator('#time').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#checks')).toContainText('required time');
});
