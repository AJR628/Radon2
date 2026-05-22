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

### Phase 3: Mitigation Systems pillar (May 2026)

| URL | File |
|---|---|
| `/radon-mitigation-systems/` | `radon-mitigation-systems/index.html` (How Radon Mitigation Works hub) |
| `/radon-mitigation-systems/sub-slab-depressurization/` | `radon-mitigation-systems/sub-slab-depressurization/index.html` |
| `/radon-mitigation-systems/crawlspace-sub-membrane/` | `radon-mitigation-systems/crawlspace-sub-membrane/index.html` |
| `/radon-mitigation-systems/passive-vs-active/` | `radon-mitigation-systems/passive-vs-active/index.html` |
| `/radon-mitigation-systems/fans-pipes-suction-points/` | `radon-mitigation-systems/fans-pipes-suction-points/index.html` |
| `/radon-mitigation-systems/why-sealing-isnt-enough/` | `radon-mitigation-systems/why-sealing-isnt-enough/index.html` |
| `/radon-mitigation-systems/what-happens-after-mitigation/` | `radon-mitigation-systems/what-happens-after-mitigation/index.html` |

### Phase 4: Testing & Real Estate pillar (May 2026)

| URL | File |
|---|---|
| `/radon-testing/` | `radon-testing/index.html` (How to Test for Radon in Colorado hub) |
| `/radon-testing/short-term-vs-long-term/` | `radon-testing/short-term-vs-long-term/index.html` |
| `/radon-testing/where-to-place-a-test/` | `radon-testing/where-to-place-a-test/index.html` |
| `/radon-testing/during-real-estate-transactions/` | `radon-testing/during-real-estate-transactions/index.html` |
| `/radon-testing/for-rentals/` | `radon-testing/for-rentals/index.html` |
| `/radon-testing/for-businesses/` | `radon-testing/for-businesses/index.html` |

### Phase 5a: Radon Basics pillar (May 2026)

| URL | File |
|---|---|
| `/radon-basics/` | `radon-basics/index.html` (What Is Radon hub) |
| `/radon-basics/why-common-in-colorado/` | `radon-basics/why-common-in-colorado/index.html` |
| `/radon-basics/how-it-enters-homes/` | `radon-basics/how-it-enters-homes/index.html` |
| `/radon-basics/health-risks/` | `radon-basics/health-risks/index.html` |
| `/radon-basics/levels-explained/` | `radon-basics/levels-explained/index.html` |
| `/radon-basics/by-foundation-type/` | `radon-basics/by-foundation-type/index.html` |

### Phase 5b: Contractor Selection pillar (May 2026)

| URL | File |
|---|---|
| `/radon-contractors/` | `radon-contractors/index.html` (How to Choose a Contractor hub) |
| `/radon-contractors/verify-licenses-and-certifications/` | `radon-contractors/verify-licenses-and-certifications/index.html` |
| `/radon-contractors/questions-to-ask/` | `radon-contractors/questions-to-ask/index.html` |
| `/radon-contractors/red-flags-in-a-quote/` | `radon-contractors/red-flags-in-a-quote/index.html` |
| `/radon-contractors/warranties-and-retesting/` | `radon-contractors/warranties-and-retesting/index.html` |
| `/radon-contractors/how-to-file-a-complaint/` | `radon-contractors/how-to-file-a-complaint/index.html` |

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
- `pages_systems.py` — Phase 3 Mitigation Systems pillar (7 pages)
- `pages_testing.py` — Phase 4 Testing & Real Estate pillar (6 pages)
- `pages_basics.py` — Phase 5a Radon Basics pillar (6 pages)
- `pages_contractors.py` — Phase 5b Contractor Selection pillar (6 pages)
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
