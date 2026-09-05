"""Build a factual English academic CV for the homepage download."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    HRFlowable,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "pdf" / "cv.pdf"
INK = HexColor("#222222")
MUTED = HexColor("#555555")
RULE = HexColor("#245f93")


def register_fonts():
    candidates = [
        (r"C:\Windows\Fonts\times.ttf", r"C:\Windows\Fonts\timesbd.ttf", r"C:\Windows\Fonts\timesi.ttf"),
        (r"C:\Windows\Fonts\Times.ttf", r"C:\Windows\Fonts\Timesbd.ttf", r"C:\Windows\Fonts\Timesi.ttf"),
    ]
    for regular, bold, italic in candidates:
        if Path(regular).exists() and Path(bold).exists() and Path(italic).exists():
            pdfmetrics.registerFont(TTFont("CV-Roman", regular))
            pdfmetrics.registerFont(TTFont("CV-Bold", bold))
            pdfmetrics.registerFont(TTFont("CV-Italic", italic))
            return "CV-Roman", "CV-Bold", "CV-Italic"
    return "Times-Roman", "Times-Bold", "Times-Italic"


def styles():
    roman, bold, italic = register_fonts()
    base = getSampleStyleSheet()
    s = {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName=bold,
            fontSize=16,
            leading=19,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName=roman,
            fontSize=9.5,
            leading=12.5,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName=bold,
            fontSize=11,
            leading=14,
            textColor=RULE,
            spaceBefore=8,
            spaceAfter=3,
        ),
        "job": ParagraphStyle(
            "Job",
            parent=base["Normal"],
            fontName=bold,
            fontSize=10,
            leading=13,
            textColor=INK,
            spaceBefore=5,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName=italic,
            fontSize=9.2,
            leading=12,
            textColor=MUTED,
            spaceAfter=1,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName=roman,
            fontSize=9.6,
            leading=12.4,
            textColor=INK,
            alignment=TA_JUSTIFY,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName=roman,
            fontSize=9.6,
            leading=12.4,
            textColor=INK,
            alignment=TA_JUSTIFY,
        ),
        "edu": ParagraphStyle(
            "Edu",
            parent=base["Normal"],
            fontName=roman,
            fontSize=9.6,
            leading=12.6,
            textColor=INK,
            spaceAfter=2,
        ),
        "loose": ParagraphStyle(
            "Loose",
            parent=base["Normal"],
            fontName=roman,
            fontSize=10,
            leading=13.6,
            textColor=INK,
            alignment=TA_JUSTIFY,
        ),
    }
    return s


def bullets(items, style, space_before=1, space_after=1):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=10, bulletColor=INK) for item in items],
        bulletType="bullet",
        start="•",
        leftIndent=14,
        bulletFontName="Times-Roman",
        bulletFontSize=9,
        spaceBefore=space_before,
        spaceAfter=space_after,
    )


def build():
    s = styles()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.5 * inch,
        title="Zhenghao Xu — Curriculum Vitae",
        author="Zhenghao Xu",
    )
    story = [
        Paragraph("Zhenghao Xu", s["name"]),
        Paragraph(
            "Undergraduate, Computer Science and Technology, University of Science and Technology Beijing<br/>"
            '<link href="mailto:U202442468@xs.ustb.edu.cn">U202442468@xs.ustb.edu.cn</link>'
            " · "
            '<link href="https://xu-zhenghao-zzz.github.io">xu-zhenghao-zzz.github.io</link>'
            " · "
            '<link href="https://github.com/Xu-zhenghao-zzz">github.com/Xu-zhenghao-zzz</link>',
            s["contact"],
        ),
        HRFlowable(width="100%", thickness=1.1, color=RULE, spaceAfter=2),
        Paragraph("Education", s["section"]),
        Paragraph(
            "<b>University of Science and Technology Beijing (USTB)</b> — B.Eng. candidate, Computer Science and Technology"
            " &nbsp;&nbsp; Sep. 2024 – Jun. 2028 (expected)<br/>"
            "School of Computer and Communication Engineering. GPA <b>3.81/4.00</b>, weighted average <b>89.6/100</b>, major rank <b>10/137</b>.",
            s["edu"],
        ),
        Paragraph(
            "<b>Carnegie Mellon University</b> — Collaborative course, <i>Algorithms for Big Data</i> (Prof. David P. Woodruff)"
            " &nbsp;&nbsp; Oct. 11, 2024 – Jan. 5, 2025<br/>"
            "Grade: <b>88.70/100</b>.",
            s["edu"],
        ),
        Paragraph(
            "<b>Westlake University</b> — 2026 PEBBLE BioFusion Workshop, Center for Interdisciplinary Studies"
            " &nbsp;&nbsp; Jul. 24 – Aug. 4, 2026",
            s["edu"],
        ),
        Paragraph("Research Experience", s["section"]),
        Paragraph("GRACE: Graph-Aware Routing Along with Compression for End-to-End Optimization", s["job"]),
        Paragraph("Fourth author · Sep. 2025 – Present", s["meta"]),
        bullets(
            [
                "Implemented the PPO training, evaluation, and logging pipeline for joint routing and in-network compression with GNN-encoded network states.",
                "Designed cross-topology generalization experiments by evaluating a policy trained on one topology directly on unseen topologies, without additional training.",
                "Ran workload, parameter-sensitivity, baseline, and ablation experiments for the current IEEE TNSM Major Revision.",
            ],
            s["bullet"],
        ),
        Paragraph("RobustVidBench: Benchmarking Robustness of Multimodal Video Understanding", s["job"]),
        Paragraph("Fourth author · Sep. 2025 – Present", s["meta"]),
        bullets(
            [
                "Worked on video preprocessing for the benchmark, including download, clipping, transcoding, sampling, format normalization, audio handling, and metadata cleaning.",
                "Implemented controlled degradations: bitrate/resolution/frame-rate reduction, frame dropping, stuttering/repeated frames, and audio–video misalignment.",
                "Participated in QA verification, model evaluation, experimental analysis, and manuscript preparation.",
            ],
            s["bullet"],
        ),
        Paragraph("Automated Video Understanding Dataset Construction", s["job"]),
        Paragraph("Fourth author · Feb. 2026 – Present", s["meta"]),
        bullets(
            [
                "Participated in the design of a Video → Knowledge Graph → Summary → QA data-construction pipeline.",
                "Implemented core video-processing and QA-generation components and used vLLM for batched inference.",
                "The project covers 600+ videos; I directly worked on about 150 videos and generated or processed nearly 10,000 QA samples across the main pipeline and experimental variants.",
            ],
            s["bullet"],
        ),
        Paragraph("A Recurrent Rab8a-associated Hypoxic Niche in Spatial CRISPR Tumour Data", s["job"]),
        Paragraph("First author · 2026 PEBBLE BioFusion Workshop, Westlake University · Jul. 2026 – Aug. 2026", s["meta"]),
        bullets(
            [
                "Developed a dual-view representation that combines local cellular-neighborhood information and gene-expression features with graph neural networks.",
                "Contributed to model implementation, experiments, and manuscript preparation. The work received the Excellent Research Report Award.",
            ],
            s["bullet"],
        ),
        Paragraph("Computation–Routing Joint Optimization in UAV Networks", s["job"]),
        Paragraph("Second author · 2025 – Present", s["meta"]),
        bullets(
            [
                "Led problem formulation, reinforcement-learning implementation, and simulation experiments for joint routing, compute placement, and compression decisions in a shared wireless environment.",
            ],
            s["bullet"],
        ),
        PageBreak(),
        Paragraph("Selected Research Outputs", s["section"]),
        bullets(
            [
                "Xiaolong Cui, Xuebin Tang, Zixu Wang, <b>Zhenghao Xu</b>, Wei Huangfu. “GRACE: Graph-Aware Routing Along with Compression for End-to-End Optimization.” <i>IEEE Transactions on Network and Service Management</i> (TNSM), Major Revision.",
                "Dongyan Zhang, Peijie Wu, Jingyu Wu, <b>Zhenghao Xu</b>, Xiaotian Hu, Yuqing Zhang. “RobustVidBench: Benchmarking Robustness of Multimodal Video Understanding.” Manuscript in preparation.",
                "<b>Zhenghao Xu</b> et al. “A Recurrent Rab8a-associated Hypoxic Niche in Spatial CRISPR Tumour Data.” Research manuscript, 2026 PEBBLE BioFusion Workshop, Westlake University.",
            ],
            s["loose"],
            space_before=3,
            space_after=4,
        ),
        Paragraph("Patent", s["section"]),
        bullets(
            [
                "Xiaolong Cui, Xuebin Tang, Zixu Wang, Wei Huangfu, <b>Zhenghao Xu</b>. “A Deep Reinforcement Learning Method and System for Joint Optimization of Computing-Network Routing and In-Network Data Processing.” Chinese Invention Patent Application No. 2026102073230, 2026.",
            ],
            s["loose"],
            space_before=3,
            space_after=4,
        ),
        Paragraph("Awards", s["section"]),
        bullets(
            [
                "Meritorious Winner, Interdisciplinary Contest in Modeling (ICM 2026), Problem E. Team captain; mainly responsible for modeling and implementation.",
                "Excellent Research Report Award, 2026 PEBBLE BioFusion Workshop, Westlake University.",
                "First Prize (Beijing), Jingcai Dachuang Innovation and Entrepreneurship Competition.",
                "Second Prize (Beijing), Challenge Cup Capital Entrepreneurship Plan Competition, “Qingzhi Future” track (team captain).",
                "Second Prize (Beijing), Challenge Cup Capital Entrepreneurship Plan Competition, “Qingli Grassroots” track.",
                "First Prize, USTB Cradle Cup Innovation and Entrepreneurship Competition.",
            ],
            s["loose"],
            space_before=3,
            space_after=4,
        ),
        Paragraph("Skills", s["section"]),
        Paragraph(
            "<b>Programming:</b> Python, C/C++, Java, SQL<br/>"
            "<b>ML &amp; AI:</b> PyTorch, vLLM, Hugging Face, TensorBoard<br/>"
            "<b>Development:</b> Linux, Git, Docker, LaTeX<br/>"
            "<b>Scientific computing:</b> NumPy, Pandas, NetworkX, MATLAB",
            s["loose"],
        ),
        Spacer(1, 8),
        Paragraph("Activities", s["section"]),
        Paragraph(
            "Class Representative, Computer Science Class 242. Head of Academic Affairs, Suosi Science and Technology Association.",
            s["loose"],
        ),
    ]
    doc.build(story)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
