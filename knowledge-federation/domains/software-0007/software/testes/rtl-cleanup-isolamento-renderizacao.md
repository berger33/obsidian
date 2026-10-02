---
id: software.testes.tranche08.000169
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://testing-library.com/docs/react-testing-library/setup/", "https://testing-library.com/docs/react-testing-library/intro/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testing Library: limpeza e isolamento entre renders

## Em uma frase
Garanta que cada teste comece com DOM e mocks previsíveis e que um render não influencie assertions do próximo.

## Por que importa
DOM residual, mock não restaurado ou singleton com estado compartilhado podem produzir falsos positivos dependentes da ordem.

## Como funciona
Siga a configuração de cleanup do ambiente, restaure mocks e crie estado de aplicação por teste. Use beforeEach para reset claro, não para carregar cenário oculto.

## Exemplo
Uma suíte renderiza uma tela autenticada e depois uma pública; o segundo teste cria store e DOM novos e não herda o usuário do primeiro.

## Limites e trade-offs
Cleanup do DOM não limpa automaticamente timers, local storage, módulos singleton ou estado de servidor; cada fronteira exige política própria.

## Como verificar
Execute testes em ordem inversa e isolados. Inspecione timers pendentes, spies e armazenamento após cada caso e force uma falha para checar teardown.

## Conexões
- [[playwright-fixture-ciclo-vida-isolamento]] — Veja também: Playwright: ciclo de vida de fixtures por teste.
- [[playwright-teardown-recursos-externos]] — Veja também: Playwright: teardown confiável de recursos externos.

## Fontes
- [Testing Library — Setup](https://testing-library.com/docs/react-testing-library/setup/) — render customizado e provedores de contexto; consultado em 2026-10-02.
- [Testing Library — React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) — orientação por DOM e comportamento percebido pelo usuário; consultado em 2026-10-02.
