import { test, expect } from "@playwright/test";

test("has title", async ({ page }) => {
  await page.goto("localhost:3000");
  await expect(page).toHaveTitle(/FairBuddy/);
});

test("home content", async ({ page }) => {
  await page.goto("localhost:3000");
  await expect(page.getByRole("heading", { name: "FairBuddy" })).toBeVisible();
});
