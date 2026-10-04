---
id: software.seguranca.tranche16.001566
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md", "https://docs.ligolo.ng/Quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Por Que Usar **`nmap --unprivileged`** (ou `-sT -Pn`) Através do Ligolo-ng? Entendendo a Tradução de Pacotes `SYN` e `ICMP` no `gVisor` do Agente

## Em uma frase
Na seção *Caveats* do `README.md` oficial do Ligolo-ng, o autor faz um alerta técnico fundamental: *"Because the agent is running without privileges, it's not possible to forward raw packets. When you perform a NMAP SYN-SCAN, a TCP connect() is performed on the agent. When using nmap, you should use `--unprivileged` or `-PE` to avoid false positives."* Por que isso acontece no nível de pacotes?

## Por que importa
Entenda o que ocorre se você rodar o `nmap` como `root` na sua estação de auditoria sem passar `--unprivileged`: **(1)** Como você é `root` na sua máquina local, o `nmap` assume que pode fazer **Raw Socket SYN Scan (`-sS`)** e enviar pacotes TCP `ACK` de descoberta de host (`-PA`); **(2)** Quando o `gVisor` da interface `TUN` recebe um pacote `ACK` solto de descoberta, ele pode responder `RST`, fazendo o `nmap` achar que **todos os 254 IPs da sub-rede estão vivos (Falso Positivo de Host Discovery!)**!

## Como funciona
Já quando você passa **`nmap --unprivileged`** (ou **`-sT -PE -n`**), o Nmap sabe que deve usar chamadas de conexão TCP completas (`-sT`) e ping `ICMP Echo Request` (`-PE`, que o Ligolo-ng traduz perfeitamente!), entregando resultados 100% precisos e super rápidos!

## Exemplo
```bash
# Executar varredura de descoberta e portas com Nmap sobre a interface TUN do Ligolo-ng usando --unprivileged e -PE conforme documentado no README
nmap --unprivileged -PE -n -T4 -p 22,80,88,135,139,389,443,445,636,1433,3306,3389,5432,5985 172.16.40.0/24
```

## Limites e trade-offs
Veja na prática: como o Ligolo-ng suporta **Multiplexação Nativa sobre `gVisor`** (sem o overhead de abrir uma nova conexão SOCKS para cada porta como no `proxychains4`), o comando `nmap --unprivileged` acima escaneia uma sub-rede `/24` inteira em **poucos segundos**!

## Como verificar
E para varreduras de portas UDP (como DNS `53/udp`, SNMP `161/udp` ou Kerberos `88/udp`), como o Ligolo-ng transporta **TCP, UDP e ICMP Echo** nativamente na interface `TUN`, você também pode rodar `nmap -sU -Pn -p 53,161 172.16.40.10` diretamente!

## Conexões
- [[ligolo-port-forwarding-reverso-listeners-agent-bind-transferencia]] — Veja também: Listeners e Port Forwarding Reverso no Ligolo-ng (**`listener_add`**, **`listener_list`**): Recebendo Conexões e Implantes da Rede Interna Isolada.
- [[ligolo-transporte-websocket-socks-proxy-saida-corporativo-bind-mode]] — Veja também: Atravessando Proxies Corporativos e Firewalls no Ligolo-ng: **Suporte a WebSockets (`ws://` / `wss://`)**, Proxy de Saída (**`--socks`**) e **Modo Bind**.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap]] — Referência cruzada direta com chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
