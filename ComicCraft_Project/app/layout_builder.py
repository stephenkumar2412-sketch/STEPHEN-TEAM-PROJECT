import re

def _panel_text(story, panel_number):
    # Accept either "Panel 1:" style output or simply split by panels.
    pattern = rf"(?is)(?:panel\s*{panel_number}\s*:)(.*?)(?=panel\s*{panel_number+1}\s*:|$)"
    m = re.search(pattern, story)
    return m.group(1).strip() if m else story

def build_comic_layout(outline, story, image_paths):
    layout = []
    for i, panel in enumerate(outline):
        layout.append({
            "panel_number": panel["panel_number"],
            "title": panel["title"],
            "image": image_paths[i],
            "scene_description": panel["scene_description"],
            "text": _panel_text(story, panel["panel_number"]),
            "image_prompt": panel["image_prompt"],
        })
    return layout
