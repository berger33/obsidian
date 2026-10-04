---
id: software.testes.tranche25.001864
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

# Integração com Cucumber: cucumber-rails, within e a tag @javascript

## Em uma frase
Na seção Using Capybara with Cucumber, o README explica que a gem cucumber-rails já traz suporte ao Capybara embutido (fora do Rails, carrega-se require 'capybara/cucumber' e define-se Capybara.app = MyRackApp); os steps usam a DSL diretamente (como within("#session"), fill_in e click_button), e a tag @javascript troca o driver do cenário para Capybara.javascript_driver (:selenium por padrão), além de existirem tags explícitas para cada driver registrado (@selenium, @rack_test).

## Por que importa
Em projetos BDD, a maioria dos cenários não precisa do custo de abrir um navegador completo; controlar o driver por tag Gherkin permite manter a suíte padrão em Rack::Test e reservar o navegador real apenas para os fluxos que acionam Ajax ou DOM dinâmico.

## Como funciona
Escreva os step definitions usando within, fill_in e click_button, mantenha os cenários comuns sem tag de driver e anote com @javascript (ou @selenium) apenas os cenários que dependem de execução de scripts no cliente.

## Exemplo
O exemplo oficial encapsula os campos dentro de within("#session") { fill_in 'Email', with: 'user@example.com'; fill_in 'Password', with: 'password' } antes de chamar click_button 'Sign in'.

## Limites e trade-offs
Taggear toda uma feature com @javascript aplica o driver de navegador a todos os cenários daquele arquivo; se apenas um cenário usa Ajax, aplique a tag somente nele para não desacelerar o restante.

## Como verificar
Conferi a seção Using Capybara with Cucumber do README oficial.

## Conexões
- [[capybara-puma-server]] — Veja também: Configuração do servidor Puma e o modo Silent no Rails 5.0+.
- [[capybara-rspec-feature-system]] — Veja também: Integração com RSpec 3.5+: spec/features, spec/system e metadados type.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
