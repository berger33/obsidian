---
id: software.seguranca.tranche04.000381
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

# Sigstore Rekor: Arquitetura do Transparency Log Imutável de Cadeia de Suprimentos e Árvores de Merkle

## Em uma frase
**Rekor** (do grego *"Record"*, projeto Sigstore / Linux Foundation sob Apache-2.0) é um livro-razão de transparência (*Transparency Log*) imutável, *append-only* e criptograficamente verificável para registrar assinaturas e metadados da cadeia de suprimentos de software.

## Por que importa
Impede ataques furtivos de assinatura retroativa ou uso silencioso de chaves comprometidas: toda assinatura registrada torna-se auditável publicamente com um carimbo de tempo confiável (`IntegratedTime`) que não pode ser apagado nem alterado.

## Como funciona
O servidor Rekor valida matematicamente a assinatura e o manifesto enviados via API REST (`/api/v1/log/entries`) antes de aceitá-los e inseri-los em uma árvore de Merkle gerenciada pelo backend **Trillian** (no Rekor v1) ou por **Tile-Based Logs / Trillian-Tessera** (na arquitetura Rekor v2 `rekor-tiles`), retornando um `LogIndex`, `UUID` e um `SignedEntryTimestamp` (SET).

## Exemplo
```bash
# Consultar informações da árvore de Merkle atual (TreeSize e RootHash assinado) da instância Rekor
rekor-cli loginfo --rekor_server https://rekor.sigstore.dev --format json | jq .
```

## Limites e trade-offs
O Rekor armazena apenas hashes, assinaturas, chaves públicas/certificados e metadados de atestação (com limite de 100 KB por entrada na instância pública `rekor.sigstore.dev`), nunca o binário ou imagem de container em si.

## Como verificar
Execute `rekor-cli loginfo` e confirme a validação criptográfica do `SignedTreeHead` (STH) usando a chave pública do log (`/api/v1/log/publicKey`).

## Conexões
- [[rekor-tipos-pluggable-hashedrekord-intoto-dsse-jar-rpm-tuf]] — Veja também: Sigstore Rekor: Esquemas Pluggable Types (`hashedrekord`, `rekord`, `intoto`, `dsse`, `jar`, `rpm` e `tuf`).
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Referência cruzada direta com rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
