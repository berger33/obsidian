---
id: software.testes.tranche20.001392
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
fontes: ["https://keploy.io/docs/", "https://keploy.io/api-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: ler e ajustar as verificações geradas

## Em uma frase
O caso gravado compara a resposta devolvida na repetição com a resposta registrada, campo a campo, sinalizando diferenças.

## Por que importa
Conhecer o critério de comparação evita tanto aceitar regressões quanto interromper a esteira por campos que variam entre execuções.

## Como funciona
Revise os artefatos gerados, normalize campos voláteis e ajuste o caso quando a mudança de resposta for intencional.

## Exemplo
Um identificador de correlação devolvido em cada resposta precisa ser normalizado para não marcar diferença falsa.

## Limites e trade-offs
Comparação rígida de todos os campos gera falhas espúrias, e comparação frouxa deixa passar mudanças reais de contrato.

## Como verificar
Altere um campo da resposta de propósito e confirme que a repetição aponta exatamente o campo divergente.

## Conexões
- [[keploy-replay-in-ci]] — Veja também: Keploy: repetir na esteira de integração.
- [[keploy-deduplication]] — Veja também: Keploy: reduzir casos sem perder cobertura.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — Testes de API](https://keploy.io/api-testing) — geração de casos a partir de tráfego e cobertura de interface; consultado em 2026-10-03.
