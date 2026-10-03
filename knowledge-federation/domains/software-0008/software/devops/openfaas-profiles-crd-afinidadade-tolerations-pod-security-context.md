---
id: software.devops.tranche19.001808
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS `Profile` CRD: aplicação reutilizável de `affinity`, `tolerations`, `runtimeClassName` e `podSecurityContext`

## Em uma frase
No `faas-netes`, o Custom Resource **`Profile`** (`openfaas.com/v1`, criado no namespace `openfaas`) permite definir políticas avançadas de agendamento e segurança do Kubernetes (`tolerations`, `affinity`, `podSecurityContext`, `runtimeClassName`, `dnsPolicy`) que podem ser aplicadas a qualquer função por meio da anotação `com.openfaas.profile`.

## Por que importa
Expor toda a especificação bruta de um Pod Kubernetes dentro do `stack.yaml` do desenvolvedor quebraria a simplicidade da abstração serverless; com `Profiles`, a equipe de plataforma define perfis nomeados (ex.: `gpu-nodes`, `arm64-spot`, `restricted-pss`) e o desenvolvedor apenas referencia o nome do perfil.

## Como funciona
Quando uma função possui a anotação `com.openfaas.profile: gpu-nodes,restricted-pss`, o `faas-netes` busca os objetos `Profile` correspondentes e injeta as regras de afinidade, tolerations e contextos de segurança no `Deployment` gerado em `openfaas-fn`.

## Exemplo
```yaml
apiVersion: openfaas.com/v1
kind: Profile
metadata:
  name: spot-workers
  namespace: openfaas
spec:
  tolerations:
    - key: "spot-instance"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"
```

## Limites e trade-offs
Os objetos `Profile` devem ser criados no namespace do controlador (`openfaas`), mesmo que as funções que os consomem rodem no namespace `openfaas-fn`.

## Como verificar
Aplique um `Profile` em `openfaas`, adicione a anotação `com.openfaas.profile` em uma função e confirme em `kubectl get deploy -n openfaas-fn -o yaml` que a `toleration` foi injetada.

## Conexões
- [[openfaas-gerenciamento-secrets-kubernetes-mounted-var-openfaas-secrets]] — Veja também: OpenFaaS Secrets: gerenciamento declarativo de segredos montados como arquivos em `/var/openfaas/secrets/`.
- [[openfaas-event-connectors-cron-connector-kafka-sqs-annotations]] — Veja também: OpenFaaS Event Connectors e Cron: disparo de funções por tópicos (`topic` annotation) e agendamentos `cron-connector`.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
