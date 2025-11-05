#!/usr/bin/env python3
"""
Build Python KACTL in exact KACTL style - HTML that prints to perfect PDF
"""

import os
from datetime import datetime

def escape_html(text):
    """Escape HTML special characters"""
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;'))

def generate_kactl_style_html():
    """Generate HTML that matches KACTL PDF style exactly"""
    
    # Count total algorithms
    total_algos = 0
    for cat_dir in ['combinatorial', 'number_theory', 'data_structures', 
                    'graph', 'strings', 'geometry', 'numerical', 'various']:
        if os.path.exists(cat_dir):
            files = [f for f in os.listdir(cat_dir) 
                    if f.endswith('.py') and f != '__init__.py']
            total_algos += len(files)
    
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Python KACTL</title>
    <style>
        /* KACTL-style formatting for print */
        @page {
            size: A4 landscape;
            margin: 1cm 0.5cm 0.4cm 0.5cm;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Courier New", Courier, monospace;
            font-size: 7.5pt;
            line-height: 1.2;
            column-count: 3;
            column-gap: 15px;
            column-rule: 0.5pt solid #ccc;
            padding: 0;
            background: white;
        }
        
        /* Header on every page */
        @media print {
            body {
                column-count: 3;
            }
            
            .page-header {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: 0.8cm;
                background: white;
                border-bottom: 0.5pt solid black;
                padding: 2pt 0.5cm;
                font-size: 8pt;
                display: flex;
                justify-content: space-between;
                z-index: 1000;
            }
            
            .page-footer {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                height: 0.4cm;
                background: white;
                border-top: 0.5pt solid black;
                text-align: center;
                font-size: 6pt;
                padding: 2pt;
            }
            
            h1, h2 {
                break-after: avoid;
                page-break-after: avoid;
            }
            
            pre {
                break-inside: avoid;
                page-break-inside: avoid;
            }
            
            .algorithm {
                break-inside: avoid;
                page-break-inside: avoid;
            }
        }
        
        h1 {
            font-size: 14pt;
            font-weight: bold;
            margin-top: 8pt;
            margin-bottom: 4pt;
            break-after: avoid;
            column-span: all;
            border-bottom: 1pt solid black;
            padding-bottom: 2pt;
        }
        
        h2 {
            font-size: 10pt;
            font-weight: bold;
            margin-top: 6pt;
            margin-bottom: 3pt;
            break-after: avoid;
        }
        
        .algo-header {
            font-size: 7pt;
            color: #555;
            margin-bottom: 2pt;
        }
        
        .filename {
            font-size: 6.5pt;
            color: #777;
            font-style: italic;
        }
        
        pre {
            font-family: "Courier New", Courier, monospace;
            font-size: 6.5pt;
            line-height: 1.15;
            background: #f8f8f8;
            padding: 3pt;
            margin: 2pt 0 6pt 0;
            border-left: 2pt solid #ddd;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .toc {
            column-span: all;
            margin-bottom: 10pt;
            border-bottom: 1pt solid black;
            padding-bottom: 5pt;
        }
        
        .toc-title {
            font-size: 16pt;
            font-weight: bold;
            text-align: center;
            margin: 5pt 0 8pt 0;
        }
        
        .toc-item {
            font-size: 8pt;
            margin: 1pt 0;
            padding-left: 10pt;
        }
        
        .title-page {
            column-span: all;
            text-align: center;
            margin-bottom: 10pt;
            border-bottom: 2pt solid black;
            padding-bottom: 8pt;
        }
        
        .main-title {
            font-size: 24pt;
            font-weight: bold;
            margin: 5pt 0;
        }
        
        .subtitle {
            font-size: 14pt;
            margin: 3pt 0;
        }
        
        .date {
            font-size: 9pt;
            color: #555;
            margin: 3pt 0;
        }
        
        /* Syntax highlighting */
        .keyword { color: #0000ff; font-weight: bold; }
        .string { color: #a31515; }
        .comment { color: #008000; font-style: italic; }
        .function { color: #795e26; }
        .number { color: #098658; }
    </style>
</head>
<body>
"""
    
    # Title page
    html_content += f"""
    <div class="title-page">
        <div class="main-title">Python KACTL</div>
        <div class="subtitle">KTH Algorithm Competition Template Library</div>
        <div class="subtitle">Python Edition</div>
        <div class="date">{datetime.now().strftime("%B %d, %Y")}</div>
        <div class="date" style="margin-top: 8pt;">{total_algos} Algorithms</div>
    </div>
"""
    
    # Dynamically scan all category directories
    category_dirs = ['combinatorial', 'number_theory', 'data_structures', 
                     'graph', 'strings', 'geometry', 'numerical', 'various']
    
    categories = []
    for cat_dir in category_dirs:
        if os.path.exists(cat_dir):
            # Count actual algorithm files
            files = [f for f in os.listdir(cat_dir) 
                    if f.endswith('.py') and f != '__init__.py']
            if files:
                # Convert directory name to title
                cat_name = cat_dir.replace('_', ' ').title()
                if cat_dir == 'number_theory':
                    cat_name = 'Number Theory'
                elif cat_dir == 'data_structures':
                    cat_name = 'Data Structures'
                elif cat_dir == 'graph':
                    cat_name = 'Graph Algorithms'
                elif cat_dir == 'strings':
                    cat_name = 'String Algorithms'
                elif cat_dir == 'numerical':
                    cat_name = 'Numerical Methods'
                elif cat_dir == 'various':
                    cat_name = 'Various Algorithms'
                categories.append((cat_dir, cat_name))
    
    html_content += """
    <div class="toc">
        <div class="toc-title">Table of Contents</div>
"""
    
    for i, (cat_dir, cat_name) in enumerate(categories, 1):
        html_content += f'        <div class="toc-item">{i}. {cat_name}</div>\n'
    
    html_content += "    </div>\n\n"
    
    # Generate content for each category
    for cat_dir, cat_name in categories:
        html_content += f'    <h1>{cat_name}</h1>\n\n'
        
        category_path = cat_dir
        if not os.path.exists(category_path):
            continue
        
        files = sorted([f for f in os.listdir(category_path) 
                       if f.endswith('.py') and f != '__init__.py'])
        
        for filename in files:
            filepath = os.path.join(category_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Algorithm name from filename
                algo_name = filename[:-3].replace('_', ' ').title()
                
                # Extract docstring
                description = ""
                time_complexity = ""
                if '"""' in content:
                    parts = content.split('"""')
                    if len(parts) >= 3:
                        doc = parts[1].strip()
                        for line in doc.split('\n'):
                            line = line.strip()
                            if 'Description:' in line:
                                description = line.replace('Description:', '').strip()
                            elif 'Time:' in line or 'Time complexity:' in line:
                                time_complexity = line.replace('Time:', '').replace('Time complexity:', '').strip()
                
                # Algorithm section
                html_content += f'    <div class="algorithm">\n'
                html_content += f'        <h2>{algo_name}</h2>\n'
                
                if description:
                    html_content += f'        <div class="algo-header">{escape_html(description[:150])}</div>\n'
                if time_complexity:
                    html_content += f'        <div class="algo-header">Time: {escape_html(time_complexity)}</div>\n'
                
                html_content += f'        <div class="filename">{cat_dir}/{filename}</div>\n'
                
                # Code with basic syntax highlighting
                html_content += '        <pre>'
                
                lines = content.split('\n')
                # Limit to reasonable length
                max_lines = 60
                code_lines = lines[:max_lines] if len(lines) > max_lines else lines
                
                for line in code_lines:
                    # Very basic syntax highlighting
                    escaped_line = escape_html(line)
                    
                    # Keywords
                    for keyword in ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 
                                   'return', 'import', 'from', 'try', 'except', 'with',
                                   'yield', 'lambda', 'and', 'or', 'not', 'in', 'is']:
                        escaped_line = escaped_line.replace(f' {keyword} ', f' <span class="keyword">{keyword}</span> ')
                        if escaped_line.startswith(f'{keyword} '):
                            escaped_line = f'<span class="keyword">{keyword}</span> ' + escaped_line[len(keyword)+1:]
                    
                    # Comments
                    if '#' in escaped_line:
                        parts = escaped_line.split('#', 1)
                        escaped_line = parts[0] + '<span class="comment">#' + parts[1] + '</span>'
                    
                    html_content += escaped_line + '\n'
                
                if len(lines) > max_lines:
                    html_content += '<span class="comment"># ... (continued)</span>\n'
                
                html_content += '</pre>\n'
                html_content += '    </div>\n\n'
                
            except Exception as e:
                print(f"Warning: Could not process {filepath}: {e}")
    
    html_content += """
</body>
</html>
"""
    
    return html_content

def main():
    """Main function"""
    print("=" * 70)
    print("Python KACTL Builder - KACTL-Style HTML for PDF")
    print("=" * 70)
    
    print("\n📝 Generating KACTL-style HTML...")
    html_content = generate_kactl_style_html()
    
    output_file = 'PYTHON_KACTL_PRINT.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    size = os.path.getsize(output_file)
    print(f"✅ Created: {output_file} ({size/1024:.1f} KB)")
    
    # Count algorithms
    total_algos = 0
    for cat_dir in ['combinatorial', 'number_theory', 'data_structures', 
                    'graph', 'strings', 'geometry', 'numerical', 'various']:
        if os.path.exists(cat_dir):
            files = [f for f in os.listdir(cat_dir) 
                    if f.endswith('.py') and f != '__init__.py']
            total_algos += len(files)
    
    print(f"\n📊 Total algorithms included: {total_algos}")
    print("\n" + "=" * 70)
    print("📄 TO CREATE PDF:")
    print("=" * 70)
    print(f"1. Open {output_file} in your browser")
    print("2. Press Cmd+P (or File → Print)")
    print("3. Select 'Save as PDF'")
    print("4. Save as 'python_kactl.pdf'")
    print("\nThe HTML is styled to print perfectly in 3-column A4 landscape")
    print("matching the original KACTL format!")
    print("=" * 70)

if __name__ == "__main__":
    main()

