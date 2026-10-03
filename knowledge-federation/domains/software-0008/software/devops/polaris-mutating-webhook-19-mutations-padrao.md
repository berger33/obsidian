---
id: software.devops.tranche11.001055
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
fontes: ["https://polaris.docs.fairwinds.com/admission-controller/", "https://polaris.docs.fairwinds.com/infrastructure-as-code/", "https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Mutating Webhook do Polaris (--set webhook.mutate=true) e as 19 checagens com suporte nativo a mutação

## Em uma frase
Quando instalado com **`--set webhook.mutate=true`**, o Admission Controller do Polaris passa a operar também como um **Mutating Webhook**, remediando automaticamente problemas nos workloads durante a admissão em vez de apenas rejeitá-los, com **19 checagens padrão** habilitadas para mutação.

## Por que importa
Em clusters de desenvolvimento ou plataformas onde se deseja aplicar padrões seguros automaticamente (como forçar `readOnlyRootFilesystem: true`, remover capabilities perigosas ou preencher requests/limits padrão), o Mutating Webhook corrige o manifesto em voo antes da persistência no etcd.

## Como funciona
Conforme lista a seção *Mutating Webhook* da documentação oficial (`polaris.docs.fairwinds.com/admission-controller/`), adicionar `--set webhook.mutate=true` na instalação Helm ativa a remediação automática para as seguintes **19 checagens padrão**: `hostPIDSet`, `hostNetworkSet`, `hostIPCSet`, `priorityClassNotSet`, `hostPortSet`, `pullPolicyNotAlways`, `deploymentMissingReplicas`, `dangerousCapabilities`, `cpuLimitsMissing`, `memoryLimitsMissing`, `livenessProbeMissing`, `memoryRequestsMissing`, `cpuRequestsMissing`, `runAsPrivileged`, `readinessProbeMissing`, `privilegeEscalationAllowed`, `notReadOnlyRootFilesystem`, `insecureCapabilities` e `runAsRootAllowed`. Mutações adicionais podem ser controladas pela flag `webhook.mutations`.

## Exemplo
```bash
# Instalar o Polaris via Helm habilitando tanto o Validating Webhook quanto o Mutating Webhook
helm upgrade --install polaris fairwinds-stable/polaris \
  --namespace polaris \
  --create-namespace \
  --set webhook.enable=true \
  --set webhook.mutate=true \
  --set dashboard.enable=true
```

## Limites e trade-offs
Usar um Mutating Webhook que altera campos do pod spec em tempo de admissão (como injetar `pullPolicyNotAlways`, `cpuRequestsMissing` ou `notReadOnlyRootFilesystem`) em clusters gerenciados por **Argo CD** ou **Flux** pode fazer com que o recurso vivo no cluster difira do YAML no Git (*OutOfSync*), além de quebrar containers que tentam escrever em caminhos fora de volumes montados quando `readOnlyRootFilesystem: true` é injetado; em ambientes GitOps estritos, prefira usar `polaris fix` no Git + Validating Webhook no cluster.

## Como verificar
Inspecione `kubectl get mutatingwebhookconfigurations` no cluster e verifique os campos `securityContext` e `resources` de um Deployment recém-aplicado no namespace monitorado.

## Conexões
- [[polaris-admission-controller-validating-mutating-webhook]] — Veja também: Polaris Admission Controller: instalação via Helm, certificados TLS (cert-manager vs caBundle) e comportamento diante de danger vs warning.
- [[polaris-categorias-checagens-seguranca-eficiencia-confiabilidade]] — Veja também: Categorias de políticas embutidas do Polaris: Segurança (SecurityContext/Host), Eficiência (CPU/Memory) e Confiabilidade (Probes/Replicas/Tags).
- [[polaris-remediacao-automatica-cli-polaris-fix-yaml]] — Referência cruzada direta com polaris-remediacao-automatica-cli-polaris-fix-yaml.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/admission-controller/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
