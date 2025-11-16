from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import datetime, json

HTML_TEMPLATE = "templates/report_template.html"
CSS_TEMPLATE = "templates/style.css"

def generate_html_report(data, output_path="security_report.html"):
    with open(HTML_TEMPLATE, "r") as f:
        html = f.read()
    with open(CSS_TEMPLATE, "r") as f:
        css = f.read()

    html = html.replace("{{DATE}}", datetime.datetime.now().strftime("%Y-%m-%d"))
    html = html.replace("{{REPORT_DATA}}", json.dumps(data, indent=4))
    html = html.replace("{{STYLE}}", css)

    with open(output_path, "w") as f:
        f.write(html)

def generate_pdf_report(data, output_path="security_report.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("SE-Defense Suite – Security Report", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Date: " + datetime.datetime.now().strftime("%Y-%m-%d"), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Summary:", styles["Heading2"]))

    for key, val in data.items():
        story.append(Paragraph(f"<b>{key}</b>: {val}", styles["Normal"]))
        story.append(Spacer(1, 8))

    doc.build(story)

if __name__ == "__main__":
    sample = {
        "ML Classifier": "Detected 2 phishing emails",
        "URL Analyzer": "3 high-risk URLs",
        "Log Monitor": "1 brute-force attack detected",
        "SE Simulator": "Quiz generated successfully"
    }
    generate_html_report(sample)
    generate_pdf_report(sample)
