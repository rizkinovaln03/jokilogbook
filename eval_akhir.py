from playwright.sync_api import sync_playwright

def isi_eval_akhir(username: str, password: str, id_stase: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://logbook-fk.apps.undip.ac.id/koas/login.php")
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_placeholder("Password").press("Enter")

        page.goto(f"https://logbook-fk.apps.undip.ac.id/koas/isi_evaluasi.php?id={id_stase}")

        for i in range(5, 20):
            try:
                page.locator(f"tr:nth-child({i}) td:nth-child(5) .radio label").first.click()
            except:
                pass

        page.locator("textarea[name='refleksi']").fill("Semoga baik lagi")
        page.locator("textarea[name='komentar']").fill("semoga dapat diperbaiki seluruh kekurangan yang ada")
        page.get_by_label("> 75%").check()
        page.get_by_label("Sangat puas").check()

        page.locator("#select2-dosen1-container").click()
        page.get_by_role("searchbox").fill("ilham uddin")
        page.get_by_role("searchbox").press("Enter")
        page.locator("textarea[name='tatap_muka1']").fill("80")
        page.locator("textarea[name='komentar_dosen1']").fill("sudah bagus")

        context.close()
        browser.close()