---
id: software.seguranca.tranche16.001596
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

# Limitações Conhecidas da Análise Estática do `govulncheck`: Ponteiros de Função/Interfaces, Pacotes **`reflect`** e **`unsafe`**, Go < 1.18 e Binários *Stripped*

## Em uma frase
Todo engenheiro de AppSec precisa conhecer exatamente quais são as **6 limitações técnicas** documentadas oficialmente pelo Go Security Team na seção *Limitations* de `pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`! Quais situações podem gerar **Falsos Positivos** ou **Falsos Negativos** no `govulncheck`?

## Por que importa
Veja o resumo exato da documentação oficial: **(1) Chamadas via Ponteiros de Função e Interfaces**: o algoritmo de grafo de chamadas (`VTA`) analisa interfaces e ponteiros de função de maneira **conservadora**, o que pode ocasionalmente gerar falsos positivos se uma implementação vulnerável implementar uma interface usada em outro ponto; **(2) Uso de `reflect` e `unsafe` (Risco de Falso Negativo!)**: chamadas de funções feitas dinamicamente via reflexão (`package reflect`) ou manipulação de ponteiros com `package unsafe` **não são visíveis à análise estática**!

## Como funciona
**(3) Análise de Binários (`-mode binary`)**: como o binário compilado não guarda o grafo de chamadas completo, se uma função vulnerável foi incluída no binário mas não é chamada em tempo de execução, ela será reportada; **(4) Binários sem Tabela de Símbolos (*Stripped Binaries* `-ldflags="-s -w"`)**: se os símbolos das funções não puderem ser extraídos, o `govulncheck` faz fallback seguro reportando vulnerabilidades para **todos os módulos** dos quais o binário depende!

## Exemplo
```bash
# Comparar a auditoria de um binario Go compilado normalmente (com tabela de simbolos) vs. o impacto de remover simbolos no nivel de precisao
go build -o ./app_com_simbolos ./cmd/app
govulncheck -mode binary ./app_com_simbolos
```

## Limites e trade-offs
Olhe a lição prática da **Limitação 4** acima para equipes de DevSecOps que constroem imagens de container Go: se você compilar seus binários Go removendo a tabela de símbolos (`-s`), o `govulncheck -mode binary` perderá a capacidade de saber quais funções específicas foram eliminadas pelo linker e terá que reportar todas as vulnerabilidades de nível de módulo! Manter a tabela de símbolos (ou rodar `govulncheck ./...` no código-fonte e `govulncheck -mode extract` antes do strip) preserva 100% da precisão!

## Como verificar
E lembre-se da **Limitação 5**: para binários muito antigos compilados com versões anteriores ao **Go 1.18**, o `-mode binary` reporta apenas vulnerabilidades da biblioteca padrão (`stdlib`).

## Conexões
- [[govulncheck-banco-dados-customizado-db-espelho-local-air-gapped-privacy]] — Veja também: Operando o `govulncheck` Offline (**Air-Gapped**) ou com Mirror Corporativo via Flag **`-db`**: Arquitetura do Go Vulnerability Database (`vuln.go.dev`).
- [[govulncheck-api-programatica-golang-org-x-vuln-scan-automacao-customizada]] — Veja também: Usando o `govulncheck` como Biblioteca em Go (**`golang.org/x/vuln/scan`**): Construindo Ferramentas Internas de Segurança e Scanners de Plataforma.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.
- [[govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract]] — Referência cruzada direta com govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract.

## Fontes
- [Official Go Vulnerability Management Repository (`golang/vuln`)](https://raw.githubusercontent.com/golang/vuln/master/README.md) — repositório oficial do Go Security Team para gerenciamento de vulnerabilidades cobrindo `govulncheck`, base `vuln.go.dev` e pacote `golang.org/x/vuln/scan`; consultado em 2026-10-03.
- [Official `govulncheck` Command Documentation (`pkg.go.dev/golang.org/x/vuln/cmd/govulncheck`)](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) — documentação técnica oficial do comando `govulncheck` detalhando análise de código-fonte e binários (`-mode binary` / `-mode extract`), `-show traces`, formatos `sarif`/`openvex`/`json`, exit codes e limitações; consultado em 2026-10-03.
