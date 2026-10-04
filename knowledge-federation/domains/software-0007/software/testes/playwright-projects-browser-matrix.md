---
id: software.testes.tranche12.000550
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/test-projects", "https://playwright.dev/docs/test-configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: projetos para uma matriz de browsers

## Em uma frase
Um projeto nomeado combina os testes com opções de execução, como browser, dispositivo ou ambiente.

## Por que importa
Uma matriz explícita expõe diferenças entre engines sem copiar a mesma especificação em vários diretórios e torna a intenção de cada job visível no relatório.

## Como funciona
Declare cada entrada em `projects`, configure seu `name` e o bloco `use`, e limite cada projeto aos alvos que o produto realmente suporta. Para reproduzir uma falha, execute apenas o projeto indicado em vez de percorrer toda a matriz.

## Exemplo
Dois projetos podem apontar para os mesmos arquivos e usar configurações `use` diferentes; a saída separa o resultado por nome sem exigir duas implementações do cenário.

## Limites e trade-offs
Adicionar combinações aumenta a duração e pode exigir snapshots ou expectativas específicas por plataforma. Projetos de browser não substituem validação em versões ou sistemas operacionais ausentes da matriz.

## Como verificar
Rode um teste conhecido em dois projetos e confirme que cada execução reporta o browser e o identificador esperados antes de ampliar a matriz.

## Conexões
- [[playwright-project-dependencies-setup]] — Veja também: Playwright Test: setup como dependência de projeto.

## Fontes
- [Playwright — Projects](https://playwright.dev/docs/test-projects) — projetos por browser/dispositivo/ambiente, dependências, teardown e parametrização; consultado em 2026-10-02.
- [Playwright — Test configuration](https://playwright.dev/docs/test-configuration) — configuração de testDir, projetos, expect, retries, workers e artefatos; consultado em 2026-10-02.
