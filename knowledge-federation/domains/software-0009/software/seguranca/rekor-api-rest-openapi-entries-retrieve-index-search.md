---
id: software.seguranca.tranche04.000388
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

# Sigstore Rekor: API REST v1 (`/api/v1/log`, `/api/v1/log/entries`, `/api/v1/index/retrieve`) e Limites Operacionais

## Em uma frase
O servidor Rekor expõe uma API REST padronizada sob especificação OpenAPI (Swagger) com SLO de 99,5% de disponibilidade na instância pública para os endpoints `/api/v1/log`, `/api/v1/log/publicKey`, `/api/v1/log/proof`, `/api/v1/log/entries` e `/api/v1/log/entries/retrieve`.

## Por que importa
Permite integrar verificação de transparência diretamente em controladores de admissão Kubernetes, gerenciadores de pacotes (npm provenance, PyPI, Homebrew, Maven) e portais de auditoria sem depender do binário `rekor-cli`.

## Como funciona
Uma chamada `POST /api/v1/index/retrieve` com payload JSON `{"hash": "sha256:..."}` retorna a lista de UUIDs de entradas; em seguida, `POST /api/v1/log/entries/retrieve` busca os corpos completos em lote (incluindo o `body` codificado em Base64, o `integratedTime` Unix epoch e o objeto `verification` com a `inclusionProof`).

## Exemplo
```bash
# Consultar a API REST do Rekor via curl pelo hash SHA-256 e decodificar o corpo da entrada
ENTRY_UUID=$(curl -sS -X POST https://rekor.sigstore.dev/api/v1/index/retrieve \
  -H "Content-Type: application/json" \
  -d '{"hash":"sha256:3d80236772ca7c5405e398a4d685e715859260a8733070b86de7322e233c68d2"}' | jq -r '.[0]')

curl -sS "https://rekor.sigstore.dev/api/v1/log/entries/${ENTRY_UUID}" \
  | jq -r 'to_entries[0].value.body' | base64 -d | jq .
```

## Limites e trade-offs
O índice de busca (`/api/v1/index/retrieve`) na instância pública é um auxílio de descoberta (*best-effort*) e não um componente criptográfico; sistemas de produção devem armazenar o Sigstore Bundle junto ao artefato em vez de depender de buscas por índice em tempo de execução.

## Como verificar
Execute a chamada `curl` acima contra `/api/v1/log/entries/<uuid>` e confirme a presença do objeto `.verification.inclusionProof` na resposta JSON.

## Conexões
- [[rekor-integracao-assinatura-ssh-minisign-x509-openpgp]] — Veja também: Sigstore Rekor: Registro de Assinaturas Não-Fulcio (`ssh-keygen -Y sign`, `minisign` e X.509 Tradicional).
- [[rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles]] — Veja também: Sigstore Rekor: Auto-Hospedagem Privada (`rekor-server`), KMS Signing, Limite `--max_request_body_size` e Sharding.
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Referência cruzada direta com rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
