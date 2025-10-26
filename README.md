# Illustrated Flora of Türkiye - Instructions for Authors, Illustrators and Editors

<div align="center">

![Logo](docs/assets/od_logo.png)

**Illustrated Flora of Türkiye - Instructions for Authors, Illustrators and Editors**

[![build](https://github.com/demirogun/ifot-instructions/actions/workflows/build.yml/badge.svg)](https://github.com/demirogun/ifot-instructions/actions/workflows/build.yml)
[![Quality Gate Status](https://sonarqube.turkiyeflorasi.org.tr/api/project_badges/measure?project=NezahatGokyigitBotanicGarden_ifot-instructions_ad6ef117-0924-46c8-aff1-d19428bfbc8d&metric=alert_status&token=sqb_451e9a6e591fc266c4d1e796f65458af8169425a)](https://sonarqube.turkiyeflorasi.org.tr/dashboard?id=NezahatGokyigitBotanicGarden_ifot-instructions_ad6ef117-0924-46c8-aff1-d19428bfbc8d)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

[**Website**](https://yazimkurallari.turkiyeflorasi.org.tr/) • [**Documentation**](https://yazimkurallari.turkiyeflorasi.org.tr/)

</div>

---

## 📖 About

This repository contains the comprehensive writing and illustration guidelines for the **Illustrated Flora of Türkiye (Resimli Türkiye Florası)** project. It serves as the primary reference for authors, editors, and illustrators contributing to this significant botanical documentation effort.

The guidelines cover all aspects of scientific botanical documentation, from taxonomic writing standards to technical illustration requirements, ensuring consistency and quality across all flora publications.

## ✨ Features

- **📝 Writing Guidelines (Yazım Kuralları)**: Comprehensive botanical writing standards
- **🎨 Illustration Rules (Genel Çizim Kuralları)**: Technical drawing and illustration specifications
- **👥 Author/Illustrator Guide**: Step-by-step workflow for contributors
- **📋 Editorial Board Information**: RTF Editorial Committee guidelines
- **📎 12 Detailed Appendices**: Including nomenclature, keys, descriptions, distributions, and more
- **💰 Financial Guide (Mali Rehber)**: Expense documentation and reimbursement procedures
- **📰 Blog**: Updates and announcements
- **🔍 Full-text Search**: Quick access to any guideline
- **🌓 Dark/Light Mode**: Comfortable reading in any environment
- **📱 Responsive Design**: Access on any device

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/demirogun/ifot-instructions.git
   cd ifot-instructions
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Serve locally**
   ```bash
   mkdocs serve
   ```
   
   The site will be available at `http://127.0.0.1:8000/`

### Building for Production

To build the static site:

```bash
mkdocs build
```

The generated site will be in the `site/` directory.

## 📚 Documentation Structure

```
docs/
├── index.md                          # Homepage
├── yazim_kurallari.md               # Writing rules
├── genel_cizim_kurallari.md         # Illustration rules
├── yazar_ressam_calisma_rehberi.md  # Author/Illustrator guide
├── rtf_editorler_heyeti.md          # Editorial board
├── ekler/                            # Appendices
│   ├── ek1.md                       # Family order
│   ├── ek2.md                       # Nomenclature
│   ├── ek3.md                       # Key examples
│   ├── ek4.md                       # Descriptions
│   ├── ek5.md                       # Terminology
│   ├── ek6.md                       # Distributions
│   ├── ek7.md                       # References
│   ├── ek8.md                       # Abbreviations
│   ├── ek9.md                       # Type notation
│   ├── ek10.md                      # Checklist
│   ├── ek11.md                      # Synonym notation
│   └── ek12.md                      # Turkish names system
└── mali_rehber/                      # Financial guide
    ├── mali_konular.md              # Financial matters
    ├── belgesiz_masraf.md           # Undocumented expenses
    ├── seyahat_onay_belgesi.md      # Travel approval
    └── yurtdisi_belgeli_harcama.md  # International documented expenses
```

## 🛠️ Technology Stack

- **[MkDocs](https://www.mkdocs.org/)**: Static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**: Beautiful documentation theme
- **[Python-Markdown Extensions](https://facelessuser.github.io/pymdown-extensions/)**: Enhanced markdown features
- **[MkDocs Minify Plugin](https://github.com/byrnereese/mkdocs-minify-plugin)**: HTML/CSS/JS minification

## 🎨 Customization

The project uses custom overrides located in `src/overrides/`:

- **Custom styling**: `src/overrides/assets/stylesheets/custom.css`
- **Custom JavaScript**: `src/overrides/assets/javascripts/custom.js`
- **Custom home page**: `src/overrides/home.html`
- **Hooks and extensions**: `src/overrides/hooks/`

## 📝 Contributing

This instructions are for the authors and editors of the Illustrated Flora of Türkiye (Resimli Türkiye Florası) project. Only editors can contribute to this repository.

## 📄 License

This work is licensed under a [Creative Commons Attribution 4.0 International License](LICENSE).

You are free to:
- **Share**: Copy and redistribute the material in any medium or format
- **Adapt**: Remix, transform, and build upon the material for any purpose

Under the following terms:
- **Attribution**: You must give appropriate credit to Ali Nihat Gökyiğit Vakfı

## 🏛️ Organization

**Ali Nihat Gökyiğit Vakfı**

This project is maintained by the Ali Nihat Gökyiğit Foundation, dedicated to advancing botanical research and education in Türkiye.

## 🔗 Links

- **Live Site**: [https://yazimkurallari.turkiyeflorasi.org.tr/](https://yazimkurallari.turkiyeflorasi.org.tr/)
- **Repository**: [https://github.com/demirogun/ifot-instructions](https://github.com/demirogun/ifot-instructions)
- **Issue Tracker**: [GitHub Issues](https://github.com/demirogun/ifot-instructions/issues)

## 📧 Contact

For questions or feedback regarding the guidelines, please open an issue on GitHub or contact the editorial board through the official channels.

---

<div align="center">

**[Documentation](https://yazimkurallari.turkiyeflorasi.org.tr/)** • **[Issues](https://github.com/demirogun/ifot-instructions/issues)** • **[License](LICENSE)**

Copyright © 2025 Ali Nihat Gökyiğit Vakfı

</div>