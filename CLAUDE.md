# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **MkDocs-based documentation site** for CyberSecAI - a comprehensive guide covering AI applications in cybersecurity. The site is published as a GitHub Pages site at https://cybersecai.github.io/.

## Architecture

### Content Structure
- **docs/** - All documentation content in Markdown format
- **docs/assets/images/** - Image assets for documentation
- **docs/overrides/** - MkDocs Material theme customizations
- **docs/includes/** - Reusable content snippets and abbreviations
- **mkdocs.yml** - Main site configuration with navigation structure

### Key Content Areas
- **Introduction** - AI fundamentals for cybersecurity
- **NotebookLM** - Google's NotebookLM for vulnerability analysis
- **CWE Assignment** - Common Weakness Enumeration analysis tools
- **Context Engineering** - Prompt engineering and Fabric integration
- **Software Engineering** - AI agents for software development and security
- **CyberSecurity Models** - Specialized AI models for security tasks

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv Guide
source Guide/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Local Development
```bash
# Serve site locally for development
mkdocs serve

# Serve on specific IP/port
mkdocs serve -a 127.0.0.1:8001
```

### Building and Deployment
```bash
# Build static site
mkdocs build

# Deploy to GitHub Pages (gh-pages branch)
mkdocs gh-deploy --force

# Push source changes to main branch
git push -u origin main
```

### Maintenance
```bash
# Check for broken links
./checklinks.sh

# Split large PDFs (utility script)
./pdfsplit.sh
```

## MkDocs Configuration

The site uses **MkDocs Material** theme with the following key features:
- Mermaid diagram support
- Print-to-PDF functionality
- Search with highlighting
- Dark/light theme toggle
- Google Analytics integration
- Social media links

### Extensions in Use
- **pymdownx.snippets** - Include external content
- **pymdownx.superfences** - Advanced code blocks and Mermaid
- **pymdownx.highlight** - Syntax highlighting
- **markdown_include.include** - File inclusion
- **admonition** - Callout boxes

## Content Guidelines

### Admonitions Format
Use descriptive text for all admonitions:
```markdown
!!! abstract "Overview"
!!! success "Takeaways"
!!! info "Key Information"
```

### Image Optimization
- Optimize image sizes and formats for web performance
- Store images in `docs/assets/images/`
- Use descriptive filenames

### File Organization
- Follow the navigation structure defined in `mkdocs.yml`
- Use meaningful directory names that match content topics
- Keep related content grouped together

## Publishing Workflow

1. **Edit content** in `docs/` directory
2. **Test locally** with `mkdocs serve`
3. **Build and deploy** with `mkdocs gh-deploy --force`
4. **Push source** with `git push -u origin main`

The site automatically publishes to GitHub Pages from the `gh-pages` branch (not `main`).