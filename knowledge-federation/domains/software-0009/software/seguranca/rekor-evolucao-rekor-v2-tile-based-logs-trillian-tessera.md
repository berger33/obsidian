---
id: software.seguranca.tranche04.000385
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

# Sigstore Rekor: Evolução do Rekor v1 (Trillian gRPC + MySQL) para Rekor v2 (`rekor-tiles` e `Trillian-Tessera`)

## Em uma frase
A arquitetura **Rekor v2** (`sigstore/rekor-tiles`) substitui a pilha complexa do Rekor v1 (Trillian Log Server + Trillian Signer + MySQL + Redis) por um log baseado em ladrilhos estáticos (**Tile-Based Log** especificação C2SP `tlog-tiles`) construído sobre a biblioteca **Trillian-Tessera**.

## Por que importa
Reduz drasticamente o custo operacional e de infraestrutura ao permitir que as folhas e subárvores da árvore de Merkle sejam servidas diretamente como arquivos estáticos imutáveis (*tiles*) a partir de Object Storage (GCS, S3 ou POSIX) e CDNs.

## Como funciona
Em um *Tile-Based Log*, os nós internos da árvore de Merkle são agrupados em ladrilhos (*tiles*) de altura fixa endereçáveis por caminho determinístico (`/tile/<level>/<index>`). Os clientes verificam provas de inclusão e consistência buscando apenas alguns *tiles* cacheáveis em CDN e o arquivo `/checkpoint` assinado, eliminando cálculos dinâmicos pesados de banco de dados a cada leitura.

## Exemplo
```bash
# Inspecionar o checkpoint assinado (C2SP tlog-checkpoint) de uma instância Rekor / Tessera
curl -sS https://rekor.sigstore.dev/api/v1/log \
  | jq -r '.signedTreeHead'
```

## Limites e trade-offs
Durante a coexistência de múltiplos shards do Rekor (v1 sharding e v2 tiles), os clientes verificadores devem usar o `trusted_root.json` distribuído via Sigstore TUF para validar o `LogID` e a chave pública correta de cada shard histórico ou ativo.

## Como verificar
Verifique o campo `treeID` e `signedTreeHead` retornados por `/api/v1/log` (incluindo o array `inactiveShards`) e confirme que todos os shards constam no bundle TUF.

## Conexões
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Veja também: Sigstore Rekor: Provas Criptográficas de Árvore de Merkle (`Inclusion Proof`, `Consistency Proof`, `STH` e `SET`).
- [[rekor-monitoramento-continuo-rekor-monitor-checkpoints-identidades]] — Veja também: Sigstore Rekor: Auditoria e Monitoramento Contínuo com `rekor-monitor` (Consistência e Identidades OIDC).
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.
- [[rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles]] — Referência cruzada direta com rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
