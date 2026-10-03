---
id: software.seguranca.tranche09.000818
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod", "https://docs.projectdiscovery.io/tools/naabu/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Naabu: Varredura Direta por **ASN (`AS1449`) e CIDR**, Exclusão de Escopo (`-eh` / `-ef`) e Política de Rede (`networkpolicy`)

## Em uma frase
Assim como o `tlsx` e o `uncover`, o Naabu aceita na entrada (`-host` ou `-list`) não apenas IPs e domínios, mas também identificadores de **Sistemas Autônomos (`AS<numero>`, ex.: `AS13335`)** e blocos **CIDR (`192.0.2.0/24`)**, expandindo automaticamente o ASN para seus prefixos IPv4 anunciados via `projectdiscovery/mapcidr` e `asnmap`!

## Por que importa
Para garantir conformidade estrita com o escopo autorizado da auditoria, as flags **`-exclude-hosts` (`-eh`)** e **`-exclude-file` (`-ef <arquivo.txt>`)** removem IPs, sub-redes CIDR ou domínios proibidos antes que qualquer pacote saia da interface de rede.

## Como funciona
Além disso, o Naabu incorpora a biblioteca **`projectdiscovery/networkpolicy`** para evitar redirecionamentos ou sondagens acidentais para endereços restritos não autorizados.

## Exemplo
```bash
# Varrer blocos CIDR autorizados excluindo uma lista de IPs criticos (-ef) e portas de impressoras (-ep 9100)
naabu -list /cases/easm/authorized_cidrs.txt \
  -exclude-file /cases/easm/do_not_scan_ips.txt \
  -exclude-ports 9100 \
  -top-ports 100 \
  -rate 1000 \
  -o /cases/easm/cidr_port_inventory.txt
```

## Limites e trade-offs
Assim como no Masscan e no ZMap, mantenha sempre um arquivo padrão `/cases/easm/do_not_scan_ips.txt` atualizado e passe **`-ef`** em todos os jobs agendados do Naabu.

## Como verificar
Valide com um IP de teste dentro do `do_not_scan_ips.txt` que o Naabu ignora completamente o endereço excluído.

## Conexões
- [[naabu-varredura-atraves-proxies-socks5-connect-payload-ipv6]] — Veja também: Naabu em Operações Red Team e Pivoting: Varredura `CONNECT` via **Proxy SOCKS5 (`-proxy`, `-proxy-auth`)** e **`-connect-payload` (`-cp`)**.
- [[naabu-configuracao-persistente-resume-cfg-metricas-monitoramento]] — Veja também: Naabu: Arquivo de Configuração Persistente (`~/.config/naabu/config.yaml`), Retomada de Varredura (**`-resume`**) e Telemetria (`-metrics-port`).
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — Referência cruzada direta com zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
