---
id: software.seguranca.tranche05.000449
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/paralus/paralus/main/README.md", "https://www.paralus.io/docs/", "https://www.paralus.io/docs/usage/audit-logs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Paralus: Criação de `Custom Roles` Restritivas (Bloqueio de `pods/exec`, `pods/portforward` e Leitura de `secrets`)

## Em uma frase
Enquanto o papel padrão `admin` ou `edit` do Kubernetes permite executar comandos arbitrários dentro de containers (`pods/exec`), abrir túneis diretos (`pods/portforward`) e ler variáveis sensíveis (`secrets`), o sistema de **`Custom Roles`** do Paralus permite compor permissões cirúrgicas por `apiGroups`, `resources` e `verbs`.

## Por que importa
Bloquear `pods/exec`, `pods/attach` e leitura de `secrets` em clusters de produção permite que desenvolvedores inspecionem logs (`pods/log`), eventos e estado de Deployments para depuração sem poder extrair chaves privadas da memória do container.

## Como funciona
No Paralus, o administrador cria uma `Custom Role` de escopo `NAMESPACE` contendo apenas os recursos `pods`, `pods/log`, `deployments`, `events`, `configmaps` com verbos `get`, `list`, `watch`, omitindo explicitamente `secrets` e `pods/exec`, e a associa ao grupo de desenvolvedores em todos os clusters de produção.

## Exemplo
```yaml
# Especificação de Custom Role de observabilidade segura sem acesso a secrets ou pods/exec
kind: Role
metadata:
  name: prod-developer-safe-troubleshoot
spec:
  scope: NAMESPACE
  rolepermissions:
    - apiGroups: ["", "apps"]
      resources: ["pods", "pods/log", "events", "deployments", "replicasets"]
      verbs: ["get", "list", "watch"]
```

## Limites e trade-offs
Conceder o verbo `create` ou `patch` sobre `deployments` ou `pods` no mesmo namespace onde reside uma `ServiceAccount` privilegiada equivale indiretamente a conceder acesso aos `secrets` daquele namespace, pois o usuário poderia alterar a imagem do pod para exfiltrar os segredos montados.

## Como verificar
Associe a `Custom Role` acima a uma conta de teste e confirme que `kubectl logs pod/app -n payments` sucede enquanto `kubectl exec -it pod/app -n payments -- sh` e `kubectl get secrets -n payments` são negados (`Forbidden`).

## Conexões
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — Veja também: CNCF Paralus: Trilhas de Auditoria Imutáveis (`System Audit Logs` e `Kubectl / Relay Audit Logs`) para Conformidade e SIEM.
- [[paralus-hardening-producao-postgres-kratos-tls-networkpolicies]] — Veja também: CNCF Paralus: Hardening da Própria Instalação do Paralus (Certificados TLS, Isolamento de Rede e Proteção de Segredos).
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — Referência cruzada direta com paralus-organizacao-projects-groups-custom-roles-namespace-rbac.
- [[kubearmor-protecao-arquivos-sensi-readonly-fromsource-serviceaccount-token]] — Referência cruzada direta com kubearmor-protecao-arquivos-sensi-readonly-fromsource-serviceaccount-token.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
