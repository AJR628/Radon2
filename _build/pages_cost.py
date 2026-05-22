"""Content for the Cost & Quote pillar pages (Phase 2 build).

Eight pages total:
1. /radon-mitigation-cost/                          — statewide anchor (NEW)
2. /colorado-springs/radon-mitigation-cost/        — CS refresh (replaces V1 body)
3. /radon-mitigation-cost/quote-variation/         — Why quotes vary
4. /radon-mitigation-cost/quote-too-high/          — Is my quote too high
5. /radon-mitigation-cost/whats-in-a-quote/        — What should a quote include
6. /radon-mitigation-cost/crawlspaces/             — Crawlspace mitigation cost
7. /radon-mitigation-cost/finished-basements/      — Finished basement cost
8. /radon-mitigation-cost/real-estate-deadlines/   — Cost under closing pressure
"""
import json
from pages_main import s, SOURCES

# Add the extra source URLs the cost pillar uses
SOURCES.setdefault("epa_citizens_guide", "https://www.epa.gov/radon/citizens-guide-radon")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")
SOURCES.setdefault("aarst_standards", "https://standards.aarst.org/")
SOURCES.setdefault("aarst_sgm_sf", "https://aarst.org/product/sgm-sf-2023-pdf/")
SOURCES.setdefault("nrpp_search", "https://nrpp.info/pro-search/")
SOURCES.setdefault("nrsb_search", "https://nrsb.org/for-professional/")
SOURCES.setdefault("dora_lookup", "https://apps.colorado.gov/dora/licensing/Lookup/LicenseLookup.aspx")
SOURCES.setdefault("pprbd", "https://www.pprbd.org/")
SOURCES.setdefault("radonaway_specs", "https://www.radonaway.com/")
SOURCES.setdefault("crec_spd", "https://dre.colorado.gov/division-real-estate-commission-forms")


# =========================================================================
# 1. /radon-mitigation-cost/    — STATEWIDE ANCHOR
# =========================================================================
COST_CO_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you just want the short answer: most Colorado radon mitigation systems land between <strong>$1,000 and $2,000</strong>. That's the range <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a> uses for a standard single-family install, and it's the same range <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health</a> publishes locally.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
    <p>The longer answer is the one you're probably looking for. A real quote on <em>your</em> Colorado home can come in anywhere from $900 to $4,800+ depending on your foundation, your soil, your finishes, and your routing. This page walks through that spread by scenario, what every honest Colorado quote should include, and how to read the difference between a fair $1,400 quote and a fair $3,200 quote — because both can be honest, on the same street.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">CDPHE baseline</div>
      <div class="stat">$1,000–$2,000</div>
      <div class="source">Typical Colorado single-family system. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">Source</a></div>
    </div>
    <div class="factbox">
      <div class="label">Real-world spread</div>
      <div class="stat">$900–$4,800</div>
      <div class="source">Across all foundation types in Colorado Springs market data, 2024–2026</div>
    </div>
    <div class="factbox">
      <div class="label">Reduction</div>
      <div class="stat">Up to 99%</div>
      <div class="source">Properly designed active system. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
    <div class="factbox">
      <div class="label">Operating cost</div>
      <div class="stat">&lt;$10/mo</div>
      <div class="source">Electricity to run the fan. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
  </div>
</section>

<section>
  <h2>The four-scenario framework</h2>
  <div class="prose-wide">
    <p>Cost pages that just quote a national average leave you guessing. Here's what Colorado homeowners actually pay, broken out by the scenario that matches your home. Use this to orient a quote you've received — not to argue with a contractor before they've seen your basement.</p>
    <table>
      <thead>
        <tr><th>Scenario</th><th>Typical Colorado range</th><th>Median</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>A. Basic basement</strong><br><span style="font-size:.88rem;color:var(--text-muted);">Single suction point, exterior PVC routing, standard 4" fan</span></td>
          <td>$900–$1,900</td>
          <td>~$1,400</td>
        </tr>
        <tr>
          <td><strong>B. Finished basement</strong><br><span style="font-size:.88rem;color:var(--text-muted);">Interior routing around drywall, closets, utility space</span></td>
          <td>$1,400–$2,800</td>
          <td>~$1,900</td>
        </tr>
        <tr>
          <td><strong>C. Crawlspace</strong><br><span style="font-size:.88rem;color:var(--text-muted);">Sub-membrane depressurization with sealed vapor barrier</span></td>
          <td>$1,800–$4,000</td>
          <td>~$2,600</td>
        </tr>
        <tr>
          <td><strong>D. Multi-zone foundation</strong><br><span style="font-size:.88rem;color:var(--text-muted);">Basement + crawlspace combination, tri-level, split-level</span></td>
          <td>$2,200–$4,800</td>
          <td>~$3,200</td>
        </tr>
      </tbody>
    </table>
    <p style="font-size:.88rem;color:var(--text-muted);">Bands compiled from CDPHE, El Paso County Public Health, Angi, CostWhale, ProMatcher, InspectAndTest, and Colorado Springs contractor public pricing, 2024–2026.</p>
  </div>
</section>

<section>
  <h2>Why prices vary in Colorado specifically</h2>
  <div class="prose-wide">
    <p>Four things move a Colorado quote that don't show up in a national average:</p>

    <h3>Altitude affects fan sizing</h3>
    <p>Radon fans lose roughly <strong>4% of their airflow capacity for every 1,000 feet of elevation</strong>.<sup><a href="#src-3">[3]</a></sup> Denver sits at 5,280 feet. Colorado Springs is closer to 6,000. That means a fan model that's perfectly sized for sea-level installs may need to be upgraded — or the system may need a second suction point to compensate. A contractor working only off a national catalog spec is more likely to under-fan a Colorado home, and you'll see it in the post-mitigation test result.</p>

    <h3>Front Range geology pushes some homes higher</h3>
    <p>Colorado's uranium-bearing granites and shales sit beneath most homes along the Front Range. That doesn't change the install price directly, but it does mean homes here tend to start with higher radon and may need a more robust system to bring levels below 4.0 pCi/L.<sup><a href="#src-1">[1]</a></sup></p>

    <h3>State-licensed contractor density</h3>
    <p>Colorado is one of the few states with <strong>state-level radon contractor licensing</strong> — through the <a href="{s('dora_radon')}" rel="noopener" target="_blank">DORA Office of Radon Professionals</a>.<sup><a href="#src-4">[4]</a></sup> Quotes from DORA-licensed contractors will reflect the cost of training, certification, and insurance that an unlicensed handyman wouldn't carry. That's not a markup; it's the work being done correctly.</p>

    <h3>Real estate deadline pressure</h3>
    <p>Colorado real estate transactions move quickly. Mitigations done under closing-deadline pressure sometimes carry a small premium for guaranteed-completion scheduling. If you're under contract, see our <a href="/radon-mitigation-cost/real-estate-deadlines/">real-estate deadline cost page</a>.</p>
  </div>
</section>

<section>
  <h2>What every honest Colorado quote includes</h2>
  <div class="prose-wide">
    <p>If a written quote is missing one of these line items, it's not necessarily padded — but it is incomplete. Ask before you sign.</p>
    <ul class="checklist">
      <li><strong>DORA license number</strong> — required for any contractor performing radon mitigation in Colorado<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>NRPP or NRSB certification</strong> — national professional credential, looked up at <a href="{s('nrpp_search')}" rel="noopener" target="_blank">nrpp.info</a> or <a href="{s('nrsb_search')}" rel="noopener" target="_blank">nrsb.org</a></li>
      <li><strong>Number of suction points</strong> and where they'll go</li>
      <li><strong>Fan model and warranty</strong> — typically 5 years on a name-brand fan</li>
      <li><strong>Pipe routing</strong> — interior vs exterior, where it exits, and how high above the roof</li>
      <li><strong>Sealing scope</strong> — slab cracks, sump cover, floor-wall joint, slab penetrations</li>
      <li><strong>Manometer</strong> install location (you should be able to see it from a normal walking path through the basement)</li>
      <li><strong>Permit responsibility</strong> — electrical and mechanical permits, who pulls them</li>
      <li><strong>Post-mitigation test</strong> — within 30 days of install, 2–7 day duration, closed-house conditions<sup><a href="#src-5">[5]</a></sup></li>
      <li><strong>Workmanship warranty</strong> — usually 1–2 years labor, separate from fan warranty</li>
      <li><strong>Itemized add-ons</strong> — anything not included (debris removal, drywall touch-up, aesthetic options) priced separately, not hidden</li>
    </ul>
  </div>
</section>

<section>
  <h2>How to compare two quotes side by side</h2>
  <div class="prose-wide">
    <p>The trap is comparing the bottom-line numbers. Compare scope first, numbers second.</p>
    <ol>
      <li><strong>Same scenario?</strong> Make sure both contractors are quoting the same foundation work. A $1,400 basement quote and a $3,200 crawlspace quote aren't comparable.</li>
      <li><strong>Same number of suction points?</strong> If one quote has one and the other has two, the work is genuinely different.</li>
      <li><strong>Same fan?</strong> An RP145 and a GP500 are sized for different soil types. A contractor specifying a smaller fan may be optimizing for cost; a contractor specifying a larger one may be planning for tight soil.</li>
      <li><strong>Same exhaust?</strong> Above the roof costs more than exterior wall above the eave. Both can be code-compliant; one may be more aesthetic.</li>
      <li><strong>Same post-mit test?</strong> A contractor who skips this is the cheaper bid for a reason.</li>
      <li><strong>Same warranty?</strong> 1-year vs 5-year workmanship matters.</li>
    </ol>
    <p>If one quote is significantly higher after all of that lines up, ask the contractor what they're doing differently. There's usually an honest answer — multiple suction points after a diagnostic test, a heavier vapor barrier in a crawlspace, an interior routing aesthetic upgrade — or there isn't, and you have your decision.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — three quotes for the same finished walk-out basement</strong>
    <p>A homeowner gets three Colorado mitigation quotes: $1,950, $2,800, and $4,200. The lowest doesn't include a post-mitigation test or drywall touch-up. The middle one is a clean interior routing job with both. The highest is from a contractor who ran a sub-slab communication test first and found the soil was tight enough that two suction points are needed. <em>All three can be honest quotes.</em> The right one depends on what the homeowner actually wants to pay for: the cheapest install, the cleanest finished product, or the most thorough diagnostic. A second short-term test after mitigation will tell you whether the system worked — regardless of which quote was chosen.</p>
  </div>
</section>

<section>
  <h2>When you should expect more than CDPHE's baseline</h2>
  <div class="prose-wide">
    <p>The $1,000–$2,000 figure is for a standard single-family install. Plan for the higher end (or above) if any of these apply to your home:</p>
    <ul>
      <li>Crawlspace (full or partial) under any portion of the home</li>
      <li>Tri-level, split-level, or addition that created a multi-zone foundation</li>
      <li>Finished basement where pipe must run inside</li>
      <li>Sump pit needs full sealing and a new lid</li>
      <li>Soil is tight clay (more common in some Front Range subdivisions)</li>
      <li>Electrical panel is at capacity (a sub-panel adds cost)</li>
    </ul>
    <p>Plan for the lower end if your home is a single-zone basement on porous gravel, you already have a passive radon rough-in from new construction, and you don't need interior routing.</p>
  </div>
</section>

<section>
  <h2>About DIY mitigation</h2>
  <div class="prose-wide">
    <div class="callout">
      <strong>It's not recommended — and in Colorado, contractor licensing is real.</strong>
      <p>A correctly designed system depressurizes the entire sub-slab, exhausts above the roof per <a href="{s('aarst_standards')}" rel="noopener" target="_blank">AARST standards</a>, accounts for back-drafting and combustion safety, and is verified with a post-install test. CDPHE specifically warns that sealing cracks alone is unreliable and can sometimes make levels worse.<sup><a href="#src-1">[1]</a></sup> Colorado also requires DORA licensure for anyone performing mitigation work for hire.<sup><a href="#src-4">[4]</a></sup> If budget is the constraint, see CDPHE's <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">low-income mitigation assistance program</a>.</p>
    </div>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-3">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
    <li id="src-4">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-5">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def cost_co_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How much does radon mitigation cost in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "CDPHE's published range for a typical Colorado single-family mitigation system is $1,000–$2,000. Real-world Colorado Springs market data spans roughly $900–$4,800 depending on foundation type: basic basement $900–$1,900, finished basement $1,400–$2,800, crawlspace $1,800–$4,000, and multi-zone foundation $2,200–$4,800."}},
            {"@type": "Question", "name": "Why do radon mitigation quotes vary so much in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Quotes vary because scope varies: foundation type, suction point count, fan sizing (Colorado's altitude requires more powerful fans), sealing scope, pipe routing, and whether a post-mitigation test and permits are included. Always compare scope before comparing prices."}},
            {"@type": "Question", "name": "Is DIY radon mitigation legal in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Colorado requires anyone performing radon mitigation work for hire to hold a license from the DORA Office of Radon Professionals. Homeowners can technically install on their own home, but doing so without AARST standards expertise commonly results in systems that don't reduce radon below the action level — and CDPHE warns that sealing cracks alone can sometimes make levels worse."}},
            {"@type": "Question", "name": "What does it cost to run a radon mitigation system in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Less than $10 per month in electricity for the fan, per EPA estimates. A name-brand radon fan typically lasts 5+ years; replacement runs $150–$400 in parts plus labor."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 2. /colorado-springs/radon-mitigation-cost/   — CS REFRESH (replaces V1)
# =========================================================================
CS_COST_BODY_V2 = f"""
<section>
  <div class="prose-wide">
    <p>If you're testing in Colorado Springs and starting to think about cost, here's the honest range. A typical Colorado Springs mitigation system lands between <strong>$900 and $1,900</strong> for a straightforward basement install — which lines up with <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a>'s $1,000–$2,000 baseline.<sup><a href="#src-1">[1]</a></sup> Crawlspaces, finished basements, and multi-zone foundations push higher, sometimes well above $3,000.</p>
    <p>This page walks through the four scenarios that cover almost every Colorado Springs home, what's actually driving the price in each one, and what to look for in a written quote. We'll also flag the things that make Colorado Springs different from a national average — your altitude affects your fan, your foundation type may not match the national baseline, and Colorado's contractor licensing is real and verifiable.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">CS basic basement</div>
      <div class="stat">$900–$1,900</div>
      <div class="source">Median around $1,400. Single suction point, exterior routing</div>
    </div>
    <div class="factbox">
      <div class="label">CS crawlspace</div>
      <div class="stat">$1,800–$4,000</div>
      <div class="source">Median around $2,600. Sub-membrane system, heavier labor</div>
    </div>
    <div class="factbox">
      <div class="label">El Paso County</div>
      <div class="stat">40%+</div>
      <div class="source">homes tested 2005–2023 had elevated radon. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">EPCPH</a></div>
    </div>
    <div class="factbox">
      <div class="label">EPA action level</div>
      <div class="stat">4.0 pCi/L</div>
      <div class="source">Mitigate at or above. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
  </div>
</section>

<section>
  <h2>Why Colorado Springs is on the higher-risk side of Colorado</h2>
  <div class="prose-wide">
    <p>Colorado is entirely classified as <strong>EPA Zone 1</strong>, meaning every county is predicted to have an indoor average above 4.0 pCi/L.<sup><a href="#src-2">[2]</a></sup> El Paso County is among the highest-risk counties in that high-risk state: county public health data shows that more than <strong>40% of homes tested between 2005 and 2023 came back elevated</strong>.<sup><a href="#src-3">[3]</a></sup> The reason is in the rock under your feet — Pikes Peak granite is uranium-bearing, and uranium decay is where indoor radon comes from. That doesn't change the install price directly, but it does mean Colorado Springs homes tend to start higher and may need slightly more robust systems to bring levels down to safe ranges.</p>
  </div>
</section>

<section>
  <h2>Cost by scenario — Colorado Springs market data</h2>
  <div class="prose-wide">
    <p>These ranges are compiled from CDPHE, El Paso County Public Health, Angi, CostWhale, ProMatcher, InspectAndTest, and Colorado Springs contractor public pricing, 2024–2026. Use them to orient an estimate — not to argue with a contractor before they've seen your home.</p>
  </div>

  <h3>Scenario A — Basic basement</h3>
  <div class="prose-wide">
    <p><strong>$900–$1,900</strong> in Colorado Springs (median around $1,400).</p>
    <p>One suction point through the slab, sealed pit, 4" PVC up an exterior wall to a roof exhaust, name-brand inline fan (often a RadonAway RP145 for porous gravel), manometer at the suction point, post-mitigation test included. This is the most common Colorado Springs install — single-story or two-story home over an unfinished or partially finished basement.</p>
    <p>What drives the price: soil porosity (loose gravel is cheaper; clay is harder), pipe routing distance, fan location (attic versus exterior wall), and electrical access. A passive radon rough-in from new construction can pull this scenario well below $1,200.</p>
  </div>

  <h3>Scenario B — Finished basement</h3>
  <div class="prose-wide">
    <p><strong>$1,400–$2,800</strong> in Colorado Springs (median around $1,900).</p>
    <p>Same core sub-slab design as Scenario A, but the pipe has to navigate around drywall, closets, drop ceilings, or finished utility space. Some installs need minor drywall cut-and-patch; some get routed through a mechanical room to minimize disruption. Aesthetic options like paint match, decorative pipe boxing, or exterior alternate routing add $200–$600.</p>
    <p>What drives the price: how much finished surface needs to be protected or restored, ceiling height clearance, and HVAC interference. The contractor should walk the basement with you before quoting and explain exactly where the pipe will run.</p>
  </div>

  <h3>Scenario C — Crawlspace</h3>
  <div class="prose-wide">
    <p><strong>$1,800–$4,000</strong> in Colorado Springs (median around $2,600).</p>
    <p>A heavy vapor barrier laid across the entire crawlspace floor, sealed perimeter-to-perimeter, with lap seams sealed, penetrations sealed, and the barrier attached to footings. Suction is pulled from underneath. The labor is harder (low headroom, debris removal, footing complexity) and the materials are more expensive.</p>
    <p>What drives the price: crawlspace headroom (lower = harder labor), total area, debris and moisture in the space, existing partial encapsulation, and the thickness of the vapor barrier. Older 6-mil barriers are no longer the recommended minimum — newer crawlspace installs commonly use 10–20 mil for durability. If your quote calls for 6-mil for a permanent system, ask why.</p>
  </div>

  <h3>Scenario D — Multi-zone foundation</h3>
  <div class="prose-wide">
    <p><strong>$2,200–$4,800</strong> in Colorado Springs (median around $3,200).</p>
    <p>Common in tri-level homes, split-levels, homes with additions, and homes with both a basement and a crawlspace under different parts of the footprint. Multiple suction points, sometimes multiple fans, and a diagnostic test (called pressure field extension, or PFE) should happen before the quote is finalized.</p>
    <p>What drives the price: number of foundation zones, total square footage, soil conditions that may differ across the home, and number of fans needed. A contractor who quotes a multi-zone home like a Scenario A job — without diagnostics — is the contractor most likely to undersize the system. Ask whether they'll run a PFE before installing.</p>
  </div>
</section>

<section>
  <h2>Add-ons that should be priced separately</h2>
  <div class="prose-wide">
    <p>An honest quote breaks these out instead of burying them.</p>
    <table class="compact">
      <thead>
        <tr><th>Add-on</th><th>Typical Colorado Springs cost</th></tr>
      </thead>
      <tbody>
        <tr><td>Electrical sub-panel work (if needed for fan circuit)</td><td>$150–$400</td></tr>
        <tr><td>Independent (third-party) post-mitigation test</td><td>$125–$200</td></tr>
        <tr><td>Decorative exterior paint match</td><td>$50–$150</td></tr>
        <tr><td>Pipe boxing or framing for finished-basement aesthetics</td><td>$150–$400</td></tr>
        <tr><td>Drywall restoration and paint (finished basement)</td><td>$200–$600</td></tr>
        <tr><td>Crawlspace debris removal</td><td>$150–$500</td></tr>
        <tr><td>Crawlspace dehumidifier (sometimes bundled with crawlspace mitigation)</td><td>$800–$1,500</td></tr>
        <tr><td>Replacement fan (5+ year fan lifespan)</td><td>$150–$400 plus labor</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>What a fair Colorado Springs quote looks like</h2>
  <div class="prose-wide">
    <p>A complete written quote has these items called out. If yours is missing one, ask before signing.</p>
    <ul class="checklist">
      <li>Contractor's <strong>DORA license number</strong> for radon mitigation, plus NRPP or NRSB certification number<sup><a href="#src-4">[4]</a></sup></li>
      <li>Number of <strong>suction points</strong> and where they'll go</li>
      <li>Specific <strong>fan model</strong> (RP145, GP500, HS-series, etc.) and 5-year warranty</li>
      <li>Where the <strong>pipe exits</strong> (interior, exterior, above roof or above eave)</li>
      <li><strong>Sealing</strong> scope — slab cracks, sump cover, floor-wall joint, plumbing penetrations</li>
      <li><strong>Manometer</strong> install at the suction point, accessible and visible</li>
      <li><strong>Permits</strong> — electrical permit handled by the contractor (Pikes Peak Regional Building Department covers most of El Paso County)<sup><a href="#src-5">[5]</a></sup></li>
      <li><strong>Post-mitigation test</strong> — within 30 days of install, 2–7 day duration, closed-house conditions</li>
      <li><strong>Workmanship warranty</strong> — 1–2 year labor warranty separate from the fan warranty</li>
    </ul>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a Briargate homeowner gets two quotes</strong>
    <p>Same single-story home over a partially-finished basement. Contractor A quotes $1,250 for a single-point exterior install with a 1-year workmanship warranty and no post-mitigation test. Contractor B quotes $1,800 with the same scope plus a 5-year workmanship warranty and a 48-hour post-mitigation test included. The $550 difference covers the verification step that proves the system actually brought radon below 4.0 pCi/L. Most Colorado Springs homeowners in this position pay the extra for the post-mit test — it's the only way to know the job worked.</p>
  </div>
</section>

<section>
  <h2>Testing costs are separate</h2>
  <div class="prose-wide">
    <p>Mitigation quotes don't include the initial test. Your options in Colorado Springs:</p>
    <ul>
      <li><strong>El Paso County Public Health Lab</strong> kits: $15 short-term, $42 long-term (1675 W. Garden of the Gods Rd; 719-578-3199 option 3)<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Retail short-term kits</strong>: $15–$40 from Home Depot, Lowe's, Ace, or Amazon</li>
      <li><strong>Professional measurement</strong>: $150–$300 for a continuous monitor placed by a DORA-licensed tester (used for real estate transactions)</li>
    </ul>
    <p>Full detail on which test to use when: <a href="/colorado-springs/radon-testing/">radon testing in Colorado Springs</a>.</p>
  </div>
</section>

<section>
  <h2>Ongoing operating cost</h2>
  <div class="prose-wide">
    <p>A typical radon fan draws 50–90 watts. At Colorado Springs electricity rates, that's roughly <strong>$5–$10 per month</strong> in electricity — EPA pegs it at under $10/mo for a typical system.<sup><a href="#src-6">[6]</a></sup> The fan is the only maintenance item; manufacturers rate them for 5+ years, and replacement runs $150–$400 in parts plus labor.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">U.S. EPA. <em>EPA Map of Radon Zones</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-3">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-4">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-5">Pikes Peak Regional Building Department. <a href="{s('pprbd')}" rel="noopener" target="_blank">pprbd.org</a></li>
    <li id="src-6">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def cs_cost_faq_jsonld_v2():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How much does radon mitigation cost in Colorado Springs?",
             "acceptedAnswer": {"@type": "Answer", "text": "A typical Colorado Springs basement mitigation runs $900–$1,900 (median around $1,400), which lines up with CDPHE's $1,000–$2,000 baseline. Finished basements run $1,400–$2,800, crawlspaces $1,800–$4,000, and multi-zone foundations $2,200–$4,800."}},
            {"@type": "Question", "name": "Why is my Colorado Springs mitigation quote higher than the national average?",
             "acceptedAnswer": {"@type": "Answer", "text": "Colorado Springs is at roughly 6,000 feet of elevation, and radon fans lose about 4% of their airflow capacity per 1,000 feet of altitude. That sometimes requires a larger fan or a second suction point. El Paso County also has higher baseline radon, which can require a more robust system."}},
            {"@type": "Question", "name": "Is the cheapest Colorado Springs radon mitigation quote always a bad sign?",
             "acceptedAnswer": {"@type": "Answer", "text": "No, but check the scope. A low quote may be perfectly fair if it's a basic single-suction-point exterior install on porous gravel. It becomes a red flag when it's missing a post-mitigation test, a written warranty, the contractor's DORA license number, or a specified fan model."}},
            {"@type": "Question", "name": "How long does mitigation installation take in Colorado Springs?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most Colorado Springs single-family installs take one day on site. End-to-end (quote, scheduling, install, post-mitigation test) is typically one to two weeks. Real estate timelines can compress this further — see our real-estate deadline cost page."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 3. /radon-mitigation-cost/quote-variation/   — WHY QUOTES VARY
# =========================================================================
COST_VARIATION_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Two Colorado mitigation contractors come look at the same house. One quotes $1,500. The other quotes $4,200. You're standing there reading the two emails and wondering how that's even possible.</p>
    <p>It usually is possible, and the answer is usually scope, not greed. This page walks through the real reasons radon mitigation quotes vary in Colorado — and the few cases where the spread is actually a red flag.</p>
  </div>
</section>

<section>
  <h2>The five real cost drivers</h2>
  <div class="prose-wide">

    <h3>1. Foundation type</h3>
    <p>This is the biggest driver. A simple basement install runs $900–$1,900 in Colorado Springs. A crawlspace can hit $4,000 because of the heavy vapor barrier and the labor of sealing it. Multi-zone homes (tri-level, split-level, basement-plus-crawlspace) can push past $4,800.<sup><a href="#src-1">[1]</a></sup> If one contractor priced a basement and the other priced a crawlspace, the quotes aren't comparable — even if they're for the same address.</p>

    <h3>2. Suction point count</h3>
    <p>One suction point is the most common. Multiple suction points are needed when the home has multiple foundation zones, or when a diagnostic test (pressure field extension, or PFE) shows the soil under the slab doesn't communicate well from one corner to the other. Each additional point adds labor, materials, and sometimes a second fan.</p>

    <h3>3. Fan sizing — and Colorado's altitude correction</h3>
    <p>This is where Colorado is genuinely different from a national average. Radon fans lose roughly <strong>4% of their airflow capacity for every 1,000 feet of elevation</strong>.<sup><a href="#src-2">[2]</a></sup> Colorado Springs sits at roughly 6,000 feet — meaning a fan that's perfectly sized for a sea-level install is significantly underpowered here. A contractor working off the national catalog spec without adjusting for altitude can quote less but install a system that doesn't bring your radon below 4.0 pCi/L. A contractor who specifies a larger fan or a second suction point isn't padding the quote — they're compensating for the altitude.</p>

    <h3>4. Sealing scope</h3>
    <p>Two contractors can both "seal the basement" and mean very different things. Slab cracks, sump pit lid, floor-wall joint, plumbing penetrations, sub-slab membrane in a crawlspace — each is a separate scope item. A quote that lists what's being sealed is more credible than one that just says "sealing included."</p>

    <h3>5. Pipe routing</h3>
    <p>Exterior routing (fan on the outside wall, pipe up the side of the house above the eave) is faster and cheaper than full interior routing (pipe through closets, the attic, and out the roof). Both can be AARST-compliant.<sup><a href="#src-3">[3]</a></sup> Interior routing costs more for a reason — it looks cleaner from the outside and protects the pipe from weather and damage.</p>
  </div>
</section>

<section>
  <h2>The diagnostic step that should happen first</h2>
  <div class="prose-wide">
    <p>Before quoting a tight-soil or multi-zone home, a quality Colorado contractor will run a <strong>pressure field extension (PFE) test</strong> — drilling a small test hole through the slab, applying suction, and measuring how well the vacuum spreads through the sub-slab. If the field extends well, one suction point will work; if it doesn't, two or three may be needed.</p>
    <p>Contractors who skip this step on a complex home are the contractors most likely to install a system that doesn't bring radon below the action level. If your home is anything other than a simple single-zone basement and your quote doesn't mention diagnostics, ask.</p>
  </div>
</section>

<section>
  <h2>Markup differences vs work differences</h2>
  <div class="prose-wide">
    <p>Sometimes the spread between quotes is real markup, not real scope. A handful of honest reasons for markup:</p>
    <ul>
      <li><strong>Established contractor with overhead</strong> — full-time staff, marketing, insurance, warranty reserves. Their per-job overhead is higher; their failure rate is also typically lower.</li>
      <li><strong>Premium fan model and longer warranty</strong> — a 7-year manufacturer warranty costs more than a 5-year.</li>
      <li><strong>Same-day or guaranteed-completion scheduling</strong> — real estate deadline pressure usually carries a small premium.</li>
      <li><strong>Better aesthetic finishing</strong> — paint match, pipe boxing, exterior alternative routing.</li>
    </ul>
    <p>And the reasons that aren't fair:</p>
    <ul>
      <li>Quote doesn't list scope at all — just a price.</li>
      <li>"Required" upgrades that the contractor can't explain technically.</li>
      <li>Fear-based sales language ("your family is in danger if you don't act today").</li>
      <li>Refusal to put the post-mitigation test result threshold in writing.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The apples-to-apples comparison checklist</h2>
  <div class="prose-wide">
    <p>When you have two quotes that look genuinely different, run them through this filter:</p>
    <table class="compact">
      <thead>
        <tr><th>Compare</th><th>What you're checking</th></tr>
      </thead>
      <tbody>
        <tr><td>Foundation work</td><td>Same scope, same zones</td></tr>
        <tr><td>Suction point count</td><td>Same number, same locations</td></tr>
        <tr><td>Fan model</td><td>Both correctly sized for Colorado altitude</td></tr>
        <tr><td>Sealing scope</td><td>Same items called out</td></tr>
        <tr><td>Pipe routing</td><td>Interior vs exterior matches</td></tr>
        <tr><td>Exhaust point</td><td>Above roof vs above eave</td></tr>
        <tr><td>Manometer install</td><td>Included and accessible in both</td></tr>
        <tr><td>Permits</td><td>Same contractor responsibility</td></tr>
        <tr><td>Post-mitigation test</td><td>Included, with target pCi/L written</td></tr>
        <tr><td>Workmanship warranty</td><td>Same length</td></tr>
        <tr><td>DORA license + NRPP/NRSB</td><td>Both provided<sup><a href="#src-4">[4]</a></sup></td></tr>
      </tbody>
    </table>
    <p>If all of those line up and one quote is still significantly higher, ask why. There's usually a defensible answer — or there isn't.</p>
  </div>
</section>

<section>
  <h2>When the cheap quote is the right quote</h2>
  <div class="prose-wide">
    <p>The cheaper quote is often the better choice when:</p>
    <ul>
      <li>The home is a simple single-zone basement with porous gravel soil</li>
      <li>The home already has a passive radon rough-in from new construction (post-2009 builds often do)</li>
      <li>The roof line favors exterior routing and the homeowner doesn't care about the aesthetic of an exterior pipe</li>
      <li>The contractor is established, licensed, and has 5+ year warranty on the fan</li>
    </ul>
    <p>And when the cheap quote is the wrong call:</p>
    <ul>
      <li>The home is multi-zone or has a crawlspace and the cheap quote treats it as Scenario A</li>
      <li>The cheap quote omits the post-mitigation test</li>
      <li>No DORA license number or NRPP/NRSB certification on file</li>
      <li>The contractor can't or won't put scope details in writing</li>
    </ul>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — same home, different scope</strong>
    <p>A homeowner with a 2,400 sq ft tri-level home gets three Colorado quotes. The lowest ($1,300) treats it like a single-zone basement — one suction point, one fan. The middle ($2,900) includes a PFE diagnostic and proposes two suction points. The highest ($4,400) proposes the same two suction points plus a sub-membrane system for the small crawlspace under the garage extension. The lowest quote is technically possible to install — but the homeowner's post-mitigation test will likely come back above 4.0 pCi/L because tri-levels are multi-zone homes. The middle quote is probably the right one. The highest may be over-scoping the garage crawlspace if it's outside conditioned space.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
    <li id="src-3">ANSI/AARST. <em>SGM-SF-2023 Soil Gas Mitigation Standards</em>. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
    <li id="src-4">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
  </ol>
</aside>
"""


def cost_variation_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Why do radon mitigation quotes vary so much for the same house?",
             "acceptedAnswer": {"@type": "Answer", "text": "The five main drivers are foundation type, number of suction points, fan sizing (Colorado altitude affects this), sealing scope, and pipe routing. A $1,500 quote and a $4,200 quote can both be honest if the scopes are genuinely different — a contractor who ran a pressure field extension diagnostic may propose two suction points where another proposed one."}},
            {"@type": "Question", "name": "Does Colorado's altitude really affect radon fan choice?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Radon fans lose roughly 4% of their airflow capacity per 1,000 feet of elevation. Colorado Springs at 6,000 feet requires fans sized larger than a national catalog spec would suggest. Contractors who don't adjust for altitude can install systems that don't bring radon below the EPA action level."}},
            {"@type": "Question", "name": "What is a pressure field extension test and do I need one?",
             "acceptedAnswer": {"@type": "Answer", "text": "A pressure field extension (PFE) test measures how well vacuum applied to one point under the slab spreads through the sub-slab soil. It tells the contractor whether one suction point is enough or whether two or more are needed. Quality contractors run a PFE on any multi-zone home, tight-soil home, or home larger than a simple single-foundation footprint."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 4. /radon-mitigation-cost/quote-too-high/   — IS MY QUOTE TOO HIGH
# =========================================================================
COST_TOO_HIGH_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You got a quote for $4,500 and your gut says it's too much. Or maybe a quote for $1,200 that feels too cheap. Either way, you want to know whether the price is fair before you sign.</p>
    <p>The short answer: a Colorado mitigation quote that lines up with the right scenario, lists scope in writing, and comes from a DORA-licensed contractor is almost certainly fair — even if it feels high.<sup><a href="#src-1">[1]</a></sup> Most "too high" quotes turn out to be reasonable when you check what's actually in them. Here's how to run the check.</p>
  </div>
</section>

<section>
  <h2>The short test</h2>
  <div class="prose-wide">
    <p>Match your home to the right scenario. If your quote falls inside that band, it's probably fair.</p>
    <table class="compact">
      <thead>
        <tr><th>Your home</th><th>Fair Colorado Springs range</th><th>Median</th></tr>
      </thead>
      <tbody>
        <tr><td>Basic basement, single suction point</td><td>$900–$1,900</td><td>$1,400</td></tr>
        <tr><td>Finished basement, interior routing</td><td>$1,400–$2,800</td><td>$1,900</td></tr>
        <tr><td>Crawlspace, sub-membrane system</td><td>$1,800–$4,000</td><td>$2,600</td></tr>
        <tr><td>Multi-zone (tri-level, basement + crawlspace)</td><td>$2,200–$4,800</td><td>$3,200</td></tr>
      </tbody>
    </table>
    <p>If your quote is significantly above the high end of your scenario, ask what's driving it. If it's below the low end, ask what's missing.</p>
  </div>
</section>

<section>
  <h2>Why "too high" usually isn't greed</h2>
  <div class="prose-wide">
    <p>Most quotes that feel too high turn out to be honest. Common drivers:</p>
    <ul>
      <li><strong>Diagnostic test found tight soil or poor sub-slab communication.</strong> A second suction point adds $300–$700 in materials and labor.</li>
      <li><strong>Larger fan is needed.</strong> A GP500 or HS-series fan costs more than an RP145. Colorado altitude correction can push a contractor to spec up.<sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>Crawlspace work was hidden in your basement.</strong> Some homes have a partial crawlspace under a single room (often a kitchen addition). If a contractor noticed and is including it, that's a feature, not padding.</li>
      <li><strong>Interior routing through finished space.</strong> An extra $200–$600 on top of a basic install.</li>
      <li><strong>Heavier vapor barrier in a crawlspace.</strong> 10–20 mil costs more than the old 6-mil minimum.</li>
      <li><strong>Real estate deadline scheduling.</strong> Same-day or guaranteed-by-closing service carries a small premium.</li>
    </ul>
  </div>
</section>

<section>
  <h2>When "too high" really is too high</h2>
  <div class="prose-wide">
    <p>A few red flags that should make you pause:</p>
    <ul>
      <li>The quote is a flat number with no written scope description.</li>
      <li>The contractor can't or won't provide a DORA license number or NRPP/NRSB certification.<sup><a href="#src-1">[1]</a></sup></li>
      <li>The quote includes "required upgrades" that the contractor can't explain technically.</li>
      <li>The contractor uses fear-based language ("urgent," "danger to your family," "act today for this price").</li>
      <li>The post-mitigation test isn't included.</li>
      <li>The warranty is shorter than 1 year on workmanship or 5 years on the fan.</li>
      <li>Cash-only or no written quote at all.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The sanity-check tree</h2>
  <div class="prose-wide">

    <h3>Step 1 — Match your scenario</h3>
    <p>Look at the table above. Which scenario describes your home? If your quote is inside that band, skip to step 4. If it's above, keep going.</p>

    <h3>Step 2 — Read the written scope</h3>
    <p>What's the contractor proposing? Single suction point or multiple? Interior or exterior routing? Heavy vapor barrier in a crawlspace? Each of those moves the price.</p>

    <h3>Step 3 — Ask the question</h3>
    <p>Email or call the contractor and ask: "I'm comparing this quote to a baseline of [your scenario's band]. What's pushing this above the range?" A legitimate contractor will explain — usually it comes back to soil, suction points, fan sizing, or scope you hadn't considered.</p>

    <h3>Step 4 — Get a second quote on the same scope</h3>
    <p>The strongest sanity check is a second written quote with the same scope. Send the second contractor the first quote's scope summary and ask them to price the same work. If the prices come in close, your original quote was fair. If the second comes in much lower, ask the first contractor to explain the difference.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a $4,500 quote that turned out to be fair</strong>
    <p>A homeowner with a finished walk-out basement plus a small crawlspace under the laundry room got a $4,500 quote and called for a second opinion. The second contractor came out, ran a pressure field extension test, and confirmed the soil communication was poor. Both contractors ended up proposing two suction points plus a sub-membrane system for the laundry crawlspace. The second quote came in at $4,300. The $200 spread was warranty length and fan model. The original $4,500 quote was fair — it just looked high because the homeowner had been mentally anchored to the $1,000–$2,000 CDPHE baseline, which doesn't apply to multi-zone homes.</p>
  </div>
</section>

<section>
  <h2>What "too low" should make you ask</h2>
  <div class="prose-wide">
    <p>A quote significantly below the band for your scenario isn't automatically a problem — but it's worth asking what's not included. Common reasons a quote runs low:</p>
    <ul>
      <li>Passive radon rough-in from new construction (saves real money)</li>
      <li>Simple porous-gravel soil that doesn't need a larger fan</li>
      <li>Exterior routing favored over interior</li>
      <li>No finished surfaces to protect</li>
    </ul>
    <p>And the reasons that should give you pause:</p>
    <ul>
      <li>Post-mitigation test not included</li>
      <li>No written workmanship warranty</li>
      <li>No DORA license number on the quote</li>
      <li>"Cash discount" pricing with no written scope</li>
      <li>Contractor is willing to skip the electrical permit to save you money (don't)</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-2">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
  </ol>
</aside>
"""


def cost_too_high_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How do I know if my radon mitigation quote is fair?",
             "acceptedAnswer": {"@type": "Answer", "text": "Match your home to the right scenario: basic basement $900–$1,900, finished basement $1,400–$2,800, crawlspace $1,800–$4,000, multi-zone $2,200–$4,800. If your quote falls inside that band and lists scope in writing, it's almost certainly fair. If it's outside the band, ask the contractor what's pushing it up or down."}},
            {"@type": "Question", "name": "What are the red flags in a high radon mitigation quote?",
             "acceptedAnswer": {"@type": "Answer", "text": "Vague scope, no DORA license or NRPP/NRSB certification provided, fear-based sales pressure, 'required upgrades' the contractor can't explain technically, missing post-mitigation test, and warranties shorter than 1 year on workmanship or 5 years on the fan."}},
            {"@type": "Question", "name": "Should I trust a really cheap radon quote?",
             "acceptedAnswer": {"@type": "Answer", "text": "Sometimes — a basic basement with a passive rough-in and porous gravel soil can legitimately come in under $1,000. But ask what's not included: post-mitigation test, written warranty, DORA license number, and electrical permit responsibility are all things cheap quotes often omit."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 5. /radon-mitigation-cost/whats-in-a-quote/   — WHAT'S IN A QUOTE
# =========================================================================
COST_INCLUDES_BODY = f"""
<section>
  <div class="prose-wide">
    <p>A radon mitigation quote should read like a contract, not a sticky note. The price means very little without the scope behind it. This page is the line-by-line checklist of what a complete Colorado mitigation quote includes — what to look for, what to ask about, and what to walk away from.</p>
  </div>
</section>

<section>
  <h2>The 14-item checklist</h2>
  <div class="prose-wide">
    <p>Every honest Colorado mitigation quote covers each of these. Print this page if it helps — or screenshot it and compare line by line against the quote in your email.</p>
    <ul class="checklist">
      <li><strong>1. Contractor's full legal business name and address.</strong> Not just a logo.</li>
      <li><strong>2. DORA radon mitigation license number.</strong> Required for any contractor performing mitigation in Colorado.<sup><a href="#src-1">[1]</a></sup> Verifiable at the <a href="{s('dora_lookup')}" rel="noopener" target="_blank">DORA license lookup</a>.</li>
      <li><strong>3. NRPP or NRSB certification number.</strong> National professional credential, verifiable at <a href="{s('nrpp_search')}" rel="noopener" target="_blank">nrpp.info</a> or <a href="{s('nrsb_search')}" rel="noopener" target="_blank">nrsb.org</a>.<sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>4. Number and location of suction points.</strong> If your home is multi-zone, "diagnostic test to be performed before install" is the right answer.</li>
      <li><strong>5. Specific fan model.</strong> RadonAway RP145, GP500, HS-series, Fantech, or equivalent. Not "an inline fan."</li>
      <li><strong>6. Fan warranty length.</strong> Typically 5 years on a name-brand fan. EPA notes most manufacturer warranties don't exceed five years.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>7. Pipe size and routing.</strong> 3-inch or 4-inch Schedule 40 PVC, interior or exterior, where it exits the home, and how high above the roofline or eave.</li>
      <li><strong>8. Sealing scope.</strong> Slab cracks, sump pit cover, floor-wall joint, plumbing penetrations — each itemized.</li>
      <li><strong>9. Manometer install.</strong> Where it goes, and that it's accessible and visible from a normal walking path.</li>
      <li><strong>10. Permit responsibility.</strong> Pikes Peak Regional Building Department covers most of El Paso County and requires permits for the electrical work.<sup><a href="#src-4">[4]</a></sup> The contractor should pull it.</li>
      <li><strong>11. Post-mitigation test.</strong> Within 30 days of install, no sooner than 24 hours after the fan is running, 2–7 day duration, closed-house conditions.<sup><a href="#src-3">[3]</a></sup> The quote should specify the target — a result below 4.0 pCi/L is the standard.</li>
      <li><strong>12. Workmanship warranty.</strong> Typically 1–2 years on labor, separate from the fan warranty.</li>
      <li><strong>13. Itemized add-ons.</strong> Electrical sub-panel work, drywall repair, aesthetic options, debris removal — each priced separately, not buried.</li>
      <li><strong>14. Total price with tax and payment terms.</strong> Including deposit, balance due timing, and acceptable payment methods.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Required-by-Colorado items</h2>
  <div class="prose-wide">
    <p>A few items are specifically required by Colorado regulation, not just industry best practice:</p>
    <ul>
      <li><strong>DORA license.</strong> Colorado requires anyone performing radon mitigation for hire to be licensed by the DORA Office of Radon Professionals.<sup><a href="#src-1">[1]</a></sup> No exceptions for "handyman" work.</li>
      <li><strong>Electrical permit.</strong> Radon fan installation involves electrical work — running a dedicated circuit if needed. Pikes Peak Regional Building Department requires electrical permits for this work in most jurisdictions they cover.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>Real estate disclosure.</strong> If you install mitigation on a home you later sell, Colorado SB23-206 (CRS § 38-35.7-112) requires you to disclose the system to buyers along with prior test results and the CDPHE radon brochure.<sup><a href="#src-5">[5]</a></sup> Keep the install documentation in a safe place.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Items often hidden in fine print</h2>
  <div class="prose-wide">
    <p>Watch for these — they're not always called out clearly:</p>
    <ul>
      <li><strong>Post-mitigation test fee.</strong> Sometimes priced as a separate $125–$200 line item rather than included.</li>
      <li><strong>Electrical sub-panel work.</strong> If your panel is full, the contractor may need to install a sub-panel ($150–$400+). This should be a line item, not a surprise.</li>
      <li><strong>Drywall touch-up after interior routing.</strong> Some contractors patch but don't paint. Some don't patch at all.</li>
      <li><strong>Crawlspace debris removal.</strong> If they have to clear the crawlspace before installing the barrier, that's labor — $150–$500.</li>
      <li><strong>Replacement fan after warranty.</strong> Not part of the original quote, but worth understanding: replacement fans run $150–$400 in parts plus labor every 5+ years.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Warranty language to look for</h2>
  <div class="prose-wide">
    <p>Two warranties matter, and they're separate:</p>
    <ol>
      <li><strong>Workmanship warranty</strong> — how long the contractor stands behind the install. 1–2 years is standard; some Colorado contractors offer 5 years.</li>
      <li><strong>Fan manufacturer warranty</strong> — typically 5 years on a name-brand fan (RadonAway, Fantech, Festa). EPA notes these warranties rarely exceed 5 years.<sup><a href="#src-3">[3]</a></sup></li>
    </ol>
    <p>Beyond those two, look for a written statement that the system will reduce radon below 4.0 pCi/L as verified by the post-mitigation test, and a path forward if it doesn't (additional suction point added at no charge, etc.).</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — what a complete quote looks like in your inbox</strong>
    <p>The contractor's email lists: business name and DORA license number, NRPP certification number, one suction point in the southwest corner of the basement, a RadonAway RP145 fan with 5-year warranty mounted on the exterior north wall, 4-inch Schedule 40 PVC routed up the exterior wall to 12 inches above the roof eave, sealing of two visible slab cracks and the sump pit lid, a manometer mounted at the suction point visible from the basement stairs, electrical permit handled by the contractor, post-mitigation test scheduled within 30 days of install with target below 4.0 pCi/L, 2-year workmanship warranty, total of $1,650 including tax and 50% deposit. That's a complete quote — every item from the checklist accounted for.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-2">National Radon Proficiency Program. <a href="{s('nrpp')}" rel="noopener" target="_blank">nrpp.info</a> · National Radon Safety Board. <a href="{s('nrsb')}" rel="noopener" target="_blank">nrsb.org</a></li>
    <li id="src-3">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-4">Pikes Peak Regional Building Department. <a href="{s('pprbd')}" rel="noopener" target="_blank">pprbd.org</a></li>
    <li id="src-5">Colorado General Assembly. <em>SB23-206</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


def cost_includes_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What should be in a radon mitigation quote?",
             "acceptedAnswer": {"@type": "Answer", "text": "A complete Colorado radon mitigation quote includes the contractor's DORA license number, NRPP or NRSB certification, number and location of suction points, specific fan model and warranty, pipe size and routing, sealing scope, manometer install location, permit responsibility, post-mitigation test, workmanship warranty, itemized add-ons, and total price with payment terms."}},
            {"@type": "Question", "name": "Is a DORA license required for radon mitigation in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Colorado requires anyone performing radon mitigation work for hire to hold a license from the DORA Office of Radon Professionals. The license is verifiable through the state's public licensee lookup."}},
            {"@type": "Question", "name": "What warranty should I expect on a Colorado radon system?",
             "acceptedAnswer": {"@type": "Answer", "text": "Two warranties are standard: a workmanship warranty from the contractor (typically 1–2 years on labor, sometimes 5) and a manufacturer fan warranty (typically 5 years on a name-brand fan). Look for a written statement that the system will reduce radon below 4.0 pCi/L per the post-mitigation test."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 6. /radon-mitigation-cost/crawlspaces/   — CRAWLSPACE COST
# =========================================================================
COST_CRAWLSPACE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Crawlspaces are the foundation type Colorado homeowners worry about most when they look at a radon quote. The short answer: a crawlspace mitigation system in Colorado Springs typically runs <strong>$1,800–$4,000</strong>, with a median around $2,600.<sup><a href="#src-1">[1]</a></sup> That's meaningfully higher than the $900–$1,900 a basic basement system costs — and there are real reasons for the gap.</p>
    <p>This page walks through how crawlspace mitigation actually works, why it costs what it costs, and what to look for in a written crawlspace quote.</p>
  </div>
</section>

<section>
  <h2>Why crawlspaces cost more than basements</h2>
  <div class="prose-wide">
    <p>Three things make crawlspace mitigation more expensive than a comparable basement install:</p>
    <ol>
      <li><strong>Material cost.</strong> A crawlspace mitigation needs a heavy vapor barrier covering the entire floor, sealed at the perimeter, lapped and seam-sealed, and attached to footings. That barrier alone is a meaningful material cost; a basement install has no equivalent.</li>
      <li><strong>Labor reality.</strong> A crawlspace is a small, low-headroom space. The installer is often working on knees or stomach. Sealing the perimeter against masonry or concrete footings is detailed work. Debris removal, moisture management, and existing partial encapsulation all add labor.</li>
      <li><strong>Diagnostic complexity.</strong> Some crawlspaces have multiple sub-zones (under additions, under bays). Each may need its own suction point under the membrane. Quality contractors often run diagnostic testing before quoting.</li>
    </ol>
  </div>
</section>

<section>
  <h2>What a sub-membrane system actually involves</h2>
  <div class="prose-wide">
    <p>The radon mitigation technique used in crawlspaces is called <strong>sub-membrane depressurization</strong> (sometimes "SMD"). It works the same way as sub-slab depressurization in a basement — applying suction below a barrier so radon-laden soil gas is pulled out before it enters the home — but the barrier is a vapor membrane laid across the dirt floor rather than the concrete slab the basement provides for free.</p>
    <p>A correctly installed crawlspace mitigation system has these elements:</p>
    <ul>
      <li><strong>Heavy vapor barrier</strong> covering the entire crawlspace floor.</li>
      <li><strong>Perimeter seal</strong> attaching the membrane to the foundation walls or footings.</li>
      <li><strong>Lap-and-seam sealing</strong> wherever two pieces of membrane meet.</li>
      <li><strong>Penetration sealing</strong> at plumbing, HVAC, and structural members that pass through the membrane.</li>
      <li><strong>Suction point</strong> drawing air from beneath the membrane, connected to PVC pipe that exits the home and exhausts above the roofline.</li>
      <li><strong>Fan</strong> sized for the crawlspace and Colorado's altitude.</li>
      <li><strong>Manometer</strong> visible from the access hatch or wherever you can see the system from.</li>
      <li><strong>Post-mitigation test</strong> verifying the system brought radon below 4.0 pCi/L per AARST standards.<sup><a href="#src-2">[2]</a></sup></li>
    </ul>
  </div>
</section>

<section>
  <h2>The vapor barrier — and why 6-mil is no longer enough</h2>
  <div class="prose-wide">
    <p>Old AARST standards used 6-mil polyethylene as the minimum vapor barrier thickness. That's still the language some quotes use. The industry has moved toward heavier barriers — typically <strong>10–20 mil</strong> — because they're more puncture-resistant, last longer, and stand up better to the foot traffic of future HVAC or plumbing work in the crawlspace.<sup><a href="#src-2">[2]</a></sup></p>
    <p>If your crawlspace quote calls for 6-mil for a permanent system, ask why. There may be a valid reason (very small space, no foot traffic expected, cost constraint), or the contractor may be using outdated specs. A heavier barrier costs more upfront and saves headaches later.</p>
  </div>
</section>

<section>
  <h2>Labor reality — what makes a crawlspace harder</h2>
  <div class="prose-wide">
    <p>Three crawlspace conditions push the labor cost up:</p>
    <ul>
      <li><strong>Low headroom.</strong> Anything under about 30 inches makes every motion slower. Installers can't sit up; they work on stomachs and elbows.</li>
      <li><strong>Debris and moisture.</strong> Crawlspaces often hold old insulation scraps, construction debris, or ground moisture. Clearing that before laying the membrane is real work.</li>
      <li><strong>Footing complexity.</strong> Sealing the membrane to a clean concrete footing is straightforward. Sealing to stepped or stone footings, post-and-pier supports, or pipes and ducts running close to the wall is detailed work.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Encapsulation vs mitigation — they aren't the same thing</h2>
  <div class="prose-wide">
    <p>Crawlspace <strong>encapsulation</strong> is a moisture and air quality treatment that covers the floor (and often walls) of a crawlspace with a sealed vapor barrier, sometimes paired with a dehumidifier. It can reduce radon, but it isn't designed to.</p>
    <p>Crawlspace <strong>radon mitigation</strong> is a depressurization system that actively pulls soil gas from beneath the barrier. It's verified by a post-mitigation test to confirm radon is below 4.0 pCi/L.</p>
    <p>A crawlspace encapsulation done without active depressurization may lower radon — or may have no effect, depending on how the barrier is sealed and whether there's any path for soil gas to enter above the membrane. A radon mitigation system uses active suction to guarantee the depressurization works.</p>
    <p>If you're considering both, ask the contractor how the two systems interact. Many Colorado contractors bundle them; some price the encapsulation as a separate $800–$1,500 add-on.</p>
  </div>
</section>

<section>
  <h2>Crawlspace cost band — and what drives it</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th>Range</th><th>Typical scope</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>$1,800–$2,400</strong></td><td>Small (under 600 sq ft) crawlspace, dry, decent headroom, simple footings, single suction point</td></tr>
        <tr><td><strong>$2,400–$3,200</strong></td><td>Standard 600–1,200 sq ft crawlspace, some debris removal, single or two suction points</td></tr>
        <tr><td><strong>$3,200–$4,000+</strong></td><td>Large crawlspace, low headroom, complex footings, debris/moisture, multiple suction points, encapsulation bundled</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a Black Forest homeowner with a damp crawlspace</strong>
    <p>An older home in Black Forest has a 900 sq ft crawlspace with low headroom and visible moisture on the dirt floor. The first quote ($2,200) proposes a 6-mil barrier with one suction point. The second quote ($3,400) proposes a 15-mil reinforced barrier, debris removal, perimeter sealing to the footings, two suction points (because the L-shaped crawlspace has poor air communication corner-to-corner), and a small dehumidifier. Both are legitimate; the second is the more durable install for the conditions. The homeowner's call comes down to whether to pay extra now for a system that will hold up longer.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">ANSI/AARST. <em>SGM-SF-2023 Soil Gas Mitigation Standards for Single-Family Buildings</em>. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
  </ol>
</aside>
"""


def cost_crawlspace_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How much does crawlspace radon mitigation cost in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Crawlspace mitigation in Colorado Springs typically runs $1,800–$4,000 (median around $2,600). Small dry crawlspaces with simple footings sit near the low end; large crawlspaces with debris, moisture, or multi-zone layouts can hit the high end or beyond."}},
            {"@type": "Question", "name": "Why is crawlspace mitigation more expensive than basement mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Three reasons: material cost (heavy vapor barrier covering the entire floor, sealed at the perimeter), labor reality (low headroom, debris removal, footing complexity), and diagnostic complexity (crawlspaces often need multiple suction points)."}},
            {"@type": "Question", "name": "What's the difference between crawlspace encapsulation and radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Encapsulation is a moisture treatment using a sealed vapor barrier (sometimes with a dehumidifier). Radon mitigation actively pulls soil gas from beneath a sealed barrier using a fan, and is verified by a post-mitigation test. Encapsulation alone may or may not reduce radon; active mitigation guarantees it via depressurization."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 7. /radon-mitigation-cost/finished-basements/   — FINISHED BASEMENT COST
# =========================================================================
COST_FINISHED_BODY = f"""
<section>
  <div class="prose-wide">
    <p>A finished basement is the foundation type that homeowners worry about for the wrong reason. The fear is that the mitigation crew will tear into your finished walls, leave drywall scars, and disrupt the room you spent money making nice. In practice, most finished basement installs are clean — but they do cost more than an unfinished install. Colorado Springs market data puts the typical range at <strong>$1,400–$2,800</strong> with a median around $1,900.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This page walks through the actual added cost, where the pipe can and can't go, what to expect about drywall and aesthetics, and what to ask the contractor before they show up.</p>
  </div>
</section>

<section>
  <h2>Why finished basements cost more</h2>
  <div class="prose-wide">
    <p>The system inside the slab is identical to an unfinished install — same suction point, same fan, same exhaust. What changes is the routing between the suction point and the roof. In an unfinished basement, the pipe can take the most direct path. In a finished basement, it has to navigate around drywall, closets, drop ceilings, and finished utility space.</p>
    <p>That routing complexity adds typically $300–$900 to the install:</p>
    <ul>
      <li><strong>Time to plan the route</strong> with the homeowner before drilling anything.</li>
      <li><strong>Possible drywall cut-and-patch</strong> if the pipe has to cross a finished wall.</li>
      <li><strong>Framing into a closet</strong> to box the pipe and make it look intentional.</li>
      <li><strong>Aesthetic finishing</strong> — paint match, decorative pipe boxing, or routing through a mechanical room to keep the pipe out of sight.</li>
      <li><strong>Surface protection</strong> during install — drop cloths, plastic, careful work around finished floors.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Where the pipe can — and can't — go</h2>
  <div class="prose-wide">
    <p>Three common routes through a finished basement, in rough order of cost:</p>

    <h3>1. Mechanical room or utility closet (cheapest)</h3>
    <p>If your basement has an unfinished utility room with the furnace and water heater, the pipe usually runs through it and out the rim joist or up to the attic. This is the cleanest aesthetic option — the pipe is essentially invisible from the finished space.</p>

    <h3>2. Inside a closet or storage room (middle)</h3>
    <p>If there's no mechanical room, the pipe sometimes runs vertically inside a closet with framing built around it. The closet loses a corner of usable space; the rest of the room looks untouched.</p>

    <h3>3. Through finished space with paint-matched pipe (highest)</h3>
    <p>If neither of the above is possible, the contractor may need to run the pipe through finished space — typically along a wall or in a corner — with the pipe painted to match the wall. This is the most visible option and the most disruptive install.</p>
  </div>
</section>

<section>
  <h2>Drywall touch-up — included or extra?</h2>
  <div class="prose-wide">
    <p>This is the most-asked question and the most-skipped quote line item. Two scenarios:</p>
    <ul>
      <li><strong>Touch-up included.</strong> Some Colorado contractors include drywall patching and paint match in the base quote. The pipe goes through, the hole gets patched, the wall gets painted, and you can't tell the work was done.</li>
      <li><strong>Touch-up extra.</strong> Other contractors do the structural cut and patch but leave finish work to you. That can add $200–$600 to bring in a drywall finisher and painter afterward.</li>
    </ul>
    <p>Ask before signing. "Is paint-match drywall finishing included?" is a fair question to put in writing.</p>
  </div>
</section>

<section>
  <h2>Aesthetic options worth paying for</h2>
  <div class="prose-wide">
    <p>If you want the finished space to look untouched, these add-ons are worth the spend:</p>
    <ul>
      <li><strong>Exterior alternative routing</strong> ($100–$300). Some homes can route the pipe outside the finished basement entirely — up a side wall and over the roof. You trade a visible exterior pipe for zero interior disruption.</li>
      <li><strong>Decorative pipe boxing</strong> ($150–$400). The pipe is framed into a column or boxed into a corner that matches the room.</li>
      <li><strong>Paint match</strong> ($50–$150). The pipe is painted to match the adjacent wall color so it blends in.</li>
      <li><strong>Concealed manometer</strong> ($25–$75). The manometer mount is positioned inside a utility closet rather than visible from the living area. (Note: it still has to be accessible.)</li>
    </ul>
  </div>
</section>

<section>
  <h2>Will mitigation damage your finished space?</h2>
  <div class="prose-wide">
    <p>With a competent DORA-licensed contractor, no — at least not in any way that isn't fully restored. The risks to manage:</p>
    <ul>
      <li><strong>Slab coring.</strong> The suction point requires a 4-inch hole through the slab. If your slab has tile, vinyl, or carpet over it, that finish in a small area is affected. Most contractors core through the cleanest accessible location.</li>
      <li><strong>Dust during install.</strong> Slab coring produces concrete dust. Surface protection (plastic, dropcloth) handles this. Ask whether dust containment is included.</li>
      <li><strong>Drywall opening.</strong> If interior routing crosses a finished wall, a small opening (usually 6–12 inches) is cut and patched.</li>
      <li><strong>HVAC interference.</strong> A poorly routed pipe can interfere with HVAC return ducts. A good contractor walks the basement with you first and plans around HVAC.</li>
    </ul>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a Mountain Shadows finished walk-out</strong>
    <p>A homeowner with a finished walk-out basement (TV room, bedroom, bath, utility closet) gets two quotes. The first ($1,750) proposes a single suction point in the utility closet and runs the pipe vertically up through the closet, into the attic, and out the roof. The closet loses about a foot of storage depth but the rest of the basement is untouched. The second quote ($2,300) is a more aesthetic install — exterior routing along the rear wall of the walk-out, painted to match the siding, with no interior pipe at all. Both work. The choice is whether to keep the utility closet full and accept an exterior pipe, or trade closet space for an invisible install.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
  </ol>
</aside>
"""


def cost_finished_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How much more does mitigation cost for a finished basement?",
             "acceptedAnswer": {"@type": "Answer", "text": "Finished basement mitigation runs $1,400–$2,800 in Colorado Springs (median $1,900), about $300–$900 more than an unfinished basement install. The added cost is for routing complexity around drywall, closets, and finished utility space, plus possible drywall touch-up and aesthetic options."}},
            {"@type": "Question", "name": "Will radon mitigation damage my finished basement?",
             "acceptedAnswer": {"@type": "Answer", "text": "Not with a competent DORA-licensed contractor. The suction point requires a 4-inch hole through the slab in one location, and interior pipe routing may require a small drywall opening that's patched. Ask the contractor whether paint-match drywall finishing is included before signing."}},
            {"@type": "Question", "name": "Can the radon pipe run outside instead of through the finished basement?",
             "acceptedAnswer": {"@type": "Answer", "text": "Often yes. Exterior routing keeps the pipe entirely outside the finished space — up a side wall and over the roof — for an additional $100–$300. The tradeoff is a visible exterior pipe (which can be paint-matched to the siding) versus a clean interior."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 8. /radon-mitigation-cost/real-estate-deadlines/   — REAL ESTATE DEADLINES
# =========================================================================
COST_REAL_ESTATE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You're under contract on a Colorado home. The inspection report just came back showing radon above the EPA action level. You have an inspection objection deadline approaching, a closing date locked in, and now a decision tree to navigate.</p>
    <p>The short answer: most Colorado mitigation systems can be installed in 7–10 days end-to-end (quote, scheduling, install, post-mitigation test), and a basement install typically runs $1,000–$3,500.<sup><a href="#src-1">[1]</a></sup> Whether you mitigate before closing, ask for a seller credit, or walk depends on your timeline, your contract terms, and how much pressure you're willing to absorb.</p>
    <p>This page walks through the Colorado-specific rules, your three buyer options, realistic timelines, and the tradeoffs between mitigating before closing versus taking a credit.</p>
  </div>
</section>

<section>
  <h2>Colorado SB23-206 — the disclosure law you should know</h2>
  <div class="prose-wide">
    <p>Since <strong>August 7, 2023</strong>, Colorado law requires sellers of residential property to disclose any known radon test results and any mitigation work performed on the home, along with the CDPHE radon brochure.<sup><a href="#src-2">[2]</a></sup> The disclosure happens through the Seller's Property Disclosure form (revised post-SB23-206) and applies to both sales and residential leases.</p>
    <p>What this means in practice:</p>
    <ul>
      <li>If the seller had a prior radon test, you should have seen the result in the disclosure.</li>
      <li>If the seller had mitigation done, you should have the system documentation and post-mitigation test result.</li>
      <li>If you discover elevated radon during inspection and the seller didn't disclose a prior test result, that's a fact pattern worth showing your real estate attorney.</li>
      <li>If you mitigate as a buyer and later sell the home, the system becomes <em>your</em> required disclosure.</li>
    </ul>
    <p>Colorado does <strong>not</strong> require sellers to mitigate before sale.<sup><a href="#src-1">[1]</a></sup> They must disclose; they can sell "as-is."</p>
  </div>
</section>

<section>
  <h2>Your three buyer options under the inspection objection</h2>
  <div class="prose-wide">

    <h3>Option 1 — Ask the seller to mitigate before closing</h3>
    <p>You request mitigation as part of the inspection objection. The seller hires a Colorado-licensed contractor, installs the system, completes a post-mitigation test, and provides you the documentation before closing.</p>
    <p><strong>When this works:</strong> Closing is at least 2 weeks out, the seller is motivated to keep the deal alive, and the local contractor pool has openings.</p>
    <p><strong>Tradeoffs:</strong> You don't control the contractor selection or the install quality. The seller chooses the lowest available bid.</p>

    <h3>Option 2 — Negotiate a seller credit at closing</h3>
    <p>The seller credits you a fixed dollar amount at closing — typically $1,500–$2,500 for a basement or $2,500–$4,500 for a crawlspace or multi-zone — and you hire a contractor on your own timeline after you own the home.</p>
    <p><strong>When this works:</strong> Closing is tight, you want control over the contractor, or you want to bundle mitigation with other post-purchase work (basement finishing, encapsulation).</p>
    <p><strong>Tradeoffs:</strong> You're exposed to the radon during whatever interval passes between closing and your install. The credit may not fully cover the actual install cost if the home turns out to be multi-zone or crawlspace.</p>

    <h3>Option 3 — Walk under the inspection contingency</h3>
    <p>If you have an inspection contingency and you're not willing to take a credit or wait for pre-close mitigation, you can terminate the contract.</p>
    <p><strong>When this works:</strong> You found something else in the inspection you also don't like, or you're in a buyer's market with comparable homes available.</p>
    <p><strong>Tradeoffs:</strong> Most Colorado Springs homes will test positive — the next home you go under contract on has a 40%+ chance of the same result.<sup><a href="#src-3">[3]</a></sup> "Walking on radon" alone is usually only the right call when you've also found a non-radon issue.</p>
  </div>
</section>

<section>
  <h2>How long mitigation actually takes</h2>
  <div class="prose-wide">
    <p>End-to-end, a Colorado Springs mitigation install typically runs 7–10 days:</p>
    <table class="compact">
      <thead>
        <tr><th>Step</th><th>Typical time</th></tr>
      </thead>
      <tbody>
        <tr><td>Quote (in-home assessment + written quote)</td><td>1–3 days</td></tr>
        <tr><td>Scheduling install</td><td>3–7 days out</td></tr>
        <tr><td>Install (single day)</td><td>4–8 hours on site</td></tr>
        <tr><td>Post-mitigation test wait (24h fan run, then 2–7 day test)</td><td>3–8 days</td></tr>
        <tr><td>Test result + system certification</td><td>1–3 days</td></tr>
      </tbody>
    </table>
    <p>If you're in a 14-day inspection objection window and closing 30 days out, pre-close mitigation is comfortable. If you're closing in 10 days, it's tight but doable. Closer than that, a seller credit is usually the cleaner path.</p>
  </div>
</section>

<section>
  <h2>Mitigate before close vs after close — the tradeoffs</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th></th><th>Mitigate before close</th><th>Credit + mitigate after close</th></tr>
      </thead>
      <tbody>
        <tr><td>Who picks the contractor</td><td>Seller</td><td>You</td></tr>
        <tr><td>Quality control</td><td>Seller's preference</td><td>Your choice of bids</td></tr>
        <tr><td>Documentation</td><td>Belongs to seller, transferred to you</td><td>Belongs to you from day one</td></tr>
        <tr><td>Timing</td><td>Must finish before closing date</td><td>Your schedule</td></tr>
        <tr><td>Cost certainty</td><td>Closing is contingent on a final post-mit test</td><td>Credit is fixed at closing</td></tr>
        <tr><td>Exposure during install gap</td><td>None (system in before you move in)</td><td>You live with radon until install</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Cost ranges for closing-deadline mitigations</h2>
  <div class="prose-wide">
    <p>Real estate deadlines sometimes carry a small premium for guaranteed completion scheduling — but the baseline pricing is the same as a non-rushed install. Use the four-scenario framework:</p>
    <ul>
      <li>Basic basement: $1,000–$2,000 (CDPHE baseline)</li>
      <li>Finished basement: $1,500–$3,000</li>
      <li>Crawlspace: $2,000–$4,500</li>
      <li>Multi-zone: $2,500–$5,000</li>
    </ul>
    <p>If you're negotiating a seller credit, those are reasonable numbers to anchor on. A credit at the high end of the appropriate scenario gives you room for a quality contractor without surprises.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — under contract with 18 days to closing</strong>
    <p>A buyer under contract on a 1990s tri-level home in Stetson Hills receives an inspection report showing 6.7 pCi/L. The seller's prior disclosure showed no test result. The buyer has 5 days remaining on their inspection objection and 18 days to closing. After consulting their agent, the buyer asks for a $3,000 seller credit at closing rather than asking the seller to mitigate (tri-level means multi-zone, and the buyer wants to control contractor selection and diagnostic scope). The seller agrees. After closing, the buyer takes two written quotes — both proposing a PFE diagnostic and two suction points — and installs the system in week three of ownership. The post-mitigation test comes in at 2.1 pCi/L. The buyer's documentation (test report, quotes, install paperwork, post-mit test) becomes part of their own future SB23-206 disclosure if they ever sell.</p>
  </div>
</section>

<section>
  <h2>What to keep for future disclosure</h2>
  <div class="prose-wide">
    <p>If you mitigate (or inherit a mitigation system from the seller), keep these documents permanently. They become your required SB23-206 disclosure when you eventually sell:</p>
    <ul class="checklist">
      <li>Original test report (the high reading that triggered mitigation)</li>
      <li>Contractor's written quote and final invoice</li>
      <li>System certification, DORA license verification, fan model and warranty paperwork</li>
      <li>Post-mitigation test result certificate</li>
      <li>Any retest results going forward (EPA recommends every 2 years)<sup><a href="#src-4">[4]</a></sup></li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">Colorado General Assembly. <em>SB23-206 (CRS § 38-35.7-112)</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
    <li id="src-3">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-4">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def cost_real_estate_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How long does radon mitigation take during a Colorado real estate transaction?",
             "acceptedAnswer": {"@type": "Answer", "text": "End-to-end, 7–10 days: 1–3 days for the quote, 3–7 days to schedule, single-day install, then a 3–8 day post-mitigation test cycle. If closing is 14+ days out, pre-close mitigation is comfortable. Closer than that, a seller credit is usually the cleaner path."}},
            {"@type": "Question", "name": "What does Colorado SB23-206 require for radon disclosure?",
             "acceptedAnswer": {"@type": "Answer", "text": "Effective August 7, 2023, Colorado SB23-206 (CRS § 38-35.7-112) requires sellers of residential property to disclose any known radon test results and any mitigation work performed, plus provide the CDPHE radon brochure. The law applies to sales and residential leases. Colorado does not require sellers to mitigate before sale — only to disclose."}},
            {"@type": "Question", "name": "Should I ask for a credit or have the seller mitigate?",
             "acceptedAnswer": {"@type": "Answer", "text": "A seller credit gives you control over contractor selection and timing, plus a fixed dollar amount at closing. Pre-close mitigation means no radon exposure when you move in but the seller chooses the contractor. Credit is usually cleaner for multi-zone homes (tri-level, basement + crawlspace) where the buyer wants diagnostic control."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
