---
id: software.testes.tranche08.000218
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

# ML: definir tolerância para comparações numéricas

## Em uma frase
Compare outputs numéricos com tolerância justificada quando hardware ou operações de ponto flutuante impedirem igualdade exata.

## Por que importa
Igualdade bit a bit pode falhar sem mudança relevante, enquanto tolerância ampla demais oculta regressão de score ou ranking.

## Como funciona
Escolha absolute/relative tolerance conforme escala, normalize condições e valide decisão de downstream separadamente do score bruto.

## Exemplo
Teste de inferência compara logits dentro da faixa validada e confirma que classe e threshold não mudam em casos críticos.

## Limites e trade-offs
Tolerância é específica ao modelo, dtype, backend e uso; não copie valor de outro experimento sem caracterização.

## Como verificar
Rode em plataformas de suporte, estime variação real sob configuração fixa e injete diferença acima do limite para confirmar falha.

## Conexões
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — Veja também: ML: tornar experimentos e artefatos reproduzíveis.
- [[ml-calibracao-limiares-decisao]] — Veja também: ML: testar calibração e limiares de decisão.

## Fontes
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
