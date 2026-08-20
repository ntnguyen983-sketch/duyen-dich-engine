import { test, expect } from '@playwright/test';

const payloadNumber = '369147';

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

test('full v3.1 browser flow renders canonical output', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('#question')).toHaveValue('tình cảm');
  await expect(page.locator('#run')).toHaveText('CHẠY DUYÊN DỊCH v3.1');
  await fillValidForm(page);
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText('PASS', { timeout: 15000 });
  await expect(page.locator('#out')).toContainText('3.1.0');
  await expect(page.locator('#out')).toContainText('f_net_out_excluded');
  await expect(page.locator('#layers')).toContainText('L1');
  await expect(page.locator('#layers')).toContainText('L6');
  await expect(page.locator('#checks')).toContainText('canonical vocabulary');
  const l5Check = page.locator('#checks .check', { hasText: 'L5 canonical=true' });
  await expect(l5Check).toHaveClass(/pass/);
  await expect(page.locator('#checks')).toContainText('deterministic request');
  await expect(page.locator('#summary')).toContainText('input hash');
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
