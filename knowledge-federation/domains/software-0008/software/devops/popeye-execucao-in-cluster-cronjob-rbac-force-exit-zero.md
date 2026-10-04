---
id: software.devops.tranche11.001079
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/derailed/popeye/master/README.md", "https://popeyecli.io/docs/codes.html", "https://github.com/derailed/popeye"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução do Popeye in-cluster via CronJob Kubernetes, flag --force-exit-zero e perfil RBAC somente-leitura

## Em uma frase
O Popeye pode ser executado periodicamente dentro do próprio cluster Kubernetes como um **`CronJob`** (`batch/v1`), exigindo obrigatoriamente a flag **`--force-exit-zero`** nos argumentos do container e uma `ClusterRole` somente-leitura (`verbs: ["get", "list"]`) sobre os grupos de API inspecionados.

## Por que importa
Entender por que a flag `--force-exit-zero` é indispensável em um `CronJob` evita um problema clássico de operação: como o Popeye por padrão retorna código de saída diferente de zero (`exit code != 0`) sempre que encontra qualquer erro de lint no cluster, sem `--force-exit-zero` o Kubernetes marcará todos os pods do CronJob como `Error`/`Failed`.

## Como funciona
Conforme a seção *In Cluster* e *Popeye Got Your RBAC!* do README oficial (`derailed/popeye`): (1) cria-se um namespace dedicado (`popeye`), uma `ServiceAccount` (`popeye`), uma `ClusterRole` concedendo exclusivamente os verbos **`["get", "list"]`** sobre os recursos core (`configmaps`, `endpoints`, `namespaces`, `nodes`, `persistentvolumes`, `persistentvolumeclaims`, `pods`, `secrets`, `serviceaccounts`, `services`), `apps`, `networking.k8s.io`, `batch.k8s.io`, `gateway.networking.k8s.io`, `autoscaling`, `policy`, `rbac.authorization.k8s.io` e `metrics.k8s.io`, e o respectivo `ClusterRoleBinding`; e (2) o `CronJob` executa a imagem do Popeye passando `-o yaml` (ou `--push-gtwy-url` / `--s3-bucket`) junto com **`--force-exit-zero`** para que o Job conclua com status `Completed` (`0`) mesmo quando encontrar alertas no cluster.

## Exemplo
```yaml
# Trecho do CronJob oficial do Popeye rodando a cada hora com --force-exit-zero para evitar pods em estado Error
apiVersion: batch/v1
kind: CronJob
metadata:
  name: popeye
  namespace: popeye
spec:
  schedule: "0 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: popeye
          restartPolicy: Never
          containers:
            - name: popeye
              image: quay.io/derailed/popeye:latest
              imagePullPolicy: IfNotPresent
              args:
                - -A
                - -o
                - yaml
                - --force-exit-zero
              resources:
                limits:
                  cpu: 500m
                  memory: 100Mi
```

## Limites e trade-offs
Se a `ServiceAccount` do Popeye não tiver permissão `get`/`list` em algum dos grupos de recursos esperados pelos linters ativos (por exemplo, `metrics.k8s.io` ou `gateway.networking.k8s.io`), o linter correspondente falhará com erro de RBAC; se o seu cluster restrito não permitir acesso a certos recursos, filtre os linters executados com a flag `-s`.

## Como verificar
Aplique o `CronJob`, crie uma execução manual de teste com `kubectl -n popeye create job --from=cronjob/popeye popeye-manual-1` e verifique os logs com `kubectl -n popeye logs job/popeye-manual-1`.

## Conexões
- [[popeye-metricas-prometheus-pushgateway-grafana]] — Veja também: Observabilidade contínua com Popeye: publicação de métricas no Prometheus Pushgateway e dashboards Grafana.
- [[popeye-integracao-k9s-preflight-troubleshooting-clusters]] — Veja também: Integração nativa do Popeye com o K9s (:popeye) e diagnóstico de problemas operacionais de linha de comando.
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.
- [[popeye-persistencia-relatorios-save-s3-minio-docker]] — Referência cruzada direta com popeye-persistencia-relatorios-save-s3-minio-docker.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
