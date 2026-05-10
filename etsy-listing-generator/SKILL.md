---
name: etsy-listing-generator
description: Generate optimized Etsy listing titles, all 13 tags, and a compelling
  product description from a plain-language product description. Reduces hours of
  manual SEO work to seconds. Use when an Etsy seller needs to create or refresh
  a product listing.
---

# Etsy Listing Generator Skill

## Purpose
Turn a seller's plain-language product description into a fully optimized Etsy
listing — title, 13 SEO tags, and a buyer-focused description — in one pass.
Etsy's algorithm weighs all three equally; most sellers get one or two right
and leave traffic on the table.

---

## What You Receive From the Seller
- **Product description**: what the item is, materials, size, use case, style
- **Category** (optional): e.g. "jewelry", "home decor", "digital download"
- **Target buyer** (optional): e.g. "bridesmaids", "dog moms", "minimalist home"

---

## Output Format

Produce exactly this structure. No preamble, no explanation — just the listing.

---

### LISTING TITLE
[140-character max. Lead with the strongest keyword. Include style, material,
occasion, and recipient where natural. No keyword stuffing — must read naturally.]

### TAGS (13)
1. [tag — 2-3 words, high search intent]
2. [tag]
3. [tag]
4. [tag]
5. [tag]
6. [tag]
7. [tag]
8. [tag]
9. [tag]
10. [tag]
11. [tag]
12. [tag]
13. [tag]

*Tags should span: material, style, occasion, recipient, use case, and synonyms.
No single-word tags. No repeated phrases from the title (Etsy deduplicates them).*

### DESCRIPTION
[Opening hook — one sentence that speaks directly to the buyer's desire or problem]

[Product details paragraph — materials, dimensions, colors, variations available]

[Use case / gifting paragraph — who it's for, when they'd give/use it]

[Shop details — processing time, customization options, care instructions]

[Closing CTA — one sentence encouraging them to message with questions or buy now]

---

## SEO Rules Applied
- Title front-loads the primary keyword (first 40 chars are most weighted)
- Tags avoid repeating the exact title phrase (wasted slot per Etsy's own guidance)
- Tags use multi-word phrases (2–3 words) that match real buyer searches
- Description opens with the primary keyword in the first sentence (Etsy indexes it)
- No keyword stuffing — listings that read like spam get deprioritized

---

## Deployment Options [CUSTOMIZE]
- **Standalone web app**: Use `app.py` in this directory — Flask app with clean UI
- **Claude Project**: Paste this SKILL.md as the system prompt, share link with sellers
- **Etsy seller community**: Offer as a paid tool ($5-9/month) or one-time Etsy listing
- **API embed**: Wrap in a paywall using Stripe + this skill as the core engine
