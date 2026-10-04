---
id: software.testes.tranche08.000210
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: validar schema de features antes do serving

## Em uma frase
Valide tipos, presença, domínio e versão do schema tanto na entrada de treino quanto na de predição.

## Por que importa
Mudança de coluna ou unidade pode quebrar inferência silenciosamente ou produzir resultados numericamente plausíveis, mas semanticamente errados.

## Como funciona
Defina contrato versionado, teste campos obrigatórios e opcionais, valores nulos e faixas admissíveis, e rejeite ou encaminhe dados incompatíveis conforme política.

## Exemplo
Feature de idade chega como string em um produtor; teste de contrato falha antes de chamar modelo e relata campo e versão sem expor dado sensível.

## Limites e trade-offs
Schema estrutural não detecta toda mudança semântica, drift ou correlação inesperada; valide distribuição e significado além do tipo.

## Como verificar
Execute payload válido, ausente, nulo, unidade trocada e versão incompatível; confirme que erro é acionável e registrado.

## Conexões
- [[ml-training-serving-skew-transformacao]] — Veja também: ML: detectar divergência entre transformação de treino e serving.
- [[ml-data-leakage-split-temporal]] — Veja também: ML: testar vazamento de informação entre splits.

## Fontes
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
- [Google ML — Transforming data](https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data) — transformação de dados e riscos de discrepância entre treino e serving; consultado em 2026-10-02.
