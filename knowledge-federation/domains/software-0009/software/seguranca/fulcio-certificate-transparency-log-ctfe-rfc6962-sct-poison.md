---
id: software.seguranca.tranche04.000396
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

# Sigstore Fulcio: Certificate Transparency Log (`ctfe`), Precertificates (`OID 1.3.6.1.4.1.11129.2.4.3`) e SCT (`OID 1.3.6.1.4.1.11129.2.4.2`)

## Em uma frase
O Fulcio opera acoplado a um log de **Certificate Transparency (CT)** compatível com a RFC 6962 (`ctfe.sigstore.dev`), publicando obrigatoriamente cada certificado antes de entregá-lo ao cliente e embutindo o **Signed Certificate Timestamp (SCT)** na extensão X.509 `1.3.6.1.4.1.11129.2.4.2`.

## Por que importa
Impede que uma instância Fulcio comprometida ou um provedor OIDC malicioso emita um certificado "fantasma" para a identidade de um desenvolvedor sem deixar rastro público auditável no CT Log.

## Como funciona
Seguindo a RFC 6962, o Fulcio primeiro monta um **Precertificate** contendo a extensão crítica *Poison* (`1.3.6.1.4.1.11129.2.4.3` com valor `ASN.1 NULL`), assina-o com a CA e o submete ao servidor `ctfe` (que usa sharding anual, ex.: `/2024`, `/2025`, `/2026`). O `ctfe` retorna o **SCT** assinado; o Fulcio então remove a extensão *Poison*, insere o SCT na extensão `1.3.6.1.4.1.11129.2.4.2` e assina o certificado folha final.

## Exemplo
```bash
# Verificar a presença do Signed Certificate Timestamp (CT Precertificate SCTs) em um certificado Fulcio
openssl x509 -in fulcio-leaf.crt.pem -noout -text \
  | grep -A 8 "CT Precertificate SCTs"
```

## Limites e trade-offs
Clientes verificadores **NÃO DEVEM** confiar em certificados emitidos pelo Fulcio que não apresentem um SCT válido (embutido no OID `1.3.6.1.4.1.11129.2.4.2` ou no bundle) assinado pela chave pública do CT Log.

## Como verificar
Execute o comando `openssl x509` acima e confirme a presença de `Signed Certificate Timestamp: Version : v1 (0x0)` com o `Log ID` e `Timestamp` válidos.

## Conexões
- [[fulcio-provedores-oidc-meta-issuers-kubernetes-spiffe-ci]] — Veja também: Sigstore Fulcio: Configuração de Provedores OIDC (`config.json`), Meta-Issuers (EKS/GKE/AKS) e SPIFFE/Workload Identity.
- [[fulcio-fluxo-protocolo-create-signing-certificate-proof-possession]] — Veja também: Sigstore Fulcio: Fluxo Criptográfico da API v2 (`CreateSigningCertificate`) e Prova de Posse da Chave.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Referência cruzada direta com fulcio-especificacao-certificados-x509-san-critico-subject-vazio.
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Referência cruzada direta com fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao.

## Fontes
- [Sigstore Fulcio Official Certificate Specification — docs/certificate-specification.md (RFC 5280 Requirements for Root, Intermediate & Issued Certificates, Empty Subject, Critical SAN & OIDs)](https://raw.githubusercontent.com/sigstore/fulcio/main/README.md) — Especificação normativa oficial dos certificados Fulcio detalhando exigências RFC 5280, Subject vazio, SAN crítico, algoritmos de chave e extensões CT Poison/SCT; consultado em 2026-10-03.
- [Sigstore Fulcio Official Security Model — docs/security-model.md (OIDC Proof of Ownership, CT Log Mitigation, Short-Lived Certificates vs Revocation & Rekor Timestamps)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/certificate-specification.md) — Modelo de segurança oficial do Fulcio explicando como certificados de 10 minutos combinados ao timestamp de inclusão no Rekor eliminam a necessidade de revogação e re-assinatura; consultado em 2026-10-03.
- [Sigstore Fulcio GitHub — README.md (Free Root-CA for Code Signing, TUF Trust Root Initialization, Certificate Maker & CT Log)](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/security-model.md) — README oficial do sigstore/fulcio documentando a instância pública, inicialização via go-tuf, ferramenta certificate-maker e API v2; consultado em 2026-10-03.
