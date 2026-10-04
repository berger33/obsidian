---
id: software.seguranca.tranche16.001600
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

# Arquitetura de Referência DevSecOps para **Go (`golang`)**: Combinando **`gosec` (SAST)**, **`govulncheck` (Reachable SCA)**, **`Syft` (SBOM)** e **`Cosign` (Assinatura Sigstore)**

## Em uma frase
Para celebrar a marca de **1.600 notas substantivas (`80,00%`)** do lote `software-seguranca-2000-0003`: como todas as ferramentas de segurança do ecossistema **Go** que estudamos ao longo deste lote se encaixam em uma **Esteira DevSecOps Completa e Sem Ruído** para microsserviços e CLIs em Go?

## Por que importa
Veja as **4 camadas complementares** que cobrem 100% do ciclo de vida de um binário Go: **(Camada 1 — SAST no Código Próprio com `gosec`)**: analisa a árvore AST/SSA do código que a sua equipe escreveu (caçando SQL Injection, Command Injection, `math/rand` em criptografia, TLS InsecureSkipVerify e permissões de arquivo inseguras).

## Como funciona
**(Camada 2 — SCA com Alcançabilidade de Call Graph com `govulncheck ./...` e `-mode binary`)**: verifica a `stdlib` e todas as dependências do `go.mod` provando se alguma função vulnerável é chamada e gerando o documento **OpenVEX**; **(Camada 3 — Geração de SBOM e Varredura de Container com `Syft` + `Grype`/`Trivy`)**; e **(Camada 4 — Proveniência SLSA e Assinatura Keyless com `Sigstore Cosign` + `Fulcio` + `Rekor`)**!

## Exemplo
```bash
# Pipeline de validacao de seguranca em 3 passos para um projeto Go: SAST (gosec), SCA por Call Graph (govulncheck) e auditoria do binario compilado
gosec -quiet ./...
govulncheck ./...
go build -trimpath -o ./bin/servico ./cmd/servico
govulncheck -mode binary ./bin/servico
```

## Limites e trade-offs
Repare na flag **`-trimpath`** no `go build -trimpath -o ./bin/servico` acima: ela remove caminhos absolutos do sistema de arquivos da máquina de build (ex.: `/home/runner/work/...`) de dentro do binário compilado para garantir **Builds Reprodutíveis (*Reproducible Builds*)**, sem remover os metadados `debug/buildinfo` que o **`govulncheck -mode binary`** usa para auditar o binário em produção!

## Como verificar
Com isso completamos a **Tranche 16 (`1501–1600`)**, atingindo **1.600 / 2.000 notas válidas (`80,00%`)** no lote `software-seguranca-2000-0003`!

## Conexões
- [[govulncheck-triagem-json-jq-distincao-modulo-pacote-simbolo-ci-gate]] — Veja também: Filtrando e Automatizando Quality Gates com `govulncheck -format json` e `jq`: Distinguindo Achados de **Nível de Símbolo (`function`)** vs. **Nível de Módulo**.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
