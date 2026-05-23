"""Page content for the statewide homepage and Colorado Springs hub."""
import json

# Source URLs used across the site
SOURCES = {
    "cdphe_radon": "https://cdphe.colorado.gov/radon",
    "cdphe_realestate": "https://cdphe.colorado.gov/radon/radon-and-real-estate",
    "epa_radon": "https://www.epa.gov/radon",
    "epa_action_level": "https://www.epa.gov/radon/health-risk-radon",
    "elpaso_radon": "https://www.elpasocountyhealth.org/radon",
    "denver_radon": "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Public-Health-Environment/Public-Health-Investigations/Healthy-Families-Healthy-Homes/Radon",
    "sb23_206": "https://leg.colorado.gov/bills/sb23-206",
    "dora_radon": "https://dpo.colorado.gov/RadonProfessionals",
    "nrpp": "https://nrpp.info/",
    "nrsb": "https://nrsb.org/",
}

def s(name):
    return SOURCES[name]


# =========================================================================
# HOMEPAGE — new photo-led hero, then mechanism explainer with diagram,
# then stats, action paths, law, trust line, city pick.
# =========================================================================

HOMEPAGE_HERO = f"""<section class="hero-photo">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-text">
        <span class="eyebrow">Colorado Radon Guide</span>
        <h1>Radon is in roughly half of Colorado homes. Here's what to do about yours.</h1>
        <p class="lede">Colorado's geology means most homes here have elevated indoor radon. The good news: it's testable, fixable, and the state has clear rules to help you navigate it. This is the calm, sourced guide to understanding your situation and what it should cost.</p>
        <div class="hero-buttons">
          <a href="/request-quote/" class="btn">Get a free Colorado quote</a>
          <a href="/colorado-radon-map/" class="btn btn-secondary">See the Colorado radon map</a>
        </div>
        <div class="hero-meta">
          <span><strong>Updated</strong> May 2026</span>
          <span><strong>Sources</strong> CDPHE · EPA · El Paso County · Colorado DORA</span>
        </div>
      </div>
      <div class="hero-image">
        <img src="/assets/images/hero-colorado-homes.jpg" alt="A Colorado home against the Rocky Mountain foothills." width="1600" height="1067">
        <a class="img-credit" href="https://unsplash.com/photos/HrGBOlyASYE" rel="noopener" target="_blank">Photo: Unsplash</a>
      </div>
    </div>
  </div>
</section>
<section class="decision-strip">
  <div class="container">
    <div class="lead-in">
      <span class="eyebrow">Where to start</span>
      <h2>Pick what sounds like you</h2>
      <p>Six common situations. Each links straight to the page that answers it.</p>
    </div>
    <div class="decision-grid">
      <a href="/colorado-radon-map/" class="decision-card">
        <span class="scenario">I want a visual sense of Colorado radon risk by area.</span>
        <span class="destination">See the Colorado radon map</span>
      </a>
      <a href="/radon-testing/" class="decision-card">
        <span class="scenario">I haven't tested my home yet.</span>
        <span class="destination">How to test for radon in Colorado</span>
      </a>
      <a href="/colorado-springs/failed-radon-test/" class="decision-card">
        <span class="scenario">My test came back high. What now?</span>
        <span class="destination">Failed radon test next steps</span>
      </a>
      <a href="/radon-mitigation-cost/quote-too-high/" class="decision-card">
        <span class="scenario">I have a mitigation quote and want to evaluate it.</span>
        <span class="destination">Is my quote fair?</span>
      </a>
      <a href="/radon-testing/during-real-estate-transactions/" class="decision-card">
        <span class="scenario">I'm buying or selling a Colorado home.</span>
        <span class="destination">Radon in real estate (SB23-206)</span>
      </a>
      <a href="/request-quote/" class="decision-card is-featured">
        <span class="scenario">I'm ready for a quote from a licensed Colorado contractor.</span>
        <span class="destination">Request a free quote</span>
      </a>
    </div>
  </div>
</section>"""


HOMEPAGE_BODY = f"""
<section>
  <h2>How radon gets into a Colorado home</h2>
  <div class="explainer">
    <div class="explainer-text">
      <p>Radon is an invisible, odorless gas produced by the natural decay of uranium in soil and rock. Colorado's Rocky Mountain geology is uranium-rich, so radon levels under homes here are higher than in most of the U.S. — the EPA places most of the Front Range, including El Paso County, in <strong>Zone 1</strong>: the highest indoor radon potential. (53 of Colorado's 64 counties are Zone 1; <a href="/colorado-radon-map/">see the Colorado radon map for full context</a>.)<sup><a href="#src-2">[2]</a></sup></p>
      <p>The gas rises out of the soil and finds its way indoors through small openings in the foundation: hairline slab cracks, the gap where the floor meets the wall, plumbing penetrations, sump pits, and unsealed crawl spaces. Once inside, it accumulates in lower levels — basements first, then living areas above.</p>
      <p>Two things matter: <strong>most Colorado homes have some radon</strong>, and <strong>you can't tell by sight or smell whether yours is above the action level</strong>. The only way to know is a test.</p>
    </div>
    <figure class="figure">
      <img src="/assets/images/radon-entry-diagram.jpg" alt="Cross-section illustration of a home showing radon gas rising from soil through foundation cracks and accumulating in the basement." width="1200" height="896" loading="lazy">
      <figcaption><strong>How radon enters a home.</strong> Soil gas rises through small foundation cracks, the floor-wall joint, sump pits, and plumbing penetrations into the basement and living space above.</figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">Colorado Homes</div>
      <div class="stat">~50%</div>
      <div class="source">test above the EPA action level. Source: <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a></div>
    </div>
    <div class="factbox">
      <div class="label">EPA Action Level</div>
      <div class="stat">4.0 pCi/L</div>
      <div class="source">Mitigate at or above this. Source: <a href="{s('epa_action_level')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
    <div class="factbox">
      <div class="label">El Paso County</div>
      <div class="stat">40%+</div>
      <div class="source">of homes tested 2005–2023 had high radon. Source: <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health</a></div>
    </div>
    <div class="factbox">
      <div class="label">Typical Mitigation</div>
      <div class="stat">$1,000–$2,000</div>
      <div class="source">baseline cost; complex jobs cost more. Source: <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a></div>
    </div>
  </div>
</section>

<section>
  <h2>Step one is always testing</h2>
  <div class="prose-wide">
    <p>You cannot smell, see, or feel radon. The only way to know your level is to test. CDPHE recommends every Colorado home be tested, and EPA guidance is to retest every two years or after major remodels or HVAC changes.<sup><a href="#src-1">[1]</a></sup></p>
    <p>You have three practical options:</p>
    <ul>
      <li><strong>Short-term DIY kit</strong> (2–7 days). Low-cost, available at retail and from CDPHE programs.</li>
      <li><strong>Long-term DIY kit</strong> (90+ days). Better picture of year-round exposure.</li>
      <li><strong>Professional measurement</strong> by a tester certified through the National Radon Proficiency Program (NRPP) or the National Radon Safety Board (NRSB), required for real estate transactions.<sup><a href="#src-4">[4]</a></sup></li>
    </ul>
    <p>Our <a href="/colorado-springs/radon-testing/">Colorado Springs testing guide</a> walks through each option, what they cost, and how to read the result.</p>
  </div>
</section>

<section>
  <h2>If your test is high, the fix is straightforward</h2>
  <div class="prose-wide">
    <p>A result at or above 4.0 pCi/L is the EPA's action threshold. The standard fix is <strong>active sub-slab depressurization</strong> — a sealed vent pipe and a quiet electric fan that pulls radon from under the slab and exhausts it above the roofline. Homes with crawl spaces use a sub-membrane variant; sump pits and drain tile can be tied into the same system.</p>
    <p>A correctly designed system typically reduces indoor radon by <strong>80–99%</strong>.<sup><a href="#src-2">[2]</a></sup> CDPHE and El Paso County both put a typical Colorado mitigation system in the <strong>$1,000–$2,000</strong> range, with larger or more complex installations costing more.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-5">[5]</a></sup> Our <a href="/colorado-springs/radon-mitigation-cost/">cost page</a> breaks down what drives the price.</p>
    <p>Caulking, sealing, or running fans alone is <strong>not</strong> a substitute for a properly engineered system. CDPHE notes that sealing cracks alone is unreliable and can sometimes make things worse.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>What Colorado law and licensing actually say</h2>
  <div class="prose-wide">
    <p>Two recent changes shape every Colorado radon decision:</p>
    <ul>
      <li><strong>Contractor licensing (July 2022).</strong> All radon measurement and mitigation professionals working in Colorado must be certified through NRPP or NRSB <em>and</em> registered with the <a href="{s('dora_radon')}" rel="noopener" target="_blank">Colorado Department of Regulatory Agencies (DORA) Office of Radon Professionals</a>. Always verify a contractor's registration before hiring.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>Real estate disclosure — SB23-206 (2023).</strong> Every residential sale and lease in Colorado must include a radon warning, any known test results, and any mitigation history. The CDPHE radon brochure must be provided. After January 2026, tenants gain additional remedies if a known elevated radon level was not mitigated.<sup><a href="#src-6">[6]</a></sup></li>
    </ul>
    <p>Important nuance: Colorado does <strong>not</strong> require a seller to test or mitigate — only to disclose what they know.<sup><a href="#src-1">[1]</a></sup> "No disclosure" usually means "no test was done," not "no radon."</p>
  </div>
</section>

<section>
  <h2>Pick your area</h2>
  <p style="max-width:42rem;color:var(--text-muted);">Currently building local guides for Colorado Springs and Denver, with more Colorado areas coming. Outside these two? The statewide pillar pages (testing, mitigation, cost, contractor selection) apply everywhere in Colorado — and the quote form routes by ZIP, not city.</p>
  <div class="card-grid">
    <div class="card">
      <h3>Colorado Springs</h3>
      <p>El Paso County is EPA Zone 1; more than 40% of homes tested 2005–2023 came back high. Start here for testing, mitigation cost, and what to do after a failed result.</p>
      <p><a href="/colorado-springs/" class="btn btn-secondary">Open the Colorado Springs hub</a></p>
    </div>
    <div class="card">
      <h3>Denver</h3>
      <p>Denver and every Denver Metro county sits in EPA Zone 1. Denver's housing mix — older bungalows, full basements, finished lower levels — directly shapes how testing and mitigation play out. Start here if you live in Denver or the metro.</p>
      <p><a href="/denver/" class="btn btn-secondary">Open the Denver hub</a></p>
    </div>
    <div class="card">
      <h3>Other Colorado area</h3>
      <p>The site's pillar pages — <a href="/radon-testing/">testing</a>, <a href="/radon-mitigation-systems/">mitigation systems</a>, <a href="/radon-mitigation-cost/">cost</a>, <a href="/radon-contractors/">choosing a contractor</a> — apply statewide. <a href="/contact/">Tell us</a> what city you'd like covered next.</p>
      <p><span class="pill">Statewide pillars</span></p>
    </div>
  </div>
</section>

<section>
  <div class="callout">
    <strong>About this guide.</strong>
    <p>Colorado Radon Guide is an independent editorial resource. We do not install mitigation systems and are not a contractor. When you request a quote, your information is routed to one licensed Colorado mitigation partner. <a href="/about/">More about us</a> · <a href="/disclosure/">How leads are routed</a>.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado Department of Public Health and Environment. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">U.S. Environmental Protection Agency. <em>Radon</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-3">U.S. Environmental Protection Agency. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-4">Colorado Department of Regulatory Agencies. <em>Office of Radon Professionals</em>. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
    <li id="src-5">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-6">Colorado General Assembly. <em>SB23-206: Concerning measures to mitigate the effects of radon in residential properties</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


# =========================================================================
# COLORADO SPRINGS HUB — photo-led hero with Pikes Peak imagery, same
# explainer pattern, calmer ordering.
# =========================================================================

CS_HUB_HERO = f"""<section class="hero-photo">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-text">
        <span class="eyebrow">Colorado Springs · El Paso County</span>
        <h1>Radon in Colorado Springs: what's normal, what's elevated, and what to do.</h1>
        <p class="lede">El Paso County is EPA Zone 1, and county public-health data shows more than 40% of homes tested between 2005 and 2023 came back above the action level. This is your local guide to testing, mitigation, cost, and what to do under a closing deadline.</p>
        <div class="hero-buttons">
          <a href="/colorado-springs/radon-mitigation-cost/" class="btn">See typical Colorado Springs costs</a>
          <a href="/colorado-springs/radon-testing/" class="btn btn-secondary">How to test</a>
        </div>
        <div class="hero-meta">
          <span><strong>Updated</strong> May 2026</span>
          <span><strong>Local source</strong> El Paso County Public Health</span>
        </div>
      </div>
      <div class="hero-image">
        <img src="/assets/images/hero-pikes-peak.jpg" alt="Pikes Peak rising behind Colorado Springs." width="1600" height="1071">
        <a class="img-credit" href="https://unsplash.com/s/photos/pikes-peak" rel="noopener" target="_blank">Photo: Unsplash</a>
      </div>
    </div>
  </div>
</section>"""


CS_HUB_BODY = f"""
<section>
  <div class="callout">
    <strong>New here? Start with the Colorado radon map.</strong>
    <p>El Paso County is in EPA Zone 1, the highest predicted-radon classification. The <a href="/colorado-radon-map/">Colorado Radon Map</a> shows how El Paso County compares to the other 63 Colorado counties and what the EPA zone classification does and doesn't tell you about your specific home.</p>
  </div>
</section>

<section>
  <h2>How radon gets into a Colorado Springs home</h2>
  <div class="explainer">
    <div class="explainer-text">
      <p>The same uranium-rich Rocky Mountain geology that gives Colorado Springs Pikes Peak as a backdrop is the reason radon is common indoors here. Radon is the natural decay product of uranium in soil and rock, and the EPA classifies El Paso County in <strong>Zone 1</strong>: the highest indoor radon potential.<sup><a href="#src-2">[2]</a></sup></p>
      <p>The gas rises out of the soil under and around the foundation, finds its way through cracks, sump pits, drain tile, and crawl-space openings, and accumulates indoors. Basements and finished lower levels see the highest readings; slab-on-grade homes still have radon but typically less than multi-level homes.</p>
      <p>That's why both CDPHE and El Paso County Public Health recommend <strong>every home in the county be tested</strong>.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-5">[5]</a></sup></p>
    </div>
    <figure class="figure">
      <img src="/assets/images/radon-entry-diagram.jpg" alt="Cross-section illustration of a home showing radon gas rising from soil through foundation cracks and accumulating in the basement." width="1200" height="896" loading="lazy">
      <figcaption><strong>How radon enters a home.</strong> Soil gas rises through small foundation cracks, the floor-wall joint, sump pits, and plumbing penetrations into the basement and living space above.</figcaption>
    </figure>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">El Paso County</div>
      <div class="stat">40%+</div>
      <div class="source">of homes tested above 4.0 pCi/L (2005–2023). Source: <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health</a></div>
    </div>
    <div class="factbox">
      <div class="label">EPA Zone</div>
      <div class="stat">Zone 1</div>
      <div class="source">Highest indoor radon potential category. Source: <a href="{s('epa_radon')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
    <div class="factbox">
      <div class="label">Typical Cost</div>
      <div class="stat">$1,000–$2,000</div>
      <div class="source">For most Colorado homes; complex jobs cost more. Source: <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a></div>
    </div>
  </div>
</section>

<section>
  <h2>Step 1 — Test</h2>
  <div class="prose-wide">
    <p>Every Colorado Springs home should be tested. CDPHE recommends testing at least every two years and after any major remodel or HVAC change. Short-term DIY kits are the fastest way to find out where you stand; long-term kits give a more complete year-round picture.</p>
    <p>For real estate transactions, the test must be performed by a professional certified through NRPP or NRSB and registered with the Colorado DORA Office of Radon Professionals.<sup><a href="#src-3">[3]</a></sup></p>
    <p><a href="/colorado-springs/radon-testing/" class="btn btn-secondary">Read the testing guide →</a></p>
  </div>
</section>

<section>
  <h2>Step 2 — If you're above 4.0 pCi/L, mitigate</h2>
  <div class="prose-wide">
    <p>The standard mitigation system in Colorado Springs is <strong>active sub-slab depressurization</strong>: a sealed PVC vent pipe runs from beneath the slab up through the home and discharges above the roofline, pulled by a quiet electric fan in the attic, garage, or exterior. Crawl-space homes use a sealed sub-membrane variant. Sump pits and drain-tile loops can be tied into the same system.</p>
    <p>A properly designed system reduces radon by <strong>80–99%</strong>.<sup><a href="#src-4">[4]</a></sup> Sealing cracks alone is not a fix and is sometimes counterproductive.<sup><a href="#src-5">[5]</a></sup></p>
  </div>
</section>

<section>
  <h2>How much does mitigation cost in Colorado Springs?</h2>
  <div class="prose-wide">
    <p>Use this as a quick orientation, then read the <a href="/colorado-springs/radon-mitigation-cost/">full cost guide</a> for what moves the price.</p>
    <table>
      <thead>
        <tr><th>Scenario</th><th>Typical range</th></tr>
      </thead>
      <tbody>
        <tr><td>Single-family home, single suction point, exterior fan</td><td>$1,000–$1,500</td></tr>
        <tr><td>Larger home, multi-level, finished basement</td><td>$1,500–$2,500</td></tr>
        <tr><td>Crawl space with vapor barrier work</td><td>$1,800–$3,000</td></tr>
        <tr><td>Multiple suction points or unusual foundation</td><td>$2,500+</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Estimates only. Confirm with a written quote from a licensed Colorado contractor. CDPHE places the typical baseline at $1,000–$2,000.<sup><a href="#src-5">[5]</a></sup></p>
  </div>
</section>

<section>
  <h2>If your test came back high</h2>
  <div class="prose-wide">
    <p>A reading above 4.0 pCi/L is the EPA action threshold. What you do next depends on whether you're a homeowner without a transaction pending, a buyer or seller under contract, or a tenant or landlord:</p>
    <ul>
      <li>Confirm the reading with a second test or continuous monitor</li>
      <li>Get at least two written quotes from licensed contractors</li>
      <li>If you're under contract, calculate the closing timeline before negotiating</li>
    </ul>
    <p><a href="/colorado-springs/failed-radon-test/" class="btn btn-secondary">Read the failed-test playbook →</a></p>
  </div>
</section>

<section>
  <h2>How to verify a Colorado radon contractor</h2>
  <div class="prose-wide">
    <p>Since July 2022, every radon measurement and mitigation contractor in Colorado must be certified through <a href="{s('nrpp')}" rel="noopener" target="_blank">NRPP</a> or <a href="{s('nrsb')}" rel="noopener" target="_blank">NRSB</a> <em>and</em> registered with the <a href="{s('dora_radon')}" rel="noopener" target="_blank">Colorado DORA Office of Radon Professionals</a>.<sup><a href="#src-3">[3]</a></sup></p>
    <p>Before you sign anything, ask for:</p>
    <ul class="checklist">
      <li>Their NRPP or NRSB certification number</li>
      <li>Their Colorado DORA registration</li>
      <li>A written scope: number of suction points, fan model and warranty, sealing work, exhaust routing, permit handling</li>
      <li>A post-installation test included in the quote</li>
      <li>A written warranty on the system (fan warranties are typically 5–10 years)</li>
    </ul>
  </div>
</section>

<section>
  <h2>Radon and real estate in Colorado</h2>
  <div class="prose-wide">
    <p>Colorado <strong>SB23-206</strong>, in effect since 2023, requires every residential sale or lease to include a radon warning and disclosure of known test results and any mitigation. Sellers and landlords must provide the CDPHE radon brochure. Colorado does <em>not</em> require sellers to test or mitigate — only to disclose what they know.<sup><a href="#src-6">[6]</a></sup></p>
    <p>For tenants, after January 2026, additional remedies apply if a landlord knew the property had elevated radon and did not mitigate. CDPHE maintains a <a href="{s('cdphe_realestate')}" rel="noopener" target="_blank">dedicated real estate page</a> with the current brochure and forms.</p>
  </div>
</section>

<section>
  <h2>Frequently asked questions</h2>
  <details>
    <summary>Is radon actually a problem in Colorado Springs, or is this overblown?</summary>
    <p>El Paso County Public Health reports more than 40% of homes tested between 2005 and 2023 were above the EPA action level. The county is in EPA Zone 1, the highest indoor radon category. It's a real, locally documented issue — not marketing.<sup><a href="#src-1">[1]</a></sup></p>
  </details>
  <details>
    <summary>How long does mitigation take?</summary>
    <p>Most single-family installations take one day. Add a few days to schedule, plus a post-installation test (which is typically 48 hours). A reasonable end-to-end timeline is one to two weeks once you've signed a quote.</p>
  </details>
  <details>
    <summary>Will I have to retest after mitigation?</summary>
    <p>Yes. A post-mitigation test confirms the system is working. Reputable contractors include this in the quote. After that, EPA guidance is to retest every two years.<sup><a href="#src-4">[4]</a></sup></p>
  </details>
  <details>
    <summary>Do air purifiers fix radon?</summary>
    <p>No. Radon is a soil gas; it has to be redirected away from the home's foundation. Air purifiers don't address the entry pathway and the EPA does not recommend them as a substitute for mitigation.<sup><a href="#src-2">[2]</a></sup></p>
  </details>
  <details>
    <summary>Does Colorado Springs require a permit for mitigation?</summary>
    <p>Mechanical and electrical work on a mitigation system may require a permit; your licensed contractor will pull it. Always confirm the permit is included in the written quote.</p>
  </details>
  <details>
    <summary>What if I can't afford mitigation?</summary>
    <p>CDPHE administers a low-income radon mitigation assistance program. Eligibility and funding vary year to year; check the <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE radon page</a> for the current details.<sup><a href="#src-5">[5]</a></sup></p>
  </details>
</section>

<section>
  <div class="callout">
    <strong>About this guide.</strong>
    <p>Colorado Radon Guide is an independent editorial resource. We do not install mitigation systems and are not a contractor. When you request a quote, your information is routed to one licensed Colorado mitigation partner. <a href="/about/">More about us</a> · <a href="/disclosure/">How leads are routed</a>.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-2">U.S. Environmental Protection Agency. <em>Radon</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-3">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
    <li id="src-4">U.S. Environmental Protection Agency. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-5">Colorado Department of Public Health and Environment. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-6">Colorado General Assembly. <em>SB23-206</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


def cs_hub_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Is radon actually a problem in Colorado Springs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. El Paso County Public Health reports more than 40% of homes tested between 2005 and 2023 were above the EPA action level of 4.0 pCi/L. The county is in EPA Zone 1, the highest indoor radon category."}},
            {"@type": "Question", "name": "How long does radon mitigation take in Colorado Springs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most single-family installations take one day. Add a few days for scheduling and a post-installation test. A reasonable end-to-end timeline is one to two weeks once a quote is signed."}},
            {"@type": "Question", "name": "Do I need to retest after mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. A post-mitigation test confirms the system is working. EPA guidance is to retest every two years afterward."}},
            {"@type": "Question", "name": "Do air purifiers fix radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Radon is a soil gas and must be redirected away from the foundation. The EPA does not recommend air purifiers as a substitute for mitigation."}},
            {"@type": "Question", "name": "Does Colorado Springs require a permit for mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Mechanical and electrical work on a mitigation system may require a permit. A licensed contractor will pull it. Confirm the permit is included in the written quote."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
