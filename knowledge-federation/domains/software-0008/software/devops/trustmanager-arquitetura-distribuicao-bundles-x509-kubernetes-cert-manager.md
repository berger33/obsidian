---
id: software.devops.tranche20.001911
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
fontes: ["https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md", "https://cert-manager.io/docs/trust/trust-manager/", "https://github.com/cert-manager/trust-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# trust-manager: arquitetura do operador Kubernetes do ecossistema `cert-manager` para distribuição de pacotes de confiança X.509 (`Bundle`)

## Em uma frase
O **trust-manager** (subprojeto oficial do ecossistema CNCF **cert-manager**) é um operador Kubernetes leve que automatiza a montagem e distribuição de pacotes de certificados X.509 confiáveis (*trust bundles*) através de todo o cluster por meio de um único Custom Resource cluster-scoped: **`Bundle`** (`trust.cert-manager.io/v1alpha1`).

## Por que importa
Quando uma empresa usa uma Autoridade Certificadora (CA) privada interna (gerenciada pelo `cert-manager` ou por um Vault/step-ca externo), reconstruir todas as imagens de container da empresa apenas para rodar `update-ca-certificates` toda vez que uma CA é adicionada ou rotacionada é lento e arriscado.

## Como funciona
O `trust-manager` lê certificados de múltiplas **fontes (`spec.sources`)** localizadas no *trust namespace* (incluindo `Secret`, `ConfigMap`, `inLine` e o pacote de CAs públicas padrão `useDefaultCAs: true`), combina e deduplica os certificados e sincroniza o pacote resultante automaticamente em **alvos (`spec.target`)** (`ConfigMaps` e/ou `Secrets` nos formatos PEM, JKS e PKCS#12) em todos os namespaces selecionados.

## Exemplo
```yaml
apiVersion: trust.cert-manager.io/v1alpha1
kind: Bundle
metadata:
  name: corp-ca-bundle
spec:
  sources:
    - useDefaultCAs: true
    - secret:
        name: "internal-root-ca-secret"
        key: "ca.crt"
  target:
    configMap:
      key: "ca-certificates.crt"
```

## Limites e trade-offs
Embora seja projetado para complementar o `cert-manager` (consumindo o `ca.crt` gerado por um `ClusterIssuer`), o `trust-manager` não depende do `cert-manager` para funcionar e pode ser operado de forma totalmente independente.

## Como verificar
Execute `kubectl get bundles` e `kubectl get configmap corp-ca-bundle -A` para verificar a sincronização automática do pacote de certificados nos namespaces.

## Conexões
- [[trustmanager-fontes-bundle-configmap-secret-inline-usedefaultcas]] — Veja também: trust-manager Fontes de Certificados (`spec.sources`): combinação de `configMap`, `secret`, `inLine` e `useDefaultCAs`.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://cert-manager.io/docs/trust/trust-manager/) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
