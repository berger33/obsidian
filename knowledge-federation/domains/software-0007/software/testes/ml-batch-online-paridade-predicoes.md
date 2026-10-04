---
id: software.testes.tranche08.000216
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

# ML: comparar predição batch e online

## Em uma frase
Teste a mesma entidade e instante nos caminhos batch e online quando ambos precisam produzir decisões compatíveis.

## Por que importa
Código, defaults ou feature freshness diferentes podem criar predições divergentes apesar de usarem o mesmo identificador de modelo.

## Como funciona
Fixe snapshot de entrada, versão do modelo e transformações; compare saída dentro da tolerância definida e registre dependências temporais.

## Exemplo
Um conjunto de pedidos avaliado em batch também passa por endpoint online; diferenças acima da tolerância bloqueiam release e mostram feature divergente.

## Limites e trade-offs
Paridade só faz sentido se ambos os modos compartilham contrato; previsões em instantes distintos podem divergir legitimamente por atualização de dados.

## Como verificar
Alinhe timestamp e snapshot, compare scores e explicações relevantes, e teste ausência ou atraso de feature em cada caminho.

## Conexões
- [[ml-training-serving-skew-transformacao]] — Veja também: ML: detectar divergência entre transformação de treino e serving.
- [[ml-model-serving-fallback-timeout]] — Veja também: ML: testar timeout e fallback de serving.

## Fontes
- [Google ML — Transforming data](https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data) — transformação de dados e riscos de discrepância entre treino e serving; consultado em 2026-10-02.
- [Google ML — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) — reprodutibilidade, integração e validação de releases de modelos; consultado em 2026-10-02.
