---
id: software.testes.tranche19.001262
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
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/generators.md", "https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: gerar dados de entrada

## Em uma frase
Geradores percorrem valores em sequência dentro do caso, e geradores no mesmo escopo produzem o produto cartesiano das entradas.

## Por que importa
A mesma lógica de verificação passa a valer para várias entradas sem duplicar o caso, cobrindo limites com pouco código.

## Como funciona
Use o gerador de faixa para valores numéricos, liste valores explícitos para casos de borda e evite produtos cartesianos grandes.

## Exemplo
Um caso pode percorrer valores de entrada de um formulário e verificar que a validação rejeita cada um deles.

## Limites e trade-offs
Gerar muitas combinações multiplica o tempo de execução, e valores aleatórios sem semente fixa dificultam reproduzir a falha.

## Como verificar
Acrescente um valor inválido à lista gerada e confirme que a falha reporta o valor que a produziu.

## Conexões
- [[catch2-test-fixtures]] — Veja também: Catch2: usar fixtures para estado compartilhado.
- [[catch2-matchers]] — Veja também: Catch2: usar correspondências expressivas.

## Fontes
- [Catch2 — Data generators](https://github.com/catchorg/Catch2/blob/devel/docs/generators.md) — geradores de valores, produto cartesiano e integração com seções; consultado em 2026-10-03.
- [Catch2 — Tutorial](https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md) — primeiros passos, casos de teste, seções e asserções; consultado em 2026-10-03.
