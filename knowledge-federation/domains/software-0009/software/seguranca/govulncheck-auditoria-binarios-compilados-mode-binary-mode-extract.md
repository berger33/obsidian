---
id: software.seguranca.tranche16.001593
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

# Auditando **Binários Go Compilados (`-mode binary`)** e Extração de Blobs Leves (**`-mode extract`**) para Containers e Imagens em Produção com o `govulncheck`

## Em uma frase
Imagine que você tem dezenas de binários Go já compilados rodando em servidores Linux ou dentro de imagens de container *Distroless* / `scratch` em produção, e uma nova vulnerabilidade crítica na biblioteca padrão `net/http` ou `golang.org/x/crypto/ssh` acaba de ser divulgada hoje! Como descobrir em 2 segundos se um **binário Go já compilado** contém símbolos vulneráveis **sem precisar ter o código-fonte nem o `go.mod` daquele binário**?

## Por que importa
Usando o modo de análise de binários do `govulncheck`: **`govulncheck -mode binary /caminho/do/meu-binario-go`**!

## Como funciona
Como o compilador Go (`Go 1.18+`) embute automaticamente dentro de todo binário ELF/PE/Mach-O os metadados de build (`debug/buildinfo`: versão exata do compilador Go, lista de todos os módulos e versões compilados e tabela de símbolos das funções presentes no binário), o **`govulncheck -mode binary`** extrai esses símbolos diretamente do executável e verifica se alguma função vulnerável foi linkada nele!

## Exemplo
```bash
# Auditar diretamente um binario Go ja compilado (-mode binary) e extrair o blob minimo de metadados (-mode extract) para analise remota
govulncheck -mode binary /usr/local/bin/meu-servico-go
govulncheck -mode extract /usr/local/bin/meu-servico-go > ./servico-vuln.blob
govulncheck -mode binary ./servico-vuln.blob
```

## Limites e trade-offs
Olhe as linhas 2 e 3 do exemplo acima (**`govulncheck -mode extract`**): em ambientes de produção ou clusters Kubernetes com milhares de containers onde você não quer copiar binários de 80 MB pela rede para escanear centralmente, o comando `govulncheck -mode extract /bin/app` extrai um **Blob minúsculo (de poucos Kilobytes!)** contendo apenas as informações mínimas de módulos e símbolos necessárias para a análise — e esse blob pode ser enviado ao servidor central de segurança e passado diretamente para **`govulncheck -mode binary ./servico-vuln.blob`**!

## Como verificar
Note a diferença técnica documentada em *Usage* e *Limitations*: como binários compilados não preservam o grafo completo de chamadas do código-fonte, no `-mode binary` o `govulncheck` verifica quais funções vulneráveis restaram na **Tabela de Símbolos** (após o *Dead Code Elimination* do linker do Go!) e omite os call stacks linha a linha.

## Conexões
- [[govulncheck-interpretacao-relatorio-call-stacks-show-traces-verbose]] — Veja também: Interpretando Pilhas de Chamadas (**Call Stacks**) no `govulncheck`: Vulnerabilidades **Chamadas (`Called`) vs. Apenas Importadas**, **`-show traces`** e **`-show verbose`**.
- [[govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd]] — Veja também: Exportando **`SARIF` (`-format sarif`)**, **`OpenVEX` (`-format openvex`)** e **Streaming `JSON` (`-format json`)** no `govulncheck` e o Comportamento de Exit Codes.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[govulncheck-limitacoes-analise-estatica-reflect-unsafe-stripped-binaries]] — Referência cruzada direta com govulncheck-limitacoes-analise-estatica-reflect-unsafe-stripped-binaries.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
