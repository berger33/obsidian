---
id: software.testes.tranche25.001867
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

# A DSL de aceitação embutida: feature, background, scenario e given

## Em uma frase
O README apresenta a DSL descritiva que acompanha a integração com RSpec: feature é um alias para describe ..., type: :feature, background é alias para before, scenario é alias para it, e given/given! são aliases para let/let!, respectivamente.

## Por que importa
Essa camada de vocabulário permite escrever testes de aceitação em estilo próximo ao BDD diretamente em Ruby puro sobre o RSpec, sem a camada extra de parsing de arquivos Gherkin quando apenas desenvolvedores mantêm a suíte.

## Como funciona
Use feature "Signing in" do com blocos background, given(:other_user) e scenario para estruturar especificações de aceitação autoexplicativas que já herdam automaticamente type: :feature.

## Exemplo
No exemplo do README, feature "Signing in" define um background que cria 'user@example.com', um dado preguiçoso given(:other_user) e dois blocos scenario testando credenciais válidas e de outro usuário.

## Limites e trade-offs
Como feature/scenario/given são apenas aliases sobre describe/it/let do RSpec, eles não criam isolamento de passos reutilizáveis ao estilo Cucumber; o compartilhamento de código continua sendo feito via métodos auxiliares ou shared examples do RSpec.

## Como verificar
Conferi a tabela de aliases e o exemplo feature "Signing in" na seção Using Capybara with RSpec do README oficial.

## Conexões
- [[capybara-rspec-js-driver-switching]] — Veja também: Seleção de driver no RSpec com js: true e driver: :selenium.
- [[capybara-dsl-scoping-and-matchers]] — Veja também: Navegação, escopo com within, formulários e matchers em view specs.

## Fontes
- [Capybara — README oficial](https://raw.githubusercontent.com/teamcapybara/capybara/master/README.md) — README oficial do Capybara com benefícios-chave, requisitos Ruby 3.0+, setup para Rails/Rack/Puma, integração com Cucumber e RSpec, DSL de aceitação e canais de suporte.; consultado em 2026-10-03.
- [Repositório oficial teamcapybara/capybara](https://github.com/teamcapybara/capybara) — Repositório oficial do Capybara no GitHub com código-fonte, drivers embutidos Rack::Test e Selenium, suíte de testes e GitHub Discussions.; consultado em 2026-10-03.
