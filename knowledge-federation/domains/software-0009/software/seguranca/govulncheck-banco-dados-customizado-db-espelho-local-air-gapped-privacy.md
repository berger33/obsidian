---
id: software.seguranca.tranche16.001595
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

# Operando o `govulncheck` Offline (**Air-Gapped**) ou com Mirror Corporativo via Flag **`-db`**: Arquitetura do Go Vulnerability Database (`vuln.go.dev`)

## Em uma frase
Como executar o `govulncheck` em runners de CI/CD corporativos isolados da internet (*Air-Gapped*) ou usando um espelho interno controlado pela equipe de segurança, sem depender de acesso externo a `https://vuln.go.dev`?

## Por que importa
Usando a flag oficial **`-db <URL_OU_FILE_URI>`**, documentada na seção *Overview* de `pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`!

## Como funciona
O protocolo do **Go Vulnerability Database (`https://go.dev/security/vuln/database`)** foi projetado pelo time do Go para ser **100% composto por arquivos JSON estáticos servidos sem nenhum backend dinâmico**: basta clonar/sincronizar o repositório oficial **`github.com/golang/vulndb`** (ou espelhar os arquivos estáticos em um bucket S3/servidor Nginx interno ou pasta local do disco) e passar **`govulncheck -db file:///var/cache/vulndb ./...`** ou **`govulncheck -db https://vulndb.interno.empresa.br ./...`**!

## Exemplo
```bash
# Executar o govulncheck apontando para um espelho local em disco (file://) ou servidor HTTP interno da base Go Vulnerability Database (-db)
govulncheck -db https://vuln.go.dev ./...
```

## Limites e trade-offs
Veja por que o design estático do `vuln.go.dev` é um exemplo brilhante de **Engenharia de Privacidade (*Privacy by Design*)**: quando o `govulncheck` consulta o banco de dados, primeiro ele baixa um pequeno índice global `index/modules.json` listando apenas quais módulos públicos do ecossistema Go possuem pelo menos uma vulnerabilidade registrada; se a sua empresa usa 50 pacotes internos `git.empresa.br/ time/servico`, o `govulncheck` vê que eles não estão no índice público e **jamais faz nenhuma requisição HTTP mencionando o nome dos seus módulos privados**!

## Como verificar
Em ambientes sem internet, sincronize o espelho local do `vulndb` diariamente e aponte `-db file:///caminho/local/vulndb` nos seus jobs de CI.

## Conexões
- [[govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd]] — Veja também: Exportando **`SARIF` (`-format sarif`)**, **`OpenVEX` (`-format openvex`)** e **Streaming `JSON` (`-format json`)** no `govulncheck` e o Comportamento de Exit Codes.
- [[govulncheck-limitacoes-analise-estatica-reflect-unsafe-stripped-binaries]] — Veja também: Limitações Conhecidas da Análise Estática do `govulncheck`: Ponteiros de Função/Interfaces, Pacotes **`reflect`** e **`unsafe`**, Go < 1.18 e Binários *Stripped*.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[depcheck-execucao-offline-air-gapped-espaco-corporativo-central-db]] — Referência cruzada direta com depcheck-execucao-offline-air-gapped-espaco-corporativo-central-db.
- [[pip-audit-indices-privados-index-url-extra-index-url-cache-offline]] — Referência cruzada direta com pip-audit-indices-privados-index-url-extra-index-url-cache-offline.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
