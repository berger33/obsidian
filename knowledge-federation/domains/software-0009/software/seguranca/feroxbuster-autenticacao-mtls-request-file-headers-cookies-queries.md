---
id: software.seguranca.tranche09.000897
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md", "https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example", "https://epi052.github.io/feroxbuster-docs/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Feroxbuster: Auditoria Autenticada via **`--request-file` (Raw HTTP)**, Certificados **mTLS (`--client-cert`, `--client-key`)**, `-H`, `-b` e `-Q`

## Em uma frase
Para auditar aplicações protegidas por autenticação complexa, o Feroxbuster suporta carregar diretamente um arquivo contendo uma **Requisição HTTP Bruta (`--request-file <arquivo.raw>`)** exportada do `mitmproxy`, ZAP ou Burp Suite: herdando automaticamente método HTTP, cabeçalhos, cookies e corpo da requisição!

## Por que importa
Para ambientes Zero Trust e APIs financeiras com **mTLS**, conforme documentado em `ferox-config.toml.example`, o Feroxbuster possui suporte nativo a certificados de cliente via **`--client-cert <cert.pem>`** e **`--client-key <key.pem>`**, além de **`--server-certs <ca_interna.pem>`** para confiar na Autoridade Certificadora privada da empresa sem precisar desligar a verificação TLS com `-k` (`--insecure`)!

## Como funciona
Você também pode adicionar cabeçalhos (`-H "Authorization: Bearer ..."`), cookies (`-b "session=..."`) e parâmetros fixos de Query String em todas as requisições com **`-Q` / `--query "token=abc"`**!

## Exemplo
```bash
# Executar o Feroxbuster autenticado com certificado mTLS (--client-cert/--client-key) e validando contra a CA interna (--server-certs)
feroxbuster -u https://mtls-portal.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt \
  --client-cert /cases/pentest/client.crt \
  --client-key /cases/pentest/client.key \
  --server-certs /etc/secops/corp-root-ca.pem \
  -H "Accept: application/json" \
  -o /cases/pentest/ferox_mtls_api.txt
```

## Limites e trade-offs
Ao realizar uma varredura recursiva autenticada (com `-b` cookies ou `--request-file`), utilize sempre **`--url-denylist`** ou **`--dont-scan` (`--regex-denylist "/(logout|signout|delete).*"`)** para garantir que o Feroxbuster nunca acesse rotas que destruam a sessão autenticada!

## Como verificar
Confira com `--regex-denylist` que qualquer link `/logout` extraído do HTML pelo `--extract-links` é sumariamente ignorado.

## Conexões
- [[feroxbuster-encaminhamento-seletivo-replay-proxy-replay-codes-burp-mitmproxy]] — Veja também: Feroxbuster: **`--replay-proxy`** e **`--replay-codes`** — Como Enviar Apenas os Achados Válidos (`200`, `301`, `403`) para o **`mitmproxy` / ZAP / Burp**.
- [[feroxbuster-configuracao-persistente-ferox-config-toml-escopo]] — Veja também: Feroxbuster: Padronização Corporativa com **`ferox-config.toml`**, Controle de Fronteira (**`--scope`**) e Bloqueio (**`--dont-scan`**).
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies]] — Referência cruzada direta com gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
