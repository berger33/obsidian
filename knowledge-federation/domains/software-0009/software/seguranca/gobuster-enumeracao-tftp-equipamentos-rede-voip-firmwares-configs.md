---
id: software.seguranca.tranche08.000757
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

# Gobuster Modo **`tftp`**: Auditoria de Servidores **TFTP (Porta 69/UDP)** em Redes Internas, Telefonia VoIP e Provisionamento PXE/Cisco

## Em uma frase
Em pentests de redes corporativas internas, segmentos de gerência de switches/roteadores e VLANs de telefonia IP (VoIP) ou boot PXE, é comum encontrar servidores **TFTP (*Trivial File Transfer Protocol*, RFC 1350, porta 69/UDP)** ativos.

## Por que importa
O protocolo TFTP **não possui autenticação e tampouco possui comando de listagem de diretórios (`ls` / `DIR`)**: um cliente TFTP só consegue baixar um arquivo se souber o nome exato dele!

## Como funciona
O modo **`gobuster tftp -s <servidor:69> -w <wordlist>`** automatiza a descoberta concorrente de arquivos de configuração e firmwares em servidores TFTP (como `startup-config`, `running-config`, `router-confg`, `SEP<MAC>.cnf.xml` de telefones IP contendo senhas SIP, ou `pxelinux.cfg/default`).

## Exemplo
```bash
# Auditar um servidor TFTP interno (porta 69/UDP) em busca de arquivos de configuracao de switches/roteadores e VoIP expostos
gobuster tftp -s 10.10.20.5:69 \
  -w /usr/share/seclists/Discovery/Infrastructure/common-tftp-filenames.txt \
  --timeout 2s -t 10 -o /cases/pentest/gobuster_tftp_files.txt
```

## Limites e trade-offs
Como o TFTP opera sobre **UDP**, evite usar um número alto de threads (`-t 5` a `-t 10` é o ideal): servidores TFTP embarcados têm buffers UDP pequenos e descartam pacotes se receberem 100 requisições simultâneas, gerando falsos negativos por timeout.

## Como verificar
Se o `gobuster tftp` encontrar arquivos de configuração sensíveis expostos sem autenticação, recomende desativar o TFTP em favor de SCP/SFTP/HTTPS com mTLS ou restringir o servidor TFTP por ACL de IP estrita.

## Conexões
- [[gobuster-modo-fuzz-marcador-customizado-url-headers-body-parametros]] — Veja também: Gobuster Modo **`fuzz`**: Fuzzing de Parâmetros Query/REST, Cabeçalhos HTTP e Corpo de Requisição com a Palavra-Chave **`FUZZ`**.
- [[gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies]] — Veja também: Gobuster: Varredura Autenticada com **Certificados de Cliente mTLS (`--client-cert-p12` / `--client-cert-pem`)**, Cookies, JWT e Proxies (`--proxy`).
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.
- [[masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados]] — Referência cruzada direta com masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
