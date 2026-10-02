---
id: software.testes.tranche10.000396
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://vitest.dev/guide/projects", "https://vitest.dev/guide/coverage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: separar configuração raiz e configuração de cada projeto

## Em uma frase
Vitest Projects permite agrupar conjuntos de testes com opções próprias; projetos inline podem herdar configuração conforme extends.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Esperar que toda opção configurada dentro de um projeto tenha efeito pode produzir cobertura ou reporters duplicados e inesperados.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Defina opções globais no root e nomeie projetos por ambiente ou finalidade, usando extends true/false deliberadamente.

## Exemplo
Um workspace roda unit no Node e componentes em happy-dom, enquanto reporter e coverage permanecem na configuração raiz.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Algumas opções são explicitamente root-only e projetos não transformam automaticamente a configuração raiz em um projeto de teste.

## Como verificar
Examine a saída por projeto e confirme quais arquivos e opções foram realmente selecionados em cada ambiente.

## Conexões
- [[vitest-browser-mode-spy-namespace]] — Veja também: Vitest Browser Mode: distinguir spy de substituição de export ESM.
- [[vitest-isolation-parallelism-tradeoff]] — Veja também: Vitest: avaliar custo antes de desativar isolamento.

## Fontes
- [Vitest — Test projects](https://vitest.dev/guide/projects) — configuração, herança e opções globais de projetos; consultado em 2026-10-02.
- [Vitest — Coverage](https://vitest.dev/guide/coverage) — providers e opções de relatório de cobertura; consultado em 2026-10-02.
