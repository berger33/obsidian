---
id: software.seguranca.tranche16.001597
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

# Usando o `govulncheck` como Biblioteca em Go (**`golang.org/x/vuln/scan`**): Construindo Ferramentas Internas de Segurança e Scanners de Plataforma

## Em uma frase
E se você estiver construindo uma ferramenta interna de plataforma, um Admission Controller do Kubernetes (como a integração `k8s` e `stackrox-scanner` visíveis nos diretórios do repositório `golang/vuln`) ou um CLI corporativo em Go e quiser executar o `govulncheck` **programaticamente como uma biblioteca Go** sem precisar chamar `os/exec`?

## Por que importa
Conforme destacado no `README.md` oficial (`golang/vuln`), a API pública está disponível no pacote oficial **`golang.org/x/vuln/scan`**!

## Como funciona
Com `scan.Command(ctx, args...)`, você invoca toda a máquina de análise do `govulncheck` diretamente dentro do seu processo Go, redirecionando `Stdout` e `Stderr` para um `bytes.Buffer` ou parser de streaming JSON e controlando cancelamento via `context.Context`!

## Exemplo
```go
// Executar o govulncheck programaticamente dentro de uma aplicacao Go usando o pacote oficial golang.org/x/vuln/scan
package main

import (
	"context"
	"os"
	"golang.org/x/vuln/scan"
)

func main() {
	ctx := context.Background()
	cmd := scan.Command(ctx, "-format", "json", "./...")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Start(); err == nil {
		_ = cmd.Wait()
	}
}
```

## Limites e trade-offs
Veja nos subdiretórios do repositório `golang/vuln/cmd/govulncheck/integration/` (`k8s` e `stackrox-scanner`) como a própria equipe do Go testa e integra o `govulncheck` com scanners de containers e clusters Kubernetes!

## Como verificar
Ao consumir o stream JSON gerado por `scan.Command(ctx, "-format", "json", ...)` em Go, cada mensagem emitida no stream é um objeto JSON tipado (`config`, `progress`, `osv`, `finding`), onde um `finding` cujo array `trace` possui um elemento com `function != ""` indica que a função vulnerável é efetivamente alcançada!

## Conexões
- [[govulncheck-limitacoes-analise-estatica-reflect-unsafe-stripped-binaries]] — Veja também: Limitações Conhecidas da Análise Estática do `govulncheck`: Ponteiros de Função/Interfaces, Pacotes **`reflect`** e **`unsafe`**, Go < 1.18 e Binários *Stripped*.
- [[govulncheck-remediacao-go-get-upgrade-go-mod-tidy-stdlib-toolchain]] — Veja também: Fluxo de Remediação de Vulnerabilidades Detectadas pelo `govulncheck`: Atualizando Módulos (**`go get pac@vX.Y.Z`**), **`go mod tidy`** e Toolchain **`go` (`stdlib`)**.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd]] — Referência cruzada direta com govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
