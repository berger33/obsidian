---
id: software.seguranca.tranche16.001564
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

# Acessando Serviços em **`127.0.0.1` (`localhost`)** da Própria Máquina do Agente via Ligolo-ng: O Endereço Mágico **`240.0.0.1`**

## Em uma frase
Imagine que após conectar o `agent` do Ligolo-ng a um servidor web (`10.10.10.5`), você roda `netstat` ou `ss -tulnp` naquele servidor e descobre que o **PostgreSQL (`5432`)**, o **Redis (`6379`)** ou uma API de administração (`8080`) estão escutando **exclusivamente no loopback local `127.0.0.1` daquela máquina**! Se você tentar acessar `127.0.0.1:5432` na sua própria estação de auditoria, você vai bater no seu próprio computador, e não no `localhost` do agente remoto!

## Por que importa
Como o **Ligolo-ng** resolve o acesso ao `127.0.0.1` interno da máquina onde o `agent` está rodando sem precisar criar port-forwards manuais para cada porta?

## Como funciona
Através do **IP Mágico Reservado `240.0.0.1`**! No Ligolo-ng, basta adicionar a rota **`240.0.0.1/32`** apontando para a sua interface `TUN` do Ligolo (`ip route add 240.0.0.1/32 dev ligolo` ou via `interface_add_route`): **qualquer pacote enviado pela sua máquina para o IP `240.0.0.1` é automaticamente traduzido pelo `agent` remoto para o `127.0.0.1` (`localhost`) da própria máquina onde o `agent` está rodando**!

## Exemplo
```bash
# Adicionar a rota para o IP magico 240.0.0.1/32 na interface TUN do Ligolo-ng para acessar todos os servicos em 127.0.0.1 do host remoto
ip route add 240.0.0.1/32 dev tun-dmz
psql -h 240.0.0.1 -p 5432 -U postgres
curl -sS http://240.0.0.1:8080/actuator/env
```

## Limites e trade-offs
Veja a genialidade dessa convenção **`240.0.0.1/32`**: em vez de abrir 5 comandos `portfwd` separados para as portas `5432`, `6379`, `8080`, `9000` e `9200` que escutam em `127.0.0.1` no servidor remoto, basta uma única rota `240.0.0.1/32 dev tun-dmz` — a partir desse instante, `240.0.0.1` na sua estação **É o `127.0.0.1` do servidor remoto** para todas as 65.535 portas TCP e UDP!

## Como verificar
Por que o Ligolo-ng escolheu o endereço `240.0.0.1`? Porque o bloco `240.0.0.0/4` (antiga Classe E na `RFC 1112`) nunca é roteado na internet pública nem usado pelas faixas privadas `RFC 1918` (`10/8`, `172.16/12`, `192.168/16`), evitando qualquer conflito de endereçamento com as sub-redes reais da empresa auditada!

## Conexões
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Veja também: Fluxo Operacional Completo no Console do Ligolo-ng (`v0.6+` / `v0.8+`): **`session`**, **`ifconfig`**, **`interface_create`**, **`interface_add_route`** e **`tunnel_start`**.
- [[ligolo-port-forwarding-reverso-listeners-agent-bind-transferencia]] — Veja também: Listeners e Port Forwarding Reverso no Ligolo-ng (**`listener_add`**, **`listener_list`**): Recebendo Conexões e Implantes da Rede Interna Isolada.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Referência cruzada direta com chisel-encaminhamento-portas-forward-reverse-r-socks5-udp.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
