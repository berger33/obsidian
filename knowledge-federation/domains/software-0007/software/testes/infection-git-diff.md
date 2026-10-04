---
id: software.testes.tranche23.001746
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

# Mutar só a diferença do pull request: --git-diff-filter e --git-diff-lines

## Em uma frase
A doc oficial das opções documenta o recorte por git como o modo CI de primeira classe: --git-diff-filter aplica git diff com --diff-filter para filtrar os arquivos a mutar, com os valores sensatos AM (adicionados e modificados) e A (só adicionados), e a página prescreve o par com o fetch raso do base branch (git fetch --depth=1 origin $GITHUB_BASE_REF) no GitHub Actions antes de rodar infection.phar --git-diff-filter=A.

## Por que importa
A semântica do diff: a comparação é entre o branch atual e um ancestral comum dele com o base branch — e quando não existe ancestral comum (checkout raso, branches não relacionados), o Infection cai para um diff direto entre branches, fallback documentado na página.

## Como funciona
O refinamento por linha vem com --git-diff-lines, que muta apenas as linhas tocadas — comparando com master por default (a base trocável com --git-diff-base=main) — e a página argumenta o duplo benefício: verificar o impacto no MSI de uma feature branch sem escrever teste para o arquivo legado inteiro, com menos mutantes gerados e mais performance; --git-diff-base é declarada para uso só com o filter.

## Exemplo
A mesma seção oferece a inspeção do recorte: infection config:list-sources mostra o resultado do filtro aplicado, e os comandos infection list git expõem o debug dos valores git usados — antes de abrir um PR verde, confira que o set de fontes bate com o diff do PR.

## Limites e trade-offs
A doc recomenda o modo para builds de pull request, não como substituto da mutação completa: o que não foi tocado permanece sem mutantes, e a página de --git-diff-lines descreve o motivo de performance como trade-off assumido, não como solução permanente.

## Como verificar
Abra as seções --git-diff-filter, --git-diff-base e --git-diff-lines da página Command line options e confirme o bloco do fetch, a frase do fallback e as opções de list-sources.

## Conexões
- [[infection-reuse-coverage]] — Veja também: Reusar cobertura existente em vez de gerar de novo.
- [[infection-loggers]] — Veja também: Loggers nativos de PR: GitHub annotations, GitLab code quality, HTML e JSON.

## Fontes
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
- [Infection — Installation](https://infection.github.io/guide/installation.html) — phar assinado, phive, composer, brew e tabela de compatibilidade; consultado em 2026-10-03.
