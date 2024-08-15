!!! abstract
    记录一些使用mkdocs过程中遇到的解决方案
??? note "如何在mkdocs中使用有色的数学公式"
    MathJax 本身支持使用 \color 命令来更改公式的颜色，但在 MkDocs 中你需要确保正确配置 MathJax:

    1.在 mkdocs.yml 文件中，启用 MathJax 并自定义配置：
    ```yaml
    markdown_extensions:
    - pymdownx.superfences
    - pymdownx.highlight
    - pymdownx.arithmatex

    extra_javascript:
    - http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default
    ```
    2.在 Markdown 文件中直接使用 LaTeX \color 命令来设置颜色：(两者均可)
    ```markdown
    $$ \color{red}{\alpha + \beta = \gamma} $$
    \( \color{red}{\alpha + \beta = \gamma} \)
    ```
    3.效果：
    $$ \color{red}{\alpha + \beta = \gamma} $$