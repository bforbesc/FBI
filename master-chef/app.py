import re
from pathlib import Path

import gradio as gr

DATA = Path(__file__).parent / "data"

CSS = """
/* Override Gradio CSS variables — this wins over the theme */
:root, .dark {
    --body-text-color: #111 !important;
    --body-text-color-subdued: #444 !important;
    --block-label-text-color: #333 !important;
    --color-accent: #111 !important;
    --color-accent-soft: #eee !important;
    --button-secondary-text-color: #444 !important;
    --tab-text-color: #444 !important;
    --tab-text-color-selected: #111 !important;
}

/* Container */
.gradio-container {
    max-width: none !important;
    width: 100% !important;
    padding: 48px 80px 80px !important;
    background: #fff !important;
    box-sizing: border-box !important;
}
.main.app { max-width: none !important; padding: 0 !important; }
.contain { max-width: none !important; width: 100% !important; }
.tabs { max-width: none !important; width: 100% !important; }
* { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important; }

/* Title */
.app-title h1 {
    font-size: 1.25rem !important;
    font-weight: 600 !important;
    color: #111 !important;
    letter-spacing: -0.01em !important;
    margin: 0 0 2rem 0 !important;
    padding: 0 !important;
    border: none !important;
}

/* Tabs */
.tabs > .tab-nav {
    border-bottom: 1px solid #e5e5e5 !important;
    background: none !important;
    margin-bottom: 2rem !important;
}
.tabs > .tab-nav button {
    background: none !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    color: #444 !important;
    opacity: 1 !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    padding: 8px 16px 8px 0 !important;
    margin-right: 8px !important;
    cursor: pointer !important;
    border-radius: 0 !important;
    box-shadow: none !important;
}
.tabs > .tab-nav button.selected {
    color: #111 !important;
    opacity: 1 !important;
    border-bottom: 2px solid #111 !important;
}

/* Progress */
.progress-line, .progress-line p, .progress-line * {
    font-size: 0.9rem !important;
    color: #333 !important;
    opacity: 1 !important;
    margin-bottom: 2rem !important;
}

/* Category label — the span that holds the group title */
.checkboxgroup span:not(.ml-2) {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: #333 !important;
    letter-spacing: 0 !important;
    margin-bottom: 4px !important;
}

/* Checkbox items — vertical list */
.checkboxgroup .wrap {
    flex-direction: column !important;
    gap: 0 !important;
    border: 1px solid #ebebeb !important;
    border-radius: 6px !important;
    overflow: hidden !important;
    margin-bottom: 1.5rem !important;
}
.checkboxgroup .wrap label {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 10px 14px !important;
    margin: 0 !important;
    border: none !important;
    border-bottom: 1px solid #f2f2f2 !important;
    background: #fff !important;
    font-size: 0.875rem !important;
    color: #222 !important;
    cursor: pointer !important;
    border-radius: 0 !important;
    box-shadow: none !important;
}
.checkboxgroup .wrap label:last-child { border-bottom: none !important; }
.checkboxgroup .wrap label:hover { background: #fafafa !important; }
.checkboxgroup .wrap label input[type="checkbox"] {
    accent-color: #111 !important;
    width: 14px !important;
    height: 14px !important;
    flex-shrink: 0 !important;
}
/* Strikethrough checked items */
.checkboxgroup .wrap label:has(input:checked) span {
    color: #bbb !important;
    text-decoration: line-through !important;
}

/* Remove all gray backgrounds from blocks/groups */
.block, .form, .group, .panel {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* Accordions */
.accordion {
    border: 1px solid #ebebeb !important;
    border-radius: 6px !important;
    box-shadow: none !important;
    margin-bottom: 8px !important;
    overflow: hidden !important;
}
.accordion button.label-wrap {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 16px !important;
    padding: 13px 16px !important;
    background: #fff !important;
    width: 100% !important;
    cursor: pointer !important;
}
.accordion button.label-wrap span:first-child {
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    color: #111 !important;
    flex: 1 !important;
    text-align: left !important;
}
.accordion button.label-wrap svg {
    flex-shrink: 0 !important;
    opacity: 0.25 !important;
    width: 16px !important;
    height: 16px !important;
}
.accordion .inner { padding: 0 16px 16px 16px !important; background: #fff !important; }
.accordion .inner p { font-size: 0.875rem !important; color: #444 !important; line-height: 1.65 !important; margin: 8px 0 !important; }
.accordion .inner li { font-size: 0.875rem !important; color: #444 !important; line-height: 1.65 !important; list-style-color: #bbb !important; }
.accordion .inner li::marker { color: #bbb !important; }
.accordion .inner h2 { font-size: 0.8rem !important; font-weight: 600 !important; color: #999 !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; margin: 20px 0 6px !important; border: none !important; }
.accordion .inner h3 { font-size: 0.8rem !important; font-weight: 600 !important; color: #999 !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; margin: 16px 0 4px !important; border: none !important; }
.accordion .inner hr { border: none !important; border-top: 1px solid #f0f0f0 !important; margin: 12px 0 !important; }
.accordion .inner strong { color: #222 !important; font-weight: 600 !important; }

/* Hide Gradio footer */
footer, .built-with { display: none !important; }
"""

STRIP_EMOJI = re.compile(
    r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F900-\U0001F9FF"
    r"\U00002600-\U000026FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]+",
    flags=re.UNICODE,
)


def strip_emoji(text):
    return STRIP_EMOJI.sub("", text).strip()


def parse_shopping_list():
    text = (DATA / "shopping_list.md").read_text()
    categories = {}
    current_cat = None
    for line in text.splitlines():
        if line.startswith("## "):
            current_cat = strip_emoji(line[3:].strip())
            categories[current_cat] = []
        elif (line.startswith("- [ ] ") or line.startswith("- [x] ")) and current_cat:
            checked = line.startswith("- [x] ")
            item = line[6:].strip()
            categories[current_cat].append({"item": item, "checked": checked})
    return categories


def parse_recipes():
    text = (DATA / "weekly_plan.md").read_text()
    recipe_files = list(dict.fromkeys(re.findall(r"\[\[([^\]]+)\]\]", text)))
    recipes = []
    for rf in recipe_files:
        path = DATA / "recipes" / f"{rf}.md"
        if not path.exists():
            continue
        content = path.read_text()
        title_match = re.search(r"^# (.+)", content, re.MULTILINE)
        summary_match = re.search(r"\*\*Resumo\*\*: (.+)", content)
        # Strip title, Resumo and Última atualização lines (shown separately)
        content_body = re.sub(r"^# .+\n?", "", content, count=1, flags=re.MULTILINE)
        content_body = re.sub(r"^\*\*Resumo\*\*:.+\n?", "", content_body, flags=re.MULTILINE)
        content_body = re.sub(r"^\*\*Última atualização\*\*:.+\n?", "", content_body, flags=re.MULTILINE)
        content_body = content_body.strip().lstrip("---").strip()
        # Clean wiki-style [[links]] → plain text
        content_body = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).replace("_", " ").title(), content_body)
        recipes.append({
            "title": title_match.group(1) if title_match else rf,
            "summary": summary_match.group(1) if summary_match else "",
            "content": content_body,
        })
    return recipes


def update_shopping_md(updates: dict):
    path = DATA / "shopping_list.md"
    lines = path.read_text().splitlines()
    new_lines = []
    for line in lines:
        if line.startswith("- [ ] ") or line.startswith("- [x] "):
            item_text = line[6:].strip()
            if item_text in updates:
                marker = "[x]" if updates[item_text] else "[ ]"
                line = f"- {marker} {item_text}"
        new_lines.append(line)
    path.write_text("\n".join(new_lines))


def progress_text(categories):
    all_items = [i for items in categories.values() for i in items]
    done = sum(1 for i in all_items if i["checked"])
    total = len(all_items)
    remaining = total - done
    return f"{done} comprados · {remaining} em falta"


def make_save_fn(all_choices_per_cat):
    def save(*checked_lists):
        updates = {}
        for choices, checked in zip(all_choices_per_cat, checked_lists):
            for item in choices:
                updates[item] = item in checked
        update_shopping_md(updates)
        return progress_text(parse_shopping_list())
    return save


# --- Build app ---

theme = gr.themes.Monochrome()

categories = parse_shopping_list()
recipes = parse_recipes()

with gr.Blocks(title="Chef Pessoal") as app:

    gr.Markdown("# Chef Pessoal", elem_classes=["app-title"])

    with gr.Tabs():

        # --- Tab 1: Shopping list ---
        with gr.Tab("Lista de Compras"):
            progress = gr.Markdown(
                value=progress_text(categories),
                elem_classes=["progress-line"],
            )

            checkboxes = []
            all_choices = []
            for cat, items in categories.items():
                choices = [i["item"] for i in items]
                value = [i["item"] for i in items if i["checked"]]
                cg = gr.CheckboxGroup(
                    choices=choices,
                    value=value,
                    label=cat,
                    elem_classes=["checkboxgroup"],
                )
                checkboxes.append(cg)
                all_choices.append(choices)

            save_fn = make_save_fn(all_choices)
            for cg in checkboxes:
                cg.change(fn=save_fn, inputs=checkboxes, outputs=progress)

        # --- Tab 2: Recipes ---
        with gr.Tab("Receitas"):
            for recipe in recipes:
                with gr.Accordion(
                    f"{recipe['title']}",
                    open=False,
                    elem_classes=["accordion"],
                ):
                    if recipe["summary"]:
                        gr.Markdown(f"*{recipe['summary']}*\n\n---\n\n{recipe['content']}")
                    else:
                        gr.Markdown(recipe["content"])

if __name__ == "__main__":
    app.launch(css=CSS, theme=theme)
