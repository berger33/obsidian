---
id: software.devops.tranche20.001912
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

# trust-manager Fontes de Certificados (`spec.sources`): combinação de `configMap`, `secret`, `inLine` e `useDefaultCAs`

## Em uma frase
Um recurso `Bundle` do `trust-manager` constrói o pacote final de confiança concatenando certificados X.509 a partir de quatro tipos de fontes em **`spec.sources`**: **`configMap`**, **`secret`**, **`inLine`** (certificados PEM declarados diretamente no YAML) e **`useDefaultCAs: true`** (pacote de CAs públicas baseado no pacote `ca-certificates` do Debian).

## Por que importa
Se você montar em `/etc/ssl/certs/ca-certificates.crt` do seu Pod um `ConfigMap` que contenha **apenas** a CA privada interna da empresa, sua aplicação passará a confiar nos serviços internos mas deixará de confiar em APIs públicas na internet (Let's Encrypt, AWS, Google, GitHub)!

## Como funciona
Incluir `- useDefaultCAs: true` junto com o `secret` ou `configMap` da sua CA interna no mesmo `Bundle` resolve esse problema clássico: o `trust-manager` gera um único arquivo `ca-certificates.crt` contendo tanto todas as CAs públicas padrão do Debian quanto as CAs privadas da sua organização.

## Exemplo
```yaml
apiVersion: trust.cert-manager.io/v1alpha1
kind: Bundle
metadata:
  name: hybrid-public-private-bundle
spec:
  sources:
    - useDefaultCAs: true
    - configMap:
        name: "partner-root-ca"
        key: "root.pem"
    - inLine: |
        -----BEGIN CERTIFICATE-----
        MIIDCTCCAfGgAwIBAgIUX...
        -----END CERTIFICATE-----
  target:
    configMap:
      key: "bundle.pem"
```

## Limites e trade-offs
A menos que você fixe explicitamente a versão da imagem do pacote de CAs padrão na instalação do `trust-manager`, o conteúdo de `useDefaultCAs: true` acompanha as atualizações do pacote `ca-certificates` quando o `trust-manager` é atualizado.

## Como verificar
Verifique a quantidade de certificados combinados no `ConfigMap` gerado executando `kubectl get cm hybrid-public-private-bundle -o jsonpath='{.data.bundle\.pem}' | grep -c "BEGIN CERTIFICATE"`.

## Conexões
- [[trustmanager-arquitetura-distribuicao-bundles-x509-kubernetes-cert-manager]] — Veja também: trust-manager: arquitetura do operador Kubernetes do ecossistema `cert-manager` para distribuição de pacotes de confiança X.509 (`Bundle`).
- [[trustmanager-seletores-dinamicos-includeallkeys-label-selector-sources]] — Veja também: trust-manager Fontes Dinâmicas: uso de `selector.matchLabels` e `includeAllKeys: true` em `ConfigMaps` e `Secrets`.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
