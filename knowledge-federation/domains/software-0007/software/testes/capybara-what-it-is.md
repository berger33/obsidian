---
id: software.testes.tranche25.001860
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

# Capybara: simular um usuário real interagindo com a aplicação web

## Em uma frase
O README oficial descreve o Capybara como uma biblioteca que ajuda a testar aplicações web simulando como um usuário real interagiria com o app, sendo agnóstica em relação ao driver que executa os testes; já traz suporte embutido a Rack::Test e Selenium, enquanto WebKit é suportado por gem externa.

## Por que importa
Em vez de acoplar o teste ao protocolo interno de um único navegador ou cliente HTTP, separar a DSL do driver permite escrever o fluxo do usuário uma vez e escolher depois se ele roda em modo rápido sem navegador ou num browser real.

## Como funciona
O teste descreve ações de usuário (visitar rota, preencher campos, clicar botões) sobre a sessão atual; o Capybara traduz essas operações para o driver configurado na suíte ou no cenário.

## Exemplo
Em um teste de login, o bloco visita a página, preenche Email e Password e aciona Sign in sem mencionar chamadas diretas ao Selenium ou ao Rack::Test no corpo do cenário.

## Limites e trade-offs
O suporte embutido no README cobre Rack::Test e Selenium; drivers adicionais como WebKit vivem em gems externas com manutenção própria.

## Como verificar
Conferi o parágrafo de abertura do README oficial no repositório teamcapybara/capybara.

## Conexões
- [[capybara-key-benefits]] — Veja também: Quatro benefícios declarados: zero setup em Rails/Rack, troca de backend e sincronização.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
