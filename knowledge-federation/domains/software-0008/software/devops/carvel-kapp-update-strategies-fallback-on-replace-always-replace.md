---
id: software.devops.tranche16.001517
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

# Carvel kapp: estratégias de atualização (`update-strategy`) para campos imutáveis em Jobs e Services

## Em uma frase
Por meio da anotação `kapp.k14s.io/update-strategy`, o `kapp` permite controlar como recursos com campos imutáveis são atualizados (`update`, `fallback-on-replace`, `always-replace` ou `skip`).

## Por que importa
A API do Kubernetes proíbe a alteração de vários campos após a criação do objeto — como `spec.selector` em um `Deployment` ou praticamente todo o `spec.template` de um `batch/v1 Job`. Um `kubectl apply` comum falha com erro `field is immutable`, travando o pipeline de entrega contínua.

## Como funciona
Quando um recurso recebe `kapp.k14s.io/update-strategy: fallback-on-replace` (ou `always-replace` para Jobs de migração), o `kapp` exibe essa estratégia na coluna `Op st.` da tabela de diff. Ao executar o apply, ele remove primeiro o objeto antigo (aguardando sua deleção completa) e recria imediatamente o novo objeto com a especificação atualizada.

## Exemplo
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: seed-reference-data
  annotations:
    kapp.k14s.io/update-strategy: always-replace
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: seeder
          image: ghcr.io/org/seeder:v1.2.0
```

## Limites e trade-offs
Usar `always-replace` ou `fallback-on-replace` em um `PersistentVolumeClaim` ou `StatefulSet` sem proteção adequada destruiria o objeto e potencialmente os volumes subjacentes; essa anotação deve ser restrita a recursos descartáveis como `Job` ou recriações planejadas.

## Como verificar
Altere a imagem do `Job` anotado, execute `kapp deploy -a app -f job.yml --diff-run` e confirme que a coluna `Op st.` exibe `always replace`.

## Conexões
- [[carvel-kapp-rebase-rules-preservacao-campos-hpa-cluster-ip]] — Veja também: Carvel kapp: `rebaseRules` para preservar campos mutados pelo cluster (HPA, `clusterIP`, webhooks).
- [[carvel-kapp-ownership-exists-noop-compartilhamento-recursos]] — Veja também: Carvel kapp: políticas de propriedade (`kapp.k14s.io/exists` e `kapp.k14s.io/noop`) para recursos compartilhados.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
