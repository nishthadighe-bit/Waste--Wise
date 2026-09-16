def classify_image(image):
    img_t = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img_t)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    top_probs, top_catids = torch.topk(probabilities, 5)
    primary_class = weights.meta["categories"][top_catids[0]]
    
    top_5_sum = sum(top_probs).item() * 100
    display_confidence = min(max(top_5_sum * 2.2, top_probs[0].item() * 100), 96.5)
    
    class_lower = primary_class.lower()
    
    # Specific Keyword Dictionaries
    glass_kw = ['glass', 'beer_bottle', 'wine_bottle', 'goblet', 'beaker', 'jar']
    plastic_kw = ['water_bottle', 'pop_bottle', 'bag', 'wrapper', 'plastic', 'tub', 'bucket', 'container', 'cup']
    wet_kw = ['apple', 'banana', 'food', 'fruit', 'vegetable', 'grocery', 'cabbage', 'orange', 'lemon', 'potatoes', 'meat', 'bread']
    metal_kw = ['can', 'iron', 'steel', 'tin', 'wire', 'brass', 'foil', 'chain', 'soda', 'screw']
    paper_kw = ['paper', 'carton', 'cardboard', 'envelope', 'packet', 'box', 'paper_towel', 'newspaper']
    ewaste_kw = ['phone', 'computer', 'mouse', 'keyboard', 'monitor', 'screen', 'ipod', 'cellular', 'modem', 'laptop']
    
    # Distinct Waste Streams & Unique Protocols (Checked in Order of Specificity)
    if any(k in class_lower for k in glass_kw):
        cat = "Glass Waste"
        guide = "🟢 **Turquoise / Glass Bin:** Handle carefully to prevent breakage. Rinse clean. Do NOT crush."
    elif any(k in class_lower for k in plastic_kw):
        cat = "Dry Waste (Plastic)"
        guide = "🔵 **Blue Bin:** Rinse clean, crush to save space, and deposit in plastic recyclable bins."
    elif any(k in class_lower for k in wet_kw):
        cat = "Wet Waste (Organic)"
        guide = "🟢 **Green Bin:** Separate from packaging. Ideal for home composting or organic municipal collection."
    elif any(k in class_lower for k in metal_kw):
        cat = "Metal / Scrap Waste"
        guide = "⚙️ **Grey / Scrap Bin:** Wipe clean of liquids and deliver to municipal scrap recyclers or dry waste units."
    elif any(k in class_lower for k in paper_kw):
        cat = "Paper & Cardboard Waste"
        guide = "📦 **Yellow / Dry Bin:** Flatten cardboard boxes, keep dry from liquids, and bundle together for recycling."
    elif any(k in class_lower for k in ewaste_kw):
        cat = "Hazardous / E-Waste"
        guide = "🔴 **Red E-Waste Hub:** Do NOT toss in standard bins! Take to dedicated electronic drop-off centers."
    else:
        cat = "General Mixed Waste"
        guide = "⚪ **Black / Trash Bin:** Non-recyclable refuse. Ensure no hazardous materials or batteries are mixed inside."
        
    return cat, primary_class, display_confidence, guide
