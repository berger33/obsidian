---
id: software.seguranca.tranche03.000277
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/securego/gosec/master/RULES.md", "https://raw.githubusercontent.com/securego/gosec/master/README.md", "https://github.com/securego/gosec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `gosec` Configuração Fina por Regra (`-conf config.json`): ajuste de entropia em `G101`, allowlist de erros em `G104` e permissões em `G301`/`G306`

## Em uma frase
Conforme documentado na seção *Rules configuration* de `RULES.md`, o `gosec` aceita um arquivo JSON de configuração (`gosec -conf .gosec.json ./...`) contendo ajustes globais e configurações específicas para as regras **`G101`**, **`G104`**, **`G111`**, **`G117`**, **`G301`**, **`G302`**, **`G306`** e **`G307`**.

## Por que importa
Na regra **`G104` (erros não verificados)**, funções como `fmt.Println` retornam um erro que quase nenhum código Go verifica; sem configurar uma allowlist no `G104`, a equipe acaba desativando a regra `G104` inteira e perde a detecção de erros ignorados em chamadas críticas como `tx.Rollback()` ou `rows.Close()`.

## Como funciona
No arquivo `.gosec.json`, você mantém a `G104` ativa mas ignora apenas pacotes/funções triviais (como `fmt: ["Println", "Printf"]`), além de ajustar os limiares de entropia da `G101` (`entropy_threshold`, `per_char_threshold`) e o modo máximo de permissão da `G306`!

## Exemplo
```json
{
  "global": {
    "audit": "enabled"
  },
  "G101": {
    "pattern": "(?i)passwd|pass|password|pwd|secret|private_key|token|api_key",
    "ignore_entropy": false,
    "entropy_threshold": "80.0",
    "per_char_threshold": "3.0"
  },
  "G104": {
    "fmt": ["Println", "Printf", "Fprintf"]
  },
  "G306": "0600"
}
```

## Limites e trade-offs
Você também pode excluir arquivos gerados automaticamente (como `*.pb.go` do Protobuf ou mocks) usando a flag **`-exclude-generated`** na linha de comando.

## Como verificar
Execute `gosec -conf .gosec.json -exclude-generated ./...` para validar sua configuração customizada.

## Conexões
- [[gosec-criptografia-tls-ssh-g401-a-g408-math-rand-vs-crypto-rand]] — Veja também: `gosec` Criptografia, TLS e SSH (`G401`–`G408` e `G501`–`G507`): `crypto/rand`, `MinVersion: tls.VersionTLS13`, IVs hardcoded e SSH.
- [[gosec-supressao-anotacoes-nosec-justificativa-tracking-suppressions]] — Veja também: `gosec` Supressões Auditáveis (`// #nosec Gxxx -- justificativa`) e Rastreamento com `-track-suppressions`.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
