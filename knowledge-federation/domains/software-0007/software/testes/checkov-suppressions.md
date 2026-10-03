---
id: software.testes.tranche19.001310
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
fontes: ["https://github.com/bridgecrewio/checkov/blob/master/README.md", "https://github.com/bridgecrewio/checkov"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: registrar supressões com justificativa

## Em uma frase
Uma anotação no próprio arquivo registra a aceitação do risco, com identificador da verificação e motivo declarado.

## Por que importa
Registrar a decisão junto ao recurso mantém o histórico auditável e evita que a verificação inteira seja desligada por um caso isolado.

## Como funciona
Anote a supressão no recurso correspondente, escreva o motivo de forma objetiva e reavalie as anotações periodicamente.

## Exemplo
Um recurso de conteúdo estático acessível publicamente pode registrar a supressão com explicação do uso pretendido.

## Limites e trade-offs
Supressões sem motivo impedem a revisão futura, e anotações esquecidas mantêm riscos aceitos no passado sem decisão vigente.

## Como verificar
Remova temporariamente uma anotação e confirme qual achado ela estava suprimindo antes de mantê-la.

## Conexões
- [[checkov-running-checks]] — Veja também: Checkov: selecionar e excluir verificações.
- [[checkov-baseline]] — Veja também: Checkov: separar passivo antigo de achados novos.

## Fontes
- [Checkov — Guia de uso](https://github.com/bridgecrewio/checkov/blob/master/README.md) — execução, seleção de verificações, supressões, linha de base e segredos; consultado em 2026-10-03.
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
