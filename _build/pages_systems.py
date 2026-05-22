"""Content for the Mitigation Systems pillar pages (Phase 3 build).

Seven pages:
1. /radon-mitigation-systems/                            — hub (How Radon Mitigation Works)
2. /radon-mitigation-systems/sub-slab-depressurization/  — SSD deep dive
3. /radon-mitigation-systems/crawlspace-sub-membrane/    — SMD for crawlspaces
4. /radon-mitigation-systems/passive-vs-active/          — Passive vs active systems
5. /radon-mitigation-systems/fans-pipes-suction-points/  — Equipment deep dive (altitude correction)
6. /radon-mitigation-systems/why-sealing-isnt-enough/    — The sealing myth
7. /radon-mitigation-systems/what-happens-after-mitigation/ — Post-mit test, retest cadence, manometer reading
"""
import json
from pages_main import s, SOURCES

# Ensure the cost pillar sources are also available (idempotent)
SOURCES.setdefault("epa_citizens_guide", "https://www.epa.gov/radon/citizens-guide-radon")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")
SOURCES.setdefault("aarst_standards", "https://standards.aarst.org/")
SOURCES.setdefault("aarst_sgm_sf", "https://aarst.org/product/sgm-sf-2023-pdf/")
SOURCES.setdefault("nrpp_search", "https://nrpp.info/pro-search/")
SOURCES.setdefault("nrsb_search", "https://nrsb.org/for-professional/")
SOURCES.setdefault("radonaway_specs", "https://www.radonaway.com/")
SOURCES.setdefault("irc_appendix_be", "https://aarst.org/building-codes-standards/")


# =========================================================================
# 1. /radon-mitigation-systems/   — HUB: HOW RADON MITIGATION WORKS
# =========================================================================
SYSTEMS_HUB_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Radon mitigation looks like a fan and a pipe. It isn't. A working mitigation system is a small piece of building science that depressurizes the soil beneath your home, captures radon-laden soil gas before it enters your living space, and exhausts it safely above the roofline — and then proves it worked with a written post-mitigation test.</p>
    <p>This is the plain-language tour of how the system works, what the parts do, what's different about systems built for Colorado, and what to expect a quality install to look like.</p>
  </div>
</section>

<section>
  <h2>The basic principle: depressurization</h2>
  <div class="prose-wide">
    <p>Radon enters a home because the air pressure inside is slightly lower than the air pressure in the soil beneath the foundation. That pressure difference — called the <em>stack effect</em> in winter, when warm indoor air rises and creates suction at lower levels — pulls soil gas, and the radon dissolved in it, up through any small opening it can find. Hairline slab cracks, the floor-wall joint, sump pits, plumbing penetrations.</p>
    <p>A mitigation system reverses that pressure difference. A fan applies suction to the soil under the slab (or under a sealed membrane in a crawlspace), so the pressure beneath the foundation is lower than the pressure inside the home. Soil gas now flows <em>into</em> the system instead of into your living space, and the system safely exhausts it above the roof.</p>
    <p>This is why sealing cracks alone almost never works — and sometimes makes things worse. <a href="/radon-mitigation-systems/why-sealing-isnt-enough/">More on that here</a>.</p>
  </div>
</section>

<section>
  <h2>The two main methods used in Colorado homes</h2>
  <div class="prose-wide">

    <h3>Sub-slab depressurization (SSD)</h3>
    <p>The most common method for basements and slab-on-grade homes. The contractor drills through the basement slab into the soil or gravel beneath, creates a small extraction pit, and connects it to a sealed PVC pipe that exits the home and exhausts above the roofline. A fan in the line pulls air from beneath the slab.</p>
    <p><a href="/radon-mitigation-systems/sub-slab-depressurization/">Full SSD walkthrough &rarr;</a></p>

    <h3>Sub-membrane depressurization (SMD)</h3>
    <p>The crawlspace equivalent. A heavy vapor barrier is laid across the entire crawlspace floor, sealed at the perimeter and at penetrations. The suction is applied beneath the membrane, so soil gas is pulled out before it can pass through.</p>
    <p><a href="/radon-mitigation-systems/crawlspace-sub-membrane/">Full SMD walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Active vs. passive systems</h2>
  <div class="prose-wide">
    <p>An <strong>active</strong> system has a fan that runs 24/7 and reduces indoor radon by up to <strong>99%</strong>. A <strong>passive</strong> system has the pipe in place but no fan — it relies on natural updraft and typically reduces radon by up to <strong>50%</strong>.<sup><a href="#src-1">[1]</a></sup></p>
    <p>Most homes that need mitigation in Colorado need active systems. Passive systems are common as a rough-in in newer Colorado homes (post-2009 builds often have one) but are converted to active when the post-construction test shows radon at or above 4.0 pCi/L.</p>
    <p><a href="/radon-mitigation-systems/passive-vs-active/">Passive vs active full comparison &rarr;</a></p>
  </div>
</section>

<section>
  <h2>The parts of a working system</h2>
  <div class="prose-wide">
    <p>Whether your install is sub-slab or sub-membrane, the working system has the same parts:</p>
    <ul class="checklist">
      <li><strong>Suction point</strong> through the slab (SSD) or beneath the membrane (SMD), connected to the rest of the system.</li>
      <li><strong>Sealing</strong> of slab cracks, the floor-wall joint, sump covers, plumbing penetrations (and the perimeter membrane in crawlspaces). Sealing alone doesn't work — but it is essential alongside depressurization.</li>
      <li><strong>Pipe</strong> — typically 3-inch or 4-inch Schedule 40 PVC, routed through the home or up an exterior wall.</li>
      <li><strong>Fan</strong> — the inline fan that pulls air from the suction point. Located in unconditioned space (attic or exterior wall) so any leak in the positive-pressure side doesn't release radon back into the home.</li>
      <li><strong>Exhaust point</strong> above the roofline, away from windows, chimneys, and adjacent buildings. AARST standards specify minimum distances.<sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>Manometer</strong> — a small U-tube or digital pressure gauge at the suction point. It's how you confirm the fan is running and the system is working.</li>
      <li><strong>Post-mitigation test</strong> — within 30 days of install, a 2 to 7-day closed-house test that confirms indoor radon is below 4.0 pCi/L.<sup><a href="#src-3">[3]</a></sup></li>
    </ul>
    <p><a href="/radon-mitigation-systems/fans-pipes-suction-points/">Equipment deep dive &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What's different about Colorado systems</h2>
  <div class="prose-wide">

    <h3>Altitude affects fan sizing</h3>
    <p>Radon fans lose roughly <strong>4% of their airflow capacity for every 1,000 feet of elevation</strong>.<sup><a href="#src-4">[4]</a></sup> Colorado Springs sits at about 6,000 feet. Denver at 5,280. A fan that's perfectly sized for a sea-level install is meaningfully underpowered in Colorado, which is why the right fan model matters more here than almost anywhere else. <a href="/radon-mitigation-systems/fans-pipes-suction-points/">Full altitude correction explainer &rarr;</a></p>

    <h3>Front Range geology pushes baselines higher</h3>
    <p>Colorado's uranium-bearing granite and shale are the source rocks for indoor radon. Pikes Peak granite contains uranium-bearing accessory minerals; the Front Range as a whole averages much higher indoor radon than the U.S. national average. CDPHE estimates roughly half of Colorado homes test above the EPA action level.<sup><a href="#src-5">[5]</a></sup></p>

    <h3>State licensing is real</h3>
    <p>Colorado is one of the few states with state-level radon contractor licensing through the <a href="{s('dora_radon')}" rel="noopener" target="_blank">DORA Office of Radon Professionals</a>. A correctly installed Colorado system is installed by someone who is both DORA-licensed and either NRPP or NRSB certified.<sup><a href="#src-6">[6]</a></sup></p>
  </div>
</section>

<section>
  <h2>What "working" looks like, day to day</h2>
  <div class="prose-wide">
    <p>A working system runs quietly in the background. A few signals tell you everything's fine:</p>
    <ul>
      <li>The <strong>manometer</strong> shows a steady offset between the two columns of fluid (or a steady digital reading), indicating the fan is pulling vacuum.</li>
      <li>The fan motor is <strong>quiet</strong> from inside the home and barely audible outside near the exhaust.</li>
      <li>Your <strong>retest</strong> every two years confirms radon levels remain below 4.0 pCi/L.<sup><a href="#src-3">[3]</a></sup></li>
      <li>Your <strong>electricity bill</strong> increases by less than $10/month for the fan operation.<sup><a href="#src-3">[3]</a></sup></li>
    </ul>
    <p>If any of those change — manometer columns equalize, fan starts to hum or rattle, retest shows levels rising — call the original installer. The fan itself is the most likely component to fail (typical life 5+ years), and replacement runs $150–$400 in parts plus labor.</p>
    <p><a href="/radon-mitigation-systems/what-happens-after-mitigation/">Post-mitigation expectations &rarr;</a></p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — what your first month with a system looks like</strong>
    <p>You signed off on the install on a Tuesday. The contractor arrived Wednesday, drilled the suction point, ran the pipe up through the attic and out the roof, mounted the fan in the attic, sealed the slab cracks and the sump pit, and installed the manometer at the suction point. The whole install took 5 hours. The contractor activated the fan before leaving and walked you through the manometer reading.</p>
    <p>Three days later you placed a short-term test in the basement (closed-house conditions, 12 hours before and during). Five days after install, you mailed the test to the lab. The result came back at 1.7 pCi/L — well below the EPA action level. The contractor sent you the system certification paperwork with the post-mit test result on letterhead. You stored it in the same folder as your home inspection paperwork. End-to-end: 10 days.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">ASTM E1465 / ANSI-AARST CCAH and SGM-SF standards for radon control. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
    <li id="src-2">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards for Single-Family Buildings. <a href="{s('aarst_sgm_sf')}" rel="noopener" target="_blank">aarst.org</a></li>
    <li id="src-3">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-4">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
    <li id="src-5">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-6">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/Radon</a></li>
  </ol>
</aside>
"""


def systems_hub_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How does radon mitigation actually work?",
             "acceptedAnswer": {"@type": "Answer", "text": "A radon mitigation system depressurizes the soil beneath your foundation using a fan and pipe. The fan creates suction beneath the slab (or beneath a sealed membrane in a crawlspace) so the pressure under the home is lower than inside. Soil gas, including the radon dissolved in it, now flows into the system instead of into your living space, and is exhausted safely above the roofline."}},
            {"@type": "Question", "name": "What's the difference between active and passive radon systems?",
             "acceptedAnswer": {"@type": "Answer", "text": "An active system has a fan that runs 24/7 and reduces indoor radon by up to 99%. A passive system has the pipe in place but no fan — it relies on natural updraft and typically reduces radon by up to 50%. Newer Colorado homes often have passive rough-ins from new construction, which get converted to active when post-construction testing shows radon at or above 4.0 pCi/L."}},
            {"@type": "Question", "name": "Why is sealing cracks alone not enough to fix a radon problem?",
             "acceptedAnswer": {"@type": "Answer", "text": "Radon enters because the air pressure inside a home is slightly lower than the pressure in the soil beneath. Sealing reduces some pathways but doesn't change the pressure difference, so radon still finds its way in through unsealed gaps. CDPHE specifically warns that sealing alone can sometimes make radon levels worse by concentrating the gas at remaining openings."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 2. /radon-mitigation-systems/sub-slab-depressurization/
# =========================================================================
SSD_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Sub-slab depressurization, often shortened to SSD, is the workhorse of Colorado radon mitigation. If you have a basement or a slab-on-grade home, SSD is almost certainly the method a quality contractor will propose. This page walks through how it works, the design decisions that affect whether it works <em>well</em>, and what to look for in a written quote.</p>
  </div>
</section>

<section>
  <h2>How SSD works</h2>
  <div class="prose-wide">
    <p>The contractor drills a hole through the basement slab, typically 4 inches in diameter, and excavates a small pit beneath. The pit gives the system a place to draw soil gas from. A sealed PVC pipe is connected to the pit and routed up through the home (or up an exterior wall) to a fan, and from the fan to an exhaust point above the roofline.</p>
    <p>The fan creates suction at the pit. Once it's running, the pressure beneath the slab drops below the pressure inside the home. Soil gas — and the radon dissolved in it — now flows into the pit and out through the system rather than into your basement.</p>
    <p>The mechanics are simple. The decisions that determine whether it works well are not.</p>
  </div>
</section>

<section>
  <h2>The diagnostic step that should happen first</h2>
  <div class="prose-wide">
    <p>Before installing SSD on anything other than a simple single-zone basement, a quality contractor will run a <strong>pressure field extension (PFE) test</strong>. They drill a small test hole, apply suction with a portable vacuum, and measure how far the negative pressure spreads through the sub-slab gravel or soil.</p>
    <p>If the field extends well — typically 20+ feet from the test point — a single suction point can pull the entire foundation footprint down. If the field is short, the soil under one part of the slab won't communicate with the soil under another, and the system needs <strong>two or more suction points</strong> to cover the full footprint.</p>
    <p>Contractors who skip PFE on a tight-soil or multi-zone home and propose a single suction point are the contractors most likely to install a system that doesn't bring radon below the action level. Ask whether a PFE will be run before the install starts.</p>
  </div>
</section>

<section>
  <h2>Single vs. multiple suction points</h2>
  <div class="prose-wide">
    <p>One suction point handles most Colorado basements with porous gravel under the slab. You need more than one when:</p>
    <ul>
      <li>The PFE test shows poor sub-slab communication (tight clay, dense soil).</li>
      <li>The home has multiple foundation zones — a tri-level, a split-level, an addition with its own slab.</li>
      <li>The slab is unusually large (typically 2,500+ sq ft).</li>
      <li>There's a structural footing or interior bearing wall that the soil gas can't flow under or around.</li>
    </ul>
    <p>Each additional suction point adds $300–$700 in materials and labor and sometimes a second fan. That's not padding — it's the work being done correctly. <a href="/radon-mitigation-cost/quote-variation/">More on quote variation &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Fan placement and exhaust requirements</h2>
  <div class="prose-wide">
    <p>The fan goes in <strong>unconditioned space</strong> — typically the attic or an enclosure on an exterior wall. The reason: the pipe between the fan and the exhaust is under positive pressure (radon-laden air being pushed out). If that pipe leaks in conditioned space, it would release radon back into the home. Putting the fan in unconditioned space means any leak in the positive-pressure pipe vents to the outdoors.<sup><a href="#src-1">[1]</a></sup></p>
    <p>The exhaust point has specific AARST and EPA requirements:<sup><a href="#src-2">[2]</a></sup></p>
    <ul>
      <li>At least <strong>10 feet above grade</strong>.</li>
      <li>At least <strong>12 inches above the roof edge</strong>.</li>
      <li>At least <strong>2 feet above or 10 feet horizontally</strong> from any window, door, chimney top, or adjacent building.</li>
    </ul>
    <p>These distances ensure that exhausted radon disperses safely instead of recirculating back into the home or a neighbor's home.</p>
  </div>
</section>

<section>
  <h2>Sealing scope — required, but not sufficient on its own</h2>
  <div class="prose-wide">
    <p>SSD works because of the pressure difference. Sealing reduces leakage paths so the fan can maintain that pressure difference efficiently. A correct SSD install includes sealing of:</p>
    <ul>
      <li>Visible slab cracks, especially around the perimeter and around the suction pit.</li>
      <li>The floor-wall joint (the gap between the slab and the foundation wall).</li>
      <li>Sump pit covers — a tight, gasketed seal with a transparent inspection port.</li>
      <li>Plumbing penetrations (drain pipes, water lines, gas lines).</li>
      <li>Any expansion joints in the slab.</li>
    </ul>
    <p>Sealing without depressurization is a myth — see <a href="/radon-mitigation-systems/why-sealing-isnt-enough/">why sealing alone isn't enough</a>. Sealing as part of an SSD system is essential.</p>
  </div>
</section>

<section>
  <h2>Colorado altitude correction</h2>
  <div class="prose-wide">
    <p>Radon fans are rated for sea-level performance. At Colorado Springs altitude (about 6,000 feet), a typical 4-inch inline fan loses roughly <strong>24% of its airflow capacity</strong>.<sup><a href="#src-3">[3]</a></sup> That has two implications for SSD design:</p>
    <ol>
      <li>The contractor may need to specify a <strong>larger fan</strong> than national catalog specs suggest. For tight soils or multi-point systems, this can mean upgrading from an RP145 to a GP500 or HS-series.</li>
      <li>Where a sea-level home would use one suction point, a Colorado home with the same soil type may need <strong>two</strong> — the fan can't pull a wider pressure field at altitude.</li>
    </ol>
    <p>Contractors who don't adjust for altitude can quote less but install a system that doesn't reduce radon below 4.0 pCi/L. <a href="/radon-mitigation-systems/fans-pipes-suction-points/">Full altitude correction details &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What to verify in a written SSD quote</h2>
  <div class="prose-wide">
    <ul class="checklist">
      <li>Specific number and location of suction points</li>
      <li>PFE diagnostic test included (for multi-zone or large homes)</li>
      <li>Specific fan model — RP145, GP500, HS-series, Fantech, or equivalent — selected for Colorado altitude</li>
      <li>Pipe size and routing path described</li>
      <li>Sealing scope itemized (slab cracks, floor-wall joint, sump, penetrations)</li>
      <li>Exhaust point that meets AARST/EPA distance requirements</li>
      <li>Manometer install at the suction point, accessible and visible</li>
      <li>Post-mitigation test within 30 days, 2–7 day duration, closed-house conditions<sup><a href="#src-1">[1]</a></sup></li>
      <li>Workmanship warranty (1–2 years labor minimum)</li>
      <li>Fan warranty (5 years on a name-brand fan)</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
    <li id="src-3">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
  </ol>
</aside>
"""


def ssd_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What is sub-slab depressurization?",
             "acceptedAnswer": {"@type": "Answer", "text": "Sub-slab depressurization (SSD) is the most common radon mitigation method for basements and slab-on-grade homes. A small pit is excavated beneath the slab and connected to a sealed PVC pipe that runs up to a fan and exhausts above the roofline. The fan creates suction beneath the slab so soil gas flows into the system rather than into the home."}},
            {"@type": "Question", "name": "What is a pressure field extension test?",
             "acceptedAnswer": {"@type": "Answer", "text": "A pressure field extension (PFE) test measures how far the negative pressure from one suction point spreads through the sub-slab soil. It tells the contractor whether a single suction point will cover the foundation or whether multiple points are needed. Quality contractors run a PFE on any multi-zone home, large slab, or tight-soil installation before quoting."}},
            {"@type": "Question", "name": "Why does Colorado SSD design differ from a national average?",
             "acceptedAnswer": {"@type": "Answer", "text": "Radon fans lose about 4% of airflow capacity per 1,000 feet of elevation. At Colorado Springs altitude (about 6,000 feet), a typical fan loses roughly 24% of its sea-level performance. Colorado SSD design often requires a larger fan or additional suction points to maintain the same pressure field at altitude."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 3. /radon-mitigation-systems/crawlspace-sub-membrane/
# =========================================================================
SMD_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Crawlspaces don't have a concrete slab to draw suction through, so they get a different approach: <strong>sub-membrane depressurization</strong> (SMD). Instead of drilling through concrete, the contractor creates the "slab" out of a heavy sealed vapor barrier laid across the entire crawlspace floor, then pulls suction from beneath it.</p>
    <p>This page covers how SMD works, the specific vapor barrier and sealing requirements, why crawlspace systems cost more than basement systems, and how SMD interacts with crawlspace encapsulation.</p>
  </div>
</section>

<section>
  <h2>How SMD works</h2>
  <div class="prose-wide">
    <p>A correctly installed crawlspace mitigation system has these elements:</p>
    <ol>
      <li><strong>Site prep.</strong> Debris removal, addressing moisture if present, clearing the floor to the dirt or coarse gravel base.</li>
      <li><strong>Vapor barrier laid across the entire crawlspace floor.</strong> Current best practice favors a heavier reinforced membrane (10–20 mil) over the older 6-mil minimum. The barrier overlaps any seams by at least 12 inches.</li>
      <li><strong>Perimeter sealing.</strong> The membrane is attached to the foundation walls or footings and sealed with mastic or specialized tape so soil gas can't bypass it at the edge.</li>
      <li><strong>Seam and penetration sealing.</strong> Lap seams between sheets are sealed. Plumbing, HVAC ducts, and any structural penetrations are sealed where they pass through the membrane.</li>
      <li><strong>Suction point</strong> drawing air from beneath the membrane, connected to a PVC pipe.</li>
      <li><strong>Pipe routing</strong> from the suction point, through the rim joist or up an exterior wall, to the fan and then to an exhaust point above the roofline.</li>
      <li><strong>Fan</strong> sized for the crawlspace area and Colorado altitude.</li>
      <li><strong>Manometer</strong> at the suction point, accessible from the crawlspace hatch or wherever the system is visible.</li>
      <li><strong>Post-mitigation test</strong> verifying indoor radon is below 4.0 pCi/L.<sup><a href="#src-1">[1]</a></sup></li>
    </ol>
  </div>
</section>

<section>
  <h2>The vapor barrier — why 6-mil is no longer the standard</h2>
  <div class="prose-wide">
    <p>Older AARST standards allowed 6-mil polyethylene as the minimum vapor barrier thickness. The industry has largely moved past that:</p>
    <ul>
      <li><strong>6-mil tears easily</strong> when crawlspaces see foot traffic for future HVAC or plumbing work.</li>
      <li><strong>10–20 mil reinforced</strong> membranes are more puncture-resistant and seal better at the seams.</li>
      <li>Some installers now use <strong>20-mil string-reinforced</strong> material as a standard option for permanent installs.</li>
    </ul>
    <p>If your crawlspace mitigation quote calls for 6-mil for a permanent system, ask why. There may be a valid reason (very small space, no future foot traffic expected, cost constraint, or a very dry space) — or the contractor may be using outdated specs. The heavier barrier costs more upfront and saves headaches later.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>Sealing is what makes the system work</h2>
  <div class="prose-wide">
    <p>SMD only works if the vapor barrier is genuinely sealed. Unsealed seams, gaps at the perimeter, and unsealed penetrations all let soil gas bypass the membrane and re-enter the crawlspace air above it.</p>
    <p>Three sealing scopes a quality contractor itemizes:</p>
    <ol>
      <li><strong>Perimeter sealing</strong> — the membrane attached to the foundation wall or footings with butyl tape, mastic, or polyurethane sealant.</li>
      <li><strong>Lap and seam sealing</strong> — wherever two sheets of membrane meet, they overlap by at least 12 inches and are sealed at both edges.</li>
      <li><strong>Penetration sealing</strong> — plumbing pipes, HVAC ducts, structural posts, and any other element passing through the membrane is sealed with a boot or sealant.</li>
    </ol>
  </div>
</section>

<section>
  <h2>Why labor is harder in a crawlspace</h2>
  <div class="prose-wide">
    <p>The system inside a basement is installed in standing height with good lighting. Inside a crawlspace, the installer is often on knees, stomach, and elbows. Three conditions push the labor cost up:</p>
    <ul>
      <li><strong>Low headroom.</strong> Anything under 30 inches makes every motion slower.</li>
      <li><strong>Debris and moisture.</strong> Old insulation scraps, construction debris, and damp dirt all need clearing before the barrier goes down.</li>
      <li><strong>Footing complexity.</strong> Stone, post-and-pier, or stepped foundations are detailed work to seal against.</li>
    </ul>
    <p>This is most of why crawlspace mitigation costs $1,800–$4,000 in Colorado Springs vs $900–$1,900 for a basement install. <a href="/radon-mitigation-cost/crawlspaces/">Full crawlspace cost breakdown &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Encapsulation and mitigation — same materials, different goals</h2>
  <div class="prose-wide">
    <p>Crawlspace <strong>encapsulation</strong> is a moisture and air quality treatment. A vapor barrier covers the floor (and often walls), sealed and sometimes paired with a dehumidifier. The goal is dry crawlspace air.</p>
    <p>Crawlspace <strong>radon mitigation</strong> uses similar materials — a sealed vapor barrier — but adds an active depressurization fan beneath the membrane. The goal is reducing indoor radon below 4.0 pCi/L, verified by a post-mitigation test.</p>
    <p>Encapsulation without active depressurization may incidentally reduce radon, but it isn't designed to and isn't verified. If your crawlspace has elevated radon, the system needs to be a true SMD with a fan and a post-mitigation test — not just encapsulation.</p>
    <p>Many Colorado contractors bundle the two services. If yours does, ask whether the bundled price includes the active fan and the post-mit test, or only the membrane and dehumidifier.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a Black Forest homeowner with a damp crawlspace</strong>
    <p>A homeowner with a 900 sq ft crawlspace, low headroom, and visible moisture on the dirt floor gets two quotes. Contractor A ($2,200) proposes a 6-mil barrier with one suction point and minimal perimeter sealing. Contractor B ($3,400) proposes a 15-mil reinforced barrier, full debris removal, perimeter and footing sealing, two suction points (the crawlspace is L-shaped and the soil doesn't communicate corner-to-corner), and a small dehumidifier bundled in. Both are legitimate proposals. The first will likely install in a day and may bring radon below 4.0 pCi/L. The second will last longer, address the moisture issue, and is the durable choice for the conditions. The homeowner's decision is a tradeoff between upfront cost and long-term durability.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards for Single-Family Buildings. <a href="{s('aarst_sgm_sf')}" rel="noopener" target="_blank">aarst.org</a></li>
  </ol>
</aside>
"""


def smd_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What is sub-membrane depressurization?",
             "acceptedAnswer": {"@type": "Answer", "text": "Sub-membrane depressurization (SMD) is the radon mitigation method used for crawlspaces. A heavy vapor barrier is laid across the entire crawlspace floor, sealed at the perimeter and at penetrations, and a fan creates suction beneath the membrane. Soil gas flows into the system and is exhausted above the roofline rather than entering the home."}},
            {"@type": "Question", "name": "Is a 6-mil vapor barrier enough for crawlspace radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "6-mil polyethylene was the older AARST minimum. Current industry practice favors heavier reinforced membranes (10–20 mil) because they're more puncture-resistant for future foot traffic and seal better at seams. If your quote calls for 6-mil for a permanent system, ask why."}},
            {"@type": "Question", "name": "Is crawlspace encapsulation the same as radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Encapsulation is a moisture treatment using a sealed vapor barrier (sometimes with a dehumidifier). Radon mitigation adds an active depressurization fan beneath the barrier and verifies success with a post-mitigation test. Encapsulation alone may reduce radon incidentally but isn't designed to."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 4. /radon-mitigation-systems/passive-vs-active/
# =========================================================================
PASSIVE_ACTIVE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>If you bought a newer Colorado home — say, anything built after 2009 — there's a good chance your home has a <strong>passive radon system</strong> in it. Maybe nobody mentioned it. Maybe you saw a white PVC pipe in the basement or an exhaust pipe sticking up through the roof and wondered what it was for.</p>
    <p>That's the rough-in. Whether it's actually doing anything for you depends on whether it's been tested and activated. This page explains the difference between passive and active systems, when each is right, and what to check if you bought a home with a passive system already in place.</p>
  </div>
</section>

<section>
  <h2>The short version</h2>
  <div class="prose-wide">
    <table>
      <thead>
        <tr><th></th><th>Passive system</th><th>Active system</th></tr>
      </thead>
      <tbody>
        <tr><td>Has a fan?</td><td>No</td><td>Yes</td></tr>
        <tr><td>Typical reduction</td><td>Up to 50%</td><td>Up to 99%</td></tr>
        <tr><td>Operating cost</td><td>$0</td><td>Less than $10/month</td></tr>
        <tr><td>Maintenance</td><td>None</td><td>Fan replacement every 5+ years</td></tr>
        <tr><td>Reliability</td><td>Depends on stack effect (weather-dependent)</td><td>Constant</td></tr>
        <tr><td>Sufficient on its own?</td><td>Only if post-construction test &lt; 4.0 pCi/L</td><td>Yes, when correctly designed</td></tr>
      </tbody>
    </table>
    <p style="font-size:.88rem;color:var(--text-muted);">Reduction figures: ASTM E1465 and AARST standards.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>What "passive" actually means</h2>
  <div class="prose-wide">
    <p>A passive radon system is a complete mitigation system <em>minus the fan</em>. There's a suction point through the slab (or beneath a crawlspace membrane), a sealed PVC pipe running up through the home or up an exterior wall, and an exhaust point above the roofline. What's missing is the inline fan that would create active suction.</p>
    <p>Instead, the system relies on the <strong>stack effect</strong> — the natural tendency of warm air to rise and create slight upward draft in vertical pipes. The temperature difference between the soil and the outside air, combined with the height of the exhaust stack, creates a small pressure differential that pulls soil gas up through the pipe.</p>
    <p>It works modestly. In a tight, well-sealed home in a cold climate, a passive system can reduce indoor radon by up to 50%. In warmer weather, with the stack effect weaker, the reduction is less.</p>
  </div>
</section>

<section>
  <h2>Why newer Colorado homes have passive systems</h2>
  <div class="prose-wide">
    <p>Starting in 2009, the International Residential Code (IRC) introduced an optional appendix for radon-resistant new construction. The appendix was originally called <strong>Appendix F</strong>, became Appendix AF in 2021, and is now <strong>Appendix BE</strong> in the 2024 IRC.<sup><a href="#src-2">[2]</a></sup> The appendix requires a passive radon system to be installed during new construction in EPA Zone 1 — which includes all of Colorado.</p>
    <p>What this means for buyers of newer Colorado homes:</p>
    <ul>
      <li>If your home was built after Colorado jurisdictions adopted IRC Appendix F or its successors, there's likely a passive system already roughed in.</li>
      <li>The white PVC pipe you may see in an unfinished basement, garage, or coming through the attic and roof is part of the passive system.</li>
      <li>The system is doing some work — but unless the builder ran a post-construction radon test, you don't know if it's enough.</li>
    </ul>
  </div>
</section>

<section>
  <h2>When passive becomes active</h2>
  <div class="prose-wide">
    <p>The 2021 and later IRC versions say new-home radon control is incomplete unless a post-construction test confirms radon levels below 4.0 pCi/L.<sup><a href="#src-2">[2]</a></sup> If the test fails, the system is upgraded to active — the contractor adds a fan to the existing pipe and verifies the result.</p>
    <p>Activation cost is typically <strong>$300–$800</strong> because most of the system is already there. The work is:</p>
    <ul>
      <li>Install a name-brand fan (RadonAway RP145 or equivalent) in the existing pipe, usually in the attic or in an exterior enclosure.</li>
      <li>Add a manometer at the existing suction point.</li>
      <li>Run electrical to the fan (sometimes a separate $150–$400 line item).</li>
      <li>Run a confirming post-mitigation test.</li>
    </ul>
    <p>If you bought a newer home with a passive system and haven't tested, that test should be your next move. If the result is at or above 4.0 pCi/L, activating the existing rough-in is the cheapest mitigation path you'll find.</p>
  </div>
</section>

<section>
  <h2>What to check if your home has a passive system</h2>
  <div class="prose-wide">
    <ul class="checklist">
      <li><strong>Find the pipe.</strong> It usually starts in an unfinished basement, exits through the rim joist or up through the attic, and emerges above the roofline. The pipe is white 3-inch or 4-inch PVC.</li>
      <li><strong>Look for a manometer.</strong> A passive system typically has no manometer; an active one does. If you see a U-tube gauge mounted on the pipe with both columns at the same level, the fan may have been installed but isn't running. If the columns are at different levels, the fan is running.</li>
      <li><strong>Check builder documentation.</strong> If a post-construction radon test was run, the result should be in your home's construction paperwork.</li>
      <li><strong>Test the home.</strong> A short-term DIY kit ($15–$40) is the fastest way to know whether the passive system is keeping levels below 4.0 pCi/L.</li>
      <li><strong>If the test is high, get an activation quote.</strong> Activation is far cheaper than a full new system.</li>
    </ul>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a 2018 build in Falcon</strong>
    <p>A homeowner closed on a 2018 build in Falcon. The seller's disclosure mentioned a "passive radon system" but no test result. The new owner ran a short-term DIY kit a month after moving in and got 5.4 pCi/L. They called a Colorado-licensed contractor for an activation quote: $550 for a RadonAway RP145 fan installed in the attic, manometer added, electrical permit pulled, and a post-mitigation test included. Two weeks after activation, the post-mit test came back at 1.3 pCi/L. The homeowner kept the activation documentation in their closing folder — it's now part of their required SB23-206 disclosure if they ever sell.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">ASTM E1465 and ANSI/AARST mitigation standards. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
    <li id="src-2">IRC Appendix BE (radon-resistant new construction). <a href="{s('irc_appendix_be')}" rel="noopener" target="_blank">aarst.org/building-codes-standards</a></li>
  </ol>
</aside>
"""


def passive_active_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What's the difference between a passive and active radon system?",
             "acceptedAnswer": {"@type": "Answer", "text": "A passive radon system has the pipe but no fan, relying on natural updraft (stack effect) to reduce radon by up to 50%. An active system has a fan running 24/7 and reduces radon by up to 99%. Most homes that test above the EPA action level need an active system."}},
            {"@type": "Question", "name": "Do newer Colorado homes have radon systems?",
             "acceptedAnswer": {"@type": "Answer", "text": "Often yes. Starting in 2009, the International Residential Code (IRC) introduced an appendix requiring passive radon systems in new construction in EPA Zone 1 — which includes all of Colorado. The appendix is now IRC Appendix BE as of 2024. If your home was built after the local jurisdiction adopted the appendix, there's likely a passive system already roughed in."}},
            {"@type": "Question", "name": "How much does it cost to activate a passive radon system?",
             "acceptedAnswer": {"@type": "Answer", "text": "Activation typically costs $300–$800 because most of the system (pipe, suction point, exhaust) is already in place. The work is installing the fan, adding a manometer, running electrical, and conducting a post-mitigation test. Activation is far cheaper than a full new system."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 5. /radon-mitigation-systems/fans-pipes-suction-points/   — EQUIPMENT DEEP DIVE
# =========================================================================
EQUIPMENT_BODY = f"""
<section>
  <div class="prose-wide">
    <p>The pipe is white PVC. The fan looks like a coffee can in the attic. The manometer is a small plastic U-tube with colored fluid in it. Together they make up a working radon mitigation system, and the right combination matters more in Colorado than almost anywhere else — because altitude changes what those parts need to do.</p>
    <p>This page is the equipment deep dive: what fan models do what, what pipe specs are correct, what manometers should read, and how Colorado's altitude changes all of it.</p>
  </div>
</section>

<section>
  <h2>Radon fans — the heart of the system</h2>
  <div class="prose-wide">
    <p>A radon fan looks like a small inline duct fan. It runs continuously, drawing 50–90 watts of electricity, and creates suction in the suction point beneath the slab or membrane. The right fan depends on three variables:</p>
    <ul>
      <li><strong>Soil type</strong> under the slab — porous gravel needs less suction; tight clay needs more.</li>
      <li><strong>Foundation area</strong> — bigger slabs require more airflow.</li>
      <li><strong>Altitude</strong> — Colorado fans need more power than national catalogs suggest.</li>
    </ul>

    <h3>Common fan models</h3>
    <table>
      <thead>
        <tr><th>Model</th><th>Best for</th><th>Typical retail</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>RadonAway RP140</strong><br>4-inch inline, 15–21 watts, max 0.8" WC</td>
          <td>Very porous gravel, small home</td>
          <td>$120–$160</td>
        </tr>
        <tr>
          <td><strong>RadonAway RP145</strong><br>4-inch inline, 37–71 watts, max 2.1" WC</td>
          <td>Standard porous-gravel basement install</td>
          <td>$150–$200</td>
        </tr>
        <tr>
          <td><strong>RadonAway GP500</strong><br>3-inch high-performance, 85–153 watts, max 4.0" WC</td>
          <td>Moderate-to-tight soils, multi-suction systems</td>
          <td>$250–$350</td>
        </tr>
        <tr>
          <td><strong>RadonAway HS-series</strong><br>3-inch in / 2-inch out, 120–381 watts</td>
          <td>Very tight clay or sand, extreme soil conditions</td>
          <td>$400–$600</td>
        </tr>
      </tbody>
    </table>
    <p style="font-size:.88rem;color:var(--text-muted);">All major fan brands (RadonAway, Festa AMG, Fantech) carry typical 5-year manufacturer warranties.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>Colorado's altitude correction — the part most national guides miss</h2>
  <div class="prose-wide">
    <p>This is where Colorado mitigation design genuinely differs from a national average. Radon fans are rated at sea level. Their performance drops with altitude:</p>
    <ul>
      <li><strong>~4% airflow loss per 1,000 feet of elevation.</strong><sup><a href="#src-2">[2]</a></sup></li>
      <li><strong>Denver</strong> (5,280 ft): a RadonAway RP145's maximum water column rating drops from 2.1" to roughly 1.6".</li>
      <li><strong>Colorado Springs</strong> (about 6,000 ft): roughly 24% drop. The RP145 maxes out at about 1.6" WC.</li>
      <li><strong>Mountain towns</strong> (7,000–9,000 ft): the drop is significant enough that fans must often be upsized.</li>
    </ul>
    <p>What this means in practice:</p>
    <ul>
      <li>A fan that's perfectly sized for a sea-level install may be <strong>underpowered</strong> in Colorado.</li>
      <li>Where a sea-level home could use a single suction point with an RP145, a Colorado home with the same soil might need either a <strong>larger fan</strong> (GP500 instead) or a <strong>second suction point</strong>.</li>
      <li>Contractors working only off national catalog specs are the contractors most likely to under-fan a Colorado system. The result shows up in the post-mitigation test — radon levels still above 4.0 pCi/L.</li>
    </ul>
    <p>Ask your contractor which fan model they're specifying, and ask why. A good answer references your altitude, your soil type, and your slab size. "We always use an RP145" is not a good answer for a multi-point or tight-soil install at 6,000 feet.</p>
  </div>
</section>

<section>
  <h2>Pipe — the simple part that still has specs</h2>
  <div class="prose-wide">
    <p>The pipe is Schedule 40 PVC, either 3-inch or 4-inch diameter. Specs:<sup><a href="#src-3">[3]</a></sup></p>
    <ul>
      <li><strong>3-inch minimum, 4-inch preferred</strong> for most residential installs.</li>
      <li>All joints are sealed with PVC primer and cement.</li>
      <li>Horizontal runs <strong>slope 3/8 to 1/2 inch per foot</strong> back toward the suction point so condensation drains where it can't pool.</li>
      <li>Vertical runs are supported every 4–6 feet to prevent sagging.</li>
      <li>The pipe between the fan and the exhaust is under <strong>positive pressure</strong>, so any leak in that section would release radon into the surrounding space. That section must be entirely in unconditioned space (attic, exterior).</li>
    </ul>
  </div>
</section>

<section>
  <h2>Suction points — how the system pulls air from beneath the slab</h2>
  <div class="prose-wide">
    <p>A suction point starts as a 4-inch hole cored through the slab. The contractor excavates a small pit beneath — typically 12–18 inches deep and roughly 12 inches in diameter — to give the system a place to draw soil gas from. The pipe is connected to the pit with a sealed fitting, and the slab around the pit is sealed.</p>
    <p>How many suction points do you need? It depends on:</p>
    <ul>
      <li><strong>Sub-slab soil communication</strong> — measured by a PFE diagnostic test.</li>
      <li><strong>Slab area and footprint</strong> — bigger slabs may need more points.</li>
      <li><strong>Foundation zones</strong> — split-level, tri-level, and addition slabs are separate zones.</li>
      <li><strong>Soil type</strong> — tight clay reduces the radius of influence of each suction point.</li>
    </ul>
    <p>A single suction point handles most Colorado basements with porous gravel under the slab. A multi-zone home (tri-level, split-level, basement plus crawlspace) typically needs two or more.</p>
  </div>
</section>

<section>
  <h2>Manometers — how you know the system is working</h2>
  <div class="prose-wide">
    <p>The manometer is a small U-tube gauge (or digital pressure sensor) mounted at the suction point. It measures the pressure differential between the air outside the system and the air inside the system. The standard analog manometer has two clear tubes connected at the bottom, each filled with a colored fluid (typically red mineral oil).</p>
    <p>What a working manometer shows:</p>
    <ul>
      <li>The two fluid columns are <strong>at different levels</strong>. The pressure under the slab is lower than the indoor air pressure, which pushes fluid down on the system side and up on the outside.</li>
      <li>A typical reading is <strong>0.5 to 2.0 inches of water column</strong> offset.</li>
      <li>When the fan is off (power failure or fan failure), the columns equalize.</li>
    </ul>
    <p>What to do when you check the manometer monthly:</p>
    <ul>
      <li>If both columns are at the same level → the fan isn't running. Call the original installer.</li>
      <li>If the columns show a sudden change in reading → the system condition has changed. Worth a service call.</li>
      <li>If the reading is steady and offset → the system is doing its job.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Operating cost and fan lifespan</h2>
  <div class="prose-wide">
    <p>A radon fan draws 50–90 watts continuously. At Colorado Springs electricity rates, that works out to <strong>$5–$10 per month</strong> in electricity. EPA pegs the typical cost at under $10/month.<sup><a href="#src-4">[4]</a></sup></p>
    <p>Fan lifespan: most manufacturers warranty for <strong>5 years</strong>; many fans run 7–10 years before replacement is needed.<sup><a href="#src-1">[1]</a></sup> Replacement runs $150–$400 in parts plus 1–2 hours of labor.</p>
    <p>Signs a fan needs replacement:</p>
    <ul>
      <li>Audible humming, rattling, or grinding from the fan housing.</li>
      <li>Manometer reading dropping over time.</li>
      <li>Visible vibration or movement of the fan housing.</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>: typical fan lifespan and warranty. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">RadonAway. <em>Fan Specifications &amp; Altitude Correction</em>. <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
    <li id="src-3">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards. <a href="{s('aarst_sgm_sf')}" rel="noopener" target="_blank">aarst.org</a></li>
    <li id="src-4">National Radon Proficiency Program. <a href="{s('nrpp')}" rel="noopener" target="_blank">nrpp.info</a></li>
  </ol>
</aside>
"""


def equipment_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How does Colorado altitude affect radon fan selection?",
             "acceptedAnswer": {"@type": "Answer", "text": "Radon fans lose roughly 4% of their airflow capacity per 1,000 feet of elevation. At Colorado Springs altitude (about 6,000 feet), a typical fan loses roughly 24% of its sea-level performance. Colorado systems often require a larger fan model (GP500 instead of RP145) or an additional suction point to compensate."}},
            {"@type": "Question", "name": "How long does a radon fan last?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most manufacturer warranties are 5 years. In practice, many radon fans run 7–10 years before replacement is needed. Replacement runs $150–$400 in parts plus 1–2 hours of labor. Signs a fan needs replacement include audible humming or rattling, dropping manometer readings, and visible vibration."}},
            {"@type": "Question", "name": "How do I read a radon system manometer?",
             "acceptedAnswer": {"@type": "Answer", "text": "A working manometer shows two fluid columns at different levels — typically 0.5 to 2.0 inches of water column offset. If the columns are at the same level, the fan isn't running. A sudden change in reading warrants a service call. A steady, offset reading means the system is working."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 6. /radon-mitigation-systems/why-sealing-isnt-enough/
# =========================================================================
SEALING_BODY = f"""
<section>
  <div class="prose-wide">
    <p>One of the most common things Colorado homeowners try first is sealing. Seal the basement floor cracks, seal the sump pit, seal the wall-floor joint, and hope the radon stops getting in. It feels intuitive: less openings, less radon.</p>
    <p>The problem is that radon is driven by a pressure difference, not by opening size. Without changing the pressure, sealing alone almost never reduces radon below the action level — and in some cases makes the problem worse by concentrating the gas at the openings you missed.<sup><a href="#src-1">[1]</a></sup></p>
    <p>This page explains why, what sealing IS good for (it's part of every working mitigation system), and what the right path forward looks like.</p>
  </div>
</section>

<section>
  <h2>What CDPHE says</h2>
  <div class="prose-wide">
    <div class="callout">
      <strong>CDPHE on sealing alone:</strong>
      <p>The Colorado Department of Public Health and Environment specifically warns that sealing cracks alone is unreliable as a mitigation method and can sometimes make radon levels worse.<sup><a href="#src-1">[1]</a></sup> The recommended approach is sub-slab depressurization for basements and slab homes, or sub-membrane depressurization for crawlspaces.</p>
    </div>
  </div>
</section>

<section>
  <h2>Why sealing alone doesn't work</h2>
  <div class="prose-wide">
    <p>Radon enters a home for one reason: the air pressure inside is slightly lower than the pressure in the soil. That pressure difference — driven largely by the <strong>stack effect</strong> in winter, when warm indoor air rises and creates suction at lower levels — pulls soil gas up through whatever openings it can find.</p>
    <p>Three reasons sealing without depressurization fails:</p>
    <ol>
      <li><strong>You can't seal everything.</strong> Visible slab cracks are the obvious targets. The microscopic porosity of concrete itself is not. Plumbing penetrations, slab expansion joints, and the floor-wall joint can all be sealed, but small gaps remain. Soil gas finds the smallest unsealed path and flows through it.</li>
      <li><strong>Sealing changes which openings the gas uses.</strong> If you seal 90% of the obvious openings, the 10% you missed now carry the full pressure-driven flow. Sometimes radon concentration at remaining points goes <em>up</em> rather than down, depending on where the unsealed gaps are.</li>
      <li><strong>The pressure difference is unchanged.</strong> Sealing doesn't change the stack effect or the soil-gas pressure beneath your foundation. The driving force for radon entry is exactly the same as before.</li>
    </ol>
  </div>
</section>

<section>
  <h2>What sealing IS good for</h2>
  <div class="prose-wide">
    <p>Sealing is essential — as part of a working mitigation system. Once an SSD or SMD fan is running and creating negative pressure beneath the foundation, sealing the major openings makes the system efficient. Why:</p>
    <ul>
      <li>Sealed openings mean the fan doesn't have to pull more air than necessary, so a smaller fan can do the job.</li>
      <li>Sealing prevents conditioned indoor air from being pulled into the system (which would be a waste of heating or cooling energy).</li>
      <li>Sealing prevents short-circuiting — where the system pulls air down through an obvious opening and creates only a local pressure drop instead of an even pressure field across the whole slab.</li>
    </ul>
    <p>So a correct SSD or SMD install includes both depressurization AND sealing. Neither one alone is enough.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>The temptation — and why it's expensive in the long run</h2>
  <div class="prose-wide">
    <p>Sealing kits are sold at hardware stores for $50–$200. The temptation is to seal the obvious cracks, retest, and hope the number comes down enough to skip a $1,000–$2,000 mitigation system. Two reasons this usually backfires:</p>
    <ul>
      <li>The retest typically comes back at the same level or close to it. You've spent $100 on sealant and a weekend on labor and learned what CDPHE already said: sealing alone doesn't work.</li>
      <li>Some sealed homes show <em>worse</em> radon readings after sealing, because the gas has been concentrated at fewer entry points. If you missed one of the bigger gaps, that gap now carries the full soil-gas flow.</li>
    </ul>
    <p>The cheaper path is to test once, mitigate once, and retest. The $1,000–$2,000 you spend on a working SSD system is less than the $100 sealing kit plus a second test plus the eventual mitigation install. <a href="/radon-mitigation-cost/">More on cost &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What about radon paints and barriers?</h2>
  <div class="prose-wide">
    <p>Various products are sold as "radon-blocking" paints, sealants, or floor coatings. The reality is similar to crack sealing:</p>
    <ul>
      <li>None of them changes the pressure differential driving radon entry.</li>
      <li>Concrete itself is mildly porous; coatings don't fully eliminate this pathway.</li>
      <li>Marketing claims of "blocks radon" are not the same as "reduces radon levels below 4.0 pCi/L verified by post-treatment testing."</li>
    </ul>
    <p>These products may have value as part of a larger sealed-vapor-barrier system in a crawlspace, but they aren't a standalone solution for elevated radon. The EPA, CDPHE, and AARST all recommend active depressurization as the verified method.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a Colorado homeowner who tried sealing first</strong>
    <p>A Colorado Springs homeowner tested at 5.8 pCi/L. Hoping to avoid mitigation, they spent a weekend sealing visible slab cracks, the sump pit lid, and the floor-wall joint with $130 of polyurethane sealant. Two weeks later they retested. The result: 5.4 pCi/L. The 0.4 pCi/L reduction wasn't enough to bring the home below the action level. The homeowner then hired a DORA-licensed contractor for a $1,450 sub-slab depressurization install. The post-mitigation test came back at 1.2 pCi/L. The sealing work wasn't wasted — the contractor used the same sealed openings as part of the system — but the sealing alone was never going to do the job.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def sealing_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "Can I fix my radon problem by sealing cracks?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Radon enters because of a pressure difference between the soil and your home's interior, not because of opening size. Sealing alone doesn't change that pressure difference and almost never reduces radon below the EPA action level. CDPHE specifically warns that sealing alone can sometimes concentrate radon at remaining openings and make the problem worse."}},
            {"@type": "Question", "name": "Why is sealing part of a working radon system if it doesn't work alone?",
             "acceptedAnswer": {"@type": "Answer", "text": "Sealing is essential alongside active depressurization. It prevents the fan from pulling conditioned indoor air into the system, allows a smaller fan to maintain pressure across the slab, and prevents short-circuiting. Both depressurization and sealing are required for an efficient mitigation system."}},
            {"@type": "Question", "name": "Do radon-blocking paints work?",
             "acceptedAnswer": {"@type": "Answer", "text": "Not as a standalone solution. Marketed radon-blocking paints and coatings don't change the pressure differential driving radon entry. They may have value as part of a sealed vapor barrier in a crawlspace, but EPA, CDPHE, and AARST all recommend active depressurization as the verified mitigation method."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 7. /radon-mitigation-systems/what-happens-after-mitigation/
# =========================================================================
AFTER_MITIGATION_BODY = f"""
<section>
  <div class="prose-wide">
    <p>The install crew left this afternoon. The fan is running, the manometer is showing offset between the two columns, and your contractor handed you paperwork on the way out the door. Now what? When do you know it's working? When do you need to retest? What signs should you watch for over the next 5–10 years?</p>
    <p>This page is the post-mitigation roadmap. Calmly answer those questions in the order they actually come up.</p>
  </div>
</section>

<section>
  <h2>Step 1: The post-mitigation test (the first 30 days)</h2>
  <div class="prose-wide">
    <p>A working mitigation system is verified by a post-mitigation test. The EPA and AARST recommendations:<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li><strong>Within 30 days</strong> of system activation.</li>
      <li><strong>No sooner than 24 hours</strong> after the fan starts running, to let the system stabilize.</li>
      <li><strong>2 to 7 days</strong> of test duration.</li>
      <li><strong>Closed-house conditions</strong> for 12 hours before and during the test. Normal in-and-out traffic is fine; sustained windows or doors open is not.</li>
      <li>Placed in the <strong>lowest livable level</strong> of the home, 2–6 feet above the floor, away from drafts, vents, and high-humidity areas.</li>
    </ul>
    <p>Some Colorado contractors include the post-mit test in the install quote. Others charge $125–$200 separately. If your install quote was silent on the post-mit test, ask. A working system without a verified post-mit test is a working system you can't prove.</p>
    <p>A common best practice: have an <strong>independent (non-installer) tester</strong> do the post-mitigation test to avoid any conflict of interest. EPA explicitly recommends this.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>What "passing" looks like</h2>
  <div class="prose-wide">
    <p>The post-mit test result should come back well below the EPA action level of 4.0 pCi/L. A properly designed system should bring most Colorado homes to <strong>under 2.0 pCi/L</strong> — often under 1.0.<sup><a href="#src-1">[1]</a></sup> If your result comes back:</p>
    <table class="compact">
      <thead>
        <tr><th>Result (pCi/L)</th><th>What it means</th></tr>
      </thead>
      <tbody>
        <tr><td>&lt; 2.0</td><td>System is working well. This is the expected outcome for a quality install.</td></tr>
        <tr><td>2.0–3.9</td><td>Below action level but higher than ideal. Confirm with a second test in a different season. Consider asking the contractor to verify the system.</td></tr>
        <tr><td>4.0 or above</td><td>The system did not bring radon below the action level. Call the contractor; the system needs adjustment (often an additional suction point or a larger fan).</td></tr>
      </tbody>
    </table>
    <p>Quality contractors include a written guarantee that the system will achieve below 4.0 pCi/L on post-mit testing. If yours did and the test fails, they should add the additional suction point or upgrade the fan at no extra cost.</p>
  </div>
</section>

<section>
  <h2>Step 2: The manometer routine (every month)</h2>
  <div class="prose-wide">
    <p>The manometer is your at-a-glance system health indicator. A monthly check takes 30 seconds:</p>
    <ol>
      <li>Look at the two fluid columns. They should be at <strong>different levels</strong> — typically 0.5 to 2.0 inches of water column offset.</li>
      <li>The offset doesn't have to be the same every time, but it should be reasonably steady — within roughly the same range month to month.</li>
    </ol>
    <p>What to do if you see something different:</p>
    <ul>
      <li><strong>Both columns at the same level</strong> → the fan isn't running. Could be a power issue (check the circuit), a fan failure, or a tripped GFCI. Call the original installer.</li>
      <li><strong>Reading much lower than usual</strong> → the system is losing efficiency. Possible causes: fan starting to fail, a leak in the pipe, or a seal that has broken. Service call.</li>
      <li><strong>Reading much higher than usual</strong> → less common but possible if the soil-gas conditions changed (e.g., a heavy rain saturated the soil). Worth noting but usually not urgent.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Step 3: Retest cadence (every 2 years and after major changes)</h2>
  <div class="prose-wide">
    <p>The EPA recommends retesting your home every <strong>2 years</strong>, even with a working mitigation system.<sup><a href="#src-1">[1]</a></sup> The reasons:</p>
    <ul>
      <li>Soil-gas conditions change over time as the home settles, foundations age, and water table conditions shift.</li>
      <li>Fans degrade slowly over their lifespan — a fan that's bringing levels to 1.5 pCi/L now might be at 3.5 pCi/L in five years.</li>
      <li>Climate and seasonal patterns affect radon levels. A test in summer captures different conditions than one in winter.</li>
    </ul>
    <p>Colorado has significant seasonal swings — winter levels (sealed-up homes, stronger stack effect) are typically higher than summer levels. EPA notes that long-term tests average across seasons, which is why long-term tests are useful for re-verification.</p>
    <p>You should also retest:</p>
    <ul>
      <li>After major remodeling that changes the foundation, basement, or HVAC.</li>
      <li>After adding new living space (finishing a basement, adding a room).</li>
      <li>If you notice the manometer behaving differently.</li>
      <li>Before listing the home for sale.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Step 4: Fan lifespan and replacement</h2>
  <div class="prose-wide">
    <p>The fan is the only routine maintenance item. Most manufacturers warrant fans for <strong>5 years</strong>; in practice they often run 7–10 years before needing replacement.<sup><a href="#src-1">[1]</a></sup></p>
    <p>Signs your fan needs replacement:</p>
    <ul>
      <li>Audible humming, rattling, or grinding from the fan housing.</li>
      <li>Manometer reading dropping over time.</li>
      <li>Visible vibration or movement of the fan.</li>
      <li>A retest showing radon levels rising.</li>
    </ul>
    <p>Replacement cost: $150–$400 in parts plus 1–2 hours of labor. Most Colorado contractors will replace the fan as a service call rather than a full new install.</p>
  </div>
</section>

<section>
  <h2>Step 5: Documentation and disclosure</h2>
  <div class="prose-wide">
    <p>Keep these documents permanently in a folder with your home records. They become part of your required SB23-206 disclosure if you ever sell the home:<sup><a href="#src-2">[2]</a></sup></p>
    <ul class="checklist">
      <li>Original test report (the high reading that triggered the install)</li>
      <li>Contractor's written quote and final invoice</li>
      <li>System certification, DORA license documentation, NRPP or NRSB certification number</li>
      <li>Fan model number and warranty</li>
      <li>Post-mitigation test result certificate</li>
      <li>Any retest results going forward</li>
      <li>Any service calls or fan replacements</li>
    </ul>
    <p>A buyer of your home is legally entitled to see all of this. A well-documented mitigation history is actually a selling point — it shows the radon problem is known, addressed, and verified.</p>
  </div>
</section>

<section>
  <div class="callout">
    <strong>Common scenario — a year with a working system</strong>
    <p>Day 1: install. Day 2: contractor sends activation paperwork and the manometer's initial reading (1.4 inches WC offset). Day 12: post-mit test placed in basement. Day 18: result comes back at 1.2 pCi/L. Day 19: contractor sends system certification packet. Month 1: monthly manometer check shows the same 1.4-inch offset. Months 2–11: same. Month 12: same. Year 2: retest with a short-term DIY kit. Result: 1.1 pCi/L. System is working as expected. Year 5: fan starts to make a faint humming. Manometer drops slightly to 1.1 inches WC. Homeowner calls the original contractor; new fan installed for $325. Manometer back to 1.4 inches WC. The system continues for another 5+ years.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">Colorado General Assembly. <em>SB23-206 (CRS § 38-35.7-112)</em>. <a href="{s('sb23_206')}" rel="noopener" target="_blank">leg.colorado.gov/bills/sb23-206</a></li>
  </ol>
</aside>
"""


def after_mitigation_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "When should I retest after radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Run a post-mitigation test within 30 days of install (no sooner than 24 hours after fan activation), then retest every 2 years per EPA recommendation. Also retest after major remodels that change the foundation or HVAC, after adding living space, if the manometer behaves differently, or before listing the home for sale."}},
            {"@type": "Question", "name": "What radon level should I expect after mitigation in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "A properly designed Colorado mitigation system should bring indoor radon to under 2.0 pCi/L — often under 1.0. Results above 4.0 pCi/L on the post-mitigation test mean the system needs adjustment (typically an additional suction point or larger fan). Quality contractors warranty a result below 4.0 pCi/L."}},
            {"@type": "Question", "name": "How do I read my radon system's manometer?",
             "acceptedAnswer": {"@type": "Answer", "text": "A working manometer shows two fluid columns at different levels — typically 0.5 to 2.0 inches of water column offset. If both columns are at the same level, the fan isn't running. A reading much lower than usual indicates the system is losing efficiency. A steady, offset reading means the system is working normally."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
