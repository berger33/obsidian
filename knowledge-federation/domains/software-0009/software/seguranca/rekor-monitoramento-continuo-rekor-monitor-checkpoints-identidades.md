---
id: software.seguranca.tranche04.000386
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
fontes: ["https://raw.githubusercontent.com/sigstore/rekor/main/README.md", "https://raw.githubusercontent.com/sigstore/rekor/main/types.md", "https://docs.sigstore.dev/rekor/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Rekor: Auditoria e Monitoramento Contínuo com `rekor-monitor` (Consistência e Identidades OIDC)

## Em uma frase
Um *Transparency Log* só cumpre sua garantia de segurança se for continuamente auditado por monitores independentes: o **`sigstore/rekor-monitor`** verifica periodicamente tanto a integridade matemática da árvore (provas de consistência entre checkpoints) quanto o surgimento de assinaturas para identidades específicas.

## Por que importa
Se a conta OIDC de um mantenedor ou um workflow do GitHub Actions sofrer comprometimento e for usada para assinar um artefato malicioso via Fulcio, o certificado e a assinatura aparecerão obrigatoriamente no Rekor e serão detectados pelo `rekor-monitor`.

## Como funciona
Executado como um GitHub Actions agendado ou CronJob Kubernetes, o `rekor-monitor` persiste o último checkpoint verificado, valida a `Consistency Proof` até o novo `TreeSize` e varre todas as entradas novas buscando correspondências com os `Subject Alternative Names` (e-mails ou URIs de workflows), emissores OIDC ou fingerprints de chaves configurados.

## Exemplo
```yaml
# Configuração de identidades monitoradas pelo rekor-monitor para alertas de segurança
monitoredValues:
  certIdentities:
    - certSubject: "https://github.com/org-corp/payments-service/.github/workflows/release.yml@refs/tags/.*"
      issuers:
        - "https://token.actions.githubusercontent.com"
    - certSubject: "security-release@corp.example.com"
      issuers:
        - "https://accounts.google.com"
```

## Limites e trade-offs
Executar o `rekor-monitor` sem persistir o arquivo de checkpoint anterior entre as execuções impede a validação de consistência histórica (*split-view detection*) entre execuções consecutivas.

## Como verificar
Execute o binário `rekor-monitor` com `--once=true` apontando para um arquivo de identidades de teste e confirme a validação do checkpoint e a geração de log de entradas encontradas.

## Conexões
- [[rekor-evolucao-rekor-v2-tile-based-logs-trillian-tessera]] — Veja também: Sigstore Rekor: Evolução do Rekor v1 (Trillian gRPC + MySQL) para Rekor v2 (`rekor-tiles` e `Trillian-Tessera`).
- [[rekor-integracao-assinatura-ssh-minisign-x509-openpgp]] — Veja também: Sigstore Rekor: Registro de Assinaturas Não-Fulcio (`ssh-keygen -Y sign`, `minisign` e X.509 Tradicional).
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Referência cruzada direta com rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Referência cruzada direta com fulcio-extensoes-x509-oids-57264-github-actions-ci-claims.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
