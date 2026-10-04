---
id: software.testes.tranche24.001825
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://docs.behat.org/en/latest/", "https://raw.githubusercontent.com/Behat/Behat/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cobrindo a aplicação inteira, não camadas

## Em uma frase
A seção "Cover your whole application" da doc oficial marca a distinção: o Behat ajuda a focar em expectativas de negócio e comportamento voltado ao usuário, "very different to many test runners, where tests become tied to implementations and to individual layers of your stack" — os feature files podem descrever o comportamento inteiro da aplicação, e o time mantém "total freedom to decide how to implement the code that proves the application works".

## Por que importa
O preço da amarração por camada é citado como contraste: quando o teste referencia controladores e services, refatorar quebra suíte; quando o teste fala com o usuário visível, refatorar é interno. A liberdade de implementação declarada é o payoff dessa escolha.

## Como funciona
Escreva o cenário na linguagem do que o usuário vê (respostas, páginas, efeitos), e escolha por trás dele a camada mais barata que prova o comportamento — o framework não obriga a atravessar a stack inteira em cada passo.

## Exemplo
A doc dá a régua: um feature file pode cobrir "the whole behaviour of your application", e a implementação dos steps é decisão de engenharia do time, inclusive trocar abordagem por suíte.

## Limites e trade-offs
O texto posiciona o Behat como ferramenta de especificação, não suíte completa: o próprio material contrasta com runners de baixo nível, sem afirmar que os substitui no portfólio de testes de um time.

## Como verificar
A seção "Cover your whole application" da página inicial da doc oficial fornece as frases citadas.

## Conexões
- [[behat-gherkin-features]] — Veja também: O formato: Feature, Background e Scenario em inglês estruturado.
- [[behat-mix-approaches]] — Veja também: Misture tecnologias: navegador, HTTP, shell, banco e PHP direto.

## Fontes
- [Behat — documentação oficial (en/latest)](https://docs.behat.org/en/latest/) — Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.; consultado em 2026-10-03.
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
