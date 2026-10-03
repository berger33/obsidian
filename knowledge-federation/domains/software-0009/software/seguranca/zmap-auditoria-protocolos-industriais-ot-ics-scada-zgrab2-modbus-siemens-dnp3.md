---
id: software.seguranca.tranche08.000798
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

# ZGrab 2.0 em Auditoria de Redes **OT / ICS / SCADA** e Bancos de Dados: Módulos `modbus`, `siemens` (S7), `dnp3`, `bacnet`, `fox` e `mongodb`/`redis`

## Em uma frase
Um dos recursos mais valiosos do **ZGrab 2.0** para equipes de segurança industrial (OT/ICS) e auditoria de exposição de infraestrutura é que ele inclui módulos de protocolo nativos e seguros (somente-leitura de identificação) para **Controladores Lógicos Programáveis (CLPs / PLCs) e Automação Predial**: **`modbus`** (porta `502`), **`siemens`** (protocolo S7comm na porta `102`), **`dnp3`** (subestações elétricas, porta `20000`), **`bacnet`** (automação predial HVAC, porta `47808`) e **`fox`** (Tridium Niagara, porta `1911`), além de **`jarm`** (fingerprinting ativo de servidores TLS C2)!

## Por que importa
Em vez de enviar probes genéricos agressivos (como `nmap -sV --version-all`) que podem travar a pilha TCP de um CLP industrial antigo, os módulos OT do ZGrab 2.0 enviam uma única requisição oficial de identificação de dispositivo (como *Read Device Identification — Function Code 43 / MEI 14* no Modbus) para inventariar fabricante, modelo e firmware com segurança.

## Como funciona
Da mesma forma, os módulos `redis`, `memcached`, `mongodb`, `postgres`, `mysql` e `mssql` identificam bancos de dados expostos sem autenticação.

## Exemplo
```bash
# Auditar o fingerprint TLS JARM (para deteccao de servidores C2) ou identificar bancos Redis expostos com ZGrab 2.0
echo "10.20.30.40" | zgrab2 jarm --port 443
echo "10.20.30.50" | zgrab2 redis --port 6379
```

## Limites e trade-offs
Em redes industriais OT/ICS reais, **nunca** execute varreduras de alta velocidade com ZMap/Masscan: alimente o `zgrab2 modbus` / `zgrab2 siemens` apenas com a lista conhecida de IPs e limite `--senders=5` para não sobrecarregar switches industriais de 10/100 Mbps.

## Como verificar
Analise o hash **JARM** de 62 caracteres retornado pelo módulo `zgrab2 jarm` comparando-o contra listas de hashes JARM conhecidos de frameworks de Command & Control (Cobalt Strike, Sliver, Mythic, Metasploit).

## Conexões
- [[zmap-zgrab2-configuracao-multiplos-modulos-multiple-ini-triggers]] — Veja também: **ZGrab 2.0 (`zgrab2 multiple -c config.ini`)**: Orquestração de Múltiplos Protocolos L7, Formato CSV (`IP, DOMAIN, TAG, PORT`) e **`--trigger`**.
- [[zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards]] — Veja também: ZMap: Boas Práticas de **Varredura Ética (*Ethical Scanning*)**, Reprodutibilidade Científica (**`--seed`**), Distribuição (**`--shards`**) e Metadados (`--notes`).
- [[zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes]] — Referência cruzada direta com zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
