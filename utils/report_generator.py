from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

from reportlab.lib.units import mm

def add_page_number(canvas, doc):
    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        9
    )

    canvas.drawRightString(
        200 * mm,
        10 * mm,
        f"AI Resume Analyzer | Page {doc.page}"
    )

    canvas.restoreState()

from reportlab.platypus import Paragraph, Spacer

def add_formatted_text(elements, text, styles):

    if not text:
        return

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        # Blank line
        if line == "":
            elements.append(Spacer(1, 8))
            continue

        # Markdown headings
        if line.startswith("#"):

            heading = line.replace("#", "").strip()

            elements.append(
                Paragraph(
                    f"<b>{heading}</b>",
                    styles["Heading2"]
                )
            )

            elements.append(
                Spacer(1, 10)
            )

            continue

        # Bullets
        if (
            line.startswith("-")
            or line.startswith("*")
            or line.startswith("•")
        ):

            bullet = line.lstrip("-*• ").strip()

            elements.append(
                Paragraph(
                    f"• {bullet}",
                    styles["BodyText"]
                )
            )

            continue

        # Numbered items
        if (
            len(line) > 2
            and line[0].isdigit()
            and line[1] == "."
        ):

            elements.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            continue

        # Normal paragraph
        elements.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 5)
        )

def generate_pdf_report(
    ats_result,
    ai_analysis,
    interview_questions,
    roadmap,
    output_path="report.pdf"
):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    styles["BodyText"].leading = 18
    styles["BodyText"].spaceAfter = 6

    styles["Heading1"].spaceBefore = 12
    styles["Heading1"].spaceAfter = 12

    styles["Heading2"].spaceBefore = 8
    styles["Heading2"].spaceAfter = 8

    elements = []

    #==========================
    # COVER PAGE
    #==========================

    elements.append(
        Spacer(1, 120)
    )

    elements.append(
        Paragraph(
            "<font size=28><b>AI Resume Analyzer</b></font>",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "<font size=18>Professional Resume Analysis Report</font>",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 40)
    )

    elements.append(
        Paragraph(
            f"<b>Report Generated:</b> {datetime.now().strftime('%d %B %Y')}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "<b>Powered By:</b> Gemini AI • ATS Analyzer • AI Interview Coach",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 40)
    )

    elements.append(
        Paragraph(
            """
            This report provides a comprehensive evaluation of your resume,
            ATS compatibility, AI-powered analysis, personalized interview
            questions, and a customized learning roadmap.
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 150)
    )

    elements.append(
        Paragraph(
            "<i>Prepared using AI Resume Analyzer & Interview Coach</i>",
            styles["Italic"]
        )
    )

    elements.append(PageBreak())

    #==========================
    # CANDIDATE SUMMARY
    #==========================

    elements.append(
        Paragraph(
            "Candidate Summary",
            styles["Heading1"]
        )
    )

    resume_words = len(
        ai_analysis.split()
    ) if ai_analysis else 0

    elements.append(
        Paragraph(
            f"<b>Resume Analysis Length:</b> {resume_words} words",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Interview Questions:</b> Generated",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Learning Roadmap:</b> Personalized",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # ATS SCORE
    # ==========================

    elements.append(
        Paragraph(
            "ATS Score Summary",
            styles["Heading1"]
        )
    )

    final_score = ats_result.get(
        "final_ats_score",
        "N/A"
    )

    elements.append(
        Paragraph(
            f"<b>Overall ATS Score:</b> {final_score}%",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # ==========================
    # ATS TABLE
    # ==========================

    table_data = [
        ["Category", "Score"]
    ]

    for key, value in ats_result.items():

        table_data.append(
            [
                key.replace("_", " ").title(),
                str(value)
            ]
        )

    ats_table = Table(
        table_data,
        colWidths=[250, 120]
    )

    ats_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 1, colors.black),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 1), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
                ("ALIGN", (1, 1), (-1, -1), "CENTER"),
            ]
        )
    )

    elements.append(ats_table)

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # PAGE BREAK
    # ==========================

    elements.append(PageBreak())

    # ==========================
    # AI ANALYSIS
    # ==========================

    elements.append(
        Paragraph(
            "Resume Analysis & Recommendation",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        elements,
        ai_analysis,
        styles
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # INTERVIEW QUESTIONS
    # ==========================

    elements.append(
        Paragraph(
            "Personalized Interview Preparation",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        elements,
        interview_questions,
        styles
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # PAGE BREAK
    # ==========================

    elements.append(PageBreak())

    # ==========================
    # ROADMAP
    # ==========================

    elements.append(
        Paragraph(
            "90-Day Learning Roadmap",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        elements,
        roadmap,
        styles
    )

    elements.append(
        Spacer(1, 20)
    )

    # ==========================
    # FOOTER
    # ==========================

    elements.append(
        Paragraph(
            "Generated by AI Resume Analyzer & Interview Coach",
            styles["Italic"]
        )
    )

    doc.build(
        elements,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    return output_path