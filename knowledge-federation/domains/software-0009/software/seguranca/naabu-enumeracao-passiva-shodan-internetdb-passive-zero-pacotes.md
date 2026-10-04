---
id: software.seguranca.tranche09.000813
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

# Naabu **`-passive`**: Enumeração Passiva Instantânea de Portas Abertas via **Shodan InternetDB** com Zero Pacotes Enviados ao Alvo

## Em uma frase
Quando o ROE (*Rules of Engagement*) exige reconhecimento 100% passivo (sem enviar um único pacote TCP/UDP para a infraestrutura do alvo) ou quando você precisa de uma triagem instantânea de milhares de IPs em poucos segundos, o Naabu integra nativamente a API gratuita **Shodan InternetDB (`https://internetdb.shodan.io`)** através da flag **`-passive`**!

## Por que importa
No modo **`naabu -host <ip/subdominio> -passive`**, o Naabu resolve os endereços IP (ou lê IPs/CIDRs diretamente) e consulta o banco de dados do InternetDB da Shodan, retornando todas as portas abertas conhecidas para aqueles IPs em formato `host:porta` padrão.

## Como funciona
Como a saída de `naabu -passive` é idêntica à saída de um scan ativo do Naabu, você pode substituir um scan ativo demorado por `-passive` em qualquer pipeline Unix existente sem alterar nenhum script subsequente!

## Exemplo
```bash
# Consultar passivamente todas as portas abertas conhecidas no Shodan InternetDB para uma lista de ativos sem tocar no alvo
naabu -list /cases/easm/subdomains.txt \
  -passive \
  -json -o /cases/easm/passive_ports.jsonl
```

## Limites e trade-offs
Tenha em mente o *trade-off* natural do modo `-passive`: o Shodan InternetDB reflete os dados da última varredura global do Shodan (geralmente atualizada a cada poucos dias para as portas mais comuns) e cobre apenas **IPv4 público**; portas altas efêmeras abertas hoje pela manhã ou redes internas privadas (`10.0.0.0/8`) exigem varredura ativa.

## Como verificar
Compare a saída de `naabu -passive` com uma varredura ativa `-s s -p -` para medir quais portas não-padrão o Shodan não indexou.

## Conexões
- [[naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao]] — Veja também: Naabu: Exclusão Inteligente de **IPs de CDN / WAF (`-exclude-cdn` / `-ec`)** e Proteção contra Honeypots/Port-Spoofing (**`-port-threshold` / `-pts`**).
- [[naabu-descoberta-hosts-ativos-host-discovery-sn-wn-icmp-arp-tcp]] — Veja também: Naabu **Host Discovery (`-sn` / `-wn`)**: Sondagem Híbrida de Hosts Vivos via **ICMP (`-pe`, `-pp`, `-pm`)**, **TCP Ping (`-ps`, `-pa`)**, **ARP (`-arp`)** e **IPv6 ND (`-nd`)**.
- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — Referência cruzada direta com naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.

## Fontes
- [ProjectDiscovery Naabu Official GitHub — Fast Port Scanner Written in Go](https://raw.githubusercontent.com/projectdiscovery/naabu/main/README.md) — repositório oficial do ProjectDiscovery Naabu cobrindo arquitetura SYN/CONNECT, flags CLI, descoberta de hosts e integração com Nmap; consultado em 2026-10-03.
- [ProjectDiscovery Naabu Official Documentation — Usage, Configuration & Rate Tuning](https://raw.githubusercontent.com/projectdiscovery/naabu/main/go.mod) — documentação oficial do Naabu na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/naabu/v2](https://docs.projectdiscovery.io/tools/naabu/overview) — documentação técnica do pacote Go e SDK `naabu/v2/pkg/runner`; consultado em 2026-10-03.
