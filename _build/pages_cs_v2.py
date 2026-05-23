"""Content for Phase 6 — Colorado Springs local cluster refresh.

One new page:
1. /colorado-springs/home-buyers-and-sellers/    — CS-specific real estate guide

The CS hub and failed-test page get cross-link updates in build.py.
"""
import json
from pages_main import s, SOURCES

# Idempotent source registration
SOURCES.setdefault("crec_spd", "https://dre.colorado.gov/division-real-estate-commission-forms")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")


# =========================================================================
# /colorado-springs/home-buyers-and-sellers/
# =========================================================================
CS_HOME_BUYERS_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Colorado Springs has one of the highest indoor radon prevalence rates in the country — El Paso County Public Health publishes that more than <strong>40% of homes tested 2005–2023</strong> came back at or above the EPA action level.<sup><a href="#src-1">[1]</a></sup> If you're buying or selling a Colorado Springs home, radon almost certainly comes up. This page walks through the local process from both sides of the transaction.</p>
    <p>This is information specific to Colorado Springs and the Pikes Peak region. The general Colorado real estate radon rules under SB23-206 apply statewide — see also <a href="/radon-testing/during-real-estate-transactions/">Radon Testing During Real Estate Transactions</a> and <a href="/radon-mitigation-cost/real-estate-deadlines/">Radon Mitigation Cost During a Real Estate Transaction</a>.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">El Paso County</div>
      <div class="stat">40%+</div>
      <div class="source">of homes tested 2005–2023 had elevated radon. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">EPCPH</a></div>
    </div>
    <div class="factbox">
      <div class="label">SB23-206</div>
      <div class="stat">Mandatory</div>
      <div class="source">Radon disclosure on every CO residential sale since Aug 7, 2023. <a href="{s('sb23_206')}" rel="noopener" target="_blank">CRS § 38-35.7-112</a></div>
    </div>
    <div class="factbox">
      <div class="label">CS basement install</div>
      <div class="stat">$900–$1,900</div>
      <div class="source">Median around $1,400. <a href="/colorado-springs/radon-mitigation-cost/">Local cost breakdown</a></div>
    </div>
    <div class="factbox">
      <div class="label">Closing timeline</div>
      <div class="stat">7–10 days</div>
      <div class="source">End-to-end mitigation (quote, install, post-mit test)</div>
    </div>
  </div>
</section>

<section>
  <h2>If you're a Colorado Springs buyer</h2>
  <div class="prose-wide">
    <p>The most common Colorado Springs scenario: you're under contract on a home in Stetson Hills, Briargate, Black Forest, Falcon, Mountain Shadows, Old Colorado City, or anywhere in El Paso County. Your inspection includes a radon test (most local inspectors offer it as an add-on, $150–$300). The result comes back above 4.0 pCi/L. Now what?</p>

    <h3>Step 1 — Review the seller's disclosure</h3>
    <p>Colorado SB23-206 requires the seller to disclose any prior radon test results or mitigation work in the Seller's Property Disclosure (SPD) form. Three possibilities:</p>
    <ul>
      <li><strong>"No known test."</strong> The seller never tested. Common in Colorado Springs. Move to Step 2.</li>
      <li><strong>"Prior test below 4.0 pCi/L."</strong> The seller tested and got a low result. Your inspection test may still come back higher (different test, different season, different placement). If yours is high and theirs was low, run a follow-up confirmation test.</li>
      <li><strong>"Mitigation installed."</strong> The seller has a system. Verify it's working: check the manometer reading, look at the system documentation, and re-test the home as part of inspection. <a href="/radon-mitigation-systems/what-happens-after-mitigation/">What to verify on an existing system &rarr;</a></li>
    </ul>

    <h3>Step 2 — File your inspection objection on time</h3>
    <p>Colorado real estate contracts have specific inspection objection and resolution deadlines. Typical timeline:</p>
    <table class="compact">
      <thead>
        <tr><th>Day from contract</th><th>What happens</th></tr>
      </thead>
      <tbody>
        <tr><td>0</td><td>Offer accepted, contract signed</td></tr>
        <tr><td>~3</td><td>Inspection (typically includes radon test as add-on)</td></tr>
        <tr><td>~5–7</td><td>Test results returned</td></tr>
        <tr><td>By Inspection Objection deadline (often day 7–10)</td><td>File objection if result is above 4.0 pCi/L</td></tr>
        <tr><td>~3 days later</td><td>Seller's response deadline</td></tr>
        <tr><td>By Inspection Resolution deadline</td><td>Agreement reached or contract terminated</td></tr>
        <tr><td>~Day 30</td><td>Closing</td></tr>
      </tbody>
    </table>
    <p>Don't miss the objection deadline. If you let it pass without filing, you've waived your right to negotiate the radon issue.</p>

    <h3>Step 3 — Choose your option</h3>
    <p>You have three Colorado options when the inspection result is high:</p>
    <ol>
      <li><strong>Ask the seller to mitigate before closing.</strong> Workable if closing is at least 14 days out and the seller is motivated. The seller picks the contractor.</li>
      <li><strong>Negotiate a seller credit at closing.</strong> Anchor on the four-scenario framework: $1,500–$2,500 for a basic basement, $2,500–$4,500 for crawlspace or multi-zone. You hire the contractor after closing on your schedule.</li>
      <li><strong>Walk away.</strong> Only the right call if you've found other issues. The next Colorado Springs home you put under contract has a 40%+ chance of the same result.</li>
    </ol>
    <p>Most CS buyers in this position take the credit. Pre-close mitigation is workable but tight, and you don't control quality. <a href="/radon-mitigation-cost/real-estate-deadlines/">Full credit-vs-mitigate tradeoff &rarr;</a></p>

    <h3>Step 4 — After closing</h3>
    <p>If you took a credit, hire a DORA-licensed Colorado Springs contractor on your timeline. Get at least two written quotes. For multi-zone homes (tri-levels, split-levels, basement + crawlspace combinations — common in older CS neighborhoods), make sure the contractor will run a Pressure Field Extension (PFE) diagnostic before quoting.</p>
    <p>Once installed, keep all the documentation in your home records. It becomes part of <em>your</em> required SB23-206 disclosure when you eventually sell.</p>
  </div>
</section>

<section>
  <h2>If you're a Colorado Springs seller</h2>
  <div class="prose-wide">
    <p>The Colorado Springs market reality: most homes have elevated radon, the buyer's inspection will likely catch it, and SB23-206 requires you to disclose anything you already know. Your options:</p>

    <h3>Option 1 — Test and mitigate before listing</h3>
    <p>The cleanest path. You handle radon before the listing photos go up, you control the contractor selection, and the system becomes a selling point ("mitigated, with verification test") instead of a negotiation lever.</p>
    <ul>
      <li>Total cost typically $900–$2,800 (basic basement) or higher for crawlspace/multi-zone.</li>
      <li>Timeline: 7–10 days end-to-end.</li>
      <li>You disclose the mitigation on the SPD form and provide the buyer with the system documentation.</li>
      <li>Removes a major source of friction in the inspection objection period.</li>
    </ul>

    <h3>Option 2 — Disclose and price-adjust at the offer table</h3>
    <p>If you have a recent (within 1–2 years) low radon test result, you can list "as-is" and disclose it. The buyer may still want to run their own test, but you've documented your prior result.</p>
    <p>If you have a recent high result or no prior test, the buyer's inspection will likely find it. You can:</p>
    <ul>
      <li>Price the home anticipating a buyer credit at closing.</li>
      <li>Offer a credit pro-actively in the listing description.</li>
      <li>Mitigate during the inspection objection period as part of a negotiated resolution.</li>
    </ul>

    <h3>Option 3 — Don't test, don't mitigate, disclose "no known test"</h3>
    <p>Legally permissible under SB23-206 — the law requires you to disclose what you know, not to test. But: the buyer's inspection will almost certainly include a radon test (Colorado Springs market norm), so you're deferring the conversation, not avoiding it. And once the buyer's result comes back, you're negotiating from a weaker position than if you'd handled it pre-listing.</p>
  </div>
</section>

<section>
  <h2>The SB23-206 disclosure form</h2>
  <div class="prose-wide">
    <p>The Colorado Real Estate Commission updated the Seller's Property Disclosure (SPD) form after SB23-206 took effect on August 7, 2023. The current SPD form asks the seller about:<sup><a href="#src-2">[2]</a></sup></p>
    <ul>
      <li>Whether the seller is aware of any radon test results for the property.</li>
      <li>The results of those tests if known.</li>
      <li>Whether radon mitigation has been performed.</li>
      <li>The date mitigation was installed and by whom.</li>
    </ul>
    <p>Sellers must provide the CDPHE radon brochure to buyers along with the SPD. If you're a seller, your real estate agent will provide the current form and brochure. If you're a buyer, read the radon section of the SPD carefully — anything checked "yes" should be supported by documentation.</p>
  </div>
</section>

<section>
  <h2>Local Colorado Springs context</h2>
  <div class="prose-wide">

    <h3>El Paso County Public Health resources</h3>
    <p>The EPCPH Lab at 1675 W. Garden of the Gods Rd sells radon test kits and provides local radon program information.<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li><strong>Short-term kits:</strong> $15</li>
      <li><strong>Long-term kits:</strong> $42</li>
      <li><strong>Phone:</strong> (719) 578-3199, option 3</li>
    </ul>

    <h3>Pikes Peak Regional Building Department</h3>
    <p>PPRBD covers Colorado Springs, Fountain, Manitou Springs, Monument, Palmer Lake, and Woodland Park. Radon mitigation typically requires an electrical permit for the fan wiring; the contractor should pull it.</p>

    <h3>Common Colorado Springs neighborhood radon patterns</h3>
    <p>Test results vary significantly within and between neighborhoods, but some patterns:</p>
    <ul>
      <li><strong>Newer subdivisions</strong> (post-2009 builds in Banning Lewis Ranch, Wolf Ranch, Cordera) often have passive radon rough-ins from new construction. If your buyer's home has one, test the home and activate the system if needed.</li>
      <li><strong>Older Front Range neighborhoods</strong> (Old Colorado City, Briargate, Stetson Hills, Pleasant Valley) frequently test above the action level due to direct contact with Pikes Peak granite.</li>
      <li><strong>Mountain neighborhoods</strong> (Black Forest, Mountain Shadows, parts of Manitou) often have crawlspace foundations, which can require sub-membrane mitigation systems ($1,800–$4,000).</li>
      <li><strong>Tri-level and split-level homes</strong> (common in 1970s–1990s subdivisions like Stetson Hills, Pleasant Valley) are multi-zone foundations requiring multiple suction points.</li>
    </ul>
    <p>None of this changes the basic process — test, evaluate, mitigate if needed — but it does mean the cost and approach can vary by neighborhood and home age.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — buyer under contract in Stetson Hills</strong>
    <p>A buyer under contract on a 1990s tri-level in Stetson Hills. Inspection includes a radon test from the home inspector ($200 add-on). Result: 6.7 pCi/L. The SPD said "no known prior test." With 4 days remaining on the inspection objection deadline, the buyer asks for a $3,000 seller credit at closing — anchored on the multi-zone framework band ($2,200–$4,800). Seller agrees. After closing, the buyer hires a DORA-licensed Colorado Springs contractor who runs a PFE diagnostic and installs a two-suction-point system for $2,650. The post-mitigation test comes back at 1.8 pCi/L. The buyer's documentation is filed for future SB23-206 disclosure when they eventually sell.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-2">Colorado General Assembly. <em>SB23-206 (CRS § 38-35.7-112)</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a> · Colorado Division of Real Estate (Real Estate Commission Forms). <a href="{s('crec_spd')}" rel="noopener" target="_blank">dre.colorado.gov/division-real-estate-commission-forms</a></li>
    <li id="src-3">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
  </ol>
</aside>
"""


def cs_home_buyers_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What are my options if I'm a Colorado Springs buyer and the inspection finds high radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "Three options: ask the seller to mitigate before closing (workable if 14+ days out), negotiate a seller credit at closing (most common in Colorado Springs — anchor on $1,500-$4,500 depending on foundation type), or walk away (only if you've found other issues; next CS home has a 40%+ chance of the same result). File your inspection objection on time."}},
            {"@type": "Question", "name": "Should I test my Colorado Springs home before listing?",
             "acceptedAnswer": {"@type": "Answer", "text": "It's the cleanest path. Testing pre-listing means you control the contractor selection if mitigation is needed, the system becomes a selling point rather than a negotiation lever, and the documentation transfers cleanly to the buyer. Cost: $15-$300 for testing, $900-$2,800 for basic basement mitigation if needed."}},
            {"@type": "Question", "name": "Does Colorado law require me to mitigate radon before selling?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Colorado SB23-206 requires sellers to disclose any known prior radon test results and any mitigation work, plus provide the CDPHE radon brochure. The law does not require sellers to test or mitigate. However, the buyer's inspection will almost certainly include a radon test (Colorado Springs market norm), and 40%+ of El Paso County homes test elevated — so the issue typically comes up regardless."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
