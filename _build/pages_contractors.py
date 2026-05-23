"""Content for the Contractor Selection pillar pages (Phase 5b build).

Six pages:
1. /radon-contractors/                                    — hub (How to Choose a Contractor)
2. /radon-contractors/verify-licenses-and-certifications/ — DORA + NRPP/NRSB lookup walkthrough
3. /radon-contractors/questions-to-ask/                   — Pre-hire question list
4. /radon-contractors/red-flags-in-a-quote/               — What to walk away from
5. /radon-contractors/warranties-and-retesting/           — Warranty standards + post-install
6. /radon-contractors/how-to-file-a-complaint/            — DORA complaint + BBB + AG
"""
import json
from pages_main import s, SOURCES

# Ensure needed sources registered (idempotent)
SOURCES.setdefault("dora_lookup", "https://apps.colorado.gov/dora/licensing/Lookup/LicenseLookup.aspx")
SOURCES.setdefault("nrpp_search", "https://nrpp.info/pro-search/")
SOURCES.setdefault("nrsb_search", "https://nrsb.org/for-professional/")
SOURCES.setdefault("co_attorney_general", "https://coag.gov/")
SOURCES.setdefault("bbb_colorado", "https://www.bbb.org/")
SOURCES.setdefault("epa_consumer_guide", "https://www.epa.gov/radon/consumers-guide-radon-reduction")
SOURCES.setdefault("dora_complaints", "https://dpo.colorado.gov/Filing-Complaint")
SOURCES.setdefault("aarst_standards", "https://standards.aarst.org/")
SOURCES.setdefault("radonaway_specs", "https://www.radonaway.com/")


# =========================================================================
# 1. /radon-contractors/   — HUB: How to Choose a Colorado Mitigation Contractor
# =========================================================================
CONTRACTORS_HUB_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Hiring a radon mitigation contractor in Colorado is different from hiring most contractors. Colorado is one of the few states with state-level radon contractor licensing — every legitimate mitigator has a license number you can look up in 30 seconds. That changes the dynamic. You're not picking from a stack of business cards and hoping for the best; you're verifying credentials, comparing scopes, and making a defensible choice.</p>
    <p>This page is the top-level guide: what credentials to check, what to ask, what to compare, and what to walk away from. Each link in the section below goes deeper.</p>
  </div>
</section>

<section>
  <h2>The two-credential rule</h2>
  <div class="prose-wide">
    <p>A legitimate Colorado radon mitigation contractor will have:</p>
    <ol>
      <li><strong>A current DORA radon mitigation license.</strong> Issued by Colorado DORA's Office of Radon Professionals (4 CCR 754-1). Required by law since July 1, 2022. Verifiable through the public license lookup.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>NRPP or NRSB certification.</strong> National Radon Proficiency Program or National Radon Safety Board. Voluntary nationally but required by CDPHE guidance for Colorado-licensed mitigators. Verifiable through each program's public directory.<sup><a href="#src-2">[2]</a></sup></li>
    </ol>
    <p>If a contractor can't provide both numbers, don't hire them. Not negotiable. The DORA license alone takes care of the legal requirement; the NRPP or NRSB certification confirms they actually know the AARST standards for designing a working system.</p>
    <p><a href="/radon-contractors/verify-licenses-and-certifications/">Step-by-step license verification walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What else to check</h2>
  <div class="prose-wide">
    <ul class="checklist">
      <li><strong>Years in business.</strong> 5+ years is a reasonable threshold; 10+ is preferred. New companies aren't automatically bad, but established ones have a track record.</li>
      <li><strong>BBB profile.</strong> Check for complaints, their pattern, and the contractor's responses.</li>
      <li><strong>Online reviews.</strong> Google reviews, Yelp, Angi. Read the negative reviews and look at the contractor's response — that often tells you more than the positive ones.</li>
      <li><strong>References.</strong> Ask for three recent customer references. A reputable contractor will provide them.</li>
      <li><strong>Liability insurance.</strong> $1M general liability is typical. Confirm in writing.</li>
      <li><strong>Workers' compensation.</strong> Confirms the contractor follows Colorado labor law and protects you if a worker is injured on your property.</li>
      <li><strong>Written estimate.</strong> Never accept a quote that isn't in writing. <a href="/radon-mitigation-cost/whats-in-a-quote/">Quote checklist &rarr;</a></li>
    </ul>
  </div>
</section>

<section>
  <h2>The interview process</h2>
  <div class="prose-wide">
    <p>A typical hiring sequence for Colorado mitigation:</p>
    <ol>
      <li><strong>Phone screen.</strong> Verify the DORA and NRPP/NRSB numbers, confirm they service your ZIP code, ask about availability. (~10 minutes per contractor.)</li>
      <li><strong>In-home assessment.</strong> The contractor walks the basement (or crawlspace) with you, asks about your test result, identifies the foundation type and obvious challenges. Should take 30–60 minutes. Reputable contractors don't charge for this.</li>
      <li><strong>Written quote.</strong> Detailed scope per the <a href="/radon-mitigation-cost/whats-in-a-quote/">quote checklist</a>. Usually delivered within 1–3 days.</li>
      <li><strong>Follow-up questions.</strong> If anything's unclear or different from another quote, ask. A contractor who can't or won't explain technical choices is a contractor to avoid.</li>
      <li><strong>References.</strong> Call at least one reference before signing. Ask about the install experience, whether the post-mitigation test result was as promised, and how the warranty has held up.</li>
      <li><strong>Sign and schedule.</strong> Most installs happen 1–2 weeks after signing.</li>
    </ol>
    <p><a href="/radon-contractors/questions-to-ask/">Full pre-hire question list &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Comparing quotes</h2>
  <div class="prose-wide">
    <p>Get at least two written quotes for any Colorado mitigation install, three for anything complex (crawlspace, multi-zone, finished basement with aesthetic concerns). When comparing:</p>
    <ul>
      <li>Compare <strong>scope</strong>, not just bottom-line price. A $1,400 quote and a $2,200 quote can both be honest if the scopes differ.</li>
      <li>Match foundation work, suction point count, fan model, sealing scope, pipe routing, exhaust point, manometer install, warranty, and post-mitigation test.</li>
      <li>Read the warranty language carefully.</li>
      <li>Ask each contractor what's pushing their price above or below the four-scenario framework.</li>
    </ul>
    <p><a href="/radon-mitigation-cost/quote-variation/">Five real cost drivers behind quote variation &rarr;</a> · <a href="/radon-mitigation-cost/quote-too-high/">Quote sanity-check tree &rarr;</a></p>
  </div>
</section>

<section>
  <h2>Red flags that mean walk away</h2>
  <div class="prose-wide">
    <ul>
      <li>No DORA license number, or refuses to provide one.</li>
      <li>No NRPP or NRSB certification.</li>
      <li>Cash-only payment.</li>
      <li>Won't put scope details in writing.</li>
      <li>Pressure tactics or "this price is good for today only."</li>
      <li>"Required" upgrades that the contractor can't explain technically.</li>
      <li>Refuses to provide references.</li>
      <li>Won't include a post-mitigation test in the quote.</li>
      <li>No written warranty.</li>
    </ul>
    <p><a href="/radon-contractors/red-flags-in-a-quote/">Full red flags walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>What happens after you sign</h2>
  <div class="prose-wide">
    <p>A typical Colorado mitigation install:</p>
    <ul>
      <li><strong>Install day:</strong> 4–8 hours on site for a basic basement; longer for crawlspace or multi-zone. The contractor cores the suction point, runs the pipe, installs the fan, seals openings, and mounts the manometer.</li>
      <li><strong>Activation:</strong> The fan is turned on before the contractor leaves. The manometer should show offset between the two columns within minutes.</li>
      <li><strong>Post-mitigation test:</strong> Within 30 days, 2–7 days of test duration under closed-house conditions.<sup><a href="#src-3">[3]</a></sup></li>
      <li><strong>Documentation:</strong> System certification, post-mit test result, fan model and warranty, manometer baseline reading.</li>
      <li><strong>Workmanship warranty:</strong> 1–2 years typical, 5 years on premium installs.</li>
      <li><strong>Fan warranty:</strong> 5 years typical from the manufacturer.</li>
    </ul>
    <p><a href="/radon-contractors/warranties-and-retesting/">Full warranty and post-install walkthrough &rarr;</a></p>
  </div>
</section>

<section>
  <h2>If something goes wrong</h2>
  <div class="prose-wide">
    <p>If the install doesn't bring radon below 4.0 pCi/L, if the system fails within warranty, or if the contractor becomes unreachable:</p>
    <ol>
      <li>Document the problem in writing to the contractor first. Most issues resolve at this step.</li>
      <li>File a BBB complaint if the contractor is unresponsive.</li>
      <li>File a DORA complaint with the Office of Radon Professionals. License revocation is on the table for repeat offenders.<sup><a href="#src-4">[4]</a></sup></li>
      <li>For serious financial harm, consult a Colorado consumer protection attorney.</li>
    </ol>
    <p><a href="/radon-contractors/how-to-file-a-complaint/">Full complaint process walkthrough &rarr;</a></p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA, Office of Radon Professionals (4 CCR 754-1). <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
    <li id="src-2">NRPP <a href="{s('nrpp')}" rel="noopener" target="_blank">nrpp.info</a> · NRSB <a href="{s('nrsb')}" rel="noopener" target="_blank">nrsb.org</a></li>
    <li id="src-3">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-4">Colorado DORA complaints. <a href="{s('dora_complaints')}" rel="noopener" target="_blank">dpo.colorado.gov/Filing-Complaint</a></li>
  </ol>
</aside>
"""


def contractors_hub_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How do I choose a radon mitigation contractor in Colorado?",
             "acceptedAnswer": {"@type": "Answer", "text": "Verify two credentials: a current DORA radon mitigation license (required by Colorado law since July 1, 2022, verifiable through the public license lookup) and NRPP or NRSB certification (national professional credential). Then check BBB profile, online reviews, references, liability insurance, and workers' comp. Get at least two written quotes, compare scope (not just price), and watch for red flags like cash-only payment, no DORA license, or pressure tactics."}},
            {"@type": "Question", "name": "What are the must-have credentials for a Colorado radon contractor?",
             "acceptedAnswer": {"@type": "Answer", "text": "DORA radon mitigation license (Colorado state requirement since 2022, codified at 4 CCR 754-1) plus either NRPP or NRSB national certification. Both numbers are publicly verifiable in 30 seconds. A contractor missing either credential should not be hired. Other professional indicators: 5+ years in business, BBB profile, liability insurance, and workers' comp."}},
            {"@type": "Question", "name": "How many radon mitigation quotes should I get?",
             "acceptedAnswer": {"@type": "Answer", "text": "Two minimum for any Colorado install. Three for complex situations: crawlspace mitigation, multi-zone foundations (tri-level, split-level), finished basements with aesthetic concerns, or any quote that seems outside the four-scenario framework price band."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 2. /radon-contractors/verify-licenses-and-certifications/
# =========================================================================
VERIFY_LICENSES_BODY = f"""
<section>
  <div class="prose-wide">
    <p>This is the part of the process most homeowners skip. It takes about 30 seconds per contractor and protects you from hiring someone who is either unlicensed, has had their license suspended, or has open complaints. This page walks through every step.</p>
  </div>
</section>

<section>
  <h2>Step 1 — Get the contractor's full credentials</h2>
  <div class="prose-wide">
    <p>Before you can verify anything, you need three pieces of information from each contractor you're considering:</p>
    <ul>
      <li><strong>Full legal business name.</strong> Not just the marketing name.</li>
      <li><strong>DORA radon mitigation license number.</strong> Should be on the quote, on the business card, or available on request.</li>
      <li><strong>NRPP or NRSB certification number.</strong> Same — should be readily available.</li>
    </ul>
    <p>If a contractor hesitates or won't provide these on request, that's a red flag in itself. Reputable Colorado mitigators put both numbers on every quote.</p>
  </div>
</section>

<section>
  <h2>Step 2 — Verify the DORA license</h2>
  <div class="prose-wide">
    <p>Colorado DORA maintains a public license lookup. The process:</p>
    <ol>
      <li>Go to <a href="{s('dora_lookup')}" rel="noopener" target="_blank">apps.colorado.gov/dora/licensing/Lookup/LicenseLookup.aspx</a>.</li>
      <li>In the search form, select the profession type. Radon mitigation is under "Office of Radon Professionals" — you may need to scroll or search for "radon."</li>
      <li>Enter the contractor's business name or license number.</li>
      <li>Click search.</li>
    </ol>
    <p>The result page will show:</p>
    <ul>
      <li><strong>License status.</strong> Should be "Active." Inactive, expired, suspended, or revoked means do not hire.</li>
      <li><strong>License number.</strong> Should match what the contractor provided.</li>
      <li><strong>Issue and expiration dates.</strong> Active licenses are renewed periodically; expired licenses without renewal are a red flag.</li>
      <li><strong>Any disciplinary actions.</strong> Public record. Open or recent actions warrant a follow-up question or a different contractor.</li>
    </ul>
    <p>If the DORA lookup shows no record of the license number the contractor gave you, walk away. They're either lying about the license or made a typo — either way, you can't verify what doesn't exist.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>Step 3 — Verify the NRPP or NRSB certification</h2>
  <div class="prose-wide">
    <p>NRPP and NRSB are separate national programs with separate lookups. Most Colorado contractors are certified through one or the other; some have both.</p>

    <h3>NRPP search</h3>
    <ol>
      <li>Go to <a href="{s('nrpp_search')}" rel="noopener" target="_blank">nrpp.info/pro-search</a>.</li>
      <li>Search by name, ZIP code, or certification number.</li>
      <li>Verify the certification type matches what's needed. For mitigation, look for RMP (Radon Mitigation Provider) or RMS (Radon Mitigation Specialist).</li>
      <li>Verify the certification is current — not expired, suspended, or revoked.</li>
    </ol>

    <h3>NRSB search</h3>
    <ol>
      <li>Go to <a href="{s('nrsb_search')}" rel="noopener" target="_blank">nrsb.org/for-professional</a>.</li>
      <li>Search by name, location, or certification number.</li>
      <li>For mitigation, look for RRS (Residential Radon Mitigation Specialist) or RMS.</li>
      <li>Verify currency.</li>
    </ol>

    <p>If a contractor claims an NRPP or NRSB certification that doesn't show up in the public directory, that's the same kind of red flag as a missing DORA license. The certifications exist precisely so homeowners can verify them.<sup><a href="#src-2">[2]</a></sup></p>
  </div>
</section>

<section>
  <h2>Step 4 — Check the BBB profile</h2>
  <div class="prose-wide">
    <p>BBB isn't a licensing body, but it's a useful aggregator:</p>
    <ol>
      <li>Go to <a href="{s('bbb_colorado')}" rel="noopener" target="_blank">bbb.org</a> and search the contractor's name.</li>
      <li>Look at the rating (A+ through F). Pay attention to the explanation, not just the letter.</li>
      <li>Read the complaint summaries. Pattern matters: one or two complaints in a long history is normal; a series of similar complaints (poor workmanship, no-shows, billing disputes) is a pattern.</li>
      <li>Read how the contractor responded to complaints. Quick, professional, and substantive responses are a positive signal; defensive, slow, or boilerplate ones are not.</li>
    </ol>
  </div>
</section>

<section>
  <h2>Step 5 — Verify liability insurance and workers' comp</h2>
  <div class="prose-wide">
    <p>Ask the contractor for proof of insurance. They should be able to provide a Certificate of Insurance (COI) showing:</p>
    <ul>
      <li><strong>General liability:</strong> $1M minimum is industry standard.</li>
      <li><strong>Workers' compensation:</strong> Required by Colorado law for employees.</li>
      <li><strong>Coverage dates:</strong> Make sure the policy is current and will cover the install date.</li>
    </ul>
    <p>The COI usually lists you (the homeowner) as a certificate holder or names your address as the work location. If the contractor declines to provide a COI, that's the same level of red flag as missing the DORA license.</p>
  </div>
</section>

<section>
  <h2>Step 6 — Check online reviews critically</h2>
  <div class="prose-wide">
    <p>Reviews on Google, Yelp, and Angi are valuable but selective. Tips for reading them well:</p>
    <ul>
      <li>Look at the contractor's <strong>response to negative reviews</strong>. Constructive, specific responses are positive signals.</li>
      <li>Search reviews for the words <strong>"warranty," "post-mitigation test," "still works," "5 years"</strong> — these surface long-term performance.</li>
      <li>Be skeptical of all-5-star ratings with no detail. Real customers leave detail.</li>
      <li>Cross-reference between platforms. A contractor with 5 stars on Google and 3.5 on Yelp may have a curated Google presence.</li>
    </ul>
  </div>
</section>

<section>
  <div class="callout">
    <strong>What to do when a credential is missing</strong>
    <p>If a contractor can't provide a DORA license number, don't continue. Colorado law has been clear since July 1, 2022 that mitigation work for hire requires DORA licensure. Anyone working without one is doing so illegally. They may still be doing competent work — but you have no recourse if they aren't, and any post-install warranty disputes won't have professional licensing backing them up.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA license lookup. <a href="{s('dora_lookup')}" rel="noopener" target="_blank">apps.colorado.gov/dora/licensing</a></li>
    <li id="src-2">NRPP / NRSB consumer search directories. <a href="{s('nrpp_search')}" rel="noopener" target="_blank">nrpp.info</a> · <a href="{s('nrsb_search')}" rel="noopener" target="_blank">nrsb.org</a></li>
  </ol>
</aside>
"""


def verify_licenses_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How do I verify a Colorado radon contractor's license?",
             "acceptedAnswer": {"@type": "Answer", "text": "Use the Colorado DORA public license lookup at apps.colorado.gov/dora/licensing. Search by contractor name or license number. Verify the license status is Active (not expired, suspended, or revoked), that the number matches what the contractor provided, and review any public disciplinary actions. The process takes about 30 seconds."}},
            {"@type": "Question", "name": "Where do I look up an NRPP or NRSB certification?",
             "acceptedAnswer": {"@type": "Answer", "text": "NRPP: search at nrpp.info/pro-search by name, ZIP, or certification number. Look for RMP (Radon Mitigation Provider) or RMS certifications. NRSB: search at nrsb.org/for-professional. Look for RRS (Residential Radon Mitigation Specialist). Verify the certification is current in both cases."}},
            {"@type": "Question", "name": "What if a contractor's license doesn't show up in the DORA lookup?",
             "acceptedAnswer": {"@type": "Answer", "text": "Walk away. Either they're working without the legally required license, or they gave you incorrect information. Either way, you can't verify what doesn't exist. Colorado has required DORA radon mitigation licensure since July 1, 2022 — anyone working without one is doing so illegally."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 3. /radon-contractors/questions-to-ask/
# =========================================================================
QUESTIONS_TO_ASK_BODY = f"""
<section>
  <div class="prose-wide">
    <p>The 30 minutes you spend asking the right questions before signing a radon mitigation contract is the cheapest insurance you'll buy on the install. This page is the question list, organized by stage of the hiring process.</p>
  </div>
</section>

<section>
  <h2>Phone screen (~10 minutes per contractor)</h2>
  <div class="prose-wide">
    <p>Before any in-home visit:</p>
    <ol>
      <li>"What's your DORA radon mitigation license number?"</li>
      <li>"What's your NRPP or NRSB certification number?"</li>
      <li>"How many years have you been doing mitigation in Colorado?"</li>
      <li>"Do you service [your ZIP code] / [Colorado Springs neighborhood]?"</li>
      <li>"What's your availability for an in-home assessment?"</li>
      <li>"Do you charge for the assessment?" (Reputable mitigators don't.)</li>
      <li>"Can you send me a sample written quote so I know what to expect?"</li>
    </ol>
    <p>If a contractor can't or won't answer the first two questions over the phone, you have your screening result. Move on.</p>
  </div>
</section>

<section>
  <h2>In-home assessment (~30–60 minutes)</h2>
  <div class="prose-wide">
    <p>During the walkthrough of your home:</p>

    <h3>About your test result</h3>
    <ul>
      <li>"Have you reviewed my test result? What level am I starting from?"</li>
      <li>"Does the test result tell you anything about the likely cause or pathway?"</li>
    </ul>

    <h3>About the foundation</h3>
    <ul>
      <li>"What foundation type does my home have?" (Basement, crawlspace, slab, multi-zone — confirm they noticed every zone.)</li>
      <li>"Is there a sump pit or sump pump?"</li>
      <li>"Are there any obvious slab cracks, sealing issues, or foundation concerns I should know about?"</li>
    </ul>

    <h3>About the proposed system design</h3>
    <ul>
      <li>"Will you run a pressure field extension (PFE) diagnostic before designing the system?" (Critical for multi-zone or tight-soil homes.)</li>
      <li>"How many suction points are you proposing? Why?"</li>
      <li>"Which fan model are you specifying? Why that model?"</li>
      <li>"How are you accounting for Colorado's altitude in fan sizing?" (Real contractors will have a specific answer involving 4% per 1,000 ft.)</li>
      <li>"Where will the pipe route — interior or exterior? Why?"</li>
      <li>"Where will the exhaust point be? Is that at least 10 feet above grade and 12 inches above the roof edge?" (Per AARST/EPA standards.)</li>
      <li>"Where will the manometer go? Will I be able to see it from a normal walking path?"</li>
    </ul>
  </div>
</section>

<section>
  <h2>Quote-stage questions</h2>
  <div class="prose-wide">
    <p>Once you have the written quote in hand:</p>
    <ul>
      <li>"Is the post-mitigation test included in the quoted price, or is it a separate line item?"</li>
      <li>"What's the target radon level for the post-mitigation test?" (Should be below 4.0 pCi/L; below 2.0 is ideal.)</li>
      <li>"What happens if the post-mitigation test doesn't bring levels below 4.0 pCi/L? Do you add another suction point at no charge?"</li>
      <li>"Is the electrical permit included? Who pulls it?" (Should be the contractor.)</li>
      <li>"Is drywall touch-up or paint match included if interior routing crosses a finished wall?"</li>
      <li>"What's your workmanship warranty? How long? In writing?"</li>
      <li>"What's the fan warranty? Manufacturer terms?"</li>
      <li>"How long will the install take? Will I need to be home?"</li>
    </ul>
  </div>
</section>

<section>
  <h2>Reference questions (call at least one)</h2>
  <div class="prose-wide">
    <p>When you call the contractor's references:</p>
    <ul>
      <li>"When was your install? What was the result before and after?"</li>
      <li>"Was the install timeline what they promised?"</li>
      <li>"Has the manometer reading stayed stable since installation?"</li>
      <li>"Has the system needed any service calls?"</li>
      <li>"How did the contractor handle any issues that came up?"</li>
      <li>"Did the post-mitigation test come back as promised?"</li>
      <li>"Would you hire them again?"</li>
    </ul>
    <p>References are typically curated by the contractor, so even cherry-picked references will give you signal — particularly on timeline reliability, communication, and post-install behavior.</p>
  </div>
</section>

<section>
  <h2>Pre-install logistics</h2>
  <div class="prose-wide">
    <ul>
      <li>"What time does the crew arrive? How long will the install take?"</li>
      <li>"Do you need access to the basement, attic, and exterior wall?"</li>
      <li>"Will there be drilling / coring dust I need to clean up after?"</li>
      <li>"What kind of fan noise should I expect inside the house?"</li>
      <li>"How soon after install can I run the post-mitigation test?" (Should be 24+ hours of fan running.)</li>
      <li>"Who do I call if something goes wrong with the system after install?"</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
    <li id="src-2">Colorado DORA, Office of Radon Professionals. <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
  </ol>
</aside>
"""


def questions_to_ask_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What should I ask before hiring a radon contractor?",
             "acceptedAnswer": {"@type": "Answer", "text": "Phone screen: DORA license number, NRPP/NRSB certification, years in business, service area. In-home assessment: questions about foundation type, sump pit, slab cracks. System design questions: PFE diagnostic plan, suction point count, fan model and altitude correction, pipe routing, exhaust point compliance, manometer placement. Quote stage: post-mit test included? Target level? Warranty terms? Drywall touch-up? Permit responsibility?"}},
            {"@type": "Question", "name": "Should I call the contractor's references?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes, at least one. Ask about install timeline reliability, whether the post-mitigation test result came back as promised, manometer stability over time, service call history, how the contractor handled any issues, and whether they'd hire again. Even curated references provide signal on timeline, communication, and post-install behavior."}},
            {"@type": "Question", "name": "What questions should I ask about Colorado altitude and my radon system?",
             "acceptedAnswer": {"@type": "Answer", "text": "Ask: 'How are you accounting for Colorado's altitude in fan sizing?' A real Colorado contractor will explain the 4% per 1,000 feet airflow loss and how it affects their fan model choice. A contractor who says 'altitude doesn't matter' or doesn't have a specific answer may be using national specs that under-fan Colorado homes."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 4. /radon-contractors/red-flags-in-a-quote/
# =========================================================================
RED_FLAGS_BODY = f"""
<section>
  <div class="prose-wide">
    <p>A bad radon mitigation quote isn't always obviously bad. Sometimes it looks professional, the price is reasonable, the contractor is friendly — and the quote is still missing the things that would prove the system is going to work. This page is the field guide to what to walk away from.</p>
  </div>
</section>

<section>
  <h2>The "absolute walk-away" red flags</h2>
  <div class="prose-wide">
    <p>If any one of these is true, do not sign the quote. Period.</p>
    <ul>
      <li><strong>No DORA radon mitigation license number on the quote.</strong> Colorado has required this since July 1, 2022. No exceptions.<sup><a href="#src-1">[1]</a></sup></li>
      <li><strong>No NRPP or NRSB certification number.</strong> National professional credential. Required per CDPHE guidance.</li>
      <li><strong>Cash-only payment.</strong> Reputable contractors accept check or card.</li>
      <li><strong>No written quote.</strong> Verbal promises don't bind anyone.</li>
      <li><strong>Refuses to provide proof of liability insurance or workers' comp.</strong> Means you bear the legal risk.</li>
      <li><strong>Won't provide references.</strong> Or "I'd love to but my customers value their privacy" with no other options offered.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The "ask before signing" red flags</h2>
  <div class="prose-wide">
    <p>These should prompt clarifying questions. If the answers are good, you can proceed. If the answers are vague or evasive, walk away.</p>

    <h3>Sales-tactic red flags</h3>
    <ul>
      <li><strong>"This price is only good today."</strong> Mitigation isn't a same-day-only purchase. Anything legitimate can wait two days.</li>
      <li><strong>Fear-based language.</strong> "Your family is in danger" or "if you don't act now" is pressure, not education.</li>
      <li><strong>Aggressive door-to-door sales.</strong> Some legitimate contractors do canvass, but cold-call door-to-door radon sales after a high test is suspicious.</li>
      <li><strong>"Special pricing if you sign today."</strong> Same family as the urgency tactic.</li>
    </ul>

    <h3>Scope red flags</h3>
    <ul>
      <li><strong>Single suction point on a multi-zone home (tri-level, split-level, basement + crawlspace).</strong> Should have at least two. Ask why.</li>
      <li><strong>No fan model specified.</strong> "An inline fan" isn't a fan model. Should be a specific RP145, GP500, HS-series, etc.</li>
      <li><strong>"We always use the standard fan."</strong> Colorado altitude affects fan sizing. A one-size-fits-all answer is a contractor who isn't designing for your home.</li>
      <li><strong>Pipe routing not described.</strong> Should say interior or exterior, and where it exits.</li>
      <li><strong>No discussion of sealing.</strong> Sealing scope (slab cracks, sump cover, floor-wall joint, penetrations) should be itemized.</li>
      <li><strong>6-mil vapor barrier for a crawlspace.</strong> Old standard. Current industry favors 10–20 mil. Ask why if 6 mil is proposed for a permanent system.</li>
      <li><strong>Post-mitigation test not included.</strong> Or listed as "additional cost" without a price. Ask. Some contractors charge $125–$200 separately, which is fine if disclosed.</li>
    </ul>

    <h3>Warranty red flags</h3>
    <ul>
      <li><strong>Workmanship warranty under 1 year.</strong> Industry standard is 1–2 years minimum.</li>
      <li><strong>No fan warranty mentioned.</strong> Should be 5 years from a name-brand manufacturer.</li>
      <li><strong>No performance warranty.</strong> No commitment that the system will bring radon below 4.0 pCi/L.</li>
      <li><strong>Warranty language that voids itself for normal usage.</strong> "Warranty void if homeowner opens basement windows" or similar.</li>
    </ul>

    <h3>Pricing red flags</h3>
    <ul>
      <li><strong>Suspiciously low for your scenario.</strong> $700 for a crawlspace, $1,200 for multi-zone tri-level. Something's not in the scope.</li>
      <li><strong>Suspiciously high for your scenario.</strong> $4,500 for a basic single-suction basement install. Ask what's driving it.</li>
      <li><strong>"Required upgrades" the contractor can't explain.</strong> Especially if they appear as line items without technical justification.</li>
      <li><strong>Large deposit (>50%).</strong> Industry standard is 25–50% deposit. Anything more is unusual.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The "ask but probably fine" yellow flags</h2>
  <div class="prose-wide">
    <p>These warrant a question but aren't necessarily disqualifying:</p>
    <ul>
      <li><strong>Contractor is brand new (less than 2 years).</strong> Some are excellent; some are problematic. Ask for references from comparable jobs.</li>
      <li><strong>BBB rating under A-.</strong> Look at the complaint pattern and the contractor's response.</li>
      <li><strong>Mixed online reviews.</strong> Read negative reviews carefully and look at the contractor's response.</li>
      <li><strong>Very high pricing in an expensive scenario.</strong> A $4,500 quote for a complex crawlspace + multi-zone home may be entirely fair.</li>
      <li><strong>Exterior-only routing proposed.</strong> Some homeowners prefer interior; both are AARST-compliant. Ask if interior is an option and what it costs.</li>
    </ul>
  </div>
</section>

<section>
  <h2>What to do when you spot a red flag</h2>
  <div class="prose-wide">
    <ol>
      <li><strong>Ask directly.</strong> A good contractor explains. A bad one gets defensive or vague.</li>
      <li><strong>Compare against another quote.</strong> If the second contractor's quote includes what the first one's was missing, you have your answer.</li>
      <li><strong>Document the conversation.</strong> Especially if a contractor says one thing verbally but their written quote says another.</li>
      <li><strong>Walk away if you need to.</strong> There are plenty of DORA-licensed mitigators in Colorado. You're not stuck with the first bid.</li>
    </ol>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA, Office of Radon Professionals (4 CCR 754-1). <a href="{s('dora_radon')}" rel="noopener" target="_blank">dpo.colorado.gov/RadonProfessionals</a></li>
    <li id="src-2">ANSI/AARST SGM-SF-2023 Soil Gas Mitigation Standards. <a href="{s('aarst_standards')}" rel="noopener" target="_blank">standards.aarst.org</a></li>
  </ol>
</aside>
"""


def red_flags_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What are red flags in a radon mitigation quote?",
             "acceptedAnswer": {"@type": "Answer", "text": "Absolute walk-away red flags: no DORA license, no NRPP/NRSB certification, cash-only payment, no written quote, no proof of insurance, won't provide references. Ask-before-signing red flags: high-pressure sales tactics ('only good today'), single suction point on multi-zone homes, no fan model specified, no discussion of sealing scope, missing post-mitigation test, workmanship warranty under 1 year, suspiciously low or high pricing for the scenario."}},
            {"@type": "Question", "name": "Should I trust a same-day pricing offer?",
             "acceptedAnswer": {"@type": "Answer", "text": "No. Legitimate mitigation isn't a same-day purchase. 'This price is only good today' is a high-pressure tactic, not a reflection of the work. Any legitimate quote can wait 48 hours for you to compare against another bid."}},
            {"@type": "Question", "name": "What deposit is normal for a Colorado radon install?",
             "acceptedAnswer": {"@type": "Answer", "text": "25-50% deposit is industry standard. A contractor asking for more than 50% upfront is unusual and worth questioning. Some Colorado contractors take no deposit, billing 100% at install completion."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 5. /radon-contractors/warranties-and-retesting/
# =========================================================================
WARRANTIES_BODY = f"""
<section>
  <div class="prose-wide">
    <p>A radon mitigation install isn't really finished when the contractor leaves. It's finished when the post-mitigation test comes back below 4.0 pCi/L, when you've got the system documentation in your file, and when the warranty terms are written down and clear. This page covers what to expect on all three.</p>
  </div>
</section>

<section>
  <h2>The three warranties involved</h2>
  <div class="prose-wide">
    <p>A complete Colorado mitigation install typically has three separate warranties — they overlap in time but cover different things.</p>

    <h3>Workmanship warranty (from the contractor)</h3>
    <p>Covers the install itself — the piping, sealing, fan mounting, manometer installation, electrical work.</p>
    <ul>
      <li><strong>Industry standard:</strong> 1–2 years on labor.</li>
      <li><strong>Premium installs:</strong> Some Colorado contractors offer 5 years.</li>
      <li><strong>What's covered:</strong> Pipe leaks, fan housing issues, sealing failures, manometer mounting problems, electrical issues caused by the install.</li>
      <li><strong>What's not:</strong> Normal fan wear after warranty period, damage from causes unrelated to the install, owner modifications.</li>
    </ul>

    <h3>Fan manufacturer warranty</h3>
    <p>Covers the fan itself — typically 5 years from RadonAway, Fantech, or Festa AMG.<sup><a href="#src-1">[1]</a></sup></p>
    <ul>
      <li><strong>What's covered:</strong> Motor failure, bearing failure, manufacturing defects.</li>
      <li><strong>What's not:</strong> Storm damage, ice damage, electrical surges, owner damage.</li>
      <li><strong>How to claim:</strong> Usually through the original installer. Keep the fan model and serial number in your files.</li>
    </ul>

    <h3>Performance warranty (optional but ideal)</h3>
    <p>A guarantee that the system will reduce indoor radon below 4.0 pCi/L on the post-mitigation test.</p>
    <ul>
      <li><strong>Industry standard:</strong> Most reputable Colorado contractors offer this in writing.</li>
      <li><strong>What's covered:</strong> If the post-mit test doesn't bring levels below 4.0 pCi/L, the contractor adds an additional suction point, upgrades the fan, or takes other corrective action at no extra cost.</li>
      <li><strong>Limit:</strong> Usually 1 year post-install. Get this in writing on the quote.</li>
    </ul>
  </div>
</section>

<section>
  <h2>The post-mitigation test</h2>
  <div class="prose-wide">
    <p>Per EPA recommendation:<sup><a href="#src-2">[2]</a></sup></p>
    <ul>
      <li><strong>Within 30 days</strong> of system activation.</li>
      <li><strong>No sooner than 24 hours</strong> after the fan starts running.</li>
      <li><strong>2 to 7 days</strong> of test duration.</li>
      <li><strong>Closed-house conditions</strong> for 12 hours before and during.</li>
      <li><strong>Lowest livable level,</strong> 2–6 feet above the floor, away from drafts and humidity.</li>
    </ul>
    <p>EPA also recommends having the post-mit test done by an <strong>independent (non-installer) tester</strong> to avoid any conflict of interest. Some Colorado contractors include this in the quote; others charge $125–$200 for a separate test by a third party.</p>
    <p>A working Colorado mitigation system should bring radon to <strong>under 2.0 pCi/L</strong> in most homes, often under 1.0. If the post-mit test reads above 4.0, the contractor should add another suction point or upgrade the fan under the performance warranty.</p>
  </div>
</section>

<section>
  <h2>Retest cadence — every 2 years</h2>
  <div class="prose-wide">
    <p>EPA recommends retesting your home <strong>every 2 years</strong>, even after mitigation. Three reasons:<sup><a href="#src-2">[2]</a></sup></p>
    <ul>
      <li>Soil-gas conditions change over time (settling, water table shifts, foundation aging).</li>
      <li>Fans degrade slowly. A fan that's bringing levels to 1.5 pCi/L now might be at 3.5 pCi/L in five years.</li>
      <li>Climate and seasonal patterns affect levels. A long-term retest averages across the year.</li>
    </ul>
    <p>Beyond the 2-year cadence, retest:</p>
    <ul>
      <li>After major remodels that affect the foundation, basement, or HVAC.</li>
      <li>After adding new living space (finished basement, additions).</li>
      <li>If you notice manometer behavior changing.</li>
      <li>Before listing the home for sale (Colorado SB23-206 disclosure).</li>
    </ul>
  </div>
</section>

<section>
  <h2>What to document and keep</h2>
  <div class="prose-wide">
    <p>Keep this in a single folder with your home records. It becomes part of your required SB23-206 disclosure when you sell:</p>
    <ul class="checklist">
      <li>Original radon test result (the one that triggered the install)</li>
      <li>Contractor's written quote and final invoice</li>
      <li>System certification from the contractor</li>
      <li>DORA license number, NRPP or NRSB certification number, contractor business info</li>
      <li>Fan model number and manufacturer warranty card</li>
      <li>Post-mitigation test result certificate</li>
      <li>Manometer baseline reading (the reading right after activation)</li>
      <li>All subsequent retest results</li>
      <li>Any service calls or fan replacements</li>
    </ul>
  </div>
</section>

<section>
  <h2>Manometer maintenance — a 30-second monthly check</h2>
  <div class="prose-wide">
    <p>Once a month, glance at the manometer when you're in the basement for any reason. You're checking for:</p>
    <ul>
      <li>The two fluid columns are at different levels (typically 0.5 to 2.0 inches of water column offset).</li>
      <li>The reading is reasonably close to what the contractor documented at activation.</li>
      <li>The fluid is still in the tube (occasional refilling may be needed; manometers don't usually leak in normal use).</li>
    </ul>
    <p>What to do if the reading changes:</p>
    <ul>
      <li><strong>Columns at the same level:</strong> Fan isn't running. Check the circuit breaker; call the installer if it's not a power issue.</li>
      <li><strong>Reading much lower than usual:</strong> System is losing efficiency. Fan may be failing. Service call.</li>
      <li><strong>Reading much higher than usual:</strong> Soil conditions changed (heavy rain, water table shift). Worth noting but rarely urgent.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Fan replacement — every 5–10 years</h2>
  <div class="prose-wide">
    <p>The fan is the only routine maintenance item on a radon system. Most manufacturers warranty for 5 years; many fans run 7–10 years before replacement.</p>
    <p>Signs of imminent fan failure:</p>
    <ul>
      <li>Audible humming, rattling, or grinding from the fan housing.</li>
      <li>Manometer reading dropping over time.</li>
      <li>A retest showing radon levels rising.</li>
      <li>Visible vibration of the fan.</li>
    </ul>
    <p>Replacement cost: $150–$400 for the fan, plus 1–2 hours of labor. Most Colorado mitigators handle replacement as a service call rather than a full new install. If the original installer is unavailable (out of business, retired), any DORA-licensed contractor can do the replacement.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Fan manufacturer warranties (RadonAway, Fantech, Festa AMG typical 5-year warranty). <a href="{s('radonaway_specs')}" rel="noopener" target="_blank">radonaway.com</a></li>
    <li id="src-2">U.S. EPA. <em>Consumer's Guide to Radon Reduction</em>. <a href="{s('epa_consumer_guide')}" rel="noopener" target="_blank">epa.gov/radon/consumers-guide-radon-reduction</a></li>
  </ol>
</aside>
"""


def warranties_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What warranty should I expect on Colorado radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Three warranties typically apply: workmanship warranty from the contractor (1-2 years industry standard, 5 years on premium installs), fan manufacturer warranty (5 years from RadonAway/Fantech/Festa), and a performance warranty (most reputable contractors guarantee the system will reduce radon below 4.0 pCi/L on the post-mitigation test, with corrective action at no extra cost if not)."}},
            {"@type": "Question", "name": "How often should I retest after radon mitigation?",
             "acceptedAnswer": {"@type": "Answer", "text": "Every 2 years per EPA recommendation. Also retest after major remodels affecting the foundation or HVAC, after adding new living space, if the manometer behaves differently, or before listing the home for sale (Colorado SB23-206 disclosure)."}},
            {"@type": "Question", "name": "How long does a radon fan last?",
             "acceptedAnswer": {"@type": "Answer", "text": "Most manufacturer warranties are 5 years; many radon fans run 7-10 years before needing replacement. Signs of imminent failure: audible humming or rattling, dropping manometer readings, visible vibration, or retest results showing rising radon levels. Replacement cost: $150-$400 in parts plus 1-2 hours of labor."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'


# =========================================================================
# 6. /radon-contractors/how-to-file-a-complaint/
# =========================================================================
COMPLAINT_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Most Colorado radon mitigation work goes well. Some doesn't. If your contractor disappeared after taking your deposit, if the install didn't bring radon below the action level and they won't fix it, if the fan failed within warranty and they won't honor it — Colorado has formal recourse paths. This page walks through them.</p>
    <p>This is general information, not legal advice. For serious disputes, consult a Colorado consumer protection or contracts attorney.</p>
  </div>
</section>

<section>
  <h2>Step 1 — Document the dispute in writing first</h2>
  <div class="prose-wide">
    <p>Before any complaint, send the contractor a written communication (email is fine and easier to document) that includes:</p>
    <ul>
      <li>What you contracted for (reference the original quote).</li>
      <li>What was delivered (or not delivered).</li>
      <li>What outcome you expect (re-install, refund, fan replacement, etc.).</li>
      <li>A reasonable deadline for response (typically 14 days).</li>
    </ul>
    <p>Most legitimate disputes resolve at this step. A contractor who wants to keep their license isn't going to ignore a written demand they know is about to escalate.</p>
  </div>
</section>

<section>
  <h2>Step 2 — File a DORA complaint (most powerful)</h2>
  <div class="prose-wide">
    <p>Colorado DORA's Office of Radon Professionals can investigate complaints, suspend licenses, and impose fines. This is the most direct consumer recourse for problems with a licensed Colorado mitigator.</p>
    <ol>
      <li>Go to <a href="{s('dora_complaints')}" rel="noopener" target="_blank">dpo.colorado.gov/Filing-Complaint</a>.</li>
      <li>Select the appropriate profession (Radon Mitigation Professional).</li>
      <li>Provide the contractor's name, license number, and a detailed account of the dispute.</li>
      <li>Attach supporting documentation: the contract, written communications, the test results, photos of the install.</li>
    </ol>
    <p>DORA investigates and can take action ranging from a formal warning to license suspension or revocation. The process is slower than civil court but cheaper, and a DORA finding becomes part of the public record other consumers can see.<sup><a href="#src-1">[1]</a></sup></p>
  </div>
</section>

<section>
  <h2>Step 3 — File a BBB complaint</h2>
  <div class="prose-wide">
    <p>BBB doesn't have enforcement authority, but it's effective for:</p>
    <ul>
      <li>Pushing the contractor to respond (most do, to maintain their BBB rating).</li>
      <li>Documenting the dispute publicly.</li>
      <li>Warning future consumers.</li>
    </ul>
    <p>File at <a href="{s('bbb_colorado')}" rel="noopener" target="_blank">bbb.org</a>. The process takes a few minutes; BBB typically forwards the complaint to the contractor within a few days and gives them 30 days to respond.</p>
  </div>
</section>

<section>
  <h2>Step 4 — Colorado Attorney General Consumer Complaint</h2>
  <div class="prose-wide">
    <p>The Colorado Attorney General's office investigates patterns of consumer fraud and unfair business practices. Individual complaints don't always result in direct action, but they:</p>
    <ul>
      <li>Build the AG's case if the contractor has multiple complaints.</li>
      <li>Trigger investigation if the conduct is egregious.</li>
      <li>Can lead to civil enforcement actions, including restitution.</li>
    </ul>
    <p>File at <a href="{s('co_attorney_general')}" rel="noopener" target="_blank">coag.gov</a>. Particularly useful for cases involving fraud, identity theft, or systematic consumer harm.</p>
  </div>
</section>

<section>
  <h2>Step 5 — Civil action (small claims or higher)</h2>
  <div class="prose-wide">
    <p>If you've suffered financial harm and the contractor won't make you whole, you may have grounds for civil action:</p>
    <ul>
      <li><strong>Small claims court</strong> in Colorado handles disputes up to $7,500. Filing fees are modest ($31–$80 depending on amount). No attorney is required (and not usually allowed).</li>
      <li><strong>County court</strong> handles disputes from $7,500 to $25,000. Attorney typically helpful.</li>
      <li><strong>District court</strong> handles larger disputes. Attorney essentially required.</li>
    </ul>
    <p>Before filing, send a final written demand. Many contractors will settle to avoid court even if they were stonewalling on the BBB or DORA tracks.</p>
  </div>
</section>

<section>
  <h2>When to consult an attorney</h2>
  <div class="prose-wide">
    <p>Consult a Colorado consumer protection or contracts attorney when:</p>
    <ul>
      <li>The financial harm exceeds $7,500 (above small claims limit).</li>
      <li>The contractor is making counterclaims or threatening legal action against you.</li>
      <li>The dispute involves alleged fraud, identity theft, or pattern of misconduct.</li>
      <li>You discover after closing on a home that the radon mitigation was misrepresented in the SB23-206 disclosure.</li>
      <li>The contractor is unresponsive to all of the above channels.</li>
    </ul>
    <p>Many Colorado attorneys offer a free initial consultation. The Colorado Bar Association maintains a referral service.</p>
  </div>
</section>

<section>
  <h2>What documentation to gather</h2>
  <div class="prose-wide">
    <p>For any of these paths, gather:</p>
    <ul class="checklist">
      <li>Original radon test result and any subsequent tests</li>
      <li>Written quote and any contract documents</li>
      <li>Final invoice and any payment records</li>
      <li>All written communications with the contractor (emails, texts, letters)</li>
      <li>System certification and post-mitigation test result (or absence thereof)</li>
      <li>Photos of the install — pipes, fan location, manometer, exhaust point, sealing</li>
      <li>References to specific complaints (e.g., AARST standard violations, missing scope items)</li>
      <li>Names and contact info for any witnesses (other tradespeople, real estate agents involved)</li>
    </ul>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">Colorado DORA complaint filing. <a href="{s('dora_complaints')}" rel="noopener" target="_blank">dpo.colorado.gov/Filing-Complaint</a></li>
    <li id="src-2">Colorado Attorney General consumer complaints. <a href="{s('co_attorney_general')}" rel="noopener" target="_blank">coag.gov</a></li>
    <li id="src-3">BBB Colorado. <a href="{s('bbb_colorado')}" rel="noopener" target="_blank">bbb.org</a></li>
  </ol>
</aside>

<p style="font-size:.85rem;color:var(--text-muted);">This page is general information, not legal advice. For serious disputes, consult a Colorado consumer protection or contracts attorney.</p>
"""


def complaint_faq_jsonld():
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "How do I file a complaint against a Colorado radon contractor?",
             "acceptedAnswer": {"@type": "Answer", "text": "Start with a written demand to the contractor (most disputes resolve at this step). If unresolved, file a DORA complaint at dpo.colorado.gov/Filing-Complaint (Office of Radon Professionals investigates licensed mitigators and can suspend or revoke licenses). Also file a BBB complaint at bbb.org and a Colorado Attorney General consumer complaint at coag.gov for pattern documentation."}},
            {"@type": "Question", "name": "Can I sue a Colorado radon contractor in small claims court?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes, for disputes up to $7,500. Filing fees are modest ($31-$80). No attorney is required (and not usually allowed) in Colorado small claims court. For disputes between $7,500 and $25,000, county court is the venue. Larger disputes go to district court."}},
            {"@type": "Question", "name": "What documentation do I need to file a radon contractor complaint?",
             "acceptedAnswer": {"@type": "Answer", "text": "Original test result, written quote and contract, final invoice, all written communications with the contractor, system certification (or evidence it wasn't provided), post-mitigation test result, photos of the install (pipes, fan, manometer, exhaust point, sealing), and any AARST or licensing violations you can document specifically."}}
        ]
    }
    return f'<script type="application/ld+json">{json.dumps(obj)}</script>'
