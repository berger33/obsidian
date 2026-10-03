---
id: software.seguranca.tranche09.000817
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

# Naabu em Operações Red Team e Pivoting: Varredura `CONNECT` via **Proxy SOCKS5 (`-proxy`, `-proxy-auth`)** e **`-connect-payload` (`-cp`)**

## Em uma frase
Durante uma operação de Red Team ou pentest interno em que o operador estabeleceu um túnel **SOCKS5** (via `ssh -D 1080`, Chisel, Ligolo-ng ou Sliver/Metasploit) para dentro de uma VLAN isolada, scanners baseados em pacotes SYN brutos (`masscan`, `zmap`, `nmap -sS`) **não funcionam através de um proxy SOCKS5** porque o protocolo SOCKS5 transporta fluxos TCP de camada de sessão (`CONNECT`), e não pacotes IP brutos.

## Por que importa
O Naabu resolve o reconhecimento interno via pivot perfeitamente combinando **`-s c` (CONNECT Scan)** com as flags nativas **`-proxy socks5://127.0.0.1:1080`** (ou `-proxy 127.0.0.1:1080`) e **`-proxy-auth usuario:senha`**!

## Como funciona
Não é necessário sequer usar `proxychains` externo: as goroutines internas do Naabu (`-c 25`) negociam diretamente com o servidor SOCKS5 usando a biblioteca `go-socks5` e podem enviar um payload customizado na conexão com **`-cp` / `-connect-payload`**!

## Exemplo
```bash
# Varrer portas internas de uma sub-rede isolada diretamente atraves de um tunel SOCKS5 (ex.: ssh -D 1080) usando modo CONNECT
naabu -host 10.40.50.0/24 \
  -s c \
  -p 22,80,88,135,139,389,443,445,1433,3306,3389,5432,5985,8080,8443 \
  -proxy 127.0.0.1:1080 \
  -c 20 -rate 200 \
  -o /cases/pentest/pivoted_internal_ports.txt
```

## Limites e trade-offs
Ao varrer através de um túnel SOCKS5 ou pivô SSH, mantenha a concorrência moderada (`-c 15` a `-c 25` e `-rate 100` a `300`) para não esgotar o limite de canais multiplexados (`MaxSessions`) do daemon SSH no host pivô.

## Como verificar
Verifique que as portas descobertas pelo Naabu via `-proxy` respondem ao `netexec` ou `httpx -http-proxy socks5://127.0.0.1:1080`.

## Conexões
- [[naabu-selecao-portas-top-ports-full-smart-scan-preditivo-verify]] — Veja também: Naabu: Seleção de Portas (`-p -`, `-top-ports full|100|1000`), Verificação Dupla TCP (**`-verify`**) e **Smart Scan Preditivo (`-ss` / `-smart-scan`)**.
- [[naabu-entrada-asn-cidr-exclusao-escopo-exclude-hosts-file]] — Veja também: Naabu: Varredura Direta por **ASN (`AS1449`) e CIDR**, Exclusão de Escopo (`-eh` / `-ef`) e Política de Rede (`networkpolicy`).
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
