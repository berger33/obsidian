---
id: software.seguranca.tranche16.001599
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/golang/vuln/master/README.md", "https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Filtrando e Automatizando Quality Gates com `govulncheck -format json` e `jq`: Distinguindo Achados de **Nível de Símbolo (`function`)** vs. **Nível de Módulo**

## Em uma frase
Vimos na nota `1594` que quando você executa `govulncheck -format json ./...` para salvar os resultados estruturados em um artefato de CI/CD, o comando retorna exit code `0`. E vimos na seção *Limitations* que o `govulncheck` ainda não possui uma flag nativa `--ignore` para silenciar um ID específico (`go.dev/issue/61211`). Como implementar em **5 linhas de `jq`** um Quality Gate de CI/CD sobre a saída `govulncheck -format json` que: **(1)** Quebra o build apenas quando houver vulnerabilidades de **Símbolo Chamado (`trace[0].function != null`)** e **(2)** Permite filtrar exceções temporárias aprovadas pela equipe de segurança?

## Por que importa
No stream JSON emitido por `govulncheck -format json`, cada objeto `{"finding": ...}` possui o campo `osv` (ex.: `"GO-2024-2687"`) e o array `trace` (onde o primeiro elemento `trace[0]` é o ponto mais profundo alcançado)!

## Como funciona
Se `trace[0].function` estiver preenchido (não-vazio), significa que **o símbolo vulnerável é efetivamente chamado pelo seu código**; se `trace[0].function` estiver ausente, significa que o módulo/pacote é apenas importado sem chamar a função vulnerável!

## Exemplo
```bash
# Executar o govulncheck em JSON e usar jq (-s slurp) para listar e falhar o CI apenas se houver vulnerabilidades com funcao efetivamente chamada
govulncheck -format json ./... > ./govuln.json
CHAMADAS="$(jq -s '[.[] | select(.finding != null and .finding.trace[0].function != null) | .finding.osv] | unique | length' ./govuln.json)"
echo "Total de vulnerabilidades Go alcancaveis por Call Graph: ${CHAMADAS}"
test "${CHAMADAS}" -eq 0
```

## Limites e trade-offs
Olhe que elegante o filtro `jq -s` acima: se um dia você precisar adicionar uma exceção temporária aprovada e documentada para `GO-2026-9999`, basta acrescentar `and .finding.osv != "GO-2026-9999"` dentro do `select(...)` do `jq` no seu script de CI, mantendo o gate automatizado 100% ativo para todas as demais vulnerabilidades!

## Como verificar
Esse padrão resolve de forma limpa e auditável tanto a captura do artefato JSON completo quanto a implementação de exceções temporárias de governança.

## Conexões
- [[govulncheck-remediacao-go-get-upgrade-go-mod-tidy-stdlib-toolchain]] — Veja também: Fluxo de Remediação de Vulnerabilidades Detectadas pelo `govulncheck`: Atualizando Módulos (**`go get pac@vX.Y.Z`**), **`go mod tidy`** e Toolchain **`go` (`stdlib`)**.
- [[govulncheck-pipeline-devsecops-go-completo-gosec-govulncheck-syft-cosign]] — Veja também: Arquitetura de Referência DevSecOps para **Go (`golang`)**: Combinando **`gosec` (SAST)**, **`govulncheck` (Reachable SCA)**, **`Syft` (SBOM)** e **`Cosign` (Assinatura Sigstore)**.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd]] — Referência cruzada direta com govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd.
- [[pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes]] — Referência cruzada direta com pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
