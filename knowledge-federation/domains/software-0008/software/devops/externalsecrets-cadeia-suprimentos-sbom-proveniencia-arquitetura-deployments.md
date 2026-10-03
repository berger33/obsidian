---
id: software.devops.tranche10.000919
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

# External Secrets Operator: arquitetura de componentes no cluster (core controller, webhook, cert-controller) e SBOMs de release

## Em uma frase
Uma instalação completa do ESO no cluster compõe-se de três deployments (`external-secrets`, `external-secrets-webhook` e `external-secrets-cert-controller`), cujas imagens de container e releases oficiais no GitHub incluem **SBOM** e arquivos de proveniência anexados.

## Por que importa
Operadores de segurança que auditam imagens em clusters de produção precisam verificar a cadeia de suprimentos (SBOM e proveniência SLSA) do ESO, além de compreender a função de cada um dos três pods instalados pelo Helm chart para diagnosticar falhas de webhook ou de certificados TLS internos. O README oficial (`Software bill of materials`) destaca a anexação de SBOM e proveniência.

## Como funciona
Quando instalado no cluster, o ESO divide suas responsabilidades em três processos independentes: (1) **`external-secrets` (Core Controller)**: executa os loops de reconciliação de `SecretStore`, `ClusterSecretStore`, `ExternalSecret` e `PushSecret`; (2) **`external-secrets-webhook`**: expõe os endpoints HTTPS de `ValidatingWebhookConfiguration` e conversão de versões de CRDs (`v1beta1` <-> `v1`) para rejeitar recursos malformados imediatamente no `kubectl apply`; e (3) **`external-secrets-cert-controller`**: monitora os webhooks e os CRDs para gerar e rotacionar automaticamente os certificados TLS internos usados pelo API Server do Kubernetes para falar com o `external-secrets-webhook` (dispensando `cert-manager` externo por padrão).

## Exemplo
```bash
# Verificar os três deployments do External Secrets Operator e a configuração do ValidatingWebhook no cluster
kubectl get deployments -n external-secrets
kubectl get validatingwebhookconfigurations | grep external-secrets
```

## Limites e trade-offs
Em clusters que já utilizam o **`cert-manager`** como padrão corporativo para todos os certificados de webhooks internos, você pode desabilitar o deployment `cert-controller` do ESO no Helm chart (`certController.create=false` e `webhook.certManager.enabled=true`) para economizar um pod em memória e centralizar a emissão de certificados no `cert-manager`.

## Como verificar
Execute `kubectl logs -n external-secrets deploy/external-secrets-cert-controller` para confirmar que os certificados dos webhooks e CRDs foram injetados e validados sem erros.

## Conexões
- [[externalsecrets-geradores-dinamicos-password-uuid-ecr-sts]] — Veja também: External Secrets Operator: geração dinâmica de segredos e tokens com Generators (Password, UUID, ECR, VaultDynamicSecret).
- [[externalsecrets-operacao-forcada-refresh-troubleshooting-metricas]] — Veja também: External Secrets Operator: atualização imediata sob demanda (force-sync), métricas Prometheus e diagnóstico de eventos.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-seguranca-rbac-least-privilege-multi-controller]] — Referência cruzada direta com externalsecrets-seguranca-rbac-least-privilege-multi-controller.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
