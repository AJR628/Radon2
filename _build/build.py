"""Generate all V1 HTML pages, sitemap.xml, robots.txt, and README.md."""
import os
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from template import render_page, SITE_URL, SITE_NAME, LAST_UPDATED  # noqa: E402
from pages_main import HOMEPAGE_BODY, CS_HUB_BODY, cs_hub_faq_jsonld  # noqa: E402
from pages_cs import (  # noqa: E402
    CS_COST_BODY, cs_cost_faq_jsonld,
    CS_TESTING_BODY,
    CS_FAILED_BODY, cs_failed_faq_jsonld,
)
from pages_misc import (  # noqa: E402
    QUOTE_BODY, QUOTE_THANKYOU_BODY,
    ABOUT_BODY, DISCLOSURE_BODY,
    PRIVACY_BODY, CONTACT_BODY,
)


ROOT = Path(__file__).parent.parent
print(f"Building site into {ROOT}")


def article_schema(url_path, headline, description):
    obj = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": SITE_URL + url_path,
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
        },
        "dateModified": "2026-05-21",
        "author": {"@type": "Organization", "name": SITE_NAME},
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


def write(path: str, content: str):
    fp = ROOT / path
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content, encoding="utf-8")
    print(f"  wrote {path} ({len(content):,} bytes)")


# -------------------------------------------------------------------------
# Pages
# -------------------------------------------------------------------------

# 1. HOMEPAGE
write("index.html", render_page(
    url_path="/",
    title="Colorado Radon Guide — Testing, Mitigation Cost & Next Steps",
    description="Independent Colorado radon guide. Learn radon risk in Colorado, the 4.0 pCi/L EPA action level, mitigation cost ranges, and how to find a licensed local contractor.",
    h1="Your independent Colorado radon guide",
    hero_eyebrow="Statewide guide",
    hero_lede="Roughly half of Colorado homes test above the EPA radon action level. This is the calm, sourced, contractor-independent guide to what radon is, what testing costs, what mitigation costs, and what to do next.",
    hero_meta='<span><strong>Updated</strong> ' + LAST_UPDATED + '</span> <span><strong>Sources</strong> CDPHE • EPA • El Paso County • Colorado DORA</span>',
    body_html=HOMEPAGE_BODY,
    breadcrumbs=[("Home", "/")],
    show_breadcrumbs=False,
    show_cta_banner=True,
    related=[
        ("Colorado Springs", "Local prevalence, testing, mitigation, real estate", "/colorado-springs/"),
        ("Mitigation Cost", "Typical ranges and what moves the price", "/colorado-springs/radon-mitigation-cost/"),
        ("After a Failed Test", "Step-by-step next steps for homeowners and buyers", "/colorado-springs/failed-radon-test/"),
    ],
))

# 2. COLORADO SPRINGS HUB
write("colorado-springs/index.html", render_page(
    url_path="/colorado-springs/",
    title="Radon in Colorado Springs — Testing, Mitigation & Cost Guide",
    description="Colorado Springs radon guide. El Paso County radon prevalence, testing options, mitigation cost ranges, licensed contractor verification, and SB23-206 real estate rules.",
    h1="Radon in Colorado Springs",
    hero_eyebrow="Colorado Springs · El Paso County",
    hero_lede="El Paso County is EPA Zone 1 and more than 40% of homes tested 2005–2023 came back above the EPA action level. Here is the full local guide.",
    body_html=CS_HUB_BODY,
    breadcrumbs=[("Home", "/"), ("Colorado Springs", "/colorado-springs/")],
    extra_jsonld=[
        cs_hub_faq_jsonld(),
        article_schema("/colorado-springs/", "Radon in Colorado Springs", "A local guide to radon testing, mitigation, cost, and real estate rules in Colorado Springs."),
    ],
    related=[
        ("Mitigation Cost", "Typical ranges and what moves the price", "/colorado-springs/radon-mitigation-cost/"),
        ("Radon Testing", "DIY kits, professional tests, action level", "/colorado-springs/radon-testing/"),
        ("Failed Test", "Step-by-step for homeowners and buyers", "/colorado-springs/failed-radon-test/"),
    ],
))

# 3. CS COST
write("colorado-springs/radon-mitigation-cost/index.html", render_page(
    url_path="/colorado-springs/radon-mitigation-cost/",
    title="Radon Mitigation Cost in Colorado Springs (2026 Guide)",
    description="What radon mitigation typically costs in Colorado Springs. CDPHE baseline ranges, scenario-by-scenario pricing, what moves the price, and why two quotes differ.",
    h1="Radon Mitigation Cost in Colorado Springs",
    hero_eyebrow="Cost guide",
    hero_lede="The short answer: $1,000–$2,000 for a typical Colorado mitigation system. The longer answer depends on your foundation, layout, and what's in the written scope.",
    body_html=CS_COST_BODY,
    breadcrumbs=[
        ("Home", "/"),
        ("Colorado Springs", "/colorado-springs/"),
        ("Mitigation Cost", "/colorado-springs/radon-mitigation-cost/"),
    ],
    extra_jsonld=[
        cs_cost_faq_jsonld(),
        article_schema("/colorado-springs/radon-mitigation-cost/", "Radon Mitigation Cost in Colorado Springs", "Typical Colorado Springs radon mitigation cost ranges, what moves the price, and how to evaluate a written quote."),
    ],
    related=[
        ("Radon Testing", "DIY kits, professional tests, action level", "/colorado-springs/radon-testing/"),
        ("Failed Test", "Step-by-step for homeowners and buyers", "/colorado-springs/failed-radon-test/"),
        ("Colorado Springs Hub", "Local prevalence, systems, real estate", "/colorado-springs/"),
    ],
))

# 4. CS TESTING
write("colorado-springs/radon-testing/index.html", render_page(
    url_path="/colorado-springs/radon-testing/",
    title="Radon Testing in Colorado Springs — DIY Kits & Pro Tests",
    description="Radon testing options for Colorado Springs homes. Short-term vs long-term kits, professional measurement, the EPA action level, and when to retest.",
    h1="Radon Testing in Colorado Springs",
    hero_eyebrow="Testing guide",
    hero_lede="Three test types, where to get a kit locally, how to place it correctly, and how to read the result. Plus the rules for real estate transactions.",
    body_html=CS_TESTING_BODY,
    breadcrumbs=[
        ("Home", "/"),
        ("Colorado Springs", "/colorado-springs/"),
        ("Radon Testing", "/colorado-springs/radon-testing/"),
    ],
    extra_jsonld=[
        article_schema("/colorado-springs/radon-testing/", "Radon Testing in Colorado Springs", "DIY kits, professional measurement, and how to interpret your radon result in Colorado Springs."),
    ],
    related=[
        ("Mitigation Cost", "Typical ranges and what moves the price", "/colorado-springs/radon-mitigation-cost/"),
        ("Failed Test", "What to do when your test comes back high", "/colorado-springs/failed-radon-test/"),
        ("Colorado Springs Hub", "Local prevalence, systems, real estate", "/colorado-springs/"),
    ],
))

# 5. CS FAILED TEST
write("colorado-springs/failed-radon-test/index.html", render_page(
    url_path="/colorado-springs/failed-radon-test/",
    title="Failed Radon Test in Colorado Springs — What to Do Next",
    description="Your radon test came back above 4.0 pCi/L. Step-by-step next steps for Colorado Springs homeowners, buyers, sellers, and tenants — plus closing deadlines.",
    h1="Your radon test came back high — here's what to do",
    hero_eyebrow="High result · Next steps",
    hero_lede="A reading at or above 4.0 pCi/L isn't a crisis. It's a project. Here's the playbook by situation — homeowner, buyer, seller, tenant.",
    body_html=CS_FAILED_BODY,
    breadcrumbs=[
        ("Home", "/"),
        ("Colorado Springs", "/colorado-springs/"),
        ("Failed Radon Test", "/colorado-springs/failed-radon-test/"),
    ],
    extra_jsonld=[
        cs_failed_faq_jsonld(),
        article_schema("/colorado-springs/failed-radon-test/", "Failed Radon Test in Colorado Springs", "What to do after a high radon test in Colorado Springs — by homeowner situation, real estate role, and closing deadline."),
    ],
    related=[
        ("Mitigation Cost", "What you should expect to pay", "/colorado-springs/radon-mitigation-cost/"),
        ("Radon Testing", "How to confirm a result", "/colorado-springs/radon-testing/"),
        ("Get a Quote", "Connect with a licensed Colorado contractor", "/request-quote/"),
    ],
))

# 6. QUOTE REQUEST
write("request-quote/index.html", render_page(
    url_path="/request-quote/",
    title="Request a Colorado Springs Radon Quote — Colorado Radon Guide",
    description="Submit your radon situation and we'll connect you with a licensed Colorado radon mitigation partner. Free, no obligation, no high-pressure sales.",
    h1="Request a radon quote",
    hero_eyebrow="Quote request",
    hero_lede="Tell us about your home and your radon situation. We route one inquiry to one licensed Colorado mitigation partner — no spam, no contractor pile-ons.",
    body_html=QUOTE_BODY,
    breadcrumbs=[("Home", "/"), ("Request a Quote", "/request-quote/")],
    show_cta_banner=False,
))

# 7. QUOTE THANK YOU (noindex)
THANKYOU_HTML = render_page(
    url_path="/request-quote/thank-you/",
    title="Thank you — Quote Request Received",
    description="Your radon quote request has been received. A licensed Colorado mitigation partner will reach out shortly.",
    h1="Thanks — your request is in",
    hero_eyebrow="Confirmation",
    hero_lede="One licensed Colorado mitigation partner has been notified and will reach out within one business day.",
    body_html=QUOTE_THANKYOU_BODY,
    breadcrumbs=[
        ("Home", "/"),
        ("Request a Quote", "/request-quote/"),
        ("Thank You", "/request-quote/thank-you/"),
    ],
    show_cta_banner=False,
)
THANKYOU_HTML = THANKYOU_HTML.replace(
    '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">',
    '<meta name="robots" content="noindex,follow">',
)
write("request-quote/thank-you/index.html", THANKYOU_HTML)

# 8. ABOUT
write("about/index.html", render_page(
    url_path="/about/",
    title="About Colorado Radon Guide",
    description="Who we are: an independent Colorado radon resource. Our editorial mission, sources, and what we do and do not do.",
    h1="About Colorado Radon Guide",
    hero_eyebrow="About",
    hero_lede="An independent editorial resource for Colorado homeowners, buyers, and sellers navigating radon. Not a contractor, not a referral mill, not a marketing site.",
    body_html=ABOUT_BODY,
    breadcrumbs=[("Home", "/"), ("About", "/about/")],
    show_cta_banner=False,
))

# 9. DISCLOSURE
write("disclosure/index.html", render_page(
    url_path="/disclosure/",
    title="Editorial & Lead Routing Disclosure — Colorado Radon Guide",
    description="How Colorado Radon Guide is funded, how leads are routed to a licensed mitigation partner, and the editorial separation between the two.",
    h1="Editorial and lead routing disclosure",
    hero_eyebrow="Disclosure",
    hero_lede="Plain-language: how we make money, who gets your quote request, and what separates editorial from advertising on this site.",
    body_html=DISCLOSURE_BODY,
    breadcrumbs=[("Home", "/"), ("Disclosure", "/disclosure/")],
    show_cta_banner=False,
))

# 10. PRIVACY
write("privacy/index.html", render_page(
    url_path="/privacy/",
    title="Privacy Policy — Colorado Radon Guide",
    description="How Colorado Radon Guide collects, uses, and shares data from quote requests and site visits.",
    h1="Privacy policy",
    hero_eyebrow="Privacy",
    hero_lede="What we collect, how we use it, who we share it with, and how to request a copy or deletion of your data.",
    body_html=PRIVACY_BODY,
    breadcrumbs=[("Home", "/"), ("Privacy", "/privacy/")],
    show_cta_banner=False,
))

# 11. CONTACT
write("contact/index.html", render_page(
    url_path="/contact/",
    title="Contact Colorado Radon Guide",
    description="Reach Colorado Radon Guide for press, corrections, partner inquiries, and general questions. For radon quotes, use the quote request form.",
    h1="Contact us",
    hero_eyebrow="Contact",
    hero_lede="Quote request? Use the form. Press, corrections, or contractor partnership? Email us at the address below.",
    body_html=CONTACT_BODY,
    breadcrumbs=[("Home", "/"), ("Contact", "/contact/")],
    show_cta_banner=False,
))

# -------------------------------------------------------------------------
# sitemap.xml + robots.txt
# -------------------------------------------------------------------------
SITEMAP_URLS = [
    ("/", "1.0"),
    ("/colorado-springs/", "0.9"),
    ("/colorado-springs/radon-mitigation-cost/", "0.9"),
    ("/colorado-springs/radon-testing/", "0.9"),
    ("/colorado-springs/failed-radon-test/", "0.9"),
    ("/request-quote/", "0.8"),
    ("/about/", "0.4"),
    ("/disclosure/", "0.4"),
    ("/privacy/", "0.3"),
    ("/contact/", "0.4"),
]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path, priority in SITEMAP_URLS:
    sitemap += f"  <url>\n"
    sitemap += f"    <loc>{SITE_URL}{path}</loc>\n"
    sitemap += f"    <lastmod>2026-05-21</lastmod>\n"
    sitemap += f"    <changefreq>monthly</changefreq>\n"
    sitemap += f"    <priority>{priority}</priority>\n"
    sitemap += f"  </url>\n"
sitemap += "</urlset>\n"
write("sitemap.xml", sitemap)

robots = f"""# Colorado Radon Guide robots.txt
User-agent: *
Allow: /
Disallow: /request-quote/thank-you/

Sitemap: {SITE_URL}/sitemap.xml
"""
write("robots.txt", robots)

# -------------------------------------------------------------------------
# README
# -------------------------------------------------------------------------
readme = """# ColoradoRadonGuide.com

Static V1 website for ColoradoRadonGuide.com — an independent Colorado radon information and quote-connection resource.

## Stack

Plain HTML + CSS. No build step is required to deploy. The HTML in this repo is the final, deployable output.

The Python files under `_build/` are the source-of-truth templates that produced the HTML. If you change content, edit `_build/` and re-run `python3 _build/build.py`. If you only want to tweak copy on a single page, you can edit the HTML directly — just keep the change in `_build/` too if you plan to rebuild later.

## V1 page inventory

| URL | File |
|---|---|
| `/` | `index.html` |
| `/colorado-springs/` | `colorado-springs/index.html` |
| `/colorado-springs/radon-mitigation-cost/` | `colorado-springs/radon-mitigation-cost/index.html` |
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

## Before you launch

1. **Quote form back end.** `request-quote/index.html` is wired to FormSubmit with the placeholder `REPLACE_WITH_YOUR_EMAIL` in the form `action` attribute. Replace it with your live email or swap the `action` for your CRM/webhook (Airtable, HubSpot, Zapier, etc.). The form also POSTs hidden `city` and `source_page` fields so you can attribute leads.
2. **Contact email.** `contact/index.html` shows `hello@coloradoradonguide.com` as a placeholder. Replace with your real address.
3. **Phone number.** Not currently published. When you have a tracked number, add a `tel:` link to `_build/template.py` in the header CTA and rebuild.
4. **Domain & DNS.** Point `coloradoradonguide.com` at your host. The site is plain static HTML — Cloudflare Pages, Netlify, Vercel, or GitHub Pages all work without modification.
5. **Search Console.** Verify domain ownership, submit `https://coloradoradonguide.com/sitemap.xml`, and request indexing for the four guide pages first (homepage, CS hub, CS cost, CS failed test).
6. **Analytics.** Add Plausible/Fathom/Google Analytics by inserting the script tag in `_build/template.py` (head of every page) and rebuilding.
7. **Privacy policy.** The shipped privacy policy is a plain-language V1. Before paid traffic or expanding states, have an attorney review and replace it with a jurisdiction-appropriate version.

## Editing content

The HTML pages are generated from Python templates under `_build/`:

- `template.py` — shared HTML shell, CSS, header/footer, schema helpers, page renderer
- `pages_main.py` — homepage + Colorado Springs hub content
- `pages_cs.py` — cost, testing, failed-test page content
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
"""
write("README.md", readme)

print("\nBuild complete.")
