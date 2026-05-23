"""Denver hub page (Phase 9).

One new page:
  /denver/   — Denver Radon Guide hub. Front Range radon risk context,
               Denver housing stock framing, testing and mitigation
               decision flow, real estate scenarios, quote help.

Design constraint: this is NOT a Colorado Springs clone with the city name
swapped. The page must work as a useful Denver decision page in its own
right — every section should be content a Denver homeowner without quote
intent would still find useful. Denver-specific pricing is NOT invented;
cost questions route to the statewide cost page. Denver-specific facts come
only from verified sources (EPA, CDPHE, COEPHT, DDPHE, DORA, Census ACS,
Colorado General Assembly).
"""
import json
from pages_main import s, SOURCES

# Register Denver-specific source URLs (idempotent — does not overwrite if
# pages_main or pages_map already set them). The DDPHE radon URL is now the
# canonical value in pages_main.SOURCES['denver_radon'] (updated 2026-05-22
# to the Healthy Families Healthy Homes slug after research verification).
SOURCES.setdefault("denver_cpd", "https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Community-Planning-and-Development")
SOURCES.setdefault("epa_map_radon_zones", "https://www.epa.gov/radon/epa-map-radon-zones")
SOURCES.setdefault("cdphe_testing", "https://cdphe.colorado.gov/hm/testing-your-home-radon")
SOURCES.setdefault("cdphe_understanding_radon", "https://cdphe.colorado.gov/understanding-radon")
SOURCES.setdefault("cdphe_press_jan26", "https://cdphe.colorado.gov/press-release/half-of-colorado-homes-have-elevated-radon-levels-which-can-cause-lung-cancer")
SOURCES.setdefault("coepht_radon_data", "https://coepht.colorado.gov/radon-data")
SOURCES.setdefault("coepht_radon_viz", "https://cohealthviz.dphe.state.co.us/t/EnvironmentalEpidemiologyPublic/views/Radon/RadonMeasures")
SOURCES.setdefault("epa_action_level_def", "https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean")
SOURCES.setdefault("census_acs_denver_dp04", "https://data.census.gov/table/ACSDP5Y2023.DP04?g=050XX00US08031")
SOURCES.setdefault("usgs_south_platte_radon", "https://pubs.usgs.gov/circ/circ1167/nawqa91.7.html")


# =========================================================================
# DENVER HUB — Front Range Zone 1 framing, Denver-specific housing stock
# context, route-to-pillars for cost and process, statewide law for the
# real estate parts.
# =========================================================================

DENVER_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you live in Denver — or anywhere in the Denver-Aurora-Centennial metro — radon is worth taking seriously. Denver County and every Denver Metro county sit in the EPA's highest predicted indoor-radon classification, and the most recent CDPHE statewide figure (January 2026 press release, dateline Denver) is that <strong>approximately half of Colorado homes have radon levels that exceed the EPA action level of 4.0 pCi/L</strong>.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-9">[9]</a></sup> That doesn't mean every Denver house has a problem. It means the only way to know about <em>your</em> house is to test it.</p>
    <p>The Denver Department of Public Health and Environment (DDPHE) puts the city-specific framing this way: <em>"The EPA has ranked Denver as 'Zone 1,' which means the average house will likely exceed the EPA's action level of 4.0 pCi/L."</em><sup><a href="#src-8">[8]</a></sup> DDPHE recommends testing every two to three years — slightly more conservative than EPA's every-two-year recommendation — because conditions in a home can and do change.<sup><a href="#src-8">[8]</a></sup></p>
    <p>This page is the Denver-specific entry point to the rest of the site. We don't have a separate Denver cost guide or a separate Denver testing guide because the underlying science is the same statewide — what's actually Denver-specific is the housing stock, the metro geography, the real estate market, and which county-level resources you use. Those are what this page covers. Everything else routes to the statewide pillars.</p>
  </div>
</section>

<section>
  <h2>Why Denver is on the radon map</h2>
  <div class="explainer">
    <div class="explainer-text">
      <p>Radon is a soil gas — the natural decay product of uranium in rock and soil — and Colorado's Front Range geology has more uranium-bearing material than most of the United States. CDPHE puts the mechanism simply: <em>"Radon moves from uranium-bearing granite deposits in the soil to the atmosphere."</em><sup><a href="#src-10">[10]</a></sup> The USGS, in a primary-source study of the South Platte River Basin that contains the entire Denver Metro area, puts it more precisely: <em>"High concentrations of uranium and radon in the South Platte River Basin are directly related to the local geology. The local bedrock, particularly the crystalline rocks (primarily granitic) in the mountains and marine shales and coal deposits in the plains, are naturally high in uranium."</em><sup><a href="#src-11">[11]</a></sup></p>
      <p>The EPA Map of Radon Zones classifies <strong>Denver County in Zone 1</strong>, the agency's highest predicted indoor-radon category.<sup><a href="#src-2">[2]</a></sup> So is every other Denver Metro county: Adams, Arapahoe, Boulder, Broomfield, Douglas, and Jefferson are all Zone 1. For finer-grained Denver County context, CDPHE's <a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">COEPHT radon data</a> publishes county-level test summaries (number of tests, average indoor radon, percent of measurements over 4 pCi/L) based on actual indoor measurements submitted from 2005 onward.<sup><a href="#src-4">[4]</a></sup></p>
      <p>For the why-Colorado geology story in more depth, see <a href="/radon-basics/why-common-in-colorado/">Why Radon Is Common in Colorado</a>. For the EPA zone classification across all 64 counties, see the <a href="/colorado-radon-map/">Colorado Radon Map</a>.</p>
    </div>
    <figure class="figure">
      <img src="/assets/images/radon-entry-diagram.jpg" alt="Cross-section illustration of a home showing radon gas rising from soil through foundation cracks and accumulating in the basement." width="1200" height="896" loading="lazy">
      <figcaption><strong>How radon enters a home.</strong> Soil gas rises through small foundation cracks, the floor-wall joint, sump pits, and plumbing penetrations into the basement and living space above. Denver's foundation mix (full basements, finished lower levels, older stone-and-mortar perimeters in some pre-war neighborhoods) gives radon many of those pathways.</figcaption>
    </figure>
  </div>
</section>

<section>
  <h2>Denver Metro counties at a glance</h2>
  <div class="prose-wide">
    <p>If you're not sure which county you're in, the table below is also a quick orientation. The Denver MSA spans seven counties; the city of Denver itself is contiguous with Denver County. All seven are EPA Zone 1.</p>
    <table>
      <thead>
        <tr><th>County</th><th>EPA Zone</th><th>What sits in it (selected)</th></tr>
      </thead>
      <tbody>
        <tr><td>Denver County</td><td>Zone 1</td><td>City and County of Denver</td></tr>
        <tr><td>Adams County</td><td>Zone 1</td><td>Thornton, Northglenn, Commerce City, Brighton, parts of Aurora and Westminster</td></tr>
        <tr><td>Arapahoe County</td><td>Zone 1</td><td>Centennial, Englewood, Littleton, most of Aurora, Greenwood Village</td></tr>
        <tr><td>Boulder County</td><td>Zone 1</td><td>Boulder, Longmont, Louisville, Lafayette, Superior</td></tr>
        <tr><td>Broomfield County</td><td>Zone 1</td><td>City and County of Broomfield</td></tr>
        <tr><td>Douglas County</td><td>Zone 1</td><td>Castle Rock, Parker, Lone Tree, Highlands Ranch (CDP)</td></tr>
        <tr><td>Jefferson County</td><td>Zone 1</td><td>Lakewood, Arvada, Wheat Ridge, Golden, Evergreen</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Zone classification per the EPA Map of Radon Zones.<sup><a href="#src-2">[2]</a></sup> The EPA's own framing is that the zone map is a planning tool — it "should not be used to determine if individual homes need to be tested." That instruction is part of the agency's published guidance.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>What's actually different about Denver homes</h2>
  <div class="prose-wide">
    <p>The radon science is statewide, but the housing stock that radon meets is Denver-specific. The U.S. Census Bureau's most recent American Community Survey 5-year estimates (2019-2023) describe Denver County's roughly 352,600 housing units this way:<sup><a href="#src-12">[12]</a></sup></p>
    <table class="compact">
      <thead>
        <tr><th>Denver County housing stock</th><th>Value</th></tr>
      </thead>
      <tbody>
        <tr><td>Median year structure built</td><td>1974</td></tr>
        <tr><td>Units built 1939 or earlier (pre-1940)</td><td>17.2% (about 60,700 units)</td></tr>
        <tr><td>Units built 1940-1959</td><td>18.2% (about 64,400 units)</td></tr>
        <tr><td>1-unit detached (single-family)</td><td>41.2% (about 145,300 units)</td></tr>
        <tr><td>Total housing units</td><td>352,593</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Source: U.S. Census Bureau, 2019-2023 American Community Survey 5-Year Estimates, Table DP04, Denver County (FIPS 08031).<sup><a href="#src-12">[12]</a></sup></p>
    <p>What that means in practice — three Denver-specific patterns worth knowing about before you test or mitigate:</p>
    <ol>
      <li><strong>A lot of Denver homes are old enough to have full basements.</strong> Over a third of Denver's housing stock was built before 1960, and the pre-war bungalows in Park Hill, Berkeley, Sunnyside, Wash Park, Capitol Hill, and the Highlands — along with the mid-century ranches in Mayfair, Krisana Park, and Virginia Vale — overwhelmingly have full basements. Basements concentrate radon. The lower the lived-in space and the longer it's occupied, the more your radon exposure matters.</li>
      <li><strong>Finished basements are extremely common.</strong> A finished basement isn't a problem in itself, but it changes two things: where you place a test (see the <a href="/radon-testing/where-to-place-a-test/">test placement guide</a>) and how a mitigation system gets routed (interior chase vs. exterior fan, drywall touch-up, aesthetic choices). The <a href="/radon-mitigation-cost/finished-basements/">finished basement cost page</a> walks through what that actually means for a quote.</li>
      <li><strong>Foundation mix is wider than you'd expect.</strong> A 1925 bungalow in Berkeley has a poured or stone-and-mortar perimeter and an old slab; a 1955 ranch in Mayfair has a poured slab with a crawl-space addition; a 1995 Highlands Ranch home has a poured concrete basement with a sump pit; a 2015 Central Park (formerly Stapleton) townhome may have a passive radon stub-up installed under IRC Appendix BE. Each of those translates to a different mitigation approach. The <a href="/radon-basics/by-foundation-type/">foundation-type page</a> covers each scenario.</li>
    </ol>
    <p>None of this is a reason to be alarmed. It's the reason your specific test result and your specific quote depend on which Denver house you're in, not on a generic Denver price.</p>
  </div>
</section>

<section>
  <h2>Step 1 — Test</h2>
  <div class="prose-wide">
    <p>CDPHE's published guidance is that radon "is found at elevated levels in one out of every two Colorado homes."<sup><a href="#src-1">[1]</a></sup> DDPHE's Denver-specific guidance recommends testing every two to three years because conditions in a home (HVAC changes, settling foundations, remodels, even seasonal pressure differences) can shift radon levels over time.<sup><a href="#src-8">[8]</a></sup></p>
    <div class="callout">
      <strong>Free test kits for Denver residents.</strong>
      <p>DDPHE distributes free short-term radon test kits to Denver residents while supplies last. The kit order is on the DDPHE radon page.<sup><a href="#src-8">[8]</a></sup> If supplies are exhausted, short-term DIY kits typically cost $15-$30 from CDPHE-affiliated programs and national labs.</p>
    </div>
    <p>You have three test options. Pick by use case:</p>
    <ul>
      <li><strong>Short-term DIY kit (2-7 days).</strong> Fastest snapshot. Best when you've never tested or you're between long-term tests. See <a href="/radon-testing/short-term-vs-long-term/">short-term vs long-term tests</a> for when each is right.</li>
      <li><strong>Long-term DIY kit (90+ days).</strong> Better picture of year-round exposure. Best for a confident answer in your owned home.</li>
      <li><strong>Professional measurement.</strong> Required for real estate transactions under Colorado SB23-206 and the standard Colorado Real Estate Commission contract. Performed by an NRPP- or NRSB-certified tester registered with the Colorado DORA Office of Radon Professionals.<sup><a href="#src-5">[5]</a></sup></li>
    </ul>
    <p>For complete walkthroughs:</p>
    <ul>
      <li><a href="/radon-testing/"><strong>How to test for radon in Colorado</strong></a> — pillar page</li>
      <li><a href="/radon-testing/where-to-place-a-test/"><strong>Where to place a radon test</strong></a> — EPA placement standard, closed-house conditions, common mistakes</li>
      <li><a href="/radon-testing/during-real-estate-transactions/"><strong>Testing during a Colorado real estate transaction</strong></a> — SB23-206 disclosure, CRM contract standard, DORA licensing</li>
    </ul>
  </div>
</section>

<section>
  <h2>Step 2 — If your test is at or above 4.0 pCi/L</h2>
  <div class="prose-wide">
    <p>The EPA's action level is 4.0 pCi/L; the agency recommends mitigation at that level and says homeowners should "consider mitigating" at 2.0-4.0 pCi/L.<sup><a href="#src-3">[3]</a></sup> CDPHE matches the 4.0 pCi/L recommendation.<sup><a href="#src-1">[1]</a></sup></p>
    <p>The standard mitigation approach in a Denver basement-heavy home is <strong>active sub-slab depressurization (SSD)</strong>: a sealed PVC riser pulls radon from beneath the slab and discharges it above the roofline, powered by a quiet electric fan. Crawlspace areas (more common on Denver mid-century additions and some east-metro homes) use a sub-membrane variant. Sump pits and existing perimeter drain tile can sometimes be tied into the same system.</p>
    <p>For the full how-it-works walkthrough:</p>
    <ul>
      <li><a href="/radon-mitigation-systems/"><strong>How radon mitigation works</strong></a> — pillar page</li>
      <li><a href="/radon-mitigation-systems/sub-slab-depressurization/"><strong>Sub-slab depressurization (SSD)</strong></a> — for basements and slab-on-grade</li>
      <li><a href="/radon-mitigation-systems/crawlspace-sub-membrane/"><strong>Crawlspace sub-membrane</strong></a> — for partial or full crawlspaces</li>
      <li><a href="/radon-mitigation-systems/passive-vs-active/"><strong>Passive vs active systems</strong></a> — relevant for newer Denver builds with an IRC Appendix BE rough-in</li>
      <li><a href="/radon-mitigation-systems/why-sealing-isnt-enough/"><strong>Why sealing alone isn't enough</strong></a> — CDPHE's caution against treating sealing as the fix</li>
    </ul>
  </div>
</section>

<section>
  <h2>What does radon mitigation cost in Denver?</h2>
  <div class="prose-wide">
    <p>The honest answer: Denver mitigation pricing depends much more on the house than on the ZIP code. We don't publish a Denver-specific dollar figure on this page because doing so responsibly requires a more rigorous Denver market sample than we currently have. Instead, here is what actually drives a Denver quote up or down, and where to read the pricing logic in detail.</p>
    <p>The five biggest cost drivers are the same in Denver as everywhere else in Colorado:</p>
    <ul>
      <li><strong>Foundation type</strong> — full basement is the baseline; finished basement, crawlspace, multi-zone, or tri-level all push the price higher</li>
      <li><strong>Finished basement access</strong> — interior chase, exterior fan, or sometimes a creative routing through a closet or mechanical room. Drywall touch-up may or may not be in the quote.</li>
      <li><strong>System routing</strong> — where the riser goes, where the fan sits, and how the exhaust is routed above the roofline</li>
      <li><strong>Number of suction points</strong> — a single suction point is the baseline; multiple suction points (for footing-divided slabs or additions) cost more</li>
      <li><strong>Real estate timing</strong> — a closing-deadline install can be more expensive than a routine schedule, simply because it has to jump the queue</li>
    </ul>
    <p>For the actual numbers and quote ranges:</p>
    <ul>
      <li><a href="/radon-mitigation-cost/"><strong>Radon Mitigation Cost in Colorado</strong></a> — the statewide cost anchor. CDPHE's published baseline is in the $1,000-$2,000 range; the four-scenario framework (basic basement / finished basement / crawlspace / multi-zone) layers on top.</li>
      <li><a href="/radon-mitigation-cost/quote-variation/"><strong>Why quotes vary so much</strong></a> — five real cost drivers including Colorado altitude correction for fan selection.</li>
      <li><a href="/radon-mitigation-cost/quote-too-high/"><strong>Is my quote too high?</strong></a> — sanity-check tree by scenario.</li>
      <li><a href="/radon-mitigation-cost/whats-in-a-quote/"><strong>What's in a quote</strong></a> — 14-item complete-quote checklist.</li>
    </ul>
    <div class="callout">
      <strong>One Colorado-specific cost note that matters in Denver.</strong>
      <p>Denver sits at roughly 5,280 feet (1,609 m). Radon fans are rated at sea-level airflow; airflow drops by approximately 4% per 1,000 feet of elevation. A correctly specified Denver system accounts for that altitude correction in fan selection. A quote that doesn't mention fan model and rated airflow is harder to evaluate — the <a href="/radon-mitigation-systems/fans-pipes-suction-points/">fans and equipment page</a> walks through what to look for.</p>
    </div>
  </div>
</section>

<section>
  <h2>If you're buying or selling a Denver home</h2>
  <div class="prose-wide">
    <p>Colorado's radon real estate framework is statewide, not Denver-specific. Two things shape every Denver transaction:</p>
    <ul>
      <li><strong>Colorado SB23-206 (CRS § 38-35.7-112), effective August 7, 2023.</strong> Every residential sale and lease in Colorado must include a radon warning, any known test results, and any mitigation history. Sellers and landlords must provide the CDPHE radon brochure. Colorado does <em>not</em> require sellers to test or to mitigate — only to disclose what they know.<sup><a href="#src-6">[6]</a></sup> "No disclosure" almost always means "no test was done," not "no radon."</li>
      <li><strong>The standard Colorado Real Estate Commission contract</strong> sets a defined radon inspection window. The buyer's right to test, the seller's response obligation, and the remedy if a test fails are all timing-driven, and a missed deadline can collapse a buyer's leverage.</li>
    </ul>
    <p>Buyers have three practical options at the inspection-result stage:</p>
    <ol>
      <li><strong>Mitigate during the closing window.</strong> Possible if the timeline is long enough and a licensed contractor can install before close.</li>
      <li><strong>Negotiate a closing credit</strong> in the amount of a written mitigation quote, and complete the install after close.</li>
      <li><strong>Walk away</strong> if the contract permits it under the inspection contingency.</li>
    </ol>
    <p>The full real-estate walkthrough is the same for Denver as it is for Colorado Springs:</p>
    <ul>
      <li><a href="/radon-testing/during-real-estate-transactions/"><strong>Testing During Real Estate Transactions</strong></a> — SB23-206 deep dive, CRM standard, tampering controls.</li>
      <li><a href="/radon-mitigation-cost/real-estate-deadlines/"><strong>Mitigation cost during a real estate transaction</strong></a> — buyer's three options, credit vs mitigate framework, closing timeline.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Rentals and multi-family in Denver</h2>
  <div class="prose-wide">
    <p>Colorado SB23-206 applies to leases as well as sales. A Denver landlord must disclose any known elevated radon and any mitigation history at lease signing. After <strong>January 1, 2026</strong>, additional tenant remedies take effect if a landlord knew of an elevated radon condition and did not mitigate.<sup><a href="#src-6">[6]</a></sup> CDPHE's <a href="{s('cdphe_realestate')}" rel="noopener" target="_blank">radon and real estate page</a> publishes the current disclosure forms and brochure.</p>
    <p>For tenants: you have the right to test your unit. The cheapest reliable starting point is a short-term test kit; CDPHE and several Colorado public-health agencies sell or distribute low-cost kits. Test placement in a multi-family unit follows the same EPA closed-house rules as in a single-family home — see <a href="/radon-testing/where-to-place-a-test/">where to place a test</a>.</p>
    <p>For landlords and small property owners: the rules for one- to four-unit residential properties are generally aligned with the single-family disclosure obligations. For larger multi-family and commercial buildings, the AARST commercial measurement and mitigation standards apply — see <a href="/radon-testing/for-businesses/">testing for businesses and commercial buildings</a>.</p>
  </div>
</section>

<section>
  <h2>How to verify a Denver radon contractor</h2>
  <div class="prose-wide">
    <p>Since July 1, 2022, every radon measurement and mitigation professional working in Colorado has been required to be both certified through NRPP or NRSB <em>and</em> registered with the Colorado DORA Office of Radon Professionals.<sup><a href="#src-5">[5]</a></sup> Denver has no separate city license on top of that — the DORA registration is the gating credential statewide.</p>
    <p>Before you sign a Denver contractor's quote:</p>
    <ul class="checklist">
      <li>Confirm their <strong>Colorado DORA registration number</strong> — verifiable on the DORA radon professional lookup</li>
      <li>Confirm their <strong>NRPP or NRSB certification number</strong></li>
      <li>Ask for a <strong>written scope</strong>: suction points, fan model and rated airflow, sealing scope, exhaust routing, permit handling, post-installation test, warranty</li>
      <li>Confirm what <strong>permits</strong> the contractor will pull. Denver Community Planning &amp; Development handles building permits for the City and County of Denver; suburban metro counties have their own permitting processes. Confirm with your jurisdiction before signing.<sup><a href="#src-7">[7]</a></sup></li>
    </ul>
    <p>Step-by-step license verification, including DORA, NRPP, and NRSB lookups:</p>
    <ul>
      <li><a href="/radon-contractors/"><strong>How to choose a radon contractor in Colorado</strong></a> — pillar page</li>
      <li><a href="/radon-contractors/verify-licenses-and-certifications/"><strong>Verify Licenses &amp; Certifications</strong></a> — step-by-step lookup walkthroughs</li>
      <li><a href="/radon-contractors/questions-to-ask/"><strong>Questions to ask before hiring</strong></a></li>
      <li><a href="/radon-contractors/red-flags-in-a-quote/"><strong>Red flags in a quote</strong></a></li>
    </ul>
  </div>
</section>

<section>
  <h2>When to request quote help</h2>
  <div class="prose-wide">
    <p>If you're at the point where you want one quote from a licensed Colorado mitigation partner — not a stack of contractor calls — that's what the quote form is for. We route one inquiry to one DORA-registered, NRPP- or NRSB-certified Colorado contractor whose service area covers Denver Metro. The quote is free. There's no obligation, no high-pressure sales call, and your information is not shopped to multiple contractors.</p>
    <p>If you'd rather get cost context first, the <a href="/radon-mitigation-cost/">statewide cost guide</a> and <a href="/radon-mitigation-cost/whats-in-a-quote/">what's in a quote</a> page are the right starting points.</p>
    <p style="margin-top:1.25rem;"><a href="/request-quote/" class="btn">Request a Denver radon quote</a></p>
  </div>
</section>

<section>
  <h2>Frequently asked questions</h2>

  <details>
    <summary>Is radon actually a problem in Denver, or is it overblown?</summary>
    <p>Denver County and every Denver Metro county is classified by the EPA as Zone 1 — the highest predicted indoor-radon category — and the CDPHE statewide figure is that about one in two Colorado homes test above the EPA action level. The CDPHE COEPHT dataset publishes county-level test summaries from 2005-2017 for finer-grained context. Real, locally relevant, and worth a $15-$30 short-term test kit to find out where your specific house stands.</p>
  </details>

  <details>
    <summary>Does Denver County have its own radon data separate from CDPHE?</summary>
    <p>Denver County's radon test data is captured inside the broader CDPHE Colorado Environmental Public Health Tracking (COEPHT) program, which publishes county-level summaries. Denver does not maintain a separate municipal radon survey. The Denver Department of Public Health &amp; Environment refers homeowners to CDPHE and the EPA for radon guidance.</p>
  </details>

  <details>
    <summary>Where can I get a Denver radon test kit?</summary>
    <p>DDPHE distributes free short-term radon test kits to Denver residents while supplies last — the order link is on the DDPHE radon page.<sup>[8]</sup> Beyond that, the common options are mail-order test kits sold by CDPHE-affiliated programs and national labs, retail kits at hardware stores, and DIY kits from radon-equipment websites. Costs are usually $15-$35 for a short-term kit and $20-$50 for a long-term kit, including lab analysis. For a real estate transaction, the test must be performed by a professional certified through NRPP or NRSB and registered with Colorado DORA — a DIY kit does not satisfy the CRM contract standard.</p>
  </details>

  <details>
    <summary>Does Denver require a permit to install a radon mitigation system?</summary>
    <p>Mechanical, electrical, and exhaust work on a mitigation system is generally permitted work in any Colorado jurisdiction. The City and County of Denver handles permits through Denver Community Planning &amp; Development. Suburban metro jurisdictions (Aurora, Lakewood, Arvada, Centennial, Castle Rock, Broomfield, etc.) each issue their own building permits. Any licensed Colorado radon contractor should pull the required permit; the permit should be itemized in the written quote. Confirm with your specific jurisdiction before signing.</p>
  </details>

  <details>
    <summary>How long does mitigation take in a Denver home?</summary>
    <p>Most single-family installs take one day on site. Add scheduling lead time on the front end and a 2- to 7-day post-mitigation test on the back end. A reasonable end-to-end timeline from signed quote to verified system is one to two weeks. For finished-basement homes the on-site work can extend to a second day depending on the routing and any drywall touch-up scope.</p>
  </details>

  <details>
    <summary>I'm in Aurora, Lakewood, Boulder, Longmont, or another metro suburb. Is this page still relevant?</summary>
    <p>Yes. All Denver Metro counties are EPA Zone 1, the statewide testing and disclosure rules are identical, and the underlying mitigation science is the same. What changes by city is which permitting office issues the permit and the contractor's drive time. The quote form lets you select Denver Metro or "Other Colorado area" and capture your ZIP — service-area routing happens by ZIP, not city name.</p>
  </details>

  <details>
    <summary>Why don't you publish a Denver-specific mitigation cost?</summary>
    <p>Because we don't have a rigorous Denver-specific cost sample we can stand behind, and inventing a number would be worse than referring to the statewide CDPHE figure and the cost drivers. Our published statewide cost anchor is the CDPHE $1,000-$2,000 range plus the four-scenario framework, both visible on the <a href="/radon-mitigation-cost/">cost guide</a>. When we have a sound Denver-specific dataset, we'll publish it.</p>
  </details>

  <details>
    <summary>Does the Colorado Radon Guide install mitigation systems or perform testing?</summary>
    <p>No. Colorado Radon Guide is an independent information and quote-connection resource. We don't install, don't test, and don't hold radon professional certifications. When you submit the quote form, your information is routed to one licensed Colorado mitigation partner — we don't sell your data to a list of contractors.</p>
  </details>
</section>

<section>
  <div class="callout">
    <strong>About this guide.</strong>
    <p>Colorado Radon Guide is an independent editorial resource. We are not a radon contractor. When you request a quote, your information is routed to one licensed Colorado mitigation partner. <a href="/about/">More about us</a> · <a href="/disclosure/">How leads are routed</a>.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado Department of Public Health and Environment. <em>Testing your home for radon</em>. <a href="{s('cdphe_testing')}" rel="noopener" target="_blank">cdphe.colorado.gov/hm/testing-your-home-radon</a> — "Radon is the second leading cause of lung cancer and is found at elevated levels in one out of every two Colorado homes."</li>
    <li id="src-2">U.S. Environmental Protection Agency. <em>EPA Map of Radon Zones</em>. <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">epa.gov/radon/epa-map-radon-zones</a> — Zone classifications verified from EPA's downloadable county-level spreadsheet linked on this page.</li>
    <li id="src-3">U.S. EPA. <em>What is EPA's action level for radon and what does it mean?</em> <a href="{s('epa_action_level_def')}" rel="noopener" target="_blank">epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean</a></li>
    <li id="src-4">Colorado Environmental Public Health Tracking. <em>Radon data: county-level test results</em>. <a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">coepht.colorado.gov/radon-data</a></li>
    <li id="src-5">Colorado Department of Regulatory Agencies. <em>Office of Radon Professionals</em>. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a> — statewide licensing under 4 CCR 754-1, effective July 1, 2022.</li>
    <li id="src-6">Colorado General Assembly. <em>SB23-206: Concerning measures to mitigate the effects of radon in residential properties</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a> — approved June 5, 2023; effective August 7, 2023.</li>
    <li id="src-7">City and County of Denver. <em>Community Planning and Development</em>. <a href="{s('denver_cpd')}" rel="noopener" target="_blank">denvergov.org Community Planning and Development</a></li>
    <li id="src-8">Denver Department of Public Health and Environment. <em>Radon</em>. <a href="{s('denver_radon')}" rel="noopener" target="_blank">denvergov.org DDPHE Radon</a> — "The EPA has ranked Denver as 'Zone 1,' which means the average house will likely exceed the EPA's action level of 4.0 pCi/L." DDPHE also recommends testing every 2-3 years and distributes free test kits to Denver residents while supplies last.</li>
    <li id="src-9">Colorado Department of Public Health and Environment. <em>Half of Colorado homes have elevated radon levels which can cause lung cancer</em> (press release, dateline Denver, January 5, 2026). <a href="{s('cdphe_press_jan26')}" rel="noopener" target="_blank">cdphe.colorado.gov press release</a></li>
    <li id="src-10">Colorado Department of Public Health and Environment. <em>Understanding radon</em>. <a href="{s('cdphe_understanding_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/understanding-radon</a> — "Radon moves from uranium-bearing granite deposits in the soil to the atmosphere."</li>
    <li id="src-11">U.S. Geological Survey. <em>Water Quality in the South Platte River Basin, Colorado, Nebraska, and Wyoming, 1992-95</em>, USGS Circular 1167. <a href="{s('usgs_south_platte_radon')}" rel="noopener" target="_blank">pubs.usgs.gov/circ/circ1167</a> — Dennehy et al., 1998.</li>
    <li id="src-12">U.S. Census Bureau. <em>2019-2023 American Community Survey 5-Year Estimates, Table DP04 (Selected Housing Characteristics)</em> for Denver County, Colorado (FIPS 08031). <a href="{s('census_acs_denver_dp04')}" rel="noopener" target="_blank">data.census.gov ACS DP04 Denver</a></li>
  </ol>
</aside>
"""


def denver_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Is radon actually a problem in Denver?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. Denver County and every Denver Metro county is classified by the EPA as Zone 1 — the highest predicted indoor-radon category. CDPHE reports that about one in two Colorado homes test above the EPA action level of 4.0 pCi/L. The CDPHE COEPHT dataset publishes county-level summaries. Test your home to find out where your specific house stands."}},
            {"@type": "Question", "name": "Where can I get a Denver radon test kit?",
             "acceptedAnswer": {"@type": "Answer", "text": "Mail-order test kits sold by CDPHE-affiliated programs and national labs, retail kits at hardware stores, and DIY kits from radon-equipment websites. Costs are usually $15-$35 for a short-term kit and $20-$50 for a long-term kit including lab analysis. For a real estate transaction the test must be performed by a professional certified through NRPP or NRSB and registered with Colorado DORA."}},
            {"@type": "Question", "name": "Does Denver require a permit to install a radon mitigation system?",
             "acceptedAnswer": {"@type": "Answer", "text": "Mechanical, electrical, and exhaust work on a mitigation system is generally permitted work in any Colorado jurisdiction. The City and County of Denver handles permits through Denver Community Planning and Development. Suburban metro jurisdictions each issue their own building permits. A licensed Colorado radon contractor should pull the required permit; the permit should be itemized in the written quote."}},
            {"@type": "Question", "name": "How long does radon mitigation take in a Denver home?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most single-family installs take one day on site. Add scheduling lead time on the front end and a 2 to 7 day post-mitigation test on the back end. A reasonable end-to-end timeline from signed quote to verified system is one to two weeks. Finished-basement homes can extend to a second day."}},
            {"@type": "Question", "name": "I'm in Aurora, Lakewood, Boulder, or another Denver Metro suburb. Is this page relevant?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. All Denver Metro counties are EPA Zone 1, the statewide testing and disclosure rules are identical, and the underlying mitigation science is the same. What changes by city is which permitting office issues the permit and the contractor's drive time. The quote form lets you select Denver Metro or Other Colorado area and capture your ZIP."}},
            {"@type": "Question", "name": "Why doesn't this page publish a Denver-specific mitigation cost?",
             "acceptedAnswer": {"@type": "Answer", "text": "Because we don't have a rigorous Denver-specific cost sample to stand behind, and inventing a number would be worse than referring to the statewide CDPHE figure and the underlying cost drivers. The statewide cost anchor is the CDPHE $1,000-$2,000 range plus a four-scenario framework. When we have a sound Denver dataset we will publish it."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
