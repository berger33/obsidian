---
id: software.testes.tranche08.000213
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
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: tornar experimentos e artefatos reproduzíveis

## Em uma frase
Registre código, dados, configuração e ambiente necessários para explicar como o artefato de modelo foi produzido.

## Por que importa
Sem proveniência, regressão de qualidade pode não ser reproduzível e comparação entre versões fica sujeita a mudanças ocultas.

## Como funciona
Versione referências imutáveis a dados e código, salve parâmetros, dependências e métricas, e controle seeds quando a biblioteca oferecer determinismo relevante.

## Exemplo
Dois jobs executam a mesma configuração e comparam métricas dentro de tolerância definida, preservando hash de dataset e versão do modelo.

## Limites e trade-offs
Seed fixa não garante bitwise determinism em todas as bibliotecas, hardware ou operações paralelas; registre versão e plataforma.

## Como verificar
Reexecute pipeline com manifest salvo, compare hashes e métricas e documente variação esperada em operações não determinísticas.

## Conexões
- [[ml-numerica-tolerancia-estabilidade]] — Veja também: ML: definir tolerância para comparações numéricas.
- [[ml-canary-release-rollback-metricas]] — Veja também: ML: liberar modelo por canário e critério de rollback.

## Fontes
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
