---
id: software.testes.tranche15.000880
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.seattlerb.org/minitest/", "https://docs.seattlerb.org/minitest/Minitest/Test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: reconhecer testes por classe e prefixo

## Em uma frase
Casos escritos em classes que herdam de `Minitest::Test` são descobertos pelos métodos cujo nome começa com `test_`, sem registro manual de suíte.

## Por que importa
A descoberta por convenção explica por que um método auxiliar bem nomeado vira teste executado e por que um caso sem o prefixo nunca aparece no relatório.

## Como funciona
Organize responsabilidades em classes distintas e renomeie métodos de apoio para que não comecem com o prefixo reservado à descoberta.

## Exemplo
`class CalculadoraTest < Minitest::Test; def test_soma; assert_equal 4, Calculadora.soma(2, 2); end; end` é o formato mínimo de um caso.

## Limites e trade-offs
A convenção é rígida e não usa anotações; herança duplicada ou classes aninhadas mal posicionadas podem fazer o executor não carregar o arquivo esperado.

## Como verificar
Rode o arquivo isoladamente e confirme a contagem de testes executados, incluindo um método auxiliar renomeado que deixou de ser contado.

## Conexões
- [[minitest-core-assertions]] — Veja também: Minitest: escolher a asserção adequada ao valor.

## Fontes
- [Minitest — README](https://docs.seattlerb.org/minitest/) — visão geral do projeto, plugins e formas de execução; consultado em 2026-10-02.
- [Minitest — Test](https://docs.seattlerb.org/minitest/Minitest/Test.html) — classes de teste, ciclos de vida, ordem aleatória e paralelização; consultado em 2026-10-02.
