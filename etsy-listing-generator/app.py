import os
import json
import anthropic
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SYSTEM_PROMPT = """You are an expert Etsy SEO specialist. When given a product description,
you generate a fully optimized Etsy listing with a title, 13 tags, and a description.

Rules:
- Title: max 140 characters, lead with the strongest keyword, read naturally
- Tags: exactly 13, each 2-3 words, no repeating exact title phrases, cover material/style/occasion/recipient/use case/synonyms
- Description: 5 short paragraphs — hook, product details, use case/gifting, shop logistics, CTA

Return ONLY valid JSON in this exact shape, no markdown fences, no extra text:
{
  "title": "...",
  "tags": ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6", "tag7", "tag8", "tag9", "tag10", "tag11", "tag12", "tag13"],
  "description": "..."
}"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    product_description = (data.get("description") or "").strip()
    category = (data.get("category") or "").strip()
    target_buyer = (data.get("target_buyer") or "").strip()

    if not product_description:
        return jsonify({"error": "Product description is required."}), 400

    user_message = f"Product description: {product_description}"
    if category:
        user_message += f"\nCategory: {category}"
    if target_buyer:
        user_message += f"\nTarget buyer: {target_buyer}"

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return jsonify({"error": "ANTHROPIC_API_KEY environment variable not set."}), 500

    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = message.content[0].text.strip()

    try:
        listing = json.loads(raw)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse listing from AI response.", "raw": raw}), 500

    return jsonify(listing)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
