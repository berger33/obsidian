---
id: software.testes.tranche23.001741
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://infection.github.io/guide/", "https://infection.github.io/guide/installation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Infection: biblioteca PHP de mutação por AST, CLI na raiz do projeto

## Em uma frase
A definição oficial: "Infection is a PHP mutation testing library based on AST (Abstract Syntax Tree) mutations. It works as a CLI tool and can be executed from your project's root", com o resumo do algoritmo em cinco passos — rodar a suíte para confirmar que passa, mutar o código-fonte com os mutadores predefinidos, para cada mutante rodar os testes que cobrem a linha modificada, analisar se os testes passaram a falhar, e coletar os resultados de killed, escaped, erros e timeouts.

## Por que importa
O ponto comercial é a triagem por cobertura: rodar por mutante apenas os testes da linha tocada (coverage-based test selection) transforma o custo O(mutantes × suíte) em algo rodável, e a escolha por AST significa mutações cirúrgicas no nível da sintaxe, não regex textual.

## Como funciona
A página fixa o suporte atual do núcleo: frameworks de teste PHPUnit, PhpSpec, Codeception e Testo; requer PHP 8.3+ e Xdebug, phpdbg ou pcov instalado — o pré-requisito de driver de cobertura existe porque o passo 3 depende de saber que teste cobre que linha.

## Exemplo
O exemplo didático da doc (Form::hasErrors com count($this->errors) > 0) gera concretamente os mutantes listados: Conditional boundary (maior vira maior-igual), Conditional negotiation (maior vira menor) e Integer 0-1/1-0 (zero vira um) — "and so on" fecha a lista do que a mutação por AST produz naquele trecho.

## Limites e trade-offs
A matriz de suporte de versão do PHP é a da página atual (a própria página lista Infection >= 0.32.7 a partir de PHP 8.3.0); em PHP mais antigo, a recomendação da própria página é usar versão anterior da ferramenta, com a tabela de compatibilidade como contrato — e a lista de frameworks cresce por adaptação externa, não por promessa.

## Como verificar
Rode infection --dry-run num projeto pequeno com PHPUnit e cobertura habilitada e confira que a saída enumera mutantes por linha no formato do exemplo da página, sem alterar seu código. Abra as seções What is Infection e Ready for More do Introduction oficial e confirme a definição, o suporte a frameworks, os requisitos e os três mutantes do exemplo hasErrors.

## Conexões
- [[infection-what-mutation-testing]] — Veja também: Mutation testing: matar mutantes em vez de cobrir linhas.
- [[infection-msi-metrics]] — Veja também: As três métricas: MSI, Mutation Code Coverage e Covered Code MSI.

## Fontes
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
- [Infection — Installation](https://infection.github.io/guide/installation.html) — phar assinado, phive, composer, brew e tabela de compatibilidade; consultado em 2026-10-03.
