---
id: software.devops.tranche20.001914
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://cert-manager.io/docs/trust/trust-manager/", "https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md", "https://github.com/cert-manager/trust-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# trust-manager Modelo de Segurança e *Trust Namespace*: por que fontes `Secret` e `ConfigMap` são restritas a um único namespace

## Em uma frase
O design de segurança do `trust-manager` restringe a leitura de fontes `Secret` e `ConfigMap` exclusivamente a um único namespace confiável do cluster — o **Trust Namespace** (configurado na instalação, padrão `cert-manager`) — enquanto grava os alvos (`targets`) nos demais namespaces dos aplicativos.

## Por que importa
Se o `Bundle` pudesse ler `Secrets` de qualquer namespace arbitrário e copiá-los para todos os outros namespaces do cluster, o `trust-manager` exigiria permissão RBAC `get/list/watch` de `Secrets` em nível de cluster (`ClusterRole`) e poderia ser explorado como vetor de exfiltração de segredos entre tenants.

## Como funciona
Ao confinar as fontes ao *Trust Namespace*, a `Role` de leitura de Secrets do `trust-manager` fica estritamente limitada àquele único namespace administrativo controlado pela equipe de plataforma/segurança, reduzindo drasticamente o *blast radius* de permissões no Kubernetes.

## Exemplo
```bash
# Instalando o trust-manager via Helm definindo um Trust Namespace dedicado:
helm upgrade --install trust-manager jetstack/trust-manager \
  --namespace cert-manager \
  --set app.trust.namespace=cert-manager \
  --wait
```

## Limites e trade-offs
Certifique-se de que apenas administradores de plataforma ou controladores de PKI (como o `cert-manager`) tenham permissão RBAC para criar ou modificar `Secrets` e `ConfigMaps` dentro do *Trust Namespace*.

## Como verificar
Inspecione as permissões RBAC do controlador com `kubectl get role,rolebinding -n cert-manager -l app.kubernetes.io/name=trust-manager`.

## Conexões
- [[trustmanager-seletores-dinamicos-includeallkeys-label-selector-sources]] — Veja também: trust-manager Fontes Dinâmicas: uso de `selector.matchLabels` e `includeAllKeys: true` em `ConfigMaps` e `Secrets`.
- [[trustmanager-formatos-adicionais-jks-pkcs12-java-dotnet-truststores]] — Veja também: trust-manager Formatos Binários (`additionalFormats`): geração automática de truststores `JKS` e `PKCS#12` (`.p12`) para Java e .NET.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
