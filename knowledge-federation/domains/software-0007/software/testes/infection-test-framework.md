---
id: software.testes.tranche23.001749
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
fontes: ["https://infection.github.io/guide/command-line-options.html", "https://infection.github.io/guide/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# --test-framework: o adaptador que escolhe como o Infection roda seus testes

## Em uma frase
A doc de opções documenta o seletor de motor de teste: --test-framework recebe o nome do framework a usar, com a lista oficial PHPUnit, PhpSpec, Codeception e Testo, e a regra de disponibilidade dos adaptadores — na instalação composer, o PHPUnit já vem; os demais adaptadores são instalados sob demanda, enquanto a distribuição phar carrega todos os disponíveis de fábrica.

## Por que importa
A escolha define tudo a montante: é o adaptador que sabe invocar o runner do projeto, mapear testes por cobertura e interpretar resultados — configurar o framework errado produz um erro de inicialização ruidoso em vez de mutantes.

## Como funciona
A página complementa com o canal de passagem de argumentos: desde a versão 0.34.0, --test-framework-extra-args anexa opções e argumentos ao comando do framework — o exemplo executa phpunit com --verbose --filter=just/unit/tests — substituindo a opção antiga homóloga de 0.34.0 para cá; --test-framework-options é marcada deprecated com pointer direto para a nova.

## Exemplo
A mesma seção grava uma sutileza de filtro que muda a leitura de resultados: quando você passa --configuration, --filter ou --testsuite ao PHPUnit por esse canal, eles se aplicam apenas à execução inicial — para cada mutante o Infection gera um phpunit.xml próprio apontando para o subset de testes relevante, então os filtros perdem sentido nesse contexto.

## Limites e trade-offs
A lista de quatro frameworks é o suporte atual declarado; a página encoraja pedir novos frameworks via GitHub issues, o que sinaliza que a matriz não é fechada por contrato — e a semântica dos filtros por mutante (phpunit.xml gerado) vale só para o caminho PHPUnit descrito na seção.

## Como verificar
Rode infection --test-framework=PHPUnit --test-framework-extra-args="--filter=just/unit/tests" e observe no log a linha do comando phpunit montado — é a composição literal descrita na página. Para a leitura da matriz, Abra as seções --test-framework, --test-framework-extra-args e --test-framework-options da página Command line options e confirme as frases citadas, a numeração 0.34.0 e o bloco do filtro por mutante.

## Conexões
- [[infection-mutators]] — Veja também: Mutators: famílias AST, o describe e o --id para matar um de cada vez.

## Fontes
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
