---
id: software.seguranca.tranche04.000384
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

# Sigstore Rekor: Provas Criptográficas de Árvore de Merkle (`Inclusion Proof`, `Consistency Proof`, `STH` e `SET`)

## Em uma frase
A confiança no Rekor baseia-se em três primitivas criptográficas verificáveis pelo cliente sem precisar confiar cegamente no operador do servidor: **Signed Entry Timestamp (SET)**, **Inclusion Proof** e **Consistency Proof** entre **Signed Tree Heads (STH)**.

## Por que importa
Impede ataques de *split-view* ou reescrita de histórico: se o servidor tentasse remover ou alterar uma entrada antiga, o `RootHash` da árvore de Merkle mudaria e quebraria a prova de consistência contra qualquer cliente que guardou um STH anterior.

## Como funciona
O **SET** é uma promessa assinada pelo Rekor no instante do upload contendo o `IntegratedTime` (análoga ao SCT do Certificate Transparency). A **Inclusion Proof** fornece os nós irmãos do caminho da folha até a raiz da árvore de Merkle (`RootHash`), provando que a entrada realmente faz parte da árvore. Já a **Consistency Proof** (`/api/v1/log/proof`) prova matematicamente que a árvore no tamanho $N_2$ é uma extensão estritamente *append-only* da árvore anterior no tamanho $N_1$.

## Exemplo
```bash
# Obter e verificar prova de consistência entre um checkpoint antigo (first-size) e o estado atual
rekor-cli logproof \
  --first-size 10000000 \
  --last-size 12000000 \
  --rekor_server https://rekor.sigstore.dev
```

## Limites e trade-offs
Confiar apenas no `SignedEntryTimestamp` (SET) sem verificar a `Inclusion Proof` (ou sem monitorar a árvore) confia que o servidor incorporará a promessa na árvore; os bundles Sigstore modernos já embutem a `Inclusion Proof` completa junto ao SET.

## Como verificar
Execute `rekor-cli logproof --last-size <TreeSize>` e confirme a validação matemática da consistência da árvore.

## Conexões
- [[rekor-operacoes-rekor-cli-upload-get-search-verify]] — Veja também: Sigstore Rekor: Operação com `rekor-cli` (`upload`, `get`, `search` e `verify`) por Hash, Chave ou E-mail.
- [[rekor-evolucao-rekor-v2-tile-based-logs-trillian-tessera]] — Veja também: Sigstore Rekor: Evolução do Rekor v1 (Trillian gRPC + MySQL) para Rekor v2 (`rekor-tiles` e `Trillian-Tessera`).
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.
- [[rekor-monitoramento-continuo-rekor-monitor-checkpoints-identidades]] — Referência cruzada direta com rekor-monitoramento-continuo-rekor-monitor-checkpoints-identidades.
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Referência cruzada direta com fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao.

## Fontes
- [Sigstore Rekor GitHub — README.md (Supply Chain Transparency Log Architecture, Public Instance SLOs, Rekor v2 Tile-Based Logs & Extensibility)](https://raw.githubusercontent.com/sigstore/rekor/main/README.md) — README oficial do sigstore/rekor descrevendo o ledger imutável de assinaturas, endpoints da API REST v1 e evolução para Rekor v2 baseado em tiles e Trillian-Tessera; consultado em 2026-10-03.
- [Sigstore Rekor Official Types Documentation — types.md (Signing and Uploading Pluggable Types: Minisign, SSH, PKIX/X509, TUF & HashedRekord)](https://raw.githubusercontent.com/sigstore/rekor/main/types.md) — Documentação oficial types.md do Rekor demonstrando a assinatura, upload e verificação de entradas nos esquemas plugáveis; consultado em 2026-10-03.
- [Sigstore Official Documentation — Rekor Overview](https://docs.sigstore.dev/rekor/overview/) — Visão geral oficial do Rekor na documentação do projeto Sigstore; consultado em 2026-10-03.
