---
id: software.testes.tranche25.001865
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

# Integração com RSpec 3.5+: spec/features, spec/system e metadados type

## Em uma frase
A seção Using Capybara with RSpec documenta que o suporte a RSpec 3.5+ é ativado com require 'capybara/rspec' (tipicamente no spec_helper.rb); em projetos Rails os arquivos ficam em spec/features ou spec/system, e fora desses diretórios (ou fora do Rails) os grupos describe precisam ser marcados com type: :feature ou type: :system.

## Por que importa
O RSpec só injeta a DSL do Capybara (visit, fill_in, click_button, have_content) nos grupos de exemplos cujo tipo é reconhecido; saber a convenção de diretórios e de metadados evita erros de NoMethodError para visit ao organizar suítes em pastas customizadas.

## Como funciona
Adicione require 'capybara/rspec' ao helper, posicione os testes em spec/features ou spec/system no Rails, ou passe explicitamente type: :feature no bloco describe quando a suíte não seguir a estrutura padrão do rspec-rails.

## Exemplo
O exemplo oficial declara describe "the signin process", type: :feature do, cria o usuário em before :each, chama visit '/sessions/new', preenche #session, clica em 'Sign in' e valida expect(page).to have_content 'Success'.

## Limites e trade-offs
Em system specs do Rails, a seleção de driver segue as regras próprias do rspec-rails (como driven_by), razão pela qual o README remete diretamente à documentação do rspec-rails para esse caso.

## Como verificar
Conferi a seção Using Capybara with RSpec no README oficial do Capybara.

## Conexões
- [[capybara-cucumber-integration]] — Veja também: Integração com Cucumber: cucumber-rails, within e a tag @javascript.
- [[capybara-rspec-js-driver-switching]] — Veja também: Seleção de driver no RSpec com js: true e driver: :selenium.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
