---
id: software.seguranca.tranche05.000420
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

# Dalfox: Gates de CI/CD com Comparação de Baseline (`--baseline`, `--baseline-mode`) e Exportação SARIF (`-f sarif`)

## Em uma frase
O Dalfox integra-se nativamente a pipelines de DevSecOps através de relatórios **SARIF** (`--format sarif`), arquivos de configuração declarativa (`--config dalfox.toml`) e comparação diferencial contra varreduras anteriores (`--baseline baseline.json` com `--baseline-mode filter|annotate`).

## Por que importa
Em aplicações grandes com alertas informativos ou reflexões conhecidas sob análise, `--baseline old-report.json --baseline-mode filter` faz com que a contagem de achados e o código de saída (`0` vs `1`) reflitam **exclusivamente** vulnerabilidades novas introduzidas no branch atual.

## Como funciona
Combinar `--only-poc v,r` com `--baseline main-dalfox.json --baseline-mode filter --format sarif --output results.sarif` permite falhar o pipeline de CI apenas se um novo ponto de XSS surgir e publicar a prova de conceito (`--poc-type curl` ou `http-request` com `--include-all`) diretamente na aba Security do GitHub.

## Exemplo
```bash
# Executar gate diferencial em CI: reportar e falhar apenas se surgirem novos achados em relação à baseline
dalfox --config /etc/secops/dalfox.toml scan "https://pr-42.staging.corp/search?q=test" \
  --baseline /var/lib/dast/baseline-main.json \
  --baseline-mode filter \
  --only-poc v \
  --format sarif --output /tmp/dalfox-pr-42.sarif
```

## Limites e trade-offs
Note que `--stream-findings` é desativado automaticamente quando `--output`, `--limit`, `--only-poc` ou `--baseline` estão presentes para garantir que o arquivo final passe pela deduplicação e filtragem completas antes da escrita.

## Como verificar
Execute o comando usando o próprio relatório anterior como `--baseline` e confirme que o Dalfox reporta `0` novos achados e retorna exit code `0`.

## Conexões
- [[dalfox-modos-server-rest-api-mcp-stdio-integracao-automacao]] — Veja também: Dalfox: Subcomandos `dalfox server` (REST API) e `dalfox mcp` (Model Context Protocol stdio Server).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[dalfox-pipeline-mode-katana-dedup-urls-state-file-resume]] — Referência cruzada direta com dalfox-pipeline-mode-katana-dedup-urls-state-file-resume.
- [[brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml]] — Referência cruzada direta com brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
