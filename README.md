# Biblioteca e Federação de Conhecimento Obsidian — 1 Milhão de Notas

Repositório oficial da **Federação de Conhecimento em formato Obsidian** (português do Brasil) cobrindo **Engenharia de Software, Inteligência Artificial, Vibe Coding & Orquestração Agêntica, Desenvolvimento de Jogos, Negócio/Carreira/Produto, Cannabis Medicinal (educacional/regulatório) e Micologia Segura**.

---

## Marco Consolidado (100% Concluído)

| Métrica | Total |
|---|---:|
| **Notas virtuais no ledger SQLite** (`ledger-v1000000-mat8000.sqlite.xz`) | **1.000.000** |
| **Notas físicas iniciais** (`knowledge-federation/domains/`) | **100** |
| **Total lógico no ledger** | **1.000.100** |
| **Lotes sequenciais materializados** (`50 pacotes × 100 lotes × 200 notas`) | **1.000.000** |
| **Study Packs curados por subdomínio** (`78 subdomínios × 200 notas`) | **15.600** |
| **Total materializado representado no Merge Completo** | **1.015.600** |
| **Entradas totais no arquivo `merge-completo-materializado-1m.tar.xz`** | **1.021.127** |
| **Links quebrados no Study Vault Curado (`93.894` links auditados)** | **0** |
| **Conteúdo operacional em domínios regulados (`cannabis-medicinal` / `micologia`)** | **0** |

---

## Principais Entregas e Pacotes Prontos para Abrir no Obsidian

| Pacote / Pasta | Tamanho | Descrição |
|---|---:|---|
| `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` | `34M` | **Merge Completo (1.015.600 notas):** inclui `00-home-vault/`, `00-vault-consolidado/` (78 study packs / 15.600 notas), `10-lotes/` (`0001-0100` a `4901-5000` = 5.000 lotes / 1.000.000 de notas), `90-ledger/` e `99-relatorios/`. |
| `knowledge-federation/archives/study-vault-1m-packs.zip` | `19M` | **Study Vault Curado Completo (15.600 notas):** 78 study packs cobrindo 100% dos subdomínios, 85 MOCs, 5 trilhas guiadas, 6 playbooks/matrizes e 9 Canvases. |
| `knowledge-federation/archives/starter-vault-prioritario.zip` | `1.1M` | **Starter Vault Prioritário (900 notas):** pacote leve para início imediato (IA, RAG, Backend, Orquestração e MVP). |
| `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` | `24M` | **Ledger SQLite Completo (`885 MB` descompactado):** 1.000.000 de notas virtuais + 100 físicas para consulta e materialização sob demanda. |
| `knowledge-federation/00-home-vault/` | Ativo | **Home Vault Mestre:** `Home.md`, `Indice-Global.md`, 9 MOCs globais (`MOCs/`) e 8 Canvases (`_canvas/`). |
| `vault-desenvolvimento-software-com-ia/` | Ativo | **Vault Autoral Amplo (~660 notas profundas):** engenharia de software com IA, ferramentas, jogos, árvores de decisão, trilhas e glossário (`vault-desenvolvimento-software-com-ia.zip`). |

---

## Como Baixar e Usar no Obsidian

### 1. Abrir o Study Vault Curado de 78 Subdomínios (15.600 notas)

```bash
unzip knowledge-federation/archives/study-vault-1m-packs.zip -d study-vault-1m-packs
```

No Obsidian, clique em **Open folder as vault**, selecione `study-vault-1m-packs` e abra `00-Inicio/Home.md`.

### 2. Extrair Lotes do Merge Completo (1.015.600 notas)

Para extrair um intervalo específico de 100 lotes (20.000 notas) sem criar 1 milhão de arquivos de uma só vez no disco:

```bash
# Exemplo: extrair os lotes 0001-0100
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/0001-0100

# Exemplo: extrair os lotes 4901-5000
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/4901-5000
```

Para extrair o merge completo inteiro:

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

### 3. Consultar o Ledger de 1 Milhão de Notas via CLI

```bash
python3 knowledge-federation/scripts/ledger_stats.py
python3 knowledge-federation/scripts/query_checkpoint.py "agentes" --domain ia --limit 20
```

---

## Documentação Detalhada

- [`knowledge-federation/STATUS-CONSOLIDACAO-1M.md`](knowledge-federation/STATUS-CONSOLIDACAO-1M.md) — Status final da consolidação de 1 milhão de notas
- [`knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md`](knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md) — Passo a passo para abrir e copiar para seu cofre Obsidian
- [`knowledge-federation/MERGE-COMPLETO.md`](knowledge-federation/MERGE-COMPLETO.md) — Estrutura, integridade e checksums do merge completo
- [`knowledge-federation/STUDY-VAULT-README.md`](knowledge-federation/STUDY-VAULT-README.md) — Detalhes do Study Vault curado com os 78 subdomínios
- [`knowledge-federation/LOT-SEQUENCE.md`](knowledge-federation/LOT-SEQUENCE.md) — Tabela dos 50 pacotes / 5.000 lotes sequenciais (`0001-0100` a `4901-5000`)
- [`knowledge-federation/PACK-INVENTORY.md`](knowledge-federation/PACK-INVENTORY.md) — Inventário dos 78 study packs individuais em `.zip`
- [`knowledge-federation/RELEASE-DOWNLOADS.md`](knowledge-federation/RELEASE-DOWNLOADS.md) — Links de download e hashes SHA-256

---

## Segurança e Conformidade em Domínios Regulados

Os domínios `cannabis-medicinal` e `micologia` seguem política estrita de segurança (`conteudo_operacional: false`, `0` notas operacionais):
- Foco exclusivo em **legislação, regulação, documentação de paciente, farmacologia descritiva, botânica/taxonomia, estudos clínicos, redução de danos, rastreabilidade e perguntas para profissionais habilitados**.
- **Nenhuma** instrução operacional de cultivo, extração, produção ou otimização de substâncias controladas.
