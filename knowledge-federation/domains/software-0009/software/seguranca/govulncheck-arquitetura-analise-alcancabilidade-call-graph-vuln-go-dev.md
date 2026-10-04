---
id: software.seguranca.tranche16.001591
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

# Arquitetura do **`govulncheck` (`golang.org/x/vuln/cmd/govulncheck`)**: Análise Estática de Alcançabilidade (**Call Graph Reachability**) e Base **`vuln.go.dev`**

## Em uma frase
Por que os scanners SCA tradicionais baseados apenas no arquivo `go.mod` geram dezenas de alarmes falsos em projetos **Go (`golang`)**, enquanto o analisador oficial da equipe de segurança do Go — o **`govulncheck` (`golang/vuln`)** — reduz o ruído em mais de 80% mostrando **apenas vulnerabilidades em funções que o seu código realmente chama**?

## Por que importa
Conforme documentado no `README.md` (`golang/vuln`) e na referência oficial (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`), o `govulncheck` não olha apenas se um módulo `v1.2.3` consta no `go.mod`: **(1)** Na base oficial **`https://vuln.go.dev`** (curada pelo Go Security Team), cada aviso `GO-YYYY-NNNN` registra não apenas o módulo e a versão afetada, mas **a lista exata de pacotes e símbolos (funções/métodos) vulneráveis**!

## Como funciona
**(2)** Ao rodar `govulncheck ./...` sobre o código-fonte, ele constrói a representação SSA (*Static Single Assignment*) e o **Grafo de Chamadas (*Call Graph* via algoritmo VTA — *Variable Type Analysis*)** do seu programa, verificando se existe um caminho real de chamadas entre a sua função `main()` (ou funções exportadas) e a função vulnerável da dependência!

## Exemplo
```bash
# Instalar e executar o govulncheck oficial analisando todos os pacotes do modulo Go atual (incluindo a Standard Library do Go!)
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck -version
govulncheck ./...
```

## Limites e trade-offs
Veja outro diferencial gigantesco do **`govulncheck`** em relação a scanners de terceiros: ele audita automaticamente não apenas os módulos externos do `go.mod`, mas também a **Biblioteca Padrão do Go (`stdlib`: `net/http`, `crypto/tls`, ` crypto/x509`, `archive/tar`, `html/template`)** da versão exata do compilador `go` usada no build!

## Como verificar
E como funciona a privacidade (`https://vuln.go.dev/privacy.html`) destacada na documentação oficial? O `govulncheck` **NUNCA envia seu código-fonte nem nomes de pacotes privados** para `vuln.go.dev`: ele consulta apenas caminhos de módulos públicos que já possuem vulnerabilidades conhecidas no índice do banco!

## Conexões
- [[govulncheck-interpretacao-relatorio-call-stacks-show-traces-verbose]] — Veja também: Interpretando Pilhas de Chamadas (**Call Stacks**) no `govulncheck`: Vulnerabilidades **Chamadas (`Called`) vs. Apenas Importadas**, **`-show traces`** e **`-show verbose`**.
- [[govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract]] — Referência cruzada direta com govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract.
- [[depcheck-comparativo-dependency-check-vs-dependency-track-osv-scanner-sbom]] — Referência cruzada direta com depcheck-comparativo-dependency-check-vs-dependency-track-osv-scanner-sbom.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
