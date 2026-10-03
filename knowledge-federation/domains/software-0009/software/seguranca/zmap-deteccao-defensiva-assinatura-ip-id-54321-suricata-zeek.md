---
id: software.seguranca.tranche08.000800
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
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Engenharia de Detecção (Blue Team): Identificação da Assinatura Clássica do **ZMap (`IP ID = 54321` / `0xd431`)** no **Suricata**, **Zeek** e **`tcpdump`**

## Em uma frase
Para otimizar ao máximo a construção de pacotes em memória e validar respostas *stateless*, a implementação padrão do ZMap preenche um valor constante famoso no cabeçalho IPv4 de todos os pacotes gerados: o campo de 16 bits **IP Identification (`ip.id`) é fixado por padrão no número decimal `54321` (`0xd431` em hexadecimal)**!

## Por que importa
Isso significa que qualquer analista de SOC ou engenheiro de detecção pode identificar instantaneamente pacotes de sondagem enviados por instalações padrão do ZMap na borda da rede usando um filtro BPF de uma linha no **`tcpdump`** (`ip[4:2] == 54321`), no **Wireshark** (`ip.id == 54321 and tcp.flags.syn == 1 and tcp.flags.ack == 0`) ou uma regra no **Suricata**!

## Como funciona
Combinar a detecção da assinatura estática (`ip.id == 54321`) com a detecção comportamental de varredura horizontal no **Zeek (`Scan::addr_scan`)** e listas de inteligência de IPs de scanners no **CrowdSec / Firewalls de Borda** garante visibilidade completa sobre reconhecimentos em escala de internet.

## Exemplo
```bash
# Capturar em tempo real no tcpdump pacotes TCP SYN de varredura ZMap identificando a assinatura padrao IP ID = 54321 (0xd431)
sudo tcpdump -ni eth0 'ip[4:2] == 54321 and (tcp[tcpflags] & (tcp-syn|tcp-ack)) == tcp-syn' -c 20
```

## Limites e trade-offs
Mesmo que um operador modifique o código-fonte do ZMap para randomizar o campo `ip.id`, o padrão comportamental de um **único pacote `SYN` sem retransmissão** (quando a porta está filtrada, uma pilha TCP real do Linux/Windows tenta retransmitir o `SYN` após 1s, 3s, 7s; já um scanner *stateless* como ZMap ou Masscan com `-P 1` envia apenas 1 `SYN` e nunca retransmite!) continua identificando a ferramenta no Zeek!

## Como verificar
Adicione no SIEM uma correlação para IPs externos que enviam pacotes `SYN` com `ip.id == 54321` e verifique se pertencem a projetos legítimos de pesquisa (Censys, Shadowserver, Rapid7 Sonar) ou a varreduras hostis.

## Conexões
- [[zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards]] — Veja também: ZMap: Boas Práticas de **Varredura Ética (*Ethical Scanning*)**, Reprodutibilidade Científica (**`--seed`**), Distribuição (**`--shards`**) e Metadados (`--notes`).
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
