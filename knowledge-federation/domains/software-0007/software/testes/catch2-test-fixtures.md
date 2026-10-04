---
id: software.testes.tranche19.001261
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
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/test-fixtures.md", "https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: usar fixtures para estado compartilhado

## Em uma frase
Fixtures são classes com preparação e limpeza opcionais, usadas quando seções não bastam para o estado comum.

## Por que importa
Estruturas que exigem inicialização custosa ou membros persistentes se beneficiam de fixture, mantendo o caso legível.

## Como funciona
Derive de uma classe base com preparação e limpeza, e registre o caso com a macro de fixture correspondente.

## Exemplo
Uma fixture pode preparar uma conexão de banco em memória usada por todos os casos de um arquivo.

## Limites e trade-offs
Colocar toda a preparação em fixture elimina a visibilidade do fluxo, e misturar seções com fixture sem critério confunde a leitura.

## Como verificar
Remova a limpeza da fixture e confirme que o efeito residual entre casos aparece como falha em execução encadeada.

## Conexões
- [[catch2-sections]] — Veja também: Catch2: compartilhar preparação com seções.
- [[catch2-generators]] — Veja também: Catch2: gerar dados de entrada.

## Fontes
- [Catch2 — Test fixtures](https://github.com/catchorg/Catch2/blob/devel/docs/test-fixtures.md) — preparação e limpeza por caso e por arquivo; consultado em 2026-10-03.
- [Catch2 — Tutorial](https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md) — primeiros passos, casos de teste, seções e asserções; consultado em 2026-10-03.
