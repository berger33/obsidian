---
id: software.testes.tranche20.001412
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://assertj.github.io/doc/", "https://javadoc.io/doc/org.assertj/assertj-core/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AssertJ: acumular falhas com asserções suaves

## Em uma frase
O objeto de asserções suaves coleta os erros de várias verificações e os reporta juntos ao final do bloco.

## Por que importa
Verificar múltiplos campos de uma vez evita a sequência de correções uma a uma e mostra o conjunto de divergências de uma só execução.

## Como funciona
Crie o objeto por caso, acumule as verificações e dispare o relatório final explicitamente.

## Exemplo
Uma validação de cadastro pode verificar nome, correio e telefone na mesma passagem e receber os três problemas de uma vez.

## Limites e trade-offs
Esquecer a chamada final descarta todos os erros coletados, e acumular asserções de casos distintos mistura responsabilidades.

## Como verificar
Deixe duas verificações falharem no mesmo bloco e confirme que as duas aparecem no relatório da execução.

## Conexões
- [[assertj-descriptions]] — Veja também: AssertJ: descrever asserções.
- [[assertj-junit-integration]] — Veja também: AssertJ: integrar as asserções suaves à suíte.

## Fontes
- [AssertJ — Documentação](https://assertj.github.io/doc/) — asserções fluentes, coleções, descrições, asserções suaves e próprias; consultado em 2026-10-03.
- [AssertJ — Documentação de API](https://javadoc.io/doc/org.assertj/assertj-core/latest/index.html) — referência das classes de asserção e dos módulos; consultado em 2026-10-03.
