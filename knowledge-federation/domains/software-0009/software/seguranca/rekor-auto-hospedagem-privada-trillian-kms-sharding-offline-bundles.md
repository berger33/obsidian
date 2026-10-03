---
id: software.seguranca.tranche04.000389
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

# Sigstore Rekor: Auto-Hospedagem Privada (`rekor-server`), KMS Signing, Limite `--max_request_body_size` e Sharding

## Em uma frase
Organizações que não podem publicar metadados de builds proprietários (nomes de pacotes internos, e-mails de engenheiros ou SBOMs maiores que o limite público de 100 KB) no `rekor.sigstore.dev` implantam uma instância privada do **`rekor-server`**.

## Por que importa
Permite manter todas as garantias criptográficas de não-repúdio e auditoria imutável dentro da rede corporativa e aumentar o limite de tamanho de atestações (`--max_request_body_size`) para acomodar SBOMs extensos.

## Como funciona
O `rekor-server` conecta-se a um Trillian Log Server (ou backend Tessera), assina os `SignedTreeHeads` e `SignedEntryTimestamps` usando uma chave privada protegida em HSM/Cloud KMS (`--rekor_server.signer=gcpkms://...`, AWS KMS, Azure Key Vault ou HashiCorp Vault) e suporta rotação de árvores via `--sharding_config` sem invalidar entradas de árvores anteriores.

## Exemplo
```bash
# Iniciar rekor-server corporativo assinando a árvore via Cloud KMS e aceitando atestações de até 2 MB
rekor-server serve \
  --trillian_log_server.address=trillian-logserver.internal.corp \
  --trillian_log_server.port=8090 \
  --trillian_log_server.tlog_id=482910492 \
  --rekor_server.signer="awskms:///arn:aws:kms:us-east-1:111122223333:key/mrk-9a8b7c" \
  --max_request_body_size=2097152
```

## Limites e trade-offs
Usar `--rekor_server.signer=memory` gera uma chave efêmera em RAM que é perdida no primeiro restart do pod, invalidando permanentemente a verificação de todas as entradas gravadas anteriormente; use sempre Cloud KMS ou HSM em produção.

## Como verificar
Consulte `rekor-cli loginfo --rekor_server https://rekor.internal.corp` e distribua a chave pública do log no repositório TUF interno dos verificadores.

## Conexões
- [[rekor-api-rest-openapi-entries-retrieve-index-search]] — Veja também: Sigstore Rekor: API REST v1 (`/api/v1/log`, `/api/v1/log/entries`, `/api/v1/index/retrieve`) e Limites Operacionais.
- [[rekor-sigstore-bundle-verificacao-offline-signed-timestamps]] — Veja também: Sigstore Rekor: Formato Sigstore Bundle (`.sigstore.json`) e Verificação 100% Offline de Inclusão e Tempo.
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.
- [[rekor-evolucao-rekor-v2-tile-based-logs-trillian-tessera]] — Referência cruzada direta com rekor-evolucao-rekor-v2-tile-based-logs-trillian-tessera.
- [[fulcio-implantacao-privada-certificate-maker-kms-pkcs11-tuf]] — Referência cruzada direta com fulcio-implantacao-privada-certificate-maker-kms-pkcs11-tuf.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
