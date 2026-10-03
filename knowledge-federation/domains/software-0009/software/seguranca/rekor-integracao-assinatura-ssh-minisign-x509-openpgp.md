---
id: software.seguranca.tranche04.000387
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

# Sigstore Rekor: Registro de Assinaturas Não-Fulcio (`ssh-keygen -Y sign`, `minisign` e X.509 Tradicional)

## Em uma frase
Embora faça parte do ecossistema Sigstore junto ao Fulcio, o Rekor funciona de forma totalmente independente para registrar assinaturas criadas com chaves **SSH Ed25519** (`ssh-keygen -Y sign`), **Minisign** (`minisign -S`), **X.509/PKIX** (`openssl dgst`) ou **OpenPGP/GPG**.

## Por que importa
Permite que projetos que já utilizam chaves SSH ou Minisign obtenham um carimbo de tempo imutável (`IntegratedTime`) e transparência pública de todas as releases assinadas sem alterar seu formato de chave.

## Como funciona
Ao invocar `rekor-cli upload --artifact <file> --signature <sig> --pki-format=<ssh|minisign|x509|pgp> --public-key=<pub>`, o Rekor valida a assinatura específica do formato escolhido (por exemplo, o envelope `-----BEGIN SSH SIGNATURE-----` com namespace `file`) e grava a entrada `rekord` ou `hashedrekord` no log.

## Exemplo
```bash
# Assinar um arquivo de release com chave SSH Ed25519 e registrar a assinatura no Rekor
ssh-keygen -Y sign -n file -f ~/.ssh/id_ed25519 CHECKSUMS.txt

rekor-cli upload \
  --artifact CHECKSUMS.txt \
  --signature CHECKSUMS.txt.sig \
  --pki-format=ssh \
  --public-key=~/.ssh/id_ed25519.pub
```

## Limites e trade-offs
No formato SSH (`--pki-format=ssh`), o Rekor espera que a assinatura tenha sido gerada com o namespace `-n file`; usar um namespace arbitrário diferente sem correspondência no verificador causará falha de validação.

## Como verificar
Execute `rekor-cli get --uuid <uuid>` na entrada recém-criada e verifique que `signature.format` consta como `"ssh"` (ou `"minisign"`) com a chave pública preservada em Base64.

## Conexões
- [[rekor-monitoramento-continuo-rekor-monitor-checkpoints-identidades]] — Veja também: Sigstore Rekor: Auditoria e Monitoramento Contínuo com `rekor-monitor` (Consistência e Identidades OIDC).
- [[rekor-api-rest-openapi-entries-retrieve-index-search]] — Veja também: Sigstore Rekor: API REST v1 (`/api/v1/log`, `/api/v1/log/entries`, `/api/v1/index/retrieve`) e Limites Operacionais.
- [[rekor-tipos-pluggable-hashedrekord-intoto-dsse-jar-rpm-tuf]] — Referência cruzada direta com rekor-tipos-pluggable-hashedrekord-intoto-dsse-jar-rpm-tuf.
- [[rekor-operacoes-rekor-cli-upload-get-search-verify]] — Referência cruzada direta com rekor-operacoes-rekor-cli-upload-get-search-verify.
- [[intoto-sign-assinatura-multiplas-chaves-thresholds-gpg-ssh-ed25519]] — Referência cruzada direta com intoto-sign-assinatura-multiplas-chaves-thresholds-gpg-ssh-ed25519.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
