# Status de consolidação rumo a 1 milhão materializado — CONCLUÍDO (100%)

Data: 2026-10-01

## Estado final alcançado

A federação atingiu **100% da meta de 1 milhão de notas** no **ledger SQLite**, na **sequência de 5.000 lotes materializados** e na **cobertura completa dos 78 subdomínios em Study Packs curados**.

```text
Notas virtuais no ledger: 1.000.000
Notas físicas iniciais: 100
Total lógico no ledger: 1.000.100 notas

Pacotes sequenciais materializados: 50 (0001-0100 até 4901-5000)
Lotes sequenciais materializados: 5.000
Notas por lote: 200
Notas sequenciais materializadas: 1.000.000

Study Packs curados por subdomínio: 78 (100% da taxonomia)
Notas por Study Pack: 200
Notas do vault consolidado curado: 15.600
Links wiki auditados no vault curado: 93.894 (0 quebrados)

Total materializado representado no merge completo: 1.015.600 notas
Entradas totais no TAR do merge completo: 1.021.127
Lotes em domínios regulados: 1.288
Conteúdo operacional regulado: 0
```

## O que foi finalizado nas últimas etapas

1. **Execução dos 1.700 lotes finais (`lote-3301` a `lote-5000`)**:
   - 17 pacotes de 100 lotes (`340.000 notas materializadas`), completando os **5.000 lotes = 1.000.000 de notas sequenciais**.
   - Relatórios individuais em `exports/reports/lotes-3301-3400-report.md` até `lotes-4901-5000-report.md` e resumo em `knowledge-federation/LOTS-3301-5000.md`.

2. **Expansão do Study Vault Curado de 36 para todos os 78 subdomínios (`15.600 notas`)**:
   - Foram gerados os 42 study packs faltantes e padronizados todos os **78 subdomínios** com **200 notas cada** (`78 × 200 = 15.600 notas`).
   - Adicionados **7 MOCs mestres de domínio**, **78 MOCs de subdomínio** e **9 arquivos Canvas** (`Mapa-Geral.canvas`, `Trilhas-e-Playbooks.canvas` e 7 mapas por domínio).
   - Auditados **93.894 wiki links** com **0 links quebrados** (`exports/reports/auditoria-study-vault.md`).

3. **Construção completa do `00-home-vault/` (Home Vault Mestre)**:
   - `Home.md`, `Indice-Global.md`, 9 MOCs globais (`MOCs/`) e 8 Canvases (`_canvas/`).

4. **Merge Completo (`merge-completo-materializado-1m.tar.xz`, `34M`) e Otimização `.gitignore`**:
   - Removida a regra legada do `.gitignore` que impedia o versionamento direto de `merge-completo-materializado-1m.tar.xz`.
   - O arquivo `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` (`34M`) agora é versionado diretamente no Git junto com `ledger-v1000000-mat8000.sqlite.xz` (`24M`) e `study-vault-1m-packs.zip` (`19M`).

## Artefatos principais e Checksums SHA-256

| Arquivo | Tamanho | SHA-256 |
|---|---:|---|
| `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` | `34M` | `ae692de0c8d48683de2d26a3b0ad638ea9bb0b47aa7b36ca7ae9940e5537217c` |
| `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` | `24M` | `b824467e32b188b7cf7aad57161938fa2417f8a46193524cc26a5d0c7e460c85` |
| `knowledge-federation/archives/study-vault-1m-packs.zip` | `19M` | `36861d71866d59b1aa4e4fb227f36fe004b81aff2f90765dd4d7652d3dc5e17a` |
| `knowledge-federation/archives/starter-vault-prioritario.zip` | `1.1M` | `a60001c716653916ff5d87a357c57d4cdc403a6eb992f063a02b3ffbf3198fd7` |

## Segurança

Os domínios `cannabis-medicinal` e `micologia` permanecem restritos a conteúdo educacional, documental, científico, regulatório, rastreabilidade e perguntas para profissionais habilitados (`conteudo_operacional: false`, `0` ocorrências operacionais).
