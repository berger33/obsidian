---
id: software.seguranca.tranche08.000759
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

# Gobuster: Geração de Permutações por **Arquivo de Padrões (`-p` / `--pattern`)** para Descoberta de Backups e Artefatos Corporativos

## Em uma frase
Muitas vezes, arquivos críticos esquecidos em servidores web não têm nomes genéricos de dicionário (`backup.zip`), mas nomes compostos derivados da própria palavra atual da wordlist — por exemplo, para a palavra `financeiro`, o desenvolvedor salvou `financeiro-2026.zip`, `bkp_financeiro.sql.gz` ou `financeiro_prod.bak`.

## Por que importa
Em vez de precisar multiplicar manualmente o tamanho da wordlist no disco, o Gobuster suporta a flag **`-p` / `--pattern <arquivo_padroes>`**: para cada palavra lida da wordlist principal (`-w`), o Gobuster substitui o marcador **`{GOBUSTER}`** em cada linha do arquivo de padrões!

## Como funciona
Isso permite manter uma wordlist curta de contextos de negócio da empresa (`auth`, `billing`, `users`, `portal`) e aplicar sobre cada palavra uma matriz de padrões de nomenclatura de backups e artefatos de deploy.

## Exemplo
```bash
# Criar um arquivo de padroes {GOBUSTER} para descobrir arquivos de backup contextualizados e executar o gobuster dir -p
cat << 'EOF' > /cases/pentest/backup_patterns.txt
{GOBUSTER}
{GOBUSTER}-backup.zip
{GOBUSTER}_prod.sql.gz
.{GOBUSTER}.swp
EOF

gobuster dir -u https://app.internal.corp \
  -w /cases/pentest/business_modules.txt \
  -p /cases/pentest/backup_patterns.txt \
  -b 404 --no-error -t 15
```

## Limites e trade-offs
Observe que se a wordlist `-w` tiver 1.000 palavras e o arquivo `-p` tiver 10 linhas de padrões `{GOBUSTER}`, o Gobuster fará `1.000 x 10 = 10.000` requisições (e ainda mais se você combinar com `-x` extensões!); dimensione ambos com cuidado para não exceder a janela do teste.

## Como verificar
Use `--expanded` (`-e`) na saída do `gobuster dir` para imprimir a URL completa (`https://...`) de cada artefato encontrado, facilitando o encadeamento em pipelines.

## Conexões
- [[gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies]] — Veja também: Gobuster: Varredura Autenticada com **Certificados de Cliente mTLS (`--client-cert-p12` / `--client-cert-pem`)**, Cookies, JWT e Proxies (`--proxy`).
- [[gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao]] — Veja também: Gobuster: Controle de Taxa (`--delay`, `-t`), User-Agent (`-a`), TLS (`--tls-min-version`) e **Detecção Defensiva no WAF / SIEM**.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
