---
id: software.testes.tranche25.001862
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

# Setup com Ruby 3.0+, gem capybara, capybara/rails e Capybara.app

## Em uma frase
Na seção Setup, o README estabelece que o Capybara exige Ruby 3.0.0 ou superior, instalado adicionando gem 'capybara' ao Gemfile e rodando bundle install; para uma aplicação Rails adiciona-se require 'capybara/rails' ao test helper, e para uma aplicação Rack que não seja Rails define-se Capybara.app = MyRackApp.

## Por que importa
Como o Capybara consegue montar a aplicação Rack no mesmo processo dos testes, não é preciso subir um servidor externo manualmente para testar rotas HTML simples — bastando apontar Capybara.app ou carregar o helper do Rails.

## Como funciona
Adicione a gem ao Gemfile, carregue capybara/rails no helper de testes (ou configure Capybara.app para apps Sinatra/Rack puros) e verifique a versão mínima de Ruby 3.0.0 no ambiente de CI.

## Exemplo
Em uma aplicação Rack fora do Rails, duas linhas no helper — require 'capybara/cucumber' e Capybara.app = MyRackApp — já conectam a DSL à aplicação sob teste.

## Limites e trade-offs
Quando o teste precisa executar JavaScript ou interagir com uma URL remota, o driver padrão não basta; o README avisa nessa mesma seção que é necessário selecionar outro driver.

## Como verificar
Conferi a seção Setup do README oficial do Capybara.

## Conexões
- [[capybara-key-benefits]] — Veja também: Quatro benefícios declarados: zero setup em Rails/Rack, troca de backend e sincronização.
- [[capybara-puma-server]] — Veja também: Configuração do servidor Puma e o modo Silent no Rails 5.0+.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
