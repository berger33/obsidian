---
id: software.testes.tranche19.001346
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/TNG/ArchUnit", "https://www.archunit.org/userguide/html/000_Index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: tratar falhas na esteira

## Em uma frase
A falha da verificação interrompe a construção e traz a lista das violações com as classes envolvidas.

## Por que importa
Bloquear a construção é o que dá efeito prático à regra; um relatório ignorado não altera a estrutura do código.

## Como funciona
Mantenha as regras na suíte obrigatória, não mascare falhas com exclusões apressadas e corrija a violação na origem.

## Exemplo
Uma mudança que introduz acesso indevido pode ser barrada ainda na revisão, antes de a estrutura se consolidar.

## Limites e trade-offs
Desativar a regra para liberar uma entrega transfere o problema para depois e ensina o time a ignorar a verificação.

## Como verificar
Introduza uma violação em revisão de teste e confirme que o trabalho da esteira falha indicando a regra e a classe.

## Conexões
- [[archunit-test-organization]] — Veja também: ArchUnit: organizar as verificações na suíte.
- [[archunit-limits-and-practices]] — Veja também: ArchUnit: reconhecer limites.

## Fontes
- [ArchUnit — repositório oficial](https://github.com/TNG/ArchUnit) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
