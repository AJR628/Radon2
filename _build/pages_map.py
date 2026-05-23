"""Content for /colorado-radon-map/ — Colorado Radon Map landing page.

One new page:
  /colorado-radon-map/   — what the EPA Map of Radon Zones means for Colorado,
                          how to read it, what it does not tell you, and where
                          to go next. Pairs the EPA zone map with CDPHE
                          county-level test data (COEPHT 2005-2017).
"""
import json
from pages_main import s, SOURCES

# Register the new source URLs used on this page (idempotent).
SOURCES.setdefault("epa_map_radon_zones", "https://www.epa.gov/radon/epa-map-radon-zones")
SOURCES.setdefault("epa_action_level_def", "https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean")
SOURCES.setdefault("cdphe_testing", "https://cdphe.colorado.gov/hm/testing-your-home-radon")
SOURCES.setdefault("coepht_radon_data", "https://coepht.colorado.gov/radon-data")
SOURCES.setdefault("coepht_radon_viz", "https://cohealthviz.dphe.state.co.us/t/EnvironmentalEpidemiologyPublic/views/Radon/RadonMeasures")
SOURCES.setdefault("epa_health_risk_radon", "https://www.epa.gov/radon/health-risk-radon")


# =========================================================================
# The Colorado map — inline SVG visualization.
#
# Geographic facts:
#   Colorado bounded by 37N-41N latitude, 102.03W-109.03W longitude.
#   Projects to a near-perfect rectangle. 64 counties total.
#   EPA Map of Radon Zones (1993) classifies:
#     - 53 counties as Zone 1 (highest predicted indoor radon >4 pCi/L avg)
#     - 11 counties as Zone 2 (moderate, 2-4 pCi/L avg)
#     - 0  counties as Zone 3 (low, <2 pCi/L avg)
#
# The 11 Zone 2 counties cluster into four geographic regions:
#   - NW corner:           Routt
#   - Central Mountains:   Eagle
#   - SW San Juan Mtns:    Hinsdale, Mineral, San Juan
#   - San Luis Valley:     Alamosa, Conejos, Costilla, Rio Grande, Saguache,
#                          Archuleta (Pagosa Springs)
#
# The SVG below is a stylized representation - state outline + region
# highlights + reference cities. It is NOT a literal cartographic rendering;
# the caption makes that clear and links to the source EPA map.
# =========================================================================
COLORADO_MAP_SVG = """
<svg viewBox="0 0 800 540" xmlns="http://www.w3.org/2000/svg" role="img"
     aria-labelledby="co-map-title co-map-desc" class="co-map">
  <title id="co-map-title">Colorado radon zones map (stylized)</title>
  <desc id="co-map-desc">A stylized map of Colorado showing the EPA Radon Zone classification. Fifty-three of Colorado's sixty-four counties are Zone 1 (highest predicted indoor radon). Eleven counties are Zone 2 (moderate). Zero are Zone 3. The eleven Zone 2 counties cluster in four geographic regions: Routt in the northwest, Eagle in the central mountains, Hinsdale Mineral and San Juan in the southwest San Juan Mountains, and Alamosa Conejos Costilla Rio Grande Saguache and Archuleta in the San Luis Valley and southern border region.</desc>

  <!-- State background (Zone 1 default) -->
  <rect x="40" y="60" width="720" height="420" rx="8" ry="8"
        fill="#c97a52" fill-opacity="0.62" stroke="#8e3d22" stroke-width="2"/>

  <!-- Zone 2 region: Routt (NW) -->
  <ellipse cx="200" cy="155" rx="58" ry="42" fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a" stroke-width="1.5"/>
  <text x="200" y="159" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="12" font-weight="600" fill="#14181c">Routt</text>

  <!-- Zone 2 region: Eagle (central mountains) -->
  <ellipse cx="330" cy="230" rx="52" ry="38" fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a" stroke-width="1.5"/>
  <text x="330" y="234" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="12" font-weight="600" fill="#14181c">Eagle</text>

  <!-- Zone 2 region: SW San Juan Mtns (Hinsdale, Mineral, San Juan) -->
  <ellipse cx="245" cy="370" rx="74" ry="48" fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a" stroke-width="1.5"/>
  <text x="245" y="365" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="11" font-weight="600" fill="#14181c">Hinsdale · Mineral</text>
  <text x="245" y="380" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="11" font-weight="600" fill="#14181c">San Juan</text>

  <!-- Zone 2 region: San Luis Valley + Archuleta (south central) -->
  <path d="M 200 440 Q 220 410 280 420 Q 350 415 410 430 Q 430 445 410 465 Q 380 470 330 467 Q 270 470 220 465 Q 195 460 200 440 Z"
        fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a" stroke-width="1.5"/>
  <text x="305" y="442" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="11" font-weight="600" fill="#14181c">San Luis Valley + Archuleta</text>
  <text x="305" y="457" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="10" fill="#14181c">Alamosa · Conejos · Costilla</text>
  <text x="305" y="470" text-anchor="middle" font-family="Inter, sans-serif"
        font-size="10" fill="#14181c">Rio Grande · Saguache · Archuleta</text>

  <!-- Reference cities (orientation only) -->
  <!-- Denver -->
  <circle cx="540" cy="200" r="5" fill="#14385a" stroke="#fff" stroke-width="1.5"/>
  <text x="552" y="204" font-family="Inter, sans-serif" font-size="12"
        font-weight="600" fill="#14181c">Denver</text>

  <!-- Colorado Springs -->
  <circle cx="555" cy="265" r="5" fill="#14385a" stroke="#fff" stroke-width="1.5"/>
  <text x="567" y="269" font-family="Inter, sans-serif" font-size="12"
        font-weight="600" fill="#14181c">Colorado Springs</text>

  <!-- Pueblo -->
  <circle cx="565" cy="320" r="4" fill="#14385a" stroke="#fff" stroke-width="1.5"/>
  <text x="577" y="324" font-family="Inter, sans-serif" font-size="11"
        fill="#14181c">Pueblo</text>

  <!-- Grand Junction -->
  <circle cx="155" cy="240" r="4" fill="#14385a" stroke="#fff" stroke-width="1.5"/>
  <text x="165" y="244" font-family="Inter, sans-serif" font-size="11"
        fill="#14181c">Grand Junction</text>

  <!-- Durango -->
  <circle cx="190" cy="445" r="4" fill="#14385a" stroke="#fff" stroke-width="1.5"/>
  <text x="120" y="449" font-family="Inter, sans-serif" font-size="11"
        fill="#14181c">Durango</text>

  <!-- N compass arrow -->
  <g transform="translate(70, 90)">
    <path d="M 0 0 L 5 12 L 0 9 L -5 12 Z" fill="#14181c"/>
    <text x="0" y="26" text-anchor="middle" font-family="Inter, sans-serif"
          font-size="10" font-weight="600" fill="#14181c">N</text>
  </g>

  <!-- Title at top -->
  <text x="400" y="38" text-anchor="middle" font-family="Fraunces, serif"
        font-size="20" font-weight="600" fill="#14181c">EPA Radon Zones in Colorado</text>

  <!-- Legend -->
  <g transform="translate(40, 500)">
    <rect x="0" y="0" width="22" height="14" fill="#c97a52" fill-opacity="0.62" stroke="#8e3d22"/>
    <text x="30" y="11" font-family="Inter, sans-serif" font-size="12" fill="#14181c">
      Zone 1 — highest predicted radon (53 counties)
    </text>
    <rect x="380" y="0" width="22" height="14" fill="#e5b86f" fill-opacity="0.95" stroke="#8a6d1a"/>
    <text x="410" y="11" font-family="Inter, sans-serif" font-size="12" fill="#14181c">
      Zone 2 — moderate (11 counties)
    </text>
  </g>
</svg>
"""


# =========================================================================
# /colorado-radon-map/  -- main body
# =========================================================================
COLORADO_MAP_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you searched for a Colorado radon map, you probably want a quick visual answer to one of two questions: <em>is my area high risk?</em> or <em>how worried should I be about radon in Colorado?</em> The honest answer to both is the same: <strong>almost all of Colorado is classified as the EPA's highest indoor-radon zone</strong> — and even in the eleven counties that aren't, CDPHE still says about <strong>one in two Colorado homes</strong> tests above the EPA action level.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
    <p>This page walks through what the EPA Map of Radon Zones actually shows, where to read Colorado-specific county data, and — most importantly — what the map <em>does not</em> tell you about your specific home.</p>
  </div>
</section>

<section>
  <h2>The Colorado radon zones map</h2>
  <figure class="figure co-map-figure">
    {COLORADO_MAP_SVG}
    <figcaption>
      <strong>Stylized Colorado radon zones.</strong> Out of Colorado's 64 counties, 53 are classified as Zone 1 (highest predicted indoor radon) and 11 are Zone 2 (moderate). Zero counties are Zone 3. The 11 Zone 2 counties cluster in four geographic regions: Routt in the northwest, Eagle in the central mountains, the southwest San Juan Mountains (Hinsdale, Mineral, San Juan), and the San Luis Valley plus Archuleta County in the south. This is a stylized visualization for orientation, not a literal cartographic rendering. Classification source: <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">EPA Map of Radon Zones</a>. <strong>This map is not a substitute for testing your specific home — EPA recommends every home be tested regardless of zone.</strong><sup><a href="#src-3">[3]</a></sup>
    </figcaption>
  </figure>
  <div class="prose-wide">
    <p>The Map of Radon Zones was developed by the U.S. Environmental Protection Agency in 1993 using indoor radon measurements, geology, aerial radioactivity, soil parameters, and foundation types. EPA's own description is unambiguous: the map "is intended to help governments and other organizations target risk-reduction activities and resources" and "should not be used to determine if individual homes need to be tested."<sup><a href="#src-3">[3]</a></sup> EPA recommends every home be tested for radon, no matter where it is.</p>
  </div>
</section>

<section>
  <h2>How to read EPA radon zones</h2>
  <div class="prose-wide">
    <p>EPA divides U.S. counties into three zones based on predicted average indoor radon levels:</p>
    <table class="compact">
      <thead>
        <tr><th>Zone</th><th>Predicted average indoor radon</th><th>What it means</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Zone 1</strong></td>
          <td>Greater than 4.0 pCi/L</td>
          <td>Highest predicted potential. Building codes in Zone 1 counties commonly require new construction radon-resistant features.</td>
        </tr>
        <tr>
          <td><strong>Zone 2</strong></td>
          <td>Between 2.0 and 4.0 pCi/L</td>
          <td>Moderate predicted potential. Still requires testing — many homes here come back above 4.0 pCi/L.</td>
        </tr>
        <tr>
          <td><strong>Zone 3</strong></td>
          <td>Less than 2.0 pCi/L</td>
          <td>Lowest predicted potential. EPA still recommends testing every home.</td>
        </tr>
      </tbody>
    </table>
    <p>Two things to keep in mind when reading the map:</p>
    <ul>
      <li><strong>The zone is an average across an entire county</strong> — not a verdict on any one home. Homes within a single county can vary from below 1 pCi/L to above 40 pCi/L depending on geology under the lot, foundation type, and construction.</li>
      <li><strong>The map is from 1993</strong> and has not been updated. EPA itself recommends pairing it with local data. For Colorado, that local data comes from the Colorado Department of Public Health and Environment (CDPHE) and from county-level testing results published by the Colorado Environmental Public Health Tracking program (COEPHT).<sup><a href="#src-2">[2]</a></sup><sup><a href="#src-4">[4]</a></sup></li>
    </ul>
  </div>
</section>

<section>
  <h2>Why most of Colorado is Zone 1</h2>
  <div class="prose-wide">
    <p>Colorado's geology is the short answer. The Rocky Mountain uplift produced uranium-bearing granites — particularly the Pikes Peak granite that underlies much of the Front Range — and Cretaceous-era sediments like the Pierre Shale that contain trace uranium. Uranium decays slowly through a chain of radioactive elements, eventually producing radon-222, the gas we test for. Where uranium is concentrated in bedrock, radon is concentrated in soil gas above it.</p>
    <p>That's why 53 of Colorado's 64 counties — the Front Range corridor, the eastern plains, and most of the western slope — sit in EPA Zone 1. It's not just elevation; it's the specific rock chemistry under those counties. The deeper geological story is on our <a href="/radon-basics/why-common-in-colorado/">Why radon is common in Colorado</a> page.</p>
  </div>
</section>

<section>
  <h2>The 11 Colorado counties classified as Zone 2</h2>
  <div class="prose-wide">
    <p>The eleven Zone 2 counties are not "safer" — they're just <em>less consistently elevated on average</em>. CDPHE's statement that <strong>radon is found at elevated levels in one out of every two Colorado homes</strong> applies statewide, including Zone 2 counties.<sup><a href="#src-2">[2]</a></sup></p>
    <p>The 11 Zone 2 counties cluster geographically in four regions:</p>
    <table class="compact">
      <thead>
        <tr><th>Region</th><th>Counties</th><th>What's there</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Northwest Colorado</td>
          <td>Routt</td>
          <td>Steamboat Springs and the Yampa Valley.</td>
        </tr>
        <tr>
          <td>Central Mountains</td>
          <td>Eagle</td>
          <td>Vail, Eagle, the upper Eagle River valley.</td>
        </tr>
        <tr>
          <td>Southwest San Juan Mountains</td>
          <td>Hinsdale, Mineral, San Juan</td>
          <td>Silverton, Lake City, Creede — high-elevation mountain counties.</td>
        </tr>
        <tr>
          <td>San Luis Valley + Archuleta</td>
          <td>Alamosa, Conejos, Costilla, Rio Grande, Saguache, Archuleta</td>
          <td>The San Luis Valley basin and Pagosa Springs area along the southern border.</td>
        </tr>
      </tbody>
    </table>
    <p>Why are these counties lower-average on the EPA's classification? The underlying geology differs from the Front Range uranium-bearing granites. The San Luis Valley sits on layered sediments deposited by the Rio Grande Rift; the high-elevation mountain counties have different bedrock chemistry; some of these counties also have very low population density and small testing-volume samples, which can influence the classification. Important: even with that, individual homes in Zone 2 counties absolutely can — and routinely do — test above 4.0 pCi/L. The map is a planning tool, not a per-home result.</p>
  </div>
</section>

<section>
  <h2>Beyond EPA zones: Colorado county-level test results</h2>
  <div class="prose-wide">
    <p>EPA zones are a 30-year-old planning classification. If you want a sharper signal about actual radon levels in a specific Colorado county, the Colorado Environmental Public Health Tracking program (COEPHT) publishes county-level summaries of <strong>real radon test results</strong> submitted to the state. The COEPHT dataset covers tests from 2005-2017 and includes two measures by county: average indoor radon value and percent of measurements over 4 pCi/L.<sup><a href="#src-4">[4]</a></sup></p>
    <p>Two caveats to read alongside the COEPHT data:</p>
    <ul>
      <li><strong>Sample sizes vary widely.</strong> Front Range counties with high population (El Paso, Denver, Jefferson, Larimer, Weld, Arapahoe, Boulder) have thousands of test results. Some rural counties have only dozens, which makes the percentages less reliable for those counties.</li>
      <li><strong>The data is self-selected.</strong> Test results were submitted voluntarily by homeowners, contractors, and labs. Homes that tested low and never followed up are still counted; homes that were never tested are not represented at all. The actual statewide rate is likely close to CDPHE's "one in two" headline, but per-county percentages should be read as one data point, not gospel.</li>
    </ul>
    <p>You can browse the COEPHT data two ways:</p>
    <ul>
      <li><a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">COEPHT radon data hub</a> — methodology page with downloadable county-level dataset.</li>
      <li><a href="{s('coepht_radon_viz')}" rel="noopener" target="_blank">COEPHT interactive radon map (Tableau)</a> — the official Colorado map visualization with county-level average and percent-elevated overlays.</li>
    </ul>
    <p>For El Paso County specifically — the Colorado Springs region — El Paso County Public Health reports that <strong>over 40 percent of all homes tested between 2005 and 2023 in El Paso County had high levels of radon</strong>.<sup><a href="#src-5">[5]</a></sup> That's more recent than the 2005-2017 COEPHT cutoff, and it's tracked at the county level rather than the EPA zone level. If you live in El Paso County, that 40%+ number is the more accurate signal than the EPA Zone 1 classification.</p>
  </div>
</section>

<section>
  <h2>What the map does not tell you</h2>
  <div class="callout">
    <strong>Important.</strong> The EPA Radon Zone map is a <em>planning tool</em>. It tells governments and code officials where to focus radon programs. It does not tell you whether your individual home has elevated radon. That requires a test.<sup><a href="#src-3">[3]</a></sup>
  </div>
  <div class="prose-wide">
    <p>Specifically, the map cannot tell you:</p>
    <ul>
      <li><strong>Your specific home's radon level.</strong> Homes a block apart routinely test differently. Two adjacent lots can have different bedrock chemistry, different foundation construction, and different stack-effect pressure profiles.</li>
      <li><strong>Whether your neighborhood differs from the county average.</strong> Some neighborhoods built on different sediments have systematically different averages. Some new-construction subdivisions have passive radon-resistant systems built in (IRC Appendix BE) that can be activated cheaply if needed. <a href="/radon-mitigation-systems/passive-vs-active/">Passive vs active systems &rarr;</a></li>
      <li><strong>How your home's foundation type affects entry.</strong> A walk-out basement on a slope behaves differently from a fully buried basement; a crawlspace behaves differently again. <a href="/radon-basics/by-foundation-type/">Radon by foundation type &rarr;</a></li>
      <li><strong>Whether seasonal patterns matter.</strong> Colorado's winter heating season concentrates radon indoors via the stack effect — a long-term test (90+ days) catches that variability that a short-term snapshot will miss. <a href="/radon-testing/short-term-vs-long-term/">Short-term vs long-term tests &rarr;</a></li>
    </ul>
    <p>EPA's recommendation has not changed in 30 years: <strong>test every home, regardless of zone</strong>. CDPHE's recommendation matches it. The map is useful for understanding why Colorado has a radon problem in the first place. It's not useful as a substitute for testing your specific house.</p>
  </div>
</section>

<section>
  <h2>What to do next</h2>
  <div class="prose-wide">
    <p>Use the table below to pick the right starting point for your situation:</p>
    <table>
      <thead>
        <tr><th>Your situation</th><th>Start here</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>I haven't tested my home yet</td>
          <td><a href="/radon-testing/">How to test for radon in Colorado</a></td>
        </tr>
        <tr>
          <td>I want to understand what a high result means before testing</td>
          <td><a href="/radon-basics/levels-explained/">Radon levels explained (2, 4, 10, 20 pCi/L)</a></td>
        </tr>
        <tr>
          <td>I got a high test result</td>
          <td><a href="/colorado-springs/failed-radon-test/">Failed radon test next steps (Colorado Springs)</a></td>
        </tr>
        <tr>
          <td>I have a mitigation quote and want to evaluate it</td>
          <td><a href="/radon-mitigation-cost/quote-too-high/">Is my radon mitigation quote too high?</a></td>
        </tr>
        <tr>
          <td>I'm buying or selling a home in Colorado</td>
          <td><a href="/radon-testing/during-real-estate-transactions/">Radon testing during a real estate transaction (SB23-206)</a></td>
        </tr>
        <tr>
          <td>I want a quote from a licensed Colorado contractor</td>
          <td><a href="/request-quote/">Request a quote</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Colorado Springs and El Paso County</h2>
  <div class="prose-wide">
    <p>If you're in or around Colorado Springs, El Paso County is in <strong>EPA Zone 1</strong> and has the most pointed county-level data in Colorado: over 40 percent of homes tested between 2005 and 2023 had elevated radon, per El Paso County Public Health.<sup><a href="#src-5">[5]</a></sup> Our local pages cover testing kits, mitigation cost ranges by foundation scenario, and what to do after a failed test:</p>
    <ul>
      <li><a href="/colorado-springs/"><strong>Colorado Springs radon hub</strong></a> — local prevalence, EPCPH lab kits, contractor verification, SB23-206 real estate context.</li>
      <li><a href="/colorado-springs/radon-testing/"><strong>Radon testing in Colorado Springs</strong></a> — where to get a kit, where to place it, what to do with the result.</li>
      <li><a href="/colorado-springs/radon-mitigation-cost/"><strong>Mitigation cost in Colorado Springs</strong></a> — local quote ranges by scenario ($900-$4,800 depending on foundation).</li>
      <li><a href="/colorado-springs/failed-radon-test/"><strong>Failed radon test next steps</strong></a> — step-by-step playbook for elevated results.</li>
    </ul>
    <p>The Front Range north and west of Colorado Springs — Denver, Jefferson, Boulder, Larimer, Weld counties — all sit in EPA Zone 1 as well. We'll add city-specific hubs for these regions as the site expands.</p>
  </div>
</section>

<section>
  <h2>Frequently asked questions</h2>

  <details>
    <summary>Is my Colorado county high-risk for radon according to the EPA map?</summary>
    <p>Probably. The EPA Map of Radon Zones classifies 53 of Colorado's 64 counties as Zone 1 (highest predicted indoor radon). The 11 Zone 2 counties are Alamosa, Archuleta, Conejos, Costilla, Eagle, Hinsdale, Mineral, Rio Grande, Routt, Saguache, and San Juan. There are no Zone 3 counties in Colorado. Even if your county is Zone 2, CDPHE still recommends testing because about one in two Colorado homes statewide test above the EPA action level.</p>
  </details>

  <details>
    <summary>If my county is EPA Zone 2, is my home safe from radon?</summary>
    <p>No. Zone 2 means the predicted county average is between 2.0 and 4.0 pCi/L, not that homes there are safe. Individual homes in Zone 2 counties routinely test above 4.0 pCi/L — sometimes well above. EPA's own guidance is that the zone map should not be used to decide whether to test an individual home. Every home should be tested.</p>
  </details>

  <details>
    <summary>Why hasn't EPA updated the Colorado radon map since 1993?</summary>
    <p>The Map of Radon Zones was published in 1993 to help governments and code officials target radon programs. EPA's position is that the map served its purpose as a planning tool and that updated, finer-grained data is now better captured at the state and county level. For Colorado-specific results, the COEPHT dataset (county-level test results 2005-2017) and CDPHE's current statewide guidance are more accurate than re-running the EPA zone classification would be.</p>
  </details>

  <details>
    <summary>Can I see Colorado radon test results by county?</summary>
    <p>Yes. The Colorado Environmental Public Health Tracking (COEPHT) program publishes county-level radon test summaries based on actual test results submitted from 2005-2017. Two measures are available: average indoor radon and percent of measurements over 4 pCi/L. The data is available as a downloadable file and as an interactive Tableau map visualization. Note that some rural counties have small sample sizes; the data is most reliable for Front Range counties with high test volume.</p>
  </details>

  <details>
    <summary>What's the difference between the EPA radon zones and CDPHE data?</summary>
    <p>The EPA Map of Radon Zones is a 1993 planning classification — it grouped U.S. counties into three zones based on geology, soil parameters, foundation types, and indoor measurements available at the time. CDPHE data (and the COEPHT dataset) is based on actual indoor radon test results submitted by Colorado homeowners, contractors, and labs from 2005 onward. The CDPHE data is more current and more granular but is also self-selected (only includes homes that were tested). Both data sources point in the same direction: roughly half of Colorado homes test above the EPA action level of 4.0 pCi/L.</p>
  </details>

  <details>
    <summary>If Colorado has so much radon, should I be alarmed?</summary>
    <p>Concerned, not alarmed. Radon is real — it's the second leading cause of lung cancer in the U.S. and the leading cause among non-smokers. But it's also one of the most testable and most fixable indoor air-quality problems. A short-term test kit costs $15-$30 from the El Paso County Public Health lab or CDPHE. If your result comes back above 4.0 pCi/L, a typical Colorado mitigation system runs roughly $1,000-$2,000 per CDPHE, and a properly designed system reduces indoor radon by 80-99 percent. The right framing is: test, find out where you are, and then make a decision with real data instead of a 30-year-old zone classification.</p>
  </details>

  <details>
    <summary>Where does the EPA radon zone map come from?</summary>
    <p>The map was developed by the EPA in 1993 using a combination of indoor radon measurements available at the time, regional geology surveys, aerial radioactivity data (radiation surveys flown by aircraft for the U.S. Department of Energy), soil parameter data, and foundation-type distribution by region. It's intended as a planning tool for governments and code officials targeting radon resources. The full methodology and the underlying state-level supporting documents are available on the <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">EPA Map of Radon Zones page</a>.</p>
  </details>
</section>

<section>
  <div class="callout">
    <strong>One more time, because it matters.</strong> The Colorado Radon Map on this page is a stylized visualization of the EPA's 1993 Map of Radon Zones. <strong>It is not a substitute for testing your specific home.</strong> EPA, CDPHE, and El Paso County Public Health all recommend the same thing: test your home for radon, no matter what your county's zone is. A short-term test kit costs about $15 from the El Paso County Public Health lab. <a href="/radon-testing/">How to test for radon in Colorado &rarr;</a>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>EPA Map of Radon Zones</em>. <a href="{s('epa_map_radon_zones')}" rel="noopener" target="_blank">epa.gov/radon/epa-map-radon-zones</a></li>
    <li id="src-2">Colorado Department of Public Health and Environment. <em>Testing your home for radon</em>. <a href="{s('cdphe_testing')}" rel="noopener" target="_blank">cdphe.colorado.gov/hm/testing-your-home-radon</a></li>
    <li id="src-3">U.S. EPA. <em>What is EPA's action level for radon and what does it mean?</em> <a href="{s('epa_action_level_def')}" rel="noopener" target="_blank">epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean</a></li>
    <li id="src-4">Colorado Environmental Public Health Tracking. <em>Radon data: county-level test results 2005-2017</em>. <a href="{s('coepht_radon_data')}" rel="noopener" target="_blank">coepht.colorado.gov/radon-data</a></li>
    <li id="src-5">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-6">U.S. EPA. <em>Health risk of radon</em>. <a href="{s('epa_health_risk_radon')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
  </ol>
</aside>
"""


def colorado_map_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Is my Colorado county high-risk for radon according to the EPA map?",
             "acceptedAnswer": {"@type": "Answer", "text": "Probably. The EPA Map of Radon Zones classifies 53 of Colorado's 64 counties as Zone 1 (highest predicted indoor radon). The 11 Zone 2 counties are Alamosa, Archuleta, Conejos, Costilla, Eagle, Hinsdale, Mineral, Rio Grande, Routt, Saguache, and San Juan. There are no Zone 3 counties in Colorado. Even if your county is Zone 2, CDPHE still recommends testing because about one in two Colorado homes statewide test above the EPA action level."}},
            {"@type": "Question", "name": "If my county is EPA Zone 2, is my home safe from radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Zone 2 means the predicted county average is between 2.0 and 4.0 pCi/L, not that homes there are safe. Individual homes in Zone 2 counties routinely test above 4.0 pCi/L. EPA's own guidance is that the zone map should not be used to decide whether to test an individual home. Every home should be tested."}},
            {"@type": "Question", "name": "Why hasn't EPA updated the Colorado radon map since 1993?",
             "acceptedAnswer": {"@type": "Answer", "text": "The Map of Radon Zones was published in 1993 to help governments and code officials target radon programs. EPA's position is that the map served its purpose as a planning tool and that updated, finer-grained data is now better captured at the state and county level. For Colorado-specific results, the COEPHT dataset (county-level test results 2005-2017) and CDPHE's current statewide guidance are more accurate than re-running the EPA zone classification would be."}},
            {"@type": "Question", "name": "Can I see Colorado radon test results by county?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. The Colorado Environmental Public Health Tracking (COEPHT) program publishes county-level radon test summaries based on actual test results submitted from 2005-2017. Two measures are available: average indoor radon and percent of measurements over 4 pCi/L. The data is available as a downloadable file and as an interactive Tableau map visualization."}},
            {"@type": "Question", "name": "What's the difference between EPA radon zones and CDPHE data?",
             "acceptedAnswer": {"@type": "Answer", "text": "The EPA Map of Radon Zones is a 1993 planning classification grouping U.S. counties into three zones based on geology, soil parameters, foundation types, and indoor measurements available at the time. CDPHE data and the COEPHT dataset are based on actual indoor radon test results submitted by Colorado homeowners, contractors, and labs from 2005 onward. The CDPHE data is more current and more granular but is also self-selected. Both point in the same direction: roughly half of Colorado homes test above the EPA action level."}},
            {"@type": "Question", "name": "If Colorado has so much radon, should I be alarmed?",
             "acceptedAnswer": {"@type": "Answer", "text": "Concerned, not alarmed. Radon is real and is the second leading cause of lung cancer in the U.S. But it is also one of the most testable and most fixable indoor air-quality problems. A short-term test kit costs $15-$30, a typical Colorado mitigation system runs roughly $1,000-$2,000 per CDPHE, and a properly designed system reduces indoor radon by 80-99 percent."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
