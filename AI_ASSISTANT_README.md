# AI Assistant Guide for TidiFul Website

## 🎯 Project Overview
This is the TidiFul website - an AI-powered document processing platform that converts invoices, PDFs, and images to structured data formats (Excel, CSV, JSON). The site includes a comprehensive blog system with automated SEO optimization.

## 📁 Key Project Structure
```
tidiful-website/
├── index.html                    # Main homepage
├── blog/                         # Blog system
│   ├── blogs.html               # Blog index page
│   ├── posts/                   # Individual blog posts
│   │   ├── manifest.json        # Auto-generated post index
│   │   └── *.html               # Blog post files
│   └── static/                  # SEO-optimized static versions
├── assets/                       # Static assets
│   ├── images/                  # Logo, icons, etc.
│   ├── js/                      # JavaScript files
│   └── i18n/                    # Internationalization files
├── sitemap.xml                   # SEO sitemap
└── blog_automation.py           # Blog management system
```

## 🚀 Essential Commands

### Starting the Development Server
```bash
# Check for existing servers on port 8000
lsof -i :8000

# Kill existing server if needed
kill [PID]

# Start Python HTTP server
python3 -m http.server 8000
```

### Blog Management
```bash
# Create new blog post
python3 create_blog_post.py "Your Blog Post Title"

# Run full blog automation (updates sitemap, generates static files)
python3 blog_automation.py --action full

# Other automation actions
python3 blog_automation.py --action manifest    # Generate manifest only
python3 blog_automation.py --action static      # Generate static files only
python3 blog_automation.py --action update      # Update blogs.html and sitemap
python3 blog_automation.py --action discover    # List all posts
```

## 📝 Blog Post Creation Standards

### Required SEO Elements
Every blog post MUST include:

1. **Meta Tags**
   - `title`: "[Post Title] | TidiFul"
   - `description`: Compelling, keyword-rich description (150-160 chars)
   - `keywords`: Relevant keywords separated by commas
   - `excerpt`: Detailed excerpt for blog listings
   - `canonical`: Full URL to the post

2. **Open Graph & Twitter Cards**
   - Complete og:title, og:description, og:image
   - Twitter card with summary_large_image
   - Proper image alt text

3. **Structured Data (Schema.org)**
   - Article schema with author, publisher, dates
   - FAQ schema with 3+ relevant questions
   - Organization schema for TidiFul

4. **Hreflang Tags**
   - Support for en, fr, de, es, el languages
   - x-default fallback

5. **Internal Linking**
   - Link to other blog posts contextually
   - Link to TidiFul homepage and features
   - Use blue-400 hover:text-blue-300 styling for internal links

### Content Structure Template
Follow the **image-to-excel-complete-guide.html** model:

```html
<!-- Blue info box at top -->
<div class="bg-blue-900/20 border border-blue-500/30 rounded-lg p-6 mb-8">
    <p class="text-lg text-gray-200 mb-4">
        Hundreds of businesses use <a href="../../index.html" class="text-blue-400 hover:text-blue-300 font-semibold">TidiFul</a> every day...
    </p>
    <p class="text-gray-300">
        If you're also interested in <a href="other-post.html" class="text-blue-400 hover:text-blue-300">related topic</a>...
    </p>
</div>

<!-- CTA box -->
<div class="bg-emerald-900/20 border border-emerald-500/30 rounded-lg p-6 my-8">
    <h3 class="text-emerald-400 font-semibold mb-3">🚀 Try TidiFul Free</h3>
    <p class="text-gray-300 mb-4">Description...</p>
    <a href="../../index.html" class="inline-block px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-medium rounded-lg transition-colors">
        Try TidiFul Free
    </a>
    <p class="text-sm text-gray-400 mt-2">No credit card required.</p>
</div>

<!-- Table of Contents -->
<div class="bg-gray-800 rounded-lg p-6 mb-8">
    <h2 class="text-2xl font-bold text-gray-100 mb-4">📋 Table of Contents</h2>
    <ul class="space-y-2 text-gray-300">
        <li><a href="#section1" class="text-blue-400 hover:text-blue-300">Section 1</a></li>
        <!-- More sections -->
    </ul>
</div>

<!-- Main content with section IDs -->
<h2 id="section1" class="text-3xl font-bold text-gray-100 mb-6">Section Title</h2>
<div class="bg-gray-800 rounded-lg p-6 mb-8">
    <!-- Content -->
</div>

<!-- Related Articles section -->
<h2>Related Articles</h2>
<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
    <a href="other-post.html" class="block bg-gray-800 rounded-lg p-6 hover:bg-gray-700 transition-colors">
        <h4 class="text-lg font-semibold text-gray-100 mb-2">Post Title</h4>
        <p class="text-gray-400 text-sm">Description...</p>
    </a>
    <!-- More related articles -->
</div>
```

## 🔗 Internal Linking Strategy

### Existing Blog Posts (Always Link To These)
1. **invoice-to-excel-complete-guide.html** - Invoice processing workflows
2. **pdf-to-csv-complete-guide.html** - PDF conversion methods
3. **image-to-excel-complete-guide.html** - Image data extraction
4. **how-to-scan-pdf-documents-like-a-pro-a-complete-guide-for-business-professionals.html** - Document scanning
5. **what-is-pdf-to-csv-conversion.html** - PDF to CSV fundamentals

### Linking Best Practices
- **Contextual Integration**: Links should feel natural within the content
- **Multiple CTAs**: Include CTAs throughout the article
- **Workflow Pipeline**: Show how different processes connect
- **Related Articles Grid**: Card-style links at the end
- **Blue Styling**: Use `text-blue-400 hover:text-blue-300` for internal links

## 🎨 Styling Guidelines

### Color Scheme
- **Primary Green**: `#10b981` (emerald-500)
- **Secondary Blue**: `#06b6d4` (cyan-500)
- **Background**: Dark theme with gray-900/gray-800
- **Text**: gray-100 for headings, gray-300 for body

### Component Classes
- **Info Boxes**: `bg-blue-900/20 border border-blue-500/30`
- **CTA Boxes**: `bg-emerald-900/20 border border-emerald-500/30`
- **Content Boxes**: `bg-gray-800 rounded-lg p-6`
- **Internal Links**: `text-blue-400 hover:text-blue-300`

## 📊 SEO Requirements

### Keyword Targeting
- Primary keywords in title, H1, first paragraph
- Secondary keywords in H2s and throughout content
- Long-tail keywords in natural context
- Brand mentions (TidiFul) throughout

### Content Quality
- **Minimum 2000 words** for comprehensive guides
- **Proper heading hierarchy** (H1 → H2 → H3)
- **Bullet points and numbered lists** for readability
- **Tables** for comparison data
- **Call-to-actions** every 300-400 words

### Technical SEO
- **Mobile-responsive** design
- **Fast loading** (optimize images)
- **Clean URLs** (descriptive filenames)
- **Internal linking** (5+ contextual links)
- **External linking** (authority sources when relevant)

## 🔄 Workflow Process

### Creating a New Blog Post
1. **Create Post**: `python3 create_blog_post.py "Title"`
2. **Edit Content**: Follow the template structure
3. **Add Internal Links**: Link to existing posts contextually
4. **Run Automation**: `python3 blog_automation.py --action full`
5. **Test**: Check the post at `http://localhost:8000/blog/posts/[filename]`

### Updating Existing Posts
1. **Edit the post** in `blog/posts/`
2. **Run automation** to update static files and sitemap
3. **Test changes** on the development server

## 🎯 Content Guidelines

### Tone & Voice
- **Professional but approachable**
- **Solution-focused** (problems → solutions)
- **TidiFul-centric** (always tie back to the platform)
- **Action-oriented** (clear next steps)

### Content Types
- **How-to guides** (step-by-step processes)
- **Complete guides** (comprehensive coverage)
- **Best practices** (industry insights)
- **Tool comparisons** (feature breakdowns)

### Target Audience
- **Business professionals**
- **Finance teams**
- **Document processing managers**
- **Small to medium businesses**

## 🚨 Common Issues & Solutions

### Server Issues
- **Port 8000 in use**: Check `lsof -i :8000` and kill process
- **404 errors**: Ensure files exist and paths are correct
- **Missing assets**: Check file paths in HTML

### Blog Automation Issues
- **Python not found**: Use `python3` instead of `python`
- **Missing dependencies**: Install required packages
- **Sitemap not updating**: Run full automation after changes

### SEO Issues
- **Missing meta tags**: Follow the template structure
- **Broken internal links**: Check file paths and names
- **Duplicate content**: Ensure unique titles and descriptions

## 📈 Success Metrics

### SEO Goals
- **Keyword rankings** for target terms
- **Organic traffic** growth
- **Internal link equity** distribution
- **User engagement** (time on page, bounce rate)

### Content Goals
- **Comprehensive coverage** of topics
- **Clear user pathways** between related content
- **Strong CTAs** leading to TidiFul signup
- **Professional presentation** that builds trust

## 🔧 Quick Reference

### File Locations
- **Main blog posts**: `blog/posts/`
- **Static versions**: `blog/static/`
- **Blog index**: `blog/blogs.html`
- **Sitemap**: `sitemap.xml`
- **Manifest**: `blog/posts/manifest.json`

### Key URLs
- **Homepage**: `http://localhost:8000/index.html`
- **Blog index**: `http://localhost:8000/blog/blogs.html`
- **Individual posts**: `http://localhost:8000/blog/posts/[filename]`

### Automation Commands
- **Full update**: `python3 blog_automation.py --action full`
- **Create post**: `python3 create_blog_post.py "Title"`
- **Start server**: `python3 -m http.server 8000`

---

**Remember**: Always follow the image-to-excel-complete-guide.html model for structure and internal linking. This ensures consistency and optimal SEO performance across all blog posts.
