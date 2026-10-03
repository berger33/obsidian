---
id: software.seguranca.tranche04.000349
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md", "https://docs.projectdiscovery.io/opensource/subfinder/overview", "https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Subfinder: Integração Programática em Go via SDK (`runner.NewRunner` e `EnumerateSingleDomainWithCtx`)

## Em uma frase
Além da CLI, o `subfinder/v2/pkg/runner` pode ser importado diretamente como biblioteca Go em microserviços internos de segurança para executar enumeração passiva sem invocar processos externos.

## Por que importa
Permite embutir descoberta contínua de subdomínios em plataformas internas de inventário de ativos (CMDB/CSPM), controlando timeouts via `context.Context` e processando cada resultado em callbacks de memória (`ResultCallback`).

## Como funciona
O desenvolvedor instancia `runner.Options` (definindo `Threads`, `Timeout`, `MaxEnumerationTime` e `ResultCallback`), chama `runner.NewRunner(options)` e invoca `EnumerateSingleDomainWithCtx(ctx, "example.corp", writers)` para receber estruturas `resolve.HostEntry` tipadas em tempo real.

## Exemplo
```go
package main

import (
	"bytes"
	"context"
	"github.com/projectdiscovery/subfinder/v2/pkg/runner"
)

func main() {
	opts := &runner.Options{Threads: 10, Timeout: 30, MaxEnumerationTime: 5}
	r, _ := runner.NewRunner(opts)
	var out bytes.Buffer
	_ = r.EnumerateSingleDomainWithCtx(context.Background(), "example.corp", []io.Writer{&out})
}
```

## Limites e trade-offs
Ao executar o SDK do `subfinder` dentro de um serviço Go de longa duração, passe sempre um `context.WithTimeout` para garantir que goroutines de provedores externos lentos sejam canceladas e não vazem recursos.

## Como verificar
Compile o serviço com `go build` e execute um teste unitário com `context.WithTimeout`, confirmando o preenchimento do buffer de saída sem *goroutine leaks*.

## Conexões
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Veja também: Subfinder: Encadeamento Unix (`stdin`/`stdout`) em Pipelines de Reconhecimento com `httpx`, `katana` e `nuclei`.
- [[subfinder-monitoramento-continuo-diff-novos-subdominios-alertas]] — Veja também: Subfinder: Monitoramento Contínuo de Novos Subdomínios, Detecção de *Shadow IT* e Subdomain Takeover.
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Referência cruzada direta com subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
