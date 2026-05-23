"""Content library hub page (Phase 7 polish).

One new page:
1. /library/   — Content library: every page on the site, organized by pillar
"""
import json
from pages_main import s, SOURCES


# =========================================================================
# /library/   — Content library hub
# =========================================================================
LIBRARY_BODY = f"""
<section>
  <div class="prose-wide">
    <p>This is the index of every page on Colorado Radon Guide, organized by topic. If you're looking for something specific, the categories below are the fastest way to find it. If you're new to the site, the <a href="/radon-basics/">Radon Basics</a> pillar is the right starting point; if you have a high test result, start with <a href="/colorado-springs/failed-radon-test/">Failed Radon Test in Colorado Springs</a>.</p>
  </div>
</section>

<section>
  <h2>The decision flow</h2>
  <div class="prose-wide">
    <p>Most people land here for one of four reasons. Here's where to go next:</p>
    <table>
      <thead>
        <tr><th>Your situation</th><th>Start here</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>I want a visual sense of radon risk across Colorado</td>
          <td><a href="/colorado-radon-map/">Colorado Radon Map</a></td>
        </tr>
        <tr>
          <td>I haven't tested my home yet</td>
          <td><a href="/radon-testing/">How to Test for Radon in Colorado</a></td>
        </tr>
        <tr>
          <td>I got a high test result</td>
          <td><a href="/colorado-springs/failed-radon-test/">Failed Radon Test in Colorado Springs</a></td>
        </tr>
        <tr>
          <td>I have a quote and want to evaluate it</td>
          <td><a href="/radon-mitigation-cost/quote-too-high/">Is My Quote Too High?</a></td>
        </tr>
        <tr>
          <td>I'm buying or selling a Colorado home</td>
          <td><a href="/colorado-springs/home-buyers-and-sellers/">Radon for CS Home Buyers and Sellers</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Statewide reference</h2>
  <div class="prose-wide">
    <p>Big-picture Colorado context — useful before or after testing your own home.</p>
    <ul>
      <li><a href="/colorado-radon-map/"><strong>Colorado Radon Map</strong></a> — what the EPA Radon Zone map shows for Colorado (53 Zone 1 counties, 11 Zone 2, 0 Zone 3), CDPHE county-level test data, and what the map does not tell you about your home</li>
    </ul>
  </div>
</section>

<section>
  <h2>Radon Basics</h2>
  <div class="prose-wide">
    <p>What radon is, why Colorado has it, how it works, and what your test result means.</p>
    <ul>
      <li><a href="/radon-basics/"><strong>What Is Radon?</strong></a> — plain-language introduction, uranium decay chain, how it's measured (pCi/L vs Bq/m³)</li>
      <li><a href="/radon-basics/why-common-in-colorado/"><strong>Why Radon Is Common in Colorado</strong></a> — Front Range geology, Pikes Peak granite, Pierre Shale, EPA Zone 1, El Paso County prevalence</li>
      <li><a href="/radon-basics/how-it-enters-homes/"><strong>How Radon Enters Homes</strong></a> — the stack effect, entry pathways, seasonal patterns</li>
      <li><a href="/radon-basics/health-risks/"><strong>Radon Health Risks</strong></a> — EPA risk tables, WHO action level, ATSDR on children, Surgeon General advisory</li>
      <li><a href="/radon-basics/levels-explained/"><strong>Radon Levels Explained</strong></a> — what 2, 4, 10, and 20 pCi/L actually mean</li>
      <li><a href="/radon-basics/by-foundation-type/"><strong>By Foundation Type</strong></a> — basement, crawlspace, slab, walk-out, tri-level, mixed foundations</li>
    </ul>
  </div>
</section>

<section>
  <h2>Radon Testing</h2>
  <div class="prose-wide">
    <p>How to test for radon, what your result means, and how testing differs in real estate, rentals, and commercial buildings.</p>
    <ul>
      <li><a href="/radon-testing/"><strong>How to Test for Radon in Colorado</strong></a> — three test types, where to get a kit, EPA placement, result interpretation</li>
      <li><a href="/radon-testing/short-term-vs-long-term/"><strong>Short-Term vs Long-Term Tests</strong></a> — when to use each duration, Colorado seasonal context</li>
      <li><a href="/radon-testing/where-to-place-a-test/"><strong>Where to Place a Radon Test</strong></a> — EPA placement guide, closed-house conditions, common mistakes</li>
      <li><a href="/radon-testing/during-real-estate-transactions/"><strong>Testing During Real Estate Transactions</strong></a> — SB23-206 disclosure law, CRM standard, DORA licensing, tampering controls</li>
      <li><a href="/radon-testing/for-rentals/"><strong>Testing for Rentals</strong></a> — Colorado landlord disclosure, tenant testing rights under SB23-206</li>
      <li><a href="/radon-testing/for-businesses/"><strong>Testing for Businesses</strong></a> — commercial AARST protocols, schools, childcare, multi-tenant buildings</li>
      <li><a href="/colorado-springs/radon-testing/"><strong>Radon Testing in Colorado Springs</strong></a> — EPCPH Lab kits, local resources</li>
    </ul>
  </div>
</section>

<section>
  <h2>Mitigation Systems</h2>
  <div class="prose-wide">
    <p>How radon mitigation works, system components, and what to expect from a quality install.</p>
    <ul>
      <li><a href="/radon-mitigation-systems/"><strong>How Radon Mitigation Works</strong></a> — depressurization principle, system parts, what's different about Colorado</li>
      <li><a href="/radon-mitigation-systems/sub-slab-depressurization/"><strong>Sub-Slab Depressurization (SSD)</strong></a> — basement and slab mitigation, PFE diagnostic, exhaust requirements</li>
      <li><a href="/radon-mitigation-systems/crawlspace-sub-membrane/"><strong>Crawlspace Sub-Membrane (SMD)</strong></a> — vapor barrier requirements, sealing scope, encapsulation vs mitigation</li>
      <li><a href="/radon-mitigation-systems/passive-vs-active/"><strong>Passive vs Active Systems</strong></a> — IRC Appendix BE rough-ins, newer Colorado builds, activation cost</li>
      <li><a href="/radon-mitigation-systems/fans-pipes-suction-points/"><strong>Fans, Pipes & Suction Points</strong></a> — equipment deep dive with Colorado altitude correction</li>
      <li><a href="/radon-mitigation-systems/why-sealing-isnt-enough/"><strong>Why Sealing Alone Isn't Enough</strong></a> — the sealing myth, pressure-driven entry</li>
      <li><a href="/radon-mitigation-systems/what-happens-after-mitigation/"><strong>What Happens After Mitigation</strong></a> — post-mit test, manometer routine, retest cadence, fan lifespan</li>
    </ul>
  </div>
</section>

<section>
  <h2>Cost and Quotes</h2>
  <div class="prose-wide">
    <p>What radon mitigation actually costs, why quotes vary, and how to evaluate yours.</p>
    <ul>
      <li><a href="/radon-mitigation-cost/"><strong>Radon Mitigation Cost in Colorado</strong></a> — statewide cost anchor, four-scenario framework</li>
      <li><a href="/colorado-springs/radon-mitigation-cost/"><strong>Cost in Colorado Springs</strong></a> — local quote ranges by scenario, add-ons</li>
      <li><a href="/radon-mitigation-cost/quote-variation/"><strong>Why Quotes Vary So Much</strong></a> — five real cost drivers including Colorado altitude correction</li>
      <li><a href="/radon-mitigation-cost/quote-too-high/"><strong>Is My Quote Too High?</strong></a> — sanity-check tree by scenario</li>
      <li><a href="/radon-mitigation-cost/whats-in-a-quote/"><strong>What's in a Quote</strong></a> — 14-item complete-quote checklist</li>
      <li><a href="/radon-mitigation-cost/crawlspaces/"><strong>Crawlspace Costs</strong></a> — why crawlspaces cost more, vapor barrier reality</li>
      <li><a href="/radon-mitigation-cost/finished-basements/"><strong>Finished Basement Costs</strong></a> — interior routing, drywall touch-up, aesthetic options</li>
      <li><a href="/radon-mitigation-cost/real-estate-deadlines/"><strong>Cost During a Real Estate Transaction</strong></a> — SB23-206 + three buyer options + closing timeline</li>
    </ul>
  </div>
</section>

<section>
  <h2>Choosing a Contractor</h2>
  <div class="prose-wide">
    <p>How to find, verify, and hire a DORA-licensed Colorado radon contractor.</p>
    <ul>
      <li><a href="/radon-contractors/"><strong>How to Choose a Contractor</strong></a> — DORA + NRPP/NRSB framework, scope comparison, red flags overview</li>
      <li><a href="/radon-contractors/verify-licenses-and-certifications/"><strong>Verify Licenses & Certifications</strong></a> — DORA, NRPP, NRSB lookup walkthroughs (step-by-step)</li>
      <li><a href="/radon-contractors/questions-to-ask/"><strong>Questions to Ask Before Hiring</strong></a> — full pre-hire question list by stage</li>
      <li><a href="/radon-contractors/red-flags-in-a-quote/"><strong>Red Flags in a Quote</strong></a> — walk-away red flags vs ask-before-signing yellow flags</li>
      <li><a href="/radon-contractors/warranties-and-retesting/"><strong>Warranties, Retesting & Post-Install</strong></a> — workmanship, fan, and performance warranties</li>
      <li><a href="/radon-contractors/how-to-file-a-complaint/"><strong>How to File a Complaint</strong></a> — DORA, BBB, AG, small claims paths</li>
    </ul>
  </div>
</section>

<section>
  <h2>Colorado Springs Local</h2>
  <div class="prose-wide">
    <p>Local Colorado Springs and El Paso County context.</p>
    <ul>
      <li><a href="/colorado-springs/"><strong>Colorado Springs Radon Guide</strong></a> — local prevalence, testing, mitigation, real estate</li>
      <li><a href="/colorado-springs/radon-mitigation-cost/"><strong>Mitigation Cost in Colorado Springs</strong></a> — local quote ranges, El Paso County context</li>
      <li><a href="/colorado-springs/radon-testing/"><strong>Radon Testing in Colorado Springs</strong></a> — local kit sources, professional testing</li>
      <li><a href="/colorado-springs/failed-radon-test/"><strong>Failed Radon Test in Colorado Springs</strong></a> — next steps by situation</li>
      <li><a href="/colorado-springs/home-buyers-and-sellers/"><strong>Home Buyers and Sellers</strong></a> — CS-specific real estate guide with SB23-206 context</li>
    </ul>
  </div>
</section>

<section>
  <h2>About this site</h2>
  <div class="prose-wide">
    <ul>
      <li><a href="/about/"><strong>About Colorado Radon Guide</strong></a></li>
      <li><a href="/disclosure/"><strong>Editorial & Lead Routing Disclosure</strong></a></li>
      <li><a href="/privacy/"><strong>Privacy Policy</strong></a></li>
      <li><a href="/contact/"><strong>Contact</strong></a></li>
    </ul>
  </div>
</section>
"""
