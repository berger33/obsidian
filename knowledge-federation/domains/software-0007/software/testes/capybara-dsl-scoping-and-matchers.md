---
id: software.testes.tranche25.001868
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

# Navegação, escopo com within, formulários e matchers em view specs

## Em uma frase
Ao longo dos exemplos iniciais do README e do sumário da DSL, o fluxo combina visit para abrir um caminho, within("#session") para restringir a busca de campos a uma região do DOM, fill_in com a opção with:, click_button e o matcher expect(page).to have_content, que o README destaca também funcionar em view specs do RSpec (type: :view).

## Por que importa
Páginas reais costumam repetir rótulos ou botões (como dois formulários com botão "Sign in" ou "Search" no cabeçalho e no corpo); usar within("#session") evita ambiguidade de seletor e documenta exatamente qual componente da tela está sendo exercitado.

## Como funciona
Sempre que uma página tiver múltiplos formulários ou regiões repetidas, envolva os comandos fill_in e click_button num bloco within apontando para o contêiner específico antes de disparar a submissão.

## Exemplo
Em within("#session") do fill_in 'Email', with: 'user@example.com'; fill_in 'Password', with: 'caplin' end seguido de click_button 'Sign in' e expect(page).to have_content 'Success', a busca dos inputs fica confinada ao formulário de sessão.

## Limites e trade-offs
O suporte em view specs (type: :view) exercita os matchers do Capybara sobre o HTML renderizado pela view isolada, sem navegação completa nem execução de controlador ou JavaScript.

## Como verificar
Conferi os exemplos de within, fill_in, click_button, have_content e RSpec view specs no README oficial.

## Conexões
- [[capybara-acceptance-dsl-aliases]] — Veja também: A DSL de aceitação embutida: feature, background, scenario e given.
- [[capybara-architecture-topics-and-support]] — Veja também: Arquitetura do guia oficial: seletores, exactness, sessões nomeadas e canal de suporte.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
