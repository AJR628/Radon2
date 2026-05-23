"""Content for the Testing & Real Estate pillar pages (Phase 4 build).

Six new pages:
1. /radon-testing/                              — hub (How to Test for Radon in Colorado)
2. /radon-testing/short-term-vs-long-term/      — test duration comparison
3. /radon-testing/where-to-place-a-test/        — EPA placement guidance
4. /radon-testing/during-real-estate-transactions/  — SB23-206 + inspection workflow
5. /radon-testing/for-rentals/                  — Colorado landlord disclosure
6. /radon-testing/for-businesses/               — Commercial buildings & workplaces

V1 cross-link refreshes are handled in build.py (related blocks updated).
"""
import json
from pages_main import s, SOURCES

# Ensure all needed sources are registered (idempotent across modules)
SOURCES.setdefault("epa_citizens_guide", "https://www.epa.gov/radon/citizens-guide-radon")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")
SOURCES.setdefault("epa_radon_in_schools", "https://www.epa.gov/radon/radon-schools")
SOURCES.setdefault("aarst_standards", "https://standards.aarst.org/")
SOURCES.setdefault("aarst_mams", "https://aarst.org/")
SOURCES.setdefault("crec_spd", "https://dre.colorado.gov/division-real-estate-commission-forms")
SOURCES.setdefault("colorado_landlord", "https://leg.colorado.gov/bills/sb23-206")


# =========================================================================
# 1. /radon-testing/   — HUB: How to Test for Radon in Colorado
# =========================================================================
TESTING_HUB_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You can't smell radon. You can't see it. You can't tell from looking at your house whether your level is 0.8 pCi/L (safely below the action threshold) or 12.4 pCi/L (well above it). The only way to know is to test.</p>
    <p>In Colorado, that's not a small thing. CDPHE estimates roughly half of Colorado homes test above the EPA action level of 4.0 pCi/L. In El Paso County, more than 40% of homes tested between 2005 and 2023 came back elevated.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup> This is the plain-language guide to testing your home — what kind of test to use, where to put it, what your result means, and when to retest.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">EPA action level</div>
      <div class="stat">4.0 pCi/L</div>
      <div class="source">Mitigate at or above. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">EPA</a></div>
    </div>
    <div class="factbox">
      <div class="label">WHO reference level</div>
      <div class="stat">~2.7 pCi/L</div>
      <div class="source">100 Bq/m³. Lower than EPA. <a href="https://www.who.int/" rel="noopener" target="_blank">WHO 2010</a></div>
    </div>
    <div class="factbox">
      <div class="label">Test kit (county)</div>
      <div class="stat">$15</div>
      <div class="source">El Paso County Public Health Lab short-term kit. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">EPCPH</a></div>
    </div>
    <div class="factbox">
      <div class="label">Professional test</div>
      <div class="stat">$150–$300</div>
      <div class="source">Continuous monitor for real estate transactions</div>
    </div>
  </div>
</section>

<section>
  <h2>The three test types you'll see</h2>
  <div class="prose-wide">

    <h3>1. Short-term DIY kit (2 to 7 days)</h3>
    <p>A small activated-charcoal or alpha-track canister you place in the lowest livable level of your home, then mail to a lab. Cost is typically $15–$40 including lab analysis. Results come back in 1–2 weeks.</p>
    <p>Use a short-term test when:</p>
    <ul>
      <li>You want a quick first read on your home.</li>
      <li>You're in a real estate transaction with a tight timeline (though a professional test is preferred — see below).</li>
      <li>You're confirming the result of a previous test.</li>
    </ul>

    <h3>2. Long-term DIY kit (90+ days)</h3>
    <p>An alpha-track detector that sits in place for at least 90 days. Long-term tests average radon levels across seasons, which matters in Colorado because <strong>winter levels (sealed-up homes, stronger stack effect) are typically higher than summer levels</strong>. A 90-day or year-long test gives a more accurate picture of your average exposure than a 2-day snapshot.</p>
    <p>Use a long-term test when:</p>
    <ul>
      <li>You're not under a transaction deadline.</li>
      <li>You want a more accurate annual exposure picture.</li>
      <li>A short-term test was borderline (close to 4.0 pCi/L).</li>
    </ul>

    <h3>3. Professional measurement (continuous monitor)</h3>
    <p>A continuous radon monitor placed by a DORA-licensed, NRPP or NRSB certified professional. Records hourly readings; results typically returned in 48–72 hours. The standard for real estate transactions and any situation requiring a defensible result.</p>
    <p>Use professional measurement when:</p>
    <ul>
      <li>You're buying or selling a home and need a defensible result.</li>
      <li>Your DIY test came back high and you want a third-party confirmation before mitigation.</li>
      <li>You're testing after mitigation (a post-mit test).</li>
    </ul>
    <p>Professional measurement in Colorado Springs typically runs $150–$300. <a href="/radon-testing/during-real-estate-transactions/">Full real-estate-testing walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Where to get a test kit in Colorado</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>El Paso County Public Health Laboratory.</strong> Short-term kits $15, long-term $42. Pickup at 1675 W. Garden of the Gods Rd, Colorado Springs. Phone (719) 578-3199 option 3.<sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>CDPHE state radon program.</strong> Periodically offers low-cost or free kits during National Radon Action Month (January). Check <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a>.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>Retail hardware stores.</strong> Home Depot, Lowe's, Ace Hardware, and Amazon stock EPA-listed short-term kits. Look for "EPA-listed" or "AARST-NRPP listed" on the packaging — these are the kits backed by accredited labs.</li>
      <li><strong>Online radon labs.</strong> Many ship a canister and pre-paid return mailer with lab analysis included in one price.</li>
    </ul>
  </div>
</section>

<section>
  <h2>How to place a test correctly</h2>
  <div class="prose-wide">
    <p>A test placed incorrectly returns the wrong answer. The EPA placement guidance:<sup><a href="#src-3">[3]</a></sup></p>
    <ul class="checklist">
      <li>Place the test in the <strong>lowest livable level</strong> of the home (a finished basement counts; an unfinished crawlspace does not).</li>
      <li>Place it <strong>2–6 feet above the floor</strong>, away from drafts, fireplaces, exterior walls, and high-humidity areas like bathrooms.</li>
      <li>Keep windows and exterior doors <strong>closed for at least 12 hours before and during</strong> a short-term test. Normal in-and-out traffic is fine.</li>
      <li>Avoid placing the test next to running HVAC vents or in direct sunlight.</li>
      <li>Don't move the test once it's deployed.</li>
    </ul>
    <p>Detail: <a href="/radon-testing/where-to-place-a-test/">where to place a test &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What your result means</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th>Result (pCi/L)</th><th>EPA guidance</th><th>What to do</th></tr>
      </thead>
      <tbody>
        <tr><td>&lt; 2.0</td><td>Below "consider action" threshold</td><td>Retest every 2 years.</td></tr>
        <tr><td>2.0–3.9</td><td>EPA suggests "consider mitigation"</td><td>Retest (long-term preferred) and decide. Many Colorado homes in this range still mitigate, because WHO recommends action at 2.7 pCi/L.</td></tr>
        <tr><td>4.0 or above</td><td>Action level — mitigate</td><td>Confirm with a second test or a professional continuous monitor. Then get at least two written quotes from DORA-licensed Colorado contractors.</td></tr>
        <tr><td>10.0 or above</td><td>Well above action level</td><td>Mitigate. Limit time in the lowest level until a system is in place.</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Action level reference: <a href="{s('epa_action_level')}" rel="noopener" target="_blank">EPA — Health Risk of Radon</a>. WHO reference: <a href="https://www.who.int/" rel="noopener" target="_blank">WHO Guidelines for Indoor Air Quality (2010)</a>.</p>
  </div>
</section>

<section>
  <h2>The borderline zone — 3.5 to 4.2 pCi/L</h2>
  <div class="prose-wide">
    <p>If you tested in the borderline range — say, 3.7 pCi/L or 4.1 pCi/L — you're not alone in feeling stuck. Most Colorado homeowners in this band wrestle with the same decision.</p>
    <p>A few things to know:</p>
    <ul>
      <li><strong>The EPA's 4.0 action level isn't a cliff.</strong> Risk is continuous. 3.9 pCi/L and 4.1 pCi/L are essentially the same exposure.</li>
      <li><strong>WHO recommends action at 2.7 pCi/L</strong>, which is significantly lower than EPA. Many international guidelines fall in the 2.7–4.0 range.</li>
      <li><strong>Colorado has significant seasonal swings.</strong> A short-term winter test reading at 3.7 may show 2.4 in summer, or vice versa. A long-term test (90+ days) averages across seasons.</li>
      <li><strong>Risk is exposure-time dependent.</strong> Daily use of the lowest level (a finished basement bedroom, a home office) matters more than time spent on upper floors.</li>
    </ul>
    <p>The decision tree most homeowners settle on:</p>
    <ol>
      <li>Run a long-term test for 90 days to get the seasonal average.</li>
      <li>If the long-term result is also above 3.5, most people mitigate — particularly if the lowest level is used daily.</li>
      <li>If the long-term result drops below 3.0 and the lowest level isn't heavily used, retesting every 2 years is a reasonable choice.</li>
    </ol>
  </div>
</section>

<section>
  <h2>When to retest</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Every 2 years</strong> for a previously low result. EPA standard recommendation.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>After any major remodel</strong> that changes the foundation, basement, or HVAC.</li>
      <li><strong>After mitigation</strong> — a post-install test confirms the system actually brought levels below 4.0 pCi/L.</li>
      <li><strong>Before listing or buying</strong> a home.</li>
      <li><strong>If your living patterns change</strong> — for example, finishing a basement that becomes daily living space.</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-3">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-4">U.S. EPA. <em>Citizen's Guide to Radon</em>. <a href="{s('epa_citizens_guide')}" rel="noopener" target="_blank">epa.gov/radon/citizens-guide-radon</a></li>
  </ol>
</aside>
"""


def testing_hub_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How do I test for radon in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Three options: a short-term DIY kit (2-7 days, $15-$40), a long-term DIY kit (90+ days, $30-$60), or a professional continuous monitor placed by a DORA-licensed tester ($150-$300, used for real estate transactions). El Paso County Public Health Lab sells short-term kits for $15 and long-term for $42. Place the test in the lowest livable level, 2-6 feet above the floor, away from drafts and humidity, with closed-house conditions for 12 hours before and during."}},
            {"@type": "Question", "name": "What does my radon test result mean?",
             "acceptedAnswer": {"@type": "Answer", "text": "Below 2.0 pCi/L: retest every 2 years. 2.0-3.9 pCi/L: EPA suggests consider mitigation (WHO recommends action at 2.7). 4.0 or above: EPA action level, mitigate. 10.0 or above: well above action level, mitigate and limit time in the lowest level until a system is installed."}},
            {"@type": "Question", "name": "I'm in the borderline zone (3.5-4.2 pCi/L). What should I do?",
             "acceptedAnswer": {"@type": "Answer", "text": "The EPA's 4.0 action level isn't a cliff — risk is continuous, and 3.9 vs 4.1 are essentially the same exposure. WHO recommends action at 2.7 pCi/L (lower than EPA). Most Colorado borderline-zone homeowners run a long-term test (90 days) for a seasonal average, then mitigate if it stays above 3.5 — especially if the lowest level is used daily."}},
            {"@type": "Question", "name": "When should I retest for radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "Every 2 years per EPA recommendation, after major remodels that change the foundation or HVAC, after mitigation (post-install verification), before listing or buying a home, and if your living patterns change (finishing a basement that becomes daily living space)."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 2. /radon-testing/short-term-vs-long-term/
# =========================================================================
SHORT_VS_LONG_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You're standing in the hardware-store aisle looking at two radon kits. One says "2-day test" on the box. The other says "90-day test." They cost about the same. Which one do you buy?</p>
    <p>The right answer depends on what you're trying to learn, what your timeline is, and how seasonal Colorado's radon swings actually are. This page walks through when to use which — and why a quick short-term test sometimes misses what a 90-day test catches.</p>
  </div>
</section>

<section>
  <h2>The short version</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th></th><th>Short-term</th><th>Long-term</th></tr>
      </thead>
      <tbody>
        <tr><td>Duration</td><td>2 to 7 days</td><td>90+ days (often 3 to 12 months)</td></tr>
        <tr><td>Cost</td><td>$15–$40</td><td>$30–$60</td></tr>
        <tr><td>How it works</td><td>Activated charcoal or short alpha-track detector</td><td>Long alpha-track detector</td></tr>
        <tr><td>Result reflects</td><td>Levels during the test window</td><td>Average across seasons</td></tr>
        <tr><td>Best for</td><td>Quick first read, real-estate timing, post-mit verification</td><td>Accurate annual exposure picture, borderline results, year-over-year tracking</td></tr>
        <tr><td>Closed-house required?</td><td>12 hours before + during test</td><td>Normal living, no closed-house requirement</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Short-term tests: speed over precision</h2>
  <div class="prose-wide">
    <p>A short-term test captures whatever the radon level is during a 2 to 7-day window. That window can be windy and warm (lower readings) or still and cold (higher readings). Same house, same year — two short-term tests run a month apart can land 30% apart from each other.</p>
    <p>That doesn't mean short-term tests are unreliable. It means they answer a specific question well: <strong>"Right now, is my home above the action level?"</strong> If the answer is clearly yes (say, 8 pCi/L), no further short-term tests will change that. If the answer is clearly no (1.2 pCi/L), the home is probably fine.</p>
    <p>Where short-term tests get tricky is the middle — a 3.6 pCi/L reading in March doesn't tell you whether the annual average is 2.4 or 4.8. That's where long-term tests earn their keep.</p>
  </div>
</section>

<section>
  <h2>Long-term tests: averaging across seasons</h2>
  <div class="prose-wide">
    <p>Radon levels in Colorado homes change with the seasons. The biggest driver is the <strong>stack effect</strong>: in winter, the temperature difference between warm indoor air and cold outdoor air creates suction at lower levels of the home, which pulls more soil gas (and radon) inside. In summer, the effect weakens.</p>
    <p>For a typical Colorado home:</p>
    <ul>
      <li><strong>Winter readings can be 30–50% higher</strong> than summer readings on the same home.</li>
      <li><strong>A short-term test in winter</strong> will read closer to your seasonal peak.</li>
      <li><strong>A short-term test in summer</strong> will read closer to your seasonal trough.</li>
      <li><strong>A long-term test</strong> averages both, giving you a more accurate picture of your annual exposure.</li>
    </ul>
    <p>EPA notes that the lung cancer risk from radon is cumulative — it depends on average exposure over years, not on the level during any single 2-day window.<sup><a href="#src-1">[1]</a></sup> A long-term test is closer to that average.</p>
  </div>
</section>

<section>
  <h2>When each test type is the right choice</h2>
  <div class="prose-wide">

    <h3>Use a short-term test when:</h3>
    <ul>
      <li>You've never tested before and want a quick first read.</li>
      <li>You're in a real estate transaction (though a professional continuous monitor is preferred).</li>
      <li>You need to confirm a previous test result quickly.</li>
      <li>You're running a post-mitigation test (per EPA, 2–7 days under closed-house conditions).<sup><a href="#src-2">[2]</a></sup></li>
      <li>Your previous reading was clearly high (10+ pCi/L) and you want to verify before mitigating.</li>
    </ul>

    <h3>Use a long-term test when:</h3>
    <ul>
      <li>Your short-term result was borderline (3.0–4.5 pCi/L) and you're not sure whether to mitigate.</li>
      <li>You want a defensible annual exposure picture (not under real-estate deadline pressure).</li>
      <li>You're tracking levels year-over-year in a home with previous high results.</li>
      <li>You want to capture a Colorado-specific seasonal average.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Stacking the two for a complete picture</h2>
  <div class="prose-wide">
    <p>Many Colorado homeowners use both:</p>
    <ol>
      <li><strong>Short-term first.</strong> Get the quick read. If it's clearly low (under 2.0) or clearly high (over 6.0), you have your answer.</li>
      <li><strong>Long-term follow-up</strong> when the short-term lands in the borderline zone. A 90-day or year-long test gives you the average that the short-term snapshot couldn't.</li>
      <li><strong>Short-term post-mitigation.</strong> After installing a system, a 2–7 day closed-house short-term test verifies the system worked. EPA explicitly recommends short-term for this purpose.<sup><a href="#src-2">[2]</a></sup></li>
    </ol>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — winter short-term reads high, summer long-term reads moderate</strong>
    <p>A homeowner in Stetson Hills tests in early February with a short-term kit. The result: 5.4 pCi/L — above the action level. Concerned but not panicked, they place a long-term alpha-track detector in the basement office where they spend most of their work day. Ninety days later (early May), the long-term test comes back at 3.1 pCi/L. The winter short-term captured the seasonal peak; the long-term captured the seasonal average. Both are real readings. The homeowner decides to mitigate, given the basement is daily living space and the borderline-zone-plus-winter-peak combination. The post-mitigation short-term test (closed-house, 48 hours) comes back at 0.9 pCi/L.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-2">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def short_vs_long_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Should I use a short-term or long-term radon test?",
             "acceptedAnswer": {"@type": "Answer", "text": "Use a short-term test (2-7 days) for a quick first read, real estate transactions, or post-mitigation verification. Use a long-term test (90+ days) for an accurate annual exposure picture, especially if a short-term result was borderline (3.0-4.5 pCi/L) or you want to capture Colorado's seasonal swings."}},
            {"@type": "Question", "name": "Why do my Colorado radon levels change between seasons?",
             "acceptedAnswer": {"@type": "Answer", "text": "The stack effect drives the change. In winter, warm indoor air rises and creates suction at lower levels, pulling more soil gas (and radon) inside. Winter readings in Colorado homes can be 30-50% higher than summer readings on the same home. A long-term test averages across seasons, giving a more accurate annual picture."}},
            {"@type": "Question", "name": "Can I trust a 2-day short-term test result?",
             "acceptedAnswer": {"@type": "Answer", "text": "A short-term test gives an accurate reading for the conditions during the test window — but those conditions can shift seasonally. If the result is clearly high or clearly low, no further short-term testing will change that. If it lands in the borderline zone (3.0-4.5 pCi/L), follow up with a long-term test for a more reliable annual average."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 3. /radon-testing/where-to-place-a-test/
# =========================================================================
TEST_PLACEMENT_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You ordered a kit. You opened the canister. Now where do you put it?</p>
    <p>This isn't a trick question — but it does have a right answer, and a wrong placement can make a 4.5 pCi/L home look like a 2.8 pCi/L home (or vice versa). The EPA and AARST have specific placement requirements; here's the plain-language version.</p>
  </div>
</section>

<section>
  <h2>The lowest livable level</h2>
  <div class="prose-wide">
    <p>The rule is: test in the lowest part of your home that you actually use. EPA defines this as the <strong>lowest livable level</strong>.<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li><strong>Finished basement that you use</strong> (TV room, office, gym, bedroom) — test here.</li>
      <li><strong>Unfinished basement that you walk through to do laundry</strong> — test here.</li>
      <li><strong>Unfinished crawlspace you don't enter</strong> — don't test here. Test the floor above it.</li>
      <li><strong>Slab-on-grade home (no basement)</strong> — test the ground floor.</li>
      <li><strong>Walk-out basement</strong> — test the basement, even if it has a daylight door.</li>
    </ul>
    <p>The idea is to measure radon where you actually breathe. A test in a sealed-off attic doesn't tell you much.</p>
  </div>
</section>

<section>
  <h2>Where in the room</h2>
  <div class="prose-wide">
    <p>Within the lowest livable level, EPA placement guidance is specific:<sup><a href="#src-1">[1]</a></sup></p>
    <ul class="checklist">
      <li><strong>2 to 6 feet above the floor.</strong> A shelf or table works. Don't put it on the floor; don't tape it to the ceiling.</li>
      <li><strong>At least 1 foot from exterior walls.</strong> Walls have small drafts.</li>
      <li><strong>At least 4 inches from any other surface</strong> (table edge, book, lamp).</li>
      <li><strong>Away from drafts</strong> — supply or return vents, ceiling fans, exterior doors, fireplaces.</li>
      <li><strong>Away from direct sunlight</strong> — heating affects readings.</li>
      <li><strong>Away from high humidity</strong> — bathrooms, kitchens, laundry rooms.</li>
      <li><strong>Not near electronic equipment</strong> that gives off heat (TV, computer, modem).</li>
    </ul>
    <p>A reading taped to the wall right above a heating vent will be different from a reading on a shelf in the middle of the room. That's not measurement error — it's measurement bias.</p>
  </div>
</section>

<section>
  <h2>Closed-house conditions</h2>
  <div class="prose-wide">
    <p>For short-term tests (2–7 days), the home should be under <strong>closed-house conditions</strong> for 12 hours before the test starts and the entire duration of the test.<sup><a href="#src-2">[2]</a></sup> Closed-house means:</p>
    <ul>
      <li>Windows and exterior doors closed except for normal in-and-out traffic.</li>
      <li>Whole-house fans not running.</li>
      <li>Window-mounted HVAC units running normally; window fans not running.</li>
      <li>Internal doors can be open or closed as usual — don't change the rest of your routine.</li>
    </ul>
    <p>The closed-house requirement doesn't apply to long-term tests (90+ days). Those average across normal living conditions over enough time that day-to-day variations cancel out.</p>
  </div>
</section>

<section>
  <h2>Common placement mistakes</h2>
  <div class="prose-wide">
    <p>Most homeowners get the basic placement right but trip on one of these:</p>
    <ul>
      <li><strong>Placing the test on the floor.</strong> The reading will be slightly higher than at breathing height. Use a shelf, table, or chair (2–6 feet up).</li>
      <li><strong>Placing in the laundry room.</strong> The humidity from the dryer and washer affects the reading. Use a different room.</li>
      <li><strong>Placing on an exterior windowsill.</strong> Drafts and proximity to outside air bias the reading.</li>
      <li><strong>Putting a short-term test in the master bedroom on the second floor.</strong> Test the lowest livable level, not the most-occupied room.</li>
      <li><strong>Running the test while windows are open.</strong> Closed-house conditions matter for short-term tests.</li>
      <li><strong>Moving the test mid-test.</strong> Don't.</li>
      <li><strong>Testing in a crawlspace.</strong> Test the floor above it — that's where you breathe.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Special cases</h2>
  <div class="prose-wide">

    <h3>Slab-on-grade homes</h3>
    <p>No basement, no crawlspace. Test the ground floor — but place the test in a room that gets daily use (living room, home office, bedroom) rather than a transient space like a foyer or laundry room.</p>

    <h3>Walk-out basements</h3>
    <p>The basement is still the lowest livable level even if it has a daylight door. Test the basement, with the daylight door closed for the closed-house duration.</p>

    <h3>Split-level homes</h3>
    <p>The lowest level used daily — typically a family room or office on the half-basement level — gets the test. If both half-basements are used (rare), test the lower one.</p>

    <h3>Tri-level homes</h3>
    <p>The lowest occupied level. Tri-levels often have a basement and a half-basement; test the basement.</p>

    <h3>Apartments / multi-family</h3>
    <p>The unit you actually live in. Ground-floor and basement apartments are higher priority than upper-floor units. EPA guidance for multi-family testing is largely the same as single-family within your own unit.</p>

    <h3>Multiple test locations</h3>
    <p>If your home has multiple foundation zones (basement + crawlspace under different parts), professional measurements may test each zone separately. For a homeowner kit, test the lowest livable level where you spend the most time.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Citizen's Guide to Radon</em>. <a href="{s('epa_citizens_guide')}" rel="noopener" target="_blank">epa.gov/radon/citizens-guide-radon</a></li>
    <li id="src-2">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def test_placement_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Where should I place a radon test kit?",
             "acceptedAnswer": {"@type": "Answer", "text": "Place it in the lowest livable level of your home — finished basement, walk-out basement, or ground floor of a slab home. Within the room: 2-6 feet above the floor, at least 1 foot from exterior walls, away from drafts (vents, fireplaces, doors), direct sunlight, humidity (bathrooms, kitchens, laundry), and heat-generating electronics."}},
            {"@type": "Question", "name": "What are closed-house conditions for a radon test?",
             "acceptedAnswer": {"@type": "Answer", "text": "For short-term tests (2-7 days), keep windows and exterior doors closed for 12 hours before the test starts and the entire test duration. Normal in-and-out traffic is fine. Whole-house and window fans should not run. Closed-house conditions don't apply to long-term tests (90+ days)."}},
            {"@type": "Question", "name": "Should I test my crawlspace for radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No — test the floor above the crawlspace. EPA placement guidance is to test where you actually breathe (the lowest livable level), not in the crawlspace itself. If your home is over a crawlspace, that crawlspace can be a radon source, but the test goes in the room above."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 4. /radon-testing/during-real-estate-transactions/
# =========================================================================
TESTING_REAL_ESTATE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Testing during a Colorado real estate transaction follows different rules than testing your own home. The result has to be defensible to a buyer's lender, the seller, and potentially an attorney. The method matters more, the tester's credentials matter more, and Colorado has a specific disclosure law that controls what the seller has to share.</p>
    <p>This page walks through SB23-206 (Colorado's mandatory radon disclosure law), the test methodology that's standard for real estate, who can place a test, how the inspection objection process works, and what happens when the result comes back high.</p>
  </div>
</section>

<section>
  <h2>Colorado SB23-206 — the disclosure law</h2>
  <div class="prose-wide">
    <p>Effective <strong>August 7, 2023</strong>, Colorado law (SB23-206, codified at <strong>CRS § 38-35.7-112</strong>) requires sellers of residential property to provide buyers with:<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li>Any known prior radon test results for the property.</li>
      <li>Documentation of any radon mitigation work that has been performed.</li>
      <li>The CDPHE radon brochure.</li>
    </ul>
    <p>The law applies to <strong>both sales and residential leases</strong>. It does not require sellers to test or mitigate — only to disclose what they already know. The disclosure is delivered through the Seller's Property Disclosure form (revised by the Colorado Real Estate Commission post-SB23-206).<sup><a href="#src-2">[2]</a></sup></p>
    <p>What this means in practice:</p>
    <ul>
      <li>If the seller had a prior test, you should see the result in the SPD form before you go under contract.</li>
      <li>If the seller had mitigation done, you should have the system documentation and post-mitigation test result.</li>
      <li>If you discover elevated radon during inspection that wasn't disclosed, and the seller knew about a prior test, that's a fact pattern worth showing your real estate attorney.</li>
      <li>If you mitigate after closing, the system becomes <em>your</em> required disclosure when you eventually sell.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The test method real estate uses</h2>
  <div class="prose-wide">
    <p>Real-estate testing almost always uses a <strong>professional continuous radon monitor</strong> (CRM) placed by a DORA-licensed, NRPP or NRSB certified tester.<sup><a href="#src-3">[3]</a></sup> The reasons:</p>
    <ul>
      <li><strong>Defensibility.</strong> The result must hold up if the seller, buyer, or lender disputes it. CRMs record hourly readings, time-stamp the data, and produce a written report on lab letterhead.</li>
      <li><strong>Anti-tampering.</strong> CRMs detect closed-house violations and movement. If a window is opened during the test or the monitor is moved, the hourly data shows it.</li>
      <li><strong>Speed.</strong> CRMs typically run for 48 hours and produce results in 48–72 hours total. That fits a standard Colorado inspection objection window.</li>
      <li><strong>Standard professional practice.</strong> The Colorado Association of Realtors and Pikes Peak Association of Realtors treat CRM results as the standard.</li>
    </ul>
    <p>Cost: $150–$300 in Colorado Springs. Usually paid by the buyer as part of inspection costs, though it can be negotiated.</p>
  </div>
</section>

<section>
  <h2>Who can place a real estate test in Colorado</h2>
  <div class="prose-wide">
    <p>Colorado is one of the few states with state-level radon professional licensing. To place a real-estate-grade radon test in Colorado, the tester must:</p>
    <ul class="checklist">
      <li>Hold a current <strong>DORA radon measurement license</strong> (Office of Radon Professionals, 4 CCR 754-1).<sup><a href="#src-3">[3]</a></sup></li>
      <li>Hold a current <strong>NRPP or NRSB measurement certification</strong>.<sup><a href="#src-4">[4]</a></sup></li>
      <li>Use an EPA-listed or AARST-certified continuous radon monitor.</li>
      <li>Follow AARST measurement standards (MAH or MS-MAH for residential).</li>
    </ul>
    <p>Many Colorado home inspectors are also licensed radon testers — the credentials stack. If your inspector isn't a licensed tester, they should refer to one. Don't accept a real estate radon test from anyone who can't provide both DORA and NRPP/NRSB credentials.</p>
  </div>
</section>

<section>
  <h2>The inspection objection workflow</h2>
  <div class="prose-wide">
    <p>A typical Colorado real estate timeline for radon:</p>
    <table class="compact">
      <thead>
        <tr><th>Day</th><th>What happens</th></tr>
      </thead>
      <tbody>
        <tr><td>0</td><td>Offer accepted, contract signed</td></tr>
        <tr><td>1–3</td><td>Inspection scheduled; radon test placed during inspection</td></tr>
        <tr><td>3–5</td><td>Test retrieved (48-hour CRM)</td></tr>
        <tr><td>5–7</td><td>Test result returned</td></tr>
        <tr><td>By inspection objection deadline (typically 5–10 days after contract)</td><td>Buyer submits inspection objection if result is above 4.0 pCi/L</td></tr>
        <tr><td>3 days after objection</td><td>Seller's response deadline (typical)</td></tr>
        <tr><td>By inspection resolution deadline</td><td>Buyer and seller agree on resolution or buyer terminates</td></tr>
        <tr><td>Closing day</td><td>Mitigation complete OR credit applied OR contract terminated</td></tr>
      </tbody>
    </table>
    <p>The buyer's options under the inspection objection are covered on the <a href="/radon-mitigation-cost/real-estate-deadlines/">real-estate-deadlines cost page</a>.</p>
  </div>
</section>

<section>
  <h2>What if the seller already mitigated?</h2>
  <div class="prose-wide">
    <p>If the seller's disclosure shows a prior mitigation system, the buyer should verify a few things before relying on it:</p>
    <ul>
      <li><strong>Post-mitigation test result.</strong> What was the system's verified outcome? It should be below 4.0 pCi/L.</li>
      <li><strong>System age.</strong> Fans typically last 5+ years. A 10-year-old fan may be nearing replacement.</li>
      <li><strong>Manometer condition.</strong> Look at the system. The manometer columns should be at different levels (system pulling vacuum). If they're equal, the fan isn't running.</li>
      <li><strong>System documentation.</strong> The seller should have the contractor's invoice, system certification, DORA license info, and post-mit test result.</li>
      <li><strong>Re-test the home.</strong> Run a current short-term test during the inspection period to confirm the existing system is still bringing levels below 4.0 pCi/L.</li>
    </ul>
  </div>
</section>

<section>
  <h2>What if the seller's disclosure says "no known test"?</h2>
  <div class="prose-wide">
    <p>Most Colorado sellers honestly haven't tested. In that case the disclosure says "no known test result." The buyer's typical move:</p>
    <ol>
      <li>Include a radon test in the inspection (most Colorado home inspectors offer this as an add-on).</li>
      <li>If the result is above 4.0 pCi/L, file an inspection objection and proceed through the buyer-options process.</li>
      <li>If the result is below 4.0 pCi/L but above 2.0, decide whether to ask for a credit anyway (some buyers do; this is a negotiation issue, not a legal one).</li>
      <li>If the result is below 2.0 pCi/L, the home is fine for now. Plan to retest every 2 years after closing.</li>
    </ol>
  </div>
</section>

<section>
  <h2>Tampering and validity controls</h2>
  <div class="prose-wide">
    <p>CRMs include tamper detection because real estate testing has a long history of attempts (usually by sellers) to bias the result. Common signs the tester will flag:</p>
    <ul>
      <li>Hourly data shows a sudden drop coinciding with window operation.</li>
      <li>Sustained spikes that look like the test was moved closer to a soil-gas source.</li>
      <li>Temperature or humidity changes inconsistent with normal home conditions.</li>
      <li>Motion-detected disturbance of the monitor.</li>
    </ul>
    <p>A flagged test should be re-run. The cost of the second test is typically the seller's if tampering is documented; it's the buyer's otherwise.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — under contract, no prior disclosure, inspection result 6.5 pCi/L</strong>
    <p>A buyer under contract on a 1990s tri-level in Stetson Hills. The seller's SPD form said "no known prior test." The buyer's inspector also placed a 48-hour CRM during the inspection. Result: 6.5 pCi/L. With 5 days remaining on the inspection objection deadline, the buyer filed an objection requesting a $3,000 seller credit at closing (anchored on the four-scenario framework — tri-level means multi-zone, $2,200–$4,800 band). The seller agreed. After closing, the buyer hired a DORA-licensed contractor, who ran a PFE diagnostic and installed a two-suction-point system for $2,650. Post-mitigation test came in at 1.8 pCi/L. The buyer's documentation now lives in the home folder; when they sell, it becomes part of <em>their</em> SB23-206 disclosure.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado General Assembly. <em>SB23-206 (CRS § 38-35.7-112)</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
    <li id="src-2">Colorado Division of Real Estate. <em>Real Estate Commission Forms</em>. <a href="{s('crec_spd')}" rel="noopener" target="_blank">dre.colorado.gov/division-real-estate-commission-forms</a></li>
    <li id="src-3">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
    <li id="src-4">National Radon Proficiency Program / National Radon Safety Board. <a href="{s('nrpp')}" rel="noopener" target="_blank">nrpp.info</a> · <a href="{s('nrsb')}" rel="noopener" target="_blank">nrsb.org</a></li>
  </ol>
</aside>
"""


def testing_real_estate_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Does Colorado require radon disclosure when selling a home?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Colorado SB23-206 (CRS § 38-35.7-112), effective August 7, 2023, requires sellers of residential property to disclose any known prior radon test results, any mitigation work performed, and to provide the CDPHE radon brochure. The disclosure applies to both sales and residential leases. Colorado does not require sellers to test or mitigate — only to disclose what they already know."}},
            {"@type": "Question", "name": "What kind of radon test is used during a Colorado real estate transaction?",
             "acceptedAnswer": {"@type": "Answer", "text": "A professional continuous radon monitor (CRM) placed by a DORA-licensed, NRPP or NRSB certified tester. CRMs record hourly readings, detect tampering, and produce defensible written results in 48-72 hours. Cost in Colorado Springs is typically $150-$300, usually paid by the buyer as an inspection add-on."}},
            {"@type": "Question", "name": "Who can perform a real estate radon test in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "The tester must hold a current DORA radon measurement license (Office of Radon Professionals) and a current NRPP or NRSB measurement certification. Many Colorado home inspectors are also licensed radon testers. Don't accept a real estate radon test from anyone who can't provide both credentials."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 5. /radon-testing/for-rentals/
# =========================================================================
TESTING_RENTALS_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Colorado SB23-206 extends radon disclosure obligations to residential leases — not just sales. That's a change most landlords and tenants haven't fully internalized yet. This page walks through what landlords must disclose, what tenants can do if they're concerned, and where mitigation responsibility lands.</p>
    <p>This is general information, not legal advice. For specific situations, especially landlord-tenant disputes, consult a Colorado real estate attorney.</p>
  </div>
</section>

<section>
  <h2>What SB23-206 requires of Colorado landlords</h2>
  <div class="prose-wide">
    <p>Since <strong>August 7, 2023</strong>, residential landlords in Colorado must:<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li>Disclose any <strong>known prior radon test results</strong> for the property in the lease or as a pre-lease disclosure.</li>
      <li>Disclose any <strong>radon mitigation</strong> work that has been performed.</li>
      <li>Provide the <strong>CDPHE radon brochure</strong> to the tenant.</li>
    </ul>
    <p>The law applies to landlords of any residential property — single-family rentals, condos, apartment units, and multi-family buildings. As with home sales, the law requires disclosure of what is known; it does not require testing or mitigation.</p>
  </div>
</section>

<section>
  <h2>What Colorado landlords are NOT required to do (yet)</h2>
  <div class="prose-wide">
    <p>SB23-206 stops short of imposing a duty to test or mitigate. Specifically:</p>
    <ul>
      <li>Landlords are <strong>not required to test</strong> rental properties for radon before listing.</li>
      <li>Landlords are <strong>not required to mitigate</strong> even if a test shows elevated levels.</li>
      <li>Existing leases (signed before August 7, 2023) are not retroactively affected by the disclosure rule.</li>
    </ul>
    <p>However: the practical reality of disclosure means landlords who know about elevated radon and don't address it may face friction from prospective tenants, lower rental rates, or attorney-led tenant inquiries if a health issue later arises. Many Colorado landlords have started testing rentals proactively because the disclosure burden makes "I didn't know" a less defensible position.</p>
  </div>
</section>

<section>
  <h2>What tenants can do</h2>
  <div class="prose-wide">

    <h3>Before signing a lease</h3>
    <p>Read the disclosure. If the landlord checked "yes" to a prior radon test, ask for the actual test result. If they checked "yes" to mitigation, ask for the system documentation and post-mitigation test result. If they checked "no known test," that's the standard answer — and you can decide whether to test the unit yourself.</p>

    <h3>During tenancy</h3>
    <p>Tenants have the right to test their own unit at any time. A short-term DIY kit ($15–$40) is the easiest path; placement follows the standard EPA guidance (<a href="/radon-testing/where-to-place-a-test/">where to place a test &rarr;</a>). If you find elevated levels:</p>
    <ol>
      <li>Document the result in writing to the landlord, ideally with a copy of the lab report.</li>
      <li>Reference the CDPHE radon brochure (which they should have provided at lease signing).</li>
      <li>Request mitigation in writing. The landlord is not legally obligated to mitigate, but many will — particularly if you've signed a long-term lease.</li>
      <li>If the landlord refuses, your options depend on lease terms. Consult a Colorado tenant rights attorney for specifics.</li>
    </ol>

    <h3>Multi-unit buildings</h3>
    <p>If you live in an apartment, radon levels can vary by unit. Ground-floor and basement units typically have higher levels than upper-floor units, but radon can rise through buildings via shared shafts and stairwells. A test in your own unit is the only definitive answer.</p>
  </div>
</section>

<section>
  <h2>What landlords should know about testing rentals</h2>
  <div class="prose-wide">
    <p>For Colorado landlords, treating radon testing as a standard pre-lease item — like a smoke detector check — is increasingly common:</p>
    <ul>
      <li>The disclosure requirement now exists. "I didn't test, so I had nothing to disclose" is a less defensible position than "I tested and disclosed the result."</li>
      <li>Test cost is modest. A short-term test costs $15–$40; a long-term test costs $30–$60. Either is well under one month's rent.</li>
      <li>If the test result is high, you're not legally required to mitigate — but you are required to disclose. Most Colorado landlords in this position mitigate because the disclosure makes the unit harder to rent without mitigation.</li>
      <li>If you do mitigate, the system documentation and post-mit test result transfer with the property and become part of every future disclosure.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Where mitigation costs land for rental properties</h2>
  <div class="prose-wide">
    <p>Mitigation costs are the same for rentals as for owner-occupied homes — the system is the same. Colorado Springs cost bands:</p>
    <ul>
      <li>Basic basement (single-family rental): $900–$1,900</li>
      <li>Finished basement: $1,400–$2,800</li>
      <li>Crawlspace: $1,800–$4,000</li>
      <li>Multi-zone or duplex: $2,200–$4,800</li>
    </ul>
    <p>For multi-family buildings (apartments, condos), commercial AARST standards apply (SGM-MFLB-2023), and costs scale with the building's size. <a href="/radon-mitigation-cost/">Full cost breakdown &rarr;</a></p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a tenant in a Springs Ranch garden-level apartment</strong>
    <p>A tenant in a garden-level (basement) apartment in Springs Ranch tested with a $20 short-term kit. Result: 5.9 pCi/L. They emailed the landlord with a copy of the lab report, referenced the CDPHE radon brochure provided at lease signing, and requested mitigation. The landlord (who had not tested the unit before) ran a confirming long-term test for 90 days. Result: 4.8 pCi/L. The landlord then hired a DORA-licensed contractor to install a sub-slab system serving the garden-level unit ($2,100). Post-mit test came back at 1.4 pCi/L. The mitigation documentation is now part of the property's required disclosure for all future leases and any eventual sale.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado General Assembly. <em>SB23-206 (CRS § 38-35.7-112)</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>

<p style="font-size:.85rem;color:var(--text-muted);">This page is general information, not legal advice. For specific situations, consult a Colorado real estate or tenant rights attorney.</p>
"""


def testing_rentals_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Do Colorado landlords have to test rentals for radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Colorado SB23-206 requires landlords to disclose any known prior radon test results and any mitigation work, plus provide the CDPHE radon brochure to tenants. It does not require testing or mitigation. Many landlords now test proactively because the disclosure burden makes 'I didn't know' a less defensible position."}},
            {"@type": "Question", "name": "Can a tenant test their own apartment for radon in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Tenants can test their own unit at any time. A short-term DIY kit costs $15-$40 and follows the same EPA placement guidance as homeowner testing. If the result is elevated, document it in writing to the landlord and request mitigation, referencing the CDPHE radon brochure provided at lease signing."}},
            {"@type": "Question", "name": "Is my landlord required to mitigate radon if I test high?",
             "acceptedAnswer": {"@type": "Answer", "text": "Not under Colorado law as written — SB23-206 requires disclosure, not mitigation. However, the disclosure requirement means landlords with elevated test results have to share that with all future tenants, which often motivates voluntary mitigation. For specific situations, consult a Colorado tenant rights attorney."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 6. /radon-testing/for-businesses/
# =========================================================================
TESTING_BUSINESSES_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you own or operate a commercial building in Colorado — office, retail, light industrial, healthcare, daycare, school — radon testing is a different conversation than a homeowner test. The buildings are larger, employees and visitors spend longer hours in them, the regulatory framework is more specific (especially for schools and childcare), and the testing methodology shifts accordingly.</p>
    <p>This page covers the basics for commercial Colorado property owners and operators: when to test, what standards apply, who's required to test, and what mitigation looks like at commercial scale.</p>
  </div>
</section>

<section>
  <h2>Workplace exposure context</h2>
  <div class="prose-wide">
    <p>EPA's 4.0 pCi/L action level was set for residential homes, where occupants spend the most time. Commercial workplaces have different exposure patterns:</p>
    <ul>
      <li><strong>Office workers</strong> spend 40+ hours per week in a single building.</li>
      <li><strong>Retail employees</strong> often work shifts in basement-level stockrooms.</li>
      <li><strong>Healthcare facilities</strong> have patients with vulnerable lung health.</li>
      <li><strong>Daycares and schools</strong> have children — for whom radon risk is a particular concern (higher respiration rates, developing lungs).</li>
    </ul>
    <p>OSHA does not have a specific radon limit for workplaces (the closest analog is the radiation exposure limit for "general industry," which is far higher than typical home radon levels and rarely relevant). EPA's 4.0 pCi/L is the de facto standard.</p>
  </div>
</section>

<section>
  <h2>Commercial testing protocols</h2>
  <div class="prose-wide">
    <p>For larger commercial buildings, testing follows the <strong>ANSI/AARST MAH</strong> (Measurement Protocols for Long-Term Devices) and <strong>SGM-MFLB-2023</strong> standards.<sup><a href="#src-1">[1]</a></sup> Key differences from residential:</p>
    <ul>
      <li><strong>More tests per building.</strong> AARST protocols call for testing in roughly 10–30% of habitable spaces in a commercial building, depending on building size and use.</li>
      <li><strong>Lowest occupied level.</strong> Same principle as homes — basements and ground floors first.</li>
      <li><strong>Long-term tests preferred.</strong> For initial assessment and post-mitigation verification.</li>
      <li><strong>HVAC awareness.</strong> Commercial HVAC systems can mask or dilute radon. Tests should be placed under representative HVAC operation.</li>
      <li><strong>Licensed measurement.</strong> Same DORA + NRPP/NRSB credentials required for testers, plus AARST certification for commercial measurement.</li>
    </ul>
    <p>Commercial testing typically runs $200–$500 per building for a small property, scaling up with building size.</p>
  </div>
</section>

<section>
  <h2>Special rules for Colorado schools</h2>
  <div class="prose-wide">
    <p>Schools occupy a special category in radon policy. Colorado follows EPA recommendations for school radon testing:<sup><a href="#src-2">[2]</a></sup></p>
    <ul>
      <li>Every <strong>frequently occupied room</strong> in contact with the ground (including ground floor and basement classrooms, gyms, libraries, cafeterias, offices) should be tested.</li>
      <li>Initial testing should use a long-term measurement, or two consecutive short-term measurements.</li>
      <li>Action level of 4.0 pCi/L applies.</li>
      <li>The school district is responsible for testing decisions; CDPHE provides guidance.</li>
    </ul>
    <p>Colorado does not have a state law requiring school radon testing, but EPA strongly recommends it. Many Colorado school districts have testing programs in place.</p>
  </div>
</section>

<section>
  <h2>Childcare facilities and licensed daycares</h2>
  <div class="prose-wide">
    <p>Childcare facilities licensed in Colorado are regulated by the Colorado Department of Early Childhood. Radon testing isn't currently a licensing requirement, but:</p>
    <ul>
      <li>EPA recommends radon testing in childcare facilities given child vulnerability to radon exposure.</li>
      <li>Many Colorado childcare facilities test voluntarily.</li>
      <li>Liability considerations: a daycare in a building with known elevated radon faces meaningful exposure risk if a child later develops radon-related lung disease.</li>
    </ul>
    <p>Childcare operators in Colorado are well-advised to test annually or biennially, document results, and mitigate if levels exceed 4.0 pCi/L.</p>
  </div>
</section>

<section>
  <h2>Multi-tenant commercial buildings</h2>
  <div class="prose-wide">
    <p>For office buildings, retail centers, and other multi-tenant commercial properties:</p>
    <ul>
      <li>The <strong>property owner or building manager</strong> typically arranges testing for common areas.</li>
      <li><strong>Individual tenants</strong> can request testing for their leased spaces; tenant rights vary by lease terms.</li>
      <li>Testing follows AARST SGM-MFLB-2023 standards for the building scale.</li>
      <li>Mitigation responsibility usually rests with the property owner unless the lease assigns it to the tenant (uncommon).</li>
    </ul>
  </div>
</section>

<section>
  <h2>What commercial mitigation looks like</h2>
  <div class="prose-wide">
    <p>Commercial mitigation uses the same principles as residential — sub-slab depressurization, sub-membrane for crawlspaces — but at building scale. Practical differences:</p>
    <ul>
      <li><strong>Multiple suction points</strong> are the norm. A 10,000 sq ft building typically needs 4–8 suction points.</li>
      <li><strong>Larger fans or multiple fans</strong> — often industrial-grade equipment rather than residential RadonAway/Fantech models.</li>
      <li><strong>HVAC integration.</strong> Commercial HVAC affects building pressure; mitigation system design accounts for it.</li>
      <li><strong>Building permits.</strong> Commercial mitigation work requires standard commercial building permits in Colorado Springs through Pikes Peak Regional Building Department.</li>
      <li><strong>Cost.</strong> Commercial mitigation typically starts at $4,000–$8,000 for small buildings (under 5,000 sq ft) and scales up to tens of thousands for larger facilities.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Practical timeline for a commercial test</h2>
  <div class="prose-wide">
    <ol>
      <li><strong>Hire a DORA-licensed, AARST-certified measurement professional</strong> for commercial radon testing.</li>
      <li><strong>Walkthrough and test plan.</strong> They identify the rooms to test and plan placement.</li>
      <li><strong>Long-term measurement</strong> over 90+ days (or 2 short-term measurements 1–2 weeks each).</li>
      <li><strong>Report and review.</strong> Result interpreted against EPA 4.0 pCi/L action level.</li>
      <li><strong>If above 4.0 pCi/L:</strong> mitigation design begins. For larger buildings, expect a 2–4 month timeline from test completion to system commissioning.</li>
    </ol>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">ANSI/AARST SGM-MFLB-2023 (Multi-Family and Low-Rise Buildings). <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
    <li id="src-2">U.S. EPA. <em>Radon in Schools</em>. <a href="{s('epa_radon_in_schools')}" rel="noopener" target="_blank">epa.gov/radon/radon-schools</a></li>
  </ol>
</aside>
"""


def testing_businesses_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Do Colorado businesses need to test for radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "Colorado does not have a state law requiring commercial radon testing, but EPA strongly recommends it — especially for schools, childcare facilities, and ground-level workplaces. OSHA does not have a specific workplace radon limit, so EPA's 4.0 pCi/L is the de facto standard. Larger commercial buildings follow ANSI/AARST SGM-MFLB-2023 testing protocols."}},
            {"@type": "Question", "name": "How much does commercial radon testing cost in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Commercial radon testing typically runs $200-$500 for small properties, scaling up with building size. Testing requires a DORA-licensed, NRPP or NRSB certified measurement professional, ideally with AARST commercial measurement certification. Tests follow AARST protocols that call for 10-30% of habitable spaces to be tested depending on building use."}},
            {"@type": "Question", "name": "Does Colorado require schools to test for radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "Colorado does not have a state law requiring school radon testing, but EPA strongly recommends testing every frequently-occupied ground-level room in K-12 schools. CDPHE provides guidance, and many Colorado school districts have voluntary testing programs in place. Childcare facilities are similarly encouraged but not legally required to test."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
