from pathlib import Path


def build_svg(path: Path) -> None:
    boxes = [
        (35, 55, 180, 62, "Natural rainfall", "season · location · hazard"),
        (265, 55, 180, 62, "Environmental scarcity", "dry spell · deficit · loss"),
        (495, 55, 180, 62, "Demand / request", "belief · resources · social value"),
        (725, 55, 180, 62, "Provider acceptance", "signal · price · reputation"),
        (725, 205, 180, 62, "Accepted pseudo-event", "selection, not treatment"),
        (495, 205, 180, 62, "Natural outcome", "rain is unchanged by ritual"),
        (265, 205, 180, 62, "Apparent success", "rain inside attribution window"),
        (35, 205, 180, 62, "Belief and reputation", "Bayes · recency · memory"),
        (150, 355, 220, 62, "Plural valuation / WTP", "rain value + separate social utility"),
        (570, 355, 220, 62, "Price and expenditure", "WTP · revenue-maximizing price"),
    ]
    arrows = [
        (215, 86, 265, 86),
        (445, 86, 495, 86),
        (675, 86, 725, 86),
        (815, 117, 815, 205),
        (725, 236, 675, 236),
        (495, 236, 445, 236),
        (265, 236, 215, 236),
        (125, 267, 240, 355),
        (355, 267, 290, 355),
        (605, 267, 680, 355),
        (370, 386, 570, 386),
        (125, 205, 125, 117),
        (815, 355, 815, 267),
    ]
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="940" height="470" viewBox="0 0 940 470">',
        "<defs>",
        '<marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">',
        '<path d="M0,0 L10,4 L0,8 z" fill="#475569"/></marker>',
        "</defs>",
        '<rect width="940" height="470" fill="white"/>',
        '<text x="470" y="28" text-anchor="middle" font-family="Arial" font-size="19" font-weight="bold" fill="#0f172a">Zero-effect ecological-economic generative framework</text>',
    ]
    for x1, y1, x2, y2 in arrows:
        lines.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            'stroke="#475569" stroke-width="2.2" marker-end="url(#arrow)"/>'
        )
    for x, y, w, h, title, subtitle in boxes:
        fill = "#e0f2fe" if "Natural" in title or "Environmental" in title else "#f1f5f9"
        if "Plural" in title or "Price" in title:
            fill = "#ecfccb"
        lines.extend(
            [
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#334155" stroke-width="1.5"/>',
                f'<text x="{x + w / 2}" y="{y + 25}" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#0f172a">{title}</text>',
                f'<text x="{x + w / 2}" y="{y + 45}" text-anchor="middle" font-family="Arial" font-size="10.5" fill="#334155">{subtitle}</text>',
            ]
        )
    lines.extend(
        [
            '<line x1="470" y1="185" x2="470" y2="290" stroke="#dc2626" stroke-width="2" stroke-dasharray="7,5"/>',
            '<text x="480" y="300" font-family="Arial" font-size="11" fill="#b91c1c">No causal arrow from pseudo-event to rainfall</text>',
            '<text x="470" y="450" text-anchor="middle" font-family="Arial" font-size="10.5" fill="#475569">All apparent effects arise through timing, selection, attribution, valuation, and learning; meteorological efficacy is fixed at zero.</text>',
            "</svg>",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "figures" / "figure1_framework.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    build_svg(output)
