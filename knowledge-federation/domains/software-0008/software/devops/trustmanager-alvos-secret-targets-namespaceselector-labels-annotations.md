---
id: software.devops.tranche20.001916
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

# trust-manager Targets (`configMap` vs `secret`) e `namespaceSelector`: filtragem de namespaces e metadados para GitOps

## Em uma frase
Na seção **`spec.target`** de um `Bundle`, o `trust-manager` permite escolher se os pacotes de confiança serão gravados em recursos **`configMap`** e/ou **`secret`**, filtrar quais namespaces receberão o pacote usando **`namespaceSelector.matchLabels`** e propagar `labels` e `annotations` customizados (como `argocd.argoproj.io/sync-wave`) para os objetos gerados.

## Por que importa
Sincronizar um `ConfigMap` ou `Secret` em absolutamente todos os 200 namespaces do cluster (incluindo `kube-system` e namespaces de terceiros que não usam a CA) cria objetos desnecessários; além disso, algumas bibliotecas exigem montar o truststore a partir de um `Secret`.

## Como funciona
Se `namespaceSelector` for definido (ex.: `matchLabels: { "linkerd.io/inject": "enabled" }`), o `trust-manager` cria o recurso apenas nos namespaces com esse label — e remove o recurso automaticamente caso o label seja retirado de um namespace. Para usar `secret:` como target, habilite explicitamente `secretTargets.enabled=true` e `secretTargets.authorizedSecrets` no Helm chart do `trust-manager`.

## Exemplo
```yaml
spec:
  sources:
    - useDefaultCAs: true
  target:
    configMap:
      key: "root-certs.pem"
      metadata:
        annotations:
          argocd.argoproj.io/sync-wave: "1"
        labels:
          app.kubernetes.io/component: "trust-bundle"
    namespaceSelector:
      matchLabels:
        security.corp.io/inject-ca-bundle: "true"
```

## Limites e trade-offs
Se `namespaceSelector` for omitido ou deixado vazio no `Bundle`, o `trust-manager` sincroniza o target em **todos** os namespaces existentes e futuros do cluster.

## Como verificar
Adicione o label `security.corp.io/inject-ca-bundle=true` a um namespace de teste e verifique a criação imediata do `ConfigMap` naquele namespace.

## Conexões
- [[trustmanager-formatos-adicionais-jks-pkcs12-java-dotnet-truststores]] — Veja também: trust-manager Formatos Binários (`additionalFormats`): geração automática de truststores `JKS` e `PKCS#12` (`.p12`) para Java e .NET.
- [[trustmanager-integracao-cert-manager-ca-issuer-linkerd-istio-mtls]] — Veja também: trust-manager com `cert-manager` e Service Mesh: distribuição automática da CA raiz de mTLS para Linkerd, Istio e Pods.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
