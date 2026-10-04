---
id: software.seguranca.tranche16.001568
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

# Operando **Múltiplos Túneis Simultâneos** para Diferentes Sub-Redes no Ligolo-ng: Uma Interface **`TUN`** Dedicada por Agente

## Em uma frase
Um erro comum de quem está começando a usar o Ligolo-ng: você já tem o `Agent 1` conectado com um túnel ativo na interface `tun0` roteando a rede `10.10.0.0/24`. Aí um `Agent 2` conecta de outra filial (`172.16.0.0/24`) e você tenta rodar `tunnel_start --tun tun0` na mesma interface `tun0`! Por que uma interface `TUN` só pode estar associada a **um túnel ativo por vez**, e como operar **5 túneis ativos simultaneamente** no mesmo servidor `proxy`?

## Por que importa
Porque no Kernel do sistema operacional, cada dispositivo `TUN` ponto-a-ponto possui um único descritor de arquivo leitor/escritor!

## Como funciona
Para manter **múltiplos túneis ativos ao mesmo tempo** (por exemplo, roteando pacotes simultaneamente para a DMZ pelo `Agent 1`, para a Rede de Servidores pelo `Agent 2` e para a Rede de Domínio pelo `Agent 3`), basta criar **uma interface `TUN` nomeada para cada agente** usando **`interface_create --name tun-agente1`**, **`interface_create --name tun-agente2`** e **`interface_create --name tun-agente3`**!

## Exemplo
```text
# Criar duas interfaces TUN dedicadas no Ligolo-ng e manter dois tuneis ativos simultaneamente para duas sub-redes distintas
ligolo-ng » interface_create --name "tun-rede-a"
ligolo-ng » interface_create --name "tun-rede-b"
ligolo-ng » interface_add_route --name tun-rede-a --route 10.10.10.0/24
ligolo-ng » interface_add_route --name tun-rede-b --route 172.16.20.0/24
```

## Limites e trade-offs
Veja que organização impecável na tabela de roteamento do seu Linux (`ip route show`): todo pacote destinado a `10.10.10.0/24` entra automaticamente na placa `tun-rede-a` (sendo enviado ao `Agent 1`), enquanto todo pacote destinado a `172.16.20.0/24` entra automaticamente na placa `tun-rede-b` (sendo enviado ao `Agent 2`), permitindo que suas ferramentas conversem com as duas redes ao mesmo tempo!

## Como verificar
E se duas redes isoladas de clientes ou filiais diferentes usarem **exatamente a mesma faixa de IP (ex.: ambas usam `192.168.1.0/24`)**? Você pode adicionar rotas `/32` específicas para os IPs ativos de cada filial apontando para a respectiva interface `tun-filial1` ou `tun-filial2`, ou isolar cada interface `TUN` dentro de um **Network Namespace (`ip netns`)** dedicado!

## Conexões
- [[ligolo-transporte-websocket-socks-proxy-saida-corporativo-bind-mode]] — Veja também: Atravessando Proxies Corporativos e Firewalls no Ligolo-ng: **Suporte a WebSockets (`ws://` / `wss://`)**, Proxy de Saída (**`--socks`**) e **Modo Bind**.
- [[ligolo-auditoria-active-directory-impacket-netexec-certipy-bloodhound-tun]] — Veja também: Executando Ferramentas de Auditoria **Active Directory (`NetExec`, `Impacket`, `Certipy`, `BloodHound CE`, `Responder`)** Nativamente sobre a Interface `TUN` do Ligolo-ng.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Referência cruzada direta com ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun.
- [[tcpdump-captura-remota-ssh-pipes-wireshark-containers-netns-nsenter]] — Referência cruzada direta com tcpdump-captura-remota-ssh-pipes-wireshark-containers-netns-nsenter.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
