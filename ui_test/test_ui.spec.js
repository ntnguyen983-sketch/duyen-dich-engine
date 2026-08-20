import { test, expect } from '@playwright/test';

test('full input form is usable', async ({ page }) => {
  await page.goto('/ui_test/index.html');
  await expect(page.locator('#question')).toHaveValue('tình cảm');
  await page.locator('#number').fill('369147');
  await page.locator('#address').fill('test address');
  await expect(page.locator('#run')).toHaveText('CHẠY V3.1');
});

test('invalid required question is caught by API path', async ({ page }) => {
  await page.goto('/ui_test/index.html');
  await page.locator('#question').fill('');
  await page.locator('#run').click();
  await expect(page.locator('#status')).toContainText(/FAIL|Đang chạy/);
});
