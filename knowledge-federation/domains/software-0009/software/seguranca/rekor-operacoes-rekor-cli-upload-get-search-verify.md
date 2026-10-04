---
id: software.seguranca.tranche04.000383
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

# Sigstore Rekor: Operação com `rekor-cli` (`upload`, `get`, `search` e `verify`) por Hash, Chave ou E-mail

## Em uma frase
A ferramenta de linha de comando `rekor-cli` permite registrar entradas (`upload`), recuperar registros por UUID ou índice (`get`), pesquisar todas as assinaturas associadas a um hash SHA-256, chave pública ou e-mail OIDC (`search`) e validar provas de inclusão (`verify`).

## Por que importa
Permite que equipes de resposta a incidentes respondam imediatamente: *"quais artefatos foram assinados pela identidade `dev@empresa.com` nas últimas 48 horas?"* ou *"este binário possui entrada autêntica no log de transparência?"*.

## Como funciona
O comando `rekor-cli search` consulta o índice de busca reversa (`/api/v1/index/retrieve`) passando `--sha sha256:<hash>`, `--email usuario@dominio.com` ou `--public-key chave.pub`, retornando a lista de UUIDs de todas as entradas correspondentes registradas no log.

## Exemplo
```bash
# Pesquisar no Rekor todas as entradas associadas ao digest SHA-256 de um binário ou a um e-mail OIDC
rekor-cli search --sha sha256:3d80236772ca7c5405e398a4d685e715859260a8733070b86de7322e233c68d2

rekor-cli search --email release-bot@corp.example.com

# Inspecionar e verificar criptograficamente a prova de inclusão de uma entrada pelo índice
rekor-cli verify --log-index 12849502
```

## Limites e trade-offs
O comando `rekor-cli get` recupera o conteúdo da entrada mas **não** valida a prova matemática de inclusão na árvore de Merkle; para verificação criptográfica de auditoria, execute sempre `rekor-cli verify`.

## Como verificar
Execute `rekor-cli verify --artifact release.tar.gz --signature release.sig --public-key ec_public.pem` e confirme a saída da `Inclusion Proof` com o caminho de hashes da raiz.

## Conexões
- [[rekor-tipos-pluggable-hashedrekord-intoto-dsse-jar-rpm-tuf]] — Veja também: Sigstore Rekor: Esquemas Pluggable Types (`hashedrekord`, `rekord`, `intoto`, `dsse`, `jar`, `rpm` e `tuf`).
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Veja também: Sigstore Rekor: Provas Criptográficas de Árvore de Merkle (`Inclusion Proof`, `Consistency Proof`, `STH` e `SET`).
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
