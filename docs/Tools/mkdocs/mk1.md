!!! abstract
    记录一些使用mkdocs过程中遇到的解决方案
??? note "如何在mkdocs中使用有色的数学公式(字体与背景)"
    ??? success "使用 MathJax 命令 \color \bbox"
        MathJax 本身支持使用 \color 命令更改公式的字体颜色，用 \bbox 命令更改公式的背景颜色，但在 MkDocs 中你需要确保正确配置 MathJax:
        1.在 mkdocs.yml 文件中，启用 MathJax 并自定义配置：
        ```yaml
        markdown_extensions:
        - pymdownx.superfences
        - pymdownx.highlight
        - pymdownx.arithmatex
          - generic: true
        extra_javascript:
        - _js/mathjax.js  #配置方法见https://squidfunk.github.io/mkdocs-material/reference/math/
        - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
        - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
        - https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML
        - http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default
        ```
        2.在 Markdown 文件中使用 \color 和 \bbox 命令来设置颜色:
        ```markdown
        $$ \color{red}{\alpha + \beta = \gamma} $$
        $$ \bbox[yellow]{\color{red}{\alpha + \beta = \gamma}} $$
        $$ \bbox[border: 2px solid green; background: yellow]{\color{red}{\alpha + \beta = \gamma}} $$
        ```
        3.效果：
        $$ \color{red}{\alpha + \beta = \gamma} $$
        $$ \bbox[yellow]{\color{red}{\alpha + \beta = \gamma}} $$
        $$ \bbox[border: 2px solid green; background: yellow]{\color{red}{\alpha + \beta = \gamma}} $$
    ??? success "所有公式统一颜色"
        1.创建并编辑自定义 CSS 文件：在 docs/_css/extra.css 中添加以下内容来更改 LaTeX 公式的颜色。
        ```css
        /* 更改行内公式的颜色 */
        .md-typeset .math.inline {
            color: red;
            background-color: lightgrey
        }
        /* 更改块级公式的颜色 */
        .md-typeset .math.display {
            color: blue;
            background-color: lightgrey
        }
        ```
        2.更新 mkdocs.yml 配置文件：将 extra.css 文件添加到 extra_css 列表中：
        ```yaml
        extra_css:
        - _css/extra.css  # 确保路径正确
        ```
        3.构建和预览：保存更改后，重新构建你的 MkDocs 站点，并预览结果以确保颜色设置正确  
        PS:如果你有特定的颜色需求，可以使用其他颜色值，如 #ff0000（红色）。