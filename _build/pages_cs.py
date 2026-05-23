"""Content for the three Colorado Springs guide pages: cost, testing, failed-test."""
import json
from pages_main import s, SOURCES


# =========================================================================
# COLORADO SPRINGS — MITIGATION COST
# =========================================================================
CS_COST_BODY = f"""
<section>
  <div class="prose-wide">
    <p>The short answer most Colorado Springs homeowners want: a typical radon mitigation system in Colorado runs <strong>$1,000–$2,000</strong>. That's the baseline range both <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE</a> and <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health</a> use for a standard single-family install.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
    <p>The longer answer is that a quote on your house can land anywhere from $1,000 to $3,000+ depending on foundation type, system layout, and access. This page walks through what's in a normal quote, what moves the price up or down, and how to tell a fair bid from one that's padded.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="factbox">
      <div class="label">Baseline (Colorado)</div>
      <div class="stat">$1,000–$2,000</div>
      <div class="source">CDPHE typical mitigation range. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">Source</a></div>
    </div>
    <div class="factbox">
      <div class="label">El Paso County</div>
      <div class="stat">$1,000–$2,000</div>
      <div class="source">Local public-health baseline. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">Source</a></div>
    </div>
    <div class="factbox">
      <div class="label">Reduction</div>
      <div class="stat">80–99%</div>
      <div class="source">EPA cites this radon reduction for properly designed systems. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">Source</a></div>
    </div>
  </div>
</section>

<section>
  <h2>What a standard Colorado Springs mitigation quote includes</h2>
  <div class="prose-wide">
    <p>A complete mitigation system isn't just a fan and a pipe. A licensed Colorado Springs contractor's quote should spell out each of these line items in writing:</p>
    <ul class="checklist">
      <li><strong>Suction point(s)</strong> — typically one core drilled through the slab; larger or split foundations may need two or more.</li>
      <li><strong>Sealing</strong> — sealing of slab cracks, sump pit lids, plumbing penetrations, and floor-wall joints to make depressurization effective.</li>
      <li><strong>Vent piping</strong> — 3- or 4-inch sealed PVC routed from the suction point through the home and exhausting above the roofline (or up an exterior wall and above the eave, per EPA standards).</li>
      <li><strong>Fan</strong> — a quiet inline radon fan sized for your system. Reputable manufacturers (e.g., Fantech, RadonAway) carry 5–10 year warranties.</li>
      <li><strong>System monitor (manometer)</strong> — a simple U-tube gauge that lets you confirm the fan is pulling vacuum at a glance.</li>
      <li><strong>Electrical</strong> — a dedicated outlet near the fan, on a circuit a licensed electrician has installed or signed off.</li>
      <li><strong>Permit and inspection</strong> — Colorado Springs and El Paso County may require mechanical/electrical permits; your contractor should pull them.</li>
      <li><strong>Post-installation test</strong> — a 48-hour confirmation test to verify the system actually brought your level below 4.0 pCi/L.</li>
      <li><strong>Warranty</strong> — written workmanship warranty plus the manufacturer fan warranty.</li>
    </ul>
    <p>If any of these are missing from the written quote, ask. A line missing on the page is a line missing in the install.</p>
  </div>
</section>

<section>
  <h2>What moves the price up or down</h2>
  <div class="prose-wide">
    <p>Two homes on the same street can get genuinely different mitigation quotes. The big drivers:</p>

    <h3>Foundation type</h3>
    <p>Slab-on-grade with no basement is generally the simplest install. A standard sub-slab system from a single suction point may land at the lower end of the range. Full basements add piping length and often a sealed sump pit. <strong>Crawl spaces</strong> typically need a sealed vapor barrier across the entire floor before depressurization can work, which adds material and labor.</p>

    <h3>Home size and layout</h3>
    <p>Larger footprints, especially split-level or multi-foundation homes, may need <strong>multiple suction points</strong> and longer pipe runs. Each extra suction point adds work, sealing, and sometimes a second fan.</p>

    <h3>Soil and sub-slab conditions</h3>
    <p>If the soil under your slab is dense or rocky, the fan has to pull harder to depressurize it, which can mean a larger fan or additional suction points. Wet sub-slab conditions can require drainage modifications first.</p>

    <h3>Routing and aesthetics</h3>
    <p>An exterior install (fan on outside wall, pipe up the side of the house) is usually faster and cheaper than running the entire pipe interior, through closets and the attic, to discharge above the roof. Finished basements often need interior routing for aesthetics, which costs more.</p>

    <h3>Sump pits, drain tile, and existing rough-ins</h3>
    <p>Many newer Colorado Springs homes were built with a passive radon rough-in (a capped vent stub). If your home has one, conversion to an active system is significantly cheaper because the piping is already in place.<sup><a href="#src-3">[3]</a></sup></p>

    <h3>Permit and electrical</h3>
    <p>Some homes need a new dedicated circuit for the fan. If the electrical work is straightforward, this is minor. If your panel is full or needs an upgrade, electrical can become its own line item.</p>
  </div>
</section>

<section>
  <h2>Typical Colorado Springs cost ranges by scenario</h2>
  <div class="prose-wide">
    <p>Use this table as an orientation, not a contractor quote. CDPHE's baseline is $1,000–$2,000 for a typical system; complex configurations and crawl spaces push past that.<sup><a href="#src-1">[1]</a></sup></p>
    <table>
      <thead>
        <tr><th>Scenario</th><th>Typical range</th><th>What drives it</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Slab-on-grade, single suction point, exterior fan, passive rough-in</td>
          <td>$800–$1,300</td>
          <td>Existing rough-in saves labor and material</td>
        </tr>
        <tr>
          <td>Basement, single suction point, exterior fan, no rough-in</td>
          <td>$1,000–$1,800</td>
          <td>The Colorado baseline scenario</td>
        </tr>
        <tr>
          <td>Multi-level basement / finished basement, interior routing</td>
          <td>$1,500–$2,500</td>
          <td>Interior pipe runs, drywall and aesthetic work</td>
        </tr>
        <tr>
          <td>Crawl space, sealed vapor barrier required</td>
          <td>$1,800–$3,000+</td>
          <td>Barrier material, sealing, more labor</td>
        </tr>
        <tr>
          <td>Multi-foundation home or unusual layout, multiple suction points</td>
          <td>$2,500–$4,000+</td>
          <td>More piping, possibly more than one fan</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Why one quote is $1,500 and another is $5,000</h2>
  <div class="prose-wide">
    <p>This question shows up in Colorado Reddit threads constantly. Both numbers can be legitimate for the same house — or one can be padded. A few honest reasons quotes vary:</p>
    <ul>
      <li><strong>Different scope.</strong> One contractor priced a single suction point with exterior routing; the other priced two suction points with interior routing and finished-basement repair.</li>
      <li><strong>Different fan and warranty.</strong> Premium fans with longer warranties cost more.</li>
      <li><strong>Different testing.</strong> The lower bid may not include a post-install test (it should).</li>
      <li><strong>Crawl-space scope.</strong> One quote includes sealed vapor barrier work; the other doesn't.</li>
      <li><strong>Permit handling.</strong> One contractor pulls and includes the permit; the other leaves it to you.</li>
    </ul>
    <p>And reasons that should make you pause:</p>
    <ul>
      <li>The quote is a flat number with no scope description.</li>
      <li>The contractor cannot provide an NRPP or NRSB number and Colorado DORA registration on request.<sup><a href="#src-4">[4]</a></sup></li>
      <li>The price is suspiciously low and the quote omits a post-installation test.</li>
      <li>The contractor uses fear-based pressure (one-day-only pricing, "your family is at risk").</li>
    </ul>
    <p>If you are looking at very different quotes, ask each contractor to send you the same written scope and re-price against it.</p>
  </div>
</section>

<section>
  <h2>Testing costs are separate from mitigation</h2>
  <div class="prose-wide">
    <p>A short-term DIY kit at retail typically costs $15–$40 including lab analysis. El Paso County Public Health sells kits at its lab. A professional measurement (the kind used in real estate transactions) typically runs <strong>$150–$300</strong>, depending on whether it's a same-visit continuous monitor or a placed-and-retrieved canister.<sup><a href="#src-2">[2]</a></sup></p>
    <p>Read the full <a href="/colorado-springs/radon-testing/">radon testing guide</a> for what kind of test to use when.</p>
  </div>
</section>

<section>
  <h2>The honest answer on DIY mitigation</h2>
  <div class="prose-wide">
    <div class="callout">
      <strong>Don't.</strong>
      <p>Mitigation looks like a fan and a pipe; it isn't. A correctly designed system depressurizes the entire sub-slab, exhausts above the roofline per EPA guidance, accounts for back-drafting and combustion safety, and is verified with a post-install test. CDPHE specifically warns that sealing cracks alone is unreliable and can sometimes make levels worse.<sup><a href="#src-1">[1]</a></sup></p>
    </div>
    <p>If budget is the issue, ask multiple licensed contractors for written quotes and check CDPHE's <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">low-income mitigation assistance program</a>.<sup><a href="#src-1">[1]</a></sup> Underspending on a system that doesn't actually reduce radon costs more than getting it right the first time.</p>
  </div>
</section>

<section>
  <h2>Ongoing operating cost</h2>
  <div class="prose-wide">
    <p>A typical radon fan draws roughly 50–90 watts. At Colorado Springs electricity rates that's on the order of <strong>$5–$15 per month</strong> in electricity. The fan itself is the only maintenance item: most manufacturers rate them for 5–10 years before replacement, and replacement runs $150–$400 plus labor.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-3">U.S. EPA. <em>Radon</em>. <a href="{s('epa_radon')}" rel="noopener" target="_blank">epa.gov/radon</a></li>
    <li id="src-4">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
  </ol>
</aside>
"""


def cs_cost_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How much does radon mitigation cost in Colorado Springs?",
             "acceptedAnswer": {"@type": "Answer", "text": "CDPHE and El Paso County Public Health both put a typical Colorado mitigation system at $1,000 to $2,000. Crawl spaces, multi-foundation homes, and multiple suction points push higher."}},
            {"@type": "Question", "name": "Why are radon quotes so different?",
             "acceptedAnswer": {"@type": "Answer", "text": "Quotes vary because scope varies — number of suction points, fan model, sealing, routing (interior vs. exterior), and whether a post-installation test and permit are included. Always compare scope, not just price."}},
            {"@type": "Question", "name": "Does a radon system add to my electricity bill?",
             "acceptedAnswer": {"@type": "Answer", "text": "A typical radon fan draws 50–90 watts, which is roughly $5–$15 per month on Colorado Springs electricity rates."}},
            {"@type": "Question", "name": "Can I install radon mitigation myself?",
             "acceptedAnswer": {"@type": "Answer", "text": "It is not recommended. A properly designed system requires sub-slab depressurization, sealing, exhaust above the roofline per EPA guidance, and a verified post-installation test. CDPHE warns that sealing alone can sometimes make radon levels worse."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# COLORADO SPRINGS — TESTING
# =========================================================================
CS_TESTING_BODY = f"""
<section>
  <div class="prose-wide">
    <p>You cannot smell, see, or feel radon. The only way to know whether your Colorado Springs home is above the EPA action level of 4.0 pCi/L is to test. Given that more than 40% of homes tested in El Paso County between 2005 and 2023 came back high, testing isn't optional — it's the starting point for everything else.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This page covers the three test types, where to get a kit in Colorado Springs, how to place a test correctly, and what to do with the result.</p>
  </div>
</section>

<section>
  <h2>The three test types</h2>
  <div class="prose-wide">

    <h3>1. Short-term test kit (2 to 7 days)</h3>
    <p>An activated-charcoal or alpha-track canister you place in your lowest livable level, then mail to a lab. Cost is typically $15–$40 including lab analysis. Short-term tests are the fastest way to find out whether you have a radon problem at all.</p>
    <p>Use short-term tests when:</p>
    <ul>
      <li>You want a quick first read on your home</li>
      <li>You're in a real estate transaction with limited time (though a professional test is preferred — see below)</li>
      <li>You're confirming the result of a previous test</li>
    </ul>

    <h3>2. Long-term test kit (90 days or more)</h3>
    <p>An alpha-track detector that sits in place for at least 90 days. Long-term tests average radon levels across seasons, which matters in Colorado because winter levels (sealed-up homes) are typically higher than summer levels.</p>
    <p>Use long-term tests when:</p>
    <ul>
      <li>You're not under a transaction deadline</li>
      <li>You want a more accurate annual exposure picture</li>
      <li>A short-term test was borderline (close to 4.0 pCi/L)</li>
    </ul>

    <h3>3. Professional measurement</h3>
    <p>A continuous radon monitor placed by a certified professional. Used for real estate transactions and for situations where you need a defensible, third-party-verified result. Continuous monitors record hourly readings; some labs return a written report in 48–72 hours.</p>
    <p>Use professional measurement when:</p>
    <ul>
      <li>You're buying or selling a home and need a defensible result</li>
      <li>Your DIY result was high and you want a confirming professional test before mitigation</li>
      <li>You're testing after mitigation to confirm the system worked</li>
    </ul>
    <p>For real estate transactions in Colorado, professional testers must be certified through NRPP or NRSB and registered with Colorado DORA.<sup><a href="#src-2">[2]</a></sup> Professional tests typically cost $150–$300 in Colorado Springs.</p>
  </div>
</section>

<section>
  <h2>Where to get a test kit in Colorado Springs</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>El Paso County Public Health Laboratory</strong> sells radon test kits to local residents. Check <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health</a> for current pricing and pickup hours.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>CDPHE</strong> periodically offers low-cost or free kits during <em>National Radon Action Month</em> (January). See the <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE radon page</a> for current availability.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Home improvement and hardware retail</strong> — Home Depot, Lowe's, Ace Hardware, and Amazon stock EPA-approved short-term kits.</li>
      <li><strong>Online radon labs</strong> — many ship a canister and a return mailer with lab analysis included in one price.</li>
    </ul>
    <p>If you choose a retail kit, make sure it is an EPA-approved device from a recognized lab.</p>
  </div>
</section>

<section>
  <h2>How to place a test correctly</h2>
  <div class="prose-wide">
    <p>A test placed incorrectly returns the wrong answer. EPA placement guidelines:</p>
    <ul class="checklist">
      <li>Place the test in the lowest livable level of the home (a finished basement counts; an unfinished crawl space does not).</li>
      <li>Place it 2–6 feet above the floor, away from drafts, fireplaces, exterior walls, and high-humidity areas like bathrooms or kitchens.</li>
      <li>Keep windows and exterior doors closed for at least 12 hours before and during a short-term test ("closed-house conditions"). Normal in-and-out traffic is fine.</li>
      <li>Avoid placing the test next to running HVAC vents or in direct sunlight.</li>
      <li>Don't move the test once it's deployed.</li>
    </ul>
    <p>Follow the kit's specific instructions — small differences in placement and timing affect the result.</p>
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
        <tr><td>Less than 2.0</td><td>Below "consider mitigation" threshold</td><td>Retest every two years.</td></tr>
        <tr><td>2.0–3.9</td><td>EPA suggests "consider mitigation"</td><td>Re-test (long-term preferred) and weigh mitigation. Many Colorado homes in this range choose to mitigate.</td></tr>
        <tr><td>4.0 or above</td><td>Action level — mitigate</td><td>Confirm with a second test (or a professional continuous monitor) and get at least two written quotes from licensed contractors.</td></tr>
        <tr><td>10.0 or above</td><td>Well above action level</td><td>Mitigate. EPA recommends not waiting — limit time in the lowest level until a system is in place.</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Action level reference: <a href="{s('epa_action_level')}" rel="noopener" target="_blank">EPA — Health Risk of Radon</a>.<sup><a href="#src-4">[4]</a></sup></p>
  </div>
</section>

<section>
  <h2>When to retest</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Every 2 years</strong> for a previously low result.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>After any major remodel</strong> that changes the foundation, basement, or HVAC system.</li>
      <li><strong>After mitigation</strong> — a post-install test confirms the system actually brought levels below 4.0 pCi/L.</li>
      <li><strong>Before listing or buying</strong> a home.</li>
      <li><strong>If your living patterns change</strong> — for example, finishing a basement that becomes daily living space.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Testing for real estate transactions</h2>
  <div class="prose-wide">
    <p>Real estate testing has different rules. Buyers and sellers should use a <strong>professional continuous monitor</strong> placed by an NRPP or NRSB certified, DORA-registered tester.<sup><a href="#src-2">[2]</a></sup> The reasons:</p>
    <ul>
      <li>The result must be defensible if either party disputes it.</li>
      <li>Continuous monitors record hourly data, so anti-tampering is built in.</li>
      <li>Results are typically available in 48–72 hours, which works with most inspection timelines.</li>
    </ul>
    <p>Colorado SB23-206 requires sellers and landlords to disclose any known radon test results and mitigation history.<sup><a href="#src-5">[5]</a></sup> If a previous test exists, the buyer should review it; if the seller has had mitigation done, the buyer should ask for the system's post-install test result and warranty documentation.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-2">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-3">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-4">U.S. EPA. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-5">Colorado General Assembly. <em>SB23-206</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


# =========================================================================
# COLORADO SPRINGS — FAILED TEST
# =========================================================================
CS_FAILED_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If your test result came back at or above <strong>4.0 pCi/L</strong>, the EPA considers your home above its action level. That sounds alarming. In Colorado Springs, it is also <em>common</em>: more than 40% of homes tested in El Paso County between 2005 and 2023 came back above this level.<sup><a href="#src-1">[1]</a></sup> A high result is not a crisis — it's a project.</p>
    <p>This page walks through the right next steps depending on your situation: homeowner not under contract, buyer or seller mid-deal, tenant or landlord. Each path is different.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Quick reference for what "failed" actually means</strong>
    <p>EPA's action level is 4.0 pCi/L. CDPHE recommends mitigation at or above that level. Between 2.0 and 3.9 pCi/L, the EPA says "consider mitigation."<sup><a href="#src-2">[2]</a></sup> Below 2.0 pCi/L, retest every two years.</p>
  </div>
</section>

<section>
  <h2>Step 1 — Confirm the reading</h2>
  <div class="prose-wide">
    <p>Before you commit to mitigation, confirm the result:</p>
    <ul>
      <li>If the first test was a short-term DIY kit, run a second short-term kit in the same room (different placement is fine) or a continuous monitor for a more granular read.</li>
      <li>If the first test was a long-term kit or a professional continuous monitor, you generally don't need to confirm — the methodology is already strong.</li>
      <li>If you're under a real estate transaction, a professional continuous monitor placed by an NRPP or NRSB certified, DORA-registered tester is the defensible standard.<sup><a href="#src-3">[3]</a></sup></li>
    </ul>
    <p>For very high readings (10 pCi/L or above), the EPA suggests minimizing time in the lowest level of the home until a mitigation system is installed.</p>
  </div>
</section>

<section>
  <h2>If you own the home and aren't under contract</h2>
  <div class="prose-wide">
    <p>Best case for clear-headed decision making. The steps:</p>
    <ol>
      <li><strong>Confirm the reading</strong> (above).</li>
      <li><strong>Get at least two written quotes</strong> from contractors who can prove NRPP or NRSB certification and Colorado DORA registration. Ask each to provide the same written scope so prices are comparable.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Compare scope, not just price.</strong> Number of suction points, fan model and warranty, sealing work, exhaust routing, permit handling, and post-installation test should all be in writing.</li>
      <li><strong>Schedule the install.</strong> Most Colorado Springs single-family installs take one day; allow one to two weeks for scheduling.</li>
      <li><strong>Retest after installation</strong> — a 48-hour post-mitigation test should be included in the quote and should bring you well below 4.0 pCi/L.</li>
    </ol>
    <p>If money is a constraint, check the <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">CDPHE low-income mitigation assistance program</a>.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>If you're a buyer under contract</h2>
  <div class="prose-wide">
    <p>This is the most time-sensitive situation. Colorado's inspection objection deadlines move fast, and mitigation typically takes one to two weeks end-to-end.</p>
    <ol>
      <li><strong>Day 1 — work out your timeline.</strong> When is your inspection objection deadline? When is closing? How many calendar days does that give you to negotiate <em>and</em> install if needed?</li>
      <li><strong>Day 1 to 3 — get two licensed contractor quotes</strong>, with at least one same-day if you're tight on time. Confirm each contractor can install before closing.</li>
      <li><strong>Object before the deadline.</strong> Your options typically include: (a) ask the seller to install mitigation before closing, (b) negotiate a seller credit at closing so you can install yourself, or (c) walk under the inspection contingency. Colorado law does not require sellers to mitigate, but they generally have to disclose — which means the next buyer will see the same problem.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>Document everything.</strong> Keep the test report, contractor quotes, and any seller correspondence. After closing, keep the system's installation paperwork and post-install test result — these become part of <em>your</em> SB23-206 disclosure when you sell.</li>
    </ol>
    <div class="callout">
      <strong>Practical tip</strong>
      <p>If closing is two weeks out and you don't yet have a confirmed install date, a seller credit at closing is often cleaner than waiting on a pre-close install. You hire the contractor on your timeline after you own the house.</p>
    </div>
  </div>
</section>

<section>
  <h2>If you're a seller</h2>
  <div class="prose-wide">
    <p>Two facts to know cold:</p>
    <ul>
      <li><strong>Colorado SB23-206 requires you to disclose</strong> any known radon test results and any mitigation history in the sale contract, along with the CDPHE radon brochure.<sup><a href="#src-4">[4]</a></sup></li>
      <li>Colorado does <strong>not</strong> require you to mitigate.<sup><a href="#src-2">[2]</a></sup> But once the buyer sees the disclosure (or runs their own inspection test), they'll likely want a price concession or mitigation done before closing.</li>
    </ul>
    <p>Most Colorado Springs sellers in this position do one of two things:</p>
    <ol>
      <li><strong>Mitigate before listing.</strong> Spend $1,000–$2,000 now, hand the buyer a working system and a post-install test result, and remove a major negotiation lever. Document the install for your disclosure.</li>
      <li><strong>Price-adjust at the offer table.</strong> Disclose, expect the buyer to bring it up, and credit at closing. This works when you don't have time to mitigate before listing.</li>
    </ol>
  </div>
</section>

<section>
  <h2>If you're a tenant or landlord</h2>
  <div class="prose-wide">
    <p>Colorado <strong>SB23-206</strong> applies to leases as well as sales. Landlords must include a radon warning and disclosure of any known test results and mitigation in residential leases, and they must provide the CDPHE radon brochure.<sup><a href="#src-4">[4]</a></sup></p>
    <p>After January 2026, tenants gain additional remedies (including potential lease void) if a landlord knew the property had elevated radon and did not mitigate. Tenants may also test their own unit at any time. If you're a tenant with a high reading, document it in writing to your landlord and reference the CDPHE radon brochure.</p>
    <p>If you're a landlord, treating mitigation as a standard property upgrade — like a roof or a water heater — is generally cheaper than the legal exposure of doing nothing.</p>
  </div>
</section>

<aside class="cta-inline" aria-label="Request a Colorado Springs quote">
  <div class="cta-inline-text">
    <strong>Ready for a quote based on your situation?</strong>
    Tell us your scenario — homeowner, buyer on a closing, seller — and we'll connect you with our DORA-registered Colorado mitigation partner. Written quote, no pressure.
  </div>
  <a href="/request-quote/" class="btn">Request a quote</a>
</aside>

<section>
  <h2>Choosing a contractor under deadline pressure</h2>
  <div class="prose-wide">
    <p>When you need to move fast, the temptation is to take the first quote you get. Resist that — verifying takes 10 minutes and protects you:</p>
    <ul class="checklist">
      <li>NRPP or NRSB certification number provided and verifiable</li>
      <li>Colorado DORA registration provided and verifiable<sup><a href="#src-3">[3]</a></sup></li>
      <li>Written scope with suction points, fan model, sealing, routing, and permits called out</li>
      <li>Post-installation test included</li>
      <li>Written workmanship warranty (years), plus the fan manufacturer warranty</li>
      <li>Can install before your closing deadline (get this in writing too)</li>
    </ul>
    <p>If you'd like us to route your situation to a licensed Colorado mitigation partner, <a href="/request-quote/">request a quote</a> and tell us your closing date in the form.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-2">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-3">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
    <li id="src-4">Colorado General Assembly. <em>SB23-206</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
    <li id="src-5">U.S. EPA. <em>Health Risk of Radon</em>. <a href="{s('epa_action_level')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
  </ol>
</aside>
"""


def cs_failed_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What counts as a failed radon test?",
             "acceptedAnswer": {"@type": "Answer", "text": "A result at or above 4.0 pCi/L. That is the EPA's action level and CDPHE's mitigation threshold."}},
            {"@type": "Question", "name": "How fast can radon mitigation happen if I'm closing on a house?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most Colorado Springs single-family installations take one day. End-to-end (quote, scheduling, install, post-install test) is typically one to two weeks."}},
            {"@type": "Question", "name": "Do sellers in Colorado have to mitigate radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Colorado does not require sellers to test or mitigate. Under SB23-206 they must disclose any known test results and mitigation history and provide the CDPHE radon brochure."}},
            {"@type": "Question", "name": "Should I take a seller credit or have mitigation done before closing?",
             "acceptedAnswer": {"@type": "Answer", "text": "A seller credit at closing is often cleaner when timelines are tight — you can hire the contractor yourself after closing. Pre-close mitigation works when there is enough time, the contractor can guarantee install, and both parties agree."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
