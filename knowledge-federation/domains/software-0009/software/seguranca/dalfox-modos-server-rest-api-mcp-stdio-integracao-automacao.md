---
id: software.seguranca.tranche05.000419
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/hahwul/dalfox/main/README.md", "https://dalfox.hahwul.com/reference/cli/", "https://github.com/hahwul/dalfox/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dalfox: Subcomandos `dalfox server` (REST API) e `dalfox mcp` (Model Context Protocol stdio Server)

## Em uma frase
Além da CLI de varredura direta, o Dalfox disponibiliza dois modos de integração programática: **`dalfox server`** (que levanta um servidor REST API para enfileiramento e consulta de scans) e **`dalfox mcp`** (um servidor *Model Context Protocol* sobre `stdio` para integração com agentes de segurança assistidos por IA).

## Por que importa
Permite orquestrar varreduras de XSS sob demanda a partir de sistemas de CI/CD, webhooks de Pull Request ou fluxos automatizados de triagem de AppSec sem gerenciar parsing de texto de terminal.

## Como funciona
O comando `dalfox server` expõe endpoints HTTP autenticáveis para submeter URLs/opções e consultar resultados em JSON, enquanto `dalfox mcp` expõe ferramentas tipadas via JSON-RPC sobre `stdio`, respeitando os mesmos códigos de saída (`2` em caso de falha de bind ou inicialização).

## Exemplo
```bash
# Iniciar o servidor REST do Dalfox restrito à interface de loopback em porta dedicada
dalfox server --host 127.0.0.1 --port 6664
```

## Limites e trade-offs
Nunca exponha `dalfox server` em `0.0.0.0` sem autenticação e isolamento de rede, pois qualquer cliente capaz de alcançar a API poderá instruir o servidor a disparar scans HTTP contra alvos arbitrários (SSRF-as-a-Service).

## Como verificar
Verifique com `ss -tulnp | grep 6664` que o socket escuta apenas em `127.0.0.1:6664` e valide a resposta do endpoint de health/swagger local.

## Conexões
- [[dalfox-pipeline-mode-katana-dedup-urls-state-file-resume]] — Veja também: Dalfox: Operação em Pipeline (`--input-type pipe`), Deduplicação (`--dedup-urls signature`) e Retomada (`--state-file`).
- [[dalfox-comparacao-baseline-sarif-state-file-ci-cd]] — Veja também: Dalfox: Gates de CI/CD com Comparação de Baseline (`--baseline`, `--baseline-mode`) e Exportação SARIF (`-f sarif`).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[sqlmap-api-rest-sqlmapapi-automacao-remota-ipc-json]] — Referência cruzada direta com sqlmap-api-rest-sqlmapapi-automacao-remota-ipc-json.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
