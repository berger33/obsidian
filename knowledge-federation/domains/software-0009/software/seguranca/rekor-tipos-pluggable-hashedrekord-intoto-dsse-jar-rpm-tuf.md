---
id: software.seguranca.tranche04.000382
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

# Sigstore Rekor: Esquemas Pluggable Types (`hashedrekord`, `rekord`, `intoto`, `dsse`, `jar`, `rpm` e `tuf`)

## Em uma frase
O Rekor valida cada entrada contra um esquema tipado (*Pluggable Types* em `pkg/types`), incluindo `hashedrekord`, `rekord`, `intoto`, `dsse`, `jar`, `rpm`, `alpine`, `helm`, `rfc3161` e `tuf`, além de múltiplos formatos de PKI (`x509`, `minisign`, `ssh`, `pgp`).

## Por que importa
Diferente de um banco de dados genérico onde qualquer JSON arbitrário pode ser salvo, o Rekor recusa a inserção se a assinatura criptográfica não corresponder exatamente ao hash SHA-256 e à chave pública/certificado declarados no tipo.

## Como funciona
O tipo padrão usado pelo `cosign` para assinar imagens e blobs é o **`hashedrekord`** (que recebe apenas o digest SHA-256 do artefato, a assinatura e o certificado X.509/chave pública, sem precisar enviar o arquivo inteiro ao servidor), enquanto atestações SLSA e SBOMs assinados utilizam os tipos **`dsse`** ou **`intoto`**.

## Exemplo
```bash
# Assinar um artefato com chave ECDSA P-256 e registrar no Rekor usando o tipo hashedrekord
DIGEST=$(sha256sum release.tar.gz | awk '{print $1}')
openssl dgst -sha256 -sign ec_private.pem -out release.sig release.tar.gz

rekor-cli upload \
  --type hashedrekord \
  --artifact-hash "${DIGEST}" \
  --signature release.sig \
  --pki-format x509 \
  --public-key ec_public.pem
```

## Limites e trade-offs
Usar o tipo legado `rekord` (em vez de `hashedrekord`) exige fazer upload do artefato completo para que o servidor calcule o hash, o que falha para binários grandes e expõe o conteúdo do artefato ao servidor.

## Como verificar
Consulte a entrada criada com `rekor-cli get --log-index <index> --format json` e confirme que `Body.HashedRekordObj.data.hash.value` contém o SHA-256 exato.

## Conexões
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Veja também: Sigstore Rekor: Arquitetura do Transparency Log Imutável de Cadeia de Suprimentos e Árvores de Merkle.
- [[rekor-operacoes-rekor-cli-upload-get-search-verify]] — Veja também: Sigstore Rekor: Operação com `rekor-cli` (`upload`, `get`, `search` e `verify`) por Hash, Chave ou E-mail.
- [[intoto-dsse-dead-simple-signing-envelope-pae-prevencao-ambiguidade]] — Referência cruzada direta com intoto-dsse-dead-simple-signing-envelope-pae-prevencao-ambiguidade.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
