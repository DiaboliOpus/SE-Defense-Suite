from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import datetime, json

TEMPLATE_PATH = "templates/strategy_template.txt"

AUTHOR = "Alim Askhatov"
UNIVERSITY = "Eurasian National University"

def generate_pdf(output_path="Corporate_Defense_Strategy.pdf"):
    with open(TEMPLATE_PATH) as f:
        template = f.read()

    template = template.replace("{{AUTHOR}}", AUTHOR)
    template = template.replace("{{UNIVERSITY}}", UNIVERSITY)
    template = template.replace("{{DATE}}", datetime.datetime.now().strftime("%Y-%m-%d"))

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    for line in template.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    doc.build(story)

if __name__ == "__main__":
    generate_pdf()
