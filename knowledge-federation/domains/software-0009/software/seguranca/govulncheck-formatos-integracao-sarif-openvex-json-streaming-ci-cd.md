---
id: software.seguranca.tranche16.001594
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

# Exportando **`SARIF` (`-format sarif`)**, **`OpenVEX` (`-format openvex`)** e **Streaming `JSON` (`-format json`)** no `govulncheck` e o Comportamento de Exit Codes

## Em uma frase
Como integrar o `govulncheck` a plataformas de gestão de vulnerabilidades e SBOMs gerando automaticamente documentos **`OpenVEX` (*Vulnerability Exploitability eXchange*)** — que informam formalmente aos consumidores do seu SBOM quais CVEs do `go.mod` **NÃO são exploráveis (`not_affected: vulnerable_code_not_in_execute_path`)** porque o `govulncheck` provou que a função vulnerável não é chamada?

## Por que importa
Passando a flag **`-format openvex`** (ou **`-format sarif`** para o GitHub Code Scanning, ou **`-format json`** para automação customizada)!

## Como funciona
Quando você executa `govulncheck -format openvex ./... > documento.vex.json`, o `govulncheck` emite um documento oficial seguindo a especificação **OpenVEX (`github.com/openvex/spec`)**: as vulnerabilidades cujo símbolo é alcançado pelo seu código são marcadas como `affected`, e as vulnerabilidades presentes nas dependências mas cujo símbolo não é chamado recebem declaração VEX automática de não-afetadas!

## Exemplo
```bash
# Gerar relatorios estruturados nos formatos OpenVEX, SARIF e JSON a partir do govulncheck para ingestao em pipelines DevSecOps
govulncheck -format openvex ./... > ./relatorio.openvex.json
govulncheck -format sarif ./... > ./relatorio.sarif
govulncheck -format json ./... > ./relatorio.json
```

## Limites e trade-offs
Preste **MUITA ATENÇÃO** a um detalhe crucial documentado na seção *Exit codes* de `pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`: no modo texto padrão, o `govulncheck` retorna exit code diferente de zero se encontrar vulnerabilidades; **PORÉM, quando você passa `-format json` (`-json`), `-format sarif` ou `-format openvex`, o `govulncheck` retorna Exit Code `0` (sucesso) independentemente do número de vulnerabilidades detectadas** (para não interromper pipelines que precisam fazer upload do arquivo SARIF/VEX na etapa seguinte)!

## Como verificar
Portanto, se o seu pipeline de CI/CD usa `-format sarif` ou `-format json` e você também quer quebrar o build caso existam vulnerabilidades chamadas, rode `govulncheck ./...` (ou valide o JSON/SARIF gerado com `jq`)!

## Conexões
- [[govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract]] — Veja também: Auditando **Binários Go Compilados (`-mode binary`)** e Extração de Blobs Leves (**`-mode extract`**) para Containers e Imagens em Produção com o `govulncheck`.
- [[govulncheck-banco-dados-customizado-db-espelho-local-air-gapped-privacy]] — Veja também: Operando o `govulncheck` Offline (**Air-Gapped**) ou com Mirror Corporativo via Flag **`-db`**: Arquitetura do Go Vulnerability Database (`vuln.go.dev`).
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[govulncheck-interpretacao-relatorio-call-stacks-show-traces-verbose]] — Referência cruzada direta com govulncheck-interpretacao-relatorio-call-stacks-show-traces-verbose.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
