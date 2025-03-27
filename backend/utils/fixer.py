from bs4 import BeautifulSoup

def fix_html(html):
    soup = BeautifulSoup(html, "html5lib")
    changes = []

    # Tilføj alt-tekst til <img> tags hvis de mangler
    for img in soup.find_all("img"):
        if not img.get("alt"):
            img["alt"] = "Image"
            changes.append({
                "type": "missing_alt",
                "element": str(img),
                "fix": "Added alt='Image'"
            })

    # Tilføj aria-label til knapper uden tekst
    for button in soup.find_all("button"):
        if not button.text.strip() and not button.get("aria-label"):
            button["aria-label"] = "button"
            changes.append({
                "type": "missing_aria",
                "element": str(button),
                "fix": "Added aria-label"
            })

    # Tilføj placeholder til input-felter der mangler det
    for inp in soup.find_all("input"):
        if not inp.get("placeholder"):
            inp["placeholder"] = "Enter value"
            changes.append({
                "type": "missing_placeholder",
                "element": str(inp),
                "fix": "Added placeholder"
            })

    return str(soup), changes