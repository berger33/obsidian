---
id: software.devops.tranche11.001069
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
fontes: ["https://pluto.docs.fairwinds.com/quickstart/", "https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md", "https://pluto.docs.fairwinds.com/installation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Casos reais de detecção do Pluto: MutatingWebhookConfiguration, Ingress (v1beta1 -> v1) e PodSecurityPolicy

## Em uma frase
Os exemplos oficiais do Pluto ilustram três padrões clássicos de depreciação no Kubernetes: recursos administrativos de webhook (`admissionregistration.k8s.io/v1beta1` → `v1`), objetos de rede `Ingress` (`networking.k8s.io/v1beta1` → `v1`) e recursos removidos sem substituto direto de API (`policy/v1beta1` `PodSecurityPolicy`).

## Por que importa
Em clusters reais, as depreciações mais críticas frequentemente não estão nos Deployments das aplicações de negócio (que já migraram para `apps/v1` há anos), mas sim em **charts de infraestrutura** instalados anos atrás (como `cert-manager`, ingress controllers ou políticas `PodSecurityPolicy` padrão de provedores de nuvem como `eks.privileged`).

## Como funciona
Conforme demonstram as saídas reais na documentação *QuickStart* (`pluto.docs.fairwinds.com/quickstart/`): (1) ao executar `pluto detect-helm -owide`, o Pluto flagra por exemplo `cert-manager/cert-manager-webhook` (`MutatingWebhookConfiguration`) implantado com `admissionregistration.k8s.io/v1beta1` (depreciado na `v1.16.0`, removido na `v1.19.0`, substituto `admissionregistration.k8s.io/v1`); (2) ao executar `pluto detect-all-in-cluster -o wide`, flagra objetos `Ingress` com `networking.k8s.io/v1beta1` (depreciado na `v1.19.0`, removido na `v1.22.0`, substituto `networking.k8s.io/v1`); e (3) flagra `PodSecurityPolicy` (`eks.privileged` / `psp`) em `policy/v1beta1` (depreciado na `v1.21.0`, removido na `v1.25.0`, sem `REPLACEMENT` de mesmo Kind).

## Exemplo
```bash
# Inspecionar releases Helm e recursos de API em busca de webhooks, Ingresses ou CRDs com versões depreciadas
pluto detect-all-in-cluster -o wide 2>/dev/null
```

## Limites e trade-offs
Quando o `pluto detect-helm` aponta que uma release de infraestrutura (como `cert-manager` ou `ingress-nginx`) contém uma `apiVersion` depreciada, você não deve editar manualmente o objeto vivo no cluster com `kubectl edit`; a correção correta é atualizar a versão do Helm chart (`helm upgrade`) para uma release que emita a nova `apiVersion`.

## Como verificar
Após atualizar o Helm chart da ferramenta apontada, reexecute `pluto detect-helm -n <namespace> -owide` e confirme que a release não aparece mais na listagem de depreciações.

## Conexões
- [[pluto-migracao-registro-verificacao-cosign-checksums-v5-24]] — Veja também: Cadeia de suprimentos do Pluto (v5.24.0+): migração para Artifact Registry, tags imutáveis e verificação com Cosign.
- [[pluto-fluxo-pre-upgrade-clusters-kubernetes-gitops]] — Veja também: Roteiro de pré-upgrade de clusters Kubernetes combinando Pluto, Polaris e Popeye.
- [[pluto-deteccao-em-cluster-detect-helm-api-resources-all]] — Referência cruzada direta com pluto-deteccao-em-cluster-detect-helm-api-resources-all.
- [[pluto-diferenca-deprecated-vs-removed-politica-kubernetes]] — Referência cruzada direta com pluto-diferenca-deprecated-vs-removed-politica-kubernetes.
- [[pluto-armadilha-conversao-apiserver-last-applied-configuration]] — Referência cruzada direta com pluto-armadilha-conversao-apiserver-last-applied-configuration.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/quickstart/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
