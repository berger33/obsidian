---
id: software.devops.tranche11.001056
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
fontes: ["https://polaris.docs.fairwinds.com/admission-controller/", "https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md", "https://polaris.docs.fairwinds.com/infrastructure-as-code/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Categorias de políticas embutidas do Polaris: Segurança (SecurityContext/Host), Eficiência (CPU/Memory) e Confiabilidade (Probes/Replicas/Tags)

## Em uma frase
As mais de 30 políticas embutidas do Polaris avaliam os workloads Kubernetes em três pilares operacionais: **Segurança** (isolamento de host, capabilities Linux e `securityContext`), **Eficiência** (presença de `requests` e `limits` de CPU e memória) e **Confiabilidade** (probes de saúde, múltiplas réplicas e política de pull de imagens).

## Por que importa
Uma auditoria de cluster eficaz não pode olhar apenas para vulnerabilidades de segurança ignorando resiliência ou custos: um pod seguro que roda com `runAsNonRoot: true`, mas não possui `readinessProbe` nem `memoryLimits`, ainda derrubará o serviço durante um deploy ou esgotará a RAM do nó.

## Como funciona
A partir das políticas embutidas documentadas no Polaris (`polaris.docs.fairwinds.com/admission-controller/` e README): (1) no pilar de **Segurança**, checagens como `hostPIDSet`, `hostNetworkSet`, `hostIPCSet`, `hostPortSet`, `runAsPrivileged`, `runAsRootAllowed`, `privilegeEscalationAllowed`, `notReadOnlyRootFilesystem`, `dangerousCapabilities` e `insecureCapabilities` garantem o isolamento do container; (2) no pilar de **Eficiência**, `cpuRequestsMissing`, `cpuLimitsMissing`, `memoryRequestsMissing` e `memoryLimitsMissing` garantem previsibilidade de agendamento e proteção contra vazamentos de recursos; e (3) no pilar de **Confiabilidade**, `livenessProbeMissing`, `readinessProbeMissing`, `deploymentMissingReplicas`, `pullPolicyNotAlways` e `priorityClassNotSet` evitam pontos únicos de falha e inconsistências de imagem.

## Exemplo
```yaml
# Exemplo de Deployment que atende simultaneamente aos pilares de Segurança, Eficiência e Confiabilidade do Polaris
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-resiliente
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api-resiliente
  template:
    metadata:
      labels:
        app: api-resiliente
    spec:
      priorityClassName: high-priority
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: api
          image: ghcr.io/exemplo/api:v1.2.3
          imagePullPolicy: Always
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          resources:
            requests: { cpu: 100m, memory: 128Mi }
            limits: { cpu: 500m, memory: 256Mi }
          readinessProbe:
            httpGet: { path: /healthz, port: 8080 }
          livenessProbe:
            httpGet: { path: /livez, port: 8080 }
```

## Limites e trade-offs
Algumas checagens padrão (como `pullPolicyNotAlways` ou `priorityClassNotSet`) podem não ser desejadas para todos os ambientes (por exemplo, clusters locais `kind`/`minikube` com imagens carregadas localmente que exigem `imagePullPolicy: IfNotPresent` ou `Never`); o arquivo de configuração do Polaris permite ajustar a severidade de cada checagem para `ignore`, `warning` ou `danger`.

## Como verificar
Salve o manifesto acima em `./deploy/api.yaml` e execute `polaris audit --audit-path ./deploy/api.yaml --format=pretty` para verificar a aprovação nas três categorias.

## Conexões
- [[polaris-mutating-webhook-19-mutations-padrao]] — Veja também: Mutating Webhook do Polaris (--set webhook.mutate=true) e as 19 checagens com suporte nativo a mutação.
- [[polaris-politicas-customizadas-json-schema-exencoes]] — Veja também: Políticas customizadas com JSON Schema e configuração de severidades no Fairwinds Polaris.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/admission-controller/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
