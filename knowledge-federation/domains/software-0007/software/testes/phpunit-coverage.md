---
id: software.testes.tranche18.001202
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://docs.phpunit.de/en/12.5/code-coverage.html", "https://github.com/sebastianbergmann/phpunit"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: medir e interpretar cobertura

## Em uma frase
Com a extensão apropriada habilitada, a execução coleta dados de linhas e ramos e permite gerar relatórios em formatos distintos.

## Por que importa
O relatório aponta trechos não exercitados e torna visível a diferença entre execução de linha e verificação de comportamento.

## Como funciona
Habilite a cobertura na configuração, informe o escopo de origem e gere o relatório no formato adequado ao consumo.

## Exemplo
Uma listagem de linhas ausentes aponta diretamente o trecho não executado, orientando a escrita de novos casos.

## Limites e trade-offs
Cobertura descreve o que foi executado e não o que foi verificado, e perseguir percentuais altos incentiva testes sem afirmação útil.

## Como verificar
Escolha um trecho coberto porém sem verificação relevante e proponha uma asserção que distinga comportamento correto de incorreto.

## Conexões
- [[phpunit-test-doubles]] — Veja também: PHPUnit: substituir dependências com dublês.
- [[phpunit-exception-testing]] — Veja também: PHPUnit: verificar caminhos de exceção.

## Fontes
- [PHPUnit — Code coverage](https://docs.phpunit.de/en/12.5/code-coverage.html) — medição de linhas e ramos e geração de relatórios; consultado em 2026-10-03.
- [PHPUnit — repositório oficial](https://github.com/sebastianbergmann/phpunit) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
