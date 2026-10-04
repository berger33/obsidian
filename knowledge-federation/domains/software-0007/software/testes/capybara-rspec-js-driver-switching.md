---
id: software.testes.tranche25.001866
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

# Seleção de driver no RSpec com js: true e driver: :selenium

## Em uma frase
Ainda na seção de RSpec, o README mostra como alternar drivers por grupo ou por exemplo: adicionar js: true ativa o Capybara.javascript_driver (:selenium por padrão), enquanto passar driver: :selenium (ou outro símbolo registrado) força um driver específico naquele it ou describe.

## Por que importa
Um mesmo grupo de testes pode conter exemplos que exigem o driver JavaScript padrão da suíte e um exemplo puntual que precisa de um driver específico (por exemplo, um browser não-headless para inspecionar um comportamento); os metadados do RSpec resolvem isso declarativamente.

## Como funciona
Marque o bloco describe com js: true quando todos os exemplos internos precisarem de JavaScript e sobrescreva com driver: :nome_do_driver no it individual que exigir um backend distinto.

## Exemplo
O trecho oficial combina os dois níveis: describe 'some stuff which requires js', js: true do com um it usando o driver JS padrão e outro it 'will switch to one specific driver', driver: :selenium.

## Limites e trade-offs
Esquecer que js: true aponta para Capybara.javascript_driver pode surpreender quando alguém altera o javascript_driver global no helper; use driver: explícito quando o teste depender de um navegador específico.

## Como verificar
Conferi o bloco sobre js: true e :driver na seção Using Capybara with RSpec do README oficial.

## Conexões
- [[capybara-rspec-feature-system]] — Veja também: Integração com RSpec 3.5+: spec/features, spec/system e metadados type.
- [[capybara-acceptance-dsl-aliases]] — Veja também: A DSL de aceitação embutida: feature, background, scenario e given.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
