---
id: software.seguranca.tranche05.000417
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

# Dalfox: Fingerprinting de WAF (`--waf-min-confidence`), Rastreamento de Bypass e `--custom-payload`

## Em uma frase
O Dalfox realiza *fingerprinting* automático de Web Application Firewalls (Cloudflare, AWS WAF, Akamai, ModSecurity/Coraza, Imperva, F5) com pontuação de confiança configurável (`--waf-min-confidence`) e adapta os vetores de teste ou carrega wordlists customizadas (`--custom-payload` / subcomando `dalfox payload`).

## Por que importa
Permite às equipes de AppSec validar se as regras customizadas do WAF corporativo bloqueiam vetores modernos de XSS sem tags `<script>` (como atributos de eventos SVG/MathML, `onpointerrawupdate`, `ontoggle` ou codificações HTML/Unicode).

## Como funciona
Quando um WAF é detectado acima do limiar `--waf-min-confidence`, o motor registra o provedor identificado, prioriza payloads compatíveis com evasão daquele filtro e rastreia quais payloads contornaram o bloqueio HTTP 403. O subcomando `dalfox payload` permite listar e inspecionar os conjuntos de payloads embutidos e remotos.

## Exemplo
```bash
# Auditar a eficácia de regras de WAF contra uma lista customizada de payloads XSS polimórficos
dalfox scan "https://waf-staging.internal.corp/comment?text=hello" \
  --custom-payload /etc/secops/waf-bypass-xss-payloads.txt \
  --waf-min-confidence 70 \
  --include-all \
  --format json --output /tmp/dalfox-waf-audit.json
```

## Limites e trade-offs
Apenas bloquear XSS no WAF sem corrigir a codificação contextual de saída (*Output Encoding* / *Context-Aware Escaping*) na aplicação é uma mitigação frágil; use o relatório do Dalfox para corrigir o template no código-fonte e implementar `Content-Security-Policy` (CSP) com *nonces*.

## Como verificar
Inspecione `/tmp/dalfox-waf-audit.json` e verifique se algum payload retornou status `200` com reflexão não escapada (tiers `R` ou `V`).

## Conexões
- [[dalfox-controle-escopo-out-of-scope-include-exclude-url]] — Veja também: Dalfox: Governança de Escopo (`--out-of-scope`, `--out-of-scope-file`, `--include-url`, `--exclude-url` e `--ignore-param`).
- [[dalfox-pipeline-mode-katana-dedup-urls-state-file-resume]] — Veja também: Dalfox: Operação em Pipeline (`--input-type pipe`), Deduplicação (`--dedup-urls signature`) e Retomada (`--state-file`).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[dalfox-verificacao-dom-ast-headless-blind-xss-callback]] — Referência cruzada direta com dalfox-verificacao-dom-ast-headless-blind-xss-callback.
- [[sqlmap-tamper-scripts-avaliacao-regras-waf-normalizacao]] — Referência cruzada direta com sqlmap-tamper-scripts-avaliacao-regras-waf-normalizacao.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
