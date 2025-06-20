from playwright.sync_api import sync_playwright

def isi_logbook_penyakit(username: str, password: str, id_stase: str, tanggal: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://logbook-fk.apps.undip.ac.id/koas/login.php")
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_placeholder("Password").press("Enter")

        page.goto(f"https://logbook-fk.apps.undip.ac.id/koas/edit_logbook.php?id={id_stase}&tgl={tanggal}")
        page.frame_locator("iframe[title='Rich Text Editor, evaluasi']").locator("body").fill("baik")
        page.frame_locator("iframe[title='Rich Text Editor, rencana']").locator("body").fill("baik")
        page.get_by_role("button", name=" SAVE").click()

        page.goto(f"https://logbook-fk.apps.undip.ac.id/koas/tambah_logbook.php?id={id_stase}&tgl={tanggal}")
        page.locator("#select2-kelas-container").click()
        page.get_by_role("searchbox").fill("pagi")
        page.get_by_role("searchbox").press("Enter")
        page.locator("input[name='jam_mulai']").fill("7")
        page.locator("input[name='jam_selesai']").fill("9")
        page.locator("input[name='menit_mulai']").fill("0")
        page.locator("input[name='menit_selesai']").fill("0")
        page.locator("#select2-lokasi-container").click()
        page.get_by_role("searchbox").fill("rsdk")
        page.get_by_role("searchbox").press("Enter")
        page.locator("#select2-kegiatan-container").click()
        page.get_by_role("searchbox").fill("4a")
        page.get_by_role("searchbox").press("Enter")

        penyakit = ["Hipertensi esensial", "Ekstrasistol", "Fibrilasi atrial", "Angina pektoris"]
        for i in range(4):
            page.locator(f"#select2-penyakit{i+1}-container").click()
            page.get_by_role("searchbox").fill(penyakit[i])
            page.get_by_role("searchbox").press("Enter")

        page.locator("#select2-dosen-container").click()
        page.get_by_role("searchbox").fill("ilham uddin")
        page.get_by_role("searchbox").press("Enter")
        page.get_by_role("button", name="+ TAMBAHKAN").click()

        context.close()
        browser.close()