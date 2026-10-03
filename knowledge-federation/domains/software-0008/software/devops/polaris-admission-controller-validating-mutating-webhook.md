---
id: software.devops.tranche11.001054
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

# Polaris Admission Controller: instalação via Helm, certificados TLS (cert-manager vs caBundle) e comportamento diante de danger vs warning

## Em uma frase
O Polaris pode ser implantado no cluster como um **Admission Controller** (`--set webhook.enable=true`) que atua por padrão como um **Validating Webhook**, rejeitando qualquer workload que dispare uma checagem de nível **`danger`** enquanto permite a passagem de checagens de nível **`warning`**.

## Por que importa
Mesmo que a organização possua checagens no CI/CD, alguém com acesso `kubectl apply` ou um controlador de terceiros pode tentar criar um pod privilegiado (`runAsPrivileged`) ou com `hostPID: true` diretamente no cluster. O Validating Webhook do Polaris atua como barreira final no Kubernetes API Server.

## Como funciona
Segundo a página *Admission Controller* (`polaris.docs.fairwinds.com/admission-controller/`): (1) o webhook aceita a mesma configuração do dashboard e exige um certificado TLS válido — funcionando automaticamente se o **cert-manager** estiver instalado no cluster, ou exigindo fornecer manualmente `webhook.caBundle` e `webhook.secretName` apontando para um Secret TLS; (2) o webhook vem com suporte embutido para os principais controladores (`Deployments`, `Jobs`, `DaemonSets` etc.), podendo-se adicionar novos tipos via `webhook.rules` no Helm chart; e (3) no modo padrão (pass/fail), o webhook **rejeita apenas workloads que acionem uma checagem de severidade `danger`**; checagens com severidade `warning` passam na validação do webhook (ficando registradas apenas no Polaris Dashboard ou nos logs do webhook, pois não são exibidas na saída do `kubectl` a menos que o workload seja rejeitado).

## Exemplo
```bash
# Instalar apenas o Admission Controller (Validating Webhook) do Polaris via Helm chart oficial
helm repo add fairwinds-stable https://charts.fairwinds.com/stable && helm repo update fairwinds-stable
helm upgrade --install polaris fairwinds-stable/polaris \
  --namespace polaris \
  --create-namespace \
  --set webhook.enable=true \
  --set dashboard.enable=false
```

## Limites e trade-offs
Se você deseja que uma determinada violação (que por padrão no Polaris tem severidade `warning`, como ausência de probes ou limites) seja efetivamente **bloqueada** pelo Validating Webhook no `kubectl apply`, você deve elevar a severidade dessa checagem de `warning` para `danger` na configuração customizada do Polaris.

## Como verificar
Verifique o registro do webhook com `kubectl get validatingwebhookconfigurations` e tente aplicar um manifesto de teste violando uma regra `danger` para confirmar o bloqueio imediato pelo API Server.

## Conexões
- [[polaris-remediacao-automatica-cli-polaris-fix-yaml]] — Veja também: Remediação automática de manifestos YAML na CLI com polaris fix --files-path e --checks.
- [[polaris-mutating-webhook-19-mutations-padrao]] — Veja também: Mutating Webhook do Polaris (--set webhook.mutate=true) e as 19 checagens com suporte nativo a mutação.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.

## Fontes
- [Fairwinds Polaris Official Documentation — Infrastructure as Code (polaris audit, polaris fix, Exit Code Flags, Helm & GitHub Action)](https://polaris.docs.fairwinds.com/admission-controller/) — Guia oficial de Infrastructure as Code do Polaris cobrindo polaris audit, polaris fix, --set-exit-code-on-danger, --set-exit-code-below-score, auditoria de Helm charts e setup-polaris GitHub Action; consultado em 2026-10-03.
- [Fairwinds Polaris Official Documentation — Admission Controller & README (Validating/Mutating Webhook, 19 Default Mutations & v10.2.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/polaris/master/README.md) — Documentação oficial do Admission Controller e README do Polaris detalhando Validating Webhook (danger vs warning), Mutating Webhook (--set webhook.mutate=true com 19 mutações padrão), políticas JSON Schema e imagens imutáveis v10.2.0+; consultado em 2026-10-03.
- [Fairwinds Polaris — Official Documentation & Repository](https://polaris.docs.fairwinds.com/infrastructure-as-code/) — Documentação e repositório oficial do Fairwinds Polaris; consultado em 2026-10-03.
