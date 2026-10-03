---
id: software.testes.tranche25.001869
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md", "https://github.com/teamcapybara/capybara"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Arquitetura do guia oficial: seletores, exactness, sessões nomeadas e canal de suporte

## Em uma frase
O índice e o cabeçalho do README oficial mapeiam os tópicos centrais da ferramenta — Drivers (RackTest, Selenium), The DSL (Navigating, Clicking, Forms, Querying, Finding, Scoping, Windows, Scripting, Modals, Debugging), Selectors (Name, Locator, Filters), Matching (Exactness, Strategy), Transactions and database setup, Asynchronous JavaScript, Named sessions, a armadilha "Beware the XPath // trap" e o modo "Threadsafe" — além de orientar que pedidos de ajuda sejam feitos em GitHub Discussions (categoria Q&A) em vez de abrir issues, com patrocínio via Patreon.

## Por que importa
Conhecer o mapa de recursos evita reimplementar na mão o que o Capybara já modela: múltiplas sessões simultâneas (Named sessions) para testar chat entre dois usuários, controle de exatidão de matching e cuidados com XPath // em escopos aninhados.

## Como funciona
Ao enfrentar problemas de concorrência com banco em testes JS, seletores XPath que escapam do escopo ou necessidade de dois usuários logados ao mesmo tempo, consulte as seções dedicadas do README (Transactions, Beware the XPath // trap, Named sessions) e use o GitHub Discussions para dúvidas de uso.

## Exemplo
Para simular dois usuários interagindo na mesma funcionalidade, o recurso documentado no índice é Using sessions / Named sessions, sem precisar instanciar servidores paralelos manualmente.

## Limites e trade-offs
O aviso no topo do README é explícito ("Need help? Ask on the discussions (please do not open an issue)"): o issue tracker é reservado para defeitos reproduzíveis da biblioteca, não para suporte de configuração.

## Como verificar
Conferi o cabeçalho de suporte/Patreon e o Table of contents completo do README oficial.

## Conexões
- [[capybara-dsl-scoping-and-matchers]] — Veja também: Navegação, escopo com within, formulários e matchers em view specs.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
