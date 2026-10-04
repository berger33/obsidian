---
id: software.seguranca.tranche08.000778
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
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura de Varredura em **Dois Estágios**: Descoberta Rápida de Portas (`0-65535`) com **Masscan** + Fingerprinting Profundo (`-sV -sC`) com **Nmap**

## Em uma frase
Varrer todas as **65.535 portas TCP (`-p1-65535` / `-p0-65535`)** de uma sub-rede `/16` diretamente com o Nmap tradicional pode levar dias porque o Nmap controla janela de congestionamento e retransmissões por host; por outro lado, o Masscan varre todas as 65.535 portas muito rápido, mas não executa a biblioteca de 600+ scripts NSE nem o banco completo de 10.000 assinaturas `nmap-service-probes`.

## Por que importa
Por isso, o padrão clássico de engenharia de reconhecimento de rede combina as duas ferramentas em um **Pipeline de Dois Estágios**: **(Estágio 1 — Descoberta L4 Ampla)** o **Masscan** varre todas as portas (`-p1-65535`) em alta velocidade e grava o JSON/Grepable apenas dos pares `(IP, porta)` que responderam `open`; e **(Estágio 2 — Inspeção L7 Cirúrgica)** o **Nmap (`-sV -sC`)** é invocado **exclusivamente sobre os IPs e portas abertas já confirmados pelo Masscan**!

## Como funciona
Dessa forma, o Nmap não perde 1 segundo sequer sondando as 65.530 portas fechadas de cada host, reduzindo uma auditoria completa de portas altas de 48 horas para poucos minutos!

## Exemplo
```bash
# Estagio 1: Descobrir portas abertas com Masscan (-oJ) -> Estagio 2: Passar apenas os IPs e portas abertas para o Nmap (-sV -sC)
sudo masscan 10.30.10.0/24 -p1-65535 --rate 5000 -oJ /cases/easm/stage1_open.json

PORTS=$(jq -r '.[].ports[].port' /cases/easm/stage1_open.json | sort -nu | paste -sd, -)
jq -r '.[].ip' /cases/easm/stage1_open.json | sort -u > /cases/easm/stage1_hosts.txt

if [ -n "$PORTS" ]; then
  sudo nmap -sS -sV -sC -Pn -n -p "$PORTS" -iL /cases/easm/stage1_hosts.txt -oA /cases/easm/stage2_nmap_detailed
fi
```

## Limites e trade-offs
Observe no comando do Nmap no Estágio 2 o uso de **`-Pn -n -p "$PORTS" -iL stage1_hosts.txt`**: como o Masscan já provou que aqueles IPs estão vivos e com aquelas portas abertas, `-Pn` evita refazer ping discovery e `-n` evita atrasos de DNS reverso quando não necessário.

## Como verificar
Compare o XML final `stage2_nmap_detailed.xml` com a política de firewall da sub-rede para identificar serviços rodando em portas altas não-padrão (ex.: SSH na `22222`, Redis na `16379`).

## Conexões
- [[masscan-customizacao-http-sni-vhost-payloads-heartbleed-poodle]] — Veja também: Masscan: Customização de Requisições HTTP (`--http-user-agent`, `--http-header`, `--http-method`), Captura de **Certificados TLS X.509** e Checagens **SMB / VULN**.
- [[masscan-ajustes-rede-arp-router-mac-adapter-vlan-bpf-pcap]] — Veja também: Masscan: Ajustes de Camada de Enlace (**`--interface`**, **`--adapter-ip`**, **`--adapter-mac`**, **`--router-mac`**), Tags **802.1Q VLAN** e Diagnóstico `--packet-trace`.
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[masscan-formatos-saida-binaria-ob-readscan-conversao-ox-oj-ol-og]] — Referência cruzada direta com masscan-formatos-saida-binaria-ob-readscan-conversao-ox-oj-ol-og.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
