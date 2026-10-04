---
id: software.devops.tranche10.000920
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md", "https://external-secrets.io/latest/introduction/overview/", "https://github.com/external-secrets/external-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# External Secrets Operator: atualização imediata sob demanda (force-sync), métricas Prometheus e diagnóstico de eventos

## Em uma frase
Para forçar a sincronização imediata de um `ExternalSecret` sem esperar o próximo `refreshInterval`, basta atualizar uma anotação no recurso (como `force-sync`), monitorando a saúde das sincronizações via eventos Kubernetes e métricas Prometheus (`externalsecret_sync_calls_total`).

## Por que importa
Durante uma resposta a incidente em que uma chave de API comprometida acabou de ser rotacionada no AWS Secrets Manager ou no Vault, a equipe de operações não pode esperar 1 hora pelo próximo ciclo automático de `refreshInterval` — ela precisa disparar a sincronização imediatamente via CLI ou automação e confirmar que nenhum `ExternalSecret` falhou.

## Como funciona
Como o controlador do ESO observa eventos de modificação (`Update`) no objeto `ExternalSecret` no API Server do Kubernetes, qualquer alteração nas anotações (`metadata.annotations`) do `ExternalSecret` dispara um ciclo imediato de reconciliação: executar **`kubectl annotate es <nome> force-sync=$(date +%s) --overwrite`** força o ESO a buscar imediatamente o novo valor no provedor externo e atualizar o `Secret`. Além disso, o ESO emite `Events` detalhados no próprio recurso (`Normal Created`, `Normal Updated` ou `Warning UpdateFailed`) e expõe métricas Prometheus na porta de métricas do controlador (como `externalsecret_sync_calls_total`, `externalsecret_sync_calls_error` e `externalsecret_status_condition`).

## Exemplo
```bash
# Forçar a ressincronização imediata de um ExternalSecret após rotacionar o segredo no cofre externo e checar eventos
kubectl annotate externalsecret database-credentials -n app-ns force-sync="$(date +%s)" --overwrite
kubectl describe externalsecret database-credentials -n app-ns
```

## Limites e trade-offs
Lembre-se de que quando o ESO atualiza o objeto `Kind=Secret` no Kubernetes, pods que consomem aquele `Secret` como **volume montado** recebem o arquivo atualizado automaticamente pelo `kubelet` (após o intervalo de sync do kubelet), mas pods que consomem o `Secret` como **variáveis de ambiente (`env` / `envFrom`)** não têm suas variáveis atualizadas em memória sem reiniciar o pod (sendo recomendável combinar o ESO com o `Reloader` da Stakater ou usar volumes).

## Como verificar
Após executar o comando `kubectl annotate ... force-sync=...`, verifique no `kubectl get secret <nome-do-secret> -o yaml` que o `resourceVersion` e os dados foram atualizados imediatamente.

## Conexões
- [[externalsecrets-cadeia-suprimentos-sbom-proveniencia-arquitetura-deployments]] — Veja também: External Secrets Operator: arquitetura de componentes no cluster (core controller, webhook, cert-controller) e SBOMs de release.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-ciclo-reconciliacao-creationpolicy-templates]] — Referência cruzada direta com externalsecrets-ciclo-reconciliacao-creationpolicy-templates.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
