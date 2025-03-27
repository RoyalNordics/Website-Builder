from utils.fixer import fix_html

def analyze_html(html):
    fixed_html, changes = fix_html(html)
    return {
        "original": html,
        "fixed": fixed_html,
        "changes": changes
    }