---
id: software.testes.tranche23.001747
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://infection.github.io/guide/command-line-options.html", "https://infection.github.io/guide/installation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Loggers nativos de PR: GitHub annotations, GitLab code quality, HTML e JSON

## Em uma frase
A doc oficial de opções descreve quatro saídas integráveis: --logger-github, que imprime GitHub Annotation warnings para mutantes escapados direto no pull request — com detecção automática do ambiente GitHub Actions, forçamento por =true/=false e o link do próprio workflow de exemplo do projeto — ; --logger-gitlab, que grava um Code Quality report (Code Climate) em arquivo json, consumível como artifact; --logger-html, que gera um relatório HTML navegável com exemplo hospedado no site; e --logger-text, que aceita caminhos físicos e também php://stdout, php://stderr e php://output para pipelines que capturam buffer.

## Por que importa
O mecanismo de path raiz é detalhado com cuidado: os relatórios GitHub/GitLab substituem caminhos locais pelo root do repositório detectando automaticamente GITHUB_WORKSPACE e CI_PROJECT_DIR, respectivamente, com --logger-project-root-directory para casos custom (Docker com caminho fora) e o fallback documentado git rev-parse --show-toplevel quando nenhuma variável existe.

## Como funciona
A hierarquia de precedência entre CLI e configuração está gravada nas três seções: as opções de logger na linha de comando têm precedência sobre os correspondentes no infection.json5, e a própria doc sugere que quem quer relatório sempre é para configurar no arquivo, não no flag.

## Exemplo
Num PR de exemplo, rode com --logger-github e --git-diff-filter=A; abra a aba Files e confirme as annotations nos mutantes escapados — é o produto que a página descreve, antes de qualquer relatório externo.

## Limites e trade-offs
A página GitLab anota que o link de visualização no diff do merge request é um recurso pago do tier (não disponível no free tier, com link para a doc do GitLab que o tier define); a annotation em si é gratuita, a experiência completa no diff não.

## Como verificar
Abra as seções --logger-github, --logger-gitlab, --logger-html e --logger-text da página Command line options; confirme as frases de auto-deteção, precedência e o exemplo do workflow próprio.

## Conexões
- [[infection-git-diff]] — Veja também: Mutar só a diferença do pull request: --git-diff-filter e --git-diff-lines.
- [[infection-mutators]] — Veja também: Mutators: famílias AST, o describe e o --id para matar um de cada vez.

## Fontes
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
- [Infection — Installation](https://infection.github.io/guide/installation.html) — phar assinado, phive, composer, brew e tabela de compatibilidade; consultado em 2026-10-03.
