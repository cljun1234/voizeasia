from playwright.sync_api import sync_playwright
import time
import os

def run_cuj(page):
    page.goto("http://localhost:3000/register.html")
    page.wait_for_timeout(1000)

    # Note: custom checkboxes use CSS to hide the actual input element, so we need to click the label
    # 1. Fill in Niche - Others
    page.locator("#nicheGroup label").filter(has_text="Others").click()
    page.wait_for_timeout(500)

    # Verify input appears
    others_input = page.locator("#nicheOthersInput")
    others_input.fill("Gamer / Tech")
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/screenshots/niche_others.png")

    # 2. Fill in Language - Mixed
    page.locator("#languageGroup label").filter(has_text="Mixed").click()
    page.wait_for_timeout(500)

    # Verify input appears
    mixed_input = page.locator("#languageMixedInput")
    mixed_input.fill("English & Japanese")
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/screenshots/lang_mixed.png")

    # 3. Fill out the rest of section A and move to B
    page.locator("#fullName").fill("Takumi Fujiwara")
    page.locator("#creatorName").fill("@tofu_delivery")
    page.locator("#tiktokLink").fill("https://tiktok.com/@tofu")
    page.locator("#instagramLink").fill("https://instagram.com/tofu")

    # We need an image
    with open("test_img.png", "wb") as f:
        f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')

    page.locator("#profilePicture").set_input_files("test_img.png")
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Next: Personality & Character").click()
    page.wait_for_timeout(1000)

    page.screenshot(path="/home/jules/verification/screenshots/section_b.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()