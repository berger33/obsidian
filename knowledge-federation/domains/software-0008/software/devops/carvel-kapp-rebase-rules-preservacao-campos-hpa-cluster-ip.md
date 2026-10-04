---
id: software.devops.tranche16.001516
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: `rebaseRules` para preservar campos mutados pelo cluster (HPA, `clusterIP`, webhooks)

## Em uma frase
O mecanismo de `rebaseRules` do `kapp` copia seletivamente campos do recurso já existente no cluster para o manifesto que está sendo aplicado, evitando que um novo deploy sobrescreva valores gerenciados dinamicamente pelo Kubernetes ou por controladores externos.

## Por que importa
Quando um `HorizontalPodAutoscaler` escala um `Deployment` de `2` para `8` réplicas em horário de pico, um novo deploy cujo YAML estático contém `replicas: 2` causaria um scale-down abrupto e indisponibilidade se o campo `spec.replicas` não fosse preservado do objeto vivo no cluster.

## Como funciona
O `kapp` já traz um conjunto abrangente de `rebaseRules` padrão (como preservar `spec.clusterIP` em `Service` e campos de `ServiceAccount`), e permite adicionar regras declarativas em um objeto `kind: Config` (`apiVersion: kapp.k14s.io/v1alpha1`) para copiar `spec.replicas` do recurso `existing` para o recurso `new` sempre que um HPA estiver ativo.

## Exemplo
```yaml
apiVersion: kapp.k14s.io/v1alpha1
kind: Config
rebaseRules:
  - path: [spec, replicas]
    type: copy
    sources: [existing, new]
    resourceMatchers:
      - apiVersionKindMatcher: {apiVersion: apps/v1, kind: Deployment}
```

## Limites e trade-offs
Na lista `sources: [existing, new]`, a ordem define a prioridade: o `kapp` usa o valor do recurso `existing` no cluster se ele já existir, e cai para `new` (o valor do arquivo YAML) apenas na primeira criação do `Deployment`.

## Como verificar
Escale manualmente o `Deployment` para `4` réplicas no cluster, execute `kapp deploy -a payments-api -f manifestos.yml --diff-changes --diff-run` com a `rebaseRule` ativa e confirme que `spec.replicas` permanece em `4` sem diff de redução.

## Conexões
- [[carvel-kapp-apply-waiting-reconciliacao-wait-rules-streaming-logs]] — Veja também: Carvel kapp: espera ativa de convergência (`apply waiting`), `waitRules` e streaming de logs (`--logs`).
- [[carvel-kapp-update-strategies-fallback-on-replace-always-replace]] — Veja também: Carvel kapp: estratégias de atualização (`update-strategy`) para campos imutáveis em Jobs e Services.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
