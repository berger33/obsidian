---
id: software.devops.tranche10.000930
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
fontes: ["https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md", "https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md", "https://github.com/bitnami-labs/sealed-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Bitnami Sealed Secrets: instalação em ambientes restritos sem RBAC (controller-norbac.yaml) e escopo de namespaces

## Em uma frase
Para ambientes onde o operador não possui permissão para criar recursos RBAC em nível de cluster (`ClusterRole` / `ClusterRoleBinding`) ou onde um controlador deve gerenciar apenas um subconjunto de namespaces, o Sealed Secrets fornece o manifesto `controller-norbac.yaml` e flags de customização de namespace/escopo.

## Por que importa
Em grandes clusters corporativos compartilhados (como OpenShift ou clusters Kubernetes multi-tenant), uma equipe pode ter permissão administrativa apenas dentro dos seus próprios 3 namespaces, sem poder instalar operadores globais em `kube-system`. A seção `Installation in Restricted Environments (No RBAC)` e o FAQ do README oficial documentam como operar o controlador nesse cenário.

## Como funciona
(1) **Manifesto `controller-norbac.yaml`**: disponibilizado nas páginas de Releases oficiais, inclui apenas o `Deployment`, o `Service` e o `CustomResourceDefinition` (omitindo intencionalmente `ServiceAccount`, `ClusterRole` e `ClusterRoleBinding` para usar uma ServiceAccount previamente provisionada pelo administrador do cluster); (2) **Namespace customizado do controlador**: se o controlador não estiver rodando no namespace padrão `kube-system` nem com o nome padrão `sealed-secrets-controller`, o cliente `kubeseal` deve ser informado via flags **`--controller-namespace`** e **`--controller-name`** (ou variáveis `SEALED_SECRETS_CONTROLLER_NAMESPACE` e `SEALED_SECRETS_CONTROLLER_NAME`); e (3) **Subconjunto de namespaces**: o controlador pode ser restrito a observar apenas namespaces específicos usando `--additional-namespaces`.

## Exemplo
```bash
# Invocar o kubeseal apontando para um controlador instalado em um namespace e nome customizados da equipe
kubeseal \
  --controller-namespace team-alpha-system \
  --controller-name alpha-sealed-secrets \
  -o yaml < secret.yaml > sealed-secret.yaml
```

## Limites e trade-offs
Quando o controlador é instalado em um namespace diferente de `kube-system`, qualquer execução de `kubeseal` que tente conversar com o cluster sem passar `--controller-namespace` (ou sem usar `--cert` offline) falhará tentando procurar `sealed-secrets-controller` em `kube-system`; padronize `SEALED_SECRETS_CONTROLLER_NAMESPACE` ou `SEALED_SECRETS_CERT` no ambiente da equipe.

## Como verificar
Verifique o deployment do controlador no namespace customizado com `kubectl get deploy,svc -n <namespace>` e teste `kubeseal --controller-namespace <namespace> --controller-name <nome> --fetch-cert`.

## Conexões
- [[sealedsecrets-gke-privado-firewall-8080-warden-service-proxier]] — Veja também: Bitnami Sealed Secrets: operação em clusters GKE privados (firewall 8080/8081) e restrições do GKE Warden (system:authenticated).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-certificado-publico-fetch-cert-offline-url]] — Referência cruzada direta com sealedsecrets-certificado-publico-fetch-cert-offline-url.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
