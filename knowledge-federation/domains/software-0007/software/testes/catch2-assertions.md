---
id: software.testes.tranche19.001259
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
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md", "https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: escolher entre asserção fatal e não fatal

## Em uma frase
A biblioteca oferece macros que interrompem o caso ao falhar e macros que registram a falha e continuam a execução.

## Por que importa
A escolha correta evita mascarar falhas seguintes com estado inválido e mantém a execução útil quando as verificações são independentes.

## Como funciona
Use a macro fatal para precondições que tornam o restante inválido e a não fatal para verificações encadeadas e comparações de múltiplos campos.

## Exemplo
Uma verificação de ponteiro nulo pode ser fatal, enquanto as asserções sobre o objeto retornado seguem em macro não fatal.

## Limites e trade-offs
Usar apenas asserção fatal interrompe a coleta de falhas relacionadas, e usar apenas não fatal pode prosseguir sobre estado quebrado.

## Como verificar
Provoque falha em uma verificação não fatal seguida de outra e confirme que ambas aparecem no relatório da execução.

## Conexões
- [[catch2-test-case-basics]] — Veja também: Catch2: estruturar casos de teste.
- [[catch2-sections]] — Veja também: Catch2: compartilhar preparação com seções.

## Fontes
- [Catch2 — Assertions](https://github.com/catchorg/Catch2/blob/devel/docs/assertions.md) — macros de asserção fatais e não fatais e comparações; consultado em 2026-10-03.
- [Catch2 — Tutorial](https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md) — primeiros passos, casos de teste, seções e asserções; consultado em 2026-10-03.
