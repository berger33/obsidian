---
id: software.devops.tranche16.001515
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: espera ativa de convergência (`apply waiting`), `waitRules` e streaming de logs (`--logs`)

## Em uma frase
Durante o estágio de aplicação, o `kapp` monitora ativamente o status de cada recurso modificado (`Wait to: reconcile` ou `delete`), suportando regras customizadas (`waitRules`) para CRDs e streaming em tempo real dos logs dos Pods com `--logs`.

## Por que importa
Um `Deployment` pode ser aceito pelo `kube-apiserver` em milissegundos e logo em seguida entrar em `CrashLoopBackOff` ou `ImagePullBackOff`. Sem espera ativa de convergência e coleta de logs no próprio comando de deploy, o pipeline de CI marca o estágio como verde enquanto a produção falha.

## Como funciona
O `kapp` possui avaliadores nativos para recursos padrão (`Deployment`, `StatefulSet`, `DaemonSet`, `Job`, `Pod`, `Service`, `PVC`, `CRD`) e avalia condições padrão (`Ready`, `Succeeded`, `Available`) ou expressões `ytt` em `waitRules` para Custom Resources. Quando `--logs` (ou `kapp.k14s.io/logs: ""`) é ativado, os logs dos containers afetados são intercalados no terminal enquanto o rollout progride.

## Exemplo
```bash
kapp deploy -a payments-api -f rendered-manifests.yml --logs --wait-timeout 5m --yes
```

## Limites e trade-offs
Se um `Service` do tipo `LoadBalancer` for implantado em um cluster local (como `kind` sem MetalLB), o `kapp` aguardará indefinidamente até atingir `--wait-timeout` porque o campo `.status.loadBalancer.ingress` nunca será preenchido.

## Como verificar
Acompanhe as colunas `Rs` (Reconcile state) e `Ri` (Reconcile info) durante o `kapp deploy` ou consultando posteriormente `kapp inspect -a payments-api`.

## Conexões
- [[carvel-kapp-ordenacao-mudancas-change-group-change-rule]] — Veja também: Carvel kapp: ordenação determinística de mudanças com `change-group` e `change-rule`.
- [[carvel-kapp-rebase-rules-preservacao-campos-hpa-cluster-ip]] — Veja também: Carvel kapp: `rebaseRules` para preservar campos mutados pelo cluster (HPA, `clusterIP`, webhooks).

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
