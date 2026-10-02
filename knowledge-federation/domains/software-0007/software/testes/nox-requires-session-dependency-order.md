---
id: software.testes.tranche14.000825
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://nox.thea.codes/en/stable/tutorial.html", "https://nox.thea.codes/en/stable/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: declarar dependências entre sessões com requires

## Em uma frase
`requires` permite que uma sessão dependa de outras, cuja ordem de execução Nox resolve de forma estável e topológica.

## Por que importa
Dependências explícitas evitam confiar na posição textual do noxfile ou numa invocação manual fora de ordem.

## Como funciona
Declare pré-requisitos por nome de sessão e use parametrização compatível quando a dependência também variar por versão.

## Exemplo
Uma sessão de cobertura requer as sessões de teste da matriz antes de combinar arquivos e calcular o relatório.

## Limites e trade-offs
Dependência implícita em artefatos locais ainda pode deixar conteúdo obsoleto; certifique-se de limpar ou identificar resultados por execução.

## Como verificar
Rode a sessão dependente isoladamente e confira a sequência de tarefas e os artefatos produzidos por cada etapa.

## Conexões
- [[nox-default-session-surface]] — Veja também: Nox: tirar tarefas auxiliares da execução padrão.
- [[nox-tag-filtered-ci-selection]] — Veja também: Nox: selecionar sessões por tags em jobs especializados.

## Fontes
- [Nox — Tutorial](https://nox.thea.codes/en/stable/tutorial.html) — sessões requeridas, parametrização e execução de tarefas dependentes; consultado em 2026-10-02.
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
