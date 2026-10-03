---
id: software.testes.tranche24.001824
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

# O formato: Feature, Background e Scenario em inglês estruturado

## Em uma frase
A página inicial da doc abre com o artefato canônico completo: um bloco "Feature:" com a tríade "In order to know when I have correctly implemented a feature / As a PHP developer / I want a tool to execute tests based on the agreed specifications", um "Background:" com pré-condições compartilhadas e um "Scenario:" de passos Given/When/Then.

## Por que importa
Essa gramática não é decoração: os blocos de propósito-ator-objetivo forçam a especificação a dizer para quem e por quê antes do o quê, e o Background separa o custo de setup que todo cenário paga do comportamento que o cenário prova.

## Como funciona
Estruture o arquivo .feature com um Feature e seus cenários; mova para Background as condições aceitas por todos os cenários da suíte (login, dados de teste), e deixe cada Scenario como a unidade executável e reportável.

## Exemplo
O exemplo oficial é autoexplicativo: o cenário "Work is complete" tem três passos — implementado corretamente, rodar o Behat, software se comportando como esperado — e o Background registra o acordo prévio com o product team.

## Limites e trade-offs
A doc inicial mostra o formato do bloco introdutório; a especificação completa do Gherkin (tabelas, exemplos, doc strings) vive nos guias e na linguagem do Cucumber, não na página lida.

## Como verificar
O bloco de código da seção de abertura da doc oficial fornece o exemplo literal.

## Conexões
- [[behat-semver-bc]] — Veja também: Promessa de compatibilidade: interfaces e service constants.
- [[behat-full-application-scope]] — Veja também: Cobrindo a aplicação inteira, não camadas.

## Fontes
- [Behat — documentação oficial (en/latest)](https://docs.behat.org/en/latest/) — Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.; consultado em 2026-10-03.
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
