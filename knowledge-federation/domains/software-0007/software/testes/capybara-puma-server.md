---
id: software.testes.tranche25.001863
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

# Configuração do servidor Puma e o modo Silent no Rails 5.0+

## Em uma frase
O README orienta que, ao usar Rails 5.0+ sem usar os system tests introduzidos no Rails 5.1, convém trocar o servidor que lança a aplicação para Puma a fim de acompanhar os padrões do Rails: Capybara.server = :puma durante o ajuste inicial ou Capybara.server = :puma, { Silent: true } para limpar a saída de testes.

## Por que importa
Quando um driver com navegador real faz requisições HTTP contra a aplicação, o Capybara sobe um servidor web em thread separada; alinhar esse servidor ao Puma usado em desenvolvimento evita diferenças sutis de concorrência e reduz o ruído de log no terminal com Silent: true.

## Como funciona
Configure Capybara.server = :puma no helper da suíte enquanto depura a infraestrutura e adicione a opção { Silent: true } assim que o boot estiver funcionando para manter o log de CI limpo.

## Exemplo
No spec_helper.rb de uma suíte Rails que usa rspec-rails com features clássicas, definir Capybara.server = :puma, { Silent: true } suprime os banners de inicialização do Puma a cada rodada.

## Limites e trade-offs
Essa configuração só entra em ação para drivers que acessam a aplicação via rede/HTTP; no driver padrão Rack::Test não há servidor HTTP real sendo iniciado.

## Como verificar
Conferi o bloco sobre Capybara.server = :puma na seção Setup do README oficial.

## Conexões
- [[capybara-setup-ruby-rack-rails]] — Veja também: Setup com Ruby 3.0+, gem capybara, capybara/rails e Capybara.app.
- [[capybara-cucumber-integration]] — Veja também: Integração com Cucumber: cucumber-rails, within e a tag @javascript.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
