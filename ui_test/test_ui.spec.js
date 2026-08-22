import { test, expect } from '@playwright/test';

const payloadNumber = '369147';
const hexagramPayload = JSON.stringify({
  data_1: {
    time: '2026-08-21T01:26:43+07:00',
    gps_show: { lat: 10.75554, lng: 106.611772 },
    number: '3458769',
    dong: 3,
  },
  data_2: {
    question: 'Ca làm việc shipper từ 01:45 AM đến 06:00 AM, số đơn và thu nhập.',
    que_goc_s: 'Phong Lôi Ích',
    que_bien_s: 'Phong Hỏa Gia Nhân',
    truong: { Moc: 2, Hoa: 4, Tho: -2, Kim: -4, Thuy: -6 },
    quy_tac_luan: 'QT LỰC 1',
  },
}, null, 2);

async function mockInterpretation(page) {
  await page.route('**/api/v31/interpret', async route => {
    const payload = JSON.parse(route.request().postData() || '{}');
    const engineResponse = await page.request.post('/api/v31', { data: payload });
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
          reading: 'AI đã chuyển tín hiệu Engine thành luận giải thực tế.',
          signals: [{
            name: 'Vector Khí',
            direction: 'mixed',
            evidence_paths: ['raw_measurements.khi_vector'],
            meaning: 'Có tín hiệu hỗn hợp nên cần quan sát thêm.',
          }],
          forecast: {
            near_term: 'Tiến triển từng bước.',
            condition: 'Nếu giữ cách làm hiện tại.',
            turning_point: 'Khi điều kiện thực tế thay đổi.',
          },
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
            generated_at: '2026-08-22T00:00:00+00:00',
          },
        },
      }),
    });
  });
}

async function fillValidForm(page) {
  await page.locator('#question').fill('tình cảm');
  await page.locator('#number').fill(payloadNumber);
  await page.locator('#time').fill('2026-08-20T12:00');
  await page.locator('#lat').fill('10.755124');
  await page.locator('#lng').fill('106.616242');
  await page.locator('#address').fill('TP.HCM');
}

test('user-facing flow renders AI interpretation before technical trace', async ({ page }) => {
  await mockInterpretation(page);
  await page.goto('/');
  await fillValidForm(page);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  await expect(page.locator('#ai-pill')).toHaveText('AI PROVISIONAL');
  await expect(page.locator('#interpretation')).toContainText('Luận giải AI');
  await expect(page.locator('#interpretation')).toContainText('Có lực để tiến');
  await expect(page.locator('#interpretation')).toContainText('Nếu giữ điều kiện hiện tại');
  await expect(page.locator('#interpretation')).toContainText('Dự báo có điều kiện');
  await expect(page.locator('#interpretation')).toContainText('Việc nên làm');
  await expect(page.locator('#interpretation')).toContainText('raw_measurements.khi_vector');
  await expect(page.locator('#engine-json')).toContainText('3.1.0');
  await expect(page.locator('#trace-json')).toContainText('AI_INTERPRETATION');
});

test('hexagram payload preserves user context and shows provisional interpretation', async ({ page }) => {
  await mockInterpretation(page);
  await page.goto('/');
  await page.locator('#use-hexagram').check();
  await page.locator('#hexagram-payload').fill(hexagramPayload);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  await expect(page.locator('#ai-pill')).toHaveText('AI PROVISIONAL');
  await expect(page.locator('#interpretation')).toContainText('Đã tạo luận giải ở trạng thái provisional');
  await expect(page.locator('#engine-json')).toContainText('CALIBRATION_REQUIRED');
});

test('mobile interpretation layout has no horizontal overflow or console errors', async ({ page }) => {
  await mockInterpretation(page);
  await page.setViewportSize({ width: 390, height: 844 });
  const consoleErrors = [];
  page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
  page.on('pageerror', error => consoleErrors.push(error.message));
  await page.goto('/');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  const layout = await page.evaluate(() => ({ width: window.innerWidth, scrollWidth: document.documentElement.scrollWidth }));
  expect(layout.scrollWidth).toBeLessThanOrEqual(layout.width + 1);
  expect(consoleErrors).toEqual([]);
});

test('missing question is blocked before API call', async ({ page }) => {
  await page.goto('/');
  await page.locator('#question').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('Cần nhập câu hỏi');
});

test('invalid number and missing time are blocked', async ({ page }) => {
  await page.goto('/');
  await page.locator('#number').fill('12345');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('Số sáu chữ số không hợp lệ');
  await page.locator('#number').fill(payloadNumber);
  await page.locator('#time').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('Cần nhập thời điểm quan sát');
});
