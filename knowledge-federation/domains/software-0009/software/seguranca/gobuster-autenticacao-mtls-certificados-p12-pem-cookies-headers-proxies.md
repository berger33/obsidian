---
id: software.seguranca.tranche08.000758
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

# Gobuster: Varredura Autenticada com **Certificados de Cliente mTLS (`--client-cert-p12` / `--client-cert-pem`)**, Cookies, JWT e Proxies (`--proxy`)

## Em uma frase
Em ambientes Zero Trust e APIs financeiras/corporativas (como Open Finance ou portais administrativos internos), o servidor TLS rejeita conexões na camada de handshake se o cliente não apresentar um certificado **mTLS** válido, ou retorna `401 Unauthorized` sem um token Bearer/Cookie de sessão.

## Por que importa
Conforme documentado no `README.md` oficial do Gobuster, todos os modos baseados em HTTP (`dir`, `vhost`, `fuzz`, `s3`, `gcs`) suportam nativamente **autenticação mútua TLS (mTLS)** tanto com arquivos PKCS#12 (**`--client-cert-p12 <arquivo.p12>`** + `--client-cert-p12-password`) quanto com pares PEM (**`--client-cert-pem <cert.pem>`** + **`--client-cert-key <key.pem>`**)!

## Como funciona
Além disso, você pode passar cookies de sessão (`-c "session=..."`), cabeçalhos HTTP arbitrários (`-H "Authorization: Bearer ..."`), Basic Auth (`-U usuario -P senha`) e encaminhar todo o tráfego através de um proxy HTTP/SOCKS5 (`--proxy http://127.0.0.1:8080` ou `socks5://127.0.0.1:1080`, como o **`mitmproxy`**).

## Exemplo
```bash
# Executar enumeracao autenticada com Certificado de Cliente mTLS (PEM) + Token JWT encaminhando erros pelo proxy local
gobuster dir -u https://mtls-api.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt \
  --client-cert-pem /cases/pentest/client.crt \
  --client-cert-key /cases/pentest/client.key \
  -H "Authorization: Bearer eyJhbGciOiJFUzI1NiIs..." \
  -t 15 -o /cases/pentest/gobuster_mtls_api.txt
```

## Limites e trade-offs
Ao realizar varredura autenticada com `-c` (cookie de sessão) ou `-H "Authorization: ..."`, **exclua explicitamente da wordlist palavras como `logout`, `signout`, `logoff`, `revoke` e `delete-account`**, pois se a primeira goroutine do Gobuster acessar `/logout`, o servidor invalidará a sessão no backend e todas as outras 10.000 requisições seguintes rodarão desautenticadas!

## Como verificar
Verifique no `mitmproxy` (via `--proxy http://127.0.0.1:8080`) que as requisições permanecem autenticadas durante toda a execução.

## Conexões
- [[gobuster-enumeracao-tftp-equipamentos-rede-voip-firmwares-configs]] — Veja também: Gobuster Modo **`tftp`**: Auditoria de Servidores **TFTP (Porta 69/UDP)** em Redes Internas, Telefonia VoIP e Provisionamento PXE/Cisco.
- [[gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups]] — Veja também: Gobuster: Geração de Permutações por **Arquivo de Padrões (`-p` / `--pattern`)** para Descoberta de Backups e Artefatos Corporativos.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Referência cruzada direta com mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile.
- [[testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd]] — Referência cruzada direta com testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
