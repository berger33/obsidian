---
id: software.seguranca.tranche04.000395
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/sigstore/fulcio/main/README.md", "https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md", "https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Fulcio: Configuração de Provedores OIDC (`config.json`), Meta-Issuers (EKS/GKE/AKS) e SPIFFE/Workload Identity

## Em uma frase
O arquivo de configuração de identidade do Fulcio (`--config-path=/etc/fulcio-config/config.json`) define a lista estrita de `OIDCIssuers` e `MetaIssuers` aceitos, o `ClientID` esperado (`sigstore` por padrão) e a regra de mapeamento do token para o SAN do certificado (`email`, `uri`, `spiffe`, `github-workflow`, `kubernetes`, `username`).

## Por que importa
Permite que instâncias corporativas do Fulcio aceitem exclusivamente tokens emitidos pelos clusters Kubernetes internos (ServiceAccount Token Projection), servidores SPIFFE/SPIRE, Keycloak/Dex corporativo ou instâncias GitLab self-hosted.

## Como funciona
Para o tipo `kubernetes`, o Fulcio extrai os claims `.kubernetes.io.namespace` e `.kubernetes.io.serviceaccount.name` do JWT do `kube-apiserver` e emite um certificado com SAN URI `https://kubernetes.io/namespaces/<ns>/serviceaccounts/<sa>`. Já `MetaIssuers` permite autorizar padrões de URL dinâmicos de provedores gerenciados (como `https://oidc.eks.*.amazonaws.com/id/*` ou `https://container.googleapis.com/v1/projects/*/locations/*/clusters/*`).

## Exemplo
```json
{
  "OIDCIssuers": {
    "https://dex.internal.corp": {
      "IssuerURL": "https://dex.internal.corp",
      "ClientID": "sigstore",
      "Type": "email"
    },
    "https://kubernetes.default.svc.cluster.local": {
      "IssuerURL": "https://kubernetes.default.svc.cluster.local",
      "ClientID": "sigstore",
      "Type": "kubernetes"
    }
  }
}
```

## Limites e trade-offs
Ao configurar um emissor do tipo `email` no Fulcio, a CA exige que o token OIDC contenha o claim `"email_verified": true`; provedores OIDC internos que omitam `email_verified` terão a solicitação de certificado rejeitada.

## Como verificar
Consulte `curl -sS https://fulcio.sigstore.dev/api/v2/configuration | jq .issuers` para inspecionar todos os emissores OIDC e tipos configurados na instância.

## Conexões
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Veja também: Sigstore Fulcio: Árvore de OIDs X.509 (`1.3.6.1.4.1.57264.1.*`) para GitHub Actions, GitLab CI e Buildkite.
- [[fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison]] — Veja também: Sigstore Fulcio: Certificate Transparency Log (`ctfe`), Precertificates (`OID 1.3.6.1.4.1.11129.2.4.3`) e SCT (`OID 1.3.6.1.4.1.11129.2.4.2`).
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[dexidp-arquitetura-cncf-federated-openid-connect-provider-connectors]] — Referência cruzada direta com dexidp-arquitetura-cncf-federated-openid-connect-provider-connectors.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
