---
id: software.seguranca.tranche16.001592
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

# Interpretando Pilhas de Chamadas (**Call Stacks**) no `govulncheck`: Vulnerabilidades **Chamadas (`Called`) vs. Apenas Importadas**, **`-show traces`** e **`-show verbose`**

## Em uma frase
Quando você executa `govulncheck ./...` em um projeto Go, como o relatório diferencia uma vulnerabilidade que **afeta ativamente o seu código (e retorna Exit Code != 0)** de uma vulnerabilidade presente em um módulo importado cujo símbolo vulnerável **nunca é chamado pelo seu programa**?

## Por que importa
O `govulncheck` separa os achados em duas seções distintas: **(1) Vulnerabilidades Chamadas (*Vulnerabilities called by your code*)** — para cada uma, ele imprime o resumo exato da **Pilha de Chamadas (`Call Stack`)** com arquivo, linha e coluna (ex.: `main.go:42:18: meupacote.main calls golang.org/x/text/language.Parse`), provando exatamente como o seu código chega até a função vulnerável!; e **(2) Informational (Apenas Importadas/Requeridas)** — avisa que o módulo está no `go.mod`, mas nenhuma função vulnerável é alcançável!

## Como funciona
E quando o resumo da pilha de chamadas omite funções intermediárias com `...`, basta passar **`-show traces`** (para imprimir a pilha de chamadas completa do início ao fim!) ou **`-show verbose`** (para detalhes completos de progresso e findings)!

## Exemplo
```bash
# Executar o govulncheck exibindo a pilha de chamadas completa (-show traces) e incluindo arquivos de teste (-test) e build tags (-tags)
govulncheck -show traces -test -tags integration ./...
```

## Limites e trade-offs
Olhe as duas flags de escopo de compilação no comando acima documentadas na seção *Usage* do `pkg.go.dev`: **(1) `-test`** — por padrão, o `govulncheck ./...` analisa apenas o código de produção; passando **`-test`**, ele inclui também todos os arquivos `*_test.go` e dependências exclusivas de teste; e **(2) `-tags`** — permite especificar uma lista separada por vírgulas de *build tags* (ex.: `-tags linux,amd64,fips` ou `-tags integration`) para analisar arquivos condicionais de plataforma!

## Como verificar
Como lembra a documentação oficial: diferentes configurações de build (`GOOS`, `GOARCH`, `-tags` e versão do `go` no `PATH`) podem ativar arquivos `.go` diferentes na `stdlib` e nas dependências — portanto, rode sempre o `govulncheck` com o mesmo `GOOS`/`GOARCH` e versão do Go que você usa para gerar o binário de produção!

## Conexões
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Veja também: Arquitetura do **`govulncheck` (`golang.org/x/vuln/cmd/govulncheck`)**: Análise Estática de Alcançabilidade (**Call Graph Reachability**) e Base **`vuln.go.dev`**.
- [[govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract]] — Veja também: Auditando **Binários Go Compilados (`-mode binary`)** e Extração de Blobs Leves (**`-mode extract`**) para Containers e Imagens em Produção com o `govulncheck`.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
