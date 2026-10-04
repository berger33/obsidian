---
id: software.seguranca.tranche14.001354
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/arkime/arkime/main/README.md", "https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Caça a Ameaças (**Threat Hunting**) no Arkime: Linguagem de Expressões de Busca, **Sessions**, **SPI View**, **SPI Graph** e **Connections Graph**

## Em uma frase
Como um analista de **DFIR / Threat Hunting** usa a linguagem de busca do Arkime para encontrar em segundos um ataque dentro de bilhões de pacotes capturados?

## Por que importa
Na barra de busca superior do Arkime, você consulta centenas de campos **SPI (*Session Profile Information*)** extraídos pelos *parsers* de protocolo usando operadores lógicos (`&&`, `||`, `!`), comparações (`==`, `!=`, `<`, `>`), curingas (`*`), listas (`[...]`) e expressões regulares (`/regex/`): por exemplo, **`ip.src == 10.1.2.15 && port.dst == 443 && tls.ja3 == "e7d705a3286e19ea42f587b344ee6865"`**, ou **`http.uri == "/api/*" && http.statuscode == 200 && http.method == "POST"`**, ou **`dns.host == *.onion || cert.issuer.cn != "Corporativa*"`**!

## Como funciona
Além da aba **Sessions** (que expande a conversa TCP/UDP reassemblada e decodificada em ASCII/Hex/UTF-8 ou reconstrói imagens e arquivos transferidos via **CyberChef** integrado!), o Arkime oferece três visões analíticas matadoras: **(1) `SPI View`** (lista todos os valores únicos e contagens de qualquer campo SPI na janela de tempo — excelente para encontrar *Outliers* raros!); **(2) `SPI Graph`** (histogramas temporais por valor de campo); e **(3) `Connections`** (grafo visual interativo de nós e arestas entre IPs, ASN, países ou domínios)!

## Exemplo
```text
# Exemplos de expressoes de Threat Hunting na barra de busca do Arkime (JA3/TLS, HTTP POST suspeito sem User-Agent padrao e DNS TXT longo)
protocols == tls && cert.subject.cn == cert.issuer.cn && ip.dst != [10.0.0.0/8, 192.168.0.0/16]
http.method == "POST" && http.useragent != ["Mozilla*", "curl*"] && databytes.src > 1048576
protocols == dns && dns.qtype == "TXT" && bytes.dst > 500
```

## Limites e trade-offs
Veja a primeira expressão de *Threat Hunting* acima (**`protocols == tls && cert.subject.cn == cert.issuer.cn && ip.dst != [10.0.0.0/8, 192.168.0.0/16]`**): ela encontra instantaneamente todas as conexões TLS de saída para a Internet onde o certificado do servidor remoto é **autoassinado (`cert.subject.cn == cert.issuer.cn`)** — um indicador clássico de servidores de Comando e Controle (C2) padrão de Cobalt Strike, Sliver, Metasploit e Mythic!

## Como verificar
Ao expandir qualquer sessão na tela **Sessions**, você pode clicar no botão **"CyberChef"** ao lado dos bytes de origem ou destino para abrir o payload daquela conversa diretamente dentro do CyberChef embutido no Arkime e aplicar receitas de desofuscação (`From Base64`, `Gunzip`, `XOR`) com um clique!

## Conexões
- [[arkime-otimizacao-captura-alta-velocidade-tpacketv3-snf-dpdk-threads]] — Veja também: Captura Sem Perda de Pacotes em Links de **10 Gbps a 100 Gbps** no Arkime: `packetThreads`, **`tpacketv3` (`AF_PACKET`)**, **`pcapWriteMethod=simple-nodirect`** e **Criptografia de PCAP em Repouso**.
- [[arkime-enriquecimento-wiseservice-threat-intel-regras-yara-tagger]] — Veja também: Enriquecimento em Tempo Real com **`wiseService` (*With Intelligence See Everything*)**, **YARA** em Fluxo (`yara.ini`) e **`arkime.rules`**.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.

## Fontes
- [Arkime Official GitHub Repository (`arkime/arkime`)](https://raw.githubusercontent.com/arkime/arkime/main/README.md) — repositório oficial do sistema de Full Packet Capture Arkime cobrindo arquitetura distribuída `capture` (C), `viewer` (Node.js), OpenSearch/Elasticsearch, `wiseService`, `Parliament` e `Cont3xt`; consultado em 2026-10-03.
- [Arkime Official Sample Configuration (`release/config.ini.sample`)](https://raw.githubusercontent.com/arkime/arkime/main/release/config.ini.sample) — referência oficial do `/opt/arkime/etc/config.ini` cobrindo herança em camadas, `pcapDir`, `freeSpaceG`, `pcapReadMethod=tpacketv3`, criptografia AES-256-CTR em repouso, `passwordSecret`, `serverSecret` e `authMode=header-jwt`; consultado em 2026-10-03.
