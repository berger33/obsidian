---
id: software.seguranca.tranche16.001565
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

# Listeners e Port Forwarding Reverso no Ligolo-ng (**`listener_add`**, **`listener_list`**): Recebendo Conexões e Implantes da Rede Interna Isolada

## Em uma frase
Já sabemos como o Ligolo-ng permite que a sua máquina (`proxy`) inicie conexões **para dentro** da sub-rede do `agent` (`192.168.2.0/24`). Mas e o sentido inverso: quando uma máquina `192.168.2.50` lá na rede interna isolada precisa **conectar de volta para você** (por exemplo, para baixar um arquivo HTTP, entregar uma conexão reversa, responder a uma captura SMB/HTTP ou conectar um **segundo `agent` do Ligolo-ng para Double Pivoting**)?

## Por que importa
Como a máquina `192.168.2.50` não tem rota para a internet, ela só consegue alcançar o IP interno do `Host 1` (`192.168.2.10`, onde está o seu primeiro `agent`)!

## Como funciona
Para isso, o Ligolo-ng possui o comando **`listener_add`**! Quando você executa **`listener_add --addr 0.0.0.0:8443 --to 127.0.0.1:8000 --tcp`** na sessão do `agent`, o `agent` abre a porta `8443` na máquina remota (sem precisar de root para portas `> 1024`!) e redireciona qualquer conexão recebida lá na rede interna diretamente para a porta `127.0.0.1:8000` do seu servidor **`proxy`**!

## Exemplo
```text
# Criar no agente do Ligolo-ng dois listeners reversos: um para servir arquivos HTTP (8080->8000) e outro para encadear um segundo agente Ligolo (11601->11601)
[Agent : user@srv-dmz] » listener_add --addr 0.0.0.0:8080 --to 127.0.0.1:8000 --tcp
[Agent : user@srv-dmz] » listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601 --tcp
[Agent : user@srv-dmz] » listener_list
```

## Limites e trade-offs
Olhe a segunda linha do exemplo acima (**`listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601 --tcp`**): é exatamente assim que você faz **Double / Triple / Multi-Hop Pivoting no Ligolo-ng**! O `Agent 1` na DMZ abre a porta `11601` apontando para o `127.0.0.1:11601` do seu `proxy`; quando você executa `./agent -connect <IP_INTERNO_DO_AGENT_1>:11601` lá no `Host 2` da rede interna profunda, o **`Agent 2` aparece diretamente no comando `session` do seu `proxy`** como uma nova sessão independente!

## Como verificar
Aí basta criar uma segunda interface TUN (`interface_create --name tun-interna2`), adicionar a rota da terceira rede (`10.99.0.0/24 dev tun-interna2`) e rodar `tunnel_start --tun tun-interna2` na sessão do `Agent 2` — você passa a rotear pacotes IP diretamente para duas redes isoladas simultaneamente sem nenhum `proxychains`!

## Conexões
- [[ligolo-acesso-ip-local-agente-magic-cidr-240-0-0-1-loopback]] — Veja também: Acessando Serviços em **`127.0.0.1` (`localhost`)** da Própria Máquina do Agente via Ligolo-ng: O Endereço Mágico **`240.0.0.1`**.
- [[ligolo-boas-praticas-nmap-unprivileged-pe-traducao-syn-connect-gvisor]] — Veja também: Por Que Usar **`nmap --unprivileged`** (ou `-sT -Pn`) Através do Ligolo-ng? Entendendo a Tradução de Pacotes `SYN` e `ICMP` no `gVisor` do Agente.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Referência cruzada direta com ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun.
- [[chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap]] — Referência cruzada direta com chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
