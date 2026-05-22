"""Page content for the statewide homepage and Colorado Springs hub."""
import json

# Source URLs used across the site
SOURCES = {
    "cdphe_radon": "https://cdphe.colorado.gov/radon",
    "cdphe_realestate": "https://cdphe.colorado.gov/radon/radon-and-real-estate",
    "epa_radon": "https://www.epa.gov/radon",
    "epa_action_level": "https://www.epa.gov/radon/health-risk-radon",
    "elpaso_radon": "https://www.elpasocountyhealth.org/radon",
    "denver_radon": "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Public-Health-Environment/Environmental-Quality/Air-Quality/Radon",
    "sb23_206": "https://leg.colorado.gov/bills/sb23-206",
    "dora_radon": "https://dpo.colorado.gov/Radon",
    "nrpp": "https://nrpp.info/",
    "nrsb": "https://nrsb.org/",
}

def s(name):
    return SOURCES[name]


# =========================================================================
# HOMEPAGE
# =========================================================================
HOMEPAGE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Roughly <strong>half of Colorado homes test above the U.S. Environmental Protection Agency's radon action level</strong> of 4.0 picocuries per liter (pCi/L). Colorado's uranium-rich Rocky Mountain geology means radon is not a rare problem here — it is a baseline assumption for every homeowner, buyer, and seller in the state.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This site is an <strong>independent guide</strong>. We do not install mitigation systems and we do not represent a single contractor. We pull from the Colorado Department of Public Health and Environment (CDPHE), the EPA, El Paso County Public Health, Denver Public Health, and Colorado state law to help you make the call: <em>do I need to test, do I need to mitigate, and what should it cost?</em></p>
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
  <h2>What radon is and why it matters in Colorado</h2>
  <div class="prose-wide">
    <p>Radon is an invisible, odorless, radioactive gas produced by the natural decay of uranium in soil and rock. It rises from the ground and enters homes through cracks in foundations, sump pits, drain tile, crawl spaces, and other openings. Because Colorado's geology is uranium-rich, indoor radon accumulates here more than in most of the U.S. — and the EPA classifies most of the Front Range, including El Paso County, as <strong>Zone 1: highest potential</strong>.<sup><a href="#src-2">[2]</a></sup></p>
    <p>Long-term exposure damages lung tissue and increases lung cancer risk. The EPA estimates radon causes roughly 21,000 lung cancer deaths per year in the U.S., and CDPHE identifies radon as the second-leading cause of lung cancer in Colorado overall and the leading cause among non-smokers.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-3">[3]</a></sup> Risk is additive with smoking, but you do not have to smoke for radon to be a problem.</p>
  </div>
</section>

<section>
  <h2>Testing comes first — always</h2>
  <div class="prose-wide">
    <p>You cannot smell, see, or feel radon. The only way to know your level is to test. CDPHE recommends every Colorado home be tested, and EPA guidance is to retest every two years or after major remodels or HVAC changes.<sup><a href="#src-1">[1]</a></sup></p>
    <p>You have three practical options:</p>
    <ul>
      <li><strong>Short-term DIY kit</strong> (2–7 days). Low-cost, available at retail and from CDPHE programs.</li>
      <li><strong>Long-term DIY kit</strong> (90+ days). Better picture of year-round exposure.</li>
      <li><strong>Professional measurement</strong> by a contractor certified through the National Radon Proficiency Program (NRPP) or the National Radon Safety Board (NRSB), required for real estate transactions.<sup><a href="#src-4">[4]</a></sup></li>
    </ul>
    <p>Our <a href="/colorado-springs/radon-testing/">Colorado Springs testing guide</a> walks through each option, what they cost, and how to interpret the result.</p>
  </div>
</section>

<section>
  <h2>If your test is high, mitigation is solvable</h2>
  <div class="prose-wide">
    <p>A result at or above 4.0 pCi/L is the EPA's action threshold. The standard fix is <strong>active sub-slab depressurization</strong> — a sealed vent pipe and a quiet electric fan that pulls radon from under the slab and exhausts it above the roofline. Homes with crawl spaces use a sub-membrane variant; homes with sump pits or drain tile can tie those into the system.</p>
    <p>A correctly designed system typically reduces indoor radon by <strong>80–99%</strong>.<sup><a href="#src-2">[2]</a></sup> CDPHE and El Paso County both put a typical Colorado mitigation system in the <strong>$1,000–$2,000</strong> range, with larger or more complex installations costing more.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-5">[5]</a></sup> Our <a href="/colorado-springs/radon-mitigation-cost/">cost page</a> breaks down what drives the price.</p>
    <p>Caulking, sealing, or running fans alone is <strong>not</strong> a substitute for a properly engineered system. CDPHE warns that sealing cracks alone is unreliable and can sometimes make things worse.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>Colorado law &amp; licensing — what changed in 2022 and 2023</h2>
  <div class="prose-wide">
    <p>Two recent regulatory changes shape every Colorado radon decision:</p>
    <ul>
      <li><strong>Contractor licensing (July 2022).</strong> All radon measurement and mitigation professionals working in Colorado must be certified through NRPP or NRSB <em>and</em> registered with the <a href="{s('dora_radon')}" rel="noopener" target="_blank">Colorado Department of Regulatory Agencies (DORA) Office of Radon Professionals</a>. Always verify a contractor's registration before hiring.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>Real estate disclosure — SB23-206 (2023).</strong> Every residential sale and lease in Colorado must include a radon warning, any known test results, and any mitigation history. The CDPHE radon brochure must be provided. After January 2026, tenants gain additional remedies if a known elevated radon level was not mitigated.<sup><a href="#src-6">[6]</a></sup></li>
    </ul>
    <p>Important nuance: Colorado does <strong>not</strong> require a seller to test or mitigate — only to disclose what they know.<sup><a href="#src-1">[1]</a></sup> Buyers should not assume "no disclosure" means "no radon." It usually means "no test was done."</p>
  </div>
</section>

<section>
  <h2>What this site is — and what it isn't</h2>
  <div class="prose-wide">
    <p>Colorado Radon Guide is an independent editorial resource. We publish information drawn from public Colorado and federal health sources, and we connect homeowners who request a quote with a licensed Colorado mitigation partner. That is it.</p>
    <ul>
      <li><strong>We are not a radon contractor.</strong> We do not install systems and we do not sell equipment.</li>
      <li><strong>We are not a medical or legal source.</strong> We summarize publicly available guidance and link to the originals — always confirm with CDPHE, the EPA, or a licensed professional for your specific situation.</li>
      <li><strong>We are paid when a quote is routed to a partner.</strong> See our <a href="/disclosure/">editorial &amp; lead disclosure</a> for the financial relationship and editorial separation.</li>
    </ul>
    <p>If that sounds reasonable, the most useful place to go next is your city.</p>
  </div>
</section>

<section>
  <h2>Pick your city</h2>
  <div class="card-grid">
    <div class="card">
      <h3>Colorado Springs</h3>
      <p>El Paso County is EPA Zone 1; more than 40% of homes tested 2005–2023 came back high. Start here for testing, mitigation cost, and what to do after a failed result.</p>
      <p><a href="/colorado-springs/" class="btn btn-secondary">Colorado Springs Hub</a></p>
    </div>
    <div class="card">
      <h3>More cities coming</h3>
      <p>We are expanding to Denver, Aurora, Boulder, and Fort Collins next. If you would like to be notified when your city's guide is live, <a href="/contact/">drop us a line</a>.</p>
      <p><span class="pill">Coming soon</span></p>
    </div>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado Department of Public Health and Environment. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">U.S. Environmental Protection Agency. <em>Radon</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-3">U.S. Environmental Protection Agency. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-4">Colorado Department of Regulatory Agencies. <em>Office of Radon Professionals</em>. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-5">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-6">Colorado General Assembly. <em>SB23-206: Concerning measures to mitigate the effects of radon in residential properties</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


# =========================================================================
# COLORADO SPRINGS HUB
# =========================================================================
CS_HUB_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Colorado Springs sits in El Paso County, which the EPA designates <strong>Zone 1</strong> — the highest predicted indoor radon zone in the country. The county's own public-health data is even more pointed: of all homes tested in El Paso County between 2005 and 2023, <strong>more than 40% came back above the EPA action level of 4.0 pCi/L</strong>.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This page is the starting point for everything radon-related in Colorado Springs: testing, mitigation systems, cost, what to do if your test failed, and how to verify a contractor before you hand them a check.</p>
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
  <h2>Why Colorado Springs has high radon</h2>
  <div class="prose-wide">
    <p>The same geology that gives Colorado its Rocky Mountain scenery is the reason radon levels here are elevated. Uranium-bearing rock and soil are abundant under the Front Range, and radon — a product of uranium decay — accumulates indoors when soil gas enters through foundation cracks, drain tile gaps, sump pits, and unsealed crawl spaces.<sup><a href="#src-2">[2]</a></sup></p>
    <p>What matters in practice: <strong>basements and crawl spaces are the typical entry points</strong>. Slab-on-grade homes still have radon, but multi-level homes with finished basements are where Colorado Springs sees the highest readings.</p>
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
    <p>A reading above 4.0 pCi/L is the EPA action threshold. What you do next depends on whether you are a homeowner with no transaction pending, a buyer or seller under contract, or a tenant or landlord:</p>
    <ul>
      <li>Confirm the reading with a second test or continuous monitor</li>
      <li>Get at least two written quotes from licensed contractors</li>
      <li>If you are under contract, calculate the closing timeline before negotiating</li>
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
    <p>El Paso County Public Health reports more than 40% of homes tested between 2005 and 2023 were above the EPA action level. The county is in EPA Zone 1, the highest indoor radon category. It is a real, locally documented issue — not marketing.<sup><a href="#src-1">[1]</a></sup></p>
  </details>
  <details>
    <summary>How long does mitigation take?</summary>
    <p>Most single-family installations take one day. Add a few days to schedule, plus a post-installation test (which is typically 48 hours). A reasonable end-to-end timeline is one to two weeks once you have signed a quote.</p>
  </details>
  <details>
    <summary>Will I have to retest after mitigation?</summary>
    <p>Yes. A post-mitigation test confirms the system is working. Reputable contractors include this in the quote. After that, EPA guidance is to retest every two years.<sup><a href="#src-4">[4]</a></sup></p>
  </details>
  <details>
    <summary>Do air purifiers fix radon?</summary>
    <p>No. Radon is a soil gas; it has to be redirected away from the home's foundation. Air purifiers do not address the entry pathway and the EPA does not recommend them as a substitute for mitigation.<sup><a href="#src-2">[2]</a></sup></p>
  </details>
  <details>
    <summary>Does Colorado Springs require a permit for mitigation?</summary>
    <p>Mechanical and electrical work on a mitigation system may require a permit; your licensed contractor will pull it. Always confirm the permit is included in the written quote.</p>
  </details>
  <details>
    <summary>What if I cannot afford mitigation?</summary>
    <p>CDPHE administers a low-income radon mitigation assistance program. Eligibility and funding vary year to year; check the <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE radon page</a> for the current details.<sup><a href="#src-5">[5]</a></sup></p>
  </details>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-2">U.S. Environmental Protection Agency. <em>Radon</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-3">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
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
