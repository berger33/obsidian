---
id: software.seguranca.tranche16.001563
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

# Fluxo Operacional Completo no Console do Ligolo-ng (`v0.6+` / `v0.8+`): **`session`**, **`ifconfig`**, **`interface_create`**, **`interface_add_route`** e **`tunnel_start`**

## Em uma frase
Antigamente, operar um túnel TUN exigia abrir outro terminal no Linux para rodar `ip tuntap add`, `ip link set up` e `ip route add` manualmente. Como as versões modernas do **Ligolo-ng (`v0.6+` e `v0.8+`)** automatizam 100% da criação de interfaces, descoberta de sub-redes e configuração de rotas (`autoroute`) em **Linux, Windows, macOS e BSD** diretamente de dentro do console do `proxy`?

## Por que importa
Veja a sequência de 4 comandos no console interativo do `ligolo-ng`: **(1) `session`** — seleciona o agente conectado; **(2) `ifconfig`** — exibe uma tabela formatada com **todas as placas de rede, endereços IPv4/IPv6, máscaras CIDR e MACs da máquina remota onde o `agent` está rodando** (revelando na hora quais sub-redes internas existem lá!).

## Como funciona
**(3) `interface_create --name "ligolo-rede1"`** + **`interface_add_route --name ligolo-rede1 --route 192.168.2.0/24`** (ou o assistente automático **`autoroute`** da versão `0.8+`!); e **(4) `tunnel_start --tun ligolo-rede1`** — ativa o fluxo de pacotes entre a interface `TUN` e o `gVisor` do agente!

## Exemplo
```text
# Descobrir as interfaces da maquina remota (ifconfig), criar a interface TUN, adicionar a rota e iniciar o tunel pelo console do Ligolo-ng
ligolo-ng » interface_create --name "tun-dmz"
ligolo-ng » session
[Agent : user@srv-dmz] » ifconfig
[Agent : user@srv-dmz] » interface_add_route --name tun-dmz --route 172.16.40.0/24
[Agent : user@srv-dmz] » tunnel_start --tun tun-dmz
```

## Limites e trade-offs
Olhe que avanço na versão **`Ligolo-ng 0.8+`** destacado no `README.md`: além do comando **`autoroute`** (que lê as interfaces do `ifconfig` do agente e permite selecionar com barra de espaço quais sub-redes você quer rotear automaticamente!), o Ligolo-ng 0.8 trouxe **Auto-bind** (configuração automática de túnel em arquivo YAML assim que um agente específico conecta), **Daemon Mode** e uma **Web UI + API REST para operação Multiplayer**!

## Como verificar
E se a conexão de rede cair momentaneamente? O Ligolo-ng possui **recuperação automática de túneis e listeners**: assim que o agente reconecta, o túnel volta a trafegar pacotes sem precisar recriar rotas!

## Conexões
- [[ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning]] — Veja também: Segurança Criptográfica do Túnel Ligolo-ng: **Let's Encrypt (`-autocert`)**, Certificados Próprios (`-certfile`) e Pinning de **SHA-256 Fingerprint (`-selfcert` + `-accept-fingerprint`)**.
- [[ligolo-acesso-ip-local-agente-magic-cidr-240-0-0-1-loopback]] — Veja também: Acessando Serviços em **`127.0.0.1` (`localhost`)** da Própria Máquina do Agente via Ligolo-ng: O Endereço Mágico **`240.0.0.1`**.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[ligolo-port-forwarding-reverso-listeners-agent-bind-transferencia]] — Referência cruzada direta com ligolo-port-forwarding-reverso-listeners-agent-bind-transferencia.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
