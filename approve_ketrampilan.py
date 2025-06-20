from playwright.sync_api import sync_playwright

def approve_logbook_ketrampilan(username: str, password: str, id_stase: str, tanggal: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://logbook-fk.apps.undip.ac.id/koas/login.php")
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_placeholder("Password").press("Enter")

        page.goto(f"https://logbook-fk.apps.undip.ac.id/koas/edit_logbook.php?id={id_stase}&tgl={tanggal}")
        page.locator("#freeze1 > .table-warning > tr > td:nth-child(5) > a > .btn").first.click()
        page.locator("#dosenpass").fill("196812212008121002")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name=" APPROVE").click()

        context.close()
        browser.close()