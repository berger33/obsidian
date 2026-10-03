---
id: software.seguranca.tranche03.000278
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
fontes: ["https://raw.githubusercontent.com/securego/gosec/master/README.md", "https://raw.githubusercontent.com/securego/gosec/master/RULES.md", "https://github.com/securego/gosec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `gosec` Supressões Auditáveis (`// #nosec Gxxx -- justificativa`) e Rastreamento com `-track-suppressions`

## Em uma frase
O `gosec` permite suprimir falsos positivos em um nó AST ou linha específica usando a diretiva de comentário **`// #nosec G401 -- justificativa técnica`** e oferece as flags **`-track-suppressions`** (que inclui as supressões e suas justificativas no relatório SARIF/JSON final!) e **`-ignore-nosec=true`** (que ignora todas as diretivas `#nosec`).

## Por que importa
Permitir que desenvolvedores adicionem `// #nosec` sem especificar qual regra `Gxxx` está sendo ignorada e sem registrar o motivo no relatório de segurança impede que o time de AppSec audite as exceções aprovadas.

## Como funciona
Ao exigir o formato **`// #nosec Gxxx -- motivo`** e rodar `gosec -track-suppressions -fmt sarif -out results.sarif ./...`, o relatório SARIF enviado ao GitHub Code Scanning / DefectDojo registra formalmente cada supressão com o texto da justificativa escrito pelo autor no código!

## Exemplo
```go
package legacy

import (
	"crypto/sha1" // #nosec G505 -- exigido pelo protocolo RFC 3174 do parceiro legado (sem uso criptográfico)
	"fmt"
)

func ComputeLegacyPartnerChecksum(payload []byte) string {
	// #nosec G401 -- checksum de compatibilidade protocolar não usado para assinatura ou senha
	sum := sha1.Sum(payload)
	return fmt.Sprintf("%x", sum)
}
```

## Limites e trade-offs
Nunca configure uma diretiva `#nosec` sem listar o código explícito da regra (ex.: `G401`); assim, qualquer outro problema na mesma função continuará sendo detectado normalmente.

## Como verificar
Execute `gosec -track-suppressions -fmt json ./... | jq '.Issues'` para inspecionar os metadados de supressão registrados.

## Conexões
- [[gosec-configuracao-regras-json-g101-entropia-g104-erros-allowlist]] — Veja também: `gosec` Configuração Fina por Regra (`-conf config.json`): ajuste de entropia em `G101`, allowlist de erros em `G104` e permissões em `G301`/`G306`.
- [[gosec-filtragem-severity-confidence-include-exclude-tests-build-tags]] — Veja também: `gosec` Seleção de Escopo na CLI: `-severity`, `-confidence`, `-include`/`-exclude`, `-tests` e `-tags` de compilação.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
