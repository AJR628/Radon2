"""Content for the Radon Basics pillar pages (Phase 5a build).

Six pages:
1. /radon-basics/                                    — hub (What Is Radon?)
2. /radon-basics/why-common-in-colorado/             — Colorado geology
3. /radon-basics/how-it-enters-homes/                — Entry pathways
4. /radon-basics/health-risks/                       — EPA/CDC/WHO data
5. /radon-basics/levels-explained/                   — pCi/L brackets
6. /radon-basics/by-foundation-type/                 — Basement, crawlspace, slab, walk-out, tri-level
"""
import json
from pages_main import s, SOURCES

# Ensure needed sources registered (idempotent)
SOURCES.setdefault("epa_citizens_guide", "https://www.epa.gov/radon/citizens-guide-radon")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")
SOURCES.setdefault("epa_health_risk", "https://www.epa.gov/radon/health-risk-radon")
SOURCES.setdefault("who_radon", "https://www.who.int/news-room/fact-sheets/detail/radon-and-health")
SOURCES.setdefault("surgeon_general_radon", "https://www.surgeongeneral.gov/")
SOURCES.setdefault("colorado_geological", "https://coloradogeologicalsurvey.org/")
SOURCES.setdefault("usgs_radon", "https://www.usgs.gov/")
SOURCES.setdefault("atsdr_radon", "https://www.atsdr.cdc.gov/")
SOURCES.setdefault("aarst_standards", "https://standards.aarst.org/")


# =========================================================================
# 1. /radon-basics/   — HUB: What Is Radon?
# =========================================================================
BASICS_HUB_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Radon is a naturally occurring radioactive gas — invisible, odorless, tasteless. It comes from the decay of uranium in the soil and rock beneath your home, and it's measured in units of picocuries per liter of air (pCi/L). Outdoor air averages around 0.4 pCi/L. Indoor air in Colorado averages much higher, and roughly half of Colorado homes test above the EPA's action level of 4.0 pCi/L.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This page is the plain-language introduction. We'll cover what radon actually is, where it comes from, how it's measured, and why it matters. The companion pages in this section go deeper on the Colorado-specific geology, how radon enters homes, what the health risks are, and what your specific test number means.</p>
  </div>
</section>

<section>
  <h2>The short version</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Radon is a radioactive gas</strong> produced by the natural decay of uranium in soil and rock.</li>
      <li><strong>It's invisible and odorless.</strong> You can't tell it's there without a test.</li>
      <li><strong>It accumulates in lower levels of homes</strong> — basements first, then living areas above.</li>
      <li><strong>It's the #1 cause of lung cancer in non-smokers</strong> and the #2 cause overall (after smoking).<sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>The EPA action level is 4.0 pCi/L.</strong> CDPHE recommends mitigation at or above this level.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Roughly half of Colorado homes test above the action level.</strong></li>
    </ul>
  </div>
</section>

<section>
  <h2>Where radon comes from</h2>
  <div class="prose-wide">
    <p>Radon is part of a chain of radioactive decay that starts with <strong>uranium-238</strong>, an element that exists naturally in trace amounts in most rocks and soils. Over billions of years, uranium-238 slowly decays through a series of other radioactive elements:</p>
    <ul>
      <li><strong>Uranium-238</strong> (half-life ~4.5 billion years) decays into Thorium-234.</li>
      <li>Through a series of intermediate steps, the chain produces <strong>Radium-226</strong>.</li>
      <li>Radium-226 (half-life ~1,600 years) decays into <strong>Radon-222</strong>.</li>
      <li>Radon-222 (half-life ~3.8 days) is the gas we test for. It decays further into "radon progeny" — short-lived radioactive particles that are actually what causes the lung damage.</li>
    </ul>
    <p>The chain matters because <strong>uranium is everywhere in trace amounts</strong>, so radon is everywhere in trace amounts. Some rocks and soils have more uranium than others. Colorado's geology — particularly the Front Range — has more than most.<sup><a href="#src-4">[4]</a></sup></p>
  </div>
</section>

<section>
  <h2>How radon is measured</h2>
  <div class="prose-wide">
    <p>In the United States, radon is measured in <strong>picocuries per liter of air (pCi/L)</strong>. A picocurie is a measure of radioactivity — specifically, the rate at which radon atoms are decaying in a given volume of air.</p>
    <p>In most of the world outside the U.S., radon is measured in <strong>becquerels per cubic meter (Bq/m³)</strong>. The conversion: 1 pCi/L ≈ 37 Bq/m³.</p>
    <table class="compact">
      <thead>
        <tr><th>Unit</th><th>Equivalent</th><th>Used by</th></tr>
      </thead>
      <tbody>
        <tr><td>4.0 pCi/L</td><td>~148 Bq/m³</td><td>EPA action level (U.S.)</td></tr>
        <tr><td>2.7 pCi/L</td><td>100 Bq/m³</td><td>WHO reference level (international)</td></tr>
        <tr><td>0.4 pCi/L</td><td>~15 Bq/m³</td><td>Outdoor air average (U.S.)</td></tr>
        <tr><td>1.3 pCi/L</td><td>~48 Bq/m³</td><td>U.S. indoor average</td></tr>
      </tbody>
    </table>
    <p>The U.S. EPA action level (4.0 pCi/L) is higher than the WHO's recommended action level (2.7 pCi/L). Both are based on cancer risk modeling; they differ in how much risk each agency deems acceptable.<sup><a href="#src-2">[2]</a></sup><sup><a href="#src-5">[5]</a></sup></p>
  </div>
</section>

<section>
  <h2>Why radon accumulates indoors</h2>
  <div class="prose-wide">
    <p>The air pressure inside a home is typically slightly lower than the air pressure in the soil beneath the foundation. That small pressure difference, driven by the <strong>stack effect</strong> (warm indoor air rising and creating suction at lower levels) and by HVAC systems, pulls soil gas up through small openings in the foundation: slab cracks, the floor-wall joint, sump pits, plumbing penetrations, and unsealed crawlspace gaps.</p>
    <p>The radon-laden soil gas enters the lower levels of the home and accumulates there. Lower levels (basements, crawlspaces, ground floors of slab homes) test highest. Upper floors test lower because the gas mixes with outdoor air through normal ventilation as it rises.</p>
    <p><a href="/radon-basics/how-it-enters-homes/">Full walkthrough of how radon enters homes &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Why Colorado specifically</h2>
  <div class="prose-wide">
    <p>Colorado has elevated indoor radon for two reasons:</p>
    <ol>
      <li><strong>The geology.</strong> The Front Range and Colorado Plateau contain uranium-bearing granites and shales. Pikes Peak granite, in particular, has uranium-bearing accessory minerals. Uranium in the bedrock means radium in the soil, which means radon in the gas beneath your foundation.<sup><a href="#src-4">[4]</a></sup></li>
      <li><strong>The housing stock.</strong> Most Colorado homes have full or partial basements. Basements concentrate radon. Add high baseline soil gas to homes designed to capture it, and you get the state's high indoor radon prevalence.</li>
    </ol>
    <p><a href="/radon-basics/why-common-in-colorado/">Full Colorado geology and prevalence walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>The health connection</h2>
  <div class="prose-wide">
    <p>The radon gas itself isn't the threat — it's the <strong>radon progeny</strong>, short-lived radioactive particles produced when radon-222 decays. When you breathe air containing radon, the progeny attach to lung tissue and emit alpha radiation, which damages cells and can lead to lung cancer over years of exposure.</p>
    <p>EPA estimates that radon causes roughly <strong>21,000 lung cancer deaths per year</strong> in the United States. About 2,900 of those are among people who never smoked. Among current and former smokers, the risk is multiplied by the synergy between smoking and radon — they're not additive; they're compounding.<sup><a href="#src-2">[2]</a></sup></p>
    <p><a href="/radon-basics/health-risks/">Full health risk walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What to do next</h2>
  <div class="prose-wide">
    <p>The only way to know your home's level is to <strong>test</strong>. Three options for Colorado:</p>
    <ul>
      <li>A short-term DIY kit ($15–$40, El Paso County Public Health Lab or retail).</li>
      <li>A long-term DIY kit ($30–$60, more accurate annual average).</li>
      <li>A professional continuous monitor ($150–$300, standard for real estate transactions).</li>
    </ul>
    <p><a href="/radon-testing/">Full radon testing guide &rarr;</a></p>
    <p>If your test comes back at or above 4.0 pCi/L, the standard response is mitigation. Colorado has state-level radon contractor licensing through DORA, so verification is straightforward. <a href="/radon-contractors/">How to choose a contractor &rarr;</a></p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">U.S. EPA. <em>Health Risk of Radon</em>. <a href="{s('epa_health_risk')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-3">U.S. EPA. <em>Citizen's Guide to Radon</em>. <a href="{s('epa_citizens_guide')}" rel="noopener" target="_blank">epa.gov/radon/citizens-guide-radon</a></li>
    <li id="src-4">Colorado Geological Survey. <a href="{s('colorado_geological')}" rel="noopener" target="_blank">coloradogeologicalsurvey.org</a></li>
    <li id="src-5">World Health Organization. <em>Radon and Health</em>. <a href="{s('who_radon')}" rel="noopener" target="_blank">who.int</a></li>
  </ol>
</aside>
"""


def basics_hub_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What is radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "Radon is a naturally occurring radioactive gas produced by the decay of uranium in soil and rock. It's invisible, odorless, and tasteless. It accumulates in the lower levels of homes (basements, crawlspaces, ground floors of slab homes) and is the #2 cause of lung cancer in the U.S. (after smoking) and #1 in non-smokers. EPA estimates 21,000 lung cancer deaths per year from radon."}},
            {"@type": "Question", "name": "How is radon measured?",
             "acceptedAnswer": {"@type": "Answer", "text": "In the U.S., radon is measured in picocuries per liter (pCi/L). EPA's action level is 4.0 pCi/L. The WHO recommends action at 100 Bq/m³ (about 2.7 pCi/L). Outdoor air averages 0.4 pCi/L; U.S. indoor average is 1.3 pCi/L."}},
            {"@type": "Question", "name": "Why is radon a problem in Colorado specifically?",
             "acceptedAnswer": {"@type": "Answer", "text": "Two reasons. First, Colorado geology — the Front Range and Colorado Plateau have uranium-bearing granites and shales, including Pikes Peak granite. Uranium in bedrock produces radon in soil gas. Second, the housing stock — most Colorado homes have basements, which concentrate radon. Roughly half of Colorado homes test above the EPA action level of 4.0 pCi/L."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 2. /radon-basics/why-common-in-colorado/
# =========================================================================
WHY_COLORADO_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Colorado has higher indoor radon than almost any state in the country. The EPA classifies <strong>53 of Colorado's 64 counties</strong> as Zone 1 — the highest indoor radon potential category — and the other 11 as Zone 2 (moderate). Zero are Zone 3. CDPHE estimates roughly half of Colorado homes test above the EPA action level of 4.0 pCi/L. In El Paso County, more than 40% of homes tested between 2005 and 2023 came back elevated. (See the <a href="/colorado-radon-map/">Colorado Radon Map</a> for the full zone breakdown.)<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
    <p>This isn't a fluke. It's geology, climate, and construction patterns combining to make Colorado one of the most radon-prone places to live in North America. Here's why.</p>
  </div>
</section>

<section>
  <h2>The geology</h2>
  <div class="prose-wide">
    <p>Radon enters homes from the soil and rock beneath the foundation. The amount that enters depends on how much uranium is in that soil and rock — because uranium is the decay-chain parent that ultimately produces radon-222.</p>
    <p>Colorado sits on bedrock with elevated uranium content. The geology breaks down by region:</p>

    <h3>The Front Range</h3>
    <p>The Front Range — the eastern slope of the Rockies that includes Denver, Colorado Springs, Boulder, Fort Collins, and the I-25 corridor — is built on Precambrian granitic basement rock. Two formations matter most:</p>
    <ul>
      <li><strong>Pikes Peak Granite.</strong> The dominant bedrock under Colorado Springs and much of the southern Front Range, dated to roughly 1.08 billion years ago. Pikes Peak granite contains uranium-bearing accessory minerals (zircon, monazite, allanite) that release radon as they slowly decay over geological time.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Pierre Shale.</strong> A Cretaceous marine shale that outcrops in many parts of the Colorado Springs area. Pierre Shale has elevated organic-bound uranium and is a notable radon source where it's near or at the surface.</li>
    </ul>

    <h3>The Colorado Plateau</h3>
    <p>Western Colorado sits on sedimentary rocks of the Colorado Plateau, including the Morrison Formation and the Dakota Sandstone — both known for historical uranium mining (Cold War era). These rocks still contain uranium in trace amounts and contribute to elevated indoor radon in towns like Grand Junction, Montrose, and Durango.</p>

    <h3>Mountain bedrock</h3>
    <p>Higher-elevation Colorado bedrock is a mix of granites, gneisses, and metamorphic rocks. Many of these formations have uranium-bearing minerals as well, contributing to elevated radon in mountain communities — Estes Park, Aspen, Crested Butte, Telluride, and others.</p>
  </div>
</section>

<section>
  <h2>Why El Paso County is on the higher end</h2>
  <div class="prose-wide">
    <p>El Paso County — which includes Colorado Springs, Monument, Fountain, and Manitou Springs — sits directly on Pikes Peak granite, with Pierre Shale outcrops in parts of the eastern county. The combination produces some of the highest indoor radon levels in Colorado:</p>
    <ul>
      <li>El Paso County Public Health: <strong>over 40% of homes tested 2005–2023</strong> had elevated radon.<sup><a href="#src-2">[2]</a></sup></li>
      <li>Many neighborhoods in Colorado Springs (Briargate, Stetson Hills, Black Forest, Falcon, Mountain Shadows, Old Colorado City) consistently see test results above 4.0 pCi/L.</li>
      <li>Test results vary significantly even within a single neighborhood — soil composition, foundation type, and house design all matter. Your neighbor's reading isn't your reading.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The housing stock</h2>
  <div class="prose-wide">
    <p>Geology gives you a high baseline of radon in the soil. The housing stock determines how much of it gets into your living space.</p>
    <p>Colorado homes are particularly prone to indoor radon accumulation because:</p>
    <ul>
      <li><strong>Basements are common.</strong> Approximately one in three Colorado Springs homes has a basement. Basements have the largest soil-contact area of any foundation type, so they capture more soil gas.</li>
      <li><strong>Crawlspaces are common in older neighborhoods.</strong> Crawlspaces (especially unsealed ones) provide an open soil-air pathway directly into the home.</li>
      <li><strong>Tri-level and split-level designs are common.</strong> These create multi-zone foundations where soil gas can enter through any of several pressure points.</li>
      <li><strong>Cold winters mean tight homes.</strong> When you seal a home up against Colorado winters, you reduce air exchange with the outdoors. That makes the stack effect stronger and concentrates whatever radon enters.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Altitude — the part that surprises people</h2>
  <div class="prose-wide">
    <p>Colorado's high elevation doesn't increase indoor radon directly — the gas comes from the soil under your house, not from the air above it. But altitude does affect mitigation. Radon fans lose roughly <strong>4% of their airflow capacity per 1,000 feet of elevation</strong>. At Colorado Springs altitude (about 6,000 feet), a fan that's sized for a sea-level install loses roughly 24% of its rated capacity. <a href="/radon-mitigation-systems/fans-pipes-suction-points/">More on altitude correction &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What this means for Colorado homeowners</h2>
  <div class="prose-wide">
    <p>If you live in a Colorado home and you haven't tested for radon, the statistical expectation is that you're at or above the EPA action level. That doesn't mean you definitely are — Colorado neighborhoods and even adjacent houses can read very differently — but it means testing isn't optional. The geology and the housing stock combine to make testing essential.</p>
    <p><a href="/radon-testing/">How to test &rarr;</a></p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
    <li id="src-3">Colorado Geological Survey. <a href="{s('colorado_geological')}" rel="noopener" target="_blank">coloradogeologicalsurvey.org</a></li>
  </ol>
</aside>
"""


def why_colorado_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Why is radon so common in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Two reasons working together. First, the geology — Colorado's Front Range sits on uranium-bearing granites (especially Pikes Peak granite) and Pierre Shale outcrops, both of which produce radon through natural uranium decay. Second, the housing stock — most Colorado homes have basements, which concentrate radon. The EPA classifies 53 of Colorado's 64 counties as Zone 1 (highest predicted indoor radon) and the remaining 11 as Zone 2 (moderate). CDPHE estimates roughly half of Colorado homes test above 4.0 pCi/L."}},
            {"@type": "Question", "name": "Does Colorado's high altitude make radon worse?",
             "acceptedAnswer": {"@type": "Answer", "text": "Not directly — radon comes from the soil under your home, not from the air above it. But altitude does affect mitigation. Radon fans lose roughly 4% of their airflow capacity per 1,000 feet of elevation, which means Colorado mitigation systems often need larger fans or additional suction points compared to sea-level designs."}},
            {"@type": "Question", "name": "Why is Colorado Springs / El Paso County on the higher end?",
             "acceptedAnswer": {"@type": "Answer", "text": "El Paso County sits directly on Pikes Peak granite (uranium-bearing, ~1.08 billion years old) with Pierre Shale outcrops in parts of the eastern county. El Paso County Public Health reports that over 40% of homes tested 2005-2023 had elevated radon. Many neighborhoods (Briargate, Stetson Hills, Black Forest, Falcon, Mountain Shadows) consistently see results above 4.0 pCi/L."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 3. /radon-basics/how-it-enters-homes/
# =========================================================================
HOW_ENTERS_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Radon enters a home because of one simple mechanism: pressure. The air inside your home is slightly lower in pressure than the soil gas beneath the foundation, and that pressure difference pulls radon-laden gas up through any small opening it can find. The mechanism is the same in every home; what varies is which openings the gas uses and how much accumulates inside.</p>
    <p>This page covers the physics of radon entry (briefly), the specific pathways radon uses, why basements concentrate it, and how seasonal patterns change the entry rate.</p>
  </div>
</section>

<section>
  <h2>The pressure mechanism</h2>
  <div class="prose-wide">
    <p>Two forces create the pressure difference that drives radon entry:</p>

    <h3>Stack effect (the biggest driver)</h3>
    <p>Warm indoor air is less dense than cold outdoor air. In winter, warm air inside your home rises through stairwells, upper floors, and any chimney or vent stack, creating slight suction at the lowest levels. That suction pulls soil gas — including radon — up through openings in the foundation.</p>
    <p>The stack effect is strongest in winter (largest indoor-outdoor temperature difference) and weakest in summer (temperatures roughly equalize). That's why Colorado winter readings are typically 30–50% higher than summer readings on the same home.<sup><a href="#src-1">[1]</a></sup></p>

    <h3>HVAC and exhaust systems</h3>
    <p>HVAC systems, range hoods, bathroom fans, and clothes dryers all push air out of the home. When air goes out, replacement air has to come in somewhere — typically through small foundation openings. That replacement air carries radon with it from the soil.</p>
    <p>Combustion appliances (gas furnace, water heater, fireplace) intensify this effect by drawing combustion air from inside, again creating depressurization that pulls soil gas in.</p>

    <h3>Diffusion (small effect)</h3>
    <p>Radon also diffuses through concrete and soil naturally, even without a pressure difference. Diffusion is a much smaller effect than pressure-driven flow but contributes to baseline indoor radon in tight, well-sealed homes.</p>
  </div>
</section>

<section>
  <h2>The pathways radon uses</h2>
  <div class="prose-wide">
    <p>Soil gas can enter through any opening between soil and indoor air. The common pathways:</p>
    <ol>
      <li><strong>Hairline cracks in the basement slab.</strong> Even cracks too small to see clearly are large enough for soil gas.</li>
      <li><strong>The floor-wall joint.</strong> The seam where the basement slab meets the foundation wall is almost never airtight; it's the largest single entry pathway in most basements.</li>
      <li><strong>Sump pits.</strong> An open sump pit is a direct soil-to-air connection. Even covered sumps can leak if the cover isn't sealed.</li>
      <li><strong>Plumbing penetrations.</strong> Drain pipes, water lines, and gas lines passing through the slab leave small openings around their edges.</li>
      <li><strong>Crawlspace gaps.</strong> Crawlspaces with dirt floors have a continuous soil-air interface — every square foot is a pathway.</li>
      <li><strong>Foundation walls.</strong> Concrete block walls (less common in Colorado) have hollow cores; poured concrete walls have hairline shrinkage cracks.</li>
      <li><strong>Construction joints.</strong> Where one slab section meets another, the joint isn't fully airtight.</li>
    </ol>
    <p>Radon doesn't pick one path. It uses whatever's available. Sealing a few cracks won't fix the problem — see <a href="/radon-mitigation-systems/why-sealing-isnt-enough/">why sealing alone isn't enough</a>.</p>
  </div>
</section>

<section>
  <h2>Why basements concentrate radon</h2>
  <div class="prose-wide">
    <p>Three reasons basements have higher radon than upper floors:</p>
    <ul>
      <li><strong>Largest soil-contact area.</strong> The basement floor and walls are in direct contact with the most soil. Every square foot of contact is a potential pathway.</li>
      <li><strong>Lowest level = strongest stack-effect suction.</strong> The suction created by warm air rising is strongest at the bottom of the home.</li>
      <li><strong>Less ventilation.</strong> Upper floors have windows that get opened, exterior doors that swing, and active air movement. Basements are often closed off and don't get the same air exchange.</li>
    </ul>
    <p>A typical Colorado home's radon profile: basement reads highest, ground floor reads about half the basement level, second floor reads about a third. That's why the EPA places radon test kits in the lowest livable level — that's where exposure is highest.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>Crawlspaces — a different kind of problem</h2>
  <div class="prose-wide">
    <p>An unsealed crawlspace with a dirt floor is the most direct possible path between soil and indoor air. Every square foot of crawlspace dirt is a potential entry point. The crawlspace then connects to the living space above through floor penetrations, hatches, and any unsealed seams.</p>
    <p>This is why crawlspace mitigation is its own technique (sub-membrane depressurization) rather than the same approach used for basements. <a href="/radon-mitigation-systems/crawlspace-sub-membrane/">More on crawlspace systems &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Seasonal patterns in Colorado</h2>
  <div class="prose-wide">
    <p>Colorado has significant seasonal swings in indoor radon. Three reasons:</p>
    <ul>
      <li><strong>Stack effect strongest in winter.</strong> Larger indoor-outdoor temperature difference = more suction at lower levels.</li>
      <li><strong>Tighter house in winter.</strong> Windows closed, exterior doors closed, weatherstripping engaged. Less air exchange means radon accumulates.</li>
      <li><strong>Soil conditions.</strong> Frozen ground or saturated ground (after rainfall, snowmelt) can change soil permeability and either increase or decrease radon flux into the basement.</li>
    </ul>
    <p>The practical implication: a short-term test in February captures the seasonal peak. A short-term test in July captures the seasonal trough. A long-term test (90+ days) averages both — see <a href="/radon-testing/short-term-vs-long-term/">short-term vs long-term tests</a>.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — same home, three readings</strong>
    <p>A homeowner in Black Forest ran three short-term radon tests on the same home over a year. February: 6.4 pCi/L. May: 4.1 pCi/L. August: 2.8 pCi/L. None of the readings is wrong. They're all real readings for the conditions during their respective 2-day windows. The seasonal swing — driven by stack effect and tighter house conditions in winter — is large enough that a single short-term test can mislead either direction. A 90-day long-term test running through winter and into spring would average somewhere around 4.5 pCi/L, which is much closer to the true annual exposure.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">U.S. EPA. <em>Citizen's Guide to Radon</em>. <a href="{s('epa_citizens_guide')}" rel="noopener" target="_blank">epa.gov/radon/citizens-guide-radon</a></li>
  </ol>
</aside>
"""


def how_enters_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How does radon get into a home?",
             "acceptedAnswer": {"@type": "Answer", "text": "Radon enters through small openings in the foundation because air pressure inside the home is slightly lower than soil gas pressure beneath. The stack effect (warm indoor air rising) and HVAC operation create this pressure difference. Common entry pathways: hairline slab cracks, the floor-wall joint, sump pits, plumbing penetrations, crawlspace dirt floors, and foundation construction joints."}},
            {"@type": "Question", "name": "Why do basements have higher radon than upper floors?",
             "acceptedAnswer": {"@type": "Answer", "text": "Three reasons: basements have the largest soil-contact area of any foundation type, the stack effect creates strongest suction at the lowest level, and basements typically have less ventilation than upper floors. A typical Colorado home reads highest in the basement, about half that on the ground floor, and about a third on the second floor."}},
            {"@type": "Question", "name": "Do Colorado radon levels change with the seasons?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes, significantly. Winter readings can be 30-50% higher than summer readings on the same home because the stack effect is strongest when indoor-outdoor temperature differences are largest, and homes are tighter (less air exchange). A short-term test in winter captures the peak; a long-term 90+ day test averages across seasons."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 4. /radon-basics/health-risks/
# =========================================================================
HEALTH_RISKS_BODY = f"""
<section>
  <div class="prose-wide">
    <p>This is the part of a radon page people scroll through quickly because they don't really want to read it. The honest answer: it's manageable. Radon is a serious long-term health risk, but it's also one of the most preventable indoor environmental hazards because testing is cheap, mitigation is straightforward, and the technology is reliable. This page walks through what the actual risk numbers are and where they come from.</p>
    <p>This is general information and not medical advice. If you have a specific concern about lung disease or radon exposure history, consult a physician.</p>
  </div>
</section>

<section>
  <h2>The headline numbers</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>~21,000 deaths per year</strong> in the United States are attributed to radon-induced lung cancer, per EPA estimates.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>Radon is the #2 cause of lung cancer</strong> overall in the U.S., after smoking.</li>
      <li><strong>Radon is the #1 cause of lung cancer in non-smokers</strong> — roughly 2,900 of the 21,000 annual deaths occur in people who never smoked.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>Radon and smoking have a synergistic effect.</strong> A smoker exposed to elevated radon has dramatically higher lung cancer risk than would be predicted by adding the two risks separately.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Why radon causes cancer</h2>
  <div class="prose-wide">
    <p>The radon gas itself isn't the carcinogen — the <strong>radon progeny</strong> are. Progeny are short-lived radioactive particles produced when radon-222 decays. They're not gases; they're solid particles that attach to dust and water droplets in the air.</p>
    <p>When you breathe air containing radon, the progeny lodge in lung tissue. As they continue to decay, they emit <strong>alpha radiation</strong> — high-energy particles that damage DNA in nearby cells. Over years of exposure, the accumulated DNA damage can cause cells to mutate into cancer.</p>
    <p>The mechanism is exposure-time dependent: low exposure over many years can cause cancer as readily as high exposure over a short time, because the total radiation dose to lung tissue is what matters.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>EPA's risk comparison tables</h2>
  <div class="prose-wide">
    <p>The EPA publishes lifetime lung cancer risk tables for radon exposure, separated for smokers and never-smokers. These numbers come from epidemiological studies of uranium miners and from indoor radon studies, and they assume continuous exposure at the listed level over a lifetime.<sup><a href="#src-1">[1]</a></sup></p>

    <h3>For people who have never smoked</h3>
    <table class="compact">
      <thead>
        <tr><th>Radon level</th><th>Lifetime risk of lung cancer</th></tr>
      </thead>
      <tbody>
        <tr><td>20 pCi/L</td><td>~36 in 1,000</td></tr>
        <tr><td>10 pCi/L</td><td>~18 in 1,000</td></tr>
        <tr><td>8 pCi/L</td><td>~15 in 1,000</td></tr>
        <tr><td>4 pCi/L</td><td>~7 in 1,000</td></tr>
        <tr><td>2 pCi/L</td><td>~4 in 1,000</td></tr>
        <tr><td>1.25 pCi/L</td><td>~2 in 1,000</td></tr>
        <tr><td>0.4 pCi/L (outdoor)</td><td>Baseline</td></tr>
      </tbody>
    </table>

    <h3>For current and former smokers</h3>
    <p>Smokers have a baseline lung cancer risk that's already roughly 10x higher than non-smokers. Add radon, and the combined risk is even higher than either alone:</p>
    <table class="compact">
      <thead>
        <tr><th>Radon level</th><th>Lifetime risk of lung cancer (smoker)</th></tr>
      </thead>
      <tbody>
        <tr><td>20 pCi/L</td><td>~260 in 1,000</td></tr>
        <tr><td>10 pCi/L</td><td>~150 in 1,000</td></tr>
        <tr><td>8 pCi/L</td><td>~120 in 1,000</td></tr>
        <tr><td>4 pCi/L</td><td>~62 in 1,000</td></tr>
        <tr><td>2 pCi/L</td><td>~32 in 1,000</td></tr>
        <tr><td>1.25 pCi/L</td><td>~20 in 1,000</td></tr>
        <tr><td>0.4 pCi/L (outdoor)</td><td>Baseline smoker risk</td></tr>
      </tbody>
    </table>
    <p style="font-size:.85rem;color:var(--text-muted);">Tables drawn from <a href="{s('epa_health_risk')}" rel="noopener" target="_blank">EPA Health Risk of Radon</a>, 2003 BEIR VI risk model.</p>
  </div>
</section>

<section>
  <h2>The Surgeon General advisory</h2>
  <div class="prose-wide">
    <p>The U.S. Surgeon General issued a national health advisory on radon in <strong>January 2005</strong>, calling indoor radon a serious public health threat and urging Americans to test their homes and mitigate at or above 4.0 pCi/L. The advisory remains the operative federal health advisory on radon and is referenced on EPA's current radon health risk page.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>Children and radon</h2>
  <div class="prose-wide">
    <p>The Agency for Toxic Substances and Disease Registry (ATSDR) notes that children may be more vulnerable to radon-induced lung damage than adults for two reasons:</p>
    <ul>
      <li><strong>Higher respiration rate.</strong> Children breathe more air per body weight than adults, which means more radon progeny deposition per kilogram of body mass.</li>
      <li><strong>Developing lung tissue.</strong> Still-developing lungs may be more susceptible to DNA damage from alpha radiation.</li>
    </ul>
    <p>ATSDR is careful to note that the epidemiological evidence specifically in children is limited (most radon studies are of adult occupational exposure), and the heightened pediatric concern is largely mechanistic. EPA's risk calculations for residential radon exposure include children's typical exposure patterns.<sup><a href="#src-3">[3]</a></sup></p>
    <p>The practical implication: for homes where children spend significant time in the lowest level (a finished basement bedroom, daycare in a basement, etc.), the case for mitigation gets stronger.</p>
  </div>
</section>

<section>
  <h2>WHO vs EPA action levels</h2>
  <div class="prose-wide">
    <p>The U.S. EPA's action level of 4.0 pCi/L is one of several action levels published by health agencies internationally. The World Health Organization recommends action at 100 Bq/m³, which is roughly 2.7 pCi/L — significantly lower than EPA.<sup><a href="#src-4">[4]</a></sup> The WHO position is that lower action levels are technically achievable in modern construction and that radon risk is continuous (there's no safe threshold).</p>
    <p>What this means for Colorado homeowners:</p>
    <ul>
      <li>A reading below 4.0 pCi/L but above 2.7 pCi/L is below the U.S. action level but above the WHO's recommended level.</li>
      <li>Some Colorado homeowners (particularly with high lifetime exposure already, never-smokers in the higher-risk demographic, or with children using the lowest level daily) mitigate at the WHO threshold rather than waiting for the EPA threshold.</li>
      <li>There's no medical rule that says you must mitigate at exactly 4.0 pCi/L. The decision is risk-based, not legal.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Common myths about radon health risk</h2>
  <div class="prose-wide">

    <h3>"My granite countertops are the problem"</h3>
    <p>Granite countertops can contribute small amounts of radon, but EPA explicitly states the contribution is <strong>far smaller</strong> than soil-source radon in most homes. If your home tests high, the problem is almost always the soil under the foundation, not the kitchen counters.<sup><a href="#src-1">[1]</a></sup></p>

    <h3>"Radon is only dangerous at very high levels"</h3>
    <p>Risk is continuous. There's no threshold below which radon is "safe." Lower levels mean lower risk, but the risk doesn't disappear. The 4.0 pCi/L action level isn't a safety guarantee; it's a regulatory threshold balancing health risk against feasibility of widespread mitigation.</p>

    <h3>"If my neighbor's test is low, mine will be too"</h3>
    <p>Radon levels can vary significantly between adjacent homes — different foundation types, different soil conditions, different construction quality. The only way to know your home's level is to test it.</p>

    <h3>"Radon is more dangerous in winter"</h3>
    <p>Radon levels are higher in winter (stack effect), but the danger isn't season-specific. Cumulative exposure over years is what matters. If your home runs high in winter and low in summer, the annual average is still elevated.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Health Risk of Radon</em>. <a href="{s('epa_health_risk')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
    <li id="src-2">U.S. Surgeon General. <em>National Health Advisory on Radon (January 13, 2005)</em>. Referenced in EPA materials and HHS archives.</li>
    <li id="src-3">Agency for Toxic Substances and Disease Registry (ATSDR). <em>Toxicological Profile for Radon</em>. <a href="{s('atsdr_radon')}" rel="noopener" target="_blank">atsdr.cdc.gov</a></li>
    <li id="src-4">World Health Organization. <em>WHO Handbook on Indoor Radon (2009) / Radon and Health Fact Sheet</em>. <a href="{s('who_radon')}" rel="noopener" target="_blank">who.int</a></li>
  </ol>
</aside>

<p style="font-size:.85rem;color:var(--text-muted);">This page is general information, not medical advice. If you have specific concerns about lung disease or radon exposure history, consult a physician.</p>
"""


def health_risks_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How dangerous is radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "EPA estimates radon causes approximately 21,000 lung cancer deaths per year in the U.S., making it the #2 cause of lung cancer overall (after smoking) and the #1 cause in non-smokers. About 2,900 annual deaths occur in people who never smoked. Risk is continuous and exposure-time dependent — there's no safe threshold, but lower levels mean lower risk."}},
            {"@type": "Question", "name": "What's my risk at 4.0 pCi/L?",
             "acceptedAnswer": {"@type": "Answer", "text": "Per EPA risk tables (2003 BEIR VI model), continuous lifetime exposure at 4.0 pCi/L gives roughly 7-in-1,000 lung cancer risk for never-smokers and roughly 62-in-1,000 for current/former smokers. Smokers exposed to radon have dramatically multiplied risk due to synergy between smoking and radon — they're not additive risks."}},
            {"@type": "Question", "name": "Are children more vulnerable to radon?",
             "acceptedAnswer": {"@type": "Answer", "text": "ATSDR notes children may be more vulnerable due to higher respiration rate per body weight and still-developing lung tissue. The epidemiological evidence specifically in children is limited (most studies are of adult occupational exposure). For homes where children spend significant time in the lowest level, the case for mitigation strengthens."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 5. /radon-basics/levels-explained/
# =========================================================================
LEVELS_EXPLAINED_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Your radon test result came back as a number. What does that number actually mean? This page walks through every level in the practical range — outdoor air, the U.S. indoor average, the borderline zone, the EPA action level, and the high readings — and explains what each one tells you about your home.</p>
  </div>
</section>

<section>
  <h2>The reference points</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th>Level (pCi/L)</th><th>Reference point</th></tr>
      </thead>
      <tbody>
        <tr><td>~0.4</td><td>Outdoor air average (U.S.)</td></tr>
        <tr><td>~1.3</td><td>U.S. indoor air average (single-family)</td></tr>
        <tr><td>2.0</td><td>EPA "consider action" lower bound</td></tr>
        <tr><td>2.7</td><td>WHO recommended action level (100 Bq/m³)</td></tr>
        <tr><td>4.0</td><td>EPA action level (mitigate at or above)</td></tr>
        <tr><td>~6.4</td><td>Colorado indoor average (CDPHE, recent figure)</td></tr>
        <tr><td>10.0</td><td>EPA flag — limit exposure until mitigation</td></tr>
        <tr><td>20.0+</td><td>Very high, urgent mitigation</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <h2>Below 2.0 pCi/L — below the consider-action range</h2>
  <div class="prose-wide">
    <p>Your home is in the lower half of the U.S. distribution. The EPA does not recommend action at this level. WHO would still flag it (the WHO reference is 2.7 pCi/L), but neither agency recommends mitigation below 2.0.</p>
    <p>What to do:</p>
    <ul>
      <li>Retest every 2 years. Conditions change over time.</li>
      <li>Retest after major remodels that affect the foundation or HVAC.</li>
      <li>Test before listing or buying.</li>
    </ul>
  </div>
</section>

<section>
  <h2>2.0–3.9 pCi/L — EPA says "consider mitigation"</h2>
  <div class="prose-wide">
    <p>The EPA recommends considering mitigation in this range. The WHO (2.7 pCi/L action level) would actively recommend mitigation in the upper half of this range.</p>
    <p>For Colorado homeowners specifically, the borderline zone is worth thinking carefully about:</p>
    <ul>
      <li><strong>Winter readings in this range</strong> are common. The seasonal average may be lower.</li>
      <li><strong>Summer readings in this range</strong> usually mean the seasonal average is higher.</li>
      <li><strong>Run a long-term test</strong> to get the annual picture before deciding.</li>
      <li><strong>Risk equivalents:</strong> Per EPA tables, 2 pCi/L gives roughly 4-in-1,000 lifetime lung cancer risk for never-smokers and 32-in-1,000 for smokers.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>Lifestyle matters.</strong> If the lowest level is used daily (home office, basement bedroom, kids' playroom), the case for mitigation is stronger.</li>
    </ul>
    <p><a href="/radon-basics/health-risks/">Full health risk context &rarr;</a></p>
  </div>
</section>

<section>
  <h2>4.0 pCi/L — the EPA action level</h2>
  <div class="prose-wide">
    <p>This is the threshold where the EPA recommends mitigation and where CDPHE concurs. At 4.0 pCi/L:</p>
    <ul>
      <li><strong>Risk:</strong> ~7-in-1,000 lifetime lung cancer risk for never-smokers; ~62-in-1,000 for smokers.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>Comparison:</strong> At 4 pCi/L, a smoker is about 5x more likely to die from radon than from a home fire over their lifetime, per EPA's risk comparison tables.</li>
      <li><strong>Action:</strong> Confirm with a second test or a professional continuous monitor. Then get at least two written quotes from DORA-licensed contractors.</li>
    </ul>
    <p>4.0 pCi/L isn't a cliff. Risk at 4.1 isn't meaningfully different from risk at 3.9. The line is regulatory, not medical. But it is the line the U.S. uses, and it's what most real-estate transactions key off of.</p>
  </div>
</section>

<section>
  <h2>4–10 pCi/L — clear action range</h2>
  <div class="prose-wide">
    <p>This is the most common range for Colorado homes that test high. Mitigation in this range is straightforward — a standard sub-slab depressurization system typically brings these homes below 2.0 pCi/L.</p>
    <p>Risk at this range:</p>
    <ul>
      <li>5 pCi/L: ~9-in-1,000 risk (never-smoker), ~80-in-1,000 (smoker)</li>
      <li>7 pCi/L: ~12-in-1,000 risk (never-smoker), ~110-in-1,000 (smoker)</li>
      <li>10 pCi/L: ~18-in-1,000 risk (never-smoker), ~150-in-1,000 (smoker)</li>
    </ul>
    <p>The EPA also notes that at 10 pCi/L (smoker), risk is roughly 200x higher than dying from a home fire.<sup><a href="#src-1">[1]</a></sup> The framing is meant to underscore that radon risk is real and underappreciated relative to risks people take seriously.</p>
  </div>
</section>

<section>
  <h2>10+ pCi/L — high, urgent</h2>
  <div class="prose-wide">
    <p>EPA recommends not waiting in this range — minimize time in the lowest level until a mitigation system is installed.<sup><a href="#src-1">[1]</a></sup> At this level:</p>
    <ul>
      <li>Risk is well above the action-level threshold.</li>
      <li>Mitigation is the same technique as for 4–10 range, but may need a larger fan or more suction points to bring levels down.</li>
      <li>Use the lowest level less while the system is being installed.</li>
      <li>Most Colorado contractors can do an emergency install within 7–10 days.</li>
    </ul>
  </div>
</section>

<section>
  <h2>20+ pCi/L — very high</h2>
  <div class="prose-wide">
    <p>Less common but does occur, particularly in Colorado mountain communities or homes on exposed Pierre Shale outcrops. At 20+ pCi/L:</p>
    <ul>
      <li>Risk per EPA tables is ~36-in-1,000 for never-smokers and ~260-in-1,000 for smokers.<sup><a href="#src-1">[1]</a></sup></li>
      <li>Mitigation should happen quickly. Don't sleep in the basement until it's done.</li>
      <li>The contractor may need diagnostic testing to design an appropriate system — multi-zone homes with very high readings sometimes need 3+ suction points.</li>
    </ul>
  </div>
</section>

<section>
  <h2>What if the levels vary widely between tests?</h2>
  <div class="prose-wide">
    <p>Variation between tests is normal. A 2-day short-term test captures one snapshot of conditions; a 90-day long-term test averages across seasons. Don't be alarmed if a winter reading is 6 pCi/L and a summer reading on the same home is 3 pCi/L — that's typical Colorado seasonal variation.</p>
    <p>What to do:</p>
    <ul>
      <li>If both readings are above 4.0, mitigate.</li>
      <li>If one is above and one is below, run a long-term test (90+ days) for the annual average.</li>
      <li>If the readings are dramatically different (5x or more), check the placement — placement errors can produce wide variation. <a href="/radon-testing/where-to-place-a-test/">Test placement guide &rarr;</a></li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Health Risk of Radon</em> (risk tables drawn from BEIR VI 2003 model). <a href="{s('epa_health_risk')}" rel="noopener" target="_blank">epa.gov/radon/health-risk-radon</a></li>
  </ol>
</aside>
"""


def levels_explained_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What does my radon test result mean?",
             "acceptedAnswer": {"@type": "Answer", "text": "Below 2.0 pCi/L: below EPA's consider-action range; retest every 2 years. 2.0-3.9: EPA suggests considering mitigation; WHO (2.7 pCi/L reference) recommends it. 4.0 or above: EPA action level, mitigate. 10+ pCi/L: high, urgent — limit time in lowest level until mitigated. 20+ pCi/L: very high, immediate action."}},
            {"@type": "Question", "name": "Is the EPA's 4.0 pCi/L action level safe?",
             "acceptedAnswer": {"@type": "Answer", "text": "Not exactly — risk is continuous. There's no threshold below which radon is risk-free. 4.0 pCi/L is the U.S. regulatory threshold balancing health risk against widespread mitigation feasibility. The WHO recommends action at 2.7 pCi/L. Both agencies acknowledge that lower is better; they differ on where to draw the action line."}},
            {"@type": "Question", "name": "Why are my Colorado radon readings so different between tests?",
             "acceptedAnswer": {"@type": "Answer", "text": "Seasonal variation. Colorado winter readings can be 30-50% higher than summer readings on the same home because the stack effect is stronger and homes are tighter. A 2-day test captures one snapshot; a 90-day long-term test averages across seasons. Dramatically different readings (5x or more) may also indicate placement errors."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 6. /radon-basics/by-foundation-type/
# =========================================================================
BY_FOUNDATION_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Not all Colorado homes have the same radon profile. The foundation under your home — basement, crawlspace, slab-on-grade, walk-out, tri-level — determines where soil gas enters, how it accumulates, and what mitigation looks like if needed. This page walks through each foundation type, how it interacts with radon, and what to expect.</p>
  </div>
</section>

<section>
  <h2>Full basement (most common in Colorado)</h2>
  <div class="prose-wide">
    <p>A full basement is the most common foundation type in Colorado Front Range homes. It also has the largest soil-contact area of any foundation type, which means it captures the most soil gas.</p>
    <p>Characteristics:</p>
    <ul>
      <li><strong>Largest pathway count.</strong> Basement slab, floor-wall joint, sump pit (if present), plumbing penetrations, and any expansion joints are all potential entry points.</li>
      <li><strong>Strongest stack effect.</strong> Being at the lowest level means the suction created by warm rising indoor air is strongest here.</li>
      <li><strong>Typical readings.</strong> Basements consistently read higher than upper floors. The ratio is roughly 2:1 (basement vs ground floor) and 3:1 (basement vs second floor) in a typical home.</li>
      <li><strong>Finished vs unfinished.</strong> A finished basement isn't safer — the radon still enters; you just spend more time there.</li>
      <li><strong>Mitigation.</strong> Standard sub-slab depressurization (SSD). $900–$1,900 in Colorado Springs for a basic install. <a href="/radon-mitigation-cost/">Full cost ranges &rarr;</a></li>
    </ul>
  </div>
</section>

<section>
  <h2>Crawlspace</h2>
  <div class="prose-wide">
    <p>Crawlspaces are common in older Colorado neighborhoods (1950s–1970s ranches), in some mountain communities, and as partial foundations under additions. They behave very differently from basements when it comes to radon.</p>
    <p>Characteristics:</p>
    <ul>
      <li><strong>Direct soil-air contact.</strong> An unsealed crawlspace has a continuous interface between soil and indoor air across the entire floor area.</li>
      <li><strong>Higher entry rate per square foot.</strong> Concrete slabs are mildly resistant to soil gas; dirt floors are not.</li>
      <li><strong>Less air exchange.</strong> Crawlspaces are typically closed-off spaces with limited ventilation. Radon accumulates and then migrates upward into the living space.</li>
      <li><strong>Mitigation.</strong> Sub-membrane depressurization (SMD), not sub-slab. A heavy vapor barrier is laid across the entire floor, sealed at the perimeter, and a fan pulls air from beneath it. $1,800–$4,000 in Colorado Springs. <a href="/radon-mitigation-systems/crawlspace-sub-membrane/">Full SMD walkthrough &rarr;</a></li>
    </ul>
  </div>
</section>

<section>
  <h2>Slab-on-grade</h2>
  <div class="prose-wide">
    <p>Slab-on-grade homes (no basement, no crawlspace) are less common in Colorado but exist — particularly in 1950s–1960s ranches and modern garden-level builds.</p>
    <p>Characteristics:</p>
    <ul>
      <li><strong>Smallest soil contact</strong> compared to basements.</li>
      <li><strong>Entry pathways:</strong> hairline slab cracks, plumbing penetrations, the slab-perimeter joint.</li>
      <li><strong>Typical readings.</strong> Generally lower than basement homes — but not zero. Colorado slab homes still need testing.</li>
      <li><strong>Mitigation.</strong> Sub-slab depressurization, similar to basement systems but with the suction point in the ground-floor slab. Cost ranges similar to basic basement: $900–$1,900.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Walk-out basement</h2>
  <div class="prose-wide">
    <p>Walk-out basements have a daylight door or exterior access on one side. They're common in Colorado homes built on sloped lots.</p>
    <p>Characteristics:</p>
    <ul>
      <li><strong>Three walls in soil contact</strong>, one wall above grade with a door or large windows.</li>
      <li><strong>Slightly less radon</strong> than a fully buried basement — the above-grade wall reduces total soil contact and gives some natural ventilation.</li>
      <li><strong>Still considered the lowest livable level</strong> for testing purposes. Test the basement, not the ground floor above.</li>
      <li><strong>Mitigation.</strong> Standard sub-slab depressurization. The daylight door doesn't change the system design materially.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Tri-level and split-level homes</h2>
  <div class="prose-wide">
    <p>Tri-level and split-level homes are common in 1970s–1990s Colorado Springs neighborhoods (Stetson Hills, Briargate, Mountain Shadows). They have multiple foundation zones — typically a basement under part of the home and a crawlspace or partial slab under another part.</p>
    <p>Characteristics:</p>
    <ul>
      <li><strong>Multi-zone foundation.</strong> Soil gas enters through multiple foundation pressure points.</li>
      <li><strong>Diagnostic testing matters.</strong> A single suction point may not depressurize all foundation zones. Quality contractors run a Pressure Field Extension (PFE) test before quoting.</li>
      <li><strong>Mitigation.</strong> Multi-zone systems with 2+ suction points and possibly 2 fans. Cost: $2,200–$4,800 in Colorado Springs. <a href="/radon-mitigation-cost/">Multi-zone cost details &rarr;</a></li>
      <li><strong>Watch for partial crawlspace under additions.</strong> Some tri-level homes have a small crawlspace under the kitchen or laundry that's easy to overlook. A contractor should walk the entire foundation before quoting.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Finished basement (or finished lower level)</h2>
  <div class="prose-wide">
    <p>A finished basement isn't a separate foundation type — it's a usage category. From a radon perspective, the finishing matters because:</p>
    <ul>
      <li><strong>You spend more time in finished space.</strong> A finished basement that's used as a TV room, bedroom, or home office means daily exposure to whatever radon level the basement has.</li>
      <li><strong>The slab and walls are the same as an unfinished basement.</strong> Radon enters the same way; you just don't see the slab cracks anymore.</li>
      <li><strong>Mitigation needs interior routing.</strong> The pipe has to navigate finished walls, drop ceilings, and utility space. Cost adds $300–$900 vs an unfinished basement install.</li>
      <li><strong>If a finished basement is being added later</strong>, test before and after — the new living patterns change your exposure calculation.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Mixed foundations (basement + crawlspace)</h2>
  <div class="prose-wide">
    <p>Some Colorado homes — particularly older homes with additions or homes built on irregular lots — have a basement under part of the footprint and a crawlspace under another part. These behave like multi-zone homes:</p>
    <ul>
      <li>The basement portion needs sub-slab depressurization.</li>
      <li>The crawlspace portion needs sub-membrane depressurization (with a vapor barrier).</li>
      <li>The two systems can sometimes share a single fan and pipe, or may need to be installed separately.</li>
      <li>A contractor should look at both zones before quoting. Treating a mixed-foundation home like a basement-only home will under-mitigate the crawlspace half.</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Citizen's Guide to Radon</em>. <a href="{s('epa_citizens_guide')}" rel="noopener" target="_blank">epa.gov/radon/citizens-guide-radon</a></li>
    <li id="src-2">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
  </ol>
</aside>
"""


def by_foundation_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Do all foundation types have the same radon risk?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Full basements have the largest soil-contact area and typically test highest. Crawlspaces (unsealed dirt floors) have continuous soil-air interface and can be as bad or worse. Slab-on-grade homes generally test lower than basements but aren't risk-free. Walk-out basements are slightly lower than fully buried basements. Tri-level and split-level homes are multi-zone — soil gas enters through multiple foundation pressure points."}},
            {"@type": "Question", "name": "Does my walk-out basement need radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "If a test in the walk-out basement reads at or above 4.0 pCi/L, yes. Walk-out basements have three walls in soil contact and one above grade — slightly less radon entry than a fully buried basement, but still considered the lowest livable level for testing purposes. The daylight door doesn't change mitigation system design materially."}},
            {"@type": "Question", "name": "How is mitigation different for tri-level homes?",
             "acceptedAnswer": {"@type": "Answer", "text": "Tri-level and split-level homes have multiple foundation zones — typically basement plus crawlspace or partial slab. Mitigation requires multiple suction points and sometimes multiple fans because a single suction point won't depressurize all zones. Quality contractors run a Pressure Field Extension (PFE) test before quoting. Cost: $2,200-$4,800 in Colorado Springs."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
