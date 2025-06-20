from playwright.sync_api import sync_playwright

def isi_logbook_ketrampilan(username: str, password: str, id_stase: str, tanggal: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://logbook-fk.apps.undip.ac.id/koas/login.php")
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_placeholder("Password").press("Enter")

        page.goto(f"https://logbook-fk.apps.undip.ac.id/koas/tambah_logbook2.php?id={id_stase}&tgl={tanggal}")

        keterampilan = [
            "Auskultasi jantung", "Autoanamnesis dengan pasien",
            "Edukasi berhenti merokok", "Palpasi arteri karotis"
        ]
        for i in range(4):
            page.locator(f"#select2-ketrampilan{i+1}-container").click()
            page.get_by_role("searchbox").fill(keterampilan[i])
            page.get_by_role("searchbox").press("Enter")

        page.locator("#select2-dosen-container").click()
        page.get_by_role("searchbox").fill("ilham uddin")
        page.get_by_role("searchbox").press("Enter")
        page.get_by_role("button", name="+ TAMBAHKAN").click()

        context.close()
        browser.close()