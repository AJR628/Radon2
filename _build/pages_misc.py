"""Quote form, thank-you, about, disclosure, privacy, contact pages."""
from pages_main import s, SOURCES


# =========================================================================
# QUOTE REQUEST FORM
# =========================================================================
QUOTE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Tell us a little about your home and your radon situation, and we'll route your information to our licensed Colorado mitigation partner who serves your area. The quote is free. There's no obligation, no high-pressure sales call, and we don't sell your information to multiple contractors.</p>
  </div>
  <div class="trust-strip">
    <span class="item"><strong>Free quote</strong> · no obligation</span>
    <span class="item"><strong>One partner only</strong> · we don't shop your info</span>
    <span class="item"><strong>DORA-registered</strong> · NRPP/NRSB-certified</span>
    <span class="item"><strong>Written quote</strong> · scope, fan, warranty, retest</span>
  </div>
  <div class="prose-wide">
    <p>Need cost context first? Read the <a href="/radon-mitigation-cost/">statewide cost page</a>, the <a href="/colorado-springs/radon-mitigation-cost/">Colorado Springs cost guide</a>, or the <a href="/denver/">Denver hub</a> before submitting.</p>
  </div>
</section>

<section>
  <form class="form" name="quote-request" method="POST" data-netlify="true" data-netlify-honeypot="bot-field" action="/request-quote/thank-you/" novalidate>
    <!-- Netlify Forms — captured automatically on deploy. Form appears in the Netlify dashboard under Forms → "quote-request". -->
    <input type="hidden" name="form-name" value="quote-request">

    <!-- Honeypot field. Hidden from real users; bots that auto-fill every field will trip it and be silently rejected. -->
    <p class="netlify-honeypot" aria-hidden="true" style="position:absolute;left:-9999px;height:0;overflow:hidden;">
      <label>Don't fill this out if you're human: <input name="bot-field" tabindex="-1" autocomplete="off"></label>
    </p>

    <!-- Source page tracking (visible only to the back-end). Service area is captured in the visible service_area field below. -->
    <input type="hidden" name="source_page" value="/request-quote/">

    <div class="field-row">
      <div class="field">
        <label for="name">Full name <span class="required">*</span></label>
        <input id="name" name="name" type="text" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="phone">Phone <span class="required">*</span></label>
        <input id="phone" name="phone" type="tel" autocomplete="tel" required>
      </div>
    </div>

    <div class="field-row">
      <div class="field">
        <label for="email">Email <span class="required">*</span></label>
        <input id="email" name="email" type="email" autocomplete="email" required>
      </div>
      <div class="field">
        <label for="zip">ZIP code <span class="required">*</span></label>
        <input id="zip" name="zip" type="text" inputmode="numeric" pattern="[0-9]{{5}}" autocomplete="postal-code" required>
        <div class="hint">Five-digit Colorado ZIP code. We route by ZIP, not city.</div>
      </div>
    </div>

    <div class="field">
      <label for="service-area">Where is the property located? <span class="required">*</span></label>
      <select id="service-area" name="service_area" required>
        <option value="">Select an area…</option>
        <option value="colorado-springs">Colorado Springs / El Paso County</option>
        <option value="denver-metro">Denver Metro</option>
        <option value="other-colorado">Other Colorado area</option>
      </select>
      <div class="hint">Helps us route your request to a contractor whose service area covers you.</div>
    </div>

    <div class="field">
      <label for="address">Property address</label>
      <input id="address" name="address" type="text" autocomplete="street-address">
      <div class="hint">Optional. Helps the contractor estimate access and travel.</div>
    </div>

    <div class="field-row">
      <div class="field">
        <label for="reason">Reason for inquiry <span class="required">*</span></label>
        <select id="reason" name="reason" required>
          <option value="">Select one…</option>
          <option value="test-came-back-high">My test came back high</option>
          <option value="real-estate-buyer">I'm a buyer in a real estate transaction</option>
          <option value="real-estate-seller">I'm a seller listing or under contract</option>
          <option value="never-tested">I haven't tested but want a quote</option>
          <option value="system-not-working">My existing system isn't working</option>
          <option value="testing">I need testing, not mitigation</option>
          <option value="other">Other</option>
        </select>
      </div>
      <div class="field">
        <label for="foundation">Foundation type</label>
        <select id="foundation" name="foundation">
          <option value="">Select if known…</option>
          <option value="slab">Slab on grade</option>
          <option value="basement-finished">Basement — finished</option>
          <option value="basement-unfinished">Basement — unfinished</option>
          <option value="crawl-space">Crawl space</option>
          <option value="mixed">Mixed / multi-foundation</option>
          <option value="unknown">Not sure</option>
        </select>
      </div>
    </div>

    <div class="field-row">
      <div class="field">
        <label for="result">Latest radon result (pCi/L)</label>
        <input id="result" name="result" type="text" inputmode="decimal" placeholder="e.g. 6.4">
        <div class="hint">If you've tested. Leave blank if not.</div>
      </div>
      <div class="field">
        <label for="sqft">Approx. square footage</label>
        <input id="sqft" name="sqft" type="text" inputmode="numeric" placeholder="e.g. 1800">
      </div>
    </div>

    <div class="field-row">
      <div class="field">
        <label for="is-transaction">Real estate transaction?</label>
        <select id="is-transaction" name="is_transaction">
          <option value="no">No</option>
          <option value="buying">Yes — buying</option>
          <option value="selling">Yes — selling</option>
        </select>
      </div>
      <div class="field">
        <label for="closing">Closing or inspection deadline</label>
        <input id="closing" name="closing_date" type="date">
        <div class="hint">Optional — helps us prioritize urgent timelines.</div>
      </div>
    </div>

    <div class="field">
      <label for="notes">Anything else we should know?</label>
      <textarea id="notes" name="notes" rows="4" placeholder="Sump pit, existing radon stub, finished basement, recent remodel, etc."></textarea>
    </div>

    <div class="field consent">
      <input id="consent" name="consent" type="checkbox" required>
      <label for="consent">I understand my information will be shared with a licensed Colorado radon mitigation partner so they can prepare a quote. <span class="required">*</span></label>
    </div>

    <button class="btn" type="submit">Request my quote</button>

    <p style="font-size:.85rem;color:var(--text-muted);margin-top:1.25rem;">
      We do not sell your information to multiple contractors. See our <a href="/privacy/">privacy policy</a> and <a href="/disclosure/">lead routing disclosure</a>.
    </p>
  </form>
</section>

<section>
  <h2>What happens after you submit</h2>
  <div class="prose-wide">
    <ol>
      <li>Your submission is routed to a licensed Colorado mitigation partner who serves Colorado Springs.</li>
      <li>The partner contacts you within one business day to confirm details and schedule a free quote.</li>
      <li>If your situation involves a closing deadline, we flag it as priority.</li>
      <li>You receive a written quote with scope, fan model, warranty, and post-installation test commitment.</li>
    </ol>
    <p>Before you sign anything, verify the contractor's NRPP or NRSB certification and Colorado DORA registration. We outline what to look for on the <a href="/colorado-springs/">Colorado Springs hub</a>.</p>
  </div>
</section>
"""


# =========================================================================
# QUOTE THANK YOU
# =========================================================================
QUOTE_THANKYOU_BODY = """
<section>
  <div class="prose-wide">
    <p>Your radon quote request has been received. A licensed Colorado mitigation partner who serves Colorado Springs will reach out within one business day.</p>
    <p>While you wait, two pieces of reading that'll save you money and time:</p>
    <ul>
      <li><a href="/colorado-springs/radon-mitigation-cost/">What radon mitigation actually costs in Colorado Springs</a> — and why two quotes can look very different.</li>
      <li><a href="/colorado-springs/failed-radon-test/">What to do after a failed radon test</a> — especially if you're on a closing timeline.</li>
    </ul>
    <p>If your situation has changed or you have additional details to share, <a href="/contact/">contact us</a>.</p>
  </div>
</section>
"""


# =========================================================================
# ABOUT
# =========================================================================
ABOUT_BODY = f"""
<section>
  <div class="prose-wide">
    <p>Colorado Radon Guide is an independent editorial resource for Colorado homeowners, buyers, and sellers navigating radon — what it is, why Colorado is exceptional, what testing costs, what mitigation costs, and how to find a qualified contractor.</p>
  </div>
</section>

<section>
  <h2>What we do</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Publish editorial guides</strong> drawn from public sources: CDPHE, the EPA, El Paso County Public Health, Denver Public Health, and the Colorado General Assembly.</li>
      <li><strong>Connect homeowners with a licensed Colorado mitigation partner</strong> when they request a quote. We are paid a referral fee when this happens — see our <a href="/disclosure/">editorial and lead disclosure</a>.</li>
      <li><strong>Make cost transparent</strong>. The single biggest complaint we see in Colorado homeowner forums is "is my quote too high?" We publish typical ranges from authoritative sources so the answer isn't "ask three contractors and hope."</li>
    </ul>
  </div>
</section>

<section>
  <h2>What we don't do</h2>
  <div class="prose-wide">
    <ul>
      <li>We are <strong>not a radon contractor</strong>. We do not install systems, perform testing, sell equipment, or hold any radon professional certifications.</li>
      <li>We do not publish <strong>fake reviews, fake testimonials, or paid placements</strong> as editorial.</li>
      <li>We do not provide <strong>medical or legal advice</strong>. We summarize public guidance and link to the originals. For your situation, consult a physician, attorney, or licensed contractor as appropriate.</li>
      <li>We do not <strong>sell your contact information</strong> to multiple buyers. Quote submissions go to one licensed partner per inquiry.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Why this site exists</h2>
  <div class="prose-wide">
    <p>Colorado has one of the highest indoor radon rates in the country, real laws around disclosure (<a href="{s('sb23_206')}" rel="noopener" target="_blank">SB23-206</a>), and active state regulation of radon professionals (<a href="{s('dora_radon')}" rel="noopener" target="_blank">DORA</a>). But the actual experience for a Colorado homeowner who fails a radon test is still confusing: contractors give very different quotes, the legal disclosure rules are easy to misread, and most published cost guides are written by contractors selling the service.</p>
    <p>We try to be the page you'd want a friend who happens to know radon to send you: clear, sourced, no scare tactics, and willing to tell you when DIY is fine and when it isn't.</p>
  </div>
</section>

<section>
  <h2>Our sources</h2>
  <div class="prose-wide">
    <p>Anything quantitative on this site — prevalence percentages, cost ranges, action levels, reduction percentages, legal requirements — links to its primary source. The recurring authorities we cite:</p>
    <ul>
      <li><a href="{s('cdphe_radon')}" rel="noopener" target="_blank">Colorado Department of Public Health and Environment — Radon</a></li>
      <li><a href="{s('epa_radon')}" rel="noopener" target="_blank">U.S. Environmental Protection Agency — Radon</a></li>
      <li><a href="{s('elpaso_radon')}" rel="noopener" target="_blank">El Paso County Public Health — Radon</a></li>
      <li><a href="{s('dora_radon')}" rel="noopener" target="_blank">Colorado DORA — Office of Radon Professionals</a></li>
      <li><a href="{s('sb23_206')}" rel="noopener" target="_blank">Colorado General Assembly — SB23-206</a></li>
    </ul>
    <p>If you find a claim on this site that isn't sourced or that you believe is wrong, <a href="/contact/">tell us</a> and we'll fix it or remove it.</p>
  </div>
</section>
"""


# =========================================================================
# DISCLOSURE
# =========================================================================
DISCLOSURE_BODY = f"""
<section>
  <div class="prose-wide">
    <p>This page explains how Colorado Radon Guide is funded, how leads are routed to a contractor partner, and the editorial separation between the two. Plain language and no surprises.</p>
  </div>
</section>

<section>
  <h2>Independence</h2>
  <div class="prose-wide">
    <p>Colorado Radon Guide is operated independently. We do not own, are not owned by, and are not editorially controlled by any radon contractor, equipment manufacturer, or insurance provider. The site's editorial content — what's on these pages, what we cite, what we recommend — is decided by us.</p>
  </div>
</section>

<section>
  <h2>How lead routing works</h2>
  <div class="prose-wide">
    <p>When you submit a quote request through this site, your contact information is forwarded to a licensed Colorado radon mitigation contractor who serves your area. That contractor then reaches out to you to schedule a free quote.</p>
    <p>Specifically:</p>
    <ul>
      <li>One submission goes to <strong>one</strong> partner per inquiry — not a list of three contractors who all call you.</li>
      <li>We track which city and which page the submission came from so the partner has context.</li>
      <li>We do not sell your information to data brokers, marketing lists, or unrelated services.</li>
      <li>You can opt out of further contact from the partner at any time.</li>
    </ul>
    <p>See the <a href="/privacy/">privacy policy</a> for the full data-handling details.</p>
  </div>
</section>

<section>
  <h2>Financial relationship</h2>
  <div class="prose-wide">
    <p>We are paid a referral fee by the partner when a quote request results in a customer who ultimately hires them. We are <strong>not</strong> paid for clicks, form starts, or quote requests that don't convert.</p>
    <p>That fee is paid by the contractor, not by you. The price you are quoted is the same as if you'd contacted the contractor directly. We do not mark up estimates, add fees, or take a cut of the install price.</p>
    <p>This referral fee is how we fund the site, including the editorial work that goes into the guides.</p>
  </div>
</section>

<section>
  <h2>Editorial separation from advertising</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Editorial content is not paid placement.</strong> Contractors do not pay us to be quoted, mentioned, or recommended in our guides.</li>
      <li><strong>Our cost ranges come from public sources</strong> — CDPHE, El Paso County Public Health, and the EPA — not from our partner's pricing.</li>
      <li><strong>We don't accept paid reviews.</strong> We don't publish reviews at all on this site (V1). When we do, they will be clearly attributed and not paid for.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Cost estimates are estimates</h2>
  <div class="prose-wide">
    <p>The price ranges published on this site are derived from publicly reported figures by CDPHE and El Paso County Public Health and from typical Colorado Springs market scenarios.<sup><a href="#src-1">[1]</a></sup><sup><a href="#src-2">[2]</a></sup> They are <strong>estimates only</strong>. Your written contractor quote is the only price that matters for your home.</p>
  </div>
</section>

<section>
  <h2>Corrections policy</h2>
  <div class="prose-wide">
    <p>If you find a factual error on this site — an outdated cost figure, a misstated regulation, an incorrect citation, a broken source link — <a href="/contact/">email us</a> with the page URL and the specific claim. We'll review, correct or remove the claim, and add a correction note at the bottom of the page when warranted.</p>
  </div>
</section>

<aside class="sources" aria-label="Sources">
  <h2>Sources</h2>
  <ol>
    <li id="src-1">CDPHE. <em>Radon</em>. <a href="{s('cdphe_radon')}" rel="noopener" target="_blank">cdphe.colorado.gov/radon</a></li>
    <li id="src-2">El Paso County Public Health. <em>Radon</em>. <a href="{s('elpaso_radon')}" rel="noopener" target="_blank">elpasocountyhealth.org/radon</a></li>
  </ol>
</aside>
"""


# =========================================================================
# PRIVACY
# =========================================================================
PRIVACY_BODY = """
<section>
  <div class="prose-wide">
    <p>This privacy policy explains what information Colorado Radon Guide collects, how we use it, who we share it with, and how you can request a copy or deletion of your data.</p>
    <div class="callout">
      <strong>Plain-language summary</strong>
      <p>We collect what you give us through the quote form, plus standard web analytics. We share quote submissions with one licensed Colorado mitigation partner so they can contact you about your radon situation. We do not sell your data to anyone.</p>
    </div>
  </div>
</section>

<section>
  <h2>Information we collect</h2>
  <div class="prose-wide">
    <p>When you submit a quote request, we collect:</p>
    <ul>
      <li>Name, phone, and email address</li>
      <li>ZIP code and optionally a property address</li>
      <li>The reason for your inquiry (test result, real estate transaction, etc.)</li>
      <li>Property details you choose to share (foundation type, square footage, latest radon result, closing date, notes)</li>
      <li>The page on this site that you submitted from</li>
    </ul>
    <p>When you browse the site, we also collect standard analytics: IP address, browser type, pages viewed, referring URL, and approximate location derived from IP. We use this to understand which pages are useful and to improve the site.</p>
  </div>
</section>

<section>
  <h2>How we use your information</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Quote routing.</strong> Your quote submission is shared with one licensed Colorado radon mitigation contractor who serves your area, so they can prepare a quote.</li>
      <li><strong>Communication.</strong> We may use your email to send a transactional confirmation that your submission was received and to follow up if information is missing.</li>
      <li><strong>Analytics and site improvement.</strong> We use aggregated, anonymized analytics to understand site usage.</li>
      <li><strong>Legal compliance.</strong> We may disclose information when required by law or to protect against fraud.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Who we share information with</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Our mitigation partner.</strong> One licensed Colorado contractor per quote submission. We do not sell your information to multiple contractors, data brokers, or marketing lists.</li>
      <li><strong>Service providers.</strong> Form processing, email delivery, and analytics providers may receive limited data necessary to operate the site.</li>
      <li><strong>No third-party sale or marketing.</strong> We do not sell your personal information.</li>
    </ul>
  </div>
</section>

<section>
  <h2>Cookies and analytics</h2>
  <div class="prose-wide">
    <p>We use standard first-party cookies for site functionality and may use a privacy-friendly analytics provider (e.g., Plausible, Fathom, or similar) to understand traffic patterns. We do not use cross-site tracking or ad-targeting cookies on this V1 of the site.</p>
  </div>
</section>

<section>
  <h2>Your rights</h2>
  <div class="prose-wide">
    <p>You can request a copy of the data we hold about you, ask us to correct it, or ask us to delete it. Email us at the address on the <a href="/contact/">contact page</a> and we will respond within 30 days.</p>
  </div>
</section>

<section>
  <h2>Changes to this policy</h2>
  <div class="prose-wide">
    <p>If we change this policy materially, we will update the "last updated" date in the footer and, for significant changes, post a notice on the site for at least 30 days.</p>
  </div>
</section>

<section>
  <h2>Note</h2>
  <div class="prose-wide">
    <p>This page is a plain-language privacy summary suitable for a V1 launch. Before scaling to other states or running paid traffic, have an attorney review and replace this page with a jurisdiction-appropriate privacy notice (including CCPA, CPA, and any other applicable state law sections).</p>
  </div>
</section>
"""


# =========================================================================
# CONTACT
# =========================================================================
CONTACT_BODY = """
<section>
  <div class="prose-wide">
    <p>Use the right channel for your question — it'll get to the right person faster.</p>
  </div>
</section>

<section>
  <div class="card-grid">
    <div class="card">
      <h3>Looking for a radon quote?</h3>
      <p>Use the quote request form. It captures the details a contractor needs to prepare a written quote, and your submission goes to a licensed Colorado mitigation partner.</p>
      <p><a href="/request-quote/" class="btn btn-secondary">Request a Quote</a></p>
    </div>
    <div class="card">
      <h3>Corrections, press, partnerships</h3>
      <p>For factual corrections, press inquiries, contractor partnership questions, and other non-quote requests, email us at the address below.</p>
      <p><strong>hello@coloradoradonguide.com</strong></p>
      <p style="font-size:.85rem;color:var(--text-muted);">Replace with your live address before launch.</p>
    </div>
  </div>
</section>

<section>
  <h2>Specifically:</h2>
  <div class="prose-wide">
    <ul>
      <li><strong>Factual corrections.</strong> If a claim, citation, or cost figure on this site is wrong or outdated, include the page URL and the specific claim. We'll review and correct or remove it.</li>
      <li><strong>Press.</strong> If you're a Colorado journalist, agent, or inspector covering radon, we're happy to provide research notes, source links, or interviews.</li>
      <li><strong>Contractor partnerships.</strong> If you're a Colorado-licensed radon mitigation contractor interested in receiving leads, include your DORA registration number and NRPP or NRSB certification in your first message. We require both before any further conversation.</li>
      <li><strong>Privacy.</strong> Data access, correction, or deletion requests are described in the <a href="/privacy/">privacy policy</a> and should be sent to the email above.</li>
      <li><strong>General questions.</strong> Anything else, just email us — we read it all.</li>
    </ul>
  </div>
</section>
"""
