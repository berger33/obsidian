---
id: software.seguranca.tranche05.000405
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
fontes: ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md", "https://github.com/sqlmapproject/sqlmap/wiki/Usage", "https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# sqlmap: Scripts de Transformação (`--tamper`) para Avaliação de Regras de WAF e Normalização de Payloads

## Em uma frase
A arquitetura de *Tamper Scripts* (`--tamper` em `tamper/*.py`) do `sqlmap` aplica transformações sintáticas sobre os payloads SQL antes do envio para testar a eficácia de regras de Web Application Firewall (WAF) e filtros de entrada.

## Por que importa
Em exercícios de *Purple Team* e validação de WAFs (como OWASP Coraza / ModSecurity CRS), testar scripts de *tamper* revela se o WAF bloqueia apenas assinaturas literais ingênuas (`UNION SELECT`) ou se analisa comentários inline (`/*!50000UNION*/`), codificação dupla e substituições de espaço.

## Como funciona
Cada script em `tamper/` expõe uma função `tamper(payload, **kwargs)` que reescreve o payload para o dialeto do SGBD alvo (ex.: `space2comment` troca espaços por `/**/`, `between` substitui operadores `>` por `NOT BETWEEN 0 AND`, `charencode` aplica URL-encode completo e `randomcase` alterna maiúsculas/minúsculas).

## Exemplo
```bash
# Testar se a política do WAF de homologação detecta payloads com comentários inline e BETWEEN
python3 sqlmap.py -u "https://waf-test.staging.corp/search?q=laptop" \
  -p q --dbms=MySQL \
  --tamper=space2comment,between \
  --random-agent --abort-code=403 --batch
```

## Limites e trade-offs
Encadear múltiplos scripts `--tamper` incompatíveis com o SGBD de destino (ex.: usar sintaxe específica de MySQL `versionedkeywords` contra um banco PostgreSQL) corrompe a gramática SQL e gera falsos negativos.

## Como verificar
Execute o teste contra o ambiente protegido pelo WAF e verifique nos logs do WAF (ex.: regra CRS `942100`) se os payloads transformados foram devidamente bloqueados com `HTTP 403`.

## Conexões
- [[sqlmap-injecao-second-order-csrf-tokens-sessoes-autenticadas]] — Veja também: sqlmap: Detecção de *Second-Order SQL Injection* (`--second-url`), Renovação de `--csrf-token` e `--eval`.
- [[sqlmap-exfiltracao-out-of-band-dns-domain-time-based-blind]] — Veja também: sqlmap: Aceleração de Blind SQL Injection via Exfiltração *Out-of-Band* DNS (`--dns-domain`).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — Referência cruzada direta com sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao.
- [[sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive]] — Referência cruzada direta com sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
