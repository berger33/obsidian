---
id: software.seguranca.tranche08.000760
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/OJ/gobuster/master/README.md", "https://github.com/OJ/gobuster/wiki", "https://pkg.go.dev/github.com/OJ/gobuster/v3"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gobuster: Controle de Taxa (`--delay`, `-t`), User-Agent (`-a`), TLS (`--tls-min-version`) e **Detecção Defensiva no WAF / SIEM**

## Em uma frase
Disparar 50 goroutines sem pausa (`-t 50`) contra um servidor de aplicação pequeno pode esgotar o pool de workers PHP-FPM/Gunicorn ou acionar imediatamente regras de *Rate Limiting* (`HTTP 429 Too Many Requests`) no WAF / CrowdSec / Fail2ban.

## Por que importa
Para controlar rigorosamente a taxa de requisições em ambientes sensíveis, combine um número reduzido de threads (ex.: **`-t 5`**) com **`--delay 200ms`** (que faz cada thread aguardar 200 ms entre requisições, resultando em um teto previsível de no máximo `25 req/s` no total), além de definir um **`-a` (`--useragent`)** identificando a auditoria autorizada (`SecOps-Authorized-Audit/2026`).

## Como funciona
Pelo lado da **Engenharia de Detecção (Blue Team / SOC)**, o User-Agent padrão do Gobuster (`gobuster/3.x`) e a assinatura comportamental de centenas de `404 Not Found` por segundo vindos do mesmo IP devem ser detectados imediatamente no Coraza WAF, Suricata e CrowdSec.

## Exemplo
```bash
# Executar varredura controlada (maximo ~20 req/s com 4 threads e delay de 200ms) com User-Agent de auditoria autorizada
gobuster dir -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -t 4 --delay 200ms --timeout 10s \
  -a "Mozilla/5.0 (Compatible; SecOps-Pentest-Ticket-9482)" \
  --no-progress -q -o /cases/pentest/gobuster_throttled.txt
```

## Limites e trade-offs
Quando um servidor legado exige uma versão específica de TLS ou quando você quer auditar qual versão mínima de TLS o backend aceita durante a enumeração, o Gobuster oferece a flag **`--tls-min-version`** (`1.0`, `1.1`, `1.2`, `1.3`).

## Como verificar
No lado defensivo (WAF/SIEM), configure alertas tanto pela string literal `gobuster/` no cabeçalho `User-Agent` quanto pela taxa de respostas `404`/`403` por IP (> 30 erros 404 em 10 segundos).

## Conexões
- [[gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups]] — Veja também: Gobuster: Geração de Permutações por **Arquivo de Padrões (`-p` / `--pattern`)** para Descoberta de Backups e Artefatos Corporativos.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
