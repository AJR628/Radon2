# ColoradoRadonGuide.com

Static V1 website for ColoradoRadonGuide.com — an independent Colorado radon information and quote-connection resource.

## Stack

Plain HTML + CSS. No build step is required to deploy. The HTML in this repo is the final, deployable output.

The Python files under `_build/` are the source-of-truth templates that produced the HTML. If you change content, edit `_build/` and re-run `python3 _build/build.py`. If you only want to tweak copy on a single page, you can edit the HTML directly — just keep the change in `_build/` too if you plan to rebuild later.

## Page inventory

### V1 pages

| URL | File |
|---|---|
| `/` | `index.html` |
| `/colorado-springs/` | `colorado-springs/index.html` |
| `/colorado-springs/radon-mitigation-cost/` | `colorado-springs/radon-mitigation-cost/index.html` (refreshed in Phase 2) |
| `/colorado-springs/radon-testing/` | `colorado-springs/radon-testing/index.html` |
| `/colorado-springs/failed-radon-test/` | `colorado-springs/failed-radon-test/index.html` |
| `/request-quote/` | `request-quote/index.html` |
| `/request-quote/thank-you/` | `request-quote/thank-you/index.html` (noindex) |
| `/about/` | `about/index.html` |
| `/disclosure/` | `disclosure/index.html` |
| `/privacy/` | `privacy/index.html` |
| `/contact/` | `contact/index.html` |
| `/sitemap.xml` | `sitemap.xml` |
| `/robots.txt` | `robots.txt` |

### Phase 2: Cost & Quote pillar (May 2026)

| URL | File |
|---|---|
| `/radon-mitigation-cost/` | `radon-mitigation-cost/index.html` (statewide cost anchor) |
| `/radon-mitigation-cost/quote-variation/` | `radon-mitigation-cost/quote-variation/index.html` |
| `/radon-mitigation-cost/quote-too-high/` | `radon-mitigation-cost/quote-too-high/index.html` |
| `/radon-mitigation-cost/whats-in-a-quote/` | `radon-mitigation-cost/whats-in-a-quote/index.html` |
| `/radon-mitigation-cost/crawlspaces/` | `radon-mitigation-cost/crawlspaces/index.html` |
| `/radon-mitigation-cost/finished-basements/` | `radon-mitigation-cost/finished-basements/index.html` |
| `/radon-mitigation-cost/real-estate-deadlines/` | `radon-mitigation-cost/real-estate-deadlines/index.html` |

## Before you launch

1. **Quote form back end (Netlify Forms).** `request-quote/index.html` uses Netlify Forms (`data-netlify="true"`, `name="quote-request"`). On deploy, Netlify auto-detects the form; submissions appear in the Netlify dashboard under **Forms → quote-request**. Email and Slack notifications can be added under **Forms → Notifications**. The form POSTs hidden `city` and `source_page` fields for lead attribution, plus a honeypot `bot-field` for spam protection.
2. **Contact email.** `contact/index.html` shows `hello@coloradoradonguide.com` as a placeholder. Replace with your real address.
3. **Phone number.** Not currently published. When you have a tracked number, add a `tel:` link to `_build/template.py` in the header CTA and rebuild.
4. **Domain & DNS.** Live at `coloradoradonguide.com`, hosted on Netlify.
5. **Search Console.** Verify domain ownership, submit `https://coloradoradonguide.com/sitemap.xml`, and request indexing for the four guide pages first (homepage, CS hub, CS cost, CS failed test).
6. **Analytics.** Add Plausible/Fathom/Google Analytics by inserting the script tag in `_build/template.py` (head of every page) and rebuilding.
7. **Privacy policy.** The shipped privacy policy is a plain-language V1. Before paid traffic or expanding states, have an attorney review and replace it with a jurisdiction-appropriate version.

## Editing content

The HTML pages are generated from Python templates under `_build/`:

- `template.py` — shared HTML shell, CSS, header/footer, schema helpers, page renderer
- `pages_main.py` — homepage + Colorado Springs hub content + shared `SOURCES` dict
- `pages_cs.py` — Colorado Springs testing and failed-test page content
- `pages_cost.py` — Phase 2 Cost & Quote pillar (8 pages including refreshed CS cost)
- `pages_misc.py` — quote form, thank-you, about, disclosure, privacy, contact
- `build.py` — orchestrator that calls `render_page()` for each URL

To rebuild after edits:

```bash
python3 _build/build.py
```

## SEO elements present

- Unique `<title>` and `<meta name="description">` on every page
- Canonical link tag on every page
- Open Graph and Twitter card meta
- JSON-LD: `Organization` and `WebSite` site-wide; `BreadcrumbList` per inner page; `FAQPage` on Colorado Springs hub, cost, and failed-test pages; `Article` on the guide pages
- Internal cross-linking via the "Keep reading" block at the bottom of every guide
- `sitemap.xml` listing every V1 URL
- `robots.txt` allowing crawl with `/request-quote/thank-you/` disallowed
- Mobile-first responsive CSS, one Google Font preconnect

## Sources cited in V1

Every numeric or legal claim is linked to its primary source:

- CDPHE — <https://cdphe.colorado.gov/radon>
- EPA — <https://www.epa.gov/radon>
- El Paso County Public Health — <https://www.elpasocountyhealth.org/radon>
- Colorado DORA Office of Radon Professionals — <https://dpo.colorado.gov/Radon>
- Colorado SB23-206 — <https://leg.colorado.gov/bills/sb23-206>

## License

This site is an independent editorial resource. All third-party content is cited and links to its source. The site code in this repository is private to the operator unless otherwise specified.
