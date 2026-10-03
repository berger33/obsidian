---
id: software.seguranca.tranche04.000390
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

# Sigstore Rekor: Formato Sigstore Bundle (`.sigstore.json`) e Verificação 100% Offline de Inclusão e Tempo

## Em uma frase
O formato padronizado **Sigstore Bundle** (`application/vnd.dev.sigstore.bundle.v0.3+json`) empacota em um único arquivo JSON a assinatura do artefato, o certificado de curta duração do Fulcio e a entrada completa do Rekor (incluindo o `SignedEntryTimestamp` e a `InclusionProof` com checkpoint).

## Por que importa
Elimina a necessidade de que clusters Kubernetes de produção ou ambientes *air-gapped* façam chamadas de rede para `rekor.sigstore.dev` no momento do deploy: toda a prova matemática necessária para verificação offline já viaja junto ao artefato.

## Como funciona
O verificador offline (`cosign verify --offline` ou SDKs `sigstore-go`/`sigstore-python`) lê o `trusted_root.json` local, verifica que a `InclusionProof` do bundle reconstrói o `RootHash` assinado pela chave pública do Rekor, extrai o `IntegratedTime` autenticado e confirma que o certificado Fulcio estava dentro da sua janela de validade de 10 minutos naquele exato instante.

## Exemplo
```bash
# Inspecionar a prova de inclusão do Rekor e o carimbo de tempo embutidos em um Sigstore Bundle offline
jq '{
  mediaType,
  logIndex: .verificationMaterial.tlogEntries[0].logIndex,
  integratedTime: .verificationMaterial.tlogEntries[0].integratedTime,
  hasInclusionProof: (.verificationMaterial.tlogEntries[0].inclusionProof != null)
}' artifact.sigstore.json
```

## Limites e trade-offs
Um bundle que contenha apenas o `SignedEntryTimestamp` (promessa) sem o objeto `.inclusionProof` não satisfaz políticas rigorosas de verificação de árvore de Merkle v0.3; gere bundles sempre com versões modernas dos clientes Sigstore.

## Como verificar
Execute a inspeção `jq` acima sobre o arquivo `.sigstore.json` e confirme `"hasInclusionProof": true` e a validação do artefato em rede isolada (`--offline`).

## Conexões
- [[rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles]] — Veja também: Sigstore Rekor: Auto-Hospedagem Privada (`rekor-server`), KMS Signing, Limite `--max_request_body_size` e Sharding.
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Referência cruzada direta com rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth.
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Referência cruzada direta com fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao.
- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Referência cruzada direta com fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
