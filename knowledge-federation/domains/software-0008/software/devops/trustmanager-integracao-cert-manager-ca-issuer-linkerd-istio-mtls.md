---
id: software.devops.tranche20.001917
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

# trust-manager com `cert-manager` e Service Mesh: distribuição automática da CA raiz de mTLS para Linkerd, Istio e Pods

## Em uma frase
Uma das aplicações mais poderosas do `trust-manager` em produção é fechar o ciclo de automação entre o **`cert-manager`** (que emite e rotaciona o certificado de CA em um `Secret` no namespace `cert-manager`) e os consumidores do cluster (como o plano de controle do **Linkerd** / **Istio** ou webhooks de admissão).

## Por que importa
No Linkerd, por exemplo, o `cert-manager` gera o certificado emissor `linkerd-identity-issuer` no namespace `linkerd`, mas a âncora de confiança pública (`ca.crt`) precisa ser distribuída como um `ConfigMap` (`linkerd-identity-trust-roots`) sem copiar a chave privada `tls.key` do Secret.

## Como funciona
Ao configurar um `Bundle` que lê apenas a chave `ca.crt` (ou `tls.crt`) do `Secret` da CA no namespace `cert-manager` e grava um `ConfigMap` contendo exclusivamente os certificados públicos, o `trust-manager` garante que a chave privada da CA nunca saia do Secret original.

## Exemplo
```yaml
apiVersion: trust.cert-manager.io/v1alpha1
kind: Bundle
metadata:
  name: linkerd-identity-trust-roots
spec:
  sources:
    - secret:
        name: "linkerd-trust-anchor"
        key: "tls.crt"
  target:
    configMap:
      key: "ca-bundle.crt"
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: "linkerd"
```

## Limites e trade-offs
Quando a CA passa por rotação (mantendo temporariamente o certificado antigo e o novo concatenados ou em Secrets selecionados por label), o `trust-manager` atualiza o `ConfigMap` instantaneamente e o kubelet propaga a atualização para os volumes montados nos Pods.

## Como verificar
Verifique que o `ConfigMap` gerado em `linkerd` contém apenas `-----BEGIN CERTIFICATE-----` e nenhum bloco `PRIVATE KEY`.

## Conexões
- [[trustmanager-alvos-secret-targets-namespaceselector-labels-annotations]] — Veja também: trust-manager Targets (`configMap` vs `secret`) e `namespaceSelector`: filtragem de namespaces e metadados para GitOps.
- [[trustmanager-montagem-volumes-pods-subpath-armadilha-atualizacao-kubelet]] — Veja também: trust-manager Montagem em Pods: atualização automática de `ConfigMap` pelo `kubelet` vs armadilha de `volumeMounts.subPath`.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
