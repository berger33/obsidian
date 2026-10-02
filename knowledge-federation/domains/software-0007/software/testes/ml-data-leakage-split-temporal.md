---
id: software.testes.tranche08.000212
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
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: testar vazamento de informação entre splits

## Em uma frase
Faça o split refletir unidade e tempo do problema e teste que informação futura ou duplicada não atravesse treino e avaliação.

## Por que importa
Leakage eleva métricas offline sem melhorar generalização, levando a uma implantação cujo desempenho diverge da expectativa.

## Como funciona
Escolha split por usuário, entidade ou período segundo o caso; verifique sobreposição, features derivadas de alvo e uso de estatística calculada com dados futuros.

## Exemplo
Para previsão temporal, corte por data antes de computar agregações e confirme que eventos posteriores ao instante previsto não entram em features.

## Limites e trade-offs
Nenhum teste genérico identifica todo leakage; exige conhecimento de causalidade, disponibilidade da feature e processo de geração dos rótulos.

## Como verificar
Audite origem e timestamp das features, procure IDs comuns nos splits e compare pipeline de treino com informação disponível no instante de inferência.

## Conexões
- [[ml-feature-schema-contract-validacao]] — Veja também: ML: validar schema de features antes do serving.
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — Veja também: ML: tornar experimentos e artefatos reproduzíveis.

## Fontes
- [Google ML — Transforming data](https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data) — transformação de dados e riscos de discrepância entre treino e serving; consultado em 2026-10-02.
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
